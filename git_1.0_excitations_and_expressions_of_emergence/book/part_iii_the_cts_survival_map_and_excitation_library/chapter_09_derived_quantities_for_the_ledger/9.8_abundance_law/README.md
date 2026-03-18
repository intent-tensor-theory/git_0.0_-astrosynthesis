# 9.8 Abundance Law

## 9.8.1 Motivation

Sections 9.1–9.7 derived the quantities required to characterize every CTS excitation:

$$
E_{form},\quad E_{lock},\quad E_{total},\quad \Lambda_{lock},\quad \Lambda_{expr},\quad S_*.
$$

These parameters determine:

- How easily an excitation forms
- How strongly it resists structural loss

However, to understand the actual structural population of the substrate, we must determine how frequently each excitation occurs.
This requires a law governing excitation abundance.

## 9.8.2 Statistical emergence of excitations

The CTS substrate contains continuous fluctuations of energy and field structure.
These fluctuations allow excitations to form spontaneously when sufficient energy becomes available.
The probability of forming a structure depends on its total energy cost.

## 9.8.3 Effective fluctuation energy

Let $T_{eff}$ represent the effective fluctuation energy of the substrate.
This parameter plays a role analogous to temperature in statistical mechanics.
It measures the typical energy available from background fluctuations.

## 9.8.4 Boltzmann-like distribution

The probability of forming an excitation with energy $E_{total}$ follows a Boltzmann-like distribution

$$
\boxed{A_i \propto \exp\!\left(-\frac{E_{total}}{T_{eff}}\right)}
$$

where $A_i$ represents the abundance of excitation type $i$.

## 9.8.5 Interpretation

This equation implies:

| Energy | Abundance |
|---|---|
| Low $E_{total}$ | Highly abundant |
| Moderate $E_{total}$ | Moderately abundant |
| High $E_{total}$ | Rare |

Thus the CTS substrate is naturally dominated by low-energy excitations.

## 9.8.6 Combined formation–persistence selection

Formation probability alone does not determine structural populations.
Many excitations form frequently but decay rapidly.
The effective abundance therefore becomes

$$
\boxed{N_i \propto A_i\, S_*}
$$

where $A_i$ describes formation probability and $S_*$ describes persistence.
Thus structural populations depend on the product of formation likelihood and persistence strength.

## 9.8.7 Combined abundance expression

Substituting the abundance law gives

$$
N_i \propto S_* \exp\!\left(-\frac{E_{total}}{T_{eff}}\right).
$$

This equation defines the population density of excitations within the CTS substrate.

## 9.8.8 Structural population regimes

The combined abundance relation produces three characteristic regimes.

**Background propagation regime:** Low-energy excitations dominate.
Examples:
- Waves
- Weak coherent modes

These excitations are extremely abundant but short-lived.

**Intermediate structural regime:** Moderately stable structures appear.
Examples:
- Vortices
- Vortex rings

These structures occur less frequently but persist longer.

**Persistent object regime:** Highly stabilized structures dominate persistence.
Examples:
- Shells
- Braids

These structures are rare but extremely long-lived.

## 9.8.9 Abundance hierarchy

Combining formation probability and persistence yields the following approximate population ordering:

| Excitation | Abundance | Persistence |
|---|---|---|
| Wave | Extremely high | Very low |
| Phase-locked mode | High | Low |
| Vortex | Moderate | Moderate |
| Ring | Moderate | High |
| Chiral primitive | Low | High |
| Shell | Very low | Extremely high |
| Braid | Extremely low | Extremely high |

Thus the CTS substrate contains a mixture of abundant ephemeral excitations and rare persistent structures.

## 9.8.10 Population density function

More generally the population density of excitations can be written as

$$
n(E) \sim S_*(E)\,\exp\!\left(-\frac{E}{T_{eff}}\right).
$$

This function predicts the distribution of structural energies within the substrate.

## 9.8.11 Emergence as structural selection

The abundance law reveals the deeper meaning of CTS emergence.
Structures are not simply created and maintained arbitrarily.
Instead, the substrate performs a selection process governed by two competing factors:

- Energetic accessibility
- Structural persistence

Structures that balance these factors become dominant.

## 9.8.12 Emergence landscape

Plotting abundance against persistence produces the CTS survival landscape.
This landscape naturally organizes structures into regions such as:

- Background propagation
- Localized precursors
- Closure survival
- Chirality survival
- Shell survival
- Composite survival

These regions will be derived formally in the next chapter.

## 9.8.13 Role in the CTS framework

The abundance law completes the mathematical framework required to compute structural populations.
The CTS theory now contains three fundamental components:

- Energy functional → generates possible excitations
- Persistence equation → selects which excitations survive
- Abundance law → determines structural population density

Together these equations form the predictive core of the CTS framework.

## 9.8.14 Summary

Excitation abundance follows the Boltzmann-like relation

$$
A_i \propto \exp\!\left(-\frac{E_{total}}{T_{eff}}\right).
$$

When combined with structural persistence,

$$
N_i \propto S_*\, e^{-E_{total}/T_{eff}},
$$

this law determines the population of structures in the Collapse Tension Substrate.
