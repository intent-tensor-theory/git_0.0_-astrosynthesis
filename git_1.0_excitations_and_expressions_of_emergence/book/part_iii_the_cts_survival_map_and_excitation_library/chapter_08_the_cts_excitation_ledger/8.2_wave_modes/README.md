# 8.2 Wave Modes

## 8.2.1 The simplest excitation class

The simplest excitations supported by the Collapse Tension Substrate are wave modes.
These excitations correspond to small-amplitude oscillations of the scalar field around the vacuum state

$$
\Phi(\mathbf{x},t) = \Phi_0 + \delta\Phi(\mathbf{x},t).
$$

Wave modes represent linear excitations of the substrate and therefore appear as the lowest-energy entries in the excitation ledger.
Because their formation energy is minimal, wave modes dominate the background structure of the substrate.

## 8.2.2 Linearized field equation

Starting from the CTS scalar evolution equation derived earlier

$$
\partial_t \Phi = -r\Phi + a\nabla^2\Phi - u\nabla^4\Phi - s\Phi^3,
$$

we expand around the vacuum value

$$
\Phi = \Phi_0 + \delta\Phi.
$$

Keeping only linear terms in the fluctuation yields

$$
\partial_t \delta\Phi = -r\,\delta\Phi + a\nabla^2\delta\Phi - u\nabla^4\delta\Phi.
$$

This equation governs small-amplitude wave excitations.

## 8.2.3 Plane-wave solutions

Assume a plane-wave ansatz

$$
\delta\Phi(\mathbf{x},t) = A e^{i(\mathbf{k}\cdot\mathbf{x}-\omega t)}.
$$

Substituting into the linearized equation yields

$$
-i\omega = -r - ak^2 - uk^4.
$$

Thus the dispersion relation becomes

$$
\boxed{\omega(k) = r + ak^2 + uk^4}
$$

which determines how frequency depends on wavelength.

## 8.2.4 Long-wavelength limit

For long wavelengths the quartic term becomes negligible.
The dispersion simplifies to

$$
\omega(k) \approx r + ak^2.
$$

Thus long-wavelength excitations behave like diffusive or wave-like modes depending on the sign of $r$.

## 8.2.5 Short-wavelength limit

For very large $k$,

$$
k \gg \sqrt{\frac{a}{u}},
$$

the curvature term dominates. Thus

$$
\omega(k) \approx uk^4.
$$

This quartic dispersion suppresses extremely small-scale fluctuations.
Thus the curvature term acts as an ultraviolet stabilizer for the substrate.

## 8.2.6 Group velocity

The propagation speed of wave packets is determined by the group velocity

$$
v_g = \frac{d\omega}{dk}.
$$

Using the dispersion relation gives

$$
v_g = 2ak + 4uk^3.
$$

Thus wave propagation speed increases with wavenumber.
This property reflects the increasing influence of gradient and curvature energies at smaller spatial scales.

## 8.2.7 Energy of a wave mode

The energy stored in a wave excitation can be computed from the quadratic energy density.
For a mode of amplitude $A$,

$$
E_{wave} \sim (ak^2 + uk^4 + r)\,A^2\,V
$$

where $V$ is the spatial volume occupied by the wave.
Because the amplitude can be arbitrarily small, wave excitations can possess extremely low formation energy.

## 8.2.8 Wave persistence

Despite their low energy, wave modes generally fail to become persistent objects.
This occurs because they lack several persistence mechanisms:

| Mechanism | Presence in waves |
|---|---|
| shell locking | absent |
| topological protection | absent |
| chirality | absent |

Thus wave excitations typically have

$$
T_{obj} \approx 1.
$$

Without topological protection, wave modes dissipate easily.

## 8.2.9 Wave contribution to the substrate background

Because wave excitations require minimal energy to form, they occur frequently.
From the abundance relation

$$
A_i \propto e^{-E_i/T_{eff}},
$$

low-energy modes dominate the excitation population.
Thus the CTS substrate is expected to contain a dense background of propagating wave modes.

## 8.2.10 Role in structural emergence

Although wave modes rarely become persistent objects, they play an important role in emergence.
They serve as the transport mechanism for energy and information across the substrate.
Wave interactions can generate higher-order excitations such as:

- vortices
- solitons
- domain walls.

Thus wave modes provide the dynamical background from which more complex structures arise.

## 8.2.11 Wave modes in the excitation ledger

The ledger entry for wave modes can be summarized as:

| Parameter | Approximate value |
|---|---|
| excitation type | wave mode |
| formation energy | very low |
| locking energy | none |
| topology factor | $T_{obj} \approx 1$ |
| persistence | low |

Thus waves occupy the lowest-energy tier of the CTS excitation hierarchy.

## 8.2.12 Interpretation within the CTS framework

Within the Collapse Tension Substrate interpretation, wave modes represent the simplest expression of structural tension in the substrate.
They correspond to propagating disturbances of the field rather than discrete objects.
Thus waves form the background propagation layer of the CTS survival map.

## 8.2.13 Summary

Wave modes are the simplest excitations of the Collapse Tension Substrate.
They arise as linear oscillations of the scalar field around the vacuum state.
Their dispersion relation is

$$
\omega(k) = r + ak^2 + uk^4.
$$

Because their formation energy is minimal but their topological protection is absent, wave modes dominate the background but rarely become persistent structures.
