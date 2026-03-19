# 22.3 Composite Thresholds in ICHTB Terms

## Composite Thresholds: The Energy Barrier to Multi-Zone Occupation

A **composite threshold** is the minimum total energy (or minimum zone configuration energy) that must be reached for a multi-charge composite to form and persist. Below the threshold, the charges remain separated (individual single-charge excitations). Above the threshold, the composite forms and may become a persistent Region VI configuration.

In standard quantum mechanics, the composite threshold is the **binding threshold**: the total energy must be below the continuum threshold (the energy of the constituents at infinite separation). In ICHTB terms, the composite threshold has two components:

1. **Activation barrier** $\Lambda_{\text{barrier}}$: the zone energy cost required to bring the individual charges close enough for their zones to overlap (the ICHTB analog of the Coulomb barrier)
2. **Composite lock energy** $\Lambda_{\text{comp}}$: the zone energy gained once the charges are close enough to form the composite (the ICHTB analog of the binding energy)

The composite forms and persists if and only if $\Lambda_{\text{comp}} > \Lambda_{\text{barrier}}$ (the composite gains more from zone sharing than it costs to overcome the barrier). The composite threshold is the condition $\Lambda_{\text{comp}} = \Lambda_{\text{barrier}}$ — the boundary between the bound (composite) and unbound (separated) phases.

---

## Zone Activation Barrier: Coulomb-Like Repulsion

When two topological charges approach each other (decreasing their separation $d$), they encounter a zone activation barrier from the Forward zone phase repulsion. For two same-chirality charges ($\chi_1 = \chi_2 = +1$): the Forward zone phase gradients add constructively (both pushing in the same direction), creating an increasing repulsive energy as $d \to 0$:

$$
\Lambda_{\text{barrier}}^{(\text{Coulomb})} = \frac{e^2}{4\pi\epsilon_0 d}
$$

(for electrically charged composite — the Coulomb barrier). For neutral charges: the activation barrier comes from the Expansion zone overlap energy:

$$
\Lambda_{\text{barrier}}^{(\text{neutral})} = D\Phi_B^2 \frac{r_{\text{bloom}}^2}{d^2}
$$

(the energy cost of the two Expansion zone blooms overlapping — they must compress each other as they come together, which costs energy since the bloom prefers to expand). This is the **van der Waals barrier** for neutral composites — the short-range repulsion from overlapping Expansion zones.

**Tunneling through the barrier:** Quantum-mechanically, the charges need not classically surmount the barrier — they can tunnel through it. The tunneling probability:

$$
P_{\text{tunnel}} \approx e^{-2\int_0^d k(r)\,dr}
$$

(the WKB approximation), where $k(r)$ is the local momentum under the barrier. For nuclear fusion: $P_{\text{tunnel}} = P_{\text{Gamow}} = e^{-2\pi\eta}$ (the Gamow factor, section 14.1), where $\eta = Z_1 Z_2 e^2/(4\pi\epsilon_0\hbar v)$ (the Sommerfeld parameter). The Gamow factor gives the dominant contribution to stellar fusion rates.

---

## Composite Lock Energy: Zone Sharing Benefit

Once the charges overcome or tunnel through the barrier and their zones overlap, the composite lock energy is:

$$
\Lambda_{\text{comp}} = \sum_\alpha \Lambda_\alpha(\mathbf{z}_{\text{merged}}) - \sum_\alpha \sum_i \Lambda_\alpha(\mathbf{z}_{\text{sep},i})
$$

(the merged zone energy minus the sum of individual zone energies — the **binding energy** from zone sharing). The sign of this difference determines whether the composite is bound:

- $\Lambda_{\text{comp}} > 0$: zone sharing is energetically favorable — composite is bound
- $\Lambda_{\text{comp}} < 0$: zone sharing is energetically unfavorable — composite is unbound (repulsive)
- $\Lambda_{\text{comp}} = 0$: marginal binding — composite is at the threshold

**Example: Two-charge pair threshold.** For a pair of charges with opposite chirality ($\chi_1 = +1, \chi_2 = -1$), the composite lock energy contributions:

| Zone | Separate | Merged | $\Delta\Lambda$ |
|------|----------|--------|-----------------|
| Core | $\Lambda_c^{(1)} + \Lambda_c^{(2)}$ | $\Lambda_c^{(\text{pair})} \approx 2\Lambda_c$ | $\approx 0$ |
| Memory | $\Lambda_m^{(1)} + \Lambda_m^{(2)}$ | $\Lambda_m^{(\text{pair})} < 2\Lambda_m$ | $< 0$ (asymmetry penalty) |
| Expansion | $\Lambda_e^{(1)} + \Lambda_e^{(2)}$ | $\Lambda_e^{(\text{pair})} < 2\Lambda_e$ | $< 0$ (overlap penalty) |
| Forward | $\Lambda_f^{(1)} + \Lambda_f^{(2)}$ | $\Lambda_f^{(\text{pair})} \approx 0$ | $> 0$ (gradient cancellation benefit) |
| Apex | $\Lambda_a^{(1)} + \Lambda_a^{(2)}$ | $\Lambda_a^{(\text{pair})} = 2\Lambda_a + \Delta_{\text{Cooper}}$ | $> 0$ (Cooper pair binding) |
| Transition | $\Lambda_t^{(1)} + \Lambda_t^{(2)}$ | $\Lambda_t^{(\text{pair})} \approx 2\Lambda_t$ | $\approx 0$ |

The net composite lock energy:

$$
\Lambda_{\text{comp}} = \Delta\Lambda_{\text{fwd}} + \Delta\Lambda_{\text{apex}} + \Delta\Lambda_{\text{mem}} + \Delta\Lambda_{\text{exp}}
$$

$$
= (\text{Forward cancellation} + \text{Cooper pairing}) - (\text{Memory asymmetry} + \text{Expansion overlap})
$$

The composite is bound if the Forward gradient cancellation plus Cooper pair binding exceeds the Memory asymmetry and Expansion overlap penalties. For a Cooper pair ($\chi_+ + \chi_-$ pair moving in opposite directions): Forward zone gradients cancel exactly ($k_+ + k_- = 0$ for opposite momenta), giving large $\Delta\Lambda_{\text{fwd}} > 0$; plus the Apex Cooper pair binding $\Delta_{\text{Cooper}} > 0$. The composite lock energy is positive — the Cooper pair is bound.

---

## The N-Charge Threshold: When Does the Composite Form?

For an $n$-charge composite, the composite threshold generalizes to:

$$
\Lambda_{\text{comp}}^{(n)} > \Lambda_{\text{barrier}}^{(n)}
$$

The composite lock energy $\Lambda_{\text{comp}}^{(n)}$ scales with $n$ in a complex way (because the zone energy contributions are not simply additive for $n > 2$). The key scaling relations:

**For pair composites ($n = 2$):**
$$
\Lambda_{\text{comp}}^{(2)} \sim \Delta_{\text{Cooper}} \propto e^{-1/\lambda_{\text{eff}} N(0)}
$$
(exponentially small in the weak-coupling limit $\lambda_{\text{eff}} N(0) \ll 1$, where $\lambda_{\text{eff}}$ is the effective Apex zone coupling and $N(0)$ is the Memory zone density of states at the Fermi level — the BCS formula)

**For triple composites ($n = 3$):**
$$
\Lambda_{\text{comp}}^{(3)} \sim J_{\text{color}} \propto \alpha_s / r_{\text{confinement}}
$$
(linear in the strong coupling constant $\alpha_s$ and inverse confinement radius — the QCD confinement string tension in ICHTB language)

**For large composites ($n \gg 1$):**
$$
\Lambda_{\text{comp}}^{(n)} \sim a_V n - a_S n^{2/3} - \ldots
$$
(the SEMF for nuclei, section 21.1) — the composite lock energy becomes the nuclear binding energy for large $n$.

The composite threshold for large $n$ is the **stability threshold**: the minimum mass number $A_{\text{min}}$ above which the SEMF gives $E_B > 0$ (positive binding energy). From the SEMF:

$$
a_V A - a_S A^{2/3} > 0 \implies A > (a_S/a_V)^3 \approx (18.3/15.8)^3 \approx 1.55
$$

(the minimum stable composite has $A > 1.55$, i.e., $A_{\text{min}} = 2$ — the deuteron is the lightest bound two-nucleon composite). This matches the observed fact that the deuteron is the lightest stable nucleus (no bound dineutron or diproton), consistent with $A_{\text{min}} = 2$.

---

## Resonant Composite Thresholds

Not all composite thresholds involve stable composites — some are **resonant thresholds**: the composite forms temporarily (as a resonance above the threshold) before decaying back to its constituents. Resonant composites correspond to Region III or IV configurations in the survival map — they have $S^* \lesssim 1$ (just below the persistence threshold).

**Example: The Borromean nucleus threshold.** Borromean nuclei (e.g., ${}^{11}$Li, ${}^{6}$He) are three-body composites where the three-body composite is bound ($\Lambda_{\text{comp}}^{(3)} > 0$) but no two-body sub-composite is bound ($\Lambda_{\text{comp}}^{(2)} < 0$ for all pairs). This is the ICHTB version of the Borromean rings — a topological entanglement where the composite is bound only as a whole, not in parts.

In ICHTB terms: the Borromean nucleus is a triple-braid composite ($\Delta^2 \in B_3$) where the full $B_3$ braid is necessary for the composite threshold to be exceeded ($\Lambda_{\text{comp}}^{(\Delta^2)} > \Lambda_{\text{barrier}}$), but any $B_2$ sub-braid ($\sigma_1^2$ for any pair) gives $\Lambda_{\text{comp}}^{(\sigma_1^2)} < 0$ (pair is unbound). The Borromean structure requires the non-abelian ($B_3$ beyond $B_2$) braid topology — it is impossible in $B_2$ (pairs) alone.

The Borromean threshold is a **genuinely three-body threshold** — it cannot be reduced to a product of pair thresholds. This is the ICHTB signature of **Efimov physics** (Efimov 1970): the universal three-body bound states that appear at the unitary limit of two-body interactions (where all pair composites are exactly at threshold). The Efimov states are the ICHTB triple-braid configurations at the cusp $\Lambda_{\text{comp}}^{(2)} = 0, \Lambda_{\text{comp}}^{(3)} > 0$.

