# 9.2 Lock Energy

## 9.2.1 Motivation

However, formation energy alone does not determine whether a structure will persist.
Many structures are cheap to form but decay quickly.
Persistence instead depends on stabilizing mechanisms that resist structural loss.
These stabilizing contributions collectively define the lock energy $E_{lock}$.

## 9.2.2 Definition of lock energy

Let $E_{total}$ be the total energy of the excitation.
We define lock energy as the portion of energy associated with stabilizing structural constraints.

$$
E_{lock} = E_{total} - E_{form}.
$$

Lock energy represents the energetic barrier that must be overcome to destroy the structure.

## 9.2.3 Locking mechanisms

Different excitation classes possess different stabilization mechanisms.
The major locking mechanisms in CTS include:

| Mechanism | Description |
|---|---|
| Circulation | Phase winding |
| Geometric confinement | Closed-loop topology |
| Chirality | Twist stabilization |
| Shell locking | Multi-axis balance |
| Braid topology | Strand linking |

Each mechanism contributes energy that resists structural decay.

## 9.2.4 Circulation locking

For vortex excitations the locking mechanism arises from circulation conservation.
The circulation invariant is

$$
\Gamma = \oint_C \mathbf{v}\cdot d\mathbf{l} = 2\pi n.
$$

To remove the vortex this circulation must vanish.
The energy required to eliminate the vortex core contributes to the lock energy.
Approximate locking energy for a vortex line is

$$
E_{lock}^{vortex} \sim \pi a n^2 \Phi_0^2.
$$

## 9.2.5 Closure locking

Closed structures such as vortex rings possess additional stabilization from geometric closure.
Breaking the ring requires opening the loop, which increases energy.
For a ring of radius $R$

$$
E_{lock}^{ring} \sim \rho \Gamma^2 R.
$$

This energy represents the cost of disrupting the circulation loop.

## 9.2.6 Chirality locking

Chiral excitations possess stabilization due to twist.
The twist energy is

$$
E_{twist} = \frac{k_t}{2} \int \left(\frac{d\theta}{ds}\right)^2 ds.
$$

This energy penalizes untwisting of the structure.
The energy barrier between left- and right-handed states contributes to persistence.

## 9.2.7 Shell locking

Shell structures are stabilized by balanced structural flows along their surface.
Recall the multi-fan locking condition

$$
\sum_{i=1}^{N_f} \mathbf{F}_i = 0.
$$

Disrupting the shell requires breaking this balance.
The shell locking energy can be approximated as

$$
E_{lock}^{shell} = \kappa_c \int_\Sigma H^2 \, dA,
$$

where $H$ is the mean curvature and $\kappa_c$ is the curvature stiffness.

## 9.2.8 Braid locking

Braids derive stability from topological linking.
The linking number $Lk$ cannot change without reconnection.
The energy required for reconnection defines the braid locking energy.
A simplified expression is

$$
E_{lock}^{braid} = k_b Lk^2.
$$

## 9.2.9 Lock energy hierarchy

Different excitation classes therefore exhibit different lock energies.

| Excitation | Lock mechanism | Relative magnitude |
|---|---|---|
| Phase-locked mode | Coherence | Low |
| Vortex | Circulation | Moderate |
| Chiral primitive | Multi-fan locking | Very high |
| Shell | Curvature balance | Extremely high |

Thus lock energy generally increases with structural complexity.

## 9.2.10 Lock ratio

To compare structures we introduce the lock ratio

$$
\boxed{ \Lambda_{lock} = \frac{E_{lock}}{E_{form}} }
$$

This dimensionless quantity measures how strongly a structure is stabilized relative to the cost of forming it.
Large values indicate strong persistence potential.

## 9.2.11 Lock ratio interpretation

The lock ratio provides a useful classification of excitations.

| Regime | Condition | Interpretation |
|---|---|---|
| Weak lock | $\Lambda_{lock} \ll 1$ | Easy to destroy |
| Moderate lock | $\Lambda_{lock} \sim 1$ | Moderate stability |
| Strong lock | $\Lambda_{lock} \gg 1$ | Highly persistent |

Shells and braids typically fall into the strong-lock regime.

## 9.2.12 Relation to persistence number

The persistence threshold derived earlier depends strongly on locking energy.
Recall the selection number

$$
S = \frac{R}{\dot{R}\,t_{ref}}.
$$

Because $R$ includes stabilizing energy contributions, structures with large lock energy tend to produce larger persistence numbers.

## 9.2.13 Role in the excitation ledger

Each ledger entry therefore records $E_{lock}$ alongside formation energy.
The combination $(E_{form}, E_{lock})$ determines both the abundance and persistence of the excitation.

## 9.2.14 Summary

Lock energy measures the stabilizing energy that protects an excitation from structural decay.
It arises from mechanisms such as circulation, closure, chirality, shell locking, and braid topology.
Comparing lock energy to formation energy yields the lock ratio

$$
\Lambda_{lock} = \frac{E_{lock}}{E_{form}}.
$$

This quantity plays a central role in determining whether excitations survive in the CTS survival landscape.
