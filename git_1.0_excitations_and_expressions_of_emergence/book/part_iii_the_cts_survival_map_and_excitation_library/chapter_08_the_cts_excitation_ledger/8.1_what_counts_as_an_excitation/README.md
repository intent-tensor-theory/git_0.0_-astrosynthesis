# 8.1 What Counts as an Excitation

## 8.1.1 Motivation

Chapter 7 derived the CTS energy functional, which governs the dynamics of the Collapse Tension Substrate. Solutions of the Euler–Lagrange equations of this functional produce the possible field configurations of the substrate.
However, not every configuration deserves classification as an excitation.
Many configurations are trivial or correspond merely to background fluctuations.
Thus we require a precise mathematical definition of what constitutes a CTS excitation.

## 8.1.2 Definition of excitation

Let the CTS vacuum configuration be
Φ=Φ0.\Phi = \Phi_0.Φ=Φ0​.
An excitation is a configuration
Φ=Φ0+δΦ\Phi = \Phi_0 + \delta\PhiΦ=Φ0​+δΦ
that satisfies the following conditions:
it solves the field equations derived from the CTS functional,

it carries finite energy above the vacuum, and

it possesses a localized or structured energy distribution.

Thus we define excitation energy as
Eexc=E[Φ]−E[Φ0].E_{exc} = E[\Phi] - E[\Phi_0].Eexc​=E[Φ]−E[Φ0​].
An excitation must satisfy
0<Eexc<∞.0 < E_{exc} < \infty.0<Eexc​<∞.

## 8.1.3 Localized versus delocalized excitations

Excitations fall into two broad categories.
Delocalized excitations
These extend across large regions of the substrate.
Examples:
plane waves

oscillatory modes

long-wavelength fluctuations.

Mathematically they satisfy
∣Φ∣∼constant over large volume.| $\Phi| \sim \text{constant over large volume}.$
Localized excitations
These occupy finite spatial regions.
Examples:

solitons

domain walls

rings.

Localized excitations satisfy
Thus their energy density vanishes at infinity.

## 8.1.4 Energy density

Define the energy density
$$
E(x).\mathcal{E}$\mathbf{x}$.E(x).
$$
The total excitation energy is
Eexc=∫E(x) d3x.E_{exc} = \int \mathcal{E}$\mathbf{x}$\,d^3x.Eexc​=∫E(x)d3x.
An excitation requires that the integral converges.
Thus
$$
E(x)0asx.\mathcal{E}$\mathbf{x}$ \rightarrow 0 \quad \text{as} \quad |\mathbf{x}| \rightarrow \infty.E(x)
$$

## 8.1.5 Stationary versus dynamic excitations

Excitations can also be classified by temporal behavior.
Stationary excitations
These configurations remain static in time.
∂tΦ=0.\partial_t \Phi = 0.∂t​Φ=0.
Examples:
domain walls

static vortices

soliton solutions.

Dynamic excitations
These configurations evolve in time but maintain coherent structure.
Examples:
propagating waves

traveling solitons

oscillatory bound states.

Dynamic excitations satisfy
$$
(x,t)=(xvt).\Phi$\mathbf{x},t$ = \Phi$\mathbf{x}-vt$.
$$

## 8.1.6 Topological excitations

Some excitations are protected by topology.
These excitations possess conserved invariants such as
n=12π∮∇θ⋅dl.n = \frac{1}{2\pi}\oint\nabla\theta\cdot dl.n=2π1​∮∇θ⋅dl.
Such excitations cannot decay continuously into the vacuum.
Examples include
vortices

rings

knots.

## 8.1.7 Non-topological excitations

Other excitations are stabilized not by topology but by energy balance.
Examples include

oscillons

localized wave packets.

These structures persist due to nonlinear stabilization mechanisms.

## 8.1.8 Structural parameters of an excitation

Each CTS excitation can be characterized by a set of structural parameters:
parameter
formation energy
structural locking energy
retained structure
characteristic size
topology factor

These parameters determine whether the excitation survives persistence selection.

## 8.1.9 Persistence threshold

An excitation becomes a persistent structure when it satisfies
S∗=EshellEDTobjRR˙ tref≥1.S_* = \mathcal{E}_{shell}\mathcal{E}D T_{obj} \frac{R}{\dot R\,t_{ref}} \ge 1.S∗​=Eshell​EDTobj​R˙tref​R​≥1.
Thus the excitation ledger must record the parameters required to evaluate this condition.

## 8.1.10 Excitation classification problem

The goal of the CTS excitation ledger is to systematically classify all excitations supported by the substrate.
Each entry in the ledger corresponds to a solution of the field equations together with its structural parameters.
This classification allows us to determine
which excitations appear frequently

which excitations are rare

which excitations become persistent objects.

## 8.1.11 Ledger structure

Each entry in the ledger takes the form
(type,Eform,Elock,Etotal,L,Tobj)$\text{type}, E_{form}, E_{lock}, E_{total}, L, T_{obj}$(type,Eform​,Elock​,Etotal​,L,Tobj​)
These quantities will be used in later chapters to construct the CTS survival map.

## 8.1.12 Role of the excitation ledger

The ledger serves as the bridge between two components of the theory:
the energy functional, which generates possible excitations,

the persistence framework, which determines which excitations survive.

Thus the excitation ledger provides the mathematical inventory of structural possibilities within the substrate.

## 8.1.13 Summary

An excitation is a finite-energy field configuration above the vacuum that possesses structured spatial organization.
Excitations may be
localized or delocalized

stationary or dynamic

topological or non-topological.

Each excitation is characterized by parameters such as formation energy, locking energy, size, and topology factor.
These parameters form the entries of the CTS excitation ledger.

 Wave Modes
This section derives the mathematical structure of the simplest CTS excitations: propagating substrate waves.

