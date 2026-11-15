# Learning the exponential-update problem

[Project overview](../README.md) · [Watrous bridge](WATROUS_BRIDGE.md) · [30 milestones](MILESTONES.md) · [Complete science](../science/README.md)

The learning route uses **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**. The [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/) identifies this edition and provides its chapter structure. The source remains with its author and publisher; the explanations here connect its foundations to this project's result.

Begin with the [worked qubit example](WATROUS_BRIDGE.md#a-complete-qubit-example). It shows why applying a known filter and adding the same evidence to the logarithm of a state give different outputs. Then follow the [bridge](WATROUS_BRIDGE.md) into the copy model, discrimination and hidden orientation. The [30 milestones](MILESTONES.md) form one continuous route through those ideas and the proof.

The endpoint is a precise claim: even with the input spectrum supplied exactly, one normalized exponential-update output can require a number of source copies proportional to the Hilbert-space dimension. The hard inputs are full rank, the spectral ratio is nine, the tilt is fixed and known, and the output tolerance is fixed. The proof allows collective processing and arbitrary memory.

Watrous supplies the language of states, channels, measurements, discrimination and unitary symmetry. The project supplies the matrix-response calculation, the exact use of O'Donnell–Wright's mixedness bound, and the resulting update-cost theorem. These additions are identified in the [bridge](WATROUS_BRIDGE.md#what-the-project-adds-to-the-anchor) and [related-work account](../references/RELATED_WORK.md).

The route ends with the scope and the unresolved gap: the lower bound is linear in dimension, while the general collective-tomography upper bound is quadratic at fixed accuracy. Neither a matching algorithm nor a practical hardware advantage is established.
