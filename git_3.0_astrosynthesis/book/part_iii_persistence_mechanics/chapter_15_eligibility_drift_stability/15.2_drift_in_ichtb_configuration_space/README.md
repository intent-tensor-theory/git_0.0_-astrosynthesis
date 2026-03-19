# 15.2 Drift in ICHTB Configuration Space

## Configuration Space and Drift

The ICHTB field $\Phi(\mathbf{r}, t)$ lives in the infinite-dimensional **field configuration space** $\mathcal{C}$ — the space of all possible field configurations $\Phi: \text{ICHTB} \to \mathbb{C}$. The dynamics of the master equation define a **flow** on this space: each configuration $\Phi_0$ evolves under the master equation to produce a trajectory $\Phi_0 \to \Phi(t)$ in $\mathcal{C}$.

**Drift** is the systematic component of this flow — the deterministic part of the trajectory, as opposed to the stochastic fluctuations. In the master equation (with noise $\eta(\mathbf{r}, t)$ added to represent external fluctuations):

$$
\partial_t\Phi = \underbrace{D\mathcal{M}^{ij}\partial_i\partial_j\Phi + f_{\text{nonlin}}[\Phi] - \kappa\Phi}_{\text{drift } \mathbf{v}[\Phi]} + \underbrace{\eta(\mathbf{r}, t)}_{\text{noise}}
$$

The drift velocity field $\mathbf{v}[\Phi]$ on configuration space is the deterministic evolution direction at each point $\Phi$. The noise $\eta$ causes the trajectory to deviate from the drift direction — but the drift determines the long-time average behavior.

In the zone decomposition, drift acts independently on each zone's configuration, subject to the constraint that adjacent zones remain coupled through the membrane conditions. The drift in zone $\alpha$ is:

$$
\mathbf{v}_\alpha[\Phi_\alpha] = D_\alpha\nabla^2\Phi_\alpha + f_{\alpha,\text{nonlin}}[\Phi_\alpha] - \kappa_\alpha\Phi_\alpha + \sum_{\beta\sim\alpha}J_{\alpha\beta}[\Phi_\beta]
$$

where $J_{\alpha\beta}[\Phi_\beta]$ is the inter-zone coupling current from adjacent zone $\beta$ into zone $\alpha$ (via the membrane state).

---

## Drift Topology: Fixed Points, Limit Cycles, Attractors

The drift defines the topology of the configuration space flow. The fixed points of the drift ($\mathbf{v}[\Phi] = 0$) are the equilibria of the ICHTB dynamics:

**Vacuum fixed point:** $\Phi = 0$ — the trivial equilibrium. Stable in the linear limit (all modes decay to zero), unstable in the nonlinear regime (the nonlinear gain $\gamma|\Phi|^2\Phi$ becomes relevant when $|\Phi| \sim \Phi_B$, driving the field away from zero toward the B-state).

**B-state fixed point:** $\Phi = \Phi_B e^{i\theta}$ for any phase $\theta$ — the stable B-state equilibrium. The entire circle $|\Phi| = \Phi_B$ in field amplitude space is a manifold of fixed points (due to the U(1) phase symmetry). The B-state is a **stable manifold** of fixed points, not a single point.

**Topological fixed points:** The 3.B Hopfion, the 2.B vortex configuration, the 1.B soliton — all are fixed points of the drift (stationary solutions of the master equation). They are **saddle points** in configuration space: stable in the topological direction (the Hopf invariant cannot change) but potentially unstable in the non-topological directions (amplitude fluctuations can destabilize them without changing $H$).

**Limit cycles:** The KT-disordered Memory zone (section 9.2, above $T_{KT}$) exhibits **limit-cycle** behavior: the vortex gas undergoes periodic nucleation and annihilation events, creating a bounded oscillatory trajectory in configuration space rather than a fixed point.

---

## Drift Direction in the Eligibility Regions

The drift direction (the velocity vector $\mathbf{v}[\Phi]$ in configuration space) determines whether the ICHTB moves toward or away from the eligibility region $\{\mathcal{E} = 1\}$ and the persistence horizon $\{S = 1\}$.

**In the subcritical region ($S < 1$, $\mathcal{E} = 0$):** The drift points toward the vacuum — the ICHTB is drifting away from the persistence horizon, toward the vacuum fixed point. The trajectory spirals into the vacuum without crossing the persistence horizon.

**Near the critical manifold ($S \approx 1$):** The drift is approximately tangent to the persistence horizon — the ICHTB is moving along the critical manifold without crossing it. This is the **critical drift** — the trajectory that stays near $S = 1$ for an extended time before either crossing into the supercritical region (forming matter) or retreating back to the subcritical region (dissolving).

**In the supercritical region ($S > 1$):** The drift points away from the vacuum and toward the B-state attractor. Once in the supercritical region, the trajectory is carried by the drift toward higher $S$ and ultimately to the 3.B lock.

The **emergence event** (section 14.3) is the moment when the drift direction flips — the trajectory transitions from pointing toward the vacuum (subcritical drift) to pointing toward the B-state (supercritical drift). This is the bifurcation point of the ICHTB dynamics: a supercritical pitchfork bifurcation (in the language of dynamical systems theory, Strogatz 1994, *Nonlinear Dynamics and Chaos*) where the vacuum fixed point becomes unstable and the B-state manifold becomes the stable attractor.

---

## Drift as a Gradient Flow

In the limit of purely dissipative dynamics (no noise, no time-reversal-invariant terms), the drift is a **gradient flow** on the free energy landscape:

$$
\mathbf{v}[\Phi] = -\frac{\delta\mathcal{F}}{\delta\Phi^*}
$$

where $\mathcal{F}[\Phi]$ is the ICHTB free energy (section 14.5). The drift points in the direction of steepest descent of $\mathcal{F}$ — the ICHTB always moves toward lower free energy.

The free energy landscape (schematically, as a function of the field amplitude $|\Phi|$):

$$
\mathcal{F}(|\Phi|) = \frac{\kappa}{2}|\Phi|^2 - \frac{\gamma}{4}|\Phi|^4 + \frac{\mu}{6}|\Phi|^6 - T_{\text{eff}}\mathcal{S}(|\Phi|)
$$

This has two local minima:
1. At $|\Phi| = 0$ (vacuum): local minimum for $T > T_c$ (high effective temperature)
2. At $|\Phi| = \Phi_B$ (B-state): global minimum for all $T$ below the spinodal

The **spinodal** is the amplitude at which the free energy's curvature changes sign — the inflection point of $\mathcal{F}$. Above the spinodal amplitude, the field is in the basin of attraction of the B-state; below, it is in the basin of attraction of the vacuum. The spinodal is the field-space version of the persistence horizon.

The drift as gradient flow gives a **descent equation** for $R = \mathcal{F} - \mathcal{F}_{\text{ref}}$:

$$
\frac{dR}{dt} = -\left|\frac{\delta\mathcal{F}}{\delta\Phi}\right|^2 \leq 0
$$

This is a Lyapunov-type equation — $R$ decreases monotonically along the drift (confirming the Lyapunov analysis of section 14.5). The speed of descent is proportional to the gradient of the free energy — the ICHTB descends fastest when the free energy gradient is steepest (near the spinodal, where the landscape is steeply sloped).

---

## Zone Drift and Inter-Zone Coherence Development

The drift within each zone drives the zone toward its individual B-state ($\Phi_\alpha \to \Phi_{B,\alpha}$), but the inter-zone coupling causes the zones to synchronize their drift directions. The full drift in zone $\alpha$:

$$
\mathbf{v}_\alpha = -\frac{\delta\mathcal{F}_\alpha}{\delta\Phi_\alpha^*} + \sum_{\beta\sim\alpha}K_{\alpha\beta}(\Phi_\beta - e^{i\Delta\phi_{\alpha\beta}^{\text{opt}}}\Phi_\alpha)
$$

where $K_{\alpha\beta}$ is the inter-zone coupling strength (proportional to the membrane transmission $T_{\alpha\beta}$) and $\Delta\phi_{\alpha\beta}^{\text{opt}}$ is the optimal phase difference between zones $\alpha$ and $\beta$ (the phase difference that maximizes the retention matrix element $\mathcal{R}^{\alpha\beta}$, section 12.2).

The coupling term $K_{\alpha\beta}(\Phi_\beta - e^{i\Delta\phi}\Phi_\alpha)$ drives zone $\alpha$ to phase-align with zone $\beta$ — it is a **phase-pulling** term that synchronizes the zones. For strong coupling ($K_{\alpha\beta} \gg \kappa$): the zones quickly align and drift together as a unit. For weak coupling ($K_{\alpha\beta} \ll \kappa$): the zones drift independently and may develop misaligned phases (junction vortices, section 12.3).

The **drift-induced coherence development** is the progressive alignment of zone phases as the ICHTB evolves toward the B-state lock:

1. Early: zones drift independently ($K_{\alpha\beta} \sim 0$, weak membrane coupling)
2. Intermediate: zones begin to couple ($K_{\alpha\beta}$ grows as amplitudes increase), partial alignment
3. Late: zones are strongly coupled ($K_{\alpha\beta} \gg \kappa$), all phases aligned, 3.B lock established

This three-stage drift is the microscopic mechanism underlying the sequential gate activation of section 15.1 — the collapse development sequence emerges naturally from the zone drift dynamics.

---

## Metastable Drift: Trapping and Escape

The ICHTB drift can be temporarily **trapped** in a metastable configuration — a local minimum of the free energy that is not the global B-state minimum. Metastable configurations include:

- **Vortex-antivortex pairs** (section 9.2): the bound pair state is a local minimum of the Memory zone free energy, separated from the free-vortex state by the pair binding energy $E_{\text{pair}} \sim D_m\Phi_B^2\ln(R_{\text{pair}}/\xi)$
- **Domain wall bubbles** (section 9.3): a circular domain wall is a local minimum of the 2D NLS free energy at fixed total topological charge, separated from the vacuum by the bubble energy $E_{\text{bubble}} \sim D_m\Phi_B^2 r_{\text{bubble}}$
- **Frustrated braids** (section 10.3): three-vortex configurations with non-minimum-energy braid type, separated from the minimum braid by the braid energy difference

The **drift escape time** from a metastable configuration:

$$
\tau_{\text{escape}} = \tau_0\exp\!\left(\frac{\Delta\mathcal{F}_{\text{metastable}}}{T_{\text{eff}}}\right)
$$

where $\Delta\mathcal{F}_{\text{metastable}}$ is the free energy barrier separating the metastable minimum from the true global minimum (B-state lock). For $T_{\text{eff}} \ll \Delta\mathcal{F}$: the escape time is astronomically long — the ICHTB is effectively trapped. For $T_{\text{eff}} \sim \Delta\mathcal{F}$: the escape time is $\sim\tau_0$ — rapid escape.

Metastable trapping reduces the effective drift speed toward the B-state lock, extending the time to reach full eligibility. An ICHTB trapped in a metastable vortex-pair configuration may have $S \gg 1$ (supercritical — the vortex pairs are stable) but $\mathcal{E} = 0$ (ineligible — no free vortex in the Memory zone, so no spin for the composite excitation). It is stuck in a supercritical but ineligible state.

The resolution: the noise term $\eta(\mathbf{r}, t)$ in the master equation provides the fluctuations needed to escape the metastable trap. If $T_{\text{eff}} \sim \Delta\mathcal{F}_{\text{metastable}}$, the noise drives the ICHTB out of the metastable minimum and into the global B-state basin. The **effective drift** (including noise-driven escape) eventually reaches the globally eligible, globally supercritical 3.B lock.

