# 8.4 Persistence of 1D States in ICHTB Terms

## What Does "Persistent" Mean?

In everyday language, persistent means "lasting." In the CTS, persistence has a precise technical definition: an excitation is **persistent** if its amplitude remains above the noise floor $\Phi_{\text{noise}}$ for all time, without requiring external energy input. A persistent excitation is self-sustaining — it maintains itself against the linear damping $-\kappa\Phi$ through its own nonlinear dynamics.

All A states (1.A, 2.A, 3.A) are non-persistent: they decay exponentially with rate $\kappa$ and require repeated re-excitation to be maintained. All B states (1.B, 2.B, 3.B) are (in principle) persistent: their nonlinear structure counteracts the linear damping.

But "in principle" is doing a lot of work. The 1.B states (soliton, shock, kink) are persistent against linear damping, but they can be destroyed by perturbations that change their topological or dynamical invariants. This section examines, for each 1D excitation type, the precise conditions for persistence and the mechanisms of failure.

---

## Persistence of the Soliton

The soliton is the most precisely characterized 1D persistent excitation. Its four conserved quantities (norm $N$, momentum $P$, energy $E$, phase $\theta_0$) are exactly conserved by the master equation in the absence of perturbations. The soliton is **algebraically stable** in the strict sense: small perturbations to the soliton parameters shift the values of $N, P, E, \theta_0$ but do not destroy the soliton — they merely shift it to a nearby soliton solution.

The soliton's persistence is governed by four mechanisms:

**1. Amplitude robustness** — The soliton amplitude is fixed at $\Phi_B\sqrt{2(1 - v^2/v_{\max}^2)^{-1}}$ by the balance condition. A perturbation that reduces the amplitude by $\delta A$ causes the soliton to shed **radiation** (a 1.A wave packet that carries away the excess energy), and the soliton relaxes to the nearest soliton solution with the corrected amplitude. The soliton is robust against amplitude perturbations: it heals.

**2. Velocity robustness** — The soliton velocity can be changed by an external force (a spatially varying $\kappa(\mathbf{x})$ or a time-dependent $D(t)$). In the ICHTB, the velocity changes as the soliton crosses zone boundaries. Using the **adiabatic approximation** (valid when the zone metric varies slowly on the scale of $\xi_{\text{sol}}$):

$$
v_{\text{sol}}(t) \approx v_0\sqrt{\frac{D_x(t)}{D_x(0)}}
$$

The soliton accelerates in zones of increasing diffusivity and decelerates in zones of decreasing diffusivity. The soliton trajectory through the ICHTB is a **geodesic in the effective metric** $D_x(\mathbf{x})$ — a curved path determined by the zone metric variations.

**3. Collision robustness** — As established in section 8.3, soliton-soliton collisions are elastic — the soliton emerges from every collision with its norm $N$ and amplitude $\Phi_B\sqrt{2}$ unchanged. The only permanent change is the phase shift $\Delta\theta_{12}$. This makes solitons ideal information carriers: they can pass through each other without being destroyed, accumulating phase information about every collision.

**4. Zone boundary robustness** — At the ICHTB zone boundaries (membranes), the soliton is partially transmitted and partially reflected. The **soliton transmission coefficient** at a membrane with surface conductance $\sigma$:

$$
T_{\text{sol}} = 1 - \frac{\sigma^2\xi^2}{4D_x^2 + \sigma^2\xi^2}
$$

For $\sigma = 0$ (transparent membrane): $T_{\text{sol}} = 1$, full transmission. For $|\sigma\xi/D_x| \ll 1$ (weakly opaque): $T_{\text{sol}} \approx 1 - (\sigma\xi)^2/4D_x^2$ (small reflection loss). The soliton can traverse the full ICHTB (crossing all membranes) if each membrane is sufficiently transparent. The total transmission through $n$ membranes is $T_{\text{tot}} = T_{\text{sol}}^n$; for $n = 12$ membranes and $T_{\text{sol}} = 0.99$, $T_{\text{tot}} = 0.99^{12} \approx 0.886$ — still 89% of the soliton survives a full ICHTB traversal.

---

## Persistence of the Kink

The kink is topologically persistent — its topological charge $q_{\text{kink}} = \pm 1$ cannot be changed without a globally destructive event (the field must reach zero everywhere, costing infinite energy in the thermodynamic limit). But the kink is only finitely persistent in a finite ICHTB: in a finite system, the kink can **annihilate** with an anti-kink (a kink of opposite topological charge) if they approach each other closely enough.

**Kink-antikink annihilation:** When a kink (+1) and anti-kink (−1) approach within distance $d_{\text{ann}} \sim \xi$, their overlap allows quantum tunneling between the two topological sectors. The annihilation rate per unit time:

$$
\Gamma_{\text{ann}} = \omega_{\text{att}}\exp\!\left(-\frac{E_{\text{kink}}}{D_x/\xi}\right) = \omega_{\text{att}}\exp\!\left(-\frac{2\sqrt{2}}{3}\frac{\Phi_B^2\xi^2}{D_x}\cdot\frac{1}{\xi}\cdot\xi\right)
$$

This is a thermally activated process in the CTS sense: the kink can be destroyed by fluctuations with energy $\sim E_{\text{kink}}$. For $\Phi_B^2\xi^2/D_x \gg 1$ (deep in the B-state regime), the annihilation rate is exponentially suppressed — the kink is essentially permanent. For $\Phi_B^2\xi^2/D_x \sim 1$ (near the A-state threshold), the kink is fragile and rapidly annihilates.

The **kink persistence condition** in ICHTB terms: the kink survives if the ICHTB size $L \gg L_{\text{ann}} = \xi\exp(E_{\text{kink}}/D_x)$ — the system must be large enough that kink and anti-kink are unlikely to encounter each other during the observation time.

---

## Persistence of the Shock

The shock is the least persistent of the 1D nonlinear structures. It is not topologically protected (no topological invariant), and it is not algebraically stable (no exact conservation law protects it). The shock persists only as long as the nonlinear steepening overcomes the linear diffusion.

The **shock lifetime** in the CTS:

$$
\tau_{\text{shock}} = \frac{\xi^2}{D_x}\frac{1}{(A/\Phi_B)^2 - 1}
$$

For $A \gg \Phi_B$: $\tau_{\text{shock}} \approx \xi^2/D_x(A/\Phi_B)^{-2}$ — large-amplitude shocks decay quickly (counter-intuitively, because the large amplitude enhances both the self-steepening and the dissipation). For $A \to \Phi_B^+$: $\tau_{\text{shock}} \to \infty$ — a shock at the threshold amplitude is permanent (it has become a soliton). The shock lifetime diverges as the shock approaches the soliton balance condition.

The shock is a **transient** 1D excitation on the way to becoming either a soliton (if amplitude adjusts to $\sim\Phi_B$) or dispersive radiation (if amplitude falls below $\Phi_B$). It does not have a stable long-time limit of its own — its long-time fate is always one of the other three structures.

---

## The Persistence Hierarchy of 1D States

Ranking the 1D structures by persistence (most to least durable):

| Structure | Persistence mechanism | Typical lifetime | ICHTB zone |
|-----------|----------------------|-----------------|-----------|
| Kink | Topological charge | $\gg \tau = 1/\kappa$ (permanent for $L \gg L_{\text{ann}}$) | Compression/Forward membrane |
| Soliton | Algebraic invariants ($N, P, E$) | $\gg \tau$ (permanent in homogeneous ICHTB) | Compression (−X) |
| Shock | Nonlinear steepening vs. diffusion | $\sim \xi^2/D_x$ (finite, converts to soliton or radiation) | Forward/Compression transition |
| Signal (1.A) | None | $\tau = 1/\kappa$ (exponential decay) | Forward (+X) |

The persistence hierarchy confirms the A/B split of section 7.1: 1.A signals are non-persistent, 1.B structures (soliton, kink) are persistent. The shock occupies a liminal position — more persistent than the 1.A signal but less than the true B states.

---

## 1D States as Information Storage

The four invariants of the soliton ($N, P, E, \theta_0$) are four independent bits of information that the soliton carries without loss. A **soliton information channel** in the ICHTB encodes information in these four parameters and transmits them from one zone to another via soliton propagation.

Each soliton-soliton collision adds a phase shift $\Delta\theta_{12}$ that depends on the relative soliton parameters — this phase shift is **a record of the collision**. A soliton that has passed through $n$ other solitons carries a total phase shift:

$$
\theta_{\text{total}} = \theta_0 + \sum_{j=1}^{n}\Delta\theta_{1j}
$$

This cumulative phase is the soliton's **history** — a complete record of every interaction it has undergone since its formation. In a dense ICHTB soliton gas, the phase of each soliton encodes the full interaction history of the system. This is the CTS model of **memory**: not stored in a static structure (like a kink), but encoded in the dynamical phase of an active propagating excitation.

The kink, by contrast, is static memory: it stores information in its position $x_0$ and topological charge $q_{\text{kink}}$. A kink at position $x_0$ is a binary bit (charge $\pm 1$) at a fixed location — it is the CTS equivalent of a classical bit in a digital memory. The soliton is a more sophisticated storage medium: analog, multi-valued, and dynamically updated by interactions.

Both the kink (static, binary) and the soliton (dynamic, analog) are 1D B-state information structures. Together they constitute the **1D information layer** of the ICHTB — the simplest persistent information structures in the CTS, from which all higher-dimensional information structures (2D vortex memories, 3D topological archives) are built.

