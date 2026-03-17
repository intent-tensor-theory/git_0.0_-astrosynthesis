# 9.5 Expression Ratio

## 9.5.1 Motivation

Section 9.4 introduced the lock ratio
$$
\Lambda_{lock} = \frac{E_{lock}}{E_{form}}
$$
which measures structural stabilization relative to formation cost.
However, persistence is not determined by locking strength alone.
An excitation may be extremely well locked but so expensive to create that it rarely appears.
To quantify the ease of structural expression, we introduce a complementary dimensionless parameter: the expression ratio.

## 9.5.2 Definition

The expression ratio is defined as
$$
\boxed{
\Lambda_{expr} =
\frac{E_{form}}{E_{lock} + \epsilon_0}
}
$$
where
$$
$\epsilon_0$ is a small regularization constant preventing division by zero.
$$
This ratio measures the ease with which an excitation can appear relative to the energy required to stabilize it.

## 9.5.3 Interpretation

The expression ratio measures structural expressibility.
Three regimes emerge.
Highly expressive structures
$$
\Lambda_{expr} \gg 1
$$
Formation energy dominates stabilization energy.
These structures appear frequently but are fragile.
Examples:
waves
weak coherent packets.

Balanced structures
$$
\Lambda_{expr} \sim 1
$$
Formation and stabilization energies are comparable.
Examples:
vortices
vortex rings.

Difficult-to-express structures
$$
\Lambda_{expr} \ll 1
$$
Stabilization energy greatly exceeds formation energy.
These structures require substantial energetic organization.
Examples:
shells
braid structures.

## 9.5.4 Complementarity with lock ratio

The lock ratio and expression ratio are mathematically related.
Ignoring the small constant ( $\epsilon_0),$
$$
\Lambda_{expr} \approx \frac{1}{\Lambda_{lock}}.
$$
Thus the two ratios form complementary structural measures:
quantity
interpretation
$$
$\Lambda_{lock}$
$$
stabilization strength
$$
$\Lambda_{expr}$
$$
formation accessibility

Together they describe the trade-off between stability and accessibility.

## 9.5.5 Expression ratio for CTS excitations

Approximate expression ratios for the main excitation classes are:
excitation
$$
$\Lambda_{expr}$
$$
wave
very large
phase-locked mode
large
vortex
~1
ring
<1
chiral primitive
≪1
shell
≪1
braid
≪1

Thus simple excitations are highly expressive while complex structures are difficult to form.

## 9.5.6 Structural interpretation

The expression ratio reveals a fundamental principle of CTS emergence:
the universe favors structures that are easy to express but persistent structures require high locking energy.
This duality creates a structural landscape consisting of
abundant, low-lock structures
rare, high-lock persistent objects.

## 9.5.7 Expression ratio and excitation abundance

Recall the abundance relation
$$
A_i \propto \exp!\left(-\frac{E_{total}}{T_{eff}}\right).
$$
Because
$$
E_{total} = E_{form} + E_{lock},
$$
structures with high formation energy appear less frequently.
Thus small expression ratios generally correspond to low abundance.

## 9.5.8 Expression axis of the survival map

The expression ratio also plays an important role in constructing the CTS survival map.
Recall the horizontal coordinate of the map:
$$
x = \Lambda_{lock}.
$$
Using the reciprocal relation
$$
\Lambda_{expr} \approx \frac{1}{x},
$$
the expression ratio provides an alternative interpretation of this axis.
Small (x) corresponds to high expressibility.
Large (x) corresponds to high locking strength.

## 9.5.9 Structural efficiency diagram

Plotting the two ratios together produces a structural classification diagram.
region
structure type
high expression / low lock
waves
moderate expression / moderate lock
vortices
low expression / high lock
shells
very low expression / extreme lock
braids

This diagram visually illustrates the structural hierarchy of CTS excitations.

## 9.5.10 Expression ratio and emergence sequence

The expression ratio also helps explain why certain structures appear earlier in the emergence sequence.
Excitations with large expression ratios require less coordinated energy.
Thus the typical emergence sequence proceeds:
$$
\text{waves}
\rightarrow
\text{vortices}
\rightarrow
\text{rings}
\rightarrow
\text{chiral structures}
\rightarrow
\text{shells}
\rightarrow
\text{braids}.
$$
Each step requires increasing structural organization.

## 9.5.11 Ledger entry

The expression ratio therefore becomes another important field in the excitation ledger.
Each ledger entry records
$$
\mathcal{L}i =
(
\text{type},
E{form},
E_{lock},
E_{total},
\Lambda_{lock},
\Lambda_{expr},
\dots
).
$$
These quantities allow structural expressibility and persistence to be compared directly.

## 9.5.12 Summary

The expression ratio
$$
\Lambda_{expr} =
\frac{E_{form}}{E_{lock}+\epsilon_0}
$$
measures how easily an excitation forms relative to its stabilization energy.
It complements the lock ratio and reveals the trade-off between structural accessibility and persistence.
Together these two dimensionless quantities form the primary structural coordinates of the CTS excitation landscape.

Structural Persistence
This section derives the quantitative measure of structural survival used to determine which excitations cross the CTS persistence threshold.

