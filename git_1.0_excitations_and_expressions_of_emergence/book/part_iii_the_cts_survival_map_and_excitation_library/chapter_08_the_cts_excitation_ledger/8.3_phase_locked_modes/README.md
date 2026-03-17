# 8.3 Phase-Locked Modes

## 8.3.1 From linear waves to nonlinear coherence

Section 8.2 showed that ordinary wave modes arise from linear fluctuations of the CTS field around the vacuum state.
However, when wave amplitudes become sufficiently large, nonlinear terms in the CTS functional become important.
Recall the scalar field equation
∂tΦ=2a∇2Φ−2u∇4Φ−2rΦ−4sΦ3.\partial_t \Phi = 2a\nabla^2\Phi - 2u\nabla^4\Phi - 2r\Phi - 4s\Phi^3.∂t​Φ=2a∇2Φ−2u∇4Φ−2rΦ−4sΦ3.
The cubic term
$$
4s3-4s\Phi^3
$$
introduces nonlinear coupling between wave modes.
These nonlinear interactions can cause waves to synchronize their phases, producing phase-locked coherent structures.

## 8.3.2 Multi-mode wave interactions

Consider a superposition of wave modes:
Φ(x,t)=∑iAiei(ki⋅x−ωit).\Phi$\mathbf{x},t$ = \sum_i A_i e^{i$\mathbf{k}_i\cdot\mathbf{x}-\omega_i t$}.Φ(x,t)=i∑​Ai​ei(ki​⋅x−ωi​t).
Substituting this expansion into the nonlinear term produces cross-coupling between modes.
Specifically,
Thus nonlinear terms generate mode coupling.

## 8.3.3 Resonance condition

Phase locking occurs when the interacting modes satisfy the resonance condition
k1+k2=k3\mathbf{k}_1 + \mathbf{k}_2 = \mathbf{k}_3k1​+k2​=k3​
When these relations hold, energy transfers efficiently between the modes.
This resonance allows the phases of the waves to synchronize.

## 8.3.4 Phase evolution equation

Let each wave mode be written in amplitude-phase form
Aieiθi.A_i e^{i\theta_i}.Ai​eiθi​.
The phase dynamics can be approximated by
dθidt=ωi+∑jKijsin⁡(θj−θi).\frac{d\theta_i}{dt} = \omega_i + \sum_j K_{ij} \sin$\theta_j - \theta_i$.dtdθi​​=ωi​+j∑​Kij​sin(θj​−θi​).
This equation resembles the Kuramoto synchronization model.
The coefficients KijK_{ij}Kij​ represent nonlinear coupling strengths between modes.

## 8.3.5 Phase locking condition

Phase locking occurs when the coupling strength exceeds frequency mismatch.
Mathematically
When this condition holds, the phase difference becomes constant:
θi−θj=constant.\theta_i - \theta_j = \text{constant}.θi​−θj​=constant.
Thus the waves become synchronized.

## 8.3.6 Coherent wave packets

Once phase locking occurs, the wave system behaves as a single coherent structure.
The resulting configuration can be written as
$$
(x,t)=A(x)ei(kxt).\Phi$\mathbf{x},t$ = A$\mathbf{x}$ e^{i$\mathbf{k}\cdot\mathbf{x}-\omega t$}.
$$
$$
A(x)A$\mathbf{x}$A(x)
$$
varies slowly across space.
This structure represents a coherent wave packet.

## 8.3.7 Envelope equation

The envelope dynamics of the coherent wave packet can be approximated by the nonlinear Schrödinger equation
i∂tA+α∇2A+β∣A∣2A=0.i\partial_t A + \alpha \nabla^2 A + \beta |A|^2 A =0.i∂t​A+α∇2A+β∣A∣2A=0.
$$
\alpha
$$

$$
\beta
$$

Solutions of this equation include localized structures known as solitons.

## 8.3.8 Soliton-like solutions

A simple soliton solution takes the form
A(x,t)=A0sech⁡ ⁣(x−vtL)ei(kx−ωt).A(x,t) = A_0 \operatorname{sech}\!\left$\frac{x-vt}{L}\right$ e^{i(kx-\omega t)}.A(x,t)=A0​sech(Lx−vt​)ei(kx−ωt).
This solution represents a localized wave packet that maintains its shape during propagation.
The characteristic width is
L=2αβA02.L = \sqrt{\frac{2\alpha}{\beta A_0^2}}.L=βA02​2α​​.
Thus nonlinear interactions can produce localized coherent excitations.

## 8.3.9 Energy of phase-locked modes

The energy of a coherent wave packet scales approximately as
Elock∼∫∣A∣2d3x.E_{lock} \sim \int |A|^2 d^3x.Elock​∼∫∣A∣2d3x.
Because phase locking suppresses destructive interference, the energy remains localized for long durations.
Thus phase-locked modes possess higher structural retention than ordinary waves.

## 8.3.10 Persistence properties

Phase-locked modes improve persistence relative to simple waves because they introduce internal coherence.
However they still lack strong topological protection.
Thus their topology factor remains close to
Tobj≈1.T_{obj} \approx 1.Tobj​≈1.
As a result they occupy an intermediate tier in the excitation hierarchy.

## 8.3.11 Role in the excitation ladder

Phase-locked modes represent the transition between
purely linear waves

localized nonlinear excitations.

They serve as precursors to solitons and vortices.
In the CTS hierarchy they correspond to the localized precursor region of the survival map.

## 8.3.12 Ledger entry for phase-locked modes

parameter
excitation type
phase-locked wave
formation energy
locking energy
topology factor
persistence
intermediate

Thus phase-locked modes appear more frequently than topological objects but less frequently than ordinary waves.

## 8.3.13 Summary

Phase-locked modes arise from nonlinear coupling between wave modes in the CTS substrate.
Resonance conditions synchronize wave phases, producing coherent wave packets described by nonlinear envelope equations.
These structures represent the first step toward localized excitations capable of forming persistent objects.

 Open Vortices
This section derives rotational excitations of the CTS substrate and shows how circulation introduces topological structure into the excitation ledger.

