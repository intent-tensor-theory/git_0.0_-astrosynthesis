# 9.7 Structural Persistence Scaling

## 9.7.1 Motivation

Section 9.6 introduced the corrected persistence number

$$
S_* = \mathcal{E}_{shell}\,\mathcal{E}\,D\,T_{obj}\,\frac{R}{\dot{R}\, t_{ref}},
$$

which determines whether an excitation survives.
However, to use this equation predictively we must understand how each term scales with excitation size, topology, and environmental conditions.
Persistence scaling reveals why certain structural classes dominate different regions of the CTS survival map.

## 9.7.2 Scaling of retained structure

Let the excitation have characteristic size $L$.
Retained structural energy typically scales with the spatial extent of the structure.
For a $d$-dimensional structure

$$
R \sim \rho L^d,
$$

where $\rho$ is the structural energy density and $d$ is the effective dimensionality of the structure.
Typical dimensionalities include:

| Structure | Effective dimension |
|---|---|
| Wave packet | $d = 3$ |
| Vortex line | $d = 1$ |
| Ring | $d = 1$ |
| Shell | $d = 2$ |
| Braid | $d = 1$–$3$ depending on geometry |

Thus larger structures generally possess larger retained energy.

## 9.7.3 Scaling of structural loss

Loss occurs through dissipation, diffusion, or perturbation.
The structural loss rate can be approximated as

$$
\dot{R} \sim \gamma L^{d-1},
$$

where $\gamma$ represents environmental coupling strength.
This scaling reflects the fact that structural loss occurs primarily across boundaries.

## 9.7.4 Persistence ratio scaling

Substituting the above relations into the persistence number gives

$$
S_* = \mathcal{E}_{shell}\,\mathcal{E}\,D\,T_{obj}\,\frac{\rho L^d}{\gamma L^{d-1} t_{ref}}.
$$

Simplifying yields

$$
\boxed{S_* \sim \mathcal{E}_{shell}\,\mathcal{E}\,D\,T_{obj}\,\frac{\rho}{\gamma\, t_{ref}}\,L}
$$

Thus persistence grows approximately linearly with structural size.

## 9.7.5 Interpretation

This result reveals a crucial principle:
larger structures tend to persist longer than smaller ones, provided structural locking exists.
However, this scaling holds only when structural locking mechanisms prevent fragmentation.
Without locking, large structures become unstable.

## 9.7.6 Topological scaling

Topology modifies persistence scaling through the factor $T_{obj}$.
Approximate topology factors for different excitations are:

| Excitation | $T_{obj}$ |
|---|---|
| Wave | 1 |
| Phase-locked mode | $\sim 1$ |
| Vortex | $\sim 2$–$5$ |
| Ring | $\sim 5$–$10$ |
| Chiral primitive | $\sim 10$–$20$ |
| Shell | $\sim 20$–$100$ |
| Braid | $\gg 100$ |

Thus topological protection dramatically increases persistence.

## 9.7.7 Shell amplification

Shell structures receive an additional persistence multiplier $\mathcal{E}_{shell}$.
Because shell closure distributes stress across the surface, small perturbations do not easily destroy the structure.
Typical shell factors may satisfy

$$
\mathcal{E}_{shell} \sim 10\text{–}100.
$$

This explains why shell-like structures are extremely stable.

## 9.7.8 Environmental scaling

Environmental fluctuations influence persistence through $\gamma$ and $t_{ref}$.
Strong environmental coupling increases loss rate and reduces persistence.
Conversely, weak environmental coupling allows structures to survive longer.
Thus

$$
S_* \propto \frac{1}{\gamma}.
$$

## 9.7.9 Size threshold for survival

Using the scaling relation $S_* \sim C\, L$ where

$$
C = \mathcal{E}_{shell}\,\mathcal{E}\,D\,T_{obj}\,\frac{\rho}{\gamma\, t_{ref}},
$$

the survival condition $S_* > 1$ becomes

$$
L > \frac{1}{C}.
$$

Thus there exists a minimum structural size required for persistence.

## 9.7.10 Persistence hierarchy

Combining all scaling relations yields the following qualitative persistence ordering:

| Excitation | Persistence scaling |
|---|---|
| Wave | Very low |
| Phase-locked mode | Low |
| Vortex | Moderate |
| Ring | Moderate–high |
| Chiral primitive | High |
| Shell | Very high |
| Braid | Extremely high |

Thus persistence increases with both topological protection and structural dimensionality.

## 9.7.11 Implication for CTS emergence

Persistence scaling reveals why emergence proceeds through a hierarchy of structures.
Small weakly locked excitations appear first but decay quickly.
Larger topologically protected structures appear later but persist much longer.
Thus the structural population of the CTS substrate evolves toward increasingly stable excitations.

## 9.7.12 Persistence scaling and the survival map

Substituting the persistence scaling into the survival condition $xy = 1$ gives

$$
\Lambda_{lock}\left(\mathcal{E}_{shell}\,\mathcal{E}\,D\,T_{obj}\,\frac{\rho}{\gamma\, t_{ref}}\,L\right) = 1.
$$

This equation defines the boundary between ephemeral and persistent excitations in the CTS phase chart.

## 9.7.13 Summary

Structural persistence scales approximately linearly with excitation size and strongly with topology.
The corrected persistence number can be approximated as

$$
S_* \sim \mathcal{E}_{shell}\,\mathcal{E}\,D\,T_{obj}\,\frac{\rho}{\gamma\, t_{ref}}\,L.
$$

This scaling explains why large topologically protected structures dominate the persistent region of the CTS survival landscape.
