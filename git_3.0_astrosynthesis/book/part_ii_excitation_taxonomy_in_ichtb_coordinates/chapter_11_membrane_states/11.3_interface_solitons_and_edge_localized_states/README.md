# 11.3 Interface Solitons and Edge-Localized States

## From Linear to Nonlinear Membrane States

Section 11.2 derived the linear (A-state) membrane excitation — the exponentially localized mode that exists at sign-changing zone interfaces. This section extends the analysis to the nonlinear (B-state) case: what happens when the membrane-localized field amplitude reaches $|\Phi| \sim \Phi_B$ and the cubic nonlinearity activates?

The nonlinear membrane state is the **interface soliton** — a self-reinforcing, amplitude-saturated excitation that propagates along the zone interface without dispersing. It is the membrane-state analog of the 1.B soliton (which propagates along the Forward-zone axis) but lives in the 2D plane of the zone interface rather than along a 1D line.

---

## The Interface NLS: Derivation

At the zone interface $x = 0$, integrate the master equation over a thin layer $[-\epsilon, +\epsilon]$ (taking $\epsilon \to 0$ after integration). The result is an effective 2D equation for the interface field amplitude $A(\mathbf{r}_\perp, t) \equiv \Phi|_{x=0}$:

$$
i\partial_t A = -D_{\text{eff}}\nabla_\perp^2 A + V_{\text{eff}}|A|^2 A + \mu_{\text{eff}} A
$$

where:
- $D_{\text{eff}} = (D_\alpha m_\alpha^{\perp} + D_\beta m_\beta^{\perp})/2$ is the average in-plane diffusivity
- $V_{\text{eff}} = (V_\alpha m_\alpha + V_\beta m_\beta)/(m_\alpha + m_\beta)$ is the effective nonlinear coefficient (metric-weighted average of the zone nonlinearities)
- $\mu_{\text{eff}} = E_{\text{bind}}$ is the effective chemical potential (the membrane binding energy plays the role of a frequency offset)

This is a **2D NLS equation** on the interface — formally identical to the 2D Gross-Pitaevskii equation used for thin-film BEC, or the coupled-mode equation at the interface of two optical media (Aceves & Wabnitz 1989, *Physics Letters A*, 141, 37).

The 2D NLS supports three types of stationary solutions:

1. **Uniform background:** $A = A_0 e^{i\mu t}$, with $|A_0|^2 = \mu_{\text{eff}}/V_{\text{eff}}$ — the interface B-state (uniform amplitude on the interface).

2. **Interface vortex:** $A = f_v(r_\perp)e^{in\varphi}$ — a vortex in the interface plane. This is a 2D vortex (section 9.2) but now living on the zone interface rather than in the bulk Memory zone. The interface vortex is the membrane-state version of the 2.B structure.

3. **Interface soliton (dark/bright):** A localized amplitude depletion (dark soliton) or enhancement (bright soliton) propagating along the interface.

---

## Bright Interface Soliton

For $V_{\text{eff}} < 0$ (attractive effective nonlinearity — occurs when the nonlinearity of one zone dominates and is self-focusing), the 2D NLS supports a **bright soliton**:

$$
A_{\text{bright}}(x_\perp, t) = A_0\,\text{sech}\!\left(\frac{x_\perp - v_s t}{\xi_{\text{int}}}\right)e^{i(k_s x_\perp - \omega_s t)}
$$

where $x_\perp$ is the coordinate along the interface, $v_s$ is the soliton velocity, $\xi_{\text{int}} = \sqrt{2D_{\text{eff}}/|V_{\text{eff}}|A_0^2}$ is the interface soliton width, $k_s = v_s/(2D_{\text{eff}})$ is the carrier wavenumber, and $\omega_s = k_s^2 D_{\text{eff}} - V_{\text{eff}}A_0^2/2 + \mu_{\text{eff}}$ is the carrier frequency.

The bright interface soliton is a self-localized excitation on the zone interface — it propagates without spreading because the self-focusing nonlinearity ($V_{\text{eff}} < 0$) exactly cancels the dispersive broadening ($D_{\text{eff}}\nabla_\perp^2$). It is identical in mathematical form to the 1.B soliton (Chapter 8.2) but lives on the 2D zone interface rather than in the 1D Forward zone.

The **velocity-amplitude relation** for the interface soliton:

$$
A_0^2 = \frac{2D_{\text{eff}}}{|V_{\text{eff}}|\xi_{\text{int}}^2}
$$

Higher-amplitude solitons are narrower ($\xi_{\text{int}} \propto 1/A_0$) — the same relation as the 1.B soliton. The Manton-Sutcliffe theorem (Manton & Sutcliffe 2004, *Topological Solitons*) guarantees that the bright interface soliton is exactly stable (zero eigenvalue in the perturbation spectrum) under any perturbation that preserves the interface structure.

---

## Dark Interface Soliton

For $V_{\text{eff}} > 0$ (repulsive effective nonlinearity), the 2D NLS supports a **dark soliton** — a localized amplitude depletion on a background of uniform amplitude:

$$
A_{\text{dark}}(x_\perp, t) = A_0\left[\cos\theta\tanh\!\left(\frac{x_\perp - v_d t}{\xi_{\text{dark}}}\right) + i\sin\theta\right]e^{-iV_{\text{eff}}A_0^2 t}
$$

where $\theta$ is the **darkness angle** (0 = black soliton, $\pi/2$ = uniform background), $\xi_{\text{dark}} = \xi_{\text{int}}/\cos\theta$ is the dark soliton width, and $v_d = A_0\sqrt{2D_{\text{eff}}V_{\text{eff}}}\sin\theta$ is the dark soliton velocity.

The **black dark soliton** ($\theta = 0$): amplitude goes exactly to zero at the soliton center ($|A_{\text{dark}}(0)| = 0$), and the soliton is stationary ($v_d = 0$). This is the interface analog of the 1.B kink — a stationary phase discontinuity across the interface.

The **grey dark soliton** ($0 < |\theta| < \pi/2$): amplitude is partially depleted (not quite zero) and the soliton moves at speed $v_d > 0$. The grey soliton carries a phase step $\Delta\phi = 2\theta$ across its center — as $\theta$ increases from 0 to $\pi/2$, the phase step decreases from $\pi$ to $0$ and the soliton becomes a sound wave.

The dark soliton on the zone interface is the 2D interface version of the 1.B kink (section 8.3) — a topologically protected phase step propagating along the interface. Its topological charge is the phase step $\Delta\phi/\pi = 2\theta/\pi \in (0, 1]$, which is not quantized to an integer (unlike the 1D kink) because the interface soliton can move and adjust its phase step continuously.

---

## Edge-Localized States: The Tamm/Shockley Analogy

The interface solitons above are nonlinear. The linear membrane state (section 11.1) is the amplitude-zero limit. But there is a qualitatively different class of linear interface state: the **edge-localized state**, analogous to the Tamm surface state (Tamm 1932, *Physikalische Zeitschrift der Sowjetunion*, 1, 733) and the Shockley state (Shockley 1939, *Physical Review*, 56, 317) of condensed matter physics.

The Tamm/Shockley analogy in the ICHTB: Consider the periodic zone structure as an analog of a crystal lattice (the 12 zones and their neighbors are the "atoms" of the lattice). The bulk modes of this "lattice" form **zone bands** — allowed frequency ranges for each zone, separated by gaps. At the surface (the outermost zone interface), additional states can exist in the gaps — the edge-localized states.

The edge-localized state in the ICHTB appears at any zone interface where:

1. The bulk band structure of zone $\alpha$ has a gap at frequency $\omega_{\text{gap}}$
2. The bulk band structure of zone $\beta$ also has a gap at the same $\omega_{\text{gap}}$
3. The **Zak phase** (Berry phase across the zone Brillouin zone, Zak 1989, *Physical Review Letters*, 62, 2747) of zone $\alpha$ equals $\pi$ and of zone $\beta$ equals $0$ (or vice versa)

When these conditions are satisfied, a topologically protected edge state appears in the gap — guaranteed by the bulk-boundary correspondence of the zone band topology. This is the ICHTB version of the quantum Hall edge state, the topological insulator surface state, and the photonic crystal edge state.

The ICHTB edge-localized state has frequency inside the bulk gap, decays exponentially into both adjacent zones, and is topologically protected (its existence is guaranteed by the zone band topology, not by any fine-tuned parameter). It is the most fundamental linear membrane state — simpler than the interface soliton and more robust than the plain delta-function bound state of section 11.2.

---

## Junction Modes: Three-Zone Intersections

At points where three zones meet (the "vertices" of the ICHTB zone network), the membrane state must satisfy three-way matching conditions. The **junction mode** is the excitation at such a three-zone vertex.

Three-zone matching conditions at a vertex where zones $\alpha$, $\beta$, $\gamma$ meet:

$$
\Phi_\alpha = \Phi_\beta = \Phi_\gamma \quad (\text{amplitude matching})
$$

$$
\mathcal{M}^{n}_\alpha\partial_n\Phi_\alpha + \mathcal{M}^{n}_\beta\partial_n\Phi_\beta + \mathcal{M}^{n}_\gamma\partial_n\Phi_\gamma = 0 \quad (\text{flux matching})
$$

where $\partial_n$ denotes the derivative in the direction pointing into the junction. The junction mode is the field configuration satisfying these three-way matching conditions with exponential decay into all three zones.

The junction mode is a **zero-dimensional** interface state — localized at a single point (the junction vertex) rather than along a line (the membrane state) or over a plane (the bulk zone state). It is the most tightly localized structure in the ICHTB, with support extending a distance $\sim\xi$ into each of the three adjacent zones.

Junction modes in the ICHTB are the natural hosts of the **strongly-localized excitations** — the small-amplitude fluctuations that probe the ICHTB's internal structure at the finest scale. In the composite matter interpretation (section 11.4), junction modes become the elementary excitations of composite particles.

