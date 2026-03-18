# 15.2 Three-Body Braid Structures

## 15.2.1 Motivation

Section 15.1 showed how two persistent objects can combine to form a pair structure through an interaction potential that produces a stable equilibrium separation.
However, when three persistent structures interact, entirely new structural possibilities emerge.
Unlike pairs, three-body systems can produce topological braids — configurations whose stability arises not merely from energetic minima but from topological constraints.
These braided configurations represent the next level of composite persistence in the CTS framework.

## 15.2.2 Three-body interaction geometry

Consider three persistent objects located at
$$
\mathbf{r}_1,\quad \mathbf{r}_2,\quad \mathbf{r}_3.
$$
Define pairwise separations
$$
r_{12}=|\mathbf{r}_1-\mathbf{r}_2|,
$$
$$
r_{23}=|\mathbf{r}_2-\mathbf{r}_3|,
$$
$$
r_{31}=|\mathbf{r}_3-\mathbf{r}_1|.
$$
The total interaction energy becomes
$$
E_{3} =
E_1+E_2+E_3
+
V(r_{12})+V(r_{23})+V(r_{31})
+
V_{3-body}.
$$
The additional term
$$
V_{3-body}
$$
represents collective interactions not reducible to pair potentials.

## 15.2.3 Topological linking

Three-body systems permit topological linking.
The linking number between two trajectories is defined as
$$
Lk =
\frac{1}{4\pi}
\oint\!\oint
\frac{(\mathbf{r}_1-\mathbf{r}_2)\cdot(d\mathbf{r}_1\times d\mathbf{r}_2)}
{|\mathbf{r}_1-\mathbf{r}_2|^3}.
$$
When trajectories wind around one another, the linking number becomes nonzero.
This creates a topological constraint that stabilizes the configuration.

## 15.2.4 Braiding dynamics

A braid occurs when three trajectories interchange positions in time while avoiding intersection.
Let trajectories be
$$
\mathbf{r}_i(t).
$$
The braid condition requires
$$
\mathbf{r}_i(t)\neq \mathbf{r}_j(t)
\quad
(i\neq j)
$$
for all $t$.
This ensures the strands do not intersect.
The topology of these trajectories defines the braid.

## 15.2.5 Braid group structure

Braids are classified by the braid group $B_n$.
For three strands the generators are
$$
\sigma_1,\quad \sigma_2.
$$
These represent elementary strand crossings.
They satisfy the braid relation
$$
\sigma_1\sigma_2\sigma_1 =
\sigma_2\sigma_1\sigma_2.
$$
These algebraic rules classify all possible three-strand braids.

## 15.2.6 Topological stabilization

Braided structures gain stability because the topology cannot change continuously.
To untangle a braid requires breaking and reconnecting strands.
This requires large energy.
Thus braided configurations exhibit large effective locking energy
$$
E_{lock}^{braid}.
$$

## 15.2.7 Persistence condition

For a braid to remain stable we require
$$
S_*^{braid} =
\mathcal{E}_{shell} \cdot \mathcal{E}_D \cdot T_{obj} \cdot
\frac{E_{lock}^{braid}}{\dot{R}\,t_{ref}}
$$
The topology factor
$$
T_{obj}
$$
is large for braided structures.
Thus braids often exhibit extremely strong persistence.

## 15.2.8 Energy scaling

The energy of a braid grows with strand tension and curvature.
A simple estimate is
$$
E_{braid} \sim T L + \kappa \int k^2\, ds
$$
where $T$ = strand tension, $L$ = strand length, $k$ = curvature.
Higher curvature increases energy cost, stabilizing smooth braid configurations.

## 15.2.9 Braided oscillation modes

Braids support several dynamical modes.
Examples include

| Mode | Description |
|---|---|
| twist modes | strands rotate around axis |
| stretch modes | braid length oscillates |
| kink modes | localized bending |

These modes allow braids to store energy without breaking topology.

## 15.2.10 Comparison with pair structures

Pairs rely on energy minima for stability.
Braids rely on topological constraints.
Thus braids are typically more persistent.

| Structure | Stabilization |
|---|---|
| pair | energy minimum |
| braid | topology |

This distinction is important for composite persistence.

## 15.2.11 Phase chart interpretation

Within the CTS survival map, braided structures lie in the upper extreme of the composite persistence region.
They exhibit
$$
x = \Lambda_{lock} \gg 1
$$
$$
y = S_* \gg 1.
$$
Thus braided structures represent some of the most persistent excitations in the CTS hierarchy.

## 15.2.12 Structural significance

Braided structures introduce a powerful persistence mechanism:
topological protection.
Because topology cannot change continuously, braided structures resist perturbations that would destroy simpler configurations.

## 15.2.13 Emergence role

Braids may serve as the scaffolding for complex structural systems.
They can trap energy, support oscillations, and link multiple persistent objects.
Thus they represent a key step toward higher-order structural architectures.

## 15.2.14 CTS hierarchy extension

Including braids extends the structural hierarchy to
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
\text{pairs}
\rightarrow
\text{braids}.
$$
Each stage introduces a stronger persistence mechanism.

## 15.2.15 Summary

Three-body braid structures arise when persistent objects interact in ways that produce topological linking.
Because braid topology cannot change without structural reconnection, braided configurations possess large effective locking energy and extremely high persistence.
These structures represent one of the most powerful composite persistence mechanisms within the Collapse Tension Substrate.

Composite Thresholds
This section derives the mathematical conditions under which multi-body structures transition from transient assemblies to persistent composite architectures.

