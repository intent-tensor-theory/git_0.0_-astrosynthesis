# 3.2 1D: Gradient Bias

## 3.2.1 Transition from scalar to spatial variation

In the 0D regime the substrate was described by a homogeneous scalar field
$$
\Phi(t)
$$
with no spatial variation.
However, small perturbations can introduce spatial differences in the field. When this occurs, the substrate develops gradients
$$
\nabla \Phi(\mathbf{x},t) \neq 0.
$$
These gradients represent the first directional structure within the CTS.
The presence of gradients means the field now contains information about relative differences between neighboring regions.

## 3.2.2 Gradient definition

The gradient of the scalar field is defined as
$$
\nabla \Phi =
\left(
\frac{\partial \Phi}{\partial x},
\frac{\partial \Phi}{\partial y},
\frac{\partial \Phi}{\partial z}
\right).
$$
The magnitude of the gradient is
$$
|\nabla \Phi| =
\sqrt{
\left(\frac{\partial \Phi}{\partial x}\right)^2
+
\left(\frac{\partial \Phi}{\partial y}\right)^2
+
\left(\frac{\partial \Phi}{\partial z}\right)^2
}.
$$
This quantity measures how rapidly the field varies across space.

## 3.2.3 Energy stored in gradients

Gradients store structural energy in the field.
From the CTS energy functional,
$$
E[\Phi] =
\int
\left(
a |\nabla \Phi|^2
+
u (\nabla^2\Phi)^2
+
r \Phi^2
+
s \Phi^4
\right)
d^3x,
$$
the gradient contribution is
$$
E_{grad} = a \int |\nabla \Phi|^2 d^3x.
$$
This energy represents the structural tension associated with spatial variation.

## 3.2.4 Gradient-driven dynamics

The CTS equation contains a diffusion-like term
$$
a\nabla^2\Phi.
$$
The Laplacian operator
$$
\nabla^2 \Phi =
\frac{\partial^2 \Phi}{\partial x^2}
+
\frac{\partial^2 \Phi}{\partial y^2}
+
\frac{\partial^2 \Phi}{\partial z^2}
$$
describes how gradients evolve.
Substituting into the field equation,
$$
\partial_t \Phi = -r\Phi + a\nabla^2\Phi - u\nabla^4\Phi - s\Phi^3,
$$
we see that spatial variation influences the evolution of the field.

## 3.2.5 Linear perturbation analysis

Consider a small spatial perturbation
$$
\delta\Phi(\mathbf{x},t).
$$
Express this perturbation as a Fourier mode
$$
\delta\Phi = A e^{i(\mathbf{k}\cdot\mathbf{x}-\omega t)}.
$$
Substituting into the linearized CTS equation gives the dispersion relation
$$
\omega(k) = r + a k^2 + u k^4.
$$
Here
$$
k = |\mathbf{k}|
$$
is the spatial frequency of the perturbation.

## 3.2.6 Growth of directional structure

If
$$
\omega(k) > 0
$$
the perturbation grows.
This growth produces spatial variation in the field.
Thus gradients become amplified.
The direction of the gradient defines the first spatial axis of organization in the substrate.
This marks the transition from scalar variation to directional structure.

## 3.2.7 One-dimensional bias

When a dominant gradient forms along a particular direction
$$
\hat{n},
$$
the field becomes approximately
$$
\Phi(\mathbf{x}) \approx \Phi(n)
$$
where
$$
n = \mathbf{x}\cdot\hat{n}.
$$
Thus variation occurs primarily along one axis.
This regime is effectively one-dimensional.

## 3.2.8 Structural retention in the gradient regime

Retained structure now includes both amplitude and gradient contributions.
Define
$$
R =
\alpha_0 \int \Phi^2 d^3x
+
\alpha_1 \int |\nabla\Phi|^2 d^3x.
$$
The gradient term provides an additional channel for storing structural energy.
This increases the potential persistence of the configuration.

## 3.2.9 Loss processes in gradient structures

Gradient structures remain subject to dissipative smoothing.
The dominant loss process is diffusion.
For a characteristic length scale
$$
L,
$$
the decay rate is approximately
$$
\Gamma \sim \frac{D}{L^2}.
$$
Thus smaller gradient structures decay more rapidly.
Larger structures have longer lifetimes.

## 3.2.10 Selection number with gradients

Using the persistence condition
$$
S = \frac{R}{\dot{R}\,t_{ref}},
$$
and the gradient-based retention measure,
$$
R =
\alpha_0 \|\Phi\|^2
+
\alpha_1 \|\nabla\Phi\|^2,
$$
we see that gradient energy increases the numerator of the selection number.
Thus sufficiently strong gradients may allow
$$
S \geq 1.
$$
In this case the directional structure persists.

## 3.2.11 Physical interpretation

The gradient regime introduces the first form of spatial organization in the CTS.
Key features include:

- directional bias
- spatial differentiation
- storage of structural energy in gradients

These properties allow the substrate to support more complex dynamical behavior.

## 3.2.12 Transition to circulation

Gradients alone do not produce closed structures.
However interacting gradients can generate rotational flows.
Mathematically this occurs when the curl of a vector field becomes nonzero.
Thus the next stage of emergence involves circulation:
$$
\nabla \times \mathbf{v} \neq 0.
$$
This marks the transition from the 1D gradient regime to the 2D circulation regime.

## 3.2.13 Summary

The second stage of dimensional emergence occurs when scalar fluctuations develop spatial gradients.
These gradients introduce directional structure and store energy through
$$
E_{grad} = a\int |\nabla\Phi|^2 d^3x.
$$
If gradient energy is sufficiently large relative to loss processes, the configuration satisfies the persistence condition and becomes a stable directional structure.

*Transition to Section 3.3:* The next section derives how interacting gradients produce rotational structures and persistent circulation in the CTS.
