# 15.3 Six-Fan Lock Logic in Zone Terms

## The Six-Fan Structure

The "six-fan lock" is the geometric structure that describes the final stage of ICHTB convergence to the 3.B lock. The term refers to the six positive zones of the ICHTB (+X, +Y, +Z, and the three others in the ICHTB's cuboctahedral geometry) fanning out from the Core (+0) and converging, via the three negative zones (−X, −Y, −Z), toward the Apex lock (+Z). The six-fan is the field-theoretic analog of a funnel: six wide entry channels (one per positive zone) converging through six narrow channels (the zone-to-zone transitions) to a single exit point (the 3.B lock in the Apex zone).

More precisely, the six-fan lock logic refers to the **six-step logical sequence** that must be satisfied for the ICHTB to achieve a 3.B lock, expressed in terms of the zone admissibility conditions of section 15.1:

**Step 1 (Core fan):** Core zone admissibility $\mathcal{A}_{\text{core}} = 1$. The collapse has reached the ICHTB center with sufficient amplitude.

**Step 2 (Forward fan):** Forward zone admissibility $\mathcal{A}_{\text{fwd}} = 1$. The field has developed propagating structure along +X.

**Step 3 (Expansion fan):** Expansion zone admissibility $\mathcal{A}_{\text{exp}} = 1$. The 2D bloom has spread to at least $r_{\min} = \xi_\perp$.

**Step 4 (Memory fan):** Memory zone admissibility $\mathcal{A}_{\text{mem}} = 1$. At least one vortex (winding number $\pm1$) is present in the Memory zone.

**Step 5 (Apex fan):** Apex zone admissibility $\mathcal{A}_{\text{apex}} = 1$. The Apex zone has begun phase-locking at $\omega_B$.

**Step 6 (Compression fan):** Compression zone admissibility $\mathcal{A}_{\text{comp}} = 1$. The Compression zone has developed a soliton, providing the mass component.

The **lock** occurs when all six steps are simultaneously satisfied: $\mathcal{E} = \prod_{\alpha=1}^6\mathcal{A}_\alpha = 1$.

---

## The Logic Gates

Each fan step is a logic gate that the ICHTB must pass through. The gates are **ordered but not independent**:

- Steps 1 and 2 are prerequisites for Steps 3 and 4 (the Core must be active before the outer zones can organize)
- Steps 3 and 4 are prerequisites for Step 5 (the Apex phase lock requires both a spatial pattern to lock and a temporal oscillation to synchronize to)
- Step 5 is a prerequisite for Step 6 (the Compression soliton can only form once the Apex lock provides the temporal coherence that sets the soliton frequency)

The directed dependency graph of the six fan steps:

```
Step 1 (Core) ──→ Step 2 (Forward) ──→ Step 6 (Compression)
     │                                         ↑
     └──────────→ Step 3 (Expansion) ──→ Step 4 (Memory) ──→ Step 5 (Apex) ──┘
```

Steps 2 and 3 can proceed in parallel (both require Core activation but not each other). Steps 4 and 5 are sequential. The longest path through the dependency graph is the **critical path** — the sequence of steps that takes the most time and hence determines the total time to lock:

$$
t_{\text{lock}} = \max\left(t_1 + t_4 + t_5 + t_6, \quad t_1 + t_2 + t_6\right)
$$

where $t_i$ is the time to complete step $i$. For typical ICHTB parameters, the Memory zone vortex formation (step 4) is the slowest step: $t_4 \sim T_{KT}^{-1}$ (the time to nucleate a vortex — set by the KT transition temperature, which requires the Memory zone to cool below $T_{KT}$). The critical path is therefore $1 \to 3 \to 4 \to 5 \to 6$.

---

## Zone-Specific Gate Timing

**Step 1 timing (Core activation):**

The Core activates when $|\Phi(0)| > \Phi_{c,\min} = \epsilon_c\Phi_B$. For an incoming excitation of amplitude $\Phi_0$ at the ICHTB boundary, the Core amplitude grows as:

$$
|\Phi_{\text{core}}(t)| \approx \Phi_0\exp\!\left[-(\kappa - \gamma\Phi_{\text{core}}^2)t\right]
$$

(logistic growth from initial $\Phi_0$ to $\Phi_B$). The time to reach $\Phi_{c,\min} = \epsilon_c\Phi_B$:

$$
t_1 = \frac{1}{2\kappa}\ln\!\left(\frac{\epsilon_c\Phi_B}{\Phi_0}\right) \approx \frac{1}{2\kappa}\ln\!\left(\frac{\epsilon_c}{\Phi_0/\Phi_B}\right)
$$

For $\Phi_0 = 0.1\Phi_B$ (10% of B-state amplitude) and $\epsilon_c = 0.1$: $t_1 = 0$. For $\Phi_0 = 0.01\Phi_B$: $t_1 \approx \ln(10)/(2\kappa) \approx 1.15/\kappa$. Core activation is fast.

**Step 4 timing (Memory vortex formation):**

The Memory zone vortex forms via the Kibble-Zurek mechanism (Kibble 1976, Zurek 1985, 1996): as the Memory zone cools through the KT transition temperature $T_{KT}$, vortices spontaneously nucleate in the field phase. The vortex nucleation time:

$$
t_4 \sim \frac{1}{\Gamma_{\text{nucleation}}} = \tau_0\exp\!\left(\frac{E_{\text{vortex}}}{T_{\text{eff}}}\right)
$$

For $T_{\text{eff}} \lesssim E_{\text{vortex}} \sim D_m\Phi_B^2\ln(R_{\text{ICHTB}}/\xi)$: $t_4 \gg \tau_0$ — vortex nucleation is slow (nucleation requires overcoming the vortex energy barrier). For $T_{\text{eff}} \gg E_{\text{vortex}}$ (above KT temperature): vortices nucleate instantly.

The Kibble-Zurek scaling: in a quench from above $T_{KT}$ to below, the vortex nucleation time scales as $t_4 \propto |\dot{T}/T_{KT}|^{-\nu}$ where $\nu$ is the KT correlation length exponent ($\nu = 1/2$ for the 2D XY model). For a slow quench ($|\dot{T}|$ small): $t_4$ is long; for a rapid quench: $t_4$ is short (many vortices nucleate simultaneously).

**Step 5 timing (Apex phase lock):**

As derived in section 13.2, the Apex synchronization time:

$$
t_5 = \tau_{\text{sync}} \approx \frac{1}{\langle E_{\text{bind}}\rangle - \Delta\omega}
$$

For $\langle E_{\text{bind}}\rangle = D_a\Phi_B^2$ and $\Delta\omega = \kappa$: $t_5 \approx 1/(D_a\Phi_B^2 - \kappa) \approx 1/\kappa$ (for $D_a\Phi_B^2 \gg \kappa$). The Apex lock establishes quickly once the Memory vortex is formed (step 4 is the bottleneck, not step 5).

**Step 6 timing (Compression soliton):**

The Compression soliton forms when the field amplitude in the Compression zone reaches the soliton threshold (section 8.2):

$$
t_6 \approx \frac{1}{2\kappa}\ln\!\left(\frac{\Phi_{s,\text{thresh}}}{\Phi_{\text{comp}}(0)}\right)
$$

Similar to the Core activation time but for the soliton amplitude threshold $\Phi_{s,\text{thresh}} \sim \Phi_B/\sqrt{2}$ (the 1D kink amplitude, section 8.3). For initial Compression zone amplitude $\Phi_{\text{comp}}(0) \sim 0.1\Phi_B$: $t_6 \approx \ln(\sqrt{2}/0.1)/(2\kappa) \approx 1/(2\kappa)$. Compression soliton formation is fast.

**Total lock time:**

$$
t_{\text{lock}} = t_1 + t_3 + t_4 + t_5 + t_6 \approx \frac{1}{2\kappa} + \frac{1}{\kappa} + t_4 + \frac{1}{\kappa} + \frac{1}{2\kappa} = 3/\kappa + t_4
$$

The lock time is dominated by the vortex nucleation time $t_4$. For a well-driven ICHTB ($T_{\text{eff}} \gg E_{\text{vortex}}$): $t_4 \approx 0$ and $t_{\text{lock}} \approx 3/\kappa$ — the lock forms in about three coherence times. For a slowly driven ICHTB ($T_{\text{eff}} \lesssim E_{\text{vortex}}$): $t_4 \gg 1/\kappa$ and the lock time is dominated by vortex nucleation.

---

## The Six-Fan as a Decision Tree

The six-fan lock logic can be represented as a **decision tree**: at each fan step, the ICHTB either passes the gate (condition satisfied, advance to next step) or fails (condition not satisfied, return to earlier step and wait).

The decision tree probabilities (for a given ICHTB parameter set):

$$
P(\text{lock}) = P(\mathcal{A}_1)P(\mathcal{A}_3|\mathcal{A}_1)P(\mathcal{A}_4|\mathcal{A}_1, \mathcal{A}_3)P(\mathcal{A}_5|\mathcal{A}_4)P(\mathcal{A}_6|\mathcal{A}_5) \times P(\mathcal{A}_2|\mathcal{A}_1)
$$

(conditioned probabilities reflecting the dependency structure). The overall lock probability:

$$
P(\text{lock}) = \prod_\alpha P(\mathcal{A}_\alpha|\text{predecessors}) \equiv \mathcal{P}_{\text{lock}}
$$

This is a product of probabilities, all less than or equal to 1. For an ICHTB with all conditions strongly satisfied ($T_{\text{eff}} \gg$ all thresholds): $\mathcal{P}_{\text{lock}} \approx 1$. For a marginal ICHTB: $\mathcal{P}_{\text{lock}} \ll 1$, and only a small fraction of trials result in a 3.B lock.

The Selection Number $S$ and the lock probability $\mathcal{P}_{\text{lock}}$ are related but distinct: $S$ measures how strongly the ICHTB persists (how much structure survives), while $\mathcal{P}_{\text{lock}}$ measures how likely it is that the ICHTB achieves the correct configuration to lock. An ICHTB can be strongly supercritical ($S \gg 1$) but have low $\mathcal{P}_{\text{lock}}$ (if it is likely to be trapped in a metastable vortex-pair state, for example).

