# 15.4 The Corrected Persistence Condition

## Beyond $S > 1$: The Full Condition

Sections 15.1–15.3 introduced three additional elements beyond the basic $S > 1$ condition:

1. **Eligibility** $\mathcal{E}$: all zone admissibility conditions satisfied (section 15.1)
2. **Drift** direction: the ICHTB must be drifting toward the B-state (supercritical drift), not trapped in metastable configurations (section 15.2)
3. **Lock probability** $\mathcal{P}_{\text{lock}}$: all six fan steps must be satisfied in the correct order (section 15.3)

These three elements combine with the basic Selection Number $S$ to give the **corrected persistence condition** — a comprehensive criterion for successful matter formation.

Additionally, the chapter title mentions two factors not yet explicitly defined: the **shell eligibility** $\mathcal{E}_{\text{shell}}$ and an object-level temporal factor $T_{\text{obj}}$. These are introduced here.

---

## The Shell Eligibility Factor $\mathcal{E}_{\text{shell}}$

The **shell** refers to the external boundary of the ICHTB — the zone membranes that separate the ICHTB interior from the external environment (the surrounding collapse field or the pre-collapse medium). The shell eligibility $\mathcal{E}_{\text{shell}}$ measures whether the ICHTB boundary conditions are compatible with the 3.B lock formation.

Shell admissibility requires:

1. **Closed shell condition:** The outermost zone membranes must be sufficiently reflective to prevent the field from leaking out before the lock forms. Formally:

$$
T_{\text{shell}} \leq T_{\text{shell,max}} = \frac{\xi^2}{R_{\text{ICHTB}}^2}
$$

where $T_{\text{shell}}$ is the shell membrane transmission coefficient and $R_{\text{ICHTB}}$ is the ICHTB outer radius. This condition ensures the field is "contained" within the ICHTB for at least one coherence time $1/\kappa$.

2. **Non-destructive environment:** The external field (outside the ICHTB shell) must not be strongly absorptive — it must not drain the ICHTB faster than the internal dynamics can replenish it. Formally:

$$
\Gamma_{\text{env}} \leq \bar{\Gamma}_{\text{int}}
$$

where $\Gamma_{\text{env}}$ is the external absorption rate and $\bar{\Gamma}_{\text{int}}$ is the internal effective decay rate. If $\Gamma_{\text{env}} > \bar{\Gamma}_{\text{int}}$, the external environment drains the ICHTB faster than its internal B-state dynamics can maintain it.

3. **Shell phase coherence:** The external field at the ICHTB boundary must not imprint a strongly incoherent phase pattern that disrupts the internal zone alignment. The shell phase coherence condition:

$$
|\psi_{\text{shell}}| = \left|\langle e^{i\omega_B t}\Phi\rangle_{\partial\text{ICHTB}}\right| > \psi_{\text{shell,min}}
$$

The shell eligibility factor:

$$
\mathcal{E}_{\text{shell}} = \Theta(T_{\text{shell,max}} - T_{\text{shell}}) \cdot \Theta(\bar{\Gamma}_{\text{int}} - \Gamma_{\text{env}}) \cdot \Theta(|\psi_{\text{shell}}| - \psi_{\text{shell,min}})
$$

(product of three step-function conditions). $\mathcal{E}_{\text{shell}} = 1$ when all three shell conditions are satisfied; $\mathcal{E}_{\text{shell}} = 0$ when any fails.

---

## The Object Temporal Factor $T_{\text{obj}}$

The **object temporal factor** $T_{\text{obj}}$ accounts for the timescale mismatch between the ICHTB's internal dynamics (governed by $1/\kappa$) and the external collapse process (governed by $t_{\text{ref}}$). Specifically, $T_{\text{obj}}$ measures whether the ICHTB has had enough time to develop its internal organization before the collapse window closes.

Define:

$$
T_{\text{obj}} = \min\!\left(1, \frac{t_{\text{available}}}{t_{\text{lock}}}\right)
$$

where $t_{\text{available}} = t_{\text{ref}} - t_{\text{current}}$ is the time remaining in the collapse window and $t_{\text{lock}} \approx 3/\kappa + t_4$ (the total lock time from section 15.3). 

$T_{\text{obj}} = 1$ when $t_{\text{available}} \geq t_{\text{lock}}$ — the ICHTB has enough time to complete the lock. $T_{\text{obj}} < 1$ when $t_{\text{available}} < t_{\text{lock}}$ — the collapse window will close before the lock is complete. $T_{\text{obj}} \propto t_{\text{available}}/t_{\text{lock}}$ in the latter case — a smooth interpolation.

The factor $T_{\text{obj}}$ captures the **race condition** between the ICHTB's development and the closing of the collapse window. An ICHTB that starts forming its vortex (step 4) too late will fail even if $S \gg 1$ and $\mathcal{E}_{\text{shell}} = 1$.

---

## The Corrected Persistence Condition

Combining all factors, the **corrected persistence condition** is:

$$
S^* = \mathcal{E}_{\text{shell}} \cdot \mathcal{E} \cdot D \cdot T_{\text{obj}} \cdot \frac{R}{\dot{R}\,t_{\text{ref}}} > 1
$$

where:
- $\mathcal{E}_{\text{shell}} \in \{0, 1\}$: shell eligibility (boundary conditions admit lock formation)
- $\mathcal{E} \in \{0, 1\}$: internal eligibility (all zone admissibility conditions satisfied)
- $D \in [0, 1]$: drift alignment factor (fraction of drift pointing toward B-state, not trapped in metastable wells)
- $T_{\text{obj}} \in [0, 1]$: temporal factor (sufficient time remaining for lock formation)
- $R/(\dot{R}t_{\text{ref}}) = S$: the basic Selection Number

The **corrected Selection Number** $S^* \leq S$ is always less than or equal to the basic $S$. The additional factors $\mathcal{E}_{\text{shell}}$, $\mathcal{E}$, $D$, $T_{\text{obj}}$ all reduce $S^*$ below $S$ when conditions are not fully met. Only when all conditions are simultaneously satisfied ($\mathcal{E}_{\text{shell}} = \mathcal{E} = 1$, $D = 1$, $T_{\text{obj}} = 1$) does $S^* = S$.

---

## The Drift Factor D in Detail

The drift alignment factor $D$ quantifies how well the ICHTB's instantaneous drift direction is aligned with the direction toward the B-state lock, accounting for metastable trapping:

$$
D = \frac{\mathbf{v}[\Phi]\cdot(\Phi_{\text{lock}} - \Phi)}{|\mathbf{v}[\Phi]||\Phi_{\text{lock}} - \Phi|}
$$

(the cosine of the angle between the current drift direction and the direct path to the 3.B lock $\Phi_{\text{lock}}$). $D = 1$: the ICHTB is drifting directly toward the lock. $D = 0$: the drift is perpendicular to the lock direction (sidewise motion, neither approaching nor receding). $D = -1$: the drift is pointing directly away from the lock (actively anti-drifting).

The drift factor decomposes into zone contributions:

$$
D = \frac{\sum_\alpha D_\alpha R_\alpha}{\sum_\alpha R_\alpha}
$$

where $D_\alpha$ is the zone-specific drift alignment. For zones in their supercritical state (drifting toward B-state): $D_\alpha > 0$. For zones trapped in metastable states (not drifting toward global B-state): $D_\alpha \approx 0$. For the Null zone (always drifting toward vacuum): $D_{\text{null}} < 0$.

In the fully locked ICHTB: $D = 1$ (all zones drifting exactly toward the lock, which is already reached). In the subcritical ICHTB: $D < 0$ (drifting away). The corrected $S^*$ with drift factor:

$$
S^* = D \cdot S \quad (\text{simplified form when }\mathcal{E} = \mathcal{E}_{\text{shell}} = T_{\text{obj}} = 1)
$$

The condition $S^* > 1$ becomes $D \cdot S > 1$, or equivalently $D > 1/S$: the drift must be sufficiently aligned toward the lock for the ICHTB to converge before $S$ decays to 1.

---

## Physical Interpretation of $S^*$

The corrected persistence condition $S^* > 1$ can be read as a **comprehensive viability criterion** for the ICHTB:

- $\mathcal{E}_{\text{shell}} = 1$: the environment is not hostile (the ICHTB is not in a strongly absorbing medium)
- $\mathcal{E} = 1$: the internal structure is correctly organized (all zone excitations are of the right type)
- $D > 0$: the dynamics are moving in the right direction (toward the lock, not away)
- $T_{\text{obj}} = 1$: there is sufficient time (the collapse window has not already closed)
- $S > 1$: the retained structure exceeds the loss rate times the reference time

When all five conditions hold simultaneously, the ICHTB is fully eligible for 3.B lock formation and persistent matter production. When any condition fails, matter formation is either impossible ($\mathcal{E}_{\text{shell}} = 0$ or $\mathcal{E} = 0$, hard failures) or impaired ($D < 1$ or $T_{\text{obj}} < 1$, soft failures that reduce $S^*$).

The corrected persistence condition is the central result of Chapter 15 — and of Part III as a whole. It distills the entire persistence mechanics framework into a single inequality $S^* > 1$, which encodes the ICHTB's zone geometry (through $S = R/(\dot{R}t_{\text{ref}})$), its internal organization (through $\mathcal{E}$), its boundary conditions (through $\mathcal{E}_{\text{shell}}$), its dynamical direction (through $D$), and its temporal position in the collapse process (through $T_{\text{obj}}$).

Part IV (Chapters 17–20) uses this corrected condition to derive the Survival Map — the mapping from ICHTB parameter space to the regions where $S^* > 1$ (matter-forming) and $S^* < 1$ (matter-dissolving). The Survival Map is the ICHTB's version of the phase diagram: the complete classification of all possible ICHTB configurations by their matter-formation outcome.

