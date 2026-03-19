# 16.3 The Objecthood Threshold

## Defining Objecthood Precisely

An **object** in the ICHTB framework is a configuration that satisfies three simultaneous conditions:

1. **Persistence:** $S^* > 1$ — the corrected Selection Number exceeds 1, guaranteeing that the configuration retains more structure than it loses over the reference timescale.

2. **Closure:** $T_{\text{obj}} = 1$ — the Apex zone is fully phase-locked, the Hopf loop is closed, and the Hopf invariant $H$ has reached its quantized integer value.

3. **Stability:** The Lyapunov function $R = \mathcal{F} - \mathcal{F}_{\text{lock}}$ satisfies $R < R_{\text{threshold}}$ — the configuration is in the basin of attraction of the 3.B lock (within a threshold distance of the lock in free energy space).

The **objecthood threshold** is the boundary in ICHTB configuration space where all three conditions are simultaneously satisfied for the first time. Crossing the objecthood threshold = achieving objecthood = completing the proto-particle.

---

## The Three Conditions as Nested Sets

The three conditions define nested sets in configuration space:

$$
\{\text{objects}\} = \{S^* > 1\} \cap \{T_{\text{obj}} = 1\} \cap \{R < R_{\text{threshold}}\}
$$

These sets are:

- $\{S^* > 1\}$: the "persistence region" — a open set bounded by the persistence horizon $\{S^* = 1\}$. All supercritical configurations.
- $\{T_{\text{obj}} = 1\}$: the "closure set" — a closed set (a manifold in configuration space) where the Hopf invariant is quantized. This is a **discrete** set — it consists of isolated manifolds corresponding to $H = 0, \pm 1, \pm 2, \ldots$. The $H = \pm 1$ manifolds are the objecthood manifolds (for fundamental objects).
- $\{R < R_{\text{threshold}}\}$: the "stability ball" — an open ball around the 3.B lock in free energy space, within which the drift points toward the lock.

The objecthood threshold corresponds to the boundary of $\{$objects$\}$:

$$
\partial\{\text{objects}\} = \{S^* = 1\} \cup \{T_{\text{obj}} = 1^-\} \cup \{R = R_{\text{threshold}}\}
$$

where $T_{\text{obj}} = 1^-$ means the topology factor approaching 1 from below (the last instant before quantization).

The most geometrically significant boundary is $\{T_{\text{obj}} = 1^-\}$: this is the **topological threshold** — the manifold in configuration space where the Hopf invariant is about to quantize. Crossing this manifold is the objecthood transition.

---

## The Objecthood Transition: A Topological Phase Transition

The objecthood transition (from $T_{\text{obj}} < 1$ to $T_{\text{obj}} = 1$) is a **topological phase transition** — a change in the topological character of the configuration that cannot be achieved by a smooth, continuous deformation.

Specifically: the Hopf invariant $H$ is an integer-valued topological invariant — it can only change by $\pm 1$ (or multiples thereof) via a discontinuous process (a topological defect nucleation at a membrane). The continuous growth of $T_{\text{obj}}$ from 0 to 1 is not itself discontinuous — it is the smooth growth of the Apex zone coherence. But the **quantization** of $H$ at $T_{\text{obj}} = 1$ is discontinuous: $H$ jumps from a continuous (non-integer) pre-quantization value to a discrete integer value.

This is analogous to the quantization of magnetic flux in a type-II superconductor: the flux grows continuously as the magnetic field is applied, but quantizes in units of $\Phi_0 = h/(2e)$ when the coherence is fully established (Abrikosov 1957). In the ICHTB, $H$ grows continuously during the Apex lock development and quantizes in units of 1 when $T_{\text{obj}} = 1$.

**Observable signature:** The objecthood transition is associated with a sudden increase in topological stability — the ICHTB becomes immune to perturbations that would otherwise unwrap the phase. Before the transition ($T_{\text{obj}} < 1$): phase perturbations can deform the Hopf loop and reduce $H$ continuously. After the transition ($T_{\text{obj}} = 1$): phase perturbations cannot change $H$ — they are absorbed into the collective motion of the locked configuration without changing the topology.

---

## The Objecthood Threshold in Parameter Space

The objecthood threshold is a **surface in ICHTB parameter space** — the set of ICHTB parameters $\{D, T_{\text{eff}}, \kappa, \gamma, \ldots\}$ for which the three objecthood conditions are marginally satisfied.

In the $(S^*, T_{\text{obj}})$ plane (a 2D projection of the full parameter space):

```
T_obj
  1 |────────────────── objecthood manifold ──────────────────
    |    proto-object         │           OBJECT
    |    (all zones OK,       │         (S* > 1,
    |     Hopf not           │          Hopf closed,
    |     quantized)          │          stable)
0.5 |                         │
    |         subcritical     │         eligibility-locked
    |         + developing    │         but S* < 1
    |                         │
  0 |_________________________│_______________________________→ S*
    0                         1                     ∞
                         persistence
                           horizon
```

The objecthood region is the **upper-right quadrant**: $S^* > 1$ AND $T_{\text{obj}} = 1$ (the top edge of the diagram, $T_{\text{obj}} = 1$, right of the persistence horizon).

Configurations to the left of $S^* = 1$: subcritical, dissolving. No objects here.
Configurations above $T_{\text{obj}} = 1$ but left of $S^* = 1$: proto-objects with closed topology but insufficient persistence — they have the right shape but not enough energy to survive. They achieve topological closure momentarily but then dissolve.
Configurations right of $S^* = 1$ but with $T_{\text{obj}} < 1$: supercritical proto-objects — persistent but not yet topologically closed. They are the "waiting room" for objecthood.
Configurations in the upper-right quadrant (AND $R < R_{\text{threshold}}$): **objects**.

---

## Minimum Conditions for Objecthood

What is the minimum set of ICHTB conditions that must be satisfied for objecthood to be achievable?

**Necessary conditions:**

1. $R_{\text{ICHTB}} > \xi$ (ICHTB must be large enough to contain at least one coherence length — otherwise there is no room for a vortex)
2. $T_{\text{eff}} < T_{KT}$ (effective temperature below the KT transition — otherwise Memory zone vortices spontaneously annihilate faster than they form)
3. $\kappa < \gamma\Phi_B^2/2$ (nonlinear gain must exceed linear loss — the basic supercriticality condition)
4. $t_{\text{available}} > t_{\text{lock}} = 3/\kappa + t_4$ (sufficient time for the six-fan lock)
5. $\mathcal{E}_{\text{shell}} = 1$ (boundary conditions not hostile)

**Sufficient conditions:** The necessary conditions plus:

6. The initial amplitude $\Phi_0 > \Phi_{c,\min} = \epsilon_c\Phi_B$ (Core zone activation)
7. The initial phase gradient $|\partial_x\arg\Phi|_0 > k_{\min} = 1/L_f$ (Forward zone structure)

When conditions 1–7 are all satisfied, the ICHTB will achieve objecthood (with probability approaching 1 for strongly supercritical configurations). The six conditions collapse to a single compound inequality — the **objecthood criterion**:

$$
S^* = \mathcal{E}_{\text{shell}}\cdot\mathcal{E}\cdot D\cdot T_{\text{obj}}\cdot S > 1 \quad \text{with } T_{\text{obj}} \to 1 \text{ as } t \to t_{\text{lock}}
$$

The objecthood criterion is therefore the corrected persistence condition evaluated at the moment of Hopf quantization.

---

## When the Box "Locks" a Configuration Permanently

The final element of the chapter overview: "when the box locks a configuration permanently." This refers to the B-state lock — the moment when the ICHTB's internal dynamics irreversibly commit to the 3.B configuration.

The lock is **permanent** in the sense that the free energy cost of unlocking exceeds the thermal energy available:

$$
\Delta\mathcal{F}_{\text{lock}} \gg T_{\text{eff}} \quad \text{(lock is permanent)}
$$

where $\Delta\mathcal{F}_{\text{lock}}$ is the free energy difference between the 3.B lock and the next saddle point (the energy barrier for unlocking). The lock becomes permanent when:

$$
\Delta\mathcal{F}_{\text{lock}} = \sigma_{\text{apex}}\mathcal{A}_{\text{apex}} + E_{\text{Hopf}} \sim \Phi_{B,\text{apex}}^2\xi_a^2 + D_a\Phi_{B,\text{apex}}^2 L_{\text{Hopf}} \gg T_{\text{eff}}
$$

This is the condition that the Apex membrane tension plus the Hopf loop energy exceeds the thermal fluctuations. In the strongly supercritical regime ($\Phi_{B,\text{apex}} \gg \Phi_{c,\text{apex}}$): the lock energy grows as $\Phi_B^2$, well above $T_{\text{eff}}$ — the lock is permanently stable.

The permanent lock signals the completion of the objecthood transition: the ICHTB has "decided" that it is an object. The topological charge $H$ is now conserved exactly (up to exponentially suppressed quantum tunneling), and the ICHTB carries a definite identity — a definite set of quantum numbers (spin, charge, mass) encoded in its zone configuration.

