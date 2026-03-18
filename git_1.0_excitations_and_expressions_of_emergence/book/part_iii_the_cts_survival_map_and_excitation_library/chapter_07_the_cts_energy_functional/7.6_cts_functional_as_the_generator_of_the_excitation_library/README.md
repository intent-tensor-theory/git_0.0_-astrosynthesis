# 7.6 CTS Functional as the Generator of the Excitation Library

## 7.6.1 From functional to excitation spectrum

The CTS energy functional determines which structural configurations can exist in the substrate. These configurations correspond to solutions of the Euler–Lagrange equations derived from the functional.
Recall the CTS functional

$$
E[\Phi,\mathbf{A}] = \int d^3x \left[ a\left|(\nabla - iq\mathbf{A})\Phi\right|^2 + b|\nabla\times\mathbf{A}|^2 + u\left(\nabla^2\Phi\right)^2 + r|\Phi|^2 + s|\Phi|^4 \right].
$$

Extremizing the functional yields the field equations

$$
\frac{\delta E}{\delta \Phi} = 0, \qquad \frac{\delta E}{\delta \mathbf{A}} = 0.
$$

Solutions to these equations define the excitation library of the Collapse Tension Substrate.

## 7.6.2 Classes of CTS excitations

The functional admits several classes of solutions depending on boundary conditions and topology.
The main families include:

| Excitation | Description |
|---|---|
| wave modes | linear oscillatory solutions |
| domain walls | boundaries between vacuum states |
| vortices | rotational defects |
| vortex rings | closed vortex loops |
| shells | closed coherent surfaces |
| braids | intertwined vortex structures |

Each family corresponds to a different topological or geometric configuration of the field.

## 7.6.3 Linear wave solutions

In the symmetric vacuum ($\Phi = 0$), the linearized evolution equation is

$$
\partial_t \Phi = 2a\nabla^2\Phi - 2u\nabla^4\Phi - 2r\Phi.
$$

Assuming plane-wave solutions $\Phi \sim e^{i(\mathbf{k}\cdot\mathbf{x}-\omega t)}$, the dispersion relation is

$$
\omega(k) = 2ak^2 - 2uk^4 - 2r.
$$

These solutions correspond to propagating substrate waves.

## 7.6.4 Domain wall solutions

When $r < 0$, the substrate develops two vacuum states $\Phi = \pm\Phi_0$.
A domain wall solution connects these states.
In one dimension, the wall profile interpolates smoothly between $-\Phi_0$ and $+\Phi_0$ over a thickness $\ell \sim \sqrt{a/|r|}$.
Domain walls represent localized planar excitations separating structural phases.

## 7.6.5 Vortex solutions

When the scalar field couples to the vector potential $\mathbf{A}$, vortex solutions appear.
A vortex configuration takes the form

$$
\Phi(r,\theta) = f(r)\,e^{in\theta},
$$

where $n$ is the winding number and $f(r)$ vanishes at the vortex core.
The circulation around the vortex is quantized:

$$
\oint \nabla \theta \cdot d\mathbf{l} = 2\pi n.
$$

This quantization produces topological protection.

## 7.6.6 Vortex ring solutions

A vortex line can close into a loop, producing a vortex ring.
Let the ring have radius $R$.
The energy of the ring scales approximately as

$$
E_{ring} \sim \rho\Gamma^2 R \ln\!\left(\frac{R}{a_c}\right),
$$

where $\Gamma$ is the circulation and $a_c$ is the core size.
Vortex rings are among the simplest localized closed excitations.

## 7.6.7 Shell solutions

Shell structures arise when multiple circulation channels stabilize a closed boundary.
The shell energy contains contributions from:

- surface tension
- curvature energy
- internal field energy.

A simplified shell energy expression is

$$
E_{shell} = \sigma A + \kappa_c \int H^2 \, dA + E_{int},
$$

where $A$ is shell area and $H$ is mean curvature.
Shells form stable structures when curvature energy and surface tension balance internal pressure.

## 7.6.8 Braid solutions

When multiple vortex filaments intertwine, braid structures emerge.
A braid with $N$ strands is described by the braid group $B_N$.
The braid energy includes

$$
E_{braid} = E_{vortex} + E_{twist} + E_{interaction}.
$$

Braids are topologically protected because the linking number $Lk$ cannot change without reconnection.

## 7.6.9 Excitation energy hierarchy

Each excitation class has a characteristic formation energy.
Approximate ordering from lowest to highest:

| Excitation | Formation energy |
|---|---|
| domain walls | lowest |
| vortex lines | intermediate |
| vortex rings | higher |
| shells and braids | highest |

Thus low-energy excitations dominate the substrate background.
Higher-energy excitations occur less frequently.

## 7.6.10 Excitation ledger

Each excitation can be characterized by a set of parameters:

$$
(E_{form},\; E_{lock},\; E_{total}),
$$

where $E_{lock}$ is energy associated with structural locking and $E_{total}$ is total excitation energy.
These quantities form the basis of the CTS excitation ledger introduced later in the book.

## 7.6.11 Abundance law

The abundance of excitations follows a Boltzmann-like relation

$$
A_i \propto e^{-E_i/T_{eff}}.
$$

- Low-energy excitations appear frequently.
- High-energy structures are rare.

This explains why wave-like structures dominate the substrate while complex composite objects appear less often.

## 7.6.12 Formation versus survival

It is important to distinguish two separate processes:

- **Formation**: Determined by the energy functional and excitation spectrum.
- **Survival**: Determined by the persistence equation

$$
S_* = \mathcal{E}_{shell}\,\mathcal{E}\,D\,T_{obj}\,\frac{R}{\dot{R}\,t_{ref}}.
$$

Only excitations satisfying both conditions appear as persistent structures.

## 7.6.13 Excitation library

The complete CTS excitation library therefore consists of all solutions of the energy functional.
These solutions populate the structural phase space of the substrate.
Later chapters classify these excitations according to persistence thresholds and survival regions.

## 7.6.14 Interpretation

Within the CTS framework the universe of structures is interpreted as a library of persistent excitations of the substrate.
Each structure corresponds to a particular field configuration stabilized by topology, geometry, and persistence mechanics.
Thus objects are not fundamental entities but stable excitation modes.

## 7.6.15 Summary

The CTS energy functional generates the full spectrum of structural excitations in the substrate.
These include waves, domain walls, vortices, rings, shells, and braids.
Each excitation has a characteristic energy and topology.
Persistence mechanics then determines which of these excitations survive long enough to become observable structures.

## Transition to Chapter 8

Having derived the excitation spectrum from the energy functional, we now turn to a systematic classification of these structures in terms of what counts as an excitation.
