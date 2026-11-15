# Commuting updates and ordinary quantum filters

The expensive target is the exponential update defined in the [model](model.md). A different, physically elementary quantum update stays inexpensive for every input state. Comparing the two isolates the role of noncommutativity.

## A bounded filter with charged attempts

Suppose $\lVert H\rVert\le h$ and apply the success Kraus operator

$$
K=\exp\!\left(\frac{H-hI}{2}\right).
$$

Because $K^\dagger K=\exp(H-hI)\le I$, this is a valid two-outcome instrument. Its success probability and accepted state are

$$
p_H(\rho)=\mathrm{Tr}(e^{H-hI}\rho)\ge e^{-2h},
\qquad
\mathcal F_H(\rho)=
\frac{e^{H/2}\rho e^{H/2}}{\mathrm{Tr}(e^H\rho)}.
$$

The filter consumes one input copy per attempt. Repeating on fresh copies until success uses at most $e^{2h}$ copies in expectation. With a hard cap of $r$ attempts, output a fixed fallback state if all fail. The unconditional output then has half-trace distance at most

$$
(1-e^{-2h})^r
$$

from $\mathcal F_H(\rho)$, uniformly in dimension and input. Rejected specimens are included in this count.

For the theorem's $H=0.1Z_1$, the filter is diagonal on one qubit. A controlled rotation of one flag qubit realizes its acceptance amplitudes $1$ and $e^{-0.1}$. The remaining register is untouched by the known filter. Finite gate-rotation synthesis adds its actual precision cost; fixed target accuracy requires only a fixed synthesis accuracy and no data-loading oracle.

Numerically, five attempts have failure probability

$$
(1-e^{-0.2})^5<0.000196<0.001.
$$

The ideal-gate five-copy statement is exact. A hardware implementation allocates the available accuracy slack to its flag rotation and measurements.

## When the filter is the Esscher update

If $[\rho,H]=0$, then

$$
e^{\log\rho+H}=e^H\rho=e^{H/2}\rho e^{H/2},
\qquad \mathcal E_H(\rho)=\mathcal F_H(\rho).
$$

Thus commuting Esscher updating admits the same dimension-independent copy bounds. The processor does not need the eigenbasis or a classical description of $\rho$; it applies the known-$H$ filter directly.

For a classical source with probabilities $p(x)$ and evaluable bounded tilt $H(x)$, the corresponding rejection rule accepts an observed label $x$ with probability $e^{H(x)-h}$. Its accepted distribution is the classical Esscher update. Evaluation and label acquisition have their actual classical costs; they are not coherent-access assumptions.

## Why filtering does not solve the noncommuting task

For general inputs the two maps differ:

$$
\mathcal E_H(\rho)=\frac{e^{\log\rho+H}}{\mathrm{Tr}e^{\log\rho+H}},
\qquad
\mathcal F_H(\rho)=\frac{e^{H/2}\rho e^{H/2}}{\mathrm{Tr}(e^H\rho)}.
$$

Their classical coincidence is inherited; it is not a proposed matrix identity for noncommuting operators. The [finite checks](../verification/README.md) include a direct noncommuting counterexample and commuting controls. The copy lower bound applies to $\mathcal E_H$, while the construction above implements $\mathcal F_H$.

## The two hard ensembles

In the [converse](copy_lower_bound.md), all inputs have the same supplied spectrum. In the commuting ensemble, $S$ is block diagonal in the two eigenspaces of $Z$, with a balanced involution in each block. Consequently

$$
\mathrm{Tr}(\rho_S Z)=0,
\qquad
\mathrm{Tr}\!\left(Z\mathcal E_{hZ}(\rho_S)\right)=\tanh h.
$$

A fully Haar-oriented state has a smaller mean Esscher response. The ordinary filter has no such mean obstruction: it can be applied to either ensemble using the same constant-copy instrument. The theorem distinguishes two update operations and two orientation regimes, rather than declaring all quantum inference expensive.
