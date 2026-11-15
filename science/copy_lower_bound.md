# A linear dimension cost for one exponential update

An update algorithm receives independent copies of an unknown prior. It knows the evidence operator and may use arbitrary collective quantum operations. Even if its actual input spectrum is supplied exactly, producing one exponential-update state can require a number of copies linear in the Hilbert-space dimension.

We use half trace distance

```math
T(\rho,\sigma)=\frac12\Vert \rho-\sigma\Vert _1.
```

The main statement concerns a hard worst-case copy budget. A protocol consuming at most $`n`$ copies, including an adaptive protocol, is represented by a quantum channel $`\Phi_n`$ on $`n`$ input copies: unused copies can be ignored. Known ancillas, measurements, randomness and classical control are included in that channel.

## The known-spectrum task

Fix a dimension $`D`$ divisible by four and the known balanced involution $`Z`$ from [the response calculation](response.md). The unknown prior lies in the single unitary orbit

```math
\mathcal O_D(a)
=\left\{\rho_U=\frac{I+aUZU^\dagger}{D}:U\in\mathsf U(D)\right\},
\qquad 0\lt a\lt 1.
```

Every prior has exactly the same two eigenvalues, $`(1+a)/D`$ and $`(1-a)/D`$, each with multiplicity $`D/2`$. This spectrum may be given to the algorithm. Its eigenbasis is unknown.

For a fixed $`h\gt 0`$, the required output is

```math
\mathcal E_{hZ}(\rho)
=\frac{e^{\log\rho+hZ}}{\mathrm{Tr}e^{\log\rho+hZ}}.
```

The input interface supplies copies and the stated classical information. It supplies no matrix description, purification oracle, inverse preparation oracle, block encoding, or modular-evolution oracle for $`\rho`$. The lower bound allows unlimited processing of the copies and the known evidence, so it does not rely on a gate-complexity assumption.

## Main theorem

Define the response bound established in Proposition 3 of [the response calculation](response.md):

```math
g=g(a,h)
=\left[\frac12-\frac{a}{\log((1+a)/(1-a))}\right]h
-\frac{14}{3}h^3.
```

Also put

```math
B_d(n)=\frac12\sqrt{\exp\!\left[\left(\frac{na^2}{d}\right)^2\right]-1}.
```

The parameter $`a`$ is fixed in every occurrence of $`B_d`$.

**Theorem 1 (known-spectrum copy cost).** Suppose $`g\gt 0`$ and a channel $`\Phi_n`$ satisfies

```math
T\!\left(\Phi_n(\rho^{\otimes n}),\mathcal E_{hZ}(\rho)\right)
\le\epsilon
\qquad\text{for every }\rho\in\mathcal O_D(a),
```

where $`0\le\epsilon\lt g/4`$. Then

```math
g-4\epsilon\le 2B_D(n)+4B_{D/2}(n).
```

In particular,

```math
n\ge\frac{g-4\epsilon}{5\sqrt2\,a^2}\,D.
```

For $`a=4/5`$, $`h=1/10`$ and $`\epsilon=10^{-3}`$, this implies

```math
n\gt 10^{-3}D.
```

Every input is full rank with eigenvalue ratio $`9`$, its spectrum is known, and the evidence norm is $`1/10`$. All constants are independent of $`D`$. For $`D=2^q`$ with $`q\ge2`$, this is an exponential copy cost in the number of input qubits.

## The inherited mixedness-testing bound

The information-theoretic ingredient is the exact hard ensemble in O'Donnell and Wright's *Quantum Spectrum Testing*, [arXiv:1501.05028v1](https://arxiv.org/abs/1501.05028v1), Section 4.2, Theorem 4.2. The [author-hosted January 20, 2015 PDF](https://www.cs.utexas.edu/~wright/papers/quantum-spectrum-testing.pdf) states the same bound.

For even $`d`$, let $`P_\eta`$ be the alternating spectrum with eigenvalues $`(1+2\eta)/d`$ and $`(1-2\eta)/d`$, each repeated $`d/2`$ times. Write $`\mathsf{SW}_{P_\eta}^n`$ for its Schur-Weyl distribution on Young diagrams and $`\mathsf{SW}_{\mathrm{unif}}^n`$ for the maximally mixed spectrum. Their theorem proves

```math
\chi^2\!\left(\mathsf{SW}_{P_\eta}^n,
\mathsf{SW}_{\mathrm{unif}}^n\right)
\le\exp\!\left[\left(\frac{4n\eta^2}{d}\right)^2\right]-1,
\qquad 0\le\eta\le\frac12.
```

We need its statement for this particular ensemble, rather than only the worst-case conclusion that mixedness testing takes $`\Omega(d)`$ copies.

Put $`\eta=a/2`$, let $`J_d`$ be a balanced involution in dimension $`d`$, and let $`V`$ be Haar distributed. Define

```math
\Omega_{0,n}^{(d)}=\left(\frac Id\right)^{\otimes n},\qquad
\Omega_{1,n}^{(d)}
=\mathbb E_V\left(\frac{I+aVJ_dV^\dagger}{d}\right)^{\otimes n}.
```

Both states commute with global unitaries $`W^{\otimes n}`$ and with permutations of the copies. In the Schur-Weyl decomposition

```math
(\mathbb C^d)^{\otimes n}
=\bigoplus_{\lambda\vdash n,\,\ell(\lambda)\le d}
\mathcal V^d_\lambda\otimes\mathcal W_\lambda,
```

they are therefore scalar on each block. Their block weights are precisely their Schur-Weyl probabilities. Thus their half trace distance equals the total variation distance between the corresponding Schur-Weyl distributions. Cauchy-Schwarz, followed by the quoted theorem, gives

```math
T\!\left(\Omega_{0,n}^{(d)},\Omega_{1,n}^{(d)}\right)
\le B_d(n).
```

For $`n=0`$, use the scalar empty-input state and $`B_d(0)=0`$. The bound permits arbitrary collective measurements. The testing spectrum, Schur-Weyl bound and resulting mixedness hardness are inherited results; the update-to-testing transfer below is the additional argument.

## Proof of the known-spectrum theorem

The proof compares two ensembles inside the same known-spectrum orbit. They differ in the orientation of the prior relative to the evidence.

The first ensemble is the full Haar family $`\rho_U`$. Let

```math
\Omega_{\mathrm F,n}=\mathbb E_U\rho_U^{\otimes n}
=\Omega_{1,n}^{(D)}.
```

For the second ensemble, write $`m=D/2`$ and decompose the Hilbert space into the known $`Z=+1`$ and $`Z=-1`$ sectors. In each sector choose an independent Haar conjugate of a balanced involution:

```math
S_{\mathrm C}
=(V_+J_mV_+^\dagger)\oplus(V_-J_mV_-^\dagger),\qquad
\rho_{\mathrm C}=\frac{I+aS_{\mathrm C}}D.
```

Since $`m`$ is even, this definition is valid. The operator $`S_{\mathrm C}`$ has $`D/2`$ eigenvalues of each sign, so every $`\rho_{\mathrm C}`$ belongs to $`\mathcal O_D(a)`$. There is no spectral side-information difference between the two ensembles. Moreover,

```math
[\rho_{\mathrm C},Z]=0,\qquad
\mathrm{Tr}(\rho_{\mathrm C}Z)=0.
```

It follows for every draw of $`V_+,V_-`$ that

```math
\mathrm{Tr}\!\left[Z\mathcal E_{hZ}(\rho_{\mathrm C})\right]
=\tanh h.
```

Thus the Haar-averaged output response gap between the commuting ensemble and the full Haar ensemble is at least $`g`$.

Let

```math
\Omega_{\mathrm C,n}=\mathbb E_{V_+,V_-}\rho_{\mathrm C}^{\otimes n}.
```

To bound its distance from the maximally mixed $`n`$-copy state, write

```math
\rho_{\mathrm C}=\frac12\sigma_+\oplus\frac12\sigma_-,
\qquad
\sigma_\pm=\frac{I_m+aV_\pm J_mV_\pm^\dagger}{m}.
```

Every $`Z`$-sector word $`b\in\{+,-\}^n`$ occurs with probability $`2^{-n}`$. Conditioned on that word, let $`n_+`$ and $`n_-`$ be its two counts. Averaging over the two independent Haar unitaries gives, up to a permutation of the tensor factors,

```math
\Omega_{1,n_+}^{(m)}\otimes\Omega_{1,n_-}^{(m)}.
```

The maximally mixed state has the same sector-word probabilities and has conditional quantum state

```math
\Omega_{0,n_+}^{(m)}\otimes\Omega_{0,n_-}^{(m)}.
```

The product-state trace-distance inequality and the inherited bound give a conditional distance at most

```math
B_m(n_+)+B_m(n_-)\le2B_m(n).
```

Averaging over the orthogonal sector words preserves this bound. Therefore,

```math
T\!\left(\Omega_{\mathrm C,n},\Omega_{0,n}^{(D)}\right)
\le2B_{D/2}(n).
```

The full Haar ensemble obeys

```math
T\!\left(\Omega_{\mathrm F,n},\Omega_{0,n}^{(D)}\right)
\le B_D(n).
```

The triangle inequality now yields

```math
T(\Omega_{\mathrm C,n},\Omega_{\mathrm F,n})
\le B_D(n)+2B_{D/2}(n).
```

Apply $`\Phi_n`$ to the two ensembles. Convexity carries the pointwise output guarantee to each ensemble average. An observable of norm at most one changes in expectation by at most $`2\epsilon`$ under a half trace error $`\epsilon`$, so the difference of the two algorithmic output $`Z`$ means is at least $`g-4\epsilon`$. Trace-norm contraction consequently implies

```math
g-4\epsilon
\le 2T\!\left(\Phi_n(\Omega_{\mathrm C,n}),
\Phi_n(\Omega_{\mathrm F,n})\right)
\le 2B_D(n)+4B_{D/2}(n).
```

It remains to obtain the simpler linear bound. Put $`x=na^2/D`$. For $`0\le t\le1`$,

```math
\sqrt{e^{t^2}-1}\le\sqrt2\,t.
```

One proof uses the convexity chord $`e^y-1\le(e-1)y\le2y`$ for $`0\le y\le1`$. If $`x\le1/2`$, apply this estimate at $`x`$ and $`2x`$ to obtain

```math
2B_D(n)+4B_{D/2}(n)\le5\sqrt2\,x.
```

If $`x\gt 1/2`$, the resulting linear lower bound on $`n`$ already holds: the response bound has $`g\le2`$, hence $`g-4\epsilon\le2\lt 5\sqrt2/2`$. This proves

```math
n\ge\frac{g-4\epsilon}{5\sqrt2\,a^2}D.
```

At the stated fixed constants the coefficient exceeds $`0.00108`$, which implies the conservative $`n\gt 10^{-3}D`$. $`\square`$

The proof uses a single fixed output statistic. It needs neither tomography of the output nor concentration over the unknown eigenbasis.

## A two-spectrum intermediate with a larger numerical coefficient

The comparison with the maximally mixed prior gives a useful intermediate statement. In this variant the promise allows both $`\rho_0=I/D`$ and $`\rho_U`$, and the actual choice of spectrum is not supplied to the algorithm.

**Proposition 2 (two-spectrum bound).** Let $`D\ge2`$ be even. If the same half trace output guarantee holds for every state in

```math
\{\rho_0\}\cup\mathcal O_D(a),
```

and $`0\le\epsilon\lt g/4`$, then

```math
n\ge\frac D{a^2}
\sqrt{\log\!\left(1+(g-4\epsilon)^2\right)}.
```

For $`a=4/5`$, $`h=1/10`$ and $`\epsilon=10^{-3}`$, this is $`n\gt 0.00769D`$.

**Proof.** Compare $`\Omega_{0,n}^{(D)}`$ and $`\Omega_{\mathrm F,n}`$. Their target output $`Z`$ means differ by at least $`g`$, while the algorithmic output errors can reduce that gap by at most $`4\epsilon`$. The inherited mixedness bound and data processing give

```math
g-4\epsilon
\le2T\!\left(\Omega_{0,n}^{(D)},\Omega_{\mathrm F,n}\right)
\le\sqrt{\exp\!\left[\left(\frac{na^2}{D}\right)^2\right]-1}.
```

Solve this inequality for $`n`$. $`\square`$

This proposition alone would not justify a known-actual-spectrum claim: the supplied spectrum would reveal which side of its comparison holds. Theorem 1 removes that issue by comparing commuting and noncommuting ensembles with identical spectra.

## Fixed constants

The exact analytic expressions above define the results. These decimal bounds only help interpret their scale.

| Quantity | Fixed choice or conservative bound |
| --- | --- |
| Spectral contrast $`a`$ | $`4/5`$ |
| Eigenvalue ratio | $`9`$ |
| Evidence norm $`h`$ | $`1/10`$ |
| Half trace output error $`\epsilon`$ | $`1/1000`$ |
| Response bound $`g`$ | $`\gt 0.0089237`$ |
| Main known-spectrum coefficient | $`\gt 0.00108`$ |
| Two-spectrum coefficient | $`\gt 0.00769`$ |

For example, the elementary series $`\log9=4\sum_{j\ge0}2^{-(2j+1)}/(2j+1)`$ verifies the response bound without a dimension-dependent numerical calculation. Together with $`\log(1+x)\ge x/(1+x)`$, it also gives the conservative two-spectrum coefficient.

## Heralded output and expected-copy variants

The finite constants above belong to the hard-budget statements. The following reductions retain a linear dimension lower bound, with a different constant.

**Corollary 3 (heralded success).** Suppose a run consumes at most $`t`$ copies, succeeds with probability at least a fixed $`p_{\min}\gt 0`$ on every promised input, and its conditional output on success has half trace error at most a fixed $`\epsilon\lt g/4`$. Then $`t=\Omega(D)`$.

**Proof.** Choose a fixed $`\delta\gt 0`$ with $`\epsilon+\delta\lt g/4`$. Repeat the run from fresh copies, stopping at its first success, for at most $`k`$ runs, where $`k`$ is a fixed integer with $`(1-p_{\min})^k\le\delta`$. On total failure, output any fixed state. The resulting protocol has hard budget $`kt`$ and unconditional half trace error at most $`\epsilon+\delta`$. Theorem 1 gives $`kt\ge cD`$ for a fixed $`c\gt 0`$. Since $`k`$ is independent of $`D`$, the claim follows. $`\square`$

**Corollary 4 (uniform expected copy budget).** Suppose an almost surely terminating protocol has half trace output error at most a fixed $`\epsilon\lt g/4`$ and consumes at most $`T`$ copies in expectation on every promised input. Then $`T=\Omega(D)`$.

**Proof.** Fix $`\delta\gt 0`$ with $`\epsilon+\delta\lt g/4`$. Truncate the protocol after $`L=\lceil T/\delta\rceil`$ copies: if it requests another copy, output a fixed fallback state. Markov's inequality bounds that event by $`\delta`$ on every input. The truncated protocol has half trace output error at most $`\epsilon+\delta`$, so Theorem 1 gives $`L\ge cD`$, where

```math
c=\frac{g-4(\epsilon+\delta)}{5\sqrt2\,a^2}\gt 0.
```

Since $`L\le T/\delta+1`$, one obtains $`T\ge\delta(cD-1)`$. $`\square`$

These reductions require uniform success or expectation bounds over the promised inputs. A small postselected error without a charged success probability is not covered.

## What the result distinguishes

The main obstruction remains when the actual spectrum is supplied and the algorithm has unrestricted coherent memory and collective operations. It concerns producing the normalized state from copies. A subnormalized block encoding is a different output, and a callable purification or block-encoding oracle is a different input interface.

The result is not a claim that every quantum update is expensive. The measurement-filter update

```math
\mathcal L_H(\rho)
=\frac{e^{H/2}\rho e^{H/2}}{\mathrm{Tr}(e^H\rho)}
```

has a direct probabilistic implementation with expected copy cost bounded in terms of $`\Vert H\Vert `$ alone. It is exactly $`\mathcal E_H(\rho)`$ whenever $`[\rho,H]=0`$, and implementing that filter does not require knowing the input eigenbasis. Classical exponential tilting similarly admits rejection sampling from the prior for known bounded evidence. The distinction established here is the copy cost of the noncommuting minimum-relative-entropy update.

The theorem gives a lower bound, not a matching general upper bound or an optimal dependence on output accuracy.

