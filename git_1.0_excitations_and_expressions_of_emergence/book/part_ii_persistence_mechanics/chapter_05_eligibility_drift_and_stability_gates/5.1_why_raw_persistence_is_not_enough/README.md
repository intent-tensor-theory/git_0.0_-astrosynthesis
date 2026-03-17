# 5.1 Why Raw Persistence Is Not Enough

## 5.1.1 Persistence alone does not guarantee survival

In Chapter 4 we derived the persistence condition

$$
S = \frac{R}{\dot{R}\,t_{ref}}.
$$

This equation determines whether retained structure exceeds structural loss during the persistence horizon.
However, persistence alone does not determine whether a structure can exist within the substrate.
Many configurations may satisfy

$$
S > 1
$$

yet never appear in the physical system.
This observation indicates that persistence must be supplemented by additional constraints.

## 5.1.2 The admissibility problem

Consider a configuration $\sigma$ with retained structure $R_\sigma$.
If

$$
S_\sigma > 1
$$

then the configuration should persist according to the persistence equation.
However, the configuration must also satisfy the structural rules of the substrate.
These rules may include:

- geometric compatibility
- topological admissibility
- conservation constraints
- boundary conditions

Configurations that violate these constraints cannot exist even if persistence is large.

## 5.1.3 Configuration space

Let $\Omega$ represent the set of all possible configurations of the system.
Within this space, define the subset $\Omega_{phys}$ that satisfies the physical constraints of the substrate.
Only configurations within this subset can appear in the system.
Thus

$$
\Omega_{phys} \subseteq \Omega.
$$

## 5.1.4 Persistence filtering

Persistence acts as a filter on configuration space.
Define the persistent set

$$
\Omega_{persist} = \{\sigma_i \in \Omega \mid S_i \geq 1\}.
$$

However, physical configurations must also satisfy admissibility constraints.
Thus the observable set becomes

$$
\Omega_{obs} = \Omega_{phys} \cap \Omega_{persist}.
$$

Only configurations in this intersection appear as real structures.

## 5.1.5 Example: forbidden configurations

Many systems exhibit configurations that are energetically stable but physically forbidden.
Examples include:

| System | Forbidden configuration |
|---|---|
| fluid flow | discontinuous velocity fields |
| electromagnetism | violation of Gauss's law |
| quantum mechanics | forbidden spin states |
| topological systems | broken invariants |

These configurations cannot occur even if their energy suggests stability.

## 5.1.6 Structural compatibility

Admissibility conditions arise from the underlying structure of the substrate.
For field systems these constraints often take the form of differential equations.
For example,

$$
\nabla \cdot \mathbf{B} = 0
$$

in electromagnetism.
Only field configurations satisfying this condition are allowed.
Thus admissibility acts as a structural filter.

## 5.1.7 Stability versus eligibility

Persistence measures stability, but stability does not guarantee eligibility.
We therefore distinguish two properties:

| Property | Meaning |
|---|---|
| stability | structure resists decay |
| eligibility | structure satisfies substrate rules |

Both properties must be satisfied for a configuration to exist.

## 5.1.8 Structural gates

The constraints that determine admissibility can be interpreted as structural gates.
Define a gate function $G(\sigma)$ that evaluates whether a configuration passes the necessary constraints.
If

$$
G(\sigma) = 1
$$

the configuration is allowed.
If

$$
G(\sigma) = 0
$$

the configuration is forbidden.

## 5.1.9 Sequential filtering

Emergence therefore occurs through sequential filters:

- structural gate filtering
- persistence filtering

The configuration must first satisfy

$$
G(\sigma) = 1
$$

and then satisfy

$$
S \geq 1.
$$

Only configurations satisfying both conditions become persistent structures.

## 5.1.10 Structural gates in the collapse ladder

The collapse ladder described earlier naturally introduces structural gates.

| Ladder stage | Gate condition |
|---|---|
| scalar | amplitude stability |
| gradient | spatial compatibility |
| circulation | rotational coherence |
| closure | boundary integrity |

Each stage imposes additional constraints on admissible configurations.

## 5.1.11 Structural filtering and emergence

The combined filtering process explains why many possible configurations never appear in physical systems.
The substrate continuously generates fluctuations across configuration space.
However, only a small subset of configurations satisfy both

$$
G(\sigma) = 1
$$

and

$$
S \geq 1.
$$

These configurations form the set of persistent structures.

## 5.1.12 Summary

Persistence alone cannot determine structural survival.
A configuration must also satisfy the admissibility constraints of the substrate.
Thus emergence occurs through two filters:

- structural eligibility
- persistence selection

These concepts will be formalized mathematically in the following sections.

*Transition to Section 5.2:* The Eligibility Operator introduces a formal operator that determines whether configurations satisfy the structural constraints of the substrate.
