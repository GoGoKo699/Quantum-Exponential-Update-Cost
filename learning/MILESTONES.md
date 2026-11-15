# Thirty milestones for Quantum Exponential Update Cost

This map follows one question: how many specimens of an unknown quantum prior are needed to produce one normalized exponential-update state? Its central distinction is between the known spectrum of the prior and its unknown orientation relative to a known, bounded tilt.

The single educational anchor is John Watrous, *The Theory of Quantum Information* (2018), available through the [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/). The relevant chapters are:

| Chapter | Foundation used here |
| --- | --- |
| 1, Mathematical preliminaries | Operators, spectral decompositions, tensor products and operator norms |
| 2, Basic notions of quantum information | States, channels, measurements, instruments and composite systems |
| 3, Similarity and distance among states and channels | Trace distance, distinguishability and contraction under physical processing |
| 5, Quantum entropy and source coding | Quantum relative entropy and its information-theoretic meaning |
| 7, Permutation invariance and unitarily invariant measures | Haar averages, permutation symmetry and unitary symmetry |

These chapter pointers supply foundations. The Esscher-response calculation, the Schur–Weyl reduction with the particular O'Donnell–Wright testing bound, and the constructive tomography estimates are research-level ingredients supplied or attributed in the project sources; they are not asserted to follow from reading the anchor alone.

The allocation is **12 background milestones and 18 narrative milestones**. The background builds from individual states and operations to the complete resource contract. The narrative builds from two concrete prior ensembles to a finite response witness, a collective-information converse and the constructive upper bounds. This gives the unfamiliar matrix-update operation and its access conventions enough preparation while keeping most milestones focused on the contribution. The map identifies understanding targets and their dependencies; the scientific files retain the full proofs and technical details.

## Phase I — Background and preliminaries, M01–M12

### M01 — A state, its spectrum and its specimens

- **Central question:** What information does a density operator describe, and what remains unknown when its eigenvalues are supplied?
- **Understanding target:** Distinguish a state from a classical matrix description, and its eigenvalues from its eigenspaces. Explain why many copies of the same unknown state do not come with its orientation.
- **Dependencies and story role:** Starting point; introduces the object that the source repeatedly supplies.
- **Conceptual connection:** The two-level family has fixed eigenvalues but many possible orientations, so knowing its spectrum leaves the central uncertainty intact.
- **Source pointers:** Watrous, Chapters 1–2; [model: supplied information](../science/model.md#supplied-information).

### M02 — One local observable in a large register

- **Central question:** How can a measurement on one qubit reveal a property of a state on many qubits?
- **Understanding target:** Explain expectation values and the balanced operator $Z$, and identify $Z=Z_1\otimes I$ when $D=2^q$. A local measurement can read a response influenced by globally unknown eigenspaces.
- **Dependencies and story role:** Uses M01; connects an individual specimen to the simple output statistic used throughout the proof.
- **Conceptual connection:** The theorem requires only one updated state and tests only one known observable, despite the large source dimension.
- **Source pointers:** Watrous, Chapters 1–2; [model: supplied information](../science/model.md#supplied-information); [response: family and observable](../science/response.md#the-family-and-the-observable).

### M03 — Copies and coherent access are different resources

- **Central question:** Which operations become available when a source supplies copies, and which require an additional interface?
- **Understanding target:** Distinguish independent specimens from a callable preparation unitary, its inverse, a purification oracle, a block encoding and evolution under $\log\rho$. Explain why none of these interfaces can be silently substituted for another.
- **Dependencies and story role:** Uses M01–M02; fixes what an algorithm may ask the source to provide.
- **Conceptual connection:** The lower bound concerns an unknown prior supplied as copies, while some existing Esscher algorithms assume stronger coherent access.
- **Source pointers:** Watrous, Chapter 2; [model: supplied information](../science/model.md#supplied-information); [related work: quantum Esscher transform](../references/RELATED_WORK.md#the-quantum-esscher-transform).

### M04 — Physical processing, flags and discarded registers

- **Central question:** How are measurements, random outcomes and discarded systems represented within one quantum operation?
- **Understanding target:** Explain a quantum channel, a two-outcome instrument and a state marginal. Recognize that conditioning on a success flag differs from averaging over all outcomes.
- **Dependencies and story role:** Uses M01–M03; provides the language for both the processor and the inexpensive filtering construction.
- **Conceptual connection:** A valid lower bound must include adaptive collective processing; a valid upper bound must count rejected specimens and specify its final output.
- **Source pointers:** Watrous, Chapter 2; [model: required output and budget](../science/model.md#required-output-and-budget); [baselines: bounded filter](../science/baselines.md#a-bounded-filter-with-charged-attempts).

### M05 — Output error and the ability to distinguish states

- **Central question:** What operational change can a small half trace distance permit?
- **Understanding target:** Use the convention $T(\rho,\sigma)=\|\rho-\sigma\|_1/2$. Explain why a norm-one observable changes by at most $2T$, and why a channel cannot increase input trace distance.
- **Dependencies and story role:** Uses M02 and M04; supplies the error and information rules that later connect an output response to an input-copy obstruction.
- **Conceptual connection:** Two output errors of size $\epsilon$ can reduce a response gap by $4\epsilon$; the factor follows from the stated distance convention.
- **Source pointers:** Watrous, Chapter 3; [model: normalized update and error convention](../science/model.md#the-normalized-esscher-update); [converse: proof of the known-spectrum theorem](../science/copy_lower_bound.md#proof-of-the-known-spectrum-theorem).

### M06 — Functions of matrices and a scalar that cancels

- **Central question:** How are $\log\rho$ and $e^A$ defined, and why does operator order matter?
- **Understanding target:** Read matrix functions through a spectral decomposition. Distinguish a scalar identity shift, which cancels after normalization, from a noncommuting operator contribution, which cannot be rearranged as if it were a number.
- **Dependencies and story role:** Uses M01; introduces the mathematical operation defining the desired output.
- **Conceptual connection:** For the two-level family, $\log\rho_S$ is a scalar identity term plus $(\operatorname{atanh}a)S$. Removing the scalar does not supply the unknown operator $S$.
- **Source pointers:** Watrous, Chapter 1; [model: normalized Esscher update](../science/model.md#the-normalized-esscher-update); [response: family and observable](../science/response.md#the-family-and-the-observable); [finite diagnostics](../verification/README.md).

### M07 — Why this exponential update is an inference target

- **Central question:** Which optimization problem selects the normalized Esscher state?
- **Understanding target:** Interpret the identity involving $D(\sigma\Vert\rho)-\operatorname{Tr}(H\sigma)$ and explain why normalization produces the unique minimum-relative-entropy update for a supplied tilt.
- **Dependencies and story role:** Uses M05–M06; gives the target an operational and variational purpose.
- **Conceptual connection:** The tilt $H$ is supplied. Solving for a multiplier from a prescribed expectation constraint is a separate task.
- **Source pointers:** Watrous, Chapter 5; [model: normalized Esscher update](../science/model.md#the-normalized-esscher-update); [related work: quantum Esscher transform](../references/RELATED_WORK.md#the-quantum-esscher-transform).

### M08 — Bounded filtering and its commuting limit

- **Central question:** How does a bounded change of weights become a physical accept-or-reject procedure?
- **Understanding target:** Explain the success operator $K=e^{(H-hI)/2}$, the lower success bound $e^{-2h}$, and the accepted sandwich state. Identify the commutation condition under which it is the Esscher state.
- **Dependencies and story role:** Uses M04 and M06–M07; supplies a complete inexpensive comparison before the harder result is introduced.
- **Conceptual connection:** Classical exponential rejection sampling and commuting quantum updating share this mechanism; the general quantum sandwich filter is also inexpensive.
- **Source pointers:** Watrous, Chapters 1–2; [baselines: bounded filter](../science/baselines.md#a-bounded-filter-with-charged-attempts); [baselines: commuting equality](../science/baselines.md#when-the-filter-is-the-esscher-update).

### M09 — Susceptibility measures the start of a response

- **Central question:** What does the derivative of an output expectation tell us about a small tilt?
- **Understanding target:** Interpret the partition function $F(t)$, the response $m(t)=(\log F)'(t)$, and the susceptibility $m'(0)$. Explain why noncommutativity introduces logarithmic means into the derivative.
- **Dependencies and story role:** Uses M02, M06 and M07; provides the local response language needed to construct a finite witness.
- **Conceptual connection:** A derivative suggests the mechanism, but the theorem will require a controlled gap at a fixed nonzero tilt.
- **Source pointers:** Watrous, Chapter 1 for matrix foundations; [response: partition-function control](../science/response.md#uniform-control-of-the-finite-update); [response: exact susceptibility](../science/response.md#the-exact-susceptibility).

### M10 — A random ensemble can bound a fixed unknown input

- **Central question:** Why may a worst-case lower bound average over Haar-random orientations?
- **Understanding target:** Distinguish averaging over possible fixed priors from redrawing a prior between source requests. Explain why a processor promised to work for every orientation must also work after averaging its pointwise guarantee.
- **Dependencies and story role:** Uses M01, M04–M05; introduces the proof's statistical construction without altering the source model.
- **Conceptual connection:** Haar symmetry simplifies the response and the input-copy information, while the actual orientation remains fixed throughout each execution.
- **Source pointers:** Watrous, Chapter 7; [model: supplied information](../science/model.md#supplied-information); [response: exact susceptibility](../science/response.md#the-exact-susceptibility); [converse: known-spectrum proof](../science/copy_lower_bound.md#proof-of-the-known-spectrum-theorem).

### M11 — Collective measurements and simultaneous symmetries

- **Central question:** What information survives when an ensemble is invariant under both global unitary rotations and permutations of its copies?
- **Understanding target:** Explain the purpose of Schur–Weyl blocks and why simultaneous invariance makes the relevant averaged states scalar on each block. Recognize that a classical distribution of block weights can then contain all their distinguishability.
- **Dependencies and story role:** Uses M01, M03–M05 and M10; prepares the information-theoretic ingredient while retaining arbitrary collective measurements.
- **Conceptual connection:** The lower bound will use a quantitative bound on these weights rather than a restriction to separate measurements on individual copies.
- **Source pointers:** Watrous, Chapter 7 and Chapter 3; [converse: inherited mixedness bound](../science/copy_lower_bound.md#the-inherited-mixedness-testing-bound).

### M12 — The complete update contract

- **Central question:** What exactly must one successful processor do, and which resources are counted?
- **Understanding target:** Assemble the promise of one fixed unknown prior, supplied exact spectrum, known local tilt, one normalized output marginal, uniform half trace error and a charged copy budget. Distinguish copy complexity from gate, storage and output-description costs.
- **Dependencies and story role:** Integrates M01–M11 and closes the background phase with the full task rather than another isolated prerequisite.
- **Conceptual connection:** The theorem fixes $a=0.8$, $h=0.1$, $\epsilon=0.001$ and allows unrestricted collective computation. The narrative must therefore find an obstruction in the supplied specimens themselves.
- **Source pointers:** Watrous, Chapters 2–3; [model](../science/model.md); [upper bounds: output convention](../science/upper_bounds.md#promise-and-output-convention).

## Phase II — Narrative and contribution, M13–M30

### M13 — Two orientations with one supplied spectrum

- **Central question:** How can two ensembles differ when every input has the same known eigenvalues and entropy?
- **Understanding target:** Construct the full-Haar ensemble and the ensemble with independent balanced involutions inside the two known $Z$ sectors. Explain why $D$ must be divisible by four, why both ensembles belong to the same unitary orbit, and what differs about their orientation.
- **Dependencies and story role:** Uses M01, M10 and M12; begins the contribution with its two concrete source families.
- **Conceptual connection:** The comparison removes spectral side information as an explanation for the hardness and isolates orientation relative to the tilt.
- **Source pointers:** Watrous, Chapters 1 and 7; [converse: known-spectrum task](../science/copy_lower_bound.md#the-known-spectrum-task); [converse: two ensembles](../science/copy_lower_bound.md#proof-of-the-known-spectrum-theorem).

### M14 — The commuting ensemble has a fixed response

- **Central question:** Why does every block-commuting prior give the same output expectation $\tanh h$?
- **Understanding target:** Use equal weight in the two $Z$ sectors, commutation with the tilt, and normalization of the exponential weights to obtain the response without learning either block's eigenbasis.
- **Dependencies and story role:** Uses M02, M08 and M13; supplies one exactly calculable side of the response comparison.
- **Conceptual connection:** This ensemble both shares the main theorem's supplied spectrum and admits the inexpensive physical filter.
- **Source pointers:** Watrous, Chapters 1–2; [baselines: the two hard ensembles](../science/baselines.md#the-two-hard-ensembles); [converse: known-spectrum proof](../science/copy_lower_bound.md#proof-of-the-known-spectrum-theorem).

### M15 — Hidden orientation suppresses mean susceptibility

- **Central question:** How does averaging the noncommuting response produce a deficit from the commuting slope?
- **Understanding target:** Connect logarithmic means, the Haar second moments and subtraction of the squared initial expectation to the exact formula $c_D(a)=[D^2c(a)-1-a^2]/(D^2-1)$, with $c(a)<1$.
- **Dependencies and story role:** Uses M09–M10 and M13–M14; identifies the local mechanism that separates the output responses.
- **Conceptual connection:** The exact finite-dimensional calculation avoids assuming a typical orientation or replacing the Haar mean by its large-dimension limit.
- **Source pointers:** Watrous, Chapter 7 for Haar invariance; [response: exact susceptibility](../science/response.md#the-exact-susceptibility); [finite diagnostics](../verification/README.md).

### M16 — A uniform remainder makes local response useful

- **Central question:** How can a derivative calculation control an actual finite update in every dimension?
- **Understanding target:** Explain how the iterated Duhamel formula and Schatten Hölder bound give $|F^{(k)}|\le F$, and how the fourth derivative of $\log F$ yields the sufficient bound $|m'''|\le26$.
- **Dependencies and story role:** Uses M06, M09 and M15; supplies the missing connection between infinitesimal response and the fixed task.
- **Conceptual connection:** The bound is uniform in the unknown prior and the dimension; a finite numerical check is useful for implementation diagnostics but cannot replace this argument.
- **Source pointers:** Watrous, Chapter 1 for operator foundations; [response: partition-function derivatives](../science/response.md#uniform-control-of-the-finite-update); [verification scope](../verification/README.md).

### M17 — A response gap at fixed tilt and fixed error

- **Central question:** What survives of the susceptibility deficit at the theorem's nonzero evidence strength?
- **Understanding target:** Combine Haar oddness, the cubic Taylor remainder and $\tanh h\ge h-h^3/3$ to obtain $g(a,h)=[1-c(a)]h-14h^3/3$. Explain why $g>0.0089237$ at the fixed parameters is enough after allowing $4\epsilon$ of response error.
- **Dependencies and story role:** Uses M05 and M14–M16; completes the output-side witness.
- **Conceptual connection:** The proof uses fixed evidence strength and fixed output tolerance, with no dimension-dependent precision limit or individual-input concentration claim.
- **Source pointers:** Watrous, Chapter 3 for the error interpretation; [response: finite gap](../science/response.md#a-response-gap-at-fixed-evidence-strength); [converse: fixed constants](../science/copy_lower_bound.md#fixed-constants).

### M18 — The inherited bound on hidden mixedness

- **Central question:** Which quantitative information bound is imported from spectrum testing?
- **Understanding target:** State the alternating-spectrum O'Donnell–Wright chi-squared bound, substitute its parameter $\eta=a/2$, and recognize the function $B_d(n)=\frac12\sqrt{e^{(na^2/d)^2}-1}$. Distinguish this particular ensemble bound from a generic verbal assertion that mixedness testing is hard.
- **Dependencies and story role:** Uses M05, M10–M11 and M13; introduces the input-side obstruction with its exact operational promise.
- **Conceptual connection:** The spectrum-testing theorem is inherited. Its quantitative small-bias form is what can support the update witness's small fixed response gap.
- **Source pointers:** Watrous, Chapters 3 and 7; [converse: inherited mixedness bound](../science/copy_lower_bound.md#the-inherited-mixedness-testing-bound); [attribution](../references/RELATED_WORK.md#mixedness-testing-supplies-the-information-bound).

### M19 — From Schur weights to unrestricted input distinguishability

- **Central question:** Why does a bound on a classical Schur distribution constrain every collective quantum procedure?
- **Understanding target:** Use simultaneous unitary and permutation invariance to identify scalar blocks, equate half trace distance with the total variation of block weights, and apply Cauchy–Schwarz to convert chi-squared divergence to $B_d(n)$.
- **Dependencies and story role:** Uses M05, M11 and M18; turns the imported distributional theorem into the quantum input-state bound actually needed.
- **Conceptual connection:** The reduction includes arbitrary collective measurements rather than selecting an experimentally convenient but weaker measurement class.
- **Source pointers:** Watrous, Chapter 7 and Chapter 3; [converse: Schur–Weyl reduction](../science/copy_lower_bound.md#the-inherited-mixedness-testing-bound).

### M20 — The commuting ensemble also hides its information

- **Central question:** Why is the easy-to-update commuting ensemble nevertheless hard to distinguish from the full-Haar ensemble using few copies?
- **Understanding target:** Decompose its $n$-copy state into orthogonal $Z$-sector words, identify two independent lower-dimensional Haar averages conditioned on each word, and obtain the bound $B_D(n)+2B_{D/2}(n)$ by product and triangle inequalities.
- **Dependencies and story role:** Uses M13–M14 and M18–M19; supplies the critical same-spectrum input comparison.
- **Conceptual connection:** The maximally mixed state is a reference used inside the proof. It is not one of the two main promised input ensembles and need not share their spectrum.
- **Source pointers:** Watrous, Chapters 2–3 and 7; [converse: sector-word decomposition and triangle bound](../science/copy_lower_bound.md#proof-of-the-known-spectrum-theorem).

### M21 — The response witness becomes a copy lower bound

- **Central question:** What contradiction would a processor with too few copies create?
- **Understanding target:** Combine the target mean gap, the two output-error allowances and channel contraction to obtain $g-4\epsilon\le2B_D(n)+4B_{D/2}(n)$. Explain the sufficient linear bound and the main conclusion $n>10^{-3}D$.
- **Dependencies and story role:** Integrates M12–M20; establishes the main theorem from the output witness and the input information bound.
- **Conceptual connection:** One normalized state would make a known observable informative before the supplied specimens contain enough distinguishability. For $D=2^q$, the linear dimension cost is exponential in qubit count.
- **Source pointers:** Watrous, Chapter 3; [converse: main theorem](../science/copy_lower_bound.md#main-theorem); [converse: proof](../science/copy_lower_bound.md#proof-of-the-known-spectrum-theorem); [model: main result](../science/model.md#main-result).

### M22 — Adaptive computation still fits the hard-budget theorem

- **Central question:** Can adaptive source requests, quantum memory or extra output registers evade the channel formulation?
- **Understanding target:** Represent a protocol with a hard cap of $n$ source requests by a channel on $n$ copies supplied in advance. Include its classical record and discarded systems, then take the designated output marginal.
- **Dependencies and story role:** Uses M03–M05, M12 and M21; checks that the converse covers the generous computational permissions of the stated task.
- **Conceptual connection:** The lower bound charges source access while granting computation and collective memory. It does not derive from a circuit-depth, workspace or separate-measurement restriction.
- **Source pointers:** Watrous, Chapter 2 and Chapter 3; [model: output and budget](../science/model.md#required-output-and-budget); [converse: channel model](../science/copy_lower_bound.md).

### M23 — Heralding and expected cost need uniform guarantees

- **Central question:** How does the result change when a protocol may fail or consume a variable number of copies?
- **Understanding target:** Explain bounded repetition for success probability uniformly bounded below and truncation by Markov's inequality for a uniformly bounded expected copy cost. Keep conditional error, total failure and the changed lower-bound constants distinct.
- **Dependencies and story role:** Uses M04–M05 and M21–M22; extends the resource conclusion without treating postselection as free.
- **Conceptual connection:** Fixed-probability heralding and uniform expected budgets retain an $\Omega(D)$ obstruction. A small conditional error alone supplies no success-cost guarantee.
- **Source pointers:** Watrous, Chapters 2–3; [converse: heralded and expected-copy variants](../science/copy_lower_bound.md#heralded-output-and-expected-copy-variants).

### M24 — Why the larger two-spectrum constant is a different statement

- **Central question:** Why can the maximally mixed comparison give a larger coefficient without strengthening the known-spectrum theorem by that amount?
- **Understanding target:** Explain the two-spectrum intermediate bound $n>0.00769D$ and why revealing the actual spectrum would identify its two hypotheses. Preserve the main theorem's same-spectrum premise when quoting results.
- **Dependencies and story role:** Uses M13 and M18–M21; clarifies the logical role of an intermediate result and prevents an incorrect transfer of its stronger numerical coefficient.
- **Conceptual connection:** A proof reference may have different side information from the actual source promise, so coefficients and guarantees must stay attached to their respective tasks.
- **Source pointers:** Watrous, Chapters 2–3; [converse: two-spectrum intermediate](../science/copy_lower_bound.md#a-two-spectrum-intermediate-with-a-larger-numerical-coefficient); [science guide](../science/README.md).

### M25 — The inexpensive filter passes the right comparison

- **Central question:** Why does a five-copy filtering construction coexist with the lower bound?
- **Understanding target:** Identify the accepted sandwich state, count all attempts, and use a noncommuting qubit to see that it need not be the Esscher target. Explain both the commuting equality and the failure probability $(1-e^{-0.2})^5<0.001$.
- **Dependencies and story role:** Uses M06–M08, M14 and M21; revisits the constructive comparison after the theorem so that the operation being bounded stays explicit.
- **Conceptual connection:** The same local evidence admits a cheap physical filter for every input. The obstruction concerns the particular noncommuting relative-entropy update, rather than all quantum inference.
- **Source pointers:** Watrous, Chapter 2; [filtering baselines](../science/baselines.md); [finite counterexample and controls](../verification/README.md).

### M26 — Stability under an estimated prior

- **Central question:** If a prior is estimated accurately, can its exponential update also be approximated accurately?
- **Understanding target:** Follow the trace-norm stability argument under $(c/D)I\preceq\rho\preceq(C/D)I$, including the logarithm resolvent, exponential difference and normalization. Identify $L=2(C/c)e^{2h}$ and its fixed-parameter role.
- **Dependencies and story role:** Uses M05–M07 and M12; begins the constructive account with the control needed to use a paid state estimate.
- **Conceptual connection:** The spectral floor scales naturally as $1/D$. A bounded ordinary eigenvalue ratio does not grant an inverse-minimum-eigenvalue oracle or make the source known.
- **Source pointers:** Watrous, Chapters 1 and 3; [upper bounds: spectral promise](../science/upper_bounds.md#promise-and-output-convention); [upper bounds: stability lemma](../science/upper_bounds.md#stability-under-a-trace-norm-estimate).

### M27 — Repairing a tomographic estimate before taking its logarithm

- **Central question:** How can every measurement outcome yield a defined positive-prior update, including an inaccurate estimate?
- **Understanding target:** Project an estimate into the trace-one set with the promised spectral bounds. Explain the factor-two error guarantee and why pinching permits a minimizer in the estimate's eigenbasis.
- **Dependencies and story role:** Uses M01, M05–M06 and M26; makes the upper-bound construction well-defined on every branch.
- **Conceptual connection:** Averaged output error does not justify ignoring rare invalid estimates; spectral repair controls them before the nonlinear matrix operation.
- **Source pointers:** Watrous, Chapters 1 and 3; [upper bounds: restoring the spectral promise](../science/upper_bounds.md#restoring-the-spectral-promise-after-tomography).

### M28 — A collective-copy upper bound

- **Central question:** What does a general tomography-based construction achieve when collective processing is allowed?
- **Understanding target:** Combine the inherited Frobenius-risk bound, spectral repair, trace-norm stability and convexity to obtain $O(L^2D^2/\epsilon^2)$ source copies. Include calculation and preparation of one output state in the task.
- **Dependencies and story role:** Uses M04–M05 and M26–M27; establishes attainability with quadratic dimension dependence at fixed parameters.
- **Conceptual connection:** A collective-copy upper bound is not automatically a polynomial-gate or small-memory implementation of the tomographic measurement.
- **Source pointers:** Watrous, Chapters 2–3; [upper bounds: collective construction](../science/upper_bounds.md#collective-copy-upper-bound); [upper-bound attribution](../references/RELATED_WORK.md#constructive-tomography-baselines).

### M29 — An explicit independent-copy construction and its paid costs

- **Central question:** What changes when the measurement stage is made concrete one specimen at a time?
- **Understanding target:** Explain the random-Clifford estimator, its larger Frobenius risk and the resulting $O(L^2D^3/\epsilon^2)$ copy baseline. Account for dense classical storage, matrix arithmetic, generic vector preparation and rotation synthesis.
- **Dependencies and story role:** Uses M02–M04, M26–M28; connects the abstract upper result to an explicit implementation with distinct costs.
- **Conceptual connection:** No QRAM or unknown-state preparation inverse is supplied. Operations polynomial in $D$ remain expensive in $q=\log_2D$, and the cubic copy baseline is not a matching lower-bound construction.
- **Source pointers:** Watrous, Chapters 1–2 for states and measurements; [upper bounds: independent-copy baseline](../science/upper_bounds.md#a-concrete-single-copy-measurement-baseline); [upper bounds: remaining gap](../science/upper_bounds.md#what-these-upper-bounds-do-and-do-not-settle).

### M30 — The full result, its evidence and its open frontier

- **Central question:** What can now be concluded about updating an unknown prior, and what remains unestablished?
- **Understanding target:** Assemble the supplied-spectrum orientation obstruction, fixed local tilt, normalized state output, $\Omega(D)$ lower bound, quadratic collective upper bound and cubic explicit baseline. Explain the open gap, the inherited ingredients, the role of finite diagnostics, and the absence of a universal claim about structured local Gibbs sources or all noncommuting states.
- **Dependencies and story role:** Integrates M13–M29 with the complete contract in M12; closes the narrative with the scientific consequence and its actual limits.
- **Conceptual connection:** The response witness is the task-specific bridge from established testing hardness to this transformation cost. Finite checks support their stated cases; analytical arguments establish the dimension-uniform theorem. Known modular dynamics or stronger coherent source access changes the task.
- **Source pointers:** Watrous, Chapters 2–3, 5 and 7 as the combined foundation; [interpretation](../science/interpretation.md); [related work](../references/RELATED_WORK.md); [upper-bound gap](../science/upper_bounds.md#what-these-upper-bounds-do-and-do-not-settle); [verification scope](../verification/README.md).

The map ends at a connected understanding of this scoped result. It does not claim to cover every technical lemma, certify the proofs through the finite checks, or resolve the remaining copy-complexity gap.
