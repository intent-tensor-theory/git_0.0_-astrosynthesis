# 13.2 Curvature as Closure Memory

## 13.2.1 Motivation

Section 13.1 showed that shells achieve high persistence through multi-fan locking across a closed surface. However, this raises a deeper structural question:
How does a shell remember that it is closed?
If a perturbation slightly deforms the shell, what mechanism restores the original geometry?
The answer lies in curvature memory.
Curvature encodes geometric information that allows the structure to recover its equilibrium configuration.

## 13.2.2 Surface geometry

A shell is described by a surface embedding
$$
\mathbf{r}(u,v)
$$
where (u,v) parameterize the surface.
The local geometry is determined by the first fundamental form
$$
ds^2 =
E,du^2 + 2F,du,dv + G,dv^2.
$$
Here
$$
E = \mathbf{r}_u \cdot \mathbf{r}_u,
\quad
F = \mathbf{r}_u \cdot \mathbf{r}_v,
\quad
G = \mathbf{r}_v \cdot \mathbf{r}_v.
$$
These coefficients describe intrinsic distances on the surface.

## 13.2.3 Curvature tensor

Extrinsic curvature is described by the second fundamental form
$$
II =
L,du^2 + 2M,du,dv + N,dv^2.
$$
where
$$
L = \mathbf{r}{uu}\cdot \mathbf{n},
\quad
M = \mathbf{r}{uv}\cdot \mathbf{n},
\quad
N = \mathbf{r}_{vv}\cdot \mathbf{n}.
$$
Here ( $\mathbf{n}) is the surface normal.$
These coefficients encode how the surface bends in three-dimensional space.

## 13.2.4 Principal curvatures

From the curvature tensor we obtain the principal curvatures
$$
k_1, \quad k_2.
$$
These are the eigenvalues of the curvature matrix.
Two key scalar quantities arise:
Mean curvature
$$
H = \frac{1}{2}(k_1 + k_2)
$$
Gaussian curvature
$$
K = k_1 k_2.
$$
These quantities determine the geometric character of the shell.

## 13.2.5 Gaussian curvature as topological invariant

One of the most important results of differential geometry is the Gauss–Bonnet theorem:
$$
\int_S K,dA = 2\pi \chi.
$$
Here
$$
$\chi$ is the Euler characteristic of the surface.
$$
This theorem shows that total curvature is tied to topology.
Thus curvature contains global structural information.

## 13.2.6 Curvature memory

When a shell is deformed, curvature changes.
Let
$$
\delta H, \quad \delta K
$$
represent curvature perturbations.
Because curvature contributes to the shell's energy, deviations increase the total energy.
Thus curvature acts as a memory of the equilibrium geometry.

## 13.2.7 Curvature energy functional

The curvature energy of a shell is given by
$$
E_{curv}
\int
\left[
\frac{\kappa}{2}(2H)^2
+
\bar{\kappa}K
\right]
dA.
$$
This energy penalizes deviations from the preferred curvature configuration.

## 13.2.8 Restoring forces

A curvature perturbation generates restoring forces.
Taking the variation of the curvature energy yields
$$
\delta E_{curv}
\int
\left(
\kappa \Delta H

2\kappa H(H^2-K)
\right)\delta h, dA.
$$
Here ( $\delta h) is the normal displacement.$
These forces push the surface back toward its equilibrium shape.

## 13.2.9 Curvature stiffness

The coefficient
$$
\kappa
$$
is known as the bending rigidity.
Large values of ( $\kappa) make the shell difficult to bend.$
Thus curvature stiffness enhances persistence.

## 13.2.10 Curvature and locking

Curvature stabilization combines with multi-fan locking.
Let
$$
E_{lock}
E_{fan}
+
E_{curv}.
$$
Thus shell stability arises from two sources:
structural locking
curvature memory.
Together these mechanisms produce extremely large locking energy.

## 13.2.11 Curvature as structural memory

The key insight is that curvature encodes the geometry of the shell.
When the shell is perturbed, the curvature energy increases.
The system therefore evolves toward restoring the original curvature distribution.
Thus curvature functions as a geometric memory mechanism.

## 13.2.12 Implications for persistence

Because curvature memory resists deformation, shell structures exhibit extremely high persistence.
Small perturbations merely excite oscillation modes rather than destroying the structure.
Thus shells remain stable over long timescales.

## 13.2.13 Oscillation modes

Perturbations of shells produce surface vibration modes.
These modes satisfy
$$
\Delta^2 h = \lambda h
$$
where (h) is the displacement field.
These oscillations redistribute energy without destroying the shell.

## 13.2.14 Phase-chart interpretation

Curvature stabilization increases both
$$
x = \Lambda_{lock}
$$
and
$$
y = S_*.
$$
Thus shells move deeper into the persistent region of the CTS phase chart.

## 13.2.15 Summary

Curvature provides a geometric memory that preserves shell structure.
Deformations increase curvature energy, generating restoring forces that return the shell to its equilibrium shape.
This curvature memory, combined with multi-fan locking, explains why shell architectures are among the most stable persistence solutions in the Collapse Tension Substrate.

Minimal Shell Structures
This section derives the simplest possible shell configurations capable of satisfying the CTS persistence conditions.

