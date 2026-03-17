# 13.1 Shells as Multi-Fan Lock Events

## 13.1.1 Motivation

Chapters 10–12 established that durable structures arise when excitations cross the persistence threshold
$$
xy = 1
$$
and move into regions where
$$
x = \Lambda_{lock} \gg 1,
\qquad
y = S_* \gg 1.
$$
The structural class that most naturally satisfies these conditions is the shell architecture.
Shells represent one of the most stable persistence solutions of the Collapse Tension Substrate because they introduce multi-directional locking across a closed surface.

## 13.1.2 From line locking to surface locking

Earlier structural stages involved one-dimensional stabilization.

| Structure | Locking dimension |
|---|---|
| vortex filament | 1D |
| vortex ring | 1D closed |
| helical filament | 1D torsional |

These structures concentrate tension along a line.
Shells introduce a new configuration: locking distributed across a surface.
This dramatically increases stability.

## 13.1.3 Surface parameterization

A shell structure can be described as a closed surface $\mathbf{r}(u,v)$ where
$$
u \in [0,U], \quad v \in [0,V].
$$
Closure requires periodic boundary conditions
$$
\mathbf{r}(u+U,v) = \mathbf{r}(u,v)
$$
$$
\mathbf{r}(u,v+V) = \mathbf{r}(u,v).
$$
These conditions ensure the surface has no boundaries.

## 13.1.4 Principal curvature directions

At each point on the surface two principal curvature directions exist.
Let $k_1,\, k_2$ denote the principal curvatures.
These define the mean curvature
$$
H = \frac{1}{2}(k_1 + k_2)
$$
and Gaussian curvature
$$
K = k_1 k_2.
$$
Shell stability arises from maintaining equilibrium in both curvature directions simultaneously.

## 13.1.5 Multi-fan locking

In the CTS framework shell stability is interpreted as multi-fan locking.
Instead of a single stabilization channel, shells possess many.
Let the locking forces be $\mathbf{F}_1, \mathbf{F}_2, \dots, \mathbf{F}_{N_f}$.
Equilibrium requires
$$
\sum_{i=1}^{N_f} \mathbf{F}_i = 0.
$$
This balance prevents the shell from collapsing or expanding.

## 13.1.6 Locking energy of shells

Each locking channel contributes stabilization energy.
Thus
$$
E_{lock} = \sum_{i=1}^{N_f} E_{bond,i}.
$$
If the number of channels increases, the total locking energy grows rapidly.
Thus shells typically satisfy
$$
E_{lock} \gg E_{form}.
$$

## 13.1.7 Lock ratio of shell structures

The lock ratio becomes
$$
\Lambda_{lock} = \frac{E_{lock}}{E_{form}}.
$$
Typical values for shells are
$$
10 \lesssim \Lambda_{lock} \lesssim 50.
$$
This places shells deep in the persistent region of the CTS phase chart.

## 13.1.8 Persistence amplification

The persistence number is
$$
S_* =
\mathcal{E}_{shell} \cdot \mathcal{E}_D \cdot T_{obj} \cdot
\frac{R}{\dot{R}\,t_{ref}}.
$$
For shell structures the shell factor $\mathcal{E}_{shell}$ becomes large because multiple stabilization directions reinforce each other.
Thus
$$
S_* \gg 10.
$$

## 13.1.9 Structural rigidity

Shell rigidity arises because deformation requires simultaneous changes in many directions.
The elastic energy of a shell deformation can be written
$$
E_{def} =
\int
\left(
\kappa (2H)^2
+
\bar{\kappa}K
\right)
dA.
$$
Large curvature penalties suppress deformation.

## 13.1.10 Shell equilibrium condition

Equilibrium shapes satisfy
$$
\delta E_{shell} = 0.
$$
This leads to the shape equation
$$
\kappa(2H)(2H^2 - 2K) + \Delta H = 0.
$$
Solutions to this equation define stable shell geometries.

## 13.1.11 Examples of shell geometries

Common shell solutions include:

| Geometry | Curvature |
|---|---|
| sphere | constant curvature |
| torus | mixed curvature |
| polyhedral shell | discrete curvature |

Each geometry satisfies multi-fan locking conditions.

## 13.1.12 Energy confinement

Shell architectures confine energy within a closed surface.
Let $\mathcal{E}(x)$ represent energy density.
Shell confinement ensures
$$
\int_{inside} \mathcal{E}\,dV \gg
\int_{outside} \mathcal{E}\,dV.
$$
Thus shells trap energy internally.

## 13.1.13 Stability against perturbations

Shells tolerate larger perturbations than line structures.
Stability requires
$$
E_{pert} < E_{lock}.
$$
Because shell locking energy is large, moderate disturbances cannot destroy the structure.

## 13.1.14 Shells as persistence solutions

The key insight is that shells represent a natural solution to the persistence problem.
They simultaneously maximize:
- locking energy
- curvature stability
- energy confinement.

Thus shells occupy a highly stable region of structural phase space.

## 13.1.15 Summary

Shell structures arise when excitations develop closed surfaces stabilized by multi-fan locking.
Because stabilization occurs across many directions simultaneously, shell architectures produce extremely large lock ratios and persistence numbers.
This makes shells one of the most robust persistence solutions within the Collapse Tension Substrate.
