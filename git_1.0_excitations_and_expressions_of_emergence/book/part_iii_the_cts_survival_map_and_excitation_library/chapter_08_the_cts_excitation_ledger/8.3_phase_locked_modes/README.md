# 8.3 Phase-Locked Modes

## 8.3.1 From linear waves to nonlinear coherence

Section 8.2 showed that ordinary wave modes arise from linear fluctuations of the CTS field around the vacuum state.
However, when wave amplitudes become sufficiently large, nonlinear terms in the CTS functional become important.
Recall the scalar field equation

$$
\partial_t \Phi = -r\Phi + a\nabla^2\Phi - u\nabla^4\Phi - s\Phi^3.
$$

The cubic term

$$
-s\Phi^3
$$

introduces nonlinear coupling between wave modes.
These nonlinear interactions can cause waves to synchronize their phases, producing phase-locked coherent structures.

## 8.3.2 Multi-mode wave interactions

Consider a superposition of wave modes:

$$
\Phi(\mathbf{x},t) = \sum_i A_i e^{i(\mathbf{k}_i\cdot\mathbf{x}-\omega_i t)}.
$$

Substituting this expansion into the nonlinear term produces cross-coupling between modes.
Thus nonlinear terms generate mode coupling.

## 8.3.3 Resonance condition

Phase locking occurs when the interacting modes satisfy the resonance condition

$$
\mathbf{k}_1 + \mathbf{k}_2 = \mathbf{k}_3.
$$

When these relations hold, energy transfers efficiently between the modes.
This resonance allows the phases of the waves to synchronize.

## 8.3.4 Phase evolution equation

Let each wave mode be written in amplitude-phase form

$$
A_i e^{i\theta_i}.
$$

The phase dynamics can be approximated by

$$
\frac{d\theta_i}{dt} = \omega_i + \sum_j K_{ij} \sin(\theta_j - \theta_i).
$$

This equation resembles the Kuramoto synchronization model.
The coefficients $K_{ij}$ represent nonlinear coupling strengths between modes.

## 8.3.5 Phase locking condition

Phase locking occurs when the coupling strength exceeds frequency mismatch.
When this condition holds, the phase difference becomes constant:

$$
\theta_i - \theta_j = \text{constant}.
$$

Thus the waves become synchronized.

## 8.3.6 Coherent wave packets

Once phase locking occurs, the wave system behaves as a single coherent structure.
The resulting configuration can be written as

$$
\Phi(\mathbf{x},t) = A(\mathbf{x})\,e^{i(\mathbf{k}\cdot\mathbf{x}-\omega t)},
$$

where $A(\mathbf{x})$ varies slowly across space.
This structure represents a coherent wave packet.

## 8.3.7 Envelope equation

The envelope dynamics of the coherent wave packet can be approximated by the nonlinear Schrödinger equation

$$
i\partial_t A + \alpha \nabla^2 A + \beta |A|^2 A = 0,
$$

where $\alpha$ and $\beta$ are coefficients derived from the CTS parameters.

Solutions of this equation include localized structures known as solitons.

## 8.3.8 Soliton-like solutions

A simple soliton solution takes the form

$$
A(x,t) = A_0 \operatorname{sech}\!\left(\frac{x-vt}{L}\right) e^{i(kx-\omega t)}.
$$

This solution represents a localized wave packet that maintains its shape during propagation.
The characteristic width is

$$
L = \sqrt{\frac{2\alpha}{\beta A_0^2}}.
$$

Thus nonlinear interactions can produce localized coherent excitations.

## 8.3.9 Energy of phase-locked modes

The energy of a coherent wave packet scales approximately as

$$
E_{lock} \sim \int |A|^2\,d^3x.
$$

Because phase locking suppresses destructive interference, the energy remains localized for long durations.
Thus phase-locked modes possess higher structural retention than ordinary waves.

## 8.3.10 Persistence properties

Phase-locked modes improve persistence relative to simple waves because they introduce internal coherence.
However they still lack strong topological protection.
Thus their topology factor remains close to

$$
T_{obj} \approx 1.
$$

As a result they occupy an intermediate tier in the excitation hierarchy.

## 8.3.11 Role in the excitation ladder

Phase-locked modes represent the transition between

- purely linear waves
- localized nonlinear excitations.

They serve as precursors to solitons and vortices.
In the CTS hierarchy they correspond to the localized precursor region of the survival map.

## 8.3.12 Ledger entry for phase-locked modes

| Parameter | Approximate value |
|---|---|
| excitation type | phase-locked wave |
| formation energy | low |
| locking energy | small |
| topology factor | $T_{obj} \approx 1$ |
| persistence | intermediate |

Thus phase-locked modes appear more frequently than topological objects but less frequently than ordinary waves.

## 8.3.13 Summary

Phase-locked modes arise from nonlinear coupling between wave modes in the CTS substrate.
Resonance conditions synchronize wave phases, producing coherent wave packets described by nonlinear envelope equations.
These structures represent the first step toward localized excitations capable of forming persistent objects.
