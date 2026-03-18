# 8.1 What Counts as an Excitation

## 8.1.1 Motivation

Chapter 7 derived the CTS energy functional, which governs the dynamics of the Collapse Tension Substrate. Solutions of the Euler–Lagrange equations of this functional produce the possible field configurations of the substrate.
However, not every configuration deserves classification as an excitation.
Many configurations are trivial or correspond merely to background fluctuations.
Thus we require a precise mathematical definition of what constitutes a CTS excitation.

## 8.1.2 Definition of excitation

Let the CTS vacuum configuration be

$$
\Phi = \Phi_0.
$$

An excitation is a configuration

$$
\Phi = \Phi_0 + \delta\Phi
$$

that satisfies the following conditions:

- it solves the field equations derived from the CTS functional,
- it carries finite energy above the vacuum, and
- it possesses a localized or structured energy distribution.

Thus we define excitation energy as

$$
E_{exc} = E[\Phi] - E[\Phi_0].
$$

An excitation must satisfy

$$
0 < E_{exc} < \infty.
$$

## 8.1.3 Localized versus delocalized excitations

Excitations fall into two broad categories.

**Delocalized excitations** extend across large regions of the substrate. Examples:

- plane waves
- oscillatory modes
- long-wavelength fluctuations.

Mathematically they satisfy

$$
|\Phi| \sim \text{constant over large volume.}
$$

**Localized excitations** occupy finite spatial regions. Examples:

- solitons
- domain walls
- rings.

Localized excitations satisfy

$$
\mathcal{E}(\mathbf{x}) \rightarrow 0 \quad \text{as} \quad |\mathbf{x}| \rightarrow \infty.
$$

Thus their energy density vanishes at infinity.

## 8.1.4 Energy density

Define the energy density $\mathcal{E}(\mathbf{x})$.

The total excitation energy is

$$
E_{exc} = \int \mathcal{E}(\mathbf{x})\,d^3x.
$$

An excitation requires that the integral converges. Thus

$$
\mathcal{E}(\mathbf{x}) \rightarrow 0 \quad \text{as} \quad |\mathbf{x}| \rightarrow \infty.
$$

## 8.1.5 Stationary versus dynamic excitations

Excitations can also be classified by temporal behavior.

**Stationary excitations** remain static in time:

$$
\partial_t \Phi = 0.
$$

Examples:

- domain walls
- static vortices
- soliton solutions.

**Dynamic excitations** evolve in time but maintain coherent structure. Examples:

- propagating waves
- traveling solitons
- oscillatory bound states.

Dynamic excitations satisfy

$$
\Phi(\mathbf{x},t) = \Phi(\mathbf{x}-vt).
$$

## 8.1.6 Topological excitations

Some excitations are protected by topology.
These excitations possess conserved invariants such as

$$
n = \frac{1}{2\pi}\oint\nabla\theta\cdot d\mathbf{l}.
$$

Such excitations cannot decay continuously into the vacuum. Examples include

- vortices
- rings
- knots.

## 8.1.7 Non-topological excitations

Other excitations are stabilized not by topology but by energy balance. Examples include

- oscillons
- localized wave packets.

These structures persist due to nonlinear stabilization mechanisms.

## 8.1.8 Structural parameters of an excitation

Each CTS excitation can be characterized by a set of structural parameters:

| Parameter | Description |
|---|---|
| $E_{form}$ | formation energy |
| $E_{lock}$ | structural locking energy |
| $E_{total}$ | retained structure |
| $L_*$ | characteristic size |
| $T_{obj}$ | topology factor |

These parameters determine whether the excitation survives persistence selection.

## 8.1.9 Persistence threshold

An excitation becomes a persistent structure when it satisfies

$$
S = \frac{R}{\dot{R}\,t_{ref}} \geq 1.
$$

Thus the excitation ledger must record the parameters required to evaluate this condition.

## 8.1.10 Excitation classification problem

The goal of the CTS excitation ledger is to systematically classify all excitations supported by the substrate.
Each entry in the ledger corresponds to a solution of the field equations together with its structural parameters.
This classification allows us to determine

- which excitations appear frequently
- which excitations are rare
- which excitations become persistent objects.

## 8.1.11 Ledger structure

Each entry in the ledger takes the form

$$
\left(\text{type},\; E_{form},\; E_{lock},\; E_{total},\; L_*,\; T_{obj}\right).
$$

These quantities will be used in later chapters to construct the CTS survival map.

## 8.1.12 Role of the excitation ledger

The ledger serves as the bridge between two components of the theory:

- the energy functional, which generates possible excitations,
- the persistence framework, which determines which excitations survive.

Thus the excitation ledger provides the mathematical inventory of structural possibilities within the substrate.

## 8.1.13 Summary

An excitation is a finite-energy field configuration above the vacuum that possesses structured spatial organization.
Excitations may be

- localized or delocalized
- stationary or dynamic
- topological or non-topological.

Each excitation is characterized by parameters such as formation energy, locking energy, size, and topology factor.
These parameters form the entries of the CTS excitation ledger.
