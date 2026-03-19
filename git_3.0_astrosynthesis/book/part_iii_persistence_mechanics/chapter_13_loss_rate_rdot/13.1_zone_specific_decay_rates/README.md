# 13.1 Zone-Specific Decay Rates

## From R to Ṙ: The Rate of Structural Loss

Chapter 12 defined the retained structure $R$ — the total organized energy of the ICHTB, partitioned by zone. Chapter 13 asks: how fast does $R$ decrease? The **loss rate** $\dot{R} = -dR/dt$ (positive when $R$ is decreasing) is the rate at which organized structure is converted to unstructured heat or vacuum fluctuations.

The loss rate is not uniform across zones — each zone has its own characteristic decay rate, set by its metric properties and the type of excitations it hosts. The Forward zone (+X), with its propagating modes and low topological protection, loses structure fastest. The Apex zone (+Z), with its temporal locking and strong coupling to the 3.B Hopfion, loses structure slowest (nearly zero for a fully locked 3.B state). The total loss rate is dominated by the fastest-decaying zone that contains significant retained structure.

**Definition:** The zone-specific loss rate:

$$
\dot{R}_\alpha = -\frac{dR_\alpha}{dt}
$$

The total loss rate:

$$
\dot{R} = \sum_\alpha\dot{R}_\alpha
$$

The zone contributions to $\dot{R}$ are not independent — inter-zone coupling (membrane states) transfers structure between zones, so loss in one zone can be partially compensated by transfer from adjacent zones. But the net total $\dot{R}$ is always non-negative (second law: organized structure can only decrease in the absence of external drives).

---

## The General Decay Equation

From the master equation (section 4.3):

$$
\partial_t\Phi = D\sum_{i,j}\mathcal{M}^{ij}(\mathbf{r})\partial_i\partial_j\Phi + f_{\text{nonlin}}[\Phi] - \kappa(\mathbf{r})\Phi
$$

The rate of change of $R_\alpha = \int_{\mathcal{V}_\alpha}\mathcal{E}_\alpha\,d^3r$ is:

$$
\dot{R}_\alpha = -\frac{d}{dt}\int_{\mathcal{V}_\alpha}\mathcal{E}_\alpha\,d^3r = -\int_{\mathcal{V}_\alpha}\frac{\partial\mathcal{E}_\alpha}{\partial t}\,d^3r
$$

Using the continuity equation for the energy density (derived from the master equation):

$$
\frac{\partial\mathcal{E}_\alpha}{\partial t} = -\nabla\cdot\mathbf{J}_\alpha^E + \sigma_\alpha
$$

where $\mathbf{J}_\alpha^E$ is the energy current density (carries energy between regions) and $\sigma_\alpha$ is the local energy source/sink. Integrating over the zone volume:

$$
\dot{R}_\alpha = \oint_{\partial\mathcal{V}_\alpha}\mathbf{J}_\alpha^E\cdot d\mathbf{S} - \int_{\mathcal{V}_\alpha}\sigma_\alpha\,d^3r
$$

The surface integral is the **inter-zone energy flux** (energy flowing across zone boundaries = membrane transfer). The volume integral is the **bulk dissipation** (energy lost within the zone to damping $\kappa_\alpha$). Both contribute to $\dot{R}_\alpha$.

---

## Zone-Specific Decay Rates: Derivation

For each zone, compute $\dot{R}_\alpha$ by evaluating the bulk dissipation term. In the linear (A-state) limit, the dominant dissipation comes from the damping term $-\kappa_\alpha|\Phi|^2$:

$$
\sigma_\alpha = 2\kappa_\alpha|\Phi|^2|\mathcal{V}_\alpha
$$

(energy dissipated per unit volume per unit time). For a zone with mean amplitude $\bar{\Phi}_\alpha^2 = \langle|\Phi|^2\rangle_{\mathcal{V}_\alpha}$:

$$
\dot{R}_\alpha^{\text{bulk}} = 2\kappa_\alpha\bar{\Phi}_\alpha^2|\mathcal{V}_\alpha|
$$

This gives the decay rate $\Gamma_\alpha = \dot{R}_\alpha/R_\alpha$:

$$
\Gamma_\alpha = \frac{\dot{R}_\alpha^{\text{bulk}}}{R_\alpha} = \frac{2\kappa_\alpha\bar{\Phi}_\alpha^2|\mathcal{V}_\alpha|}{\int_{\mathcal{V}_\alpha}\mathcal{E}_\alpha\,d^3r}
$$

For a zone in the A-state (small amplitude, $|\Phi| \ll \Phi_{B,\alpha}$), the energy density is primarily kinetic: $\mathcal{E}_\alpha \approx \mathcal{M}_\alpha|\nabla\Phi|^2 \sim \mathcal{M}_\alpha k^2|\Phi|^2$. Then:

$$
\Gamma_\alpha^A = \frac{2\kappa_\alpha}{\mathcal{M}_\alpha k^2 + \kappa_\alpha} \approx \frac{2\kappa_\alpha}{\mathcal{M}_\alpha k^2} \quad (\text{for }\mathcal{M}_\alpha k^2 \gg \kappa_\alpha)
$$

The **A-state decay rate** decreases with increasing metric $\mathcal{M}_\alpha$ (large metric → large gradient energy → slower relative decay) and with increasing wavenumber $k$ (smaller-scale excitations decay slower relative to their energy). This is the fundamental reason why the large-metric Apex zone decays slowly: its metric $m_z^{(a)} \gg m_0$ means $\mathcal{M}_{\text{apex}} k^2 \gg \kappa$, giving $\Gamma_{\text{apex}}^A \ll \kappa$.

For a zone in the B-state ($|\Phi| \sim \Phi_{B,\alpha}$), the energy density has both kinetic and potential contributions, and the nonlinear term provides a **gain** that partially cancels the dissipation. The effective B-state decay rate:

$$
\Gamma_\alpha^B = \kappa_\alpha - \gamma_\alpha\bar{\Phi}_\alpha^2 = \kappa_\alpha - \gamma_\alpha\Phi_{B,\alpha}^2 = 0
$$

(using $\gamma_\alpha\Phi_{B,\alpha}^2 = \kappa_\alpha$). The B-state decay rate is **exactly zero** — the nonlinear gain exactly cancels the dissipation at the B-state amplitude. This is the definition of the B-state: the amplitude where gain and loss balance exactly. So B-state zones do not decay from bulk dissipation — their $\dot{R}_\alpha^{\text{bulk}} = 0$.

The only decay mechanism for B-state zones is **inter-zone energy flux** — structure can be lost by flowing out through the zone membranes. This is the surface integral term, which is governed by the membrane transmission coefficients (section 6.2).

---

## Zone Decay Rate Table

Combining the A-state and B-state analysis, the characteristic decay rates for each ICHTB zone:

| Zone | Type | $\Gamma_\alpha^A$ | $\Gamma_\alpha^B$ | Dominant decay mechanism |
|------|------|------------------|------------------|--------------------------|
| Forward (+X) | Propagating | $\kappa_f/(\mathcal{M}_{xx}^f k_x^2)$ | $\sim 0$ (if B-state) | Rapid: propagation out of zone + boundary loss |
| Compression (−X) | Focusing | $\kappa_c/(|\mathcal{M}_{xx}^c| k_x^2)$ (imaginary $\Rightarrow$ growth) | Soliton: $\approx 0$ | Self-focusing accumulates at kink centers |
| Expansion (+Y) | Spreading | $\kappa_e/(\mathcal{M}_\perp^e k_\perp^2)$ | $\approx 0$ | Fast: 2D spread dilutes amplitude rapidly |
| Memory (−Y) | Rotating | $\kappa_m/(\mathcal{M}_m k^2)$ (slow) | Vortex: $\approx 0$ | KT transition sets slow vortex-gas loss |
| Apex (+Z) | Temporal | $\kappa_a/(\mathcal{M}_z^a k_z^2) \ll \kappa$ | Lock: $= 0$ | Slowest: large $m_z^a$ suppresses A-rate |
| Null (−0) | Dissipative | $\kappa_n/(-|\mathcal{M}_n| k^2)$ (fast) | No B-state | Fastest: all-negative metric ⇒ immediate loss |
| Core (+0) | Isotropic | $\kappa_0/(\mathcal{M}_0 k^2)$ (moderate) | $\approx 0$ | Moderate: isotropic metric, central location |
| Membrane | Interface | $E_{\text{bind}}/(\text{interface})$ | $\approx 0$ | Bound: loss requires overcoming $E_{\text{bind}}$ |

The Null zone stands out: it has all-negative metric $\mathcal{M}_n^{ij} = -m_n\delta^{ij}$, which means the effective "diffusivity" is **negative** — the field in the Null zone is unstable to growth at all wavelengths (the negative metric acts as a negative stiffness). However, this growth is self-limiting: as the amplitude increases toward $\Phi_{B,n}$, the nonlinear term saturates... but the Null zone has no stable B-state ($V_n(|\Phi|^2)$ has no local minimum). The field in the Null zone grows, reaches the edge of the zone, and is reflected back into adjacent zones — the Null zone is a **transient amplifier**, not a storage zone.

---

## The Loss Spectrum

Each zone contributes to the total loss rate $\dot{R}$ with a characteristic timescale $\tau_\alpha = 1/\Gamma_\alpha$. The **loss spectrum** $\mathcal{L}(\tau)$ — the distribution of loss timescales across all zones and modes — determines how quickly the ICHTB structure degrades.

For a typical ICHTB with all zones populated:

$$
\mathcal{L}(\tau) = \sum_\alpha\sum_{nlm}R^\alpha_{nlm}\delta(\tau - \tau^\alpha_{nlm})
$$

The loss spectrum has peaks at each zone's characteristic timescale. The **fast peak** (short $\tau$) comes from the Null zone and the Expansion zone's high-$k$ modes. The **slow peak** (long $\tau$) comes from the Apex zone's low-$k$ modes and the 3.B lock (which has $\tau \to \infty$). The **intermediate structure** fills in between, governed by the Memory zone's KT physics and the Forward zone's propagation loss.

The integrated loss rate:

$$
\dot{R} = \int_0^\infty \frac{\mathcal{L}(\tau)}{\tau}\,d\tau
$$

is dominated by the fast-decaying modes (small $\tau$). This means that the total loss rate $\dot{R}$ is set primarily by the fastest-decaying zone containing significant structure — not by the slow-decaying zones that hold most of the retained structure. For an ICHTB with a 3.B lock (slow) and transient surface excitations (fast), $\dot{R}$ is dominated by the surface excitation loss even though most of $R$ is in the stable lock.

