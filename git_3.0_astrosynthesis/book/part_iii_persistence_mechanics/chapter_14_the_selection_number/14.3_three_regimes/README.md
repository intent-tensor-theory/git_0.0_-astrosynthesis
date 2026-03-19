# 14.3 Three Regimes — Subcritical, Critical, Supercritical

## The Three Regimes of S

The Selection Number $S = \tau_{\text{eff}}/t_{\text{ref}}$ partitions all ICHTB states into three qualitatively distinct regimes. These are not just mathematical subdivisions — they correspond to fundamentally different physical behaviors of the collapse trajectory.

---

## Regime 1: Subcritical ($S < 1$)

**Condition:** $\tau_{\text{eff}} < t_{\text{ref}}$ — the ICHTB decays faster than the collapse proceeds.

**Dynamics:** The retained structure $R(t)$ decreases monotonically:

$$
R(t) \approx R_0\exp(-\bar{\Gamma}t) = R_0\exp(-t/\tau_{\text{eff}})
$$

Before the collapse window closes (at $t = t_{\text{ref}}$), the retained structure has dropped to:

$$
R(t_{\text{ref}}) = R_0 e^{-t_{\text{ref}}/\tau_{\text{eff}}} = R_0 e^{-1/S}
$$

For $S \ll 1$: $R(t_{\text{ref}}) \approx R_0 e^{-1/S} \approx 0$ — essentially all structure is lost before the collapse completes. The ICHTB dissolves and the collapse fails to produce persistent matter.

**Physical meaning:** The subcritical regime is the regime of **transient excitation** — structures that form but dissipate before the collapse window closes. All A-state excitations are subcritical: their $\tau_{\text{eff}} \sim 5/\kappa$ is shorter than or comparable to $t_{\text{ref}} = 1/\kappa$, giving $S \sim 5$... wait, $S = \tau_{\text{eff}}/t_{\text{ref}} \approx (5/\kappa)/(1/\kappa) = 5 > 1$. Let me reconsider — the all-A-state ICHTB with $\tau_{\text{struct}}^A \approx 5/\kappa$ and $t_{\text{ref}} = 1/\kappa$ gives $S = 5$, which is supercritical!

The subcritical condition $S < 1$ requires $\tau_{\text{eff}} < t_{\text{ref}} = 1/\kappa$. From the zone decay rate table (section 13.1), subcritical modes have $\Gamma_\alpha > \kappa$, i.e., $\mathcal{M}_\alpha k^2 < 2\kappa$ — modes with small metric or high wavenumber (no, high $k$ gives small $\Gamma$). Let me recalculate: $\Gamma_\alpha^A = 2\kappa/(\mathcal{M}_\alpha k^2 + \kappa)$. For $\Gamma_\alpha^A > \kappa$: $2\kappa > \kappa(\mathcal{M}_\alpha k^2 + \kappa)$... this requires $\mathcal{M}_\alpha k^2 < 1$, i.e., the gradient energy is less than $\kappa$. This applies to **long-wavelength, low-metric modes** in the Null zone ($\mathcal{M}_{\text{null}} < 0$) or in zones with very weak metric.

More precisely, the Null zone (all-negative metric) has $\Gamma_{\text{null}} > \kappa$ always — all Null zone modes are subcritical. This is consistent with the Null zone being the fastest-decaying zone (section 13.1). The subcritical regime is occupied by Null zone excitations and the short-lived A-state surface modes of other zones.

**Characteristic behavior:** In the subcritical regime:
- $R(t)$ decreases exponentially with rate $\bar{\Gamma} > 1/t_{\text{ref}}$
- The ICHTB is "transparent" to external drives — any organized structure that forms dissolves quickly
- The collapse trajectory passes through this regime during the early phase (before B-state amplitudes are reached)
- No persistent matter forms in this regime

---

## Regime 2: Critical ($S = 1$, the Boundary)

**Condition:** $\tau_{\text{eff}} = t_{\text{ref}} = 1/\kappa$ — the ICHTB decays at exactly the collapse rate.

**Dynamics:** The retained structure $R(t)$ decreases at exactly the rate that the collapse window advances. By $t = t_{\text{ref}}$:

$$
R(t_{\text{ref}}) = R_0 e^{-1/S} = R_0 e^{-1} \approx 0.368 R_0
$$

A fraction $e^{-1} \approx 37\%$ of the initial structure survives. The critical state is a **marginal survivor** — it just barely makes it through the collapse window with reduced but nonzero retained structure.

**Physical meaning:** The critical regime is the regime of **marginal persistence** — structures that are unstable enough to decay significantly but stable enough to leave a remnant. It is the boundary between ephemeral excitations (subcritical) and persistent matter (supercritical).

The critical condition $S = 1$ defines a curve in ICHTB parameter space — the **critical manifold** $\mathcal{C}$:

$$
\mathcal{C} = \left\{(\kappa, \gamma, D, \mathcal{M}^{ij}) : \bar{\Gamma}[\Phi_{\text{eq}}] = \kappa\right\}
$$

The critical manifold separates the parameter space into subcritical and supercritical regions. The CTS describes real physical systems near this manifold — the fine-tuning of nature's constants ($\hbar, e, m_e$, etc.) corresponds to the ICHTB parameters being tuned to lie in the supercritical region ($S > 1$) while remaining near the critical manifold (not excessively supercritical, which would prevent the collapse from exploring configuration space efficiently).

**Scale-free dynamics at criticality:** At $S = 1$, the ICHTB dynamics are scale-free — there is no preferred timescale (the decay time equals the reference time). Power-law correlations appear:

$$
C(r, t) = \langle\Phi^*(\mathbf{r}_0, t)\Phi(\mathbf{r}_0 + \mathbf{r}, t)\rangle \sim r^{-(d-2+\eta)} \quad \text{at criticality}
$$

This is the **critical scaling** of the ICHTB — identical in form to the scaling at a second-order phase transition (Wilson & Kogut 1974, *Physics Reports*, 12, 75). The ICHTB at criticality is a critical point of the field theory, with associated critical exponents $\eta$, $\nu$, $\beta$, etc.

---

## Regime 3: Supercritical ($S > 1$)

**Condition:** $\tau_{\text{eff}} > t_{\text{ref}}$ — the ICHTB decays slower than the collapse proceeds.

**Dynamics:** The retained structure at $t = t_{\text{ref}}$:

$$
R(t_{\text{ref}}) = R_0 e^{-1/S} \approx R_0\left(1 - \frac{1}{S}\right) \quad (\text{for }S \gg 1)
$$

For $S \gg 1$: nearly all of the initial structure survives. The ICHTB completes the collapse window with $R(t_{\text{ref}}) \approx R_0$.

**Sub-regimes within supercritical:**

*Weakly supercritical* ($1 < S \lesssim 10$): $R(t_{\text{ref}})/R_0 = e^{-1/S} \in [e^{-1}, e^{-0.1}] \approx [0.37, 0.90]$. Significant structure loss (10–63%) but the ICHTB persists. This is the regime of 1.B solitons and 2.B vortices in the early Memory zone phase.

*Moderately supercritical* ($10 < S \lesssim 100$): $R(t_{\text{ref}})/R_0 \in [e^{-0.1}, e^{-0.01}] \approx [0.90, 0.99]$. Very little structure loss (<10%). This is the regime of well-established 2.B vortex-skyrmion states with moderate inter-zone coupling.

*Strongly supercritical* ($S \gg 100$): $R(t_{\text{ref}})/R_0 \approx 1$. Effectively zero structure loss. This is the 3.B lock regime — the Hopfion decays at rate $\Gamma_{\text{lock}} \sim \kappa e^{-395}$, giving $S \sim e^{395}/(\kappa t_{\text{ref}}) = e^{395} \approx 10^{171}$. The ICHTB completes the collapse with all its structure intact, to $1 - 10^{-171}$ precision.

**Physical meaning:** The supercritical regime is the regime of **persistent matter formation**. ICHTB states in this regime survive the collapse window and become the organized structures of the post-collapse universe. The degree of supercriticality (the value of $S$) determines how much structure is retained and hence the stability of the resulting matter.

**The supercritical attractor:** For $S > 1$, the dynamics of $R(t)$ in the ICHTB (when the nonlinear gain is included) has an attractor at $R = R_B$ (the B-state). The approach to this attractor is:

$$
R(t) = R_B\left[1 - (1 - R_0/R_B)e^{-2\kappa t}\right]
$$

(from the logistic equation of section 14.1). The ICHTB doesn't just survive — it grows toward the B-state. The supercritical regime is self-reinforcing: the higher $S$ is, the faster the ICHTB grows toward the B-state, the faster the gain increases, driving $S$ to even larger values. This is the **supercritical runaway**: once $S > 1$ is established, the ICHTB bootstraps itself to the full B-state lock.

The supercritical runaway completes when $R \to R_B$ — the ICHTB has reached its B-state and the 3.B lock is established. At this point, $S \to \infty$ (by the zero decay rate of the B-state), and the ICHTB is in its final, stable configuration.

---

## The S-Landscape

The three regimes can be visualized as a **landscape** in ICHTB parameter space. The landscape has:
- A **valley** (subcritical region, $S < 1$): low-$R$, high-$\Gamma$ states that funnel toward the vacuum
- A **ridge** (critical manifold $S = 1$): the boundary between dissolution and persistence
- A **plateau** (supercritical region, $S > 1$): high-$R$, low-$\Gamma$ states that funnel toward the B-state lock

The collapse trajectory begins in the valley (pre-ICHTB, $\Phi \approx 0$), climbs toward the ridge (driven by external excitation), crosses the ridge (the emergence event), and self-propels up the plateau (supercritical runaway) to reach the B-state peak (3.B lock).

The **emergence event** — the ICHTB's transition from subcritical to supercritical — is the crossing of the critical manifold. It corresponds to $S$ passing through 1, and it is the moment at which the collapse trajectory commits to forming persistent matter. Before the emergence: the trajectory is reversible (the system can slide back into the valley). After the emergence: the trajectory is irreversible (the supercritical runaway carries it inexorably to the B-state lock).

This irreversibility is the ICHTB's version of **symmetry breaking**: the collapse crosses a separatrix (the critical manifold) and commits to one of the many possible B-state configurations (one topological sector, characterized by $H$). The Selection Number $S$ is the order parameter for this symmetry-breaking transition.

