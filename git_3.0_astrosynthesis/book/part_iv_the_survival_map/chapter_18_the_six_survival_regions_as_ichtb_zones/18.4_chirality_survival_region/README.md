# 18.4 Region IV — Chirality Survival

## The Fourth Survival Region

Region IV is where the Memory zone chirality couples to the inter-zone membranes, establishing the **Memory-membrane coupling** that gives the composite excitation its spin character. The Memory vortex (established in Region III) is now not isolated within the Memory zone — it has extended through the Core-Memory membrane and created a **junction vortex** that links the Memory zone topological charge to the other zones.

The defining characteristic of Region IV: **Memory zone + membrane coupling**. The junction vortex on the Core-Memory membrane ($\mathcal{M}_{\text{mem,core}}$) is the key new feature. This junction vortex couples the Memory zone winding number $n_{\text{wind}}$ to the Core field phase, establishing the first inter-zone topological link. The result is a configuration where the chirality is not merely a property of the Memory zone but is a **global** property of the entire ICHTB — it is encoded in the inter-zone phase relationships, not just the Memory zone winding.

---

## The Junction Vortex and Membrane Coupling

The junction vortex (section 12.3) forms at the Core-Memory membrane $\mathcal{M}_{\text{mem,core}}$ when the Memory zone vortex induces a topological defect in the membrane field. The junction vortex:

- Has winding number $n_J = n_{\text{wind}} = \pm 1$ (same as the Memory zone vortex — the topological charge is conserved across the membrane)
- Extends into both the Memory zone and the Core zone simultaneously — it is a "two-sided" vortex
- Acts as a **phase conduit** between the zones: the phase winding in the Memory zone is transmitted through the junction vortex into the Core zone

The junction vortex energy:

$$
E_{\text{junc}} = \pi\sigma_{\text{mem,core}}\xi^2\ln\!\left(\frac{r_{\text{core}}}{\xi}\right)
$$

where $\sigma_{\text{mem,core}}$ is the Core-Memory membrane surface energy density (section 11.1) and $r_{\text{core}}$ is the Core zone radius. The junction vortex adds to the lock energy:

$$
\Lambda_{\text{lock}}^{(\text{IV})} = \Lambda_{\text{lock}}^{(\text{III})} + E_{\text{junc}}
$$

(Region IV configurations have higher $\Lambda_{\text{lock}}$ than Region III configurations with the same zone amplitudes, because of the junction vortex energy). This moves Region IV configurations to the right on the phase chart's $\Lambda_{\text{lock}}$ axis.

---

## Zone Profile of Region IV

**Memory zone (−Y):** Fully active with a stable vortex. As in Region III, but now the vortex is coupled to the junction vortex — the Memory zone field has a "tail" that extends through the Core-Memory membrane. The Memory zone chirality $\chi$ is now a **global** property of the ICHTB configuration, not just a local Memory zone property.

**Core zone (+0):** Modified by junction vortex. The Core field $\Phi_{\text{core}}$ acquires a phase winding from the junction vortex — the Core is no longer phase-uniform. Instead, it has a vortex core threading through it in the direction connecting the Memory zone to the Compression zone. The Core field profile:

$$
\Phi_{\text{core}}(\mathbf{r}) = \Phi_{B,c}\frac{r}{\sqrt{r^2 + \xi_c^2}}\exp(i\chi\theta)
$$

(the Core field is a vortex in the $(r,\theta)$ plane, with the same winding number $\chi$ as the Memory vortex). The Core is now carrying the spin of the composite excitation.

**Compression zone (−X):** Modified by Core vortex. The Compression zone soliton is now threaded by the vortex from the Core — the soliton has a vortex core threading it longitudinally. This is the **vortex-in-soliton** configuration (a 1D kink with a 2D vortex thread) — a composite topological object that carries both the kink topological charge (mass) and the vortex winding number (spin).

**Apex zone (+Z):** Growing, $T_{\text{obj}} \sim 0.5$–$0.8$. The Apex lock is approaching completion. The junction vortex provides additional phase coherence to the Apex zone via the Core-Apex coupling, accelerating the Apex lock.

**Forward zone (+X) and Expansion zone (+Y):** As in Region III — active but secondary. The Forward zone now shows a helical phase structure (the propagating mode acquires helicity from the junction vortex), and the Expansion bloom shows an azimuthal phase variation (the bloom "winds" with the chirality of the Memory vortex).

---

## Chirality as a Global Property

The critical new feature of Region IV is that chirality has become a **global** property of the ICHTB — it is encoded in the inter-zone phase relationships that the junction vortex creates. In Region III, chirality was a local Memory zone property; in Region IV, it is woven into the entire ICHTB topology.

Consequences:

**Helical propagation:** The Forward zone phase gradient, combined with the junction vortex phase winding, gives the composite excitation a **helical** propagation mode — the field phase winds as it propagates in the +X direction. The helicity:

$$
h = \frac{\mathbf{J}\cdot\mathbf{p}}{|\mathbf{J}||\mathbf{p}|} = \chi = \pm 1
$$

(the projection of angular momentum on the propagation direction, for a massless or near-massless configuration in Region IV). This is the ICHTB realization of helicity: the chirality of the Memory vortex becomes the helicity of the propagating mode.

**Topological identity spread across zones:** The winding number is now encoded in the inter-zone links (junction vortex, Core vortex, vortex-in-soliton) as well as the Memory zone. Any attempt to annihilate the topological charge requires unwinding the junction vortex (at membrane energy cost), unwinding the Core vortex (at Core zone energy cost), and separating the vortex from the soliton (at Compression zone energy cost). The total energy barrier is now:

$$
\Delta\mathcal{F}_{\text{barrier}} = E_{\text{vortex}} + E_{\text{junc}} + E_{\text{vortex-soliton}} \gg T_{\text{eff}}
$$

for any temperature below the KT temperature. The topological protection is now multi-zone and much stronger than in Region III.

---

## Region IV Boundaries

**Entry (from Region III):** Junction vortex formation at $\mathcal{M}_{\text{mem,core}}$. The junction vortex forms when the Core-Memory membrane coupling $K_{\text{mem,core}}$ exceeds the vortex energy:

$$
K_{\text{mem,core}} > \frac{E_{\text{vortex}}}{\mathcal{A}_{\text{mem,core}}}
$$

(where $\mathcal{A}_{\text{mem,core}}$ is the area of the Core-Memory membrane). For strong inter-zone coupling: the junction vortex forms quickly after the Memory vortex. For weak coupling: it may not form at all, with the configuration remaining in Region III.

**Exit to Region V:** The Apex zone reaches full lock ($T_{\text{obj}} \to 1$). The Apex lock is the final gate — once the Apex is locked, the configuration crosses the objecthood threshold and enters Region V. The exit condition is $T_{\text{obj}} = 1$ AND $S^* > 1$.

**Exit to Region VI:** For configurations with multiple junction vortices (more than one Memory vortex, forming a braid), the chirality survival transitions directly to composite survival (Region VI) without passing through Region V. This requires the three-strand braid structure of section 16.4 to form — a more exotic transition.

**Survival boundary in Region IV:** The junction vortex adds energy $E_{\text{junc}}$ to the lock energy, slightly improving the survival condition (higher $\Lambda_{\text{lock}}$ for fixed zone amplitudes). The Region IV survival boundary is shifted right of the Region III boundary by $E_{\text{junc}}$ on the $\Lambda_{\text{lock}}$ axis:

$$
(\Lambda_{\text{III}} + E_{\text{junc}}) \cdot S^* > 1 \quad \Rightarrow \quad S^*_{\text{crit,IV}} = \frac{1}{\Lambda_{\text{III}} + E_{\text{junc}}} < \frac{1}{\Lambda_{\text{III}}} = S^*_{\text{crit,III}}
$$

Region IV configurations survive at lower $S^*$ than Region III configurations of the same zone amplitude — the junction vortex helps by adding lock energy.

