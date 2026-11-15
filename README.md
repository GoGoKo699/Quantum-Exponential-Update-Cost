# Quantum Exponential Update Cost

**Can a small exponential update of an unknown quantum state be sampled from a small number of existing specimens?**

This project proves a dimension-dependent obstruction for the normalized Esscher update

$$
\mathcal E_H(\rho)=\frac{e^{\log\rho+H}}{\operatorname{Tr}e^{\log\rho+H}}.
$$

Even when the **exact spectrum is supplied**, producing one updated state can require $\Omega(D)$ input copies in dimension $D$. The hard inputs are full rank, have eigenvalue ratio nine, and all share the same two-level spectrum. The tilt is the fixed known one-qubit operator $H=0.1Z_1$; the target half-trace error is $0.001$.

For $q\ge2$ qubits, $D=2^q$, so this is an exponential copy cost. The processor may use arbitrary collective quantum operations and unrestricted memory. The unknown orientation of the prior relative to the tilt supplies the obstruction.

## Results and costs

| Task and interface | Established copy cost |
| --- | --- |
| One Esscher output, known exact hard-family spectrum, unknown orientation | More than $10^{-3}D$ copies in the worst case |
| Same task with fixed-probability heralding or uniformly bounded expected budget | $\Omega(D)$, with the stated success and accuracy conventions |
| General bounded-spectral-scale prior, collective tomography and classical processing | $O(D^2)$ at fixed tilt, spectral bounds and output error |
| Explicit independent-copy Clifford-measurement implementation | $O(D^3)$ at the same fixed parameters |
| Commuting Esscher update, or ordinary bounded sandwich filtering | At most five copies at the theorem's tilt and error |

The quadratic collective upper bound and linear lower bound leave an open gap. The constructive methods charge tomography, dense classical processing and final state preparation; no QRAM, preparation inverse or modular-Hamiltonian oracle is supplied. [Upper bounds](science/upper_bounds.md) distinguish copy complexity from implementation costs.

Ordinary filtering produces $e^{H/2}\rho e^{H/2}/\operatorname{Tr}(e^H\rho)$. It agrees with the Esscher update on commuting inputs and remains inexpensive on general inputs. [The two operations](science/baselines.md) differ for noncommuting states.

## Read the science

The [science guide](science/README.md) connects the complete account.

| Question | Authoritative account |
| --- | --- |
| What is known, supplied, produced and counted? | [Model and main theorem](science/model.md) |
| How does a bounded tilt reveal hidden orientation? | [Exact response and finite-tilt witness](science/response.md) |
| Why can arbitrary collective processing do no better? | [Copy lower bound and success conventions](science/copy_lower_bound.md) |
| Why are commuting updates and ordinary filters cheap? | [Charged filtering baselines](science/baselines.md) |
| What constructive upper bounds are available? | [Stability, tomography and state output](science/upper_bounds.md) |
| What does the theorem mean, and where does it stop? | [Interpretation](science/interpretation.md) |
| Which definitions, identities and hardness results are inherited? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

The proof combines a finite Esscher-response witness with the established O'Donnell–Wright mixedness bound. It compares fully Haar-oriented and block-commuting priors with identical supplied spectra. Both input ensembles remain difficult to distinguish from a maximally mixed reference at sublinear copy count, while their updated states have different expectation values of one known observable. No typical-input concentration or dimension-dependent accuracy limit is needed.

## Learn the argument

The selected educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [learning guide](learning/README.md) connects the task to the [source bridge](learning/WATROUS_BRIDGE.md) and the [30-milestone map](learning/MILESTONES.md). The route develops 12 background milestones and 18 narrative milestones, moving from states and copy access to the complete same-spectrum argument and its constructive comparisons. The bridge includes a complete one-qubit example distinguishing exponential updating from ordinary filtering.

## Reproduce the finite checks

The [verification guide](verification/README.md) gives pinned dependencies, commands, expected results and scope. The diagnostics compare independent matrix formulas, exact qubit integration, same-spectrum controls, finite-tilt constants and selected Haar averages. Their [figure](verification/finite_diagnostics.png) summarizes the finite experiments. The analytical proofs establish the uniform lower bound.

## Scope

The source is an unknown generic mixed state with independent-copy access. Its modular Hamiltonian is not promised to be local, known or efficiently simulable. The theorem concerns this particular minimum-relative-entropy exponential update, rather than every quantum inference rule or every noncommuting source. A matching copy upper bound, efficient collective-tomography gate implementation and a practical hardware advantage remain unestablished.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
