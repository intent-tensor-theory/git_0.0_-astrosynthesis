# 5.2 The Eligibility Operator

## 5.2.1 From structural gates to operators

In the previous section we introduced the concept of structural gates. These gates determine whether a configuration is admissible within the substrate.
We now formalize this idea mathematically by introducing an eligibility operator.
Let $\sigma$ represent a configuration in configuration space $\Omega$.
The eligibility operator $\mathcal{E}$ acts on configurations to determine whether they satisfy the structural constraints of the substrate.

## 5.2.2 Definition of the eligibility operator

The eligibility operator is defined as

$$
\mathcal{E}(\sigma) =
\begin{cases}
1 & \text{if configuration is admissible} \\
0 & \text{if configuration violates constraints}
\end{cases}
$$

Thus the operator maps the configuration space into the set $\{0,1\}$.
Configurations for which

$$
\mathcal{E}(\sigma) = 1
$$

pass the structural gate.

## 5.2.3 Eligible configuration set

Using the eligibility operator we define the set of admissible configurations

$$
\Omega_{eligible} = \{\sigma \in \Omega \mid \mathcal{E}(\sigma) = 1\}.
$$

Only configurations belonging to this set can exist in the substrate.
Thus the physical configuration space becomes

$$
\Omega_{phys} = \Omega_{eligible}.
$$

## 5.2.4 Constraints defining eligibility

The eligibility operator encodes the structural constraints imposed by the underlying system.
Typical constraints include:

**Differential constraints.**
Field configurations must satisfy differential equations.
Example:

$$
\nabla \cdot \mathbf{B} = 0
$$

in electromagnetism.

**Topological constraints.**
Certain structures possess conserved topological invariants.
Example:

$$
Q = \int \mathbf{A} \cdot (\nabla \times \mathbf{A})\, d^3x
$$

which defines helicity in fluid systems.

**Symmetry constraints.**
Configurations must respect the symmetry group of the substrate.
Example:

$$
\Phi \rightarrow -\Phi
$$

in systems with parity symmetry.

**Boundary constraints.**
Structures must satisfy boundary conditions.
Example:

$$
\Phi|_{\partial V} = 0.
$$

## 5.2.5 Eligibility as a projection operator

The eligibility operator can be interpreted as a projection onto the admissible subspace.
Define $\mathcal{P}_{eligible}$.
Then

$$
\mathcal{P}_{eligible}\,\sigma =
\begin{cases}
\sigma & \text{if admissible} \\
0 & \text{otherwise}
\end{cases}
$$

This operator removes configurations that violate substrate constraints.

## 5.2.6 Eligibility in field systems

For field systems, eligibility may be expressed through functional constraints.
Let

$$
C_i[\Phi] = 0
$$

represent a set of constraint equations.
Then

$$
\mathcal{E}(\Phi) =
\prod_i \delta(C_i[\Phi]).
$$

Here $\delta$ denotes the Dirac delta function, enforcing the constraint.
Thus only fields satisfying the constraints contribute to the admissible configuration space.

## 5.2.7 Eligibility and structural complexity

As the collapse ladder introduces additional structural features, the eligibility operator becomes more restrictive.
For example:

| Structural level | Eligibility condition |
|---|---|
| scalar | amplitude stability |
| gradient | differentiability |
| circulation | vorticity continuity |
| closure | boundary smoothness |

Each level introduces new constraints.

## 5.2.8 Eligibility and topology

Topology plays an important role in eligibility.
Certain structures cannot transform continuously into others.
For example:

- vortex number
- winding number
- knot number

Define the topological invariant $Q(\sigma)$.
If the substrate allows only specific values of $Q$, the eligibility operator enforces

$$
\mathcal{E}(\sigma) = 0
\quad
\text{when}
\quad
Q(\sigma) \notin \mathcal{Q}_{allowed}.
$$

## 5.2.9 Interaction with persistence

Eligibility alone does not guarantee persistence.
Thus we combine eligibility with the selection number derived earlier.
The persistence condition becomes

$$
S_* =
\mathcal{E}(\sigma)\,
\frac{R}{\dot{R}\,t_{ref}}.
$$

Thus if

$$
\mathcal{E}(\sigma) = 0
$$

then

$$
S_* = 0
$$

regardless of the value of $S$.

## 5.2.10 Geometric interpretation

In configuration space, the eligibility operator restricts motion to a subset of allowed configurations.
The persistent structures therefore lie in the intersection

$$
\Omega_{persist} =
\{\sigma \mid \mathcal{E}(\sigma)=1\}
\cap
\{\sigma \mid S \geq 1\}.
$$

This intersection defines the observable structural manifold.

## 5.2.11 Eligibility and emergent structures

Many emergent structures arise precisely because eligibility constraints restrict the system to particular configurations.
Examples include:

| System | Emergent structure |
|---|---|
| fluid dynamics | vortices |
| condensed matter | solitons |
| field theory | topological defects |
| cosmology | domain walls |

These structures appear when admissible configurations satisfy persistence conditions.

## 5.2.12 Summary

The eligibility operator $\mathcal{E}$ defines the admissible configuration space of the substrate.
Configurations must satisfy

$$
\mathcal{E}(\sigma)=1
$$

to exist.
Combined with the persistence condition

$$
S = \frac{R}{\dot{R}\,t_{ref}},
$$

this operator determines which configurations can survive as persistent structures.

*Transition to Section 5.3:* Drift Stability derives the mathematical condition under which configurations remain localized in configuration space rather than drifting toward dissipative states.
