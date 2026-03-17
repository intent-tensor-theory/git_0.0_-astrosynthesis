# 9.2 Lock Energy

## 9.2.1 Motivation

However, formation energy alone does not determine whether a structure will persist.
Many structures are cheap to form but decay quickly.
Persistence instead depends on stabilizing mechanisms that resist structural loss.
These stabilizing contributions collectively define the lock energy
Elock.E_{lock}.Elock​.

## 9.2.2 Definition of lock energy

Let
be the total energy of the excitation.
We define lock energy as the portion of energy associated with stabilizing structural constraints.
Thus
Lock energy represents the energetic barrier that must be overcome to destroy the structure.

## 9.2.3 Locking mechanisms

Different excitation classes possess different stabilization mechanisms.
The major locking mechanisms in CTS include:
mechanism
description
circulation
phase winding
geometric confinement
chirality
twist stabilization
shell locking
multi-axis balance
braid topology
strand linking

Each mechanism contributes energy that resists structural decay.

## 9.2.4 Circulation locking

For vortex excitations the locking mechanism arises from circulation conservation.
The circulation invariant is
Γ=∮Cv⋅dl=2πn.\Gamma = \oint_C \mathbf{v}\cdot d\mathbf{l} = 2\pi n.Γ=∮C​v⋅dl=2πn.
To remove the vortex this circulation must vanish.
The energy required to eliminate the vortex core contributes to the lock energy.
Approximate locking energy for a vortex line is
Elockvortex∼πan2Φ02.E_{lock}^{vortex} \sim \pi a n^2 \Phi_0^2.Elockvortex​∼πan2Φ02​.

## 9.2.5 Closure locking

Closed structures such as vortex rings possess additional stabilization from geometric closure.
Breaking the ring requires opening the loop, which increases energy.
For a ring of radius RRR
Elockring∼ρΓ2R.E_{lock}^{ring} \sim \rho \Gamma^2 R.Elockring​∼ρΓ2R.
This energy represents the cost of disrupting the circulation loop.

## 9.2.6 Chirality locking

Chiral excitations possess stabilization due to twist.
The twist energy is
Etwist=kt2∫(dθds)2ds.E_{twist} = \frac{k_t}{2} \int \left$\frac{d\theta}{ds}\right$^2 ds.Etwist​=2kt​​∫(dsdθ​)2ds.
This energy penalizes untwisting of the structure.
Thus
The energy barrier between left- and right-handed states contributes to persistence.

## 9.2.7 Shell locking

Shell structures are stabilized by balanced structural flows along their surface.
Recall the multi-fan locking condition
∑i=1NfFi=0.\sum_{i=1}^{N_f} \mathbf{F}_i = 0.i=1∑Nf​​Fi​=0.
Disrupting the shell requires breaking this balance.
The shell locking energy can be approximated as
Elockshell=κc∫ΣH2dA.E_{lock}^{shell} = \kappa_c \int_\Sigma H^2 dA.Elockshell​=κc​∫Σ​H2dA.
HHH is mean curvature

κc\kappa_cκc​ is curvature stiffness.

## 9.2.8 Braid locking

Braids derive stability from topological linking.
The linking number between strands
LkLkLk
cannot change without reconnection.
The energy required for reconnection defines the braid locking energy.
A simplified expression is
Elockbraid=kbLk2.E_{lock}^{braid} = k_b Lk^2.Elockbraid​=kb​Lk2.

## 9.2.9 Lock energy hierarchy

Different excitation classes therefore exhibit different lock energies.
excitation
lock mechanism
phase-locked mode
coherence
low
vortex
circulation
chiral primitive
multi-fan locking
very high
extremely high

Thus lock energy generally increases with structural complexity.

## 9.2.10 Lock ratio

To compare structures we introduce the lock ratio
Λlock=ElockEform\boxed{ \Lambda_{lock} = \frac{E_{lock}}{E_{form}} }Λlock​=Eform​Elock​​​
This dimensionless quantity measures how strongly a structure is stabilized relative to the cost of forming it.
Large values indicate strong persistence potential.

## 9.2.11 Lock ratio interpretation

The lock ratio provides a useful classification of excitations.
regime
condition
interpretation
weak lock
easy to destroy
moderate stability
strong lock
highly persistent

Shells and braids typically fall into the strong-lock regime.

## 9.2.12 Relation to persistence number

The persistence threshold derived earlier depends strongly on locking energy.
Recall
Because RRR includes stabilizing energy contributions, structures with large lock energy tend to produce larger persistence numbers.

## 9.2.13 Role in the excitation ledger

Each ledger entry therefore records
ElockE_{lock}Elock​
alongside formation energy.
The combination
determines both the abundance and persistence of the excitation.

## 9.2.14 Summary

Lock energy measures the stabilizing energy that protects an excitation from structural decay.
It arises from mechanisms such as circulation, closure, chirality, shell locking, and braid topology.
Comparing lock energy to formation energy yields the lock ratio
Λlock=ElockEform.\Lambda_{lock}=\frac{E_{lock}}{E_{form}}.Λlock​=Eform​Elock​​.
This quantity plays a central role in determining whether excitations survive in the CTS survival landscape.

 Total Energy
This section derives the total excitation energy and its role in determining excitation abundance within the Collapse Tension Substrate.

