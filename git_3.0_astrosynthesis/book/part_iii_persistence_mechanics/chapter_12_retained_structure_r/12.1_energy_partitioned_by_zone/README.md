# 12.1 Energy Partitioned by Zone

## Introducing the Retained Structure R

Part II established the excitation taxonomy: the complete catalogue of structures that can exist in the ICHTB. Part III asks a different question — not "what can exist?" but "what persists?" A structure may be topologically stable in principle while being energetically negligible in practice; a membrane state may be bound but weakly so. The concept of **Retained Structure R** quantifies the total organized content of the ICHTB: how much structured field is actually present, how it is distributed across zones, and how it contributes to the ICHTB's capacity to maintain a coherent collapse trajectory.

**Definition:** The retained structure $R$ is the total zone-partitioned energy of the ICHTB collapse field $\Phi$, expressed as a sum over zone contributions:

$$
R = \sum_\alpha R_\alpha = R_{\text{core}} + R_{\text{fwd}} + R_{\text{mem}} + R_{\text{exp}} + R_{\text{comp}} + R_{\text{apex}} + R_{\text{null}} + R_{\text{membrane}}
$$

where each $R_\alpha$ is the contribution to the total retained structure from zone $\alpha$, and $R_{\text{membrane}}$ is the contribution from the zone interfaces collectively.

The word "retained" is deliberate: $R$ measures structure that has been organized (excited above the vacuum $\Phi = 0$) and is being maintained against dissipation. It is not the total energy (which includes vacuum fluctuations and dissipated heat) but the **coherent, organized fraction** of the energy — the fraction that is carrying meaningful, topologically structured information about the collapse trajectory.

---

## Zone Energy Functionals

Each zone $\alpha$ contributes to $R$ through its local energy functional. The general form:

$$
R_\alpha = \int_{\mathcal{V}_\alpha}\mathcal{E}_\alpha(\mathbf{r})\,d^3r
$$

where $\mathcal{V}_\alpha$ is the spatial volume of zone $\alpha$ within the ICHTB, and $\mathcal{E}_\alpha$ is the local energy density in that zone. The energy density has the Ginzburg-Landau form:

$$
\mathcal{E}_\alpha(\mathbf{r}) = \sum_{i,j}\mathcal{M}^{ij}_\alpha\partial_i\Phi^*\partial_j\Phi + V_\alpha(|\Phi|^2)
$$

where the first term is the **kinetic energy** (gradient energy, weighted by the zone metric) and $V_\alpha$ is the **potential energy** (zone-specific effective potential). The potential:

$$
V_\alpha(|\Phi|^2) = \frac{\kappa_\alpha}{2}|\Phi|^2 - \frac{\gamma_\alpha}{4}|\Phi|^4 + \frac{\mu_\alpha}{6}|\Phi|^6
$$

The quartic term $-\gamma_\alpha|\Phi|^4/4$ allows the potential to have a minimum at $|\Phi|^2 = \kappa_\alpha/\gamma_\alpha = \Phi_{B,\alpha}^2$ (the B-state amplitude for zone $\alpha$). The sixth-order term $\mu_\alpha|\Phi|^6/6$ ensures the potential is bounded below (prevents runaway to infinite amplitude). Together, the quadratic, quartic, and sixth-order terms give the **double-well potential** of the ICHTB — a vacuum at $|\Phi| = 0$ and a B-state minimum at $|\Phi| = \Phi_{B,\alpha}$.

The **zone-specific B-state amplitude**:

$$
\Phi_{B,\alpha}^2 = \frac{\kappa_\alpha}{\gamma_\alpha}
$$

This varies by zone: zones with large $\gamma_\alpha$ (strong nonlinearity) have small $\Phi_{B,\alpha}$; zones with small $\gamma_\alpha$ (weak nonlinearity) have large $\Phi_{B,\alpha}$. The Core zone (+0) has the largest $\Phi_{B,\text{core}}$ (deepest potential well), while the Null zone (−0) has a potential that curves upward (no stable B-state — consistent with the Null zone's role as the dissipative zone that pulls the field back toward vacuum).

---

## Explicit Zone Contributions

**Core zone contribution $R_{\text{core}}$:**

$$
R_{\text{core}} = \int_{\mathcal{V}_{\text{core}}}\left[m_c|\nabla\Phi|^2 + \frac{\kappa_c}{2}|\Phi|^2 - \frac{\gamma_c}{4}|\Phi|^4\right]d^3r
$$

The Core zone metric is isotropic ($m_c^{ij} = m_c\delta^{ij}$), so the gradient energy is simply $m_c|\nabla\Phi|^2$. The Core's $R_{\text{core}}$ is the most "universal" contribution — it samples the field at the center of the ICHTB, where all zone influences overlap. A high $R_{\text{core}}$ means the collapse field has strong, organized amplitude at the center — the ICHTB is "fully activated."

**Forward zone contribution $R_{\text{fwd}}$:**

$$
R_{\text{fwd}} = \int_{\mathcal{V}_{\text{fwd}}}\left[m_x^{(f)}|\partial_x\Phi|^2 + m_\perp^{(f)}|\nabla_\perp\Phi|^2 + V_f(|\Phi|^2)\right]d^3r
$$

The Forward zone has anisotropic metric: $m_x^{(f)} \gg m_\perp^{(f)}$, so the dominant contribution is the $x$-gradient energy $m_x^{(f)}|\partial_x\Phi|^2$. A high $R_{\text{fwd}}$ means the field has strong variation in the forward direction — i.e., the ICHTB has a well-developed propagating mode along +X.

**Memory zone contribution $R_{\text{mem}}$:**

$$
R_{\text{mem}} = \int_{\mathcal{V}_{\text{mem}}}\left[m_m|\nabla_\perp\Phi|^2 + \epsilon_M m_m\,\text{Im}(\Phi^*\nabla_\perp^2\Phi) + V_m(|\Phi|^2)\right]d^3r
$$

The Memory zone includes the antisymmetric metric contribution (proportional to $\epsilon_M$) in the form $\text{Im}(\Phi^*\nabla_\perp^2\Phi)$ — the imaginary part of the field's self-Laplacian, which is zero for real fields but non-zero for fields with phase structure. This term measures the **rotational content** of the Memory zone field: it is positive for vortices (rotating phase) and zero for irrotational fields. A high $R_{\text{mem}}$ with a large $\epsilon_M$ contribution indicates a strong vortex structure in the Memory zone.

**Apex zone contribution $R_{\text{apex}}$:**

$$
R_{\text{apex}} = \int_{\mathcal{V}_{\text{apex}}}\left[m_z^{(a)}|\partial_z\Phi|^2 + m_\perp^{(a)}|\nabla_\perp\Phi|^2 + V_a(|\Phi|^2) + \frac{\omega_B^2}{2D_a}|\Phi|^2\right]d^3r
$$

The Apex zone includes an additional temporal contribution $(\omega_B^2/2D_a)|\Phi|^2$ — this is the energy stored in the temporal oscillation at frequency $\omega_B$. When the Apex zone is fully active (3.B lock established), this term contributes $\sim(\omega_B^2/2D_a)\Phi_B^2\mathcal{V}_{\text{apex}}$ — a substantial stored energy proportional to the ICHTB volume times the B-state amplitude.

**Membrane contribution $R_{\text{membrane}}$:**

$$
R_{\text{membrane}} = \sum_{\langle\alpha\beta\rangle}\int_{\mathcal{S}_{\alpha\beta}}\mathcal{E}_{\text{mem}}(\mathbf{r}_\perp)\,d^2r_\perp
$$

where the sum is over all zone interfaces $\langle\alpha\beta\rangle$ and $\mathcal{S}_{\alpha\beta}$ is the interface surface. The interface energy density $\mathcal{E}_{\text{mem}}$ is the 2D version of the bulk energy density, evaluated at the interface amplitude $A(\mathbf{r}_\perp)$:

$$
\mathcal{E}_{\text{mem}} = D_{\text{eff}}|\nabla_\perp A|^2 + V_{\text{eff}}(|A|^2) - E_{\text{bind}}|A|^2
$$

The binding energy term $-E_{\text{bind}}|A|^2$ is negative — it lowers the energy of membrane-localized field relative to the vacuum. A high $R_{\text{membrane}}$ means the interfaces are carrying significant organized field — many membrane states are activated.

---

## The Total $R$ as a Stability Measure

The total retained structure:

$$
R = R_{\text{core}} + R_{\text{fwd}} + R_{\text{comp}} + R_{\text{exp}} + R_{\text{mem}} + R_{\text{apex}} + R_{\text{null}} + R_{\text{membrane}}
$$

is the ICHTB's primary stability measure. A high $R$ means:
- The field is organized in multiple zones simultaneously
- The zones are all contributing coherent, structured excitations
- The total organized energy is large compared to the fluctuation energy

A low $R$ means:
- The field is mostly in the vacuum ($\Phi \approx 0$ everywhere)
- Zone excitations are transient (A-state, dispersing)
- The ICHTB has not yet developed persistent structure

The dynamics of $R$ — how it grows, decays, and reaches equilibrium — are the subject of Chapter 13 (loss rate $\dot{R}$), Chapter 14 (the Selection Number $S = R/\dot{R}t_{\text{ref}}$), and Chapter 15 (stability gates). Together, these chapters describe the **persistence mechanics** of the ICHTB: the quantitative theory of how structure is created, maintained, and lost.

