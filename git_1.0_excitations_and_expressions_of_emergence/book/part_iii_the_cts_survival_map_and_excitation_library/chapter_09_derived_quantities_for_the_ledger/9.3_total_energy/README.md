# 9.3 Total Energy

## 9.3.1 Motivation

Sections 9.1 and 9.2 introduced the two primary energy components of any CTS excitation:

- Formation energy $E_{form}$
- Lock energy $E_{lock}$

While these two quantities describe different aspects of structural emergence, the excitation ledger must also track the total energetic burden of each structure.
This quantity determines how frequently the excitation appears within the substrate.
We therefore define the total excitation energy.

## 9.3.2 Definition of total energy

The total energy of an excitation is simply the sum of formation and locking energies:

$$
\boxed{E_{total} = E_{form} + E_{lock}}
$$

This quantity represents the complete energy stored in the excitation relative to the vacuum.

## 9.3.3 Energy density formulation

From the CTS energy functional the total energy is

$$
E_{total} = \int \mathcal{E}(\mathbf{x})\, d^3x,
$$

where the energy density is

$$
\mathcal{E} = a|\nabla\Phi|^2 + u(\nabla^2\Phi)^2 + r|\Phi|^2 + s|\Phi|^4 + b|\nabla\times\mathbf{A}|^2.
$$

Integrating this density over space yields the total excitation energy.

## 9.3.4 Physical interpretation

Each term in the energy density contributes to the total energy:

| Energy component | Origin |
|---|---|
| Gradient energy | Spatial variation of field |
| Curvature energy | Higher-order spatial structure |
| Potential energy | Scalar field amplitude |
| Gauge energy | Circulation fields |

The balance between these contributions determines the final energy of the excitation.

## 9.3.5 Energy hierarchy of excitation classes

Using the scaling relations derived earlier, approximate total energies for major excitation classes can be summarized as follows:

| Excitation | Approximate scaling |
|---|---|
| Wave | $E \sim A^2$ |
| Phase-locked mode | $E \sim A^2 L^3$ |
| Vortex | $E \sim \ln(R/\xi)$ |
| Ring | $E \sim R\ln(R/\xi)$ |
| Chiral primitive | $E \sim R + E_{twist}$ |
| Shell | $E \sim R^2$ |
| Braid | $E \sim NR$ |

These relations illustrate the increasing energetic cost of higher structural complexity.

## 9.3.6 Energetic ordering of CTS excitations

Combining formation and locking contributions yields the approximate energy hierarchy

$$
E_{wave} < E_{phase} < E_{vortex} < E_{ring} < E_{chiral} < E_{shell} < E_{braid}.
$$

This ordering is fundamental to the structure of the CTS survival landscape.

## 9.3.7 Total energy and abundance

Excitation abundance depends exponentially on total energy.
The statistical abundance relation is

$$
A_i \propto \exp\!\left(-\frac{E_{total}}{T_{eff}}\right).
$$

Here $T_{eff}$ represents the effective fluctuation energy of the substrate.
Thus:

- Low total energy → high abundance
- High total energy → rare structures

## 9.3.8 Cheap expressions versus durable structures

An important insight emerges from comparing formation energy and locking energy.
Two distinct structural regimes appear.

**Cheap expressions:** Structures with $E_{total} \approx E_{form}$ form easily but decay quickly.
Examples:
- Waves
- Weak coherent packets

**Durable structures:** Structures with $E_{lock} \gg E_{form}$ require more energy to form but resist destruction.
Examples:
- Shells
- Braids

## 9.3.9 Energetic efficiency

To compare structural efficiency we define

$$
\eta = \frac{E_{lock}}{E_{total}}.
$$

This quantity measures how much of the excitation energy contributes to structural stability.

| Regime | Interpretation |
|---|---|
| $\eta \approx 0$ | Fragile structures |
| $\eta \approx 0.5$ | Balanced structures |
| $\eta \approx 1$ | Highly stabilized structures |

## 9.3.10 Total energy and persistence

Although persistence primarily depends on structural retention, total energy influences persistence indirectly.
Structures with extremely high total energy tend to form rarely, even if they are stable once formed.
Thus the survival of an excitation depends on both:

- Persistence threshold
- Formation probability

## 9.3.11 Ledger entry

Each excitation entry in the CTS ledger therefore records $E_{total}$ alongside formation and locking energies.
The ledger structure becomes

$$
\mathcal{L}_i = (\text{type},\, E_{form},\, E_{lock},\, E_{total},\, \dots).
$$

These quantities determine the position of the excitation in the CTS survival map.

## 9.3.12 Summary

Total energy is the complete energetic cost of an excitation relative to the CTS vacuum.
It combines formation energy and lock energy:

$$
E_{total} = E_{form} + E_{lock}.
$$

This quantity determines the abundance of excitations within the substrate and helps distinguish cheap background expressions from rare but highly persistent structures.
