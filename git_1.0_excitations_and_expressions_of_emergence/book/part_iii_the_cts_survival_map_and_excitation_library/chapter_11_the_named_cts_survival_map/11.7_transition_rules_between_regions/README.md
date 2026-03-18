# 11.7 Transition Rules Between Regions

## 11.7.1 Motivation

Sections 11.1–11.6 defined the six structural regions of the CTS survival map:
- Background propagation
- Localized precursors
- Closure survival
- Chirality survival
- Shell survival
- Composite survival

However, excitations are not static objects within the phase chart.
Instead they evolve dynamically as environmental conditions and internal structure change.
Thus excitations move through the phase chart according to transition rules.
These rules determine when a structure migrates from one region to another.

## 11.7.2 Phase-space coordinates

Recall that every excitation occupies a location
$$
(x,y)
$$
in the survival map where
$$
x = \Lambda_{lock}
$$
$$
y =
\frac{\mathcal{E}_{shell}}{\mathcal{E}_D}\,
T_{obj}
\frac{R}{\dot{R}\,t_{ref}}.
$$
Transitions occur whenever the parameters controlling $x$ or $y$ change.

## 11.7.3 Evolution equations

Let the excitation coordinates evolve in time
$$
x = x(t), \qquad y = y(t).
$$
The motion of the excitation in phase space can be written as
$$
\frac{dx}{dt} = f_x(\Phi, \nabla\Phi, T_{eff})
$$
$$
\frac{dy}{dt} = f_y(\Phi, \nabla\Phi, T_{eff}).
$$
These functions describe how locking strength and persistence change due to interactions.

## 11.7.4 Wave → precursor transition

The first transition occurs when nonlinear wave coupling creates coherent structures.
Mathematically this happens when the nonlinear interaction term in the CTS field equation becomes comparable to the linear term:
$$
|s \Phi^3| \sim |r \Phi|.
$$
This yields the threshold amplitude
$$
|\Phi| \sim \sqrt{\frac{r}{s}}.
$$
Above this amplitude, coherent packets form and the excitation moves into the precursor region.

## 11.7.5 Precursor → closure transition

Localized packets may develop circulation.
Circulation appears when phase gradients satisfy
$$
\nabla \times (\nabla \theta) \neq 0.
$$
Once circulation becomes nonzero, vortex filaments form.
If the filament reconnects with itself, closure occurs and the excitation enters the closure survival region.

## 11.7.6 Closure → chirality transition

A closed vortex ring may acquire torsion through perturbations or interactions.
Chirality appears when the torsion parameter satisfies
$$
\tau \neq 0.
$$
The helicity then becomes nonzero
$$
H =
\int
\mathbf{v}\cdot(\nabla\times\mathbf{v})\,d^3x
\neq 0.
$$
Once helicity becomes significant, the structure enters the chirality survival region.

## 11.7.7 Chirality → shell transition

Shell formation occurs when multiple chiral structures interact and form a closed surface.
Mathematically this corresponds to satisfying the multi-axis force balance condition
$$
\sum_{i=1}^{N_f} \mathbf{F}_i = 0.
$$
This condition creates surface closure and moves the structure into the shell survival region.

## 11.7.8 Shell → composite transition

Composite formation occurs when persistent structures become topologically linked.
The defining condition is
$$
Lk \neq 0
$$
where $Lk$ is the linking number.
Once linking occurs, the structure becomes a topological composite and moves into the composite region.

## 11.7.9 Reverse transitions

Transitions are not strictly one-directional.
Strong perturbations may drive structures back into lower regions.
Examples include:

| Transition | Cause |
|---|---|
| composite → shell | reconnection |
| shell → chirality | surface rupture |
| chirality → closure | torsion loss |
| closure → precursor | ring collapse |

These reverse transitions correspond to decreases in $x$ or $y$.

## 11.7.10 Environmental control parameters

Several environmental parameters influence transitions:

| Parameter | Effect |
|---|---|
| $T_{eff}$ | fluctuation energy |
| $\gamma$ | dissipation rate |
| $a,u,r,s$ | field constants |

Changes in these parameters alter the phase-space trajectories of excitations.

## 11.7.11 Transition diagram

The hierarchical transition structure can be summarized as

```
waves
  ↓
localized precursors
  ↓
vortex closure
  ↓
chirality
  ↓
shell formation
  ↓
composite structures
```

Each transition corresponds to the introduction of a new stabilization mechanism.

## 11.7.12 Phase-space trajectory example

Consider a precursor excitation with coordinates
$$
(x,y) = (0.5,0.7).
$$
If nonlinear interactions increase locking energy such that
$$
x \rightarrow 1.2
$$
and persistence rises to
$$
y \rightarrow 1.1,
$$
then
$$
xy = 1.32 > 1.
$$
The excitation crosses the survival boundary and becomes persistent.

## 11.7.13 Structural interpretation

Transitions between survival-map regions represent qualitative structural changes.
They correspond to the appearance of new structural invariants:

| Transition | New invariant |
|---|---|
| waves → precursors | coherence |
| precursors → closure | circulation |
| closure → chirality | helicity |
| chirality → shell | curvature closure |
| shell → composite | linking number |

Each invariant increases persistence.

## 11.7.14 Summary

Transitions between CTS survival regions occur when structural parameters evolve such that
$$
x(t), y(t)
$$
cross the boundaries separating regions of the phase chart.
Each transition introduces a new stabilization mechanism that increases persistence.
These rules define the dynamical pathway through which emergence proceeds within the Collapse Tension Substrate.
