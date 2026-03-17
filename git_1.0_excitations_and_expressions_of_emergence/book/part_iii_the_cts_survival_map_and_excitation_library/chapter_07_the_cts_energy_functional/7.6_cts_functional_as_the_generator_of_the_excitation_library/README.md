# 7.6 CTS Functional as the Generator of the Excitation Library

## 7.6.1 From functional to excitation spectrum

The CTS energy functional determines which structural configurations can exist in the substrate. These configurations correspond to solutions of the Euler–Lagrange equations derived from the functional.
Recall the CTS functional
$$
E[,A]=d3x[a(iqA)2+bA2+u(2)2+r2+s4].E[\Phi,\mathbf A] = \int d^3x \left[ a|$\nabla - iq\mathbf A$\Phi|^2 + b|\nabla\times\mathbf A|^2 + u$\nabla^2\Phi$^2 + r|\Phi|^2 + s|\Phi|^4 \right].E[
$$
Extremizing the functional yields the field equations
δEδΦ=0,δEδA=0.\frac{\delta E}{\delta \Phi}=0, \qquad \frac{\delta E}{\delta \mathbf A}=0.δΦδE​=0,δAδE​=0.
Solutions to these equations define the excitation library of the Collapse Tension Substrate.

## 7.6.2 Classes of CTS excitations

The functional admits several classes of solutions depending on boundary conditions and topology.
The main families include:
excitation
description
wave modes
linear oscillatory solutions
domain walls
boundaries between vacuum states
vortices
rotational defects
closed vortex loops
shell structures
closed coherent surfaces
intertwined vortex structures

Each family corresponds to a different topological or geometric configuration of the field.

## 7.6.3 Linear wave solutions

In the symmetric vacuum (Φ=0 $\Phi=0$
∂tΦ=2a∇2Φ−2u∇4Φ−2rΦ.\partial_t \Phi = 2a\nabla^2\Phi - 2u\nabla^4\Phi - 2r\Phi.∂t​Φ=2a∇2Φ−2u∇4Φ−2rΦ.
Assuming plane-wave solutions
$$
ei(kxt),\Phi \sim e^{i$\mathbf{k}\cdot x-\omega t$},
$$
the dispersion relation is
$$
(k)=2ak22uk42r.\omega(k) = 2ak^2 - 2uk^4 - 2r.
$$
These solutions correspond to propagating substrate waves.

## 7.6.4 Domain wall solutions

When r<0r<0r<0, the substrate develops two vacuum states
Φ=±Φ0.\Phi=\pm\Phi_0.Φ=±Φ0​.
A domain wall solution connects these states.
In one dimension
Domain walls represent localized planar excitations separating structural phases.

## 7.6.5 Vortex solutions

When the scalar field couples to the vector potential A $\mathbf AA, vortex solutions appear.$
A vortex configuration takes the form
$$
(r,)=f(r)ein.\Phi(r,\theta) = f(r)e^{in\theta}.
$$
nnn is the winding number

f(r)f(r)f(r) vanishes at the vortex core.

The circulation around the vortex is quantized:
$$
dl=2n.\oint \nabla \theta \cdot dl = 2\pi n.
$$
This quantization produces topological protection.

## 7.6.6 Vortex ring solutions

A vortex line can close into a loop, producing a vortex ring.
Let the ring have radius RRR.
The energy of the ring scales approximately as
Ering∼ρΓ2Rln⁡ ⁣(Rac)E_{ring} \sim \rho\Gamma^2 R \ln\!\left$\frac{R}{a_c}\right$Ering​∼ρΓ2Rln(ac​R​)
$$
\Gamma
$$

aca_cac​ is core size.

Vortex rings are among the simplest localized closed excitations.

## 7.6.7 Shell solutions

Shell structures arise when multiple circulation channels stabilize a closed boundary.
The shell energy contains contributions from:
surface tension

curvature energy

internal field energy.

A simplified shell energy expression is
Eshell=σA+κc∫H2dA+Eint.E_{shell} = \sigma A + \kappa_c \int H^2 dA + E_{int}.Eshell​=σA+κc​∫H2dA+Eint​.
AAA is shell area

HHH is mean curvature.

Shells form stable structures when curvature energy and surface tension balance internal pressure.

## 7.6.8 Braid solutions

When multiple vortex filaments intertwine, braid structures emerge.
A braid with NNN strands is described by the braid group BNB_NBN​.
The braid energy includes
Ebraid=Evortex+Etwist+Einteraction.E_{braid} = E_{vortex} + E_{twist} + E_{interaction}.Ebraid​=Evortex​+Etwist​+Einteraction​.
Braids are topologically protected because the linking number
LkLkLk
cannot change without reconnection.

## 7.6.9 Excitation energy hierarchy

Each excitation class has a characteristic formation energy.
Approximate ordering:
excitation
formation energy
domain walls
vortex lines
vortex rings

Thus low-energy excitations dominate the substrate background.
Higher-energy excitations occur less frequently.

## 7.6.10 Excitation ledger

Each excitation can be characterized by a set of parameters:
(Eform,  Elock,  Etotal).(E_{form},\;E_{lock},\;E_{total}).(Eform​,Elock​,Etotal​).

ElockE_{lock}Elock​ is energy associated with structural locking

EtotalE_{total}Etotal​ is total excitation energy.

These quantities form the basis of the CTS excitation ledger introduced later in the book.

## 7.6.11 Abundance law

The abundance of excitations follows a Boltzmann-like relation
Ai∝e−Ei/Teff.A_i \propto e^{-E_i/T_{eff}}.Ai​∝e−Ei​/Teff​.
low-energy excitations appear frequently

high-energy structures are rare.

This explains why wave-like structures dominate the substrate while complex composite objects appear less often.

## 7.6.12 Formation versus survival

It is important to distinguish two separate processes:
Formation
Determined by the energy functional and excitation spectrum.
Survival
Determined by the persistence equation
S∗=EshellEDTobjRR˙ tref.S_* = \mathcal{E}_{shell}\mathcal{E}D T_{obj} \frac{R}{\dot R\,t_{ref}}.S∗​=Eshell​EDTobj​R˙tref​R​.
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

Transition to Chapter 8
Having derived the excitation spectrum from the energy functional, we now turn to a systematic classification of these structures.

 What Counts as an Excitation

