# 10.1 Choosing the Phase Variables

## 10.1.1 Motivation

Chapters 7–9 established the mathematical framework needed to evaluate CTS excitations:

- Energy quantities: $E_{form}$, $E_{lock}$, $E_{total}$
- Derived ratios: $\Lambda_{lock}$, $\Lambda_{expr}$
- Persistence number: $S_*$
- Abundance relation: $N_i \propto S_*\, e^{-E_{total}/T_{eff}}$

However, to understand the global structure of emergence, we require a visual representation of these relationships.
This representation is the CTS Threshold Phase Chart.

## 10.1.2 Purpose of the phase chart

The phase chart maps every excitation class into a two-dimensional structural space.
The purpose of the chart is to identify:

- Which excitations form easily
- Which excitations survive
- Where the survival threshold lies
- How structural classes are distributed

Thus the chart becomes a geometric map of emergence.

## 10.1.3 Requirements for phase variables

To construct the chart we must choose two variables that satisfy several conditions.
The variables must:

- Be dimensionless
- Apply to all excitation classes
- Capture formation vs persistence dynamics
- Produce a clear survival threshold

From the quantities derived earlier, two parameters satisfy these conditions.

## 10.1.4 Horizontal coordinate: structural locking

The first variable describes structural stabilization strength.
From Chapter 9 we defined the lock ratio

$$
\Lambda_{lock} = \frac{E_{lock}}{E_{form}}.
$$

This ratio measures how strongly an excitation resists destruction relative to the energy required to create it.
We therefore define the horizontal coordinate

$$
\boxed{x = \Lambda_{lock}}
$$

## 10.1.5 Interpretation of the horizontal axis

The horizontal axis represents structural locking strength.
Typical values include:

| Excitation | $x = \Lambda_{lock}$ |
|---|---|
| Wave | $\approx 0$ |
| Phase-locked mode | $\sim 0.1$–$0.5$ |
| Vortex | $\sim 1$ |
| Ring | $\sim 2$–$5$ |
| Chiral primitive | $\sim 5$–$10$ |
| Shell | $\sim 10$–$50$ |
| Braid | $\gg 50$ |

Moving to the right on the chart corresponds to increasing structural stabilization.

## 10.1.6 Vertical coordinate: persistence strength

The second variable must measure the ability of a structure to survive environmental loss.
From Chapter 9 the corrected persistence number was

$$
S_* = \mathcal{E}_{shell}\,\mathcal{E}\,D\,T_{obj}\,\frac{R}{\dot{R}\, t_{ref}}.
$$

Because this number measures structural survival strength, we define the vertical coordinate as

$$
\boxed{y = \mathcal{E}_{shell}\,\mathcal{E}\,D\,T_{obj}\,\frac{R}{\dot{R}\, t_{ref}}}
$$

Thus $y = S_*$.

## 10.1.7 Interpretation of the vertical axis

The vertical axis represents persistence strength.
Typical values:

| Excitation | $y$ |
|---|---|
| Wave | $\ll 1$ |
| Phase-locked mode | $< 1$ |
| Vortex | $\sim 1$ |
| Ring | $> 1$ |
| Chiral primitive | $\gg 1$ |
| Shell | $\gg 10$ |
| Braid | $\gg 100$ |

Moving upward corresponds to increasing persistence.

## 10.1.8 Combined survival number

Earlier derivations showed that survival occurs when $S_* \geq 1$.
In phase chart variables this becomes

$$
xy \geq 1.
$$

Thus the survival boundary is

$$
\boxed{xy = 1}
$$

This curve separates ephemeral and persistent excitations.

## 10.1.9 Phase chart geometry

The CTS phase chart therefore has coordinates

$$
(x, y) = (\Lambda_{lock},\; S_*).
$$

The chart divides into two fundamental regions:

| Region | Condition |
|---|---|
| Ephemeral region | $xy < 1$ |
| Persistent region | $xy > 1$ |

Excitations that lie above the threshold curve survive.

## 10.1.10 Structural interpretation

The phase chart reveals a geometric interpretation of emergence.
Structures can survive in two ways:

- High locking strength (large $x$)
- High persistence capacity (large $y$)

The most durable structures possess both.

## 10.1.11 Mapping the excitation hierarchy

Using approximate values for CTS excitations, their positions on the chart become:

| Excitation | $x$ | $y$ |
|---|---|---|
| Wave | $\approx 0$ | $\ll 1$ |
| Phase-locked mode | Small | $< 1$ |
| Vortex | $\sim 1$ | $\sim 1$ |
| Ring | $\sim 2$–$5$ | $> 1$ |
| Chiral primitive | $\sim 5$–$10$ | $\gg 1$ |
| Shell | $\sim 10$–$50$ | $\gg 10$ |
| Braid | $\gg 50$ | $\gg 100$ |

This mapping naturally produces the structural regions derived earlier.

## 10.1.12 Structural phase diagram

Plotting these points produces a phase diagram with regions corresponding to:

- Background propagation
- Localized precursors
- Closure survival
- Chirality survival
- Shell survival
- Composite survival

The boundaries between these regions will be derived in the following sections.

## 10.1.13 Summary

The CTS Threshold Phase Chart uses two dimensionless variables:

$$
x = \Lambda_{lock}
$$

$$
y = \mathcal{E}_{shell}\,\mathcal{E}\,D\,T_{obj}\,\frac{R}{\dot{R}\, t_{ref}}
$$

The survival boundary is

$$
xy = 1.
$$

This chart provides a geometric representation of structural emergence within the Collapse Tension Substrate.
