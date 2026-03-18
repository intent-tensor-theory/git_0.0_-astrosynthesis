# 2.4 Symmetry, Perturbation, and the First Asymmetry

## 2.4.1 Symmetric scalar state

The previous section showed that the CTS can exist in a homogeneous scalar regime where $\Phi(\mathbf{x}, t) = \Phi_0$ is spatially uniform.
In this state $\nabla \Phi = 0$ and no spatial directions are distinguished.
The substrate therefore possesses continuous spatial symmetry.
Mathematically this symmetry means that the system is invariant under translations:

$$
\Phi(\mathbf{x}) = \Phi(\mathbf{x} + \mathbf{a})
$$

for any displacement vector $\mathbf{a}$.
As long as this symmetry holds, no directional structure exists.

## 2.4.2 Perturbations of the symmetric state

Consider a small perturbation $\delta\Phi(\mathbf{x}, t)$ added to the homogeneous state.
The total field becomes

$$
\Phi(\mathbf{x},t) = \Phi_0 + \delta\Phi(\mathbf{x},t).
$$

To analyze the evolution of the perturbation we linearize the CTS equation around the equilibrium state.

## 2.4.3 Linearized CTS dynamics

The CTS field equation is

$$
\partial_t \Phi = -r\Phi + a\nabla^2\Phi - u\nabla^4\Phi - s\Phi^3.
$$

Substituting $\Phi = \Phi_0 + \delta\Phi$ and expanding to first order in $\delta\Phi$ gives

$$
\partial_t (\delta\Phi) = -(r + 3s\Phi_0^2)\,\delta\Phi + a\nabla^2(\delta\Phi) - u\nabla^4(\delta\Phi).
$$

## 2.4.4 Fourier mode analysis

To analyze stability we decompose the perturbation into Fourier modes:

$$
\delta\Phi(\mathbf{x},t) = \int \tilde{\Phi}(\mathbf{k},t)\, e^{i\mathbf{k}\cdot\mathbf{x}} \, d^3k.
$$

Substituting into the linearized equation yields

$$
\frac{d\tilde{\Phi}}{dt} = \omega(k)\, \tilde{\Phi}.
$$

The growth rate is

$$
\omega(k) = -(r + 3s\Phi_0^2) - ak^2 - uk^4.
$$

## 2.4.5 Instability condition

For perturbations to grow we require $\omega(k) > 0$.
Thus instability occurs when

$$
-(r + 3s\Phi_0^2) - ak^2 - uk^4 > 0.
$$

If this condition is satisfied for some value of $k$, then the symmetric state becomes unstable.
A particular spatial wavelength becomes amplified.

## 2.4.6 First asymmetry

When a particular Fourier mode grows faster than others, the substrate develops spatial variation.
The gradient becomes

$$
\nabla\Phi \neq 0.
$$

This represents the first asymmetry in the substrate.
Spatial locations become distinguishable because the scalar field now varies across space.
Thus directional structure begins to emerge.

## 2.4.7 Characteristic wavelength

The fastest-growing mode corresponds to the value of $k$ that maximizes the growth rate.
Setting $d\omega/dk = 0$ yields

$$
-2ak - 4uk^3 = 0.
$$

Thus

$$
k(2a + 4uk^2) = 0.
$$

The nontrivial solution gives

$$
k^2 = -\frac{a}{2u}.
$$

Thus the characteristic wavelength is

$$
\lambda_c = \frac{2\pi}{k_c} = 2\pi\sqrt{-\frac{2u}{a}}.
$$

This wavelength determines the scale of the first spatial structures.

## 2.4.8 Gradient formation

Once perturbations grow, the field develops gradients $\nabla\Phi(\mathbf{x}) \neq 0$.
Gradients represent directional bias in the substrate.
Energy stored in gradients is

$$
E_{grad} = \int |\nabla\Phi|^2 \, d^3x.
$$

This energy contributes to structural retention.

## 2.4.9 Structural retention from gradients

The retained structure now becomes

$$
R = \alpha_0 \int \Phi^2 \, d^3x + \alpha_1 \int |\nabla\Phi|^2 \, d^3x.
$$

Thus gradients add a new retention channel.
Configurations with stronger gradients can resist collapse more effectively.

## 2.4.10 Selection number with gradients

Using the persistence condition $S = R / (\dot{R} \, t_{ref})$, we now have

$$
R = \alpha_0 \|\Phi\|^2 + \alpha_1 \|\nabla\Phi\|^2.
$$

If gradient retention grows large enough relative to loss mechanisms, the configuration may satisfy $S \geq 1$.
This marks the first stage at which spatial structures can persist.

## 2.4.11 Interpretation

The emergence of gradients breaks the symmetry of the homogeneous scalar state.
Before perturbation growth: $\nabla\Phi = 0$.
After instability: $\nabla\Phi \neq 0$.
Thus the system develops directional structure.
This is the earliest stage at which spatial organization begins to appear within the CTS.

## 2.4.12 Summary

The symmetric scalar regime becomes unstable when perturbations with certain wavelengths grow.
This instability produces spatial gradients and breaks translational symmetry.
Gradients introduce the first directional structure in the substrate and contribute to structural retention.
These processes mark the transition from purely scalar dynamics to spatially structured dynamics.

---

*Transition to Section 2.5:*
This section will derive how the CTS field stores and distributes retained structure across its configurations.
