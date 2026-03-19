# 18.3 Region III — Closure Survival

## The Third Survival Region

Region III is where **topological closure** is first achieved. The Memory zone vortex has formed (winding number $|n_{\text{wind}}| = 1$), the Core is strongly active, and the Expansion bloom is well-developed. The Hopf loop has completed its Type-II circuit (Memory + Core + Compression, section 16.1) — the configuration carries a nonzero topological charge for the first time.

But the Hopf invariant is not yet at its full quantized value: $T_{\text{obj}} < 1$ (the Apex zone is not fully locked). The configuration is **topologically nontrivial but not yet an object** in the full sense of section 16.3. It has crossed the closure threshold but not the objecthood threshold. Region III is the "closed but not locked" regime.

The defining characteristic of Region III: **Memory zone activation**. The Memory zone is the first zone to contribute topological structure (winding number), and its activation is what separates Region III from Region II. The zone admissibility gate $\mathcal{A}_{\text{mem}} = 1$ is the entry condition.

---

## Zone Profile of Region III

**Memory zone (−Y):** Fully active with a single stable vortex. $n_{\text{wind}} = \pm 1$ — the chirality $\chi = \pm 1$ is established. The Memory zone is below the KT temperature ($T_{\text{eff}} < T_{KT}$): the vortex is thermally stable, not immediately annihilating with an antivortex. Lock energy:

$$
\Lambda_{\text{mem}} = \pi D_m\Phi_{B,m}^2\ln\!\left(\frac{R_{\text{mem}}}{\xi}\right)
$$

Now a significant contributor to the total $\Lambda_{\text{lock}}$.

**Core zone (+0):** Strongly active. The Core amplitude is near the B-state ($|\Phi(0)| \approx \Phi_{B,c}$). The Core serves as the junction between the Memory zone vortex and the other zone excitations — it is the "hub" through which the Hopf loop passes.

**Compression zone (−X):** Active. The Compression soliton has formed (admissibility gate $\mathcal{A}_{\text{comp}} = 1$ — the soliton threshold has been crossed). The kink-antikink pair in the Compression zone provides the mass contribution. $\Lambda_{\text{comp}} = E_{\text{kink}} = (4/3)\Phi_B^2\xi_c D_c k_c$ — now a major contribution.

**Apex zone (+Z):** Developing. $T_{\text{obj}} \sim 0.4$–$0.7$ — significant but not complete Apex coherence. The Hopf loop's Type-III circuit is being established, but the Apex zone is the bottleneck (as identified in section 15.3). The configuration is in the "proto-object" state of section 16.2.

**Forward zone (+X):** Active but secondary. The Forward phase gradient has been absorbed into the Core-Memory-Compression structure. The Forward zone contribution to $\Lambda_{\text{lock}}$ is now smaller than the Memory+Compression contributions.

**Expansion zone (+Y):** Active with full bloom ($r_{\text{bloom}} \gg \xi_\perp$). The bloom has reached its equilibrium radius, set by the competition between the outward diffusion force and the inter-zone coupling to the Memory zone.

**Zone configuration for Region III:**

$$
\Lambda_{\text{lock}} \approx \Lambda_{\text{mem}} + \Lambda_{\text{comp}} + \Lambda_{\text{core}}
$$

Memory, Compression, and Core now dominate. Forward and Expansion are secondary. Apex is developing.

---

## Topological Protection in Region III

The critical new feature of Region III: **topological protection**. The Memory zone vortex carries a conserved winding number $n_{\text{wind}} = \pm 1$. To change this winding number, the field must:
1. Create a vortex-antivortex pair in the Memory zone (at energy cost $E_{\text{pair}} \sim 2E_{\text{vortex}}$)
2. Move the antivortex to annihilate the existing vortex (crossing a membrane if necessary)
3. The net result: $n_{\text{wind}} = 0$, destroying the topological charge

Step 1 requires energy $\sim 2\pi D_m\Phi_B^2\ln(R/\xi) > T_{\text{eff}}$ (in the topologically ordered phase below $T_{KT}$). This barrier is the **topological protection energy** — the energy that prevents the Region III configuration from dissolving back to Region II.

The topological protection makes Region III configurations qualitatively more stable than Region II:
- Region II: kinetic stability only (Core amplitude maximum can be washed out by fluctuations)
- Region III: topological stability (vortex winding number conserved unless barrier is crossed)

The transition from Region II to Region III is therefore a **qualitative change** in the stability character of the configuration — not just a quantitative improvement. This is why the Survival Map treats them as distinct regions, not a continuum.

---

## Why Region III Is Not Yet Objecthood

Despite having topological protection, Region III configurations are not yet objects (in the sense of section 16.3). They have the Hopf loop partially closed (Type-II: Memory+Core+Compression) but not fully closed (Type-III: requiring the Apex zone). The Hopf invariant:

$$
H[\Phi]\Big|_{\text{Region III}} = T_{\text{obj}}^2 \cdot n_{\text{wind}} \in [0, n_{\text{wind}})
$$

is nonzero but not yet quantized to the integer value $n_{\text{wind}}$. The configuration carries a partial Hopf charge — it is topologically non-trivial but not yet topologically quantized.

The physical consequence: Region III configurations have definite chirality ($\chi = \pm 1$, from the Memory zone) and definite mass (from the Compression soliton) but **indefinite identity** — their quantum numbers are not yet fully commuted. The Apex zone lock is needed to "commit" the configuration to a specific identity by establishing the temporal quantum number (the Apex frequency $\omega_B$, which sets the mass scale).

Until $T_{\text{obj}} = 1$ (Region V), the configuration exists in a **superposition** of identities — it has the right topological structure to become a particle but has not yet committed to which particle it will be. This is the ICHTB version of an intermediate resonance: localized, topologically structured, but not yet in a definite quantum state.

---

## Region III Boundaries

**Entry (from Region II):** Memory vortex nucleation — the stochastic event where the Memory zone KT temperature is crossed and a stable vortex forms. Marked by $\mathcal{A}_{\text{mem}} = 1$ and $\Lambda_{\text{mem}} > 0$.

**Exit to Region IV:** The Memory zone vortex couples to the inter-zone membranes — specifically, the Memory-Core membrane $\mathcal{M}_{\text{mem,core}}$ develops a Junction vortex (section 12.3). This junction vortex couples the Memory chirality $\chi$ to the Core phase, establishing the first full membrane coupling. The exit to Region IV is marked by this coupling event.

**Exit to Region V (Apex lock):** In rare configurations where the Apex zone locks before the Memory-Core coupling is established, the configuration skips Region IV and goes directly to Region V. This requires unusually strong Apex zone drive ($\langle E_{\text{bind}}\rangle \gg \kappa$) with weak Memory-Core coupling ($K_{\text{mem,core}} \ll K_{\text{apex,core}}$).

**The survival boundary:** The Memory zone vortex energy $\Lambda_{\text{mem}} = \pi D_m\Phi_B^2\ln(R/\xi)$ combined with the Compression soliton energy $\Lambda_{\text{comp}} = (4/3)\Phi_B^2\xi_c D_c k_c$ must satisfy $(\Lambda_{\text{mem}} + \Lambda_{\text{comp}}) \cdot S^* > 1$. For fixed $S^*$, this sets a minimum Memory zone coupling $D_m > D_{m,\min}$:

$$
D_{m,\min} = \frac{1}{\pi\Phi_B^2\ln(R/\xi)\,S^*} - \frac{4\xi_c D_c k_c}{3\pi\ln(R/\xi)}
$$

This is the closure survival condition — the minimum diffusion coefficient in the Memory zone for a Region III configuration to persist.

