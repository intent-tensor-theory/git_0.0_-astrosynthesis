# 10.5 Mapping the Structural Regions

## 10.5.1 Motivation

Sections 10.1–10.4 established the mathematical structure of the CTS Threshold Phase Chart.
Coordinates:
$$
x = \Lambda_{lock}
$$
$$
y =
\frac{\mathcal{E}_{shell}}{\mathcal{E}_D}\,
T_{obj}
\frac{R}{\dot{R}\,t_{ref}}
$$
Survival boundary:
$$
xy = 1.
$$
However, the phase chart contains distinct structural regions corresponding to different classes of excitations.
These regions form the CTS Survival Map.
This section derives those regions explicitly.

The six regions are:
- Region I — Background propagation
- Region II — Localized precursors
- Region III — Closure survival
- Region IV — Chirality survival
- Region V — Shell survival
- Region VI — Composite survival

Each region occupies a distinct domain of the $(x,y)$ plane and corresponds to a different dominant stabilization mechanism.

## 10.5.2 Structural classification principle

The survival map divides the phase chart according to the dominant stabilization mechanism.
Each region corresponds to a specific structural feature:

| Region | Dominant mechanism |
|---|---|
| Background propagation | wave dynamics |
| Localized precursors | nonlinear coherence |
| Closure survival | geometric closure |
| Chirality survival | helicity locking |
| Shell survival | multi-axis locking |
| Composite survival | topological linking |

Each region corresponds to increasing structural complexity.
The regions are separated by boundaries defined by conditions on $x$, $y$, and derived quantities.

## 10.5.3 Region I — Background propagation

This region occupies the lower-left corner of the phase chart.
Conditions:
$$
x \approx 0
$$
$$
y \ll 1.
$$
Thus
$$
xy \ll 1.
$$
Structures in this region consist primarily of linear wave excitations.
These excitations satisfy the linearized CTS field equation and carry the dispersion relation
$$
\omega(k) = \sqrt{2ak^2 + 2uk^4 + 2r}.
$$
Their energy is
$$
E_{wave} = (ak^2 + uk^4 + r)\,A^2\,V.
$$
Because the amplitude $A$ can be arbitrarily small, the formation energy approaches zero.

Properties:

| Property | Value |
|---|---|
| formation energy | extremely low |
| locking energy | negligible |
| topology factor | $T_{obj} = 1$ |
| persistence | very low |

These excitations dominate the background activity of the substrate.
They are extremely abundant but decay rapidly on the timescale $\tau = 1/\gamma$.

## 10.5.4 Region II — Localized precursors

Moving slightly upward and rightward we reach the precursor region.
Typical values:
$$
x \sim 0.3\text{–}1
$$
$$
y < 1.
$$
Thus
$$
xy < 1
$$
so these structures remain below the persistence threshold.
They are formed by nonlinear wave coupling.
When the nonlinear term in the CTS field equation satisfies
$$
|s\Phi^3| \sim |r\Phi|,
$$
coherent packets emerge with amplitude
$$
|\Phi| \sim \sqrt{\frac{r}{s}}.
$$
These packets are spatially localized and phase-locked.
They carry a small but nonzero locking energy
$$
E_{lock} > 0,
$$
which yields
$$
\Lambda_{lock} = \frac{E_{lock}}{E_{form}} \sim 0.3\text{–}1.
$$
Although they remain transient, localized precursors act as seeds for higher-order structures.

Properties:

| Property | Value |
|---|---|
| formation energy | low |
| locking energy | small but nonzero |
| topology factor | $T_{obj} \approx 1$ |
| persistence | below threshold |

## 10.5.5 Region III — Closure survival

The closure survival region is the first region lying above the persistence threshold.
Approximate coordinates:
$$
1 \lesssim x \lesssim 3
$$
$$
y \gtrsim 1.
$$
Thus
$$
xy > 1.
$$
Closure occurs when a circulating flow reconnects with itself.
Mathematically, closure occurs when a vortex filament satisfies
$$
\mathbf{r}(s+L) = \mathbf{r}(s)
$$
for some periodic parameter $s$.
Closure introduces a conserved circulation
$$
\Gamma = \oint \mathbf{v}\cdot d\mathbf{l}.
$$
The energy of a closed vortex ring of radius $R$ is
$$
E_{ring}
\approx
\rho\,\kappa^2\,R
\left(
\ln\frac{8R}{a} - 2
\right).
$$
Topology protection raises the persistence number above unity, establishing the first class of durable structures.

Properties:

| Property | Value |
|---|---|
| formation energy | moderate |
| locking energy | moderate |
| topology factor | $T_{obj} > 1$ |
| persistence | $xy \gtrsim 1$ |

## 10.5.6 Region IV — Chirality survival

Beyond closure, structures may acquire torsion.
Approximate coordinates:
$$
5 \lesssim x \lesssim 10
$$
$$
y \gg 1.
$$
Chirality appears when the torsion parameter satisfies $\tau \neq 0$.
This yields nonzero helicity
$$
H =
\int
\mathbf{v}\cdot(\nabla\times\mathbf{v})\,d^3x
\neq 0.
$$
Helicity is a robust topological invariant: it cannot be removed without reconnection events.
Thus chiral structures possess substantially higher locking strength and persistence than simple closure structures.

Properties:

| Property | Value |
|---|---|
| formation energy | moderate–high |
| locking energy | high |
| topology factor | $T_{obj} \gg 1$ |
| persistence | $xy \gg 1$ |

## 10.5.7 Region V — Shell survival

Shell structures arise when multiple chiral excitations interact and organize into a closed surface.
Approximate coordinates:
$$
10 \lesssim x \lesssim 50
$$
$$
y \gg 10.
$$
Shell closure requires multi-axis force balance
$$
\sum_{i=1}^{N_f} \mathbf{F}_i = 0.
$$
The shell energy satisfies
$$
E_{shell} = \oint \sigma\,dA
$$
where $\sigma$ is the surface tension of the CTS interface.
Because the shell encloses volume, it carries a substantially larger locking energy than open structures.
This places shell structures deep within the persistent regime.

Properties:

| Property | Value |
|---|---|
| formation energy | high |
| locking energy | very high |
| topology factor | $T_{obj} \gg 1$ |
| persistence | $xy \gg 10$ |

## 10.5.8 Region VI — Composite survival

The composite survival region contains structures formed by topological linking of multiple persistent excitations.
Approximate coordinates:
$$
x \gg 50
$$
$$
y \gg 100.
$$
The defining topological condition is
$$
Lk \neq 0
$$
where $Lk$ is the linking number of the constituent loops.
Linking introduces mutual topological constraints that cannot be released without global reconnection.
Thus composite structures achieve the highest persistence values accessible within the CTS framework.

Properties:

| Property | Value |
|---|---|
| formation energy | very high |
| locking energy | extremely high |
| topology factor | $T_{obj} \gg 1$ |
| persistence | $xy \gg 100$ |

## 10.5.9 Phase chart coordinates summary

Combining the regional analyses yields the following structural atlas:

| Region | Name | $x$ | $y$ |
|---|---|---|---|
| I | Background propagation | $\approx 0$ | $\ll 1$ |
| II | Localized precursors | $0.3$–$1$ | $< 1$ |
| III | Closure survival | $1$–$3$ | $\approx 1$ |
| IV | Chirality survival | $5$–$10$ | $\gg 1$ |
| V | Shell survival | $10$–$50$ | $\gg 10$ |
| VI | Composite survival | $\gg 50$ | $\gg 100$ |

This table provides the first approximation of the CTS structural atlas within the Threshold Phase Chart.

## 10.5.10 Structural boundaries

The regions are separated by approximate boundary conditions.
The primary survival boundary is
$$
xy = 1.
$$
This boundary separates transient excitations (Regions I and II) from persistent structures (Regions III–VI).
Secondary boundaries between persistent regions are not sharp; they correspond to transitions between dominant stabilization mechanisms.
The approximate boundary conditions are:

| Boundary | Condition |
|---|---|
| I / II | $x \gtrsim 0.3$ |
| II / III | $xy = 1$ |
| III / IV | $\tau \neq 0$ (torsion onset) |
| IV / V | multi-axis force balance achieved |
| V / VI | $Lk \neq 0$ (linking onset) |

## 10.5.11 Emergence pathway

The structural regions define a natural pathway of increasing complexity.
Beginning from the background propagation layer, the emergence pathway follows
$$
\text{waves}
\rightarrow
\text{precursors}
\rightarrow
\text{closure}
\rightarrow
\text{chirality}
\rightarrow
\text{shells}
\rightarrow
\text{composites}.
$$
Each step introduces a new stabilization mechanism that increases $x$, $y$, or both.
Each step also introduces a new conserved quantity:

| Transition | New conserved quantity |
|---|---|
| waves $\rightarrow$ precursors | coherence phase |
| precursors $\rightarrow$ closure | circulation $\Gamma$ |
| closure $\rightarrow$ chirality | helicity $H$ |
| chirality $\rightarrow$ shells | surface area |
| shells $\rightarrow$ composites | linking number $Lk$ |

This hierarchy of conserved quantities underlies the hierarchy of structural persistence.

## 10.5.12 Summary

The CTS Threshold Phase Chart is partitioned into six structural regions corresponding to six classes of excitations.
These regions are ordered by the dominant stabilization mechanism:
wave dynamics, nonlinear coherence, geometric closure, helicity conservation, multi-axis surface locking, and topological linking.
The primary survival boundary
$$
xy = 1
$$
divides transient excitations from persistent structures.
Together these regions define the CTS Survival Map, which provides a unified geometric classification of all structural excitations within the Collapse Tension Substrate.
