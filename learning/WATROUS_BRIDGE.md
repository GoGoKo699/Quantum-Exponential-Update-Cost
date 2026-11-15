# From Watrous to exponential-update cost

[Learning guide](README.md) · [30 milestones](MILESTONES.md) · [Science guide](../science/README.md)

**Anchor:** John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018. Chapter and section numbers below refer to that edition and the manuscript linked from the [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/).

This project uses natural logarithms throughout. Watrous writes $`\log`$ for base-two logarithms and $`\ln`$ for natural logarithms; his relative entropy in bits becomes the project's natural-log value after multiplication by $`\ln 2`$.

## The scientific story

A source repeatedly supplies specimens in the same unknown quantum state. A known, small evidence term is then specified. The desired operation adds that evidence to the logarithm of the prior and normalizes the result. In a commuting problem, a simple accept-or-reject filter produces the target. The question is whether such a small update remains inexpensive when the prior's orientation is unknown.

The main theorem shows a worst-case obstruction. All hard inputs have the same supplied spectrum, so learning eigenvalues cannot explain the cost. The missing information is how their eigenspaces sit relative to the evidence. A successful exponential update would reveal part of that hidden orientation before the available input specimens permit any collective measurement to reveal it.

## The anchor route

| Watrous location | Foundation used here | Project destination |
| --- | --- | --- |
| Chapter 1, mathematical preliminaries | Operators, spectral calculus and norms | Logarithms, exponentials and full-rank priors |
| Section 2.1.2, quantum states of registers | Density operators, mixtures and tensor products | Independent copies of one unknown state |
| Section 2.2, quantum channels | Physical transformations and discarded registers | An arbitrary processor acting on all supplied copies |
| Chapter 2, measurements | Outcome probabilities from positive measurement operators | The known evidence observable and the success flag |
| Section 3.1.1; Theorem 3.4 | Binary discrimination and the trace norm | Turning an output difference into a forbidden input distinction |
| Chapter 5, quantum entropy and source coding | Quantum relative entropy | The variational meaning of exponential updating |
| Section 7.1, permutation-invariant vectors and operators | Symmetry among copies | The tensor-power ensemble comparison |
| Section 7.2.1, uniform spherical measure and Haar measure | Unbiased distributions of orientations | The hidden-eigenbasis lower-bound distribution |

These readings establish the vocabulary. The research ingredients needed beyond the anchor are described [below](#what-the-project-adds-to-the-anchor).

## Translate a state into a source contract

A density operator is a positive semidefinite matrix with trace one. In this project the prior is positive definite, so its matrix logarithm exists. If

```math
\rho=\sum_j p_j|v_j\rangle\langle v_j|,
```

then

```math
\log\rho=\sum_j(\log p_j)|v_j\rangle\langle v_j|.
```

This is a definition of the target, not an operation supplied by the source. Possessing a specimen in state $`\rho`$ does not provide the numbers $`p_j`$, the vectors $`v_j`$, a circuit preparing $`\rho`$, or evolution under $`\log\rho`$.

In the main theorem, the exact eigenvalue multiset is supplied separately as classical information; the eigenspaces remain unknown.

An $`n`$-copy request supplies $`\rho^{\otimes n}`$. Every copy in that expression has the **same fixed unknown orientation**. The processor may entangle them, retain a quantum memory, measure adaptively and use unlimited classical computation. Every consumed specimen counts, including those discarded after a failed attempt. The [model](../science/model.md) gives the complete contract.

## Two operations that coincide classically

The desired normalized exponential update is

```math
\mathcal E_H(\rho)=
\frac{e^{\log\rho+H}}{\mathrm{Tr}e^{\log\rho+H}}.
```

The ordinary sandwich filter produces

```math
\mathcal F_H(\rho)=
\frac{e^{H/2}\rho e^{H/2}}{\mathrm{Tr}(e^H\rho)}.
```

For commuting $`\rho`$ and $`H`$, the matrix identity $`e^{\log\rho+H}=e^H\rho`$ makes the outputs equal. Outside that regime, changing the order of matrix operations changes the answer. Both outputs are valid states, but only the first solves the specified task.

## A complete qubit example

Take one qubit and supply the matrices

```math
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
```

```math
\rho=\frac{I+0.8X}{2}
=\begin{pmatrix}0.5&0.4\\0.4&0.5\end{pmatrix},
\qquad H=0.1Z.
```

The prior has eigenvalues $`0.9`$ and $`0.1`$. Its polarization points along $`X`$, while the evidence points along $`Z`$; the two operators do not commute.

Put

```math
b=\mathrm{atanh}(0.8)=\tfrac12\log9,
\qquad s=\sqrt{b^2+0.1^2}.
```

Since $`\log\rho=(\log0.3)I+bX`$, the scalar part cancels on normalization. The exponential formula for Pauli matrices gives the complete target:

```math
\mathcal E_H(\rho)
=\frac12\left[I+\frac{\tanh s}{s}(bX+0.1Z)\right]
\approx
\begin{pmatrix}
0.536333506026&0.399164362110\\
0.399164362110&0.463666493974
\end{pmatrix}.
```

Direct multiplication and normalization instead give

```math
\mathcal F_H(\rho)
=\frac12\left[I+\frac{0.8}{\cosh0.1}X+\tanh0.1\,Z\right]
\approx
\begin{pmatrix}
0.549833997312&0.398008299581\\
0.398008299581&0.450166002688
\end{pmatrix}.
```

Measuring $`Z`$ on either ideal output gives outcomes $`+1`$ and $`-1`$. Their predicted means are

```math
\mathrm{Tr}[Z\mathcal E_H(\rho)]\approx0.072667012053,
\qquad
\mathrm{Tr}[Z\mathcal F_H(\rho)]\approx0.099667994625.
```

For qubit states, half trace distance is half the Euclidean distance between their Bloch vectors. Here it is

```math
\frac12\|\mathcal E_H(\rho)-\mathcal F_H(\rho)\|_1
\approx0.013549898359.
```

This is larger than the main theorem's output tolerance $`0.001`$, so treating the filter as an exact implementation of the target would matter at that tolerance.

### What the example costs

The known success operator

```math
K=e^{(H-0.1I)/2}
=\begin{pmatrix}1&0\\0&e^{-0.1}\end{pmatrix}
```

is a valid filter because $`K^\dagger K\le I`$. Each attempt consumes **one fresh source copy**. For this particular prior its success probability is

```math
p=\frac{1+e^{-0.2}}2\approx0.909365376539,
```

so repeating until success uses $`1/p\approx1.099667994625`$ copies on average. Uniformly over all priors, five attempts with a fixed fallback output give half-trace error below $`0.000196`$ relative to the ideal sandwich-filter state. Flag-rotation synthesis has its actual implementation cost; the five-copy claim concerns ideal operations. See the [charged baseline](../science/baselines.md).

The displayed Esscher matrix was calculated from a classically specified prior to show what the two definitions mean. That calculation is not a copy-only preparation algorithm for an unknown prior. Likewise, the displayed $`Z`$ means are exact predictions: estimating a mean experimentally requires repeated output preparations and measurements, with all their source copies charged.

This qubit example illustrates the difference between the maps. It is **not** the main lower-bound proof, whose known-spectrum construction uses dimensions divisible by four and compares ensembles of orientations.

## Why half trace distance is the right output requirement

The project uses

```math
T(\sigma,\tau)=\frac12\|\sigma-\tau\|_1.
```

For equal-prior binary discrimination, Watrous's Holevo–Helstrom theorem gives

```math
p_{\rm opt}=\frac12+\frac12T(\sigma,\tau).
```

For a measurement effect $`0\le M\le I`$, the probability difference is at most $`T(\sigma,\tau)`$. For a signed observable such as $`Z`$, with norm at most one, its mean difference is at most $`2T(\sigma,\tau)`$. This factor of two is retained throughout the [copy converse](../science/copy_lower_bound.md).

A channel cannot increase distinguishability. Therefore an alleged update processor followed by a $`Z`$ measurement cannot extract more information than a measurement on its original input copies. That restriction applies even if the processor never estimates a density matrix.

## Haar orientation and a fixed hidden source

The main family is

```math
\rho_S=\frac{I+0.8S}{D},\qquad
S=S^\dagger,\quad S^2=I,\quad\mathrm{Tr}S=0.
```

Every input has eigenvalues $`1.8/D`$ and $`0.2/D`$, each repeated $`D/2`$ times. The processor is told that exact spectrum. The evidence is the fixed operator $`H=0.1Z`$, with $`Z`$ balanced between its two eigenspaces.

The proof compares two distributions within this same spectrum. In one, $`S=UZU^\dagger`$ has a full Haar-random orientation. In the other, $`S`$ is randomly oriented separately inside each eigenspace of $`Z`$, so the prior commutes with the evidence. Each execution draws its hidden orientation once and supplies copies of that state.

The averaged input is consequently

```math
\Omega_n=\mathbb E_U[\rho_U^{\otimes n}],
```

which is generally different from

```math
(\mathbb E_U\rho_U)^{\otimes n}=(I/D)^{\otimes n}.
```

The copies share an unknown orientation; they are not independently redrawn mixed states. Permutation and unitary symmetries organize the information in these correlated averages. The maximally mixed tensor power is a mathematical comparison state, rather than an alternative input carrying different supplied spectrum information.

## What the project adds to the anchor

Three research ingredients connect these foundations to the theorem. They are supplied in this repository and the cited papers, not attributed to Watrous's textbook.

First, differentiating the normalized exponential along $`tZ`$ gives the response

```math
\left.\frac{d}{dt}\mathrm{Tr}[Z\mathcal E_{tZ}(\rho)]\right|_{t=0}
=\int_0^1\mathrm{Tr}(\rho^{1-s}Z\rho^sZ)\,ds
-(\mathrm{Tr}\rho Z)^2.
```

This is the Bogoliubov–Kubo–Mori susceptibility. In an eigenbasis its matrix weights are logarithmic means. The [response account](../science/response.md) derives it by Duhamel differentiation, computes the exact Haar second moment, and controls the remainder uniformly in dimension. That last step turns an infinitesimal response into a gap at the fixed tilt $`0.1`$.

Second, the proof uses the **quantitative** O'Donnell–Wright mixedness bound for the balanced two-level spectrum. It shows that sublinear supplies of copies cannot distinguish the relevant averaged states. The exact statement and its Schur-Weyl interpretation are in the [copy converse](../science/copy_lower_bound.md#the-inherited-mixedness-testing-bound).

Third, the commuting and fully oriented ensembles have different mean output responses. Uniformly accurate updating would preserve enough of this gap to distinguish the input ensembles. Channel contractivity then forces more than $`10^{-3}D`$ source copies at output error $`0.001`$. This is an average-ensemble argument supporting a worst-case task lower bound; it requires no assertion that every individual Haar draw has the same response.

## Keep the conclusion at its proved scope

The result shows that this particular normalized exponential update has no generic dimension-independent sampler from copies, even when the exact hard-family spectrum is known. A commuting update and the ordinary sandwich filter remain inexpensive. A known or efficiently simulable modular Hamiltonian would provide an additional resource absent from the model.

The [upper-bound account](../science/upper_bounds.md) supplies a collective-tomography method using $`O(D^2)`$ copies and an explicit independent-copy measurement baseline using $`O(D^3)`$ copies at fixed parameters. The lower bound is $`\Omega(D)`$. The gap remains open, and the theorem does not say that tomography is necessary. The [30 milestones](MILESTONES.md) follow this entire route from the source contract to the proof and its remaining limits.
