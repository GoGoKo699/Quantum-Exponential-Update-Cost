# What the sampling barrier means

## A local change can require global source information

The [main theorem](model.md) concerns one known term $0.1Z_1$ added to the logarithm of an unknown state. The requested output is just one updated state, not its density matrix or a reusable update circuit. Nevertheless a generic copy-only processor needs a supply of specimens proportional to the Hilbert-space dimension.

Every hard input has the same supplied two-level spectrum, full rank and spectral condition number nine. The update strength and output tolerance remain fixed as the dimension grows. Small acceptance probability, eigenvalue learning, a vanishing minimum eigenvalue relative to the natural $1/D$ scale, and a large classical output are therefore not the source of this lower bound.

The decisive difference is orientation. A bounded Esscher update makes the hidden orientation of the prior visible in one known output observable. Producing that state would distinguish two input ensembles before collective quantum measurements can distinguish their supplied specimens. The [response identity](response.md) connects this effect to the Bogoliubov–Kubo–Mori susceptibility; [O'Donnell–Wright mixedness hardness](../references/RELATED_WORK.md) supplies the indistinguishability ingredient.

## Scope of the algorithmic conclusion

There is no dimension-independent generic quantum rejection sampler for this exact copy-access task. In contrast, the [ordinary sandwich filter](baselines.md) needs a constant number of copies under a bounded tilt, and it is exactly the Esscher update on commuting inputs. This distinction concerns specific update rules, rather than the general possibility of quantum Bayesian inference.

If the source is promised to arise from a known efficiently simulable modular Hamiltonian, that is additional information. Quantum belief-propagation formulas and purified/block-encoding Esscher algorithms may use it. Our source interface supplies neither that dynamics nor a coherent preparation inverse. The [related-work account](../references/RELATED_WORK.md) explains these operational differences without treating an expensive conversion procedure as a universal lower bound.

## What is established and what remains open

The main result is a worst-case $\Omega(D)$ copy lower bound. The [constructive upper account](upper_bounds.md) gives a finite method under the same bounded-spectral-scale assumptions. Its larger cost leaves a quantitative gap; this project does not claim an optimal complete copy law.

The result does not establish that every noncommuting state is hard, that every state update requires tomography, or that a structured local Gibbs family has exponential sample cost. It also does not settle efficient gate synthesis, workspace optimality or practical hardware crossover. Unrestricted computation is allowed in the converse, while the constructive baseline separately pays its source, estimation and state-output costs.

The finite diagnostics verify constants, independent matrix formulas, same-spectrum commuting controls and selected Haar averages. The dimension-uniform theorem rests on the analytical proofs, rather than extrapolation from those experiments.
