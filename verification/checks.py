#!/usr/bin/env python3
"""Finite numerical diagnostics for normalized matrix-exponential updates.

These checks illustrate selected finite cases. The dimension-uniform lower
bound and the cumulant bound require the analytical proofs in science/.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import numpy as np
import scipy
from numpy.polynomial.legendre import leggauss
from scipy.linalg import expm


A = 0.8
H = 0.1
EPSILON = 0.001  # Half trace distance.
SEED = 2026111507
TOLERANCE = 2e-10


def density_exp(hermitian: np.ndarray) -> np.ndarray:
    """Normalize exp(H) using a stable Hermitian eigendecomposition."""
    values, vectors = np.linalg.eigh(hermitian)
    weights = np.exp(values - values.max())
    return (vectors * (weights / weights.sum())) @ vectors.conj().T


def matrix_log(positive: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(positive)
    assert values.min() > 0
    return (vectors * np.log(values)) @ vectors.conj().T


def trace_distance(left: np.ndarray, right: np.ndarray) -> float:
    return float(np.abs(np.linalg.eigvalsh(left - right)).sum() / 2)


def mean_z(state: np.ndarray, z: np.ndarray) -> float:
    return float(np.trace(z @ state).real)


def local_z(dimension: int) -> np.ndarray:
    """First-qubit Z for the power-of-two dimensions checked here."""
    assert dimension >= 2 and dimension & (dimension - 1) == 0
    return np.kron(np.diag([1.0, -1.0]), np.eye(dimension // 2))


def haar_unitary(rng: np.random.Generator, dimension: int) -> np.ndarray:
    gaussian = rng.standard_normal((dimension, dimension))
    gaussian = gaussian + 1j * rng.standard_normal((dimension, dimension))
    q, r = np.linalg.qr(gaussian)
    diagonal = np.diag(r)
    return q @ np.diag(diagonal / np.abs(diagonal))


def logmean_susceptibility(rho: np.ndarray, z: np.ndarray) -> float:
    """Independent evaluation in rho's eigenbasis using logarithmic means."""
    values, vectors = np.linalg.eigh(rho)
    w = vectors.conj().T @ z @ vectors
    x, y = np.broadcast_arrays(values[:, None], values[None, :])
    means = np.empty_like(x)
    equal = np.isclose(x, y, rtol=1e-12, atol=0)
    means[equal] = (x[equal] + y[equal]) / 2
    means[~equal] = ((x[~equal] - y[~equal])
                     / (np.log(x[~equal]) - np.log(y[~equal])))
    return float(np.sum(means * np.abs(w)**2) - mean_z(rho, z)**2)


def sandwich(rho: np.ndarray, z: np.ndarray, h: float) -> np.ndarray:
    k = expm(h * z / 2)
    out = k @ rho @ k
    return out / np.trace(out)


def constants() -> dict:
    c = 0.5 + A / math.log((1 + A) / (1 - A))
    gap = (1 - c) * H - (14 / 3) * H**3
    effective_gap = gap - 4 * EPSILON
    prefactor = math.sqrt(math.log1p(effective_gap**2)) / A**2
    five_copy_failure = (-math.expm1(-2 * H))**5
    conservative_orientation_coefficient = 0.001
    conservative_input_distance_bound = (5*A*A*conservative_orientation_coefficient
                                          / math.sqrt(2))
    exact_input_distance_bound = (0.5*math.sqrt(math.expm1(
        (A*A*conservative_orientation_coefficient)**2)) + math.sqrt(math.expm1(
        (2*A*A*conservative_orientation_coefficient)**2)))
    assert gap > 4 * EPSILON
    assert prefactor > 0.00769
    assert five_copy_failure < EPSILON
    assert 2*A*A*conservative_orientation_coefficient < 1
    assert exact_input_distance_bound < conservative_input_distance_bound < effective_gap/2
    # Check the arithmetic of the inherited testing-to-update transfer.
    inverse_rhs = math.sqrt(math.expm1((prefactor * A**2)**2))
    assert abs(inverse_rhs - effective_gap) < 1e-14
    return {
        "a": A, "h": H, "output_half_trace_error": EPSILON,
        "input_spectral_condition_number": (1 + A) / (1 - A),
        "c_a": c, "dimension_uniform_response_upper_bound": c*H + 13*H**3/3,
        "maximally_mixed_response": math.tanh(H),
        "analytical_response_gap_lower_bound": gap,
        "response_gap_after_output_error_allowance": effective_gap,
        "main_same_spectrum_copy_lower_bound": {
            "scope": "D is a positive multiple of four; both ensembles have the supplied exact two-level spectrum.",
            "conservative_coefficient_strict_lower_bound": conservative_orientation_coefficient,
            "input_distance_exact_upper_bound_at_coefficient": exact_input_distance_bound,
            "input_distance_relaxed_upper_bound_at_coefficient": conservative_input_distance_bound,
            "output_distance_lower_bound_after_error": effective_gap/2,
            "inherited_comparison_bound": "B_D(n)+2 B_(D/2)(n), B_d(n)=sqrt(expm1((n*a^2/d)^2))/2",
        },
        "maxmix_comparator_copy_lower_bound_coefficient": prefactor,
        "maxmix_comparator_conservative_display_coefficient": 0.00769,
        "commuting_single_attempt_success_lower_bound": math.exp(-2*H),
        "commuting_five_attempt_failure_upper_bound": five_copy_failure,
    }


def qubit_integration(order: int) -> dict:
    """Uniform Bloch-axis integral: x=cos(theta) is uniform on [-1,1]."""
    nodes, weights = leggauss(order)
    z = local_z(2)
    s = np.arctanh(A)
    responses, cheap_responses, chis = [], [], []
    diag_moments, offdiag_moments, initial_mean_squares = [], [], []
    for x in nodes:
        involution = np.array([[x, math.sqrt(1-x*x)],
                               [math.sqrt(1-x*x), -x]])
        rho = (np.eye(2) + A*involution) / 2
        target = density_exp(matrix_log(rho) + H*z)
        radius = math.sqrt(s*s + H*H + 2*s*H*x)
        closed_response = (s*x + H) * math.tanh(radius) / radius
        assert abs(mean_z(target, z) - closed_response) < TOLERANCE
        responses.append(mean_z(target, z))
        cheap_responses.append(mean_z(sandwich(rho, z, H), z))
        chis.append(logmean_susceptibility(rho, z))
        _, eigenvectors = np.linalg.eigh(rho)
        w = eigenvectors.conj().T @ z @ eigenvectors
        diag_moments.append(np.mean(np.abs(np.diag(w))**2))
        offdiag_moments.append(abs(w[0, 1])**2)
        initial_mean_squares.append(mean_z(rho, z)**2)
    integrate = lambda values: float(np.dot(weights, values) / 2)
    c = constants()["c_a"]
    expected_chi = (4*c - 1 - A*A) / 3
    moments = {
        "diagonal_second_moment": integrate(diag_moments),
        "offdiagonal_second_moment": integrate(offdiag_moments),
        "initial_magnetization_second_moment": integrate(initial_mean_squares),
    }
    expected_moments = [1/3, 2/3, A*A/3]
    assert max(abs(x-y) for x, y in zip(moments.values(), expected_moments)) < 2e-12
    assert abs(integrate(chis) - expected_chi) < 2e-12
    return {
        "dimension": 2, "method": "Gauss-Legendre integration of uniform Bloch axis",
        "quadrature_order": order, "mean_esscher_response": integrate(responses),
        "mean_sandwich_response": integrate(cheap_responses),
        "mean_susceptibility": integrate(chis),
        "exact_haar_susceptibility": expected_chi,
        "haar_second_moments": moments,
        "exact_haar_second_moments": dict(zip(moments.keys(), expected_moments)),
        "sampling_standard_error": None,
    }


def sample_summary(values: list[float]) -> dict:
    array = np.asarray(values)
    return {"mean": float(array.mean()),
            "standard_error": float(array.std(ddof=1)/math.sqrt(len(array)))}


def haar_diagnostic(rng: np.random.Generator, dimension: int, pairs: int) -> dict:
    z = local_z(dimension)
    j = np.kron(np.array([[0., 1.], [1., 0.]]), np.eye(dimension//2))
    assert np.allclose(j @ z @ j, -z)
    s = np.arctanh(A)
    responses, cheap_responses, chis = [], [], []
    diagonals, offdiagonals, m0squared = [], [], []
    maximum_log_residual = maximum_state_difference = maximum_m0_pair = 0.
    minimum_eigenvalue = 1.
    maximum_condition_number = 0.
    for index in range(pairs):
        u = haar_unitary(rng, dimension)
        involution = u @ z @ u.conj().T
        partner = j @ involution @ j
        rho = (np.eye(dimension) + A*involution) / dimension
        partner_rho = (np.eye(dimension) + A*partner) / dimension
        positive = density_exp(s*involution + H*z)
        negative = density_exp(s*involution - H*z)
        # J conjugation flips the tilt and the measured observable exactly.
        paired = (mean_z(positive, z) - mean_z(negative, z)) / 2
        responses.append(paired)
        cheap_responses.append((mean_z(sandwich(rho, z, H), z)
                                 + mean_z(sandwich(partner_rho, z, H), z))/2)
        chis.append(logmean_susceptibility(rho, z))
        w = u.conj().T @ z @ u
        abs_w_squared = np.abs(w)**2
        diagonals.append(float(np.diag(abs_w_squared).mean()))
        offdiagonals.append(float((abs_w_squared.sum()-np.trace(abs_w_squared))
                                  / (dimension*(dimension-1))))
        m0squared.append(mean_z(rho, z)**2)
        maximum_m0_pair = max(maximum_m0_pair,
                             abs(mean_z(rho, z)+mean_z(partner_rho, z)))
        eigenvalues = np.linalg.eigvalsh(rho)
        minimum_eigenvalue = min(minimum_eigenvalue, float(eigenvalues.min()))
        maximum_condition_number = max(maximum_condition_number,
                                      float(eigenvalues.max()/eigenvalues.min()))
        if index < 12:
            actual_log = matrix_log(rho)
            shifted_log = (math.log(math.sqrt(1-A*A)/dimension)*np.eye(dimension)
                           + s*involution)
            maximum_log_residual = max(maximum_log_residual,
                                      float(np.linalg.norm(actual_log-shifted_log, 2)))
            target_from_log = density_exp(actual_log + H*z)
            maximum_state_difference = max(maximum_state_difference,
                                           trace_distance(target_from_log, positive))
            direct_exp = expm(actual_log + H*z)
            direct_exp /= np.trace(direct_exp)
            assert trace_distance(direct_exp, positive) < TOLERANCE
            assert trace_distance(density_exp(s*partner+H*z),
                                  j @ negative @ j) < TOLERANCE
    assert maximum_m0_pair < TOLERANCE
    assert maximum_log_residual < TOLERANCE
    assert maximum_state_difference < TOLERANCE
    assert minimum_eigenvalue > 0
    assert maximum_condition_number < 9 + TOLERANCE
    c = constants()["c_a"]
    predicted = (dimension**2*c - 1 - A*A)/(dimension**2-1)
    summaries = {
        "esscher_response": sample_summary(responses),
        "sandwich_response": sample_summary(cheap_responses),
        "susceptibility": sample_summary(chis),
        "diagonal_second_moment": sample_summary(diagonals),
        "offdiagonal_second_moment": sample_summary(offdiagonals),
        "initial_magnetization_second_moment": sample_summary(m0squared),
    }
    expected = {
        "susceptibility": predicted,
        "diagonal_second_moment": 1/(dimension+1),
        "offdiagonal_second_moment": dimension/(dimension**2-1),
        "initial_magnetization_second_moment": A*A/(dimension**2-1),
    }
    zscores = {key: ((summaries[key]["mean"]-value)
                    / summaries[key]["standard_error"])
               for key, value in expected.items()}
    # This is a diagnostic of this seeded finite run, not a theorem certificate.
    assert max(abs(value) for value in zscores.values()) < 6
    return {
        "dimension": dimension, "independent_haar_draws": pairs,
        "antithetic_orientations_evaluated": 2*pairs,
        "method": "Seeded complex-Gaussian QR; J-conjugate antithetic response",
        "summary": summaries, "exact_haar_predictions": expected,
        "diagnostic_standardized_residuals": zscores,
        "maximum_initial_pair_magnetization": maximum_m0_pair,
        "maximum_logrho_scalar_cancellation_residual": maximum_log_residual,
        "maximum_half_trace_difference_log_vs_shifted_exponent": maximum_state_difference,
        "smallest_checked_input_eigenvalue": minimum_eigenvalue,
        "maximum_checked_input_condition_number": maximum_condition_number,
        "tilt_is_first_qubit_z": True,
    }


def derivative_ratios(a_matrix: np.ndarray, z: np.ndarray) -> list[float]:
    """Duhamel derivatives from one upper-triangular block exponential."""
    dimension = len(z)
    block = np.kron(np.eye(5), a_matrix).astype(complex)
    for k in range(4):
        block[k*dimension:(k+1)*dimension,
              (k+1)*dimension:(k+2)*dimension] = z
    evolution = expm(block)
    f = np.trace(evolution[:dimension, :dimension]).real
    ratios = []
    for k in range(1, 5):
        derivative = math.factorial(k)*np.trace(
            evolution[:dimension, k*dimension:(k+1)*dimension]).real
        ratios.append(float(derivative/f))
    return ratios


def cumulant_diagnostics(rng: np.random.Generator) -> dict:
    rows = []
    for dimension in (2, 4, 8):
        z = local_z(dimension)
        u = haar_unitary(rng, dimension)
        s_matrix = u @ z @ u.conj().T
        for t in (-0.3, 0., H, 0.7):
            r1, r2, r3, r4 = derivative_ratios(np.arctanh(A)*s_matrix+t*z, z)
            fourth = r4-4*r3*r1-3*r2*r2+12*r2*r1*r1-6*r1**4
            assert max(abs(r1), abs(r2), abs(r3), abs(r4)) < 1+1e-9
            assert abs(fourth) < 26+1e-9
            rows.append({"dimension": dimension, "t": t,
                         "duhamel_derivative_ratios": [r1, r2, r3, r4],
                         "fourth_log_partition_derivative": fourth})
    z = local_z(2)
    t = 0.37
    commuting_ratios = derivative_ratios(t*z, z)
    exact_ratios = [math.tanh(t), 1., math.tanh(t), 1.]
    assert np.max(np.abs(np.asarray(commuting_ratios)-exact_ratios)) < TOLERANCE
    return {
        "method": "5-by-5 block Duhamel exponential; derivatives through order four",
        "analytical_bound": 26,
        "scope": "Twelve finite examples check the implementation, not universal validity.",
        "commuting_closed_form_maximum_error": float(np.max(np.abs(
            np.asarray(commuting_ratios)-exact_ratios))),
        "maximum_observed_absolute_fourth_cumulant": max(abs(
            row["fourth_log_partition_derivative"]) for row in rows),
        "cases": rows,
    }


def known_spectrum_controls(rng: np.random.Generator) -> list[dict]:
    """A distinct commuting ensemble with the exact same supplied spectrum."""
    rows = []
    for dimension in (4, 8, 16, 32):
        half = dimension//2
        z = local_z(dimension)
        balanced = local_z(half)
        errors, initial_means, responses, spectrum_errors = [], [], [], []
        for _ in range(32):
            plus, minus = haar_unitary(rng, half), haar_unitary(rng, half)
            s_matrix = np.zeros((dimension, dimension), dtype=complex)
            s_matrix[:half, :half] = plus @ balanced @ plus.conj().T
            s_matrix[half:, half:] = minus @ balanced @ minus.conj().T
            rho = (np.eye(dimension)+A*s_matrix)/dimension
            target = density_exp(matrix_log(rho)+H*z)
            cheap = sandwich(rho, z, H)
            errors.append(trace_distance(target, cheap))
            initial_means.append(mean_z(rho, z))
            responses.append(mean_z(target, z))
            expected_spectrum = np.r_[np.full(half, (1-A)/dimension),
                                      np.full(half, (1+A)/dimension)]
            spectrum_errors.append(float(np.max(np.abs(
                np.linalg.eigvalsh(rho)-expected_spectrum))))
            assert np.linalg.norm(s_matrix @ z-z @ s_matrix) < TOLERANCE
        assert max(errors) < TOLERANCE
        assert max(abs(x) for x in initial_means) < TOLERANCE
        assert max(abs(x-math.tanh(H)) for x in responses) < TOLERANCE
        assert max(spectrum_errors) < TOLERANCE
        rows.append({
            "dimension": dimension, "independent_block_haar_draws": 32,
            "ensemble": "Independent balanced Haar involutions within the two known Z blocks",
            "spectrum": {"lower_eigenvalue": (1-A)/dimension,
                         "upper_eigenvalue": (1+A)/dimension,
                         "multiplicity_each": half},
            "mean_response": float(np.mean(responses)),
            "exact_response": math.tanh(H),
            "maximum_absolute_initial_magnetization": max(abs(x) for x in initial_means),
            "maximum_response_error": max(abs(x-math.tanh(H)) for x in responses),
            "maximum_spectrum_error": max(spectrum_errors),
            "maximum_esscher_sandwich_half_trace_difference": max(errors),
        })
    return rows


def filter_controls() -> tuple[dict, list[dict]]:
    z = local_z(2)
    curves = []
    for x in np.linspace(-1, 1, 121):
        involution = np.array([[x, math.sqrt(max(0., 1-x*x))],
                               [math.sqrt(max(0., 1-x*x)), -x]])
        rho = (np.eye(2)+A*involution)/2
        target = density_exp(matrix_log(rho)+H*z)
        cheap = sandwich(rho, z, H)
        curves.append({"alignment": float(x),
                       "half_trace_distance": trace_distance(target, cheap),
                       "esscher_magnetization": mean_z(target, z),
                       "sandwich_magnetization": mean_z(cheap, z)})
    assert curves[0]["half_trace_distance"] < TOLERANCE
    assert curves[-1]["half_trace_distance"] < TOLERANCE
    counterexample = curves[len(curves)//2]
    assert counterexample["half_trace_distance"] > 10*EPSILON
    k = expm(H*(z-np.eye(2))/2)
    k2values = np.linalg.eigvalsh(k.conj().T @ k)
    assert abs(k2values.min()-math.exp(-2*H)) < TOLERANCE
    assert abs(k2values.max()-1) < TOLERANCE
    return ({
        "commuting_endpoint_maximum_half_trace_error": max(
            curves[0]["half_trace_distance"], curves[-1]["half_trace_distance"]),
        "noncommuting_sigma_x_counterexample": counterexample,
        "success_operator_squared_eigenvalues": k2values.tolist(),
        "interpretation": "A bounded filter implements the sandwich update; it equals "
                          "the Esscher target on commuting inputs but fails at the "
                          "stated error on this noncommuting qubit input.",
    }, curves)


def figure(report: dict, destination: Path) -> None:
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(10.3, 4.2), layout="constrained")
    dimensions = [row["dimension"] for row in report["haar_diagnostics"]]
    responses = [
        row["summary"]["esscher_response"]["mean"] for row in report["haar_diagnostics"]]
    errors = [2*row["summary"]["esscher_response"]["standard_error"]
                    for row in report["haar_diagnostics"]]
    cheap = [
        row["summary"]["sandwich_response"]["mean"] for row in report["haar_diagnostics"]]
    axes[0].errorbar(dimensions, responses, yerr=errors, fmt="o-", color="#00796B",
                     capsize=3, label="Full-Haar Esscher mean (±2 SE)")
    axes[0].plot(dimensions, cheap, "s--", color="#9B4D27", label="Full-Haar sandwich mean")
    axes[0].axhline(report["constants"]["dimension_uniform_response_upper_bound"],
                    color="#00796B", ls=":", label="Analytical Esscher upper bound")
    axes[0].plot(dimensions, [row["mean_response"] for row in report["known_spectrum_commuting_controls"]],
                 "^:", color="#555555", label="Same-spectrum commuting mean")
    axes[0].set(xscale="log", xlabel="Input dimension D", ylabel="Mean output magnetization",
                title="A  Same supplied spectrum; a=0.8, h=0.1")
    axes[0].set_xticks(dimensions, [str(d) for d in dimensions])
    axes[0].xaxis.set_minor_formatter(NullFormatter())
    axes[0].legend(loc="lower right", fontsize=8)
    curve = report["filter_counterexample_curve"]
    axes[1].plot([x["alignment"] for x in curve],
                 [x["half_trace_distance"] for x in curve], color="#9B4D27", lw=2)
    axes[1].axhline(EPSILON, color="#555555", ls=":", label="Required error 0.001")
    axes[1].set(xlabel="Bloch-axis alignment with the tilt",
                ylabel="Half trace distance: Esscher vs sandwich",
                title="B  Sandwich error on one qubit")
    axes[1].legend(loc="upper right", fontsize=8)
    fig.savefig(destination.with_suffix(".png"), dpi=190)
    fig.savefig(destination.with_suffix(".pdf"))
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    args = parser.parse_args()
    script = Path(__file__).resolve()
    rng = np.random.default_rng(SEED)
    low, high = qubit_integration(96), qubit_integration(192)
    quadrature_difference = abs(low["mean_esscher_response"]-high["mean_esscher_response"])
    assert quadrature_difference < 2e-12
    controls, curve = filter_controls()
    report = {
        "scope": "Finite numerical diagnostics; analytical proofs supply universal claims. "
                 "Monte Carlo standard errors use independent antithetic pairs as sampling units.",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "seed": SEED,
        "environment": {"python": sys.version, "platform": platform.platform(),
                        "numpy": np.__version__, "scipy": scipy.__version__,
                        "matplotlib": matplotlib.__version__},
        "provenance": {"script": "verification/checks.py",
                       "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
                       "requirements_sha256": hashlib.sha256(
                           script.with_name("requirements.txt").read_bytes()).hexdigest()},
        "constants": constants(),
        "qubit_quadrature": {"coarse": low, "refined": high,
                             "response_refinement_difference": quadrature_difference,
                             "caveat": "Refinement agreement is a numerical check, not a certified integration bound."},
        "haar_diagnostics": [haar_diagnostic(rng, d, pairs) for d, pairs in
                             [(4, 2400), (8, 1600), (16, 900), (32, 400)]],
        "known_spectrum_commuting_controls": known_spectrum_controls(rng),
        "cumulant_diagnostics": cumulant_diagnostics(rng),
        "filter_controls": controls,
        "filter_counterexample_curve": curve,
        "assertion_status": "passed",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    figure(report, args.output.parent / "finite_diagnostics")
    args.output.write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    print(json.dumps({"status": "passed", "output": str(args.output),
                      "main_same_spectrum_conservative_coefficient": report["constants"][
                          "main_same_spectrum_copy_lower_bound"]["conservative_coefficient_strict_lower_bound"],
                      "maxmix_comparator_coefficient": report["constants"][
                          "maxmix_comparator_copy_lower_bound_coefficient"],
                      "noncommuting_filter_half_trace_error": controls[
                          "noncommuting_sigma_x_counterexample"]["half_trace_distance"],
                      "quadrature_refinement_difference": quadrature_difference,
                      "independent_haar_draws": sum(row["independent_haar_draws"]
                                                    for row in report["haar_diagnostics"])}, indent=2))


if __name__ == "__main__":
    main()
