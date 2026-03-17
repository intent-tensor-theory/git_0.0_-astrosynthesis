# 9.6 Structural Persistence

## 9.6.1 Motivation

The previous sections introduced energetic quantities that describe the creation and stabilization of excitations:
formation energy (E_{form})
lock energy (E_{lock})
total energy (E_{total})
lock ratio ( $\Lambda_{lock})$
expression ratio ( $\Lambda_{expr})$
However, these quantities alone do not determine whether a structure will survive long enough to become observable.
For this we require a persistence metric that measures the ability of an excitation to resist structural loss.
This metric is called structural persistence.

## 9.6.2 Retention and loss

Let
$$
R
$$
represent the retained structural energy of an excitation.
Let
$$
\dot{R}
$$
represent the rate of structural loss due to dissipation, drift, or perturbation.
If loss dominates retention, the structure disappears.
If retention dominates loss, the structure persists.

## 9.6.3 Persistence horizon

Persistence must be evaluated relative to a characteristic timescale
$$
t_{ref}.
$$
This timescale defines the persistence horizon over which the structure must survive.
Examples include:
system
typical horizon
wave packet
oscillation period
vortex
circulation lifetime
shell
structural relaxation time

## 9.6.4 Basic persistence number

The simplest persistence measure is the dimensionless ratio
$$
S = \frac{R}{\dot{R} t_{ref}}.
$$
Interpretation:
condition
interpretation
(S<1)
decay dominates
$$
(S\approx1)
$$
marginal stability
(S>1)
persistence dominates

Thus (S=1) defines the critical persistence threshold.

## 9.6.5 Structural modifiers

In real CTS excitations several structural factors enhance persistence.
These include
factor
meaning
(D)
drift stability
(T_{obj})
topology factor
$$
$\mathcal{E}$
$$
coherence factor
$$
$\mathcal{E}_{shell}$
$$
shell locking factor

Each of these parameters modifies the effective retention of the structure.

## 9.6.6 Corrected persistence number

Including these modifiers yields the corrected persistence number
$$
\boxed{
S_* =
\mathcal{E}{shell}
\mathcal{E}
D
T{obj}
\frac{R}{\dot{R} t_{ref}}
}
$$
This expression represents the full CTS persistence condition.

## 9.6.7 Physical meaning of persistence factors

Each multiplier corresponds to a structural stabilization mechanism.
Coherence factor
$$
\mathcal{E}
$$
Measures phase coherence between structural channels.
Low coherence leads to destructive interference and structural decay.

Shell factor
$$
\mathcal{E}_{shell}
$$
Measures multi-fan locking efficiency in shell structures.
Shell closure dramatically increases persistence.

Drift stability
$$
D
$$
Represents resistance to translational drift or diffusion.
Structures with large (D) remain spatially localized.

Topology factor
$$
T_{obj}
$$
Measures topological protection.
Examples:
excitation
(T_{obj})
wave
1
vortex
>1
ring
>1
braid
≫1

## 9.6.8 Persistence threshold

The persistence threshold occurs when
$$
S_* = 1.
$$
Thus
$$
\mathcal{E}{shell}
\mathcal{E}
D
T{obj}
\frac{R}{\dot{R} t_{ref}}
= 1.
$$
Structures with
$$
S_* > 1
$$
persist.
Structures with
$$
S_* < 1
$$
decay.

## 9.6.9 Relation to survival map

The persistence number forms the vertical coordinate of the CTS survival map.
Define
$$
y =
\mathcal{E}{shell}
\mathcal{E}
D
T{obj}
\frac{R}{\dot{R} t_{ref}}.
$$
Then
$$
y = S_*.
$$
Thus the vertical axis of the survival chart represents structural persistence strength.

## 9.6.10 Combined survival condition

Combining persistence with the lock ratio gives the survival number
$$
S_* = x y
$$
where
$$
x = \Lambda_{lock}
$$
and
$$
y =
\mathcal{E}{shell}
\mathcal{E}
D
T{obj}
\frac{R}{\dot{R} t_{ref}}.
$$
The survival boundary is therefore
$$
xy = 1.
$$

## 9.6.11 Structural regions

This boundary divides the excitation landscape into two regimes.
region
condition
ephemeral
(xy < 1)
persistent
(xy > 1)

Thus the survival map identifies which structures cross the persistence threshold.

## 9.6.12 Ledger entry

Each excitation entry must therefore record the persistence number
$$
S_*.
$$
The ledger entry becomes
$$
\mathcal{L}i =
(
\text{type},
E{form},
E_{lock},
E_{total},
\Lambda_{lock},
\Lambda_{expr},
S_*
).
$$
This quantity determines whether the excitation survives.

## 9.6.13 Interpretation within CTS theory

The persistence number represents the central selection mechanism of the CTS framework.
While the energy functional determines which structures can exist, the persistence number determines which structures survive.
Thus emergence becomes a selection process among possible excitations.

## 9.6.14 Summary

Structural persistence is measured by the corrected persistence number
$$
S_* =
\mathcal{E}{shell}
\mathcal{E}
D
T{obj}
\frac{R}{\dot{R} t_{ref}}.
$$
The threshold
$$
S_* = 1
$$
separates ephemeral excitations from persistent structures.
This quantity forms the vertical coordinate of the CTS survival map and determines which excitations survive within the substrate.

Structural Persistence Scaling
This section derives how persistence scales with excitation size, topology, and environmental fluctuation energy.

