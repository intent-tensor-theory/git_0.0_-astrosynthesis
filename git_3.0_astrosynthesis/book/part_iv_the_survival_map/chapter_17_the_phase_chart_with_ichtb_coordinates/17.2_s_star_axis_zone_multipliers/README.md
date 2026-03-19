# 17.2 The $S^*$ Axis — Zone-Specific Persistence Multipliers

## The $S^*$ Axis as a Persistence Measure

The second axis of the survival map is the **corrected Selection Number** $S^*$ — the comprehensive persistence criterion derived in section 15.4. On this axis, configurations are ordered by how strongly they persist: $S^* \ll 1$ (rapidly dissolving, far below threshold) to $S^* \gg 1$ (strongly persistent, far above threshold).

The $S^*$ axis is more complex than the $\Lambda_{\text{lock}}$ axis because $S^*$ contains zone-specific multipliers — factors that reduce the nominal Selection Number $S = R/(\dot{R}t_{\text{ref}})$ based on the zone configuration. These multipliers encode the fact that different zones contribute differently to the persistence of the composite excitation.

The full expression (section 15.4):

$$
S^* = \mathcal{E}_{\text{shell}} \cdot \mathcal{E} \cdot D \cdot T_{\text{obj}} \cdot S
$$

Each factor is a zone-specific multiplier. Understanding how each factor behaves as a function of the ICHTB parameters is the task of this section.

---

## Zone-Specific Decomposition of $S^*$

The corrected Selection Number decomposes into zone contributions by expressing each multiplier in terms of its zone sources:

**Shell eligibility multiplier $\mathcal{E}_{\text{shell}}$:**

As derived in section 15.4:

$$
\mathcal{E}_{\text{shell}} = \Theta(T_{\text{shell,max}} - T_{\text{shell}}) \cdot \Theta(\bar{\Gamma}_{\text{int}} - \Gamma_{\text{env}}) \cdot \Theta(|\psi_{\text{shell}}| - \psi_{\text{shell,min}})
$$

This is a binary factor (0 or 1): either the shell conditions are satisfied or they are not. It is primarily a property of the Apex zone boundary — the Apex zone membrane is the outermost interface, and its reflectivity determines $T_{\text{shell}}$. The shell multiplier:

$$
\mathcal{E}_{\text{shell}} = \mathcal{E}_{\text{shell}}(\text{Apex}) \times \mathcal{E}_{\text{shell}}(\text{Expansion}) \times \mathcal{E}_{\text{shell}}(\text{Forward})
$$

(product of shell conditions at the three outward-facing zone boundaries: Apex, Expansion, Forward).

**Internal eligibility multiplier $\mathcal{E}$:**

$$
\mathcal{E} = \mathcal{A}_{\text{core}} \cdot \mathcal{A}_{\text{fwd}} \cdot \mathcal{A}_{\text{exp}} \cdot \mathcal{A}_{\text{mem}} \cdot \mathcal{A}_{\text{apex}} \cdot \mathcal{A}_{\text{comp}}
$$

(product of all six zone admissibility factors, section 15.1). This is the most sensitive multiplier — any one zone failing its admissibility condition drives $\mathcal{E}$ to zero, regardless of how well the other zones are performing. The weakest zone determines $\mathcal{E}$.

**Drift alignment multiplier $D$:**

$$
D = \frac{\sum_\alpha D_\alpha \Lambda_\alpha}{\sum_\alpha \Lambda_\alpha}
$$

(energy-weighted average of zone drift alignments, section 15.4). Zones with larger lock energies $\Lambda_\alpha$ contribute more to $D$. For a fully supercritical ICHTB ($D_\alpha > 0$ for all zones): $D > 0$. For an ICHTB with some zones trapped in metastable states ($D_\alpha \approx 0$ for those zones): $D$ is reduced from 1.

The drift multiplier is the **smoothest** of the factors — it varies continuously from 0 to 1 as the zones transition from metastable to fully aligned. It is the primary source of variability in $S^*$ for configurations that pass the binary eligibility gates.

**Topology factor multiplier $T_{\text{obj}}$:**

$$
T_{\text{obj}} = \frac{|\psi_{\text{apex}}|}{\Phi_{B,\text{apex}}} = (\text{Apex zone coherence fraction})
$$

The topology multiplier is a property of the Apex zone alone (section 16.2). It varies continuously from 0 (no coherence) to 1 (full lock). Like the drift multiplier, it is a smooth factor — the ICHTB can have $T_{\text{obj}} = 0.7$ (70% topological closure) and this reduces $S^*$ by 30%.

**Basic Selection Number $S$:**

$$
S = \frac{R}{\dot{R}t_{\text{ref}}} = \frac{\sum_\alpha S_\alpha \Lambda_\alpha}{\sum_\alpha \Lambda_\alpha}
$$

where $S_\alpha = R_\alpha / (\dot{R}_\alpha t_{\text{ref}})$ is the zone-specific Selection Number (the retention fraction in zone $\alpha$ over the reference time). The overall $S$ is the energy-weighted average of zone-specific values. A zone with high lock energy $\Lambda_\alpha$ contributes more to the total $S$.

---

## The Zone-Multiplier Table

Combining the above, the $S^*$ multipliers by zone:

| Factor | Primary zone | Range | Behavior |
|---|---|---|---|
| $\mathcal{E}_{\text{shell}}$ | Apex + Expansion + Forward | $\{0, 1\}$ | Binary gate |
| $\mathcal{A}_{\text{core}}$ | Core (+0) | $\{0, 1\}$ | Binary gate (amplitude) |
| $\mathcal{A}_{\text{fwd}}$ | Forward (+X) | $\{0, 1\}$ | Binary gate (phase gradient) |
| $\mathcal{A}_{\text{exp}}$ | Expansion (+Y) | $\{0, 1\}$ | Binary gate (bloom radius) |
| $\mathcal{A}_{\text{mem}}$ | Memory (−Y) | $\{0, 1\}$ | Binary gate (vortex present) |
| $\mathcal{A}_{\text{apex}}$ | Apex (+Z) | $\{0, 1\}$ | Binary gate (coherence begun) |
| $\mathcal{A}_{\text{comp}}$ | Compression (−X) | $\{0, 1\}$ | Binary gate (soliton present) |
| $D_{\text{core}}$ | Core (+0) | $[-1, 1]$ | Continuous, weighted |
| $D_{\text{mem}}$ | Memory (−Y) | $[-1, 1]$ | Continuous, weighted |
| $D_{\text{apex}}$ | Apex (+Z) | $[-1, 1]$ | Continuous, weighted |
| $T_{\text{obj}}$ | Apex (+Z) | $[0, 1]$ | Continuous, smooth |
| $S_{\text{core}}$ | Core (+0) | $[0, \infty)$ | Zone retention rate |
| $S_{\text{mem}}$ | Memory (−Y) | $[0, \infty)$ | Zone retention rate |
| $S_{\text{apex}}$ | Apex (+Z) | $[0, \infty)$ | Zone retention rate |

The $S^*$ axis is the product of all these factors — it is a high-dimensional product reduced to a single scalar. Moving along the $S^*$ axis means systematically increasing (or decreasing) all of these zone-specific factors in tandem.

---

## How $S^*$ Varies Across the Phase Chart

In the survival map (next section), the $S^*$ axis runs vertically (increasing upward). The behavior of $S^*$ across the diagram:

**At low $\Lambda_{\text{lock}}$ (left side of the chart):** The zone amplitudes are small ($\Phi_{B,\alpha} \ll \Phi_{B,\max}$), so the binary gates are near their thresholds (admissibility conditions are marginally satisfied). Small perturbations can tip any zone admissibility factor to 0. $S^*$ is fragile — it drops easily.

**At high $\Lambda_{\text{lock}}$ (right side of the chart):** The zone amplitudes are large, all binary gates are comfortably satisfied ($\mathcal{A}_\alpha = 1$ robustly), and the drift alignment $D$ is close to 1 (all zones drifting strongly toward the B-state). $S^*$ is close to the nominal $S = R/(\dot{R}t_{\text{ref}})$ — the additional multipliers have little effect.

**Along the $S^* = 1$ boundary:** This is the persistence horizon — the boundary where the composite excitation is marginally persistent. Above this boundary: objects form. Below: they dissolve. The persistence horizon is a curved line in the $(\Lambda_{\text{lock}}, S^*)$ plane (see section 17.3 for the full shape).

**For the zone multipliers as diagnostic tools:** In the phase chart, different multipliers dominate in different regions:
- In the lower-left: $\mathcal{E}$ (eligibility) is the dominant limiter — zones fail their admissibility conditions
- In the middle band: $D$ (drift) is the dominant variable — configurations are eligible but not all drifting correctly
- In the upper-right: $T_{\text{obj}}$ is the fine-tuning variable — eligible, well-drifted, but Apex lock incomplete

This spatial organization of the multipliers gives the phase chart its characteristic structure: a hierarchy of thresholds, with the topological threshold ($T_{\text{obj}} = 1$) as the final gate before objecthood.

