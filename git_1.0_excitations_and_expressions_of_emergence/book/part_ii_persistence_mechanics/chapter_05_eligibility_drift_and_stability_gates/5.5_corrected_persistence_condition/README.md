# 5.5 Corrected Persistence Condition

## 5.5.1 Motivation

Chapters 4 and 5 introduced the mathematical ingredients that determine whether a structure can survive within the Collapse Tension Substrate:
retained structure (R)
structural loss rate ( $\dot R)$
persistence horizon (t_{ref})
eligibility constraints ( $\mathcal{E})$
drift stability (D)
geometric locking conditions.
Each of these factors plays a role in determining whether a configuration can survive long enough to become part of the persistent structure of the system.
We now combine these factors into a single persistence condition.

## 5.5.2 Base persistence equation

The base persistence condition derived earlier is
$$
S = \frac{R}{\dot R,t_{ref}}.
$$
This dimensionless parameter compares retained structure to structural loss during the persistence horizon.
Persistence requires
$$
S \ge 1.
$$

## 5.5.3 Incorporating eligibility

Configurations that violate structural constraints cannot exist even if they are energetically stable.
This restriction is enforced through the eligibility operator
$$
\mathcal{E}(\sigma).
$$
Thus the persistence number becomes
$$
S_1 =
\mathcal{E}(\sigma)
\frac{R}{\dot R,t_{ref}}.
$$
If
$$
\mathcal{E}(\sigma)=0,
$$
the configuration is eliminated regardless of the value of (S).

## 5.5.4 Incorporating drift stability

Configurations may drift through configuration space even if they are structurally admissible.
To account for this effect we introduce the drift stability factor
$$
D.
$$
The persistence number becomes
$$
S_2 =
\mathcal{E}(\sigma)
D
\frac{R}{\dot R,t_{ref}}.
$$
The factor (D) reduces the persistence of configurations that are weakly anchored in the stability landscape.

## 5.5.5 Incorporating shell admissibility

For complex structures such as shells, additional geometric constraints must be satisfied.
These constraints arise from the multi-channel structural balance described by the six-fan lock condition
$$
\sum_{i=1}^{6} F_i \hat{n}_i = 0.
$$
Define a shell admissibility operator
$$
\mathcal{E}_{shell}.
$$
This operator evaluates whether the geometric locking conditions are satisfied.

## 5.5.6 Final corrected persistence number

Combining these factors gives the corrected persistence number
$$
S_* =
\mathcal{E}{shell}
\mathcal{E}
D
\frac{R}{\dot R,t{ref}}.
$$
Persistence requires
$$
S_* \ge 1.
$$
This equation defines the full persistence criterion for structures within the Collapse Tension Substrate.

## 5.5.7 Structural filtering hierarchy

The corrected persistence equation represents a sequence of filters applied to configuration space.
The filtering process occurs in four stages:
structural eligibility
shell admissibility
drift stability
persistence selection.
Formally, the surviving configuration set is
$$
\Omega_{persist}
{\sigma \in \Omega
\mid
\mathcal{E}{shell}
\mathcal{E}
D
\frac{R}{\dot R,t{ref}} \ge 1
}.
$$
Only configurations within this set become persistent structures.

## 5.5.8 Structural hierarchy

The persistence equation also explains why complex structures appear in stages.
Each level of structural complexity introduces new eligibility constraints.
Examples include:
structural level
dominant constraint
scalar field
amplitude stability
gradient field
spatial compatibility
circulation
rotational coherence
closure
boundary formation
shell
multi-axis geometric lock

Thus higher structural levels require increasingly stringent persistence conditions.

## 5.5.9 Structural abundance

The corrected persistence condition also explains why certain structures are abundant while others are rare.
Configurations with
large retained structure
low loss rate
strong drift stability
simple eligibility constraints
are far more likely to satisfy
$$
S_* \ge 1.
$$
These configurations dominate the persistent structure of the system.

## 5.5.10 Structural rarity

Conversely, structures that require
precise geometric locking
high structural energy
complex coordination
occur rarely.
Such configurations lie near the boundary
$$
S_* \approx 1.
$$
Small perturbations may destabilize them.

## 5.5.11 Final persistence rule

The persistence of structures within the Collapse Tension Substrate is governed by the inequality
$$
\boxed{
\mathcal{E}{shell}\mathcal{E}D
\frac{R}{\dot R,t{ref}}
\ge 1
}
$$
This equation summarizes the survival conditions for emergent structures.

## 5.5.12 Summary of Chapter 5

Chapter 5 introduced the structural gates that determine whether configurations can persist.
Key results include:
the eligibility operator ( $\mathcal{E})$
the drift stability factor (D)
the six-fan shell locking condition
the corrected persistence number (S_*).
These concepts extend the persistence framework beyond simple energy considerations and incorporate the geometric and dynamical constraints required for structural survival.

Transition to Chapter 6
With the persistence condition fully established, the next chapter analyzes how topology determines the formation of stable objects within the Collapse Tension Substrate.

Closure as the First Objecthood Threshold
This section begins the mathematical analysis of how topological closure transforms persistent patterns into discrete structural objects.

