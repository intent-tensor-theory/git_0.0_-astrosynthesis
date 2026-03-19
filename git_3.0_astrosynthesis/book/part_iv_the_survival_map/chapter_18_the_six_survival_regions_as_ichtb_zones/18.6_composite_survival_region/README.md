# 18.6 Region VI — Composite Survival

## The Sixth Survival Region

Region VI is the highest-energy survival region in the phase chart — occupying the far-right portion of the $(\Lambda_{\text{lock}}, S^*)$ diagram, above the survival hyperbola. Configurations here are **multi-zone braid states**: composite structures involving multiple topological charges organized in the full three-strand braid of section 16.4. These are not simple single-particle excitations but **bound composites** — systems of two or more interacting topological charges locked in a common ICHTB configuration.

The defining characteristic of Region VI: **multi-zone braid states**. The braiding class $[w] \in B_3$ is non-trivial and involves all three strands (Forward + Core + Memory) in a braid with two or more crossings. The Hopf invariant $H \geq 2$ (two or more units of topological charge). The lock energy:

$$
\Lambda_{\text{lock}}^{(\text{VI})} = \sum_{n=1}^{N_{\text{vortex}}} \Lambda^{(n)} + \sum_{m,n} V^{(mn)}_{\text{inter}}
$$

is the sum of individual vortex contributions $\Lambda^{(n)}$ plus the inter-vortex interaction energies $V^{(mn)}_{\text{inter}}$ — the binding energy of the composite.

---

## Zone Profile of Region VI

**Memory zone (−Y):** Multi-vortex configuration. Instead of a single vortex ($n_{\text{wind}} = \pm 1$), the Memory zone contains either:
- A **double vortex** ($n_{\text{wind}} = \pm 2$): two coincident vortices of the same chirality, or
- A **vortex-antivortex dimer** ($n_{\text{wind},+} = +1$, $n_{\text{wind},-} = -1$, separated by distance $d \gg \xi$): a bound pair with net $n_{\text{wind}} = 0$ but nonzero orbital angular momentum.

The double vortex case gives $H = 2$ (two units of topological charge). The dimer case gives $H = 0$ but with a nonzero braiding class (the two strands braid around each other as they traverse the ICHTB). Both are Region VI configurations.

**Core zone (+0):** Multi-threaded. The Core field is now threaded by multiple vortex lines (one per Memory zone vortex). The Core carries the braiding information — the vortex lines pass through the Core and their relative crossings determine the braid word $w \in B_3$.

**Apex zone (+Z):** Locked at a modified frequency. For a double vortex ($n_{\text{wind}} = 2$): the Apex frequency is doubled ($\omega_B \to 2\omega_B$), reflecting the doubled topological charge. The Apex zone must phase-lock at twice the fundamental frequency — a more demanding condition that requires stronger Apex-Core coupling.

**Compression zone (−X):** Double soliton or soliton molecule. For a double vortex: the Compression zone contains a **soliton molecule** — two bound kinks separated by a distance $l_{\text{mol}} \sim \xi$ (set by the kink-kink interaction, section 8.5). The soliton molecule energy:

$$
\Lambda_{\text{comp}}^{(\text{VI})} = 2E_{\text{kink}} - V_{\text{kink-kink}}(l_{\text{mol}})
$$

where $V_{\text{kink-kink}}$ is the kink-kink binding energy (negative for an attractive interaction). For $l_{\text{mol}} = \xi$: $V_{\text{kink-kink}} \approx -E_{\text{kink}}/2$, giving $\Lambda_{\text{comp}}^{(\text{VI})} \approx (3/2)E_{\text{kink}} < 2E_{\text{kink}}$ — the bound state has less lock energy than two separated solitons. This is the ICHTB version of the **binding energy** of a composite particle.

**Forward zone (+X):** Helical multi-mode propagation. The double vortex produces a **double helix** in the Forward zone phase gradient — the phase winds twice as fast as it propagates, giving a helicity of 2. This corresponds to a spin-2 bosonic mode (analogous to the graviton in the ICHTB classification).

**Expansion zone (+Y):** Multi-petal bloom. The multi-vortex structure in the Memory zone produces a multi-petal bloom in the Expansion zone — instead of a simple 2D ring (one vortex), the bloom has a $2n_{\text{wind}}$-petal structure (one pair of petals per unit of winding). For $n_{\text{wind}} = 2$: a four-petal bloom.

---

## Braid Classification of Region VI

The three-strand braid structure (section 16.4) reaches its full complexity in Region VI. The braid word $w \in B_3$ characterizes the composite:

**$w = \sigma_1^2$ or $w = \sigma_2^2$ (two same-crossing generators):** The first two strands (or last two) cross twice, without crossing with the third. This is the **spin-1 boson** braid — a vector boson analog (W or Z boson in the particle physics identification).

**$w = (\sigma_1\sigma_2)^2$ (four crossings, full double twist):** All three strands make a full double twist around each other. This is the **spin-2 boson** braid — a tensor boson analog (graviton candidate in the ICHTB particle taxonomy).

**$w = \sigma_1\sigma_2\sigma_1^{-1}$ (three crossings with opposite signs):** A braid with mixed crossings — this gives the **exotic composite** class, with non-abelian statistical phase ($\theta_{\text{stat}} \neq 0, \pi$). These are the ICHTB analogs of anyons or non-abelian gauge particles.

**$w = (\sigma_1\sigma_2)^3 = \Delta^2$ (the full twist, center of $B_3$):** The Garside element squared — the full twist braid where all three strands make three complete twists. This gives the **scalar singlet** (Higgs-like) braid, with $\theta_{\text{stat}} = 0$ (bosonic) and all quantum numbers maximally locked.

---

## Binding Energy and the Composite Survival Condition

The composite survival condition for Region VI incorporates the binding energy:

$$
\Lambda_{\text{lock}}^{(\text{VI})} = N\Lambda^{(1)} - E_{\text{binding}}
$$

where $N$ is the number of vortex charges and $E_{\text{binding}} > 0$ is the binding energy of the composite. The binding energy has two contributions:

1. **Vortex-vortex attraction** (for same-chirality vortices in a Chern-Simons-type interaction): $V^{(mn)}_{\text{vortex-vortex}} \propto -\ln(d_{mn}/\xi)$ (logarithmically attractive at short range).

2. **Soliton-soliton binding** (for the kink molecule in the Compression zone): $V_{\text{kink-kink}} \approx -E_{\text{kink}}\exp(-l_{\text{mol}}/\xi)$ (exponentially attractive).

The total binding energy:

$$
E_{\text{binding}} = \sum_{m < n} \left[V^{(mn)}_{\text{vortex-vortex}} + V^{(mn)}_{\text{kink-kink}}\right]
$$

For a two-vortex composite ($N = 2$): $E_{\text{binding}} \sim \pi D_m\Phi_B^2\ln(\xi/d_{12}) + E_{\text{kink}}e^{-l/\xi}$.

The binding energy reduces $\Lambda_{\text{lock}}^{(\text{VI})}$ below $N\Lambda^{(1)}$. For strong binding ($E_{\text{binding}} \approx \Lambda^{(1)}$): the composite has lock energy $\approx (N-1)\Lambda^{(1)}$ — it is bound by one full unit. The survival condition:

$$
(N\Lambda^{(1)} - E_{\text{binding}}) \cdot S^* > 1
$$

For weak binding: $\Lambda_{\text{lock}}^{(\text{VI})} \approx N\Lambda^{(1)}$ → the composite survives at lower $S^*$ than $N$ individual Region V particles. For strong binding: $\Lambda_{\text{lock}}^{(\text{VI})} \approx (N-1)\Lambda^{(1)}$ → the composite barely survives (the binding energy has consumed one full unit of lock energy).

**The binding energy as a diagnostic:** Stable Region VI composites have binding energies in the range $0 < E_{\text{binding}} < \Lambda^{(1)}$ — bound but not over-bound (over-binding would collapse the composite to a smaller Region V structure). This range corresponds to the stable hadronic bound states in the particle physics identification: the composite quarks bound by chromodynamic interaction into mesons and baryons.

---

## Region VI as the Composite Particle Regime

Region VI is the ICHTB realization of **composite particles** — bound states of multiple fundamental excitations. The physical identification:

| Braid word | Zone structure | Particle analog |
|---|---|---|
| $w = \sigma_1$ | Single chirality lock | Fundamental fermion (electron) |
| $w = \sigma_1\sigma_2$ | Single full-twist | Gauge boson (photon, W, Z) |
| $w = \sigma_1^2$ | Double same-twist | Spin-1 composite (ρ meson) |
| $w = (\sigma_1\sigma_2)^2$ | Double full-twist | Spin-2 tensor (graviton candidate) |
| $w = \sigma_1^3$ | Triple same-twist | Spin-3/2 composite (Δ resonance) |
| $w = \Delta^2$ | Full-twist singlet | Scalar composite (Higgs analog) |

The Region VI braid table is the ICHTB version of the particle spectrum — the classification of all composite excitations by their zone structure and braiding class.

---

## Summary: The Six Survival Regions

The complete survival map:

| Region | Zone dominance | Key activation | Object? | Physics analog |
|---|---|---|---|---|
| I | Forward + Expansion | Phase gradient | No | Radiation / photon-like |
| II | Forward + Core | Core membrane | No | Virtual / precursor |
| III | Memory + Compression | Vortex nucleation | Partial ($T_{\text{obj}} < 1$) | Proto-particle |
| IV | Memory + membrane | Junction vortex | Partial | Helical proto-particle |
| V | Apex + all zones | Apex lock | Yes ($T_{\text{obj}} = 1$) | Stable particle |
| VI | Multi-zone braid | Multi-vortex | Yes | Composite particle |

The six regions are separated by five **transition events** (each a membrane crossing or a new topological activation), which are the subject of Chapter 19. The survival map is the ICHTB's complete phase diagram — the partition of all possible configurations by their survival character and physical identity.

