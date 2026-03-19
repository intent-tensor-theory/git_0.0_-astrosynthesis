# 8.2 1.B — Non-Linear: First Membrane Events

## What Happens When the Signal Is Too Strong

A 1.A signal propagating through the Forward zone is linear — the cubic and flux-coupling terms are negligible and the signal travels as a Gaussian pulse. But as the signal approaches the membrane separating the Forward zone (+X) from the Compression zone (−X), something changes.

The membrane is not just a boundary condition — it is a **zone interface where two operators of opposite sign meet**. From section 6.2, the Forward/Compression membrane does not exist directly (opposite zones are not adjacent in the cuboctahedron). But the field can arrive at a Compression-zone region through any of the membranes adjacent to the Compression zone: Apex/Compression (Face 8) or Compression/Memory (Face 10) or Compression/Core (Face 11).

It is at these interfaces — where the field transitions from a positive-operator zone into the Compression zone (−X, operator $-\nabla^2\Phi$) — that the **first nonlinear events** occur. Here the negative Laplacian operator, combined with a sufficient field amplitude, begins to focus the field: the $-\nabla^2\Phi$ term concentrates amplitude rather than spreading it.

This section identifies the four types of 1D nonlinear membrane events, explains the physical mechanism behind each, and shows how each emerges from the master equation at the membrane junction.

---

## The Amplitude Threshold for Nonlinearity at the Membrane

A signal of wavenumber $k$ and amplitude $A$ arriving at the Compression-zone membrane experiences the full master equation (nonlinear terms no longer negligible) when:

$$
\gamma A^2 \sim D_xk^2 \quad \text{(cubic term ∼ diffusion)} \quad \Rightarrow \quad A \sim \Phi_B\,(k\xi)
$$

For $k\xi \ll 1$ (long-wavelength signals), the nonlinear threshold is **below** $\Phi_B$ — long-wavelength signals enter the nonlinear regime at lower amplitude than $\Phi_B$. For $k\xi \gg 1$ (short-wavelength signals), the threshold is above $\Phi_B$ — short-wavelength signals need more than $\Phi_B$ to go nonlinear.

The first membrane event therefore depends on the signal's wavelength:

| Signal type | $k\xi$ | Nonlinear threshold | First membrane event |
|-------------|--------|---------------------|---------------------|
| Long-wavelength pulse | $\ll 1$ | $A < \Phi_B$ | Shock (steep front) |
| Intermediate wavelength | $\sim 1$ | $A \sim \Phi_B$ | Soliton (balanced pulse) |
| Short-wavelength packet | $\gg 1$ | $A > \Phi_B$ | Kink (topological defect) |
| Point singularity | $k \to \infty$ | Any $A$ | Singular point (delta-function source) |

These four events are not four separate theories — they are four regimes of the same nonlinear dynamics at the zone membrane, distinguished by the ratio $k\xi$ and the amplitude $A/\Phi_B$.

---

## The Governing Equation at the Membrane

At the membrane separating the positive Forward zone from a negative zone (Compression or Memory), the master equation must be integrated in a thin layer of thickness $\epsilon \to 0$ straddling the membrane (the "membrane layer"). In this layer, the metric transitions sharply from $\mathcal{M}^{ij}_{+X}$ to $\mathcal{M}^{ij}_{-X}$ (or whichever negative zone is on the other side).

The result of the thin-layer integration (following section 6.1) is a **membrane equation** — an effective 1D equation for the field at the membrane surface $\Phi_m(t) = \Phi(x_m, t)$:

$$
\partial_t\Phi_m = \underbrace{-\frac{\sigma}{\epsilon_{\text{eff}}}\Phi_m}_{\text{membrane damping}} + \underbrace{\frac{D_{\text{eff}}}{\epsilon_{\text{eff}}}[\![\partial_x\Phi]\!]}_{\text{flux jump drive}} + \underbrace{\gamma|\Phi_m|^2\Phi_m}_{\text{cubic (nonlinear)}} - \kappa\Phi_m
$$

where $\epsilon_{\text{eff}}$ is the effective membrane thickness and $D_{\text{eff}}$ is the geometric mean of the two zone diffusivities. This membrane equation has the same form as the 0D Duffing equation (section 6.4) plus a flux-jump drive from the incident signal.

When the flux-jump drive $\frac{D_{\text{eff}}}{\epsilon_{\text{eff}}}[\![\partial_x\Phi]\!]$ is large (strong incident signal), the cubic nonlinearity at the membrane becomes important. This is the onset of the four nonlinear events.

---

## Event 1: The Shock (Long-Wavelength Steep Front)

When a **long-wavelength signal** ($k\xi \ll 1$, amplitude $A > A_{\text{shock}} \sim \Phi_B\,k\xi$) approaches the membrane, the spatial gradient $\partial_x\Phi$ in the membrane layer becomes very large — the field is trying to change rapidly over the coherence length $\xi$, which is the minimum allowed spatial scale.

When $|\partial_x\Phi| > (1/\xi)\Phi_B$, the flux-coupling term $-\Lambda(\partial_x\Phi)^2$ in the membrane equation dominates the linear diffusion:

$$
-\Lambda(\partial_x\Phi)^2 \gg D_x\partial_x^2\Phi
$$

This is the **shock condition**: nonlinear self-steepening overtakes linear diffusion. The result is the formation of a shock front — a narrow region of very steep field gradient that propagates at the shock velocity $v_s$ determined by the Rankine-Hugoniot conditions (section 6.5):

$$
v_s = v_g + \frac{\Lambda}{\xi}\Phi_m^2
$$

The shock velocity depends on the amplitude $\Phi_m$: larger amplitude → faster shock. This amplitude-dependent velocity is the mechanism of **shock steepening**: the higher-amplitude part of the wavefront travels faster than the lower-amplitude part, so the front continually steepens until it is limited by the coherence length $\xi$ (below which the diffusion term again dominates). The final shock width is $\delta_s \sim \xi$.

The shock is the 1D analog of a tsunami: a long-wavelength disturbance that steepens as it approaches a barrier (the membrane), forming a sharp front.

---

## Event 2: The Soliton (Balanced Pulse)

When the signal amplitude is near $\Phi_B$ and the wavenumber is near $1/\xi$ ($k\xi \sim 1$), the diffusion (spreading) and the flux-coupling (self-focusing) exactly balance at the membrane:

$$
D_x\partial_x^2\Phi \approx \Lambda(\partial_x\Phi)^2
$$

In this balanced regime, the signal neither steepens into a shock nor disperses into noise — it forms a **soliton**: a permanent, unchanging pulse that propagates without spreading or decaying.

The exact soliton solution at the membrane is the sech profile derived by Zakharov and Shabat (section 5.5):

$$
\Phi_{\text{sol}}(x, t) = \Phi_B\sqrt{2}\,\text{sech}\!\left(\frac{x - v_s t}{\xi}\right)e^{i(qx - \Omega t)}
$$

with $v_s = 2D_x q$ (the soliton velocity is proportional to the carrier wavenumber $q$), $\Omega = D_x(q^2 - 1/\xi^2)$ (the nonlinear phase frequency), and amplitude $\Phi_B\sqrt{2}$ (slightly above $\Phi_B$, consistent with being a B state).

The soliton is the canonical 1.B state. It is **the** balanced 1D nonlinear excitation — the one that sits exactly at the equilibrium between dispersion and self-focusing. The factor $\sqrt{2}$ above $\Phi_B$ is exact: it comes from requiring the cubic and diffusion terms to balance, giving $\kappa = D_x/\xi^2 = \gamma\Phi_B^2$, so $\Phi_{\text{sol}} = \sqrt{2\kappa/\gamma} = \sqrt{2}\Phi_B$.

The **first membrane event** for an intermediate-wavelength signal is soliton formation: the signal crosses the Forward/negative-zone membrane and, if its amplitude and wavenumber satisfy the balance condition, exits as a soliton rather than a dispersing pulse.

---

## Event 3: The Kink (Topological Defect)

When a **short-wavelength signal** ($k\xi \gg 1$, amplitude $A \gg \Phi_B$) encounters the membrane, neither shocks nor solitons form. Instead, the field must transition between two different stable states ($\Phi = 0$ in the Forward zone and $\Phi = \Phi_B$ in the Compression zone) over a very short spatial scale. The field cannot do this instantaneously (the coherence length $\xi$ sets the minimum spatial scale); it forms a **kink** — a topological domain wall.

The kink profile:

$$
\Phi_{\text{kink}}(x) = \frac{\Phi_B}{\sqrt{2}}\tanh\!\left(\frac{x - x_0}{\xi\sqrt{2}}\right)
$$

This is a real-valued field that interpolates smoothly from $\Phi = 0$ at $x \ll x_0$ (Forward zone, near vacuum) to $\Phi = \Phi_B/\sqrt{2} \cdot \tanh(\infty) = \Phi_B/\sqrt{2}$ at $x \gg x_0$ (Compression zone, near B-state amplitude).

Wait — the full kink from $-\Phi_B$ to $+\Phi_B$ is:

$$
\Phi_{\text{kink}}(x) = \Phi_B\tanh\!\left(\frac{x - x_0}{\xi\sqrt{2}}\right)
$$

This kink is **topologically protected**: the field value at $x \to -\infty$ is $-\Phi_B$ and at $x \to +\infty$ is $+\Phi_B$. These two asymptotic values cannot be continuously deformed into each other without passing through $\Phi = 0$ everywhere — which costs infinite energy. The kink is a stable, persistent interface between the two B-state phases.

The **topological charge** of a kink is $q_{\text{kink}} = \frac{1}{2\Phi_B}[\Phi(+\infty) - \Phi(-\infty)] = \pm 1$ — an integer, invariant under any smooth deformation.

The kink is the 1D topological excitation: a topological domain wall pinned at the membrane between two zones with different field values. It is the 1D limit of the 2.B vortex (a 0D topological charge at a 1D interface).

---

## Event 4: The Singular Point

The fourth membrane event is the limiting case $k \to \infty$ — a point-like signal that is perfectly localized ($\Phi \sim \delta(x - x_m)$ at the membrane). This is the **singular point** or **delta-function membrane source**.

A singular-point source at the membrane generates a **field singularity** at $x = x_m$: the field value $\Phi(x_m)$ is well-defined (by the continuity condition, section 6.1), but the normal derivative $\partial_x\Phi$ is discontinuous, and the second derivative $\partial_x^2\Phi$ is a delta function at $x_m$.

The singular point is not a stable excitation — it spreads immediately into a Gaussian pulse (on the Forward zone side) and a sech soliton (on the Compression zone side) over the timescale $t_{\text{spread}} \sim \xi^2/D_x$. It is an **initial condition** for the other three types of membrane events, not a lasting structure.

The physical content of the singular point: it represents a field perturbation so localized that it simultaneously activates all wavenumber modes equally. Its subsequent evolution is determined by which of the three other events (shock, soliton, kink) each wavenumber component undergoes independently. The singular point is the Fourier synthesis of all possible first membrane events.

