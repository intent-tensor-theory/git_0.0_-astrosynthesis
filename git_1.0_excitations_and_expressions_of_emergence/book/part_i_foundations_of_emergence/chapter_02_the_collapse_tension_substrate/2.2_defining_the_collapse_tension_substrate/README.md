# 2.2 Defining the Collapse Tension Substrate

## 2.2.1 Motivation for a formal definition

The previous section introduced the conceptual idea of a Collapse Tension Substrate (CTS): a dynamical medium in which two opposing tendencies operate simultaneously:
collapse, which degrades organized structure
tension, which resists collapse and stabilizes configurations
To develop this idea into a quantitative framework, we must define the substrate mathematically.
The CTS will therefore be represented by a field whose dynamics encode both collapse and stabilization mechanisms.

## 2.2.2 Substrate field

Let the substrate be described by a scalar field
$$
\Phi(\mathbf{x},t).
$$
This field represents the local structural potential of the substrate.
The field is defined over a continuous domain, which for now may be treated as a three-dimensional coordinate space
$$
\mathbf{x} \in \mathbb{R}^3.
$$
Thus
$$
\Phi : \mathbb{R}^3 \times \mathbb{R} \rightarrow \mathbb{R}.
$$
Configurations of the substrate correspond to specific functions
$$
\Phi(\mathbf{x},t).
$$

## 2.2.3 Energy functional of the substrate

To determine the dynamics of the field we introduce an energy functional
$$
E[\Phi].
$$
The simplest functional capable of producing structural competition is
$$
E[\Phi] =
\int
\left(
a |\nabla \Phi|^2
+
u (\nabla^2 \Phi)^2
+
r \Phi^2
+
s \Phi^4
\right)
d^3x.
$$
Each term has a specific role.

## 2.2.4 Interpretation of the terms

Gradient term
$$
a |\nabla \Phi|^2
$$
This term penalizes rapid spatial variation.
It represents a smoothing tendency similar to diffusion.

Curvature term
$$
u (\nabla^2 \Phi)^2
$$
This higher-order term stabilizes localized structures.
It prevents indefinite collapse or runaway gradients.

Quadratic potential
$$
r \Phi^2
$$
This term determines whether the uniform state
$$
\Phi = 0
$$
is stable or unstable.

Nonlinear saturation
$$
s \Phi^4
$$
This term prevents unlimited growth of the field.
It stabilizes finite-amplitude configurations.

## 2.2.5 Dynamical equation

The time evolution of the substrate field follows a relaxation equation derived from the energy functional.
A common form is
$$
\partial_t \Phi = -\frac{\delta E}{\delta \Phi}.
$$
Computing the functional derivative gives
$$
\partial_t \Phi
r\Phi

a \nabla^2 \Phi
u \nabla^4 \Phi
s \Phi^3.
$$
This equation defines the CTS field dynamics.

## 2.2.6 Collapse term

The linear term
$$
-r\Phi
$$
represents structural collapse.
If
$$
r > 0
$$
then fluctuations tend to decay.
This term drives the system toward
$$
\Phi = 0.
$$

## 2.2.7 Tension terms

The remaining terms contribute to structural stabilization.
diffusion-like tension
$$
a \nabla^2 \Phi
$$
allows spatial redistribution of structure.
curvature tension
$$
-u \nabla^4 \Phi
$$
stabilizes localized patterns.
nonlinear tension
$$
-s \Phi^3
$$
prevents runaway growth.
Together these terms oppose collapse.

## 2.2.8 Equilibrium states

Stationary configurations satisfy
$$
\partial_t \Phi = 0.
$$
Thus
$$
-r\Phi
+
a \nabla^2 \Phi
u \nabla^4 \Phi
s \Phi^3
= 0.
$$
Solutions of this equation represent possible substrate structures.
Examples include:
uniform states
periodic patterns
localized solitons.

## 2.2.9 Linear stability analysis

Consider small perturbations
$$
\Phi = \epsilon e^{i(\mathbf{k}\cdot\mathbf{x}-\omega t)}.
$$
Substituting into the linearized equation yields the dispersion relation
$$
\omega =
r
+
a k^2
+
u k^4.
$$
The sign of
$$
\omega
$$
determines stability.
If
$$
\omega > 0
$$
the mode grows.
If
$$
\omega < 0
$$
the mode decays.

## 2.2.10 Mode selection

The growth rate of a mode depends on its wavenumber
$$
k = |\mathbf{k}|.
$$
The dominant mode corresponds to the value of
$$
k
$$
that maximizes
$$
\omega(k).
$$
Thus the substrate naturally selects preferred spatial scales.
These scales determine the characteristic size of emergent structures.

## 2.2.11 Structural retention in the CTS

The retained structure of a configuration can be expressed in terms of the energy functional.
Let
$$
R = E[\Phi].
$$
Energy stored in the field represents organized structural content.
Loss processes correspond to the dissipation of this energy.
Thus
$$
\dot R = -\frac{dE}{dt}.
$$

## 2.2.12 Persistence condition

Substituting this definition into the selection number gives
$$
S =
\frac{E[\Phi]}{\left|\frac{dE}{dt}\right| t_{ref}}.
$$
Configurations satisfying
$$
S \ge 1
$$
persist long enough to participate in higher-order structural processes.

## 2.2.13 Summary

The Collapse Tension Substrate is defined by a scalar field
$$
\Phi(\mathbf{x},t)
$$
whose dynamics follow
$$
\partial_t \Phi
r\Phi

a\nabla^2\Phi
u\nabla^4\Phi
s\Phi^3.
$$
Within this equation:
the linear term represents collapse
the gradient and curvature terms represent tension
the nonlinear term stabilizes finite amplitudes.
This competition generates the structural landscape from which persistent configurations emerge.

Scalar Potential Before Geometry
This section derives the zero-dimensional scalar regime of the substrate and shows how fluctuations behave before gradients and spatial structures emerge.

No additional sections beyond the Table of Contents.
