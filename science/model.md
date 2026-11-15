# The update task and its resources

A bounded change of a classical probability distribution can be sampled by accepting or rejecting existing samples. This project asks whether the analogous exponential update of an unknown quantum state can be performed from a small supply of specimens. The target is a specific relative-entropy update; it is different from applying a measurement filter to the state.

## The normalized Esscher update

For a positive definite density operator $`\rho`$ and known Hermitian tilt $`H`$, define

```math
\mathcal E_H(\rho)=\frac{\exp(\log\rho+H)}{\mathrm{Tr}\exp(\log\rho+H)}.
```

All logarithms in this account are natural. The input and output have the same dimension. Writing $`Z_H(\rho)=\mathrm{Tr}\exp(\log\rho+H)`$, the identity

```math
D(\sigma\Vert\mathcal E_H(\rho))
=D(\sigma\Vert\rho)-\mathrm{Tr}(H\sigma)+\log Z_H(\rho)
```

shows that the target uniquely minimizes the relative-entropy objective on the right. This variational interpretation and the Esscher map are inherited from [Qiu, Koor and Rebentrost](../references/RELATED_WORK.md#the-quantum-esscher-transform). The present task supplies the tilt itself; finding a Lagrange multiplier from an imposed expectation constraint is a different problem.

Use the half-trace convention

```math
D_{\rm tr}(\rho,\sigma)=\frac12\lVert\rho-\sigma\rVert_1.
```

## Supplied information

Let $`D`$ be divisible by four and let $`Z`$ have $`D/2`$ eigenvalues of each sign. For $`D=2^q`$, $`q\ge2`$, one may take $`Z=Z_1\otimes I_{D/2}`$: the tilt acts on just the first qubit. Fix

```math
a=\frac45,\qquad h=\frac1{10},\qquad H=hZ,
\qquad \varepsilon_0=\frac1{1000}.
```

The unknown state belongs to

```math
\rho_S=\frac{I+aS}{D},\qquad
S=S^\dagger,\quad S^2=I,\quad \mathrm{Tr}S=0.
```

The processor is supplied with this **exact eigenvalue multiset**: $`(1+a)/D`$ and $`(1-a)/D`$, each with multiplicity $`D/2`$. Thus every input has full rank, ordinary spectral condition number nine and the same entropy. Only the eigenspaces, or equivalently the orientation $`S`$, are unknown. The lower bound does not charge the processor for learning an unknown spectrum.

The source supplies independent copies of this one fixed state. The orientation is fixed throughout an execution, including across adaptive source requests. No purification, coherent preparation unitary, preparation inverse, eigenbasis description, support reflection or evolution under $`\log\rho_S`$ is supplied. Source-independent ancillas, unrestricted quantum memory, collective operations, adaptive instruments and classical computation are allowed. These generous computational permissions strengthen the copy lower bound.

## Required output and budget

An $`n`$-copy processor is a quantum channel $`\Lambda_n`$ satisfying

```math
D_{\rm tr}\!\left(\Lambda_n(\rho_S^{\otimes n}),
\mathcal E_{hZ}(\rho_S)\right)\le\varepsilon_0
\quad\text{for every balanced }S.
```

The output is one normalized quantum state. If a larger output is produced, the inequality concerns its designated state marginal. A classical density-matrix description, a purification or a reusable transformation channel is not required.

A hard budget bounds every execution branch. A protocol requesting at most $`n`$ specimens adaptively can be simulated by supplying $`n`$ specimens in advance, retaining the entire classical record, and discarding unused specimens. It is therefore included in the channel model above. Every specimen consumed by failed attempts, control programs, discarded outcomes or estimation is charged.

## Main result

**Theorem.** Every processor meeting this contract requires more than $`10^{-3}D`$ copies. In particular the worst-case copy cost is $`\Omega(D)`$, or $`\Omega(2^q)`$ for $`q`$ qubits, even with the supplied exact spectrum and the known one-qubit tilt.

The [finite-response calculation](response.md) and [copy converse](copy_lower_bound.md) prove the theorem. Their numerical constants are sufficient rather than optimized. The same order extends to fixed-probability heralding and uniformly bounded expected copy cost with the qualifications stated in the converse.

The [commuting and filtering baselines](baselines.md) use at most five copies at the same accuracy and tilt. A general constructive upper bound and the remaining gap are stated in [upper bounds](upper_bounds.md). The lower theorem grants free computation; it is not a gate lower bound or a matching characterization of total implementation cost.

## Scope of the source promise

The hard family consists of generic mixed states with unknown global eigenspaces. It is not promised to be a local-Hamiltonian Gibbs family, a low-rank state family or the output of a known short circuit. A one-qubit tilt does not make the unknown modular Hamiltonian $`-\log\rho_S`$ a local or supplied operator. Structured sources can have additional efficient update mechanisms without contradicting the theorem.
