# 13.4 Effective Decay Rate and Structural Lifetime

## From Zone Rates to System Rate

Sections 13.1–13.3 derived the zone-specific loss rates $\dot{R}_\alpha$ and identified the dominant mechanisms (dissipation, diffusion, boundary leakage) for each zone. This section synthesizes these into a single **effective decay rate** $\Gamma_{\text{eff}}$ for the entire ICHTB, and from this derives the **structural lifetime** $\tau_{\text{struct}} = 1/\Gamma_{\text{eff}}$ — the characteristic timescale over which the ICHTB's retained structure $R$ decreases by a factor $e^{-1}$.

The effective decay rate is not simply the sum or average of zone rates. The zone coupling (membrane states, inter-zone transfer) creates a network of coupled decay channels, and the system-level decay rate depends on the topology of this network as well as the individual zone rates.

---

## The Decay Rate Network

Model the ICHTB zones as nodes in a directed graph, with edge weights $\Gamma_{\alpha\beta}$ representing the rate of structure transfer from zone $\alpha$ to zone $\beta$ (via the membrane state coupling). The dynamics of the zone-specific retained structure vector $\mathbf{R} = (R_1, R_2, \ldots, R_{N_z})$:

$$
\dot{\mathbf{R}} = -\mathbf{L}\mathbf{R}
$$

where $\mathbf{L}$ is the **Laplacian matrix** of the decay rate network:

$$
L_{\alpha\beta} = \begin{cases} \sum_{\gamma \neq \alpha}\Gamma_{\alpha\gamma} + \Gamma_\alpha^{\text{dissip}} & \alpha = \beta \text{ (total outflow from zone }\alpha) \\ -\Gamma_{\beta\alpha} & \alpha \neq \beta \text{ (inflow from zone }\beta\text{ to zone }\alpha) \end{cases}
$$

This is the **decay Laplacian** — the matrix version of the loss rate. Its eigenvalues $\{\lambda_k\}$ are the system-level decay rates, and the effective decay rate is:

$$
\Gamma_{\text{eff}} = \lambda_{\min}^+ = \min\{\lambda_k : \lambda_k > 0\}
$$

(the smallest positive eigenvalue — the slowest non-trivial decay mode). The slowest mode sets the long-time behavior of the ICHTB.

The **zero eigenvalue** of $\mathbf{L}$ (if it exists) corresponds to a conserved mode — a combination of zone amplitudes that decays at zero rate. For the ICHTB with a 3.B lock, the lock's topological invariant $H$ provides exactly such a conserved mode: the Hopfion amplitude combination that cannot decay (protected by the confinement mandate). This zero mode makes $\Gamma_{\text{eff}} = 0$ for the Hopfion component, giving $\tau_{\text{struct}} \to \infty$ for the topological sector.

---

## Case 1: All-A-State ICHTB (No Topological Protection)

For an ICHTB with all zones in the A-state (small amplitude, no nonlinear structure), the decay rate network has no zero eigenvalue (all modes decay). The effective decay rate is set by the slowest-decaying A-state zone.

The A-state decay rates (from section 13.1): $\Gamma_\alpha^A \approx 2\kappa_\alpha/(\mathcal{M}_\alpha k^2)$. The smallest A-state decay rate is for the largest-metric zone at the smallest wavenumber. The Apex zone at the lowest mode ($k = k_1 = \pi/R_{\text{apex}}$, the ground mode):

$$
\Gamma_{\text{Apex}}^{A,\min} = \frac{2\kappa_a}{m_z^{(a)} k_1^2} = \frac{2\kappa_a R_{\text{apex}}^2}{\pi^2 m_z^{(a)}}
$$

For $R_{\text{apex}} \sim \xi_a = \sqrt{Dm_z^{(a)}/\kappa_a}$:

$$
\Gamma_{\text{Apex}}^{A,\min} = \frac{2\kappa_a\xi_a^2}{\pi^2 Dm_z^{(a)}} = \frac{2\kappa_a}{\pi^2\kappa_a} = \frac{2}{\pi^2} \approx 0.2
$$

(in units of $1/\tau = \kappa_a$). The slowest A-state mode decays at rate $\Gamma_{\text{eff}}^A \approx 0.2\kappa$ — about five times slower than the bare dissipation rate $\kappa$.

The **all-A-state structural lifetime**:

$$
\tau_{\text{struct}}^A = \frac{1}{\Gamma_{\text{eff}}^A} \approx \frac{\pi^2}{2\kappa} \approx \frac{5}{\kappa}
$$

Five coherence times. An all-A-state ICHTB persists for about 5 damping times before its retained structure $R$ drops to $e^{-1} \approx 0.37$ of its initial value.

---

## Case 2: Mixed ICHTB (B-State in Some Zones, A-State in Others)

A more realistic ICHTB has B-state excitations in some zones (topological solitons, vortices) and A-state excitations in others. The effective decay rate is now set by the A-state zones (since B-state zones have $\Gamma^B \approx 0$).

The effective decay rate is determined by how quickly the B-state zones can replenish the A-state zones that are decaying. If the B-state zones are well-coupled to the A-state zones (high membrane transmission), the B-state acts as a **reservoir** that feeds structure back into the A-state zones, extending the lifetime. If the coupling is weak (low transmission), the A-state zones decay independently and $\Gamma_{\text{eff}} \approx \Gamma^A$.

The coupled decay rate (in the strong-coupling limit, $\Gamma_{\text{transfer}} \gg \Gamma^A$):

$$
\Gamma_{\text{eff}}^{\text{mixed}} \approx \frac{R_A}{R_A + R_B}\Gamma^A
$$

where $R_A = \sum_{\alpha\in A\text{-zones}}R_\alpha$ and $R_B = \sum_{\alpha\in B\text{-zones}}R_\alpha$ are the A-state and B-state total retained structures. For $R_B \gg R_A$ (B-state dominates):

$$
\Gamma_{\text{eff}}^{\text{mixed}} \approx \frac{R_A}{R_B}\Gamma^A \ll \Gamma^A
$$

The effective decay rate is suppressed by the ratio $R_A/R_B$ — the B-state buffer dramatically extends the lifetime. The **mixed structural lifetime**:

$$
\tau_{\text{struct}}^{\text{mixed}} \approx \frac{R_B}{R_A}\tau_{\text{struct}}^A = \frac{R_B}{R_A}\frac{\pi^2}{2\kappa}
$$

For a 3.B Hopfion ($R_B \approx R$, $R_A \approx 0$): $\tau_{\text{struct}}^{\text{mixed}} \to \infty$ — confirming the Hopfion's near-infinite lifetime.

---

## Case 3: 3.B-Locked ICHTB (Full Confinement Mandate)

For the fully locked ICHTB (3.B Hopfion with Apex phase lock), the effective decay rate is the Arrhenius rate derived in section 10.4:

$$
\Gamma_{\text{lock}} = \kappa\exp\!\left(-\frac{C D_a\Phi_B^2\xi_a|H|^{3/4}}{T_{\text{eff}}}\right)
$$

This gives the structural lifetime:

$$
\tau_{\text{struct}}^{\text{lock}} = \frac{1}{\kappa}\exp\!\left(\frac{C D_a\Phi_B^2\xi_a|H|^{3/4}}{T_{\text{eff}}}\right)
$$

For $H = 1$ and typical parameters: $\tau_{\text{struct}}^{\text{lock}} \approx \tau_0 e^{395}$ (section 10.4).

---

## The Structural Lifetime Formula: Summary

Combining all three cases into a unified formula:

$$
\tau_{\text{struct}} = \frac{1}{\kappa}\left(1 + \frac{R_B}{R_A}\right)\exp\!\left(\frac{\Delta E_{\text{top}}}{T_{\text{eff}}}\right)
$$

where:
- The factor $1/\kappa$ is the basic ICHTB timescale
- The factor $(1 + R_B/R_A)$ is the B-state buffering enhancement (1 for all-A-state, $\gg 1$ for B-state dominated)
- The exponential factor is the topological protection ($\Delta E_{\text{top}} = 0$ for non-topological states, $\Delta E_{\text{top}} = C D_a\Phi_B^2\xi_a|H|^{3/4}$ for Hopfions)

This formula gives a complete, parameterized account of the structural lifetime for any ICHTB configuration:

| Configuration | $R_B/R_A$ | $\Delta E_{\text{top}}/T_{\text{eff}}$ | $\tau_{\text{struct}}$ |
|---------------|-----------|--------------------------------------|----------------------|
| All A-state | 0 | 0 | $\pi^2/(2\kappa)$ |
| 1.B soliton | $\sim 10$ | $E_k/T$ | $\sim 10 e^{E_k/T}/\kappa$ |
| 2.B vortex | $\sim 100$ | $E_v/T$ | $\sim 100 e^{E_v/T}/\kappa$ |
| 3.B Hopfion ($H=1$) | $\sim 10^3$ | $\sim 395$ | $\sim 10^3 e^{395}/\kappa \approx 10^{174}/\kappa$ |
| Electron composite | $\sim 10^4$ | $\sim 395$ | $\sim 10^{175}/\kappa$ |

The exponential in the Hopfion case completely dominates — the topological protection factor overwhelms both the timescale $1/\kappa$ and the buffering factor $R_B/R_A$. The structural lifetime of a 3.B locked ICHTB is, for all practical purposes, infinite. This is the quantitative foundation for the claim that 3.B topological locks are the "matter" of the CTS — they persist indefinitely on any timescale relevant to the collapse process.

