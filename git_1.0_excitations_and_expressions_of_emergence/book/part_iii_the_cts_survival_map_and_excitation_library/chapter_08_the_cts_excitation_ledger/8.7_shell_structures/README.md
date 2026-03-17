# 8.7 Shell Structures

## 8.7.1 From rings to shells

Sections 8.4–8.6 introduced a progression of localized excitations:

| Excitation | Structure |
|---|---|
| open vortex | line defect |
| closed ring | localized circulation loop |
| chiral primitive | twisted ring |

These excitations remain essentially one-dimensional structures embedded in space.
The next level of organization arises when multiple circulation channels combine to form a closed surface structure.
These structures are called shell excitations.
Shells represent the first CTS structures capable of enclosing internal volume and supporting internal excitations.

## 8.7.2 Definition of a shell excitation

Let a shell be defined by a closed surface

$$
\Sigma = \partial V
$$

that encloses a spatial region $V$.
The shell is maintained by balanced structural flows or tension channels along its surface.
Mathematically, these channels can be represented by vector fluxes

$$
\mathbf{F}_i = F_i\,\hat{n}_i
$$

distributed across the shell.

## 8.7.3 Multi-fan locking condition

For the shell to remain stable the structural fluxes must balance:

$$
\sum_i \mathbf{F}_i = 0.
$$

The minimal symmetric shell configuration occurs when

$$
N_f = 6.
$$

This configuration corresponds to the six-fan locking structure discussed earlier.

## 8.7.4 Geometric interpretation

The six-fan configuration corresponds to three orthogonal tension axes:

$$
\pm x,\; \pm y,\; \pm z.
$$

Each axis contains a pair of opposing channels.
The vector balance

$$
\sum_i \mathbf{F}_i = 0
$$

guarantees mechanical equilibrium.
This symmetry distributes stress evenly across the shell.

## 8.7.5 Surface energy of the shell

The shell possesses surface tension $\sigma$.
Thus the surface energy is

$$
E_{surf} = \sigma \int_\Sigma dA.
$$

For a spherical shell of radius $R$:

$$
E_{surf} = 4\pi\sigma R^2.
$$

This energy resists expansion of the shell.

## 8.7.6 Curvature energy

Curvature also contributes to shell stability.
The curvature energy is

$$
E_{curv} = \kappa_c \int_\Sigma H^2\,dA,
$$

where $H$ is the mean curvature.
For a sphere of radius $R$, $H = 1/R$.
This term penalizes irregular shell shapes.

## 8.7.7 Internal pressure

If the shell encloses a field or excitation inside the volume $V$, an internal pressure develops.
The pressure difference across the shell obeys the Young–Laplace relation

$$
\Delta P = 2\sigma H.
$$

For a spherical shell:

$$
\Delta P = \frac{2\sigma}{R}.
$$

This pressure stabilizes the enclosed region.

## 8.7.8 Shell stability condition

Combining tension and curvature terms gives the approximate shell energy

$$
E_{shell} = 4\pi\sigma R^2 + 4\pi\kappa_c.
$$

A stable shell occurs when internal pressure balances surface tension:

$$
P_{int}\,R \sim \sigma.
$$

This relation determines the equilibrium shell radius.

## 8.7.9 Coherence of shell channels

For the shell to remain stable, the structural channels must remain phase-coherent.
Define the coherence parameter

$$
C = \left| \frac{1}{N_f} \sum_{i=1}^{N_f} e^{i\phi_i} \right|.
$$

Stable shells require

$$
C \approx 1.
$$

Low coherence leads to destructive interference between channels.

## 8.7.10 Shell topology

The shell surface possesses topology equivalent to a sphere.
The Euler characteristic of a spherical shell is

$$
\chi = 2.
$$

This topology allows the shell to host internal excitations and structural defects.

## 8.7.11 Shell persistence

Shell structures benefit from multiple persistence mechanisms:

| Mechanism | Effect |
|---|---|
| bounded volume | closure |
| multi-fan locking | mechanical equilibrium |
| curvature energy | shape stability |
| topological protection | structural protection |

Thus shell structures possess a large topology factor

$$
T_{obj} \gg 1.
$$

## 8.7.12 Persistence number for shells

Including shell locking gives

$$
S = \mathcal{E}_{shell}\,\mathcal{E}\,D\,T_{obj}\,\chi_c\,\frac{R}{\dot{R}\,t_{ref}}.
$$

## 8.7.13 Role in the CTS excitation hierarchy

The hierarchy now becomes

| Excitation | Dominant mechanism |
|---|---|
| wave | oscillation |
| phase-locked wave | nonlinear coherence |
| open vortex | circulation |
| closed ring | closure |
| chiral primitive | directional topology |
| shell | multi-axis locking |

Shells represent the first excitations capable of supporting nested internal structures.

## 8.7.14 Ledger entry for shell structures

| Parameter | Approximate value |
|---|---|
| excitation type | shell structure |
| formation energy | very high |
| locking energy | very high |
| topology factor | $T_{obj} \gg 1$ |
| persistence | extremely high |

Thus shells occupy the shell survival region of the CTS survival map.

## 8.7.15 Summary

Shell excitations arise when multiple circulation channels organize into a closed surface stabilized by multi-fan locking.
These structures possess strong persistence due to closure, curvature stabilization, and topological protection.
Shells therefore represent one of the most stable classes of excitations in the CTS ledger.
