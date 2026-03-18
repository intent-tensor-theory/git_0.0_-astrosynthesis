# 10.2 Survival Number in Chart Form

## 10.2.1 Motivation

Section 10.1 defined the two variables that form the axes of the CTS Threshold Phase Chart:

$$
x = \Lambda_{lock}
$$

$$
y = \mathcal{E}_{shell}\,\mathcal{E}\,D\,T_{obj}\,\frac{R}{\dot{R}\, t_{ref}}
$$

These variables measure two independent structural properties:

- Locking strength
- Persistence capacity

However, to construct the threshold curve separating ephemeral excitations from persistent structures, we must rewrite the persistence condition in terms of these phase variables.

## 10.2.2 Original persistence condition

From Chapter 9 the corrected persistence number is

$$
S_* = \mathcal{E}_{shell}\,\mathcal{E}\,D\,T_{obj}\,\frac{R}{\dot{R}\, t_{ref}}.
$$

The persistence threshold occurs when $S_* = 1$.
Structures with $S_* > 1$ survive.

## 10.2.3 Inclusion of locking energy

Persistence alone does not guarantee structural survival.
A structure may have strong persistence properties but still fail to appear frequently if formation energy dominates.
Thus survival depends on both:

- Persistence strength
- Locking strength

To incorporate both effects we define the survival number $S_{surv}$.

## 10.2.4 Definition of the survival number

The survival number combines persistence with locking strength:

$$
\boxed{S_{surv} = \Lambda_{lock}\,\mathcal{E}_{shell}\,\mathcal{E}\,D\,T_{obj}\,\frac{R}{\dot{R}\, t_{ref}}}
$$

Substituting the phase chart variables gives

$$
S_{surv} = x\, y.
$$

## 10.2.5 Survival threshold

The survival threshold occurs when

$$
S_{surv} = 1.
$$

Thus

$$
\boxed{xy = 1}
$$

defines the boundary between ephemeral and persistent structures.

## 10.2.6 Geometry of the threshold

The equation $xy = 1$ represents a rectangular hyperbola in the phase plane.
Solving for $y$ gives

$$
y = \frac{1}{x}.
$$

Thus the threshold curve decreases as locking strength increases.

## 10.2.7 Physical interpretation

The hyperbolic boundary reveals two distinct survival mechanisms.

**Persistence-dominated survival:** Structures with large $y$ can survive even with small locking strength.
Examples:
- Coherent vortices
- Rings

**Locking-dominated survival:** Structures with large $x$ can survive even with moderate persistence.
Examples:
- Shells
- Braids

## 10.2.8 Regions of the phase chart

The threshold curve divides the phase chart into two fundamental regions.

**Ephemeral region** ($xy < 1$): Structures decay faster than they stabilize.
Typical examples:
- Waves
- Weak coherent packets

**Persistent region** ($xy > 1$): Structures stabilize faster than they decay.
Typical examples:
- Vortices
- Rings
- Shells
- Braids

## 10.2.9 Logarithmic representation

Because structural parameters span many orders of magnitude, the phase chart is best plotted on logarithmic axes.
Define

$$
X = \log x, \qquad Y = \log y.
$$

The survival boundary becomes

$$
X + Y = 0.
$$

Thus the threshold appears as a straight line with slope $-1$ on a log–log chart.

## 10.2.10 Structural trajectories

As an excitation evolves, its position in the phase chart may move.
For example:

- Increasing coherence raises $y$
- Stronger locking raises $x$
- Environmental fluctuations lower $y$

Thus excitations can migrate across the survival boundary.

## 10.2.11 Example positions

Approximate locations of several excitation classes illustrate the chart structure.

| Excitation | $x$ | $y$ | Survival |
|---|---|---|---|
| Wave | $\sim 0$ | $\ll 1$ | Ephemeral |
| Phase packet | $\sim 0.3$ | $< 1$ | Ephemeral |
| Vortex | $\sim 1$ | $\sim 1$ | Marginal |
| Ring | $\sim 3$ | $> 1$ | Persistent |
| Shell | $\sim 20$ | $\gg 10$ | Highly persistent |
| Braid | $\gg 50$ | $\gg 100$ | Extremely persistent |

These positions produce the structural regions of the survival map.

## 10.2.12 Emergence interpretation

The hyperbolic survival boundary provides a mathematical interpretation of emergence:
structures appear when stabilization mechanisms overcome structural loss.
The CTS framework therefore interprets emergence as a geometric threshold crossing in structural phase space.

## 10.2.13 Summary

Expressing the persistence condition in phase chart coordinates yields the survival number

$$
S_{surv} = xy.
$$

The threshold

$$
xy = 1
$$

defines the boundary separating ephemeral excitations from persistent structures.
This hyperbolic curve forms the central organizing feature of the CTS Threshold Phase Chart.
