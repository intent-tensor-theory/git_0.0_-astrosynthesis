# 9.4 Lock Ratio

## 9.4.1 Motivation

Chapters 9.1–9.3 introduced three energy quantities for CTS excitations:
$$
E_{form}, \quad E_{lock}, \quad E_{total}.
$$
However, absolute energies alone are not sufficient to compare different structures.
Two excitations with very different formation energies may have similar structural stability if their relative locking strength is comparable.
To compare structures across scales we introduce a dimensionless stability parameter.
This parameter is the lock ratio.

## 9.4.2 Definition

The lock ratio is defined as
$$
\boxed{
\Lambda_{lock} = \frac{E_{lock}}{E_{form}}
}
$$
This quantity measures the strength of structural stabilization relative to the cost of forming the structure.

## 9.4.3 Interpretation

The lock ratio determines the structural character of the excitation.
Three regimes appear:
Weak locking
$$
\Lambda_{lock} \ll 1
$$
Formation energy dominates.
Structures appear easily but decay quickly.
Examples:
linear waves
weak coherent packets.

Balanced locking
$$
\Lambda_{lock} \sim 1
$$
Formation and stabilization energies are comparable.
Examples:
vortices
vortex rings.

Strong locking
$$
\Lambda_{lock} \gg 1
$$
Stabilization energy dominates.
Examples:
shells
braid structures.

## 9.4.4 Lock ratio for common CTS excitations

Approximate values for major excitation classes are shown below.
excitation
(E_{form})
(E_{lock})
$$
$\Lambda_{lock}$
$$
wave
very small
≈0
≈0
phase-locked mode
small
small
~0.1–0.5
vortex
moderate
moderate
~1
ring
moderate
high
~2–5
chiral primitive
high
high
~5–10
shell
very high
very high
~10–50
braid
extremely high
extremely high
≫10

Thus structural locking increases dramatically along the excitation hierarchy.

## 9.4.5 Structural interpretation

The lock ratio reveals a fundamental structural pattern.
Early excitations are cheap expressions of the substrate.
Later excitations are expensive but strongly stabilized structures.
Thus the CTS substrate naturally divides into two structural populations:
class
characteristics
cheap expressions
low (E_{form}), low (E_{lock})
durable structures
high (E_{lock}), high persistence

## 9.4.6 Lock ratio and structural resistance

The physical meaning of the lock ratio can also be interpreted as a resistance parameter.
Suppose the environment introduces perturbation energy (E_p).
A structure remains stable if
$$
E_p < E_{lock}.
$$
Thus structures with large lock ratio resist environmental disturbances more effectively.

## 9.4.7 Lock ratio and structural lifetime

Structural lifetime can be approximated as
$$
\tau
\sim
\tau_0
\exp!\left(
\frac{E_{lock}}{T_{eff}}
\right).
$$
Substituting the definition of lock ratio gives
$$
\tau
\sim
\tau_0
\exp!\left(
\frac{\Lambda_{lock}E_{form}}{T_{eff}}
\right).
$$
Thus lifetime grows exponentially with lock ratio.

## 9.4.8 Role in the CTS survival map

The lock ratio becomes the horizontal axis of the CTS survival phase chart.
Define
$$
x = \Lambda_{lock}.
$$
Small (x) corresponds to weakly stabilized excitations.
Large (x) corresponds to strongly stabilized structures.
Thus the horizontal axis of the survival map represents structural locking strength.

## 9.4.9 Relation to persistence threshold

The persistence threshold derived earlier is
$$
S_* =
\mathcal{E}{shell}
\mathcal{E}
D
T{obj}
\frac{R}{\dot R,t_{ref}}.
$$
Because (R) includes stabilizing energy contributions, structures with large lock ratio tend to produce larger persistence numbers.
Thus the lock ratio strongly influences whether an excitation crosses the survival boundary.

## 9.4.10 Structural selection

Combining lock ratio with formation energy leads to an important selection principle:
Structures that form easily dominate the background.
Structures that lock strongly dominate persistence.
This dual selection principle shapes the population of CTS excitations.

## 9.4.11 Ledger entry

The lock ratio therefore becomes a key entry in the CTS excitation ledger:
$$
\mathcal{L}i =
(
\text{type},
E{form},
E_{lock},
E_{total},
\Lambda_{lock},
\dots
).
$$
This dimensionless parameter allows structures of very different scales to be compared directly.

## 9.4.12 Summary

The lock ratio
$$
\Lambda_{lock} = \frac{E_{lock}}{E_{form}}
$$
measures the strength of structural stabilization relative to formation cost.
It distinguishes fragile excitations from highly persistent structures and serves as the primary horizontal coordinate of the CTS survival map.

Expression Ratio
This section introduces the complementary dimensionless quantity that measures how easily an excitation forms relative to its locking energy.

