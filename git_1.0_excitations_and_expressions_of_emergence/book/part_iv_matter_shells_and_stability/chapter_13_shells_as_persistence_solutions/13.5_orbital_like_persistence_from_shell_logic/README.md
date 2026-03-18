# 13.5 Orbital-Like Persistence from Shell Logic

## 13.5.1 Motivation

Sections 13.1–13.4 established that shell structures are highly stable because of:
- multi-fan locking
- curvature memory
- nested shell reinforcement

However shells also generate another important structural phenomenon.
They naturally produce stable excitation pathways around the shell surface or around nested shell layers.
These pathways resemble orbital persistence states.
The goal of this section is to derive mathematically why shell architectures support these stable orbital excitations.

## 13.5.2 Bound excitation states

Consider a persistent shell structure with radius $R$.
An excitation interacting with the shell experiences a restoring potential due to curvature and structural locking.
We model the radial potential as
$$
V(r) = V_0 + \frac{\alpha}{(r-R)^2}.
$$
This potential confines excitations near the shell boundary.

## 13.5.3 Effective radial equation

The dynamics of an excitation near the shell can be written using an effective radial equation
$$
m\frac{d^2r}{dt^2} = -\frac{dV}{dr}.
$$
Substituting the shell potential yields
$$
m\frac{d^2r}{dt^2} =
-\frac{2\alpha}{(r-R)^3}.
$$
The restoring force increases rapidly as the excitation approaches the shell surface.

## 13.5.4 Angular motion

If the excitation possesses tangential velocity $v_\theta$, angular momentum becomes
$$
L = m r^2 \dot{\theta}.
$$
Conservation of angular momentum allows the excitation to circulate around the shell.
Thus the total effective potential becomes
$$
V_{eff}(r) =
V(r) + \frac{L^2}{2mr^2}.
$$

## 13.5.5 Stable orbital radius

Stable orbits occur when
$$
\frac{dV_{eff}}{dr} = 0.
$$
This gives the equilibrium radius
$$
\frac{2\alpha}{(r-R)^3} =
\frac{L^2}{mr^3}.
$$
Solutions to this equation determine allowed orbital trajectories around the shell.

## 13.5.6 Quantized excitation modes

Shell geometry imposes periodic boundary conditions
$$
\theta \sim \theta + 2\pi.
$$
Thus allowed angular modes satisfy
$$
k_n = \frac{n}{R}.
$$
Corresponding energy levels become
$$
E_n =
\frac{\hbar^2 n^2}{2mR^2}.
$$
These represent discrete orbital excitation states.

## 13.5.7 Surface wave modes

Excitations can also propagate along the shell surface.
Surface modes satisfy the Laplace–Beltrami equation
$$
\nabla_S^2 \psi + \lambda \psi = 0.
$$
For a spherical shell the eigenfunctions are spherical harmonics $Y_\ell^m(\theta,\phi)$.
Corresponding eigenvalues are
$$
\lambda_\ell = \frac{\ell(\ell+1)}{R^2}.
$$
These modes represent stable oscillations along the shell surface.

## 13.5.8 Radial standing waves

Nested shells allow standing waves between layers.
Let shells exist at radii $R_1 < R_2$.
Radial modes satisfy
$$
k_n = \frac{n\pi}{R_2-R_1}.
$$
Energy levels become
$$
E_n =
\frac{\hbar^2 n^2\pi^2}{2m(R_2-R_1)^2}.
$$
Thus nested shells naturally support radial excitation states.

## 13.5.9 Orbital persistence

These orbital modes remain stable because shell curvature confines excitations.
Persistence requires
$$
E_{orb} < E_{lock}.
$$
When this condition holds, orbital excitations remain bound to the shell.

## 13.5.10 Structural interpretation

Shell architectures therefore support three types of excitation states:

| Mode | Description |
|---|---|
| surface modes | waves along shell surface |
| orbital modes | circulation around shell |
| radial modes | standing waves between shells |

Together these modes create complex internal dynamics.

## 13.5.11 Energy hierarchy

Typical energy ordering is
$$
E_{surface}
<
E_{orbital}
<
E_{radial}.
$$
Surface modes require minimal energy.
Radial modes require the most energy because they compress shell spacing.

## 13.5.12 Persistence condition for orbitals

Orbital modes remain stable when
$$
S_*^{(orbital)} > 1.
$$
Since shells already possess large persistence numbers, orbital states typically inherit this stability.

## 13.5.13 Emergence implication

This result suggests an important structural mechanism.
Shell architectures naturally generate stable orbital excitation states.
Thus orbital behavior emerges from shell geometry rather than requiring additional forces.

## 13.5.14 CTS interpretation

Within the CTS framework orbital states represent secondary excitations bound to persistent shell structures.
These excitations circulate within the curvature field produced by the shell.
Thus shells act as structural scaffolds for additional dynamic modes.

## 13.5.15 Summary

Shell geometries create natural confinement potentials that support stable orbital excitations.
These modes arise from angular momentum conservation, surface curvature, and boundary conditions imposed by shell geometry.
Nested shells further support radial standing waves.
Thus shell architectures generate a rich spectrum of persistent excitation states within the Collapse Tension Substrate.
