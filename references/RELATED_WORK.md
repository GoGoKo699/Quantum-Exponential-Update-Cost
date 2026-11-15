# Related work and attribution

[Return to the project](../README.md) · [BibTeX](references.bib)

The operation studied here is the normalized exponential update

```math
\mathcal E_H(\rho)=\frac{\exp(\log\rho+H)}{\mathrm{Tr}\exp(\log\rho+H)}.
```

The question is how many independent copies of a prior state are required to produce one updated state when its exact two-level spectrum is supplied and its orientation is unknown. An input preparation unitary, its inverse, a purification, and a block encoding are stronger access resources; they are not supplied by this copy model.

## The quantum Esscher transform

Qiu, Koor and Rebentrost [QKR25] define and implement the quantum Esscher transform. Their Theorem 5 constructs a subnormalized block encoding under purified/block-encoding access. Section III.3 also describes extracting the **normalized state**, including its preparation overhead. Their conclusion discusses conversion from sample access and leaves its total cost for further analysis.

Their parameter $`\kappa`$ satisfies $`\rho\ge I/\kappa`$; it is an inverse eigenvalue floor, rather than the ratio of the largest and smallest eigenvalues. Section III.3 explicitly notes $`\kappa\ge D`$ for full-rank states in dimension $`D`$. Thus their bound is consistent with a dimension-dependent copy obstruction even when the spectral ratio is constant. The present result concerns the complete normalized-output task under copy access; it does not refute their algorithm or introduce the transform.

Source: [arXiv:2401.07561v2, 10 April 2025](https://arxiv.org/html/2401.07561v2), especially Lemma 3, Theorem 5 and Section III.3.

## Mixedness testing supplies the information bound

O'Donnell and Wright [OW15] prove the mixedness-testing lower bound used here. For even $`D`$, their Theorem 4.2 compares weak Schur sampling for the uniform spectrum with the balanced spectrum

```math
P_D^\eta(j)=\frac{1+(-1)^{j-1}2\eta}{D},\qquad 0\le\eta\le\frac12,
```

and establishes

```math
d_{\chi^2}\!\left(\mathrm{SW}_{P_D^\eta}^{m},\mathrm{SW}_{D}^{m}\right)
\le \exp\!\left[\left(\frac{4m\eta^2}{D}\right)^2\right]-1.
```

The Haar-averaged tensor-power comparison has the same Schur-sector information. Its trace-distance distinguishability therefore vanishes when $`m/D\to0`$ for fixed $`\eta`$. This quantitative statement supports a small constant distinguishing gap; the proof does not rely solely on the usual success-probability formulation of mixedness testing. Setting $`\eta=0.4`$ gives the eigenvalues $`1.8/D`$ and $`0.2/D`$ used here.

Source: [arXiv:1501.05028v1](https://arxiv.org/html/1501.05028v1), Section 4.2, Theorem 4.2 and Corollary 4.3; [STOC 2015 publication](https://doi.org/10.1145/2746539.2746582).

## From a testing obstruction to a transformation obstruction

Jeronimo, Magrafta, Slote and Wu [JMSW24], Section 8.6, explicitly formulate the general strategy: a transformation producing a useful functional output would enable a property test, so testing hardness constrains transformation cost. Their examples include absolute-amplitude and conjugation transformations of pure states. We use this established reduction principle. The additional task-specific step here is a finite-response witness: a fixed known bounded perturbation turns hidden noncommuting orientation into the expectation of a known observable in the normalized exponential-update output.

Source: [arXiv:2411.15148v1](https://arxiv.org/html/2411.15148v1), Section 8.6 and Corollaries 8.13–8.14.

## Block-encoding conversion and other state-generation bounds

Arihara and Murao [AM26] distinguish sample access from block-encoding channels and the reverse conversion. Their Theorem 3 gives an inverse-error sample lower bound for implementing a block-encoding channel; Theorem 4 gives a dimension-dependent query lower bound for state recovery from a block encoding. Their Gibbs-preparation Corollary 8 uses low-temperature marked Hamiltonians, with inverse temperature at least logarithmic in dimension. These are different tasks from applying one fixed bounded known tilt to a full-rank unknown prior. They reinforce the need to distinguish access resources, but do not directly imply the copy-to-normalized-update theorem proved here.

Source: [arXiv:2608.22470v1](https://arxiv.org/html/2608.22470v1), Sections III–V.

## Why quantum belief propagation does not provide free modular access

Quantum belief propagation describes how a Gibbs state changes under a Hamiltonian perturbation. In the formulation reviewed by Capel, Moscolari, Teufel and Wessel [CMTW25], Section 10.1, the derivative involves an integral of the perturbation evolved under the original Hamiltonian. For an unknown prior that Hamiltonian is $`-\log\rho`$, up to a scalar. Access to copies of $`\rho`$ is not access to this modular dynamics. Efficient local approximations also use locality assumptions absent from the hidden-eigenbasis family considered here. The perturbation identity is an inherited analytic tool, rather than a sample-efficient implementation of this update.

Source: [Communications in Mathematical Physics 406, 43 (2025)](https://doi.org/10.1007/s00220-024-05198-x), Section 10.1.

## Scope of the contribution

The contribution is the finite-response transfer to the following operational regime: the perturbation is fixed and known, the prior has an identical supplied two-level eigenvalue multiset within constant factors of $`1/D`$, and the requested output is a single normalized updated state. The two hard ensembles have identical supplied spectra and entropy. The resulting lower bound holds against arbitrary processing of the supplied copies, including collective operations. It is not an optimality claim for all exponential-update algorithms, a complete dimension–accuracy tradeoff, or a claim that all noncommuting prior families are hard. If the prior commutes with the known perturbation, the ordinary bounded filter implements the same update with constant expected copy cost. No exhaustive priority claim is made.

## Constructive tomography baselines

The upper account uses O'Donnell and Wright's existing collective tomography estimator, followed by spectral repair, a proved stability bound and ordinary classical matrix calculation. Its quadratic copy dependence is inherited from tomography rather than claimed as a new tomography result. The explicit independent-copy alternative uses the random-Clifford inverse measurement channel of Huang, Kueng and Preskill, with the Clifford-design foundation of Dankert, Cleve, Emerson and Livine. Source statements and paid output-preparation costs are given in [upper_bounds.md](../science/upper_bounds.md).

## Bibliographic keys

| Key | Work |
| --- | --- |
| QKR25 | Qiu, Koor and Rebentrost, *The Quantum Esscher Transform*, version 2 (2025) |
| OW15 | O'Donnell and Wright, *Quantum Spectrum Testing* (2015) |
| JMSW24 | Jeronimo, Magrafta, Slote and Wu, *Coherence in Property Testing: Quantum-Classical Collapses and Separations* (2024) |
| AM26 | Arihara and Murao, *Sample-Query Interconversion of Block Encoding of Unknown Quantum States* (2026) |
| CMTW25 | Capel, Moscolari, Teufel and Wessel, *From Decay of Correlations to Locality and Stability of the Gibbs State* (2025) |
