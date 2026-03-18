# 9.1 Formation Energy

## 9.1.1 Motivation

The CTS excitation ledger introduced in Chapter 8 requires several quantitative quantities for each excitation class. The first and most fundamental of these is the formation energy.
Formation energy measures the energetic cost required to create an excitation from the vacuum state of the Collapse Tension Substrate.
Formally, the formation energy determines how easily a structure can appear in the substrate.

## 9.1.2 Definition

Let the CTS vacuum configuration be

$$
\Phi = \Phi_0.
$$

Let an excitation be represented by a field configuration

$$
\Phi = \Phi_0 + \delta\Phi.
$$

The formation energy is defined as the difference between the energy of the excitation and the vacuum energy:

$$
\boxed{ E_{form} = E[\Phi] - E[\Phi_0] }
$$

where $E[\Phi]$ is the total energy of the field configuration $\Phi$.

## 9.1.3 CTS energy functional

Recall the CTS functional

$$
E[\Phi,\mathbf{A}] = \int d^3x \left[ a|(\nabla - iq\mathbf{A})\Phi|^2 + b|\nabla\times\mathbf{A}|^2 + u|\nabla^2\Phi|^2 + r|\Phi|^2 + s|\Phi|^4 \right].
$$

To compute formation energy we substitute the excitation configuration into this expression.

## 9.1.4 Energy density decomposition

The energy density can be written as

$$
\mathcal{E} = \mathcal{E}_{grad} + \mathcal{E}_{curv} + \mathcal{E}_{pot} + \mathcal{E}_{gauge}.
$$

## 9.1.5 Formation energy of wave excitations

For small-amplitude wave excitations

$$
\Phi = A e^{i(\mathbf{k}\cdot\mathbf{x}-\omega t)},
$$

the dominant contribution is gradient energy. Thus

$$
E_{form}^{wave} \sim (ak^2 + uk^4 + r) A^2 V.
$$

Here $V$ is the spatial volume of the wave.
Because $A$ can be arbitrarily small, wave formation energy can approach zero.
This explains why wave modes dominate the background excitation population.

## 9.1.6 Formation energy of vortex excitations

For vortex structures the dominant energy contribution arises from phase gradients.
Using the vortex ansatz

$$
\Phi(r,\theta) = f(r)e^{in\theta},
$$

the gradient energy density becomes

$$
\mathcal{E}_{grad} \approx a\left[ \left(\frac{df}{dr}\right)^2 + \frac{n^2}{r^2}f^2 \right].
$$

Integrating yields the approximate vortex formation energy

$$
E_{form}^{vortex} \approx \pi a n^2 \Phi_0^2 \ln\!\left(\frac{R}{\xi}\right).
$$

Thus vortex formation energy grows logarithmically with system size.

## 9.1.7 Formation energy of vortex rings

A vortex filament bent into a ring of radius $R$ has energy

$$
E_{form}^{ring} \approx \rho\Gamma^2 R \ln\!\left(\frac{8R}{\xi}\right).
$$

Here $\Gamma$ is the circulation and $\rho$ is the effective density.
The energy scales approximately linearly with ring radius.

## 9.1.8 Formation energy of shell structures

For shell excitations the dominant energy contribution comes from surface tension.
For a spherical shell of radius $R$

$$
E_{form}^{shell} = 4\pi\sigma R^2.
$$

Additional curvature energy contributes

$$
E_{curv} = 4\pi\kappa_c.
$$

This quadratic scaling explains why shell structures require significantly larger formation energy.

## 9.1.9 Formation energy scaling law

Different excitation classes therefore exhibit distinct scaling behavior.

| Excitation | Formation energy scaling |
|---|---|
| Wave | $E \sim A^2$ |
| Vortex | $E \sim \ln(R/\xi)$ |
| Vortex ring | $E \sim R\ln(R/\xi)$ |
| Shell | $E \sim R^2$ |
| Braid | $E \sim NR$ |

These scaling laws determine how difficult it is to form each structure.

## 9.1.10 Formation energy and abundance

From the abundance relation

$$
A_i \propto e^{-E_{form}/T_{eff}},
$$

structures with small formation energy appear frequently.
Thus the substrate naturally contains many low-energy excitations.
High-energy structures appear rarely.

## 9.1.11 Formation versus locking

Formation energy does not determine persistence by itself.
A structure may be cheap to form but easy to destroy.
This motivates the introduction of locking energy, which will be derived in the next section.
The interplay between formation and locking energy determines the position of each excitation in the survival map.

## 9.1.12 Ledger entry parameter

For each excitation type we record $E_{form}$ as the first quantity in the ledger entry

$$
\mathcal{L}_i = (\text{type},\, E_{form},\, E_{lock},\, E_{total},\, \dots).
$$

This parameter controls the excitation's abundance in the substrate.

## 9.1.13 Summary

Formation energy is the energetic cost required to create an excitation from the CTS vacuum.
It is computed directly from the CTS energy functional.
Different excitation classes exhibit characteristic formation-energy scaling laws, which determine how frequently they appear within the substrate.
