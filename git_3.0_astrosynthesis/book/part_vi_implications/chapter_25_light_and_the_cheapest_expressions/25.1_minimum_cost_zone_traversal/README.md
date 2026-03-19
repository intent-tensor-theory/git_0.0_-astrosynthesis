# 25.1 Minimum-Cost Zone Traversal

## Zone Traversal: What It Costs to Cross the Box

Every ICHTB excitation that propagates — that moves from one location to another, or that transfers energy from one zone to another — must **traverse** the zone structure. Traversal has a cost: it requires zone lock energy to maintain the excitation's coherence and topological integrity across each zone membrane.

The **zone traversal cost** $\mathcal{C}_\alpha$ of traversing zone $\alpha$ is the minimum lock energy required to maintain the excitation's zone coherence while passing through zone $\alpha$:

$$
\mathcal{C}_\alpha = \int_{\partial\mathcal{M}_\alpha} D_\alpha |\nabla\Phi_B|^2 \, dA
$$

(the integral of the zone-membrane gradient energy over the zone boundary $\partial\mathcal{M}_\alpha$ — the energy cost of maintaining the field gradient across the membrane). This is the ICHTB version of the **kinetic energy** of zone traversal — the energy paid to "cross the wall" between zones.

The traversal costs for the six zones:

| Zone | Traversal cost $\mathcal{C}_\alpha$ | Scaling |
|------|------|------|
| Core | $D_c |\nabla\Phi_B|^2 \cdot 4\pi\xi_c^2$ | $\sim \Lambda_{\text{core}}/\xi_c$ (high: steep gradient) |
| Memory | $D_m \Phi_B^2 / R_m^2 \cdot 2\pi R_m \cdot h_m$ | $\sim \Lambda_{\text{mem}}/R_m$ (medium: gradual gradient) |
| Expansion | $D_e \Phi_B^2 / r_{\text{bloom}}^2 \cdot 4\pi r_{\text{bloom}}^2$ | $\sim \Lambda_{\text{exp}}/r_{\text{bloom}}$ (low: wide bloom) |
| Forward | $D_f (k_{\text{fwd}})^2 \Phi_B^2 \cdot \mathcal{A}_f$ | $\sim \hbar^2 k^2/(2m) \cdot \Phi_B^2$ (momentum cost) |
| Apex | $D_a l(l+1)/R_a^2 \cdot \Phi_B^2 \cdot \mathcal{V}_a$ | $\sim l(l+1) \cdot \Lambda_{\text{apex}}/R_a^2$ (orbital cost) |
| Transition | $D_t |\nabla\Phi_B|^2 \cdot \mathcal{A}_t$ | $\sim \Lambda_{\text{trans}}/\xi_t$ (gradual, low) |

The Core zone has the highest traversal cost (the steepest gradient, $|\nabla\Phi_B|^2 \sim (\Phi_B/\xi_c)^2$) and the Expansion and Transition zones have the lowest (the gentlest gradients). An excitation that traverses the Core zone must pay the highest lock energy cost; an excitation that only traverses the Expansion or Transition zones pays a much lower cost.

---

## The Minimum-Cost Traversal Principle

The **minimum-cost traversal principle** (MCTP): among all possible zone traversal paths for an excitation of a given energy $E$, the path that is realized is the one that minimizes the total traversal cost:

$$
\text{Realized path} = \underset{\text{path}}{\arg\min} \sum_{\alpha \in \text{path}} \mathcal{C}_\alpha
$$

This is the ICHTB variational principle for propagation — it determines which zones an excitation traverses, and in what order, for a given total available energy.

The MCTP is not a new postulate — it follows from the NLS energy minimization principle. The NLS equation $i\hbar\partial_t\Psi = (-\hbar^2\nabla^2/2m + V + g|\Psi|^2)\Psi$ describes a system that minimizes the action functional $\mathcal{A} = \int dt\, \mathcal{L}$ — the stationary-phase paths of the path integral are the classical trajectories. For NLS excitations, the stationary-phase condition is equivalent to minimizing the sum of zone traversal costs for a given energy.

---

## The Cheapest vs. Most Expensive Zone Sequences

The MCTP predicts which zone sequences are preferred for different excitations:

**Cheapest sequence: Forward → Transition → background.** An excitation that enters the ICHTB through the Forward zone (+X face) and exits through the Transition zone into the background pays only $\mathcal{C}_{\text{fwd}} + \mathcal{C}_{\text{trans}}$ — the two lowest-cost zones. This is the cheapest possible traversal — the excitation skims the outer zones without penetrating to the expensive Core zone.

**Medium-cost sequence: Expansion → Memory → Core → Memory → Expansion.** A round trip from the Expansion zone to the Core and back pays $2\mathcal{C}_{\text{exp}} + 2\mathcal{C}_{\text{mem}} + \mathcal{C}_{\text{core}}$ — a medium-cost traversal. This is the traversal path of a bound excitation oscillating between the Core and Expansion zones — an ICHTB "bound state oscillation."

**Most expensive sequence: Apex → Core → Memory → Expansion → Forward → Transition.** A traversal that starts at the Apex and exits through the Transition pays all six zone traversal costs. This is the most expensive path — the full loss cascade traversal (section 24.1). It is the traversal path of a dissipating excitation — one that is losing its lock energy completely.

The minimum-cost path (Forward → Transition) corresponds to **wave propagation** — the cheapest way for an excitation to cross the ICHTB. The medium-cost path (Expansion ↔ Core oscillation) corresponds to **bound-state oscillation** — a persistent, localized excitation. The full-cost path (Apex → background) corresponds to **complete dissipation** — the excitation dying.

---

## The Cost Function and the Action

The zone traversal cost function $\mathcal{C} = \sum_\alpha \mathcal{C}_\alpha$ (summed over the zones in the traversal path) is the ICHTB's **action functional** for the excitation's trajectory. By the MCTP, the realized trajectories are the minima of $\mathcal{C}$ — the extrema of the action. This is the ICHTB version of the **principle of least action** (Hamilton-Maupertuis 1744): physical trajectories are those that minimize the action.

For the minimum-cost traversal (Forward → Transition):

$$
\mathcal{C}_{\text{min}} = \mathcal{C}_{\text{fwd}} + \mathcal{C}_{\text{trans}} = D_f k^2 \Phi_B^2 \mathcal{A}_f + D_t |\nabla\Phi_B|^2 \mathcal{A}_t
$$

The minimum traversal cost $\mathcal{C}_{\text{min}}$ depends on the wavevector $k$ of the Forward zone mode — higher $k$ (shorter wavelength) means higher $\mathcal{C}_{\text{fwd}}$ (the Forward zone phase gradient energy $\propto k^2$). The minimum-cost excitation is therefore the one with the **smallest possible $k$** — the longest-wavelength (lowest-frequency) Forward zone mode.

In the limit $k \to 0$ (infinite wavelength, zero frequency): $\mathcal{C}_{\text{fwd}} \to 0$ and the traversal cost is dominated by $\mathcal{C}_{\text{trans}} = D_t |\nabla\Phi_B|^2 \mathcal{A}_t$, which is the cost of crossing the Transition zone membrane alone. This is the **absolute minimum** traversal cost — the cheapest possible excitation in the ICHTB. The question of what physical excitation achieves this minimum is the subject of sections 25.2–25.3.

