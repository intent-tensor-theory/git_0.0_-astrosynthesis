# 8.4 Open Vortices

## 8.4.1 Emergence of rotational excitations

Wave modes and phase-locked packets described in previous sections involve oscillatory or translational field motion. However, the CTS functional also permits rotational excitations of the field.
These excitations arise when the phase of the scalar field winds around a central axis.
Such configurations create vortex structures.
Open vortices represent the first excitations in the CTS ledger that possess topological invariants.

## 8.4.2 Phase representation of the field

Write the scalar field in amplitude–phase form

$$
\Phi(\mathbf{x}) = \rho(\mathbf{x})\,e^{i\theta(\mathbf{x})},
$$

where $\rho$ is the amplitude and $\theta$ is the phase.

Substituting this into the gradient term of the functional yields

$$
|\nabla\Phi|^2 = (\nabla\rho)^2 + \rho^2(\nabla\theta)^2.
$$

The second term depends on spatial variation of the phase.

## 8.4.3 Circulation of the phase

Consider a closed loop $C$ around a point in space.
The phase circulation is defined as

$$
\oint_C \nabla\theta \cdot d\mathbf{l}.
$$

Because the field must be single-valued, the phase can change only by integer multiples of $2\pi$:

$$
\oint_C \nabla\theta \cdot d\mathbf{l} = 2\pi n, \quad n \in \mathbb{Z}.
$$

This integer $n$ is the winding number.

## 8.4.4 Vortex core

At the center of the vortex the phase becomes undefined.
To avoid infinite energy the amplitude must vanish:

$$
\rho(0) = 0.
$$

Thus the field configuration near the vortex center takes the form

$$
\Phi(r,\theta) = f(r)\,e^{in\theta}.
$$

The function $f(r)$ satisfies

$$
f(0) = 0, \quad f(\infty) = \Phi_0.
$$

## 8.4.5 Radial vortex profile

The vortex profile is determined by minimizing the energy functional.
Substituting the vortex ansatz into the scalar energy gives

$$
E = \int \left[ a\left(\left(\frac{df}{dr}\right)^2 + \frac{n^2}{r^2}f^2 \right) + r f^2 + s f^4 \right] r\,dr\,d\theta.
$$

The equilibrium profile satisfies the Euler–Lagrange equation

$$
\frac{d^2 f}{dr^2} + \frac{1}{r}\frac{df}{dr} - \frac{n^2}{r^2}f - \frac{r}{a}f - \frac{2s}{a}f^3 = 0.
$$

## 8.4.6 Vortex core radius

The vortex core size is determined by the correlation length derived earlier:

$$
\xi = \sqrt{\frac{a}{|r|}}.
$$

Inside the core ($r \lesssim \xi$) the amplitude is suppressed.
Outside the core the field approaches the vacuum state.

## 8.4.7 Energy of a vortex line

The energy per unit length of the vortex can be approximated as

$$
E_{vortex} \approx \pi a n^2 \Phi_0^2 \ln\left(\frac{R}{\xi}\right).
$$

Here $R$ is the system size and $\xi$ is the core radius.
Because of the logarithmic factor, vortex energy grows slowly with system size.

## 8.4.8 Topological protection

The winding number $n$ is a topological invariant.
Continuous deformation cannot change this number.
Thus the vortex cannot disappear unless the field amplitude vanishes along an entire path.
This topological constraint provides structural protection.

## 8.4.9 Topology factor

Because vortices possess a conserved winding number, their topology factor becomes

$$
T_{obj} > 1.
$$

This distinguishes vortices from wave excitations.
Although vortices may still decay through reconnection events, their lifetime is typically much longer than ordinary waves.

## 8.4.10 Circulation interpretation

The phase circulation corresponds to a rotational current.
Define the current

$$
\mathbf{J} = \rho^2 \nabla\theta.
$$

The circulation becomes

$$
\oint_C \mathbf{J} \cdot d\mathbf{l} = 2\pi n \rho^2.
$$

Thus vortices represent quantized circulation channels in the CTS substrate.

## 8.4.11 Open vortex geometry

Open vortices extend through space as line-like structures. Examples include

- vortex filaments
- rotational defects
- circulation tubes.

Because their ends terminate at boundaries or other defects, these structures are classified as open topological defects.

## 8.4.12 Role in the CTS excitation hierarchy

Open vortices represent the first excitation class that possesses nontrivial topology.
They therefore occupy a higher tier in the excitation hierarchy.
The hierarchy now becomes:

| Excitation | Topology |
|---|---|
| waves | none |
| phase-locked waves | weak coherence |
| open vortices | winding number |

Thus open vortices represent the transition from coherent waves to topological objects.

## 8.4.13 Ledger entry for open vortices

| Parameter | Approximate value |
|---|---|
| excitation type | open vortex |
| formation energy | moderate |
| locking energy | moderate |
| topology factor | $T_{obj} > 1$ |
| persistence | moderate–high |

These structures therefore populate the closure survival boundary of the CTS survival map.

## 8.4.14 Summary

Open vortices arise when the phase of the CTS scalar field winds around a central axis.
Their defining property is the quantized circulation

$$
\oint \nabla\theta\cdot d\mathbf{l} = 2\pi n.
$$

Because the winding number is conserved, vortices possess topological protection.
They therefore represent the first excitation class capable of forming long-lived structural objects within the CTS substrate.
