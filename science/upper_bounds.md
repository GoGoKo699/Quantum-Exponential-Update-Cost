# Attainable baselines and the remaining gap

The lower bound concerns producing one normalized exponential-update state from independent source copies. The task is achievable with finitely many copies. At fixed tilt, fixed spectral bounds and fixed output error, collective tomography gives an $`O(D^2)`$ copy upper bound, while the proved hard family requires $`\Omega(D)`$ copies. These bounds leave a genuine gap; this account does not claim an optimal copy law. The construction also covers the hard family's furnished two-level spectrum, although it does not exploit that extra information.

## Promise and output convention

Let $`D`$ be the Hilbert-space dimension and assume known constants $`0\lt c\leq1\leq C`$ satisfy

```math
\frac{c}{D}I\preceq\rho\preceq\frac{C}{D}I.
```

Let $`H`$ be a supplied classical description of a Hermitian matrix with $`\Vert H\Vert _\infty\leq h`$. In the lower-bound example, $`H`$ is a fixed multiple of a known one-qubit Pauli operator, so its description and implementation do not grow with $`D`$ apart from identifying the register. Define

```math
\mathcal T_H(\rho)=\frac{\exp(\log\rho+H)}{\mathrm{Tr}\exp(\log\rho+H)}.
```

Trace distance means $`\tfrac12\Vert A-B\Vert _1`$. The final physical state includes averaging over the algorithm's measurement outcomes and classical randomness. No preparation circuit for the unknown source, inverse circuit, modular Hamiltonian, eigenbasis or QRAM is supplied.

A bound $`R`$ on the ordinary eigenvalue ratio also implies the displayed promise with $`c=1/R`$ and $`C=R`$. These are not inverse-minimum-eigenvalue bounds independent of $`D`$.

## Stability under a trace-norm estimate

**Lemma.** If $`\rho`$ and $`\sigma`$ both satisfy the displayed spectral promise, then

```math
\Vert \mathcal T_H(\rho)-\mathcal T_H(\sigma)\Vert _1
\leq L\Vert \rho-\sigma\Vert _1,
\qquad L=2(C/c)e^{2h}.
```

**Proof.** The resolvent formula for the logarithm gives

```math
\Vert \log\rho-\log\sigma\Vert _1
\leq\int_0^\infty\frac{\Vert \rho-\sigma\Vert _1}{(c/D+t)^2}\,dt
=\frac{D}{c}\Vert \rho-\sigma\Vert _1.
```

Put $`A=\log\rho+H`$ and $`B=\log\sigma+H`$. Both have largest eigenvalue at most $`\log(C/D)+h`$. The identity

```math
e^A-e^B=\int_0^1e^{(1-s)A}(A-B)e^{sB}\,ds
```

and the ideal property of the trace norm therefore imply

```math
\Vert e^A-e^B\Vert _1\leq\frac{Ce^h}{D}\Vert A-B\Vert _1
\leq(C/c)e^h\Vert \rho-\sigma\Vert _1.
```

The normalizing traces are in $`[e^{-h},e^h]`$, by eigenvalue monotonicity applied to $`\log\rho-hI\preceq A\preceq\log\rho+hI`$ and its counterpart for $`B`$. For positive matrices $`X,Y`$ with $`\mathrm{Tr}X\geq e^{-h}`$,

```math
\left\Vert \frac X{\mathrm{Tr}X}-\frac Y{\mathrm{Tr}Y}\right\Vert _1
\leq2e^h\Vert X-Y\Vert _1.
```

Combining these inequalities proves the claim. No commutativity is used. $`\square`$

## Restoring the spectral promise after tomography

Let

```math
\mathcal K=\{\tau:\mathrm{Tr}\tau=1,\ (c/D)I\preceq\tau\preceq(C/D)I\}.
```

Given a Hermitian estimate $`A`$, choose $`\widehat\rho\in\mathcal K`$ minimizing $`\Vert \widehat\rho-A\Vert _1`$. Because the true state is feasible,

```math
\Vert \widehat\rho-\rho\Vert _1\leq2\Vert A-\rho\Vert _1.
```

This is a finite classical optimization: diagonalize $`A`$, then minimize $`\sum_i|x_i-a_i|`$ subject to $`c/D\leq x_i\leq C/D`$ and $`\sum_i x_i=1`$. A minimizer can be chosen in this eigenbasis. Indeed, pinching any feasible matrix in that basis preserves the spectral bounds and trace and cannot increase its trace-norm distance from $`A`$.

This projection is used to ensure that a rare inaccurate tomography outcome never produces an undefined logarithm. Approximate optimization and matrix arithmetic can be assigned an additional error budget.

## Collective-copy upper bound

O'Donnell and Wright's tomography estimator $`A`$ is a density matrix and obeys

```math
\mathbb E\Vert A-\rho\Vert _F^2\leq\frac{4D-3}{N}.
```

Consequently,

```math
\mathbb E\Vert \widehat\rho-\rho\Vert _1
\leq2\sqrt{\frac{D(4D-3)}{N}}
\leq\frac{4D}{\sqrt N}.
```

Compute $`\mathcal T_H(\widehat\rho)`$ classically and prepare it as a mixed state. Convexity of trace distance and the stability lemma show that the averaged ideal output has error at most $`2LD/\sqrt N`$. Taking

```math
N\geq16L^2D^2/\epsilon^2
```

reserves at most $`\epsilon/2`$ for this statistical contribution and $`\epsilon/2`$ for numerical calculation and state preparation. Thus $`O(L^2D^2/\epsilon^2)`$ copies suffice. The unknown input state is consumed only by tomography; all later processing uses the paid classical estimate.

This is a copy-complexity upper bound using a collective tomographic POVM. We do not attach a polynomial gate-count or small coherent-memory claim to the implementation of that POVM. An arbitrary collective measurement can be much more demanding than consuming the same number of source copies.

## A concrete single-copy measurement baseline

For $`D=2^n`$, a fully specified alternative uses random Clifford basis measurements. On each fresh source copy choose a uniformly random $`n`$-qubit Clifford $`U`$, measure $`U\rho U^\dagger`$ in the computational basis, and record $`|\phi\rangle=U^\dagger|b\rangle`$. Use the standard unbiased estimator

```math
X=(D+1)|\phi\rangle\langle\phi|-I,
\qquad\mathbb E X=\rho.
```

The Clifford second-moment identity supplies unbiasedness. Also $`\mathrm{Tr}X^2=D^2+D-1`$ for every outcome, so the empirical average $`A=N^{-1}\sum_jX_j`$ satisfies

```math
\mathbb E\Vert A-\rho\Vert _F^2\leq\frac{D^2+D-1}{N}.
```

After the same spectral projection and classical update calculation, the averaged ideal output has trace-distance error at most

```math
L\sqrt{\frac{D(D^2+D-1)}{N}}.
```

Hence $`N=O(L^2D^3/\epsilon^2)`$ copies suffice for the same final error budget. This baseline uses one source copy at a time, an $`O(n^2)`$-gate random Clifford circuit and computational-basis measurement; it uses no data-loading oracle. Classical storage of the accumulated dense estimate is $`O(D^2)`$ numbers. Direct matrix accumulation costs at most $`O(ND^2)`$ scalar operations. Dense spectral decomposition, projection and matrix-function calculation are polynomial in $`D`$ and the requested arithmetic precision. These deliberately loose costs are charged rather than treated as efficient in $`n=\log_2D`$.

After diagonalizing the computed target as $`\sum_jp_j|v_j\rangle\langle v_j|`$, sample $`j`$ classically and prepare the known vector $`v_j`$. Generic amplitude synthesis uses $`O(D)`$ ideal controlled rotations on $`O(\log D)`$ qubits; their finite-precision synthesis is charged. The full target description already occupies $`O(D^2)`$ classical numbers. For a general dense supplied $`H`$, reading its $`D^2`$ entries is charged as well.

## What these upper bounds do and do not settle

The collective bound proves that the state-output task is possible with quadratic dimension dependence in source copies. The explicit single-copy baseline adds a transparent implementation with a worse cubic copy dependence. Neither is a new tomography method, a demonstrated practical speedup, or a matching construction for the lower bound. Whether a direct transformation avoids full tomography and attains $`O(D)`$ copies at fixed error remains open in this account, including for the two-eigenvalue hard family.

## Sources

- Ryan O'Donnell and John Wright, [Efficient quantum tomography](https://arxiv.org/abs/1508.01907), Theorem1.2 and Corollary1.4; [author-hosted text](https://www.cs.cmu.edu/~jswright/papers/tomography.pdf).
- Hsin-Yuan Huang, Richard Kueng and John Preskill, [Predicting Many Properties of a Quantum System from Very Few Measurements](https://arxiv.org/abs/2002.08953), NaturePhysics16,1050–1057(2020), Supplementary Proposition1 and equations(S38)–(S42), for the random-Clifford inverse measurement channel.
- Christoph Dankert, Richard Cleve, Joseph Emerson and Etera Livine, [Exact and Approximate Unitary 2-Designs: Constructions and Applications](https://arxiv.org/abs/quant-ph/0606161), PhysicalReviewA80,012304(2009), Theorem1, for the Clifford second-moment foundation and the $`O(n^2)`$ gate implementation.
