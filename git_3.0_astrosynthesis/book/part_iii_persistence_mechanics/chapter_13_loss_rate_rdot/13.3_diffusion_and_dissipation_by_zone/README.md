# 13.3 Diffusion and Dissipation by Zone

## Two Loss Channels

The total loss rate $\dot{R}$ arises from two physically distinct mechanisms:

**Dissipation:** Direct conversion of organized field energy into unstructured heat or vacuum fluctuations, via the damping term $\kappa_\alpha|\Phi|^2$ in the master equation. Dissipation is a local, in-zone process — the field loses energy without spatial transport.

**Diffusion:** Transport of field amplitude (and hence retained structure) from high-amplitude regions to low-amplitude regions via the gradient term $D\mathcal{M}^{ij}\partial_i\partial_j\Phi$. Diffusion is not dissipative in itself (it conserves the total field energy if $\kappa = 0$), but it causes structure loss when field amplitude diffuses to the zone boundaries and is absorbed (boundary loss) or when it diffuses from a high-metric zone (where it was well-organized) into a low-metric zone (where the same amplitude carries less organized energy per unit volume).

The zone-specific loss rate decomposes as:

$$
\dot{R}_\alpha = \dot{R}_\alpha^{\text{dissip}} + \dot{R}_\alpha^{\text{diffuse}} + \dot{R}_\alpha^{\text{transfer}}
$$

where $\dot{R}_\alpha^{\text{dissip}}$ is the local dissipation, $\dot{R}_\alpha^{\text{diffuse}}$ is the internal diffusion loss (redistribution within the zone that reduces coherence), and $\dot{R}_\alpha^{\text{transfer}}$ is the inter-zone transfer (can be positive or negative — structure transferred in from adjacent zones reduces $\dot{R}_\alpha$).

---

## Zone-Specific Diffusion Analysis

**Forward zone (+X) diffusion:**

The Forward zone has dominant $x$-direction metric $m_x^{(f)} \gg m_\perp^{(f)}$. The 1D diffusion of structure along the $x$-axis is:

$$
\dot{R}_{\text{fwd}}^{\text{diffuse}} = D m_x^{(f)}\int_{\mathcal{V}_{\text{fwd}}}|\partial_x^2\Phi|^2\,d^3r \sim Dm_x^{(f)}k_x^2\Phi^2 |\mathcal{V}_{\text{fwd}}|
$$

This loss is large because $m_x^{(f)} \gg 1$: the large Forward zone metric amplifies the diffusion rate. However, the diffusion is **directional** — it drives the field to spread along +X. Once the field reaches the Forward zone boundary at $x = L_f$ (the ICHTB edge), it can be:
- Reflected (if the boundary is reflective, $T_{\text{membrane}} \approx 0$)
- Transmitted and lost (if the boundary is lossy, $T_{\text{membrane}} \approx 1$)

For a high-reflection membrane: $\dot{R}_{\text{fwd}}^{\text{diffuse}} \approx 0$ (the field bounces back and forth without losing energy). For a lossy membrane: $\dot{R}_{\text{fwd}}^{\text{diffuse}} \sim Dm_x^{(f)}R_{\text{fwd}}/L_f^2$ — the loss rate is proportional to the diffusivity times the retained structure divided by the zone length squared.

**Expansion zone (+Y) diffusion:**

The Expansion zone has the 2D spread operator $D_\perp\nabla_\perp^2\Phi$. The 2D diffusion of a bloom (section 9.1) causes the field amplitude to decrease as:

$$
\bar{\Phi}^2_{\text{exp}}(t) = \frac{\Phi_0^2\xi^2}{4\pi D_\perp t}e^{-\kappa t}
$$

The rate of amplitude decrease:

$$
\frac{d\bar{\Phi}^2}{dt} = -\frac{\Phi_0^2\xi^2}{4\pi D_\perp t^2}e^{-\kappa t}(1 + \kappa t)
$$

For early times ($\kappa t \ll 1$): the dominant loss is from diffusion ($\propto 1/t^2$ — rapid early loss as the bloom spreads). For late times ($\kappa t \gg 1$): exponential dissipation dominates ($e^{-\kappa t}$). The crossover at $t = 1/\kappa = \tau$ marks the transition from diffusion-dominated to dissipation-dominated loss.

The **Expansion zone loss time**: at $t = t_{\max} = 1/\kappa$, the retained structure $R_{\text{exp}}$ has been reduced by a factor:

$$
\frac{R_{\text{exp}}(t_{\max})}{R_{\text{exp}}(0)} = \frac{\xi^2}{4\pi D_\perp/\kappa} = \frac{\xi^2}{4\pi\xi_\perp^2} \leq \frac{1}{4\pi} \approx 0.08
$$

At the peak of the bloom (maximum radius), 92% of the Expansion zone's initial retained structure has been lost to diffusion. The Expansion zone is a **rapid structural diffuser** — it spreads its organized content over an area $\sim\xi_\perp^2$, reducing the local amplitude to below threshold in a single coherence time.

**Memory zone (−Y) diffusion:**

The Memory zone has the curl-dominant character (antisymmetric metric $\epsilon_M$). Unlike the Expansion zone's radial diffusion, the Memory zone's diffusion is **rotational** — it drives the field amplitude to organize into circular current patterns (vortices) rather than spreading radially.

The effective diffusion in the Memory zone is not a simple spreading but a **phase diffusion** — the amplitude $|\Phi|$ remains approximately constant while the phase $\theta(\mathbf{r}_\perp, t)$ diffuses:

$$
\partial_t\theta = D_m\nabla_\perp^2\theta + \epsilon_M D_m(\partial_x^2\theta - \partial_y^2\theta) + \text{noise}
$$

The phase diffusion coefficient in the Memory zone: $D_\theta = D_m(1 \pm \epsilon_M)$ (different in the curl and anti-curl directions). Phase diffusion causes **loss of phase coherence** — the zone order parameter $\psi_{\text{mem}} \to 0$ — but not loss of amplitude (the amplitude $|\Phi|$ remains $\sim\Phi_{B,\text{mem}}$). Thus the Memory zone's diffusion loss is a loss of coherent structure (phase coherence) rather than a loss of amplitude.

The Memory zone's coherence loss rate (from the KT theory, section 9.2):

$$
\dot{R}_{\text{mem}}^{\text{diffuse}} = \begin{cases} \pi D_m\Phi_B^2 T_{\text{eff}}\xi^{-\eta(T)} & T < T_{KT} \text{ (quasi-long-range order)} \\ \Phi_B^2/\xi_{KT}^2 & T > T_{KT} \text{ (short-range order)} \end{cases}
$$

Below $T_{KT}$: the coherence loss is algebraically slow (power law in system size, set by the KT exponent $\eta$). Above $T_{KT}$: the coherence loss is exponential (set by the KT length $\xi_{KT}$). The Memory zone is a **slow phase diffuser** in the ordered phase — it preserves amplitude while slowly losing phase coherence.

---

## Zone-Specific Dissipation Analysis

**The dissipation hierarchy:**

Each zone has a characteristic damping rate $\kappa_\alpha$ (the coefficient of the linear dissipation term $-\kappa_\alpha\Phi$ in the master equation). The zone-specific dissipation:

$$
\dot{R}_\alpha^{\text{dissip}} = 2\kappa_\alpha\int_{\mathcal{V}_\alpha}|\Phi|^2\,d^3r \approx 2\kappa_\alpha\Phi_{B,\alpha}^2|\mathcal{V}_\alpha|
$$

(using $|\Phi| \approx \Phi_{B,\alpha}$ for B-state zones). The dissipation-to-$R$ ratio (the effective dissipation rate):

$$
\frac{\dot{R}_\alpha^{\text{dissip}}}{R_\alpha} = 2\kappa_\alpha\frac{\Phi_{B,\alpha}^2|\mathcal{V}_\alpha|}{\int_{\mathcal{V}_\alpha}\mathcal{E}_\alpha\,d^3r} \approx 2\kappa_\alpha\frac{\Phi_{B,\alpha}^2}{\bar{\mathcal{E}}_\alpha}
$$

For a B-state zone (where gain and loss balance), $\bar{\mathcal{E}}_\alpha \approx \gamma_\alpha\Phi_{B,\alpha}^4/4$ (potential energy at B-state minimum), giving:

$$
\frac{\dot{R}_\alpha^{\text{dissip}}}{R_\alpha} = \frac{8\kappa_\alpha}{\gamma_\alpha\Phi_{B,\alpha}^2} = \frac{8\kappa_\alpha}{\kappa_\alpha} = 8
$$

Wait — at the B-state, $\gamma_\alpha\Phi_{B,\alpha}^2 = \kappa_\alpha$, so the ratio is $8/1$... but this must be balanced by the nonlinear gain. The gain contribution to $\dot{R}$:

$$
\dot{R}_\alpha^{\text{gain}} = -2\gamma_\alpha\int_{\mathcal{V}_\alpha}|\Phi|^4\,d^3r \approx -2\gamma_\alpha\Phi_{B,\alpha}^4|\mathcal{V}_\alpha|
$$

The net dissipation rate at B-state:

$$
\dot{R}_\alpha^{\text{dissip}} + \dot{R}_\alpha^{\text{gain}} = 2(\kappa_\alpha - \gamma_\alpha\Phi_{B,\alpha}^2)\Phi_{B,\alpha}^2|\mathcal{V}_\alpha| = 0
$$

(using $\kappa_\alpha = \gamma_\alpha\Phi_{B,\alpha}^2$). The net dissipation in a B-state zone is zero — as established in section 13.1. The dissipation and gain exactly cancel at the B-state, confirming the B-state is the gain-loss equilibrium.

**The Null zone dissipation:**

The Null zone has all-negative metric and no B-state. Its dynamics:

$$
\partial_t\Phi\big|_{\text{null}} = -D|m_n|\nabla^2\Phi - \kappa_n\Phi
$$

The negative sign of the diffusion term means the Null zone **amplifies all modes**: spatial gradients increase the field amplitude rather than reducing it. This amplification is bounded only by the zone boundary — the Null zone acts as an amplifier that drives its field toward the boundary, where it is absorbed or transmitted to adjacent zones. The Null zone's dissipation:

$$
\dot{R}_{\text{null}}^{\text{dissip}} = 2\kappa_n\int_{\mathcal{V}_{\text{null}}}|\Phi|^2\,d^3r - 2D|m_n|\int_{\mathcal{V}_{\text{null}}}|\nabla\Phi|^2\,d^3r < 0
$$

The negative sign means the Null zone has **negative net dissipation** — it generates structure rather than losing it. But this generated structure flows out through the zone membranes (the Null zone's $\dot{R}_{\text{null}}^{\text{transfer}}$ is large and positive = structure leaving the Null zone). The Null zone is an **internal amplifier** that feeds structure into adjacent positive zones.

---

## The Effective Diffusion-Dissipation Balance

The total loss rate is the sum of diffusion and dissipation terms across all zones:

$$
\dot{R} = \underbrace{\dot{R}^{\text{diffuse}}}_{\text{amplitude spreading}} + \underbrace{\dot{R}^{\text{dissip,net}}}_{\text{gain-loss imbalance}} + \underbrace{\dot{R}^{\text{boundary}}}_{\text{membrane leakage}}
$$

For an ICHTB in the 3.B lock state:
- $\dot{R}^{\text{dissip,net}} \approx 0$ (all B-state zones balance their dissipation with gain)
- $\dot{R}^{\text{diffuse}} \approx 0$ (topological lock prevents amplitude spreading)
- $\dot{R}^{\text{boundary}} \approx R \times T_{\text{membrane}}/\tau_{\text{round-trip}}$ (small leakage through membranes)

The dominant loss mechanism for a 3.B locked ICHTB is the **membrane leakage** — small-amplitude modes that tunnel through the zone membranes and carry structure out of the ICHTB into the external environment. This is the physical mechanism underlying the Arrhenius decay formula $\Gamma_{\text{lock}} \sim e^{-\Delta E/T_{\text{eff}}}$: the membrane leakage rate is proportional to the probability of overcoming the zone membrane barrier, which is the Boltzmann factor for the barrier height $\Delta E$.

