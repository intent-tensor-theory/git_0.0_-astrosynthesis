# 19.1 Every Transition Is a Membrane Crossing

## The Membrane Correspondence Principle

The six survival regions of Chapter 18 are separated by five transition events. The central claim of Chapter 19 is that each of these transition events corresponds exactly to a **zone membrane crossing** in the ICHTB geometry — the field crossing a specific inter-zone boundary with sufficient amplitude to activate new topological or kinetic structure in the destination zone.

This is the **membrane correspondence principle**: every qualitative change in the ICHTB configuration (every region-to-region transition in the survival map) is a membrane crossing event in the ICHTB zone geometry.

The five transitions and their corresponding membranes:

| Transition | Direction | Membrane crossed | Physical event |
|---|---|---|---|
| I → II | Forward → Core | $\mathcal{M}_{\text{fwd,core}}$ | Forward phase gradient activates Core amplitude |
| II → III | Core → Memory | $\mathcal{M}_{\text{core,mem}}$ | Core amplitude drives Memory vortex nucleation |
| III → IV | Memory → Core (junction) | $\mathcal{M}_{\text{mem,core}}$ (junction) | Memory vortex couples through Core to other zones |
| IV → V | Core → Apex | $\mathcal{M}_{\text{core,apex}}$ | Core-Apex coupling completes Apex phase lock |
| V → VI | Memory (multi-vortex) | $\mathcal{M}_{\text{mem,core}}$ (second) | Second vortex crosses Core membrane; braid forms |

Each membrane crossing is an irreversible event above a threshold amplitude (section 19.3), and each creates a new conserved quantity (section 19.4). The five transitions thus build up a **nested hierarchy of conserved charges** — each region adds one new conserved quantity to the set, until Region VI has the full complement of five conserved charges.

---

## Why Membranes Are the Transition Sites

Zone membranes are the transition sites for three structural reasons:

**1. Amplitude discontinuity:** The B-state amplitude can differ between adjacent zones — $\Phi_{B,\alpha} \neq \Phi_{B,\beta}$ across $\mathcal{M}_{\alpha\beta}$. This amplitude mismatch creates a **potential step** at the membrane. A field propagating from zone $\alpha$ into zone $\beta$ must overcome this step if $\Phi_{B,\beta} > \Phi_{B,\alpha}$ (the destination zone requires higher amplitude). The step creates a threshold — below which the field is reflected, above which it transmits.

**2. Diffusion coefficient discontinuity:** The diffusion coefficient $D$ can also jump at the membrane ($D_\alpha \neq D_\beta$). A jump in $D$ creates a **velocity mismatch** — the field propagates at different speeds in the two zones (speed $\sim Dk$ in each zone). This velocity mismatch is the source of the partial reflection and transmission at the membrane (the transmission coefficient $T_{\alpha\beta}$ of sections 11.2 and 18.2).

**3. Phase condition:** The membrane imposes a **phase condition** on the field — the field must be phase-continuous across the membrane (the membrane has zero thickness in the thin-membrane approximation). This phase continuity condition, combined with the amplitude and velocity mismatches, gives the full set of membrane boundary conditions (section 11.1).

The threshold amplitude for membrane crossing (below which the field is completely reflected):

$$
\Phi_{\text{thresh},\alpha\beta} = \Phi_{B,\beta}\sqrt{\frac{1 - T_{\alpha\beta}}{T_{\alpha\beta}}}
$$

(the amplitude in zone $\alpha$ at which the transmission to zone $\beta$ equals 50%). For $\Phi_\alpha > \Phi_{\text{thresh},\alpha\beta}$: the field predominantly transmits into zone $\beta$ (crossing the membrane). For $\Phi_\alpha < \Phi_{\text{thresh},\alpha\beta}$: the field is predominantly reflected back into zone $\alpha$ (failing to cross the membrane).

---

## The Five Membranes in ICHTB Geometry

The five transition membranes in the ICHTB cuboctahedral geometry:

**$\mathcal{M}_{\text{fwd,core}}$ (I→II transition):** The Forward-to-Core membrane separates the +X zone from the +0 (Core) zone. It is one of the 12 triangular facets of the cuboctahedron (section 3.3). The Forward zone phase gradient drives a wave in the +X direction; the wave reaches this membrane and must transmit into the Core to activate it.

**$\mathcal{M}_{\text{core,mem}}$ (II→III transition):** The Core-to-Memory membrane separates the +0 (Core) from the −Y (Memory) zone. The Core amplitude, once established, drives a secondary wave in the −Y direction; this wave reaches the Core-Memory membrane and, if above threshold, nucleates the Memory zone vortex.

**$\mathcal{M}_{\text{mem,core}}$ (junction, III→IV transition):** The same membrane as above, but now crossed from the Memory side (−Y → +0 direction). The Memory zone vortex drives a phase winding back through the Core-Memory membrane, creating the junction vortex. This is the **reverse crossing** of the II→III transition — the same membrane, traversed in the opposite direction.

**$\mathcal{M}_{\text{core,apex}}$ (IV→V transition):** The Core-to-Apex membrane separates the +0 (Core) from the +Z (Apex) zone. Once the junction vortex has established the inter-zone phase coherence (IV), the Core phase oscillations at $\omega_B$ drive through this membrane into the Apex zone, completing the Apex lock.

**$\mathcal{M}_{\text{mem,core}}$ (second crossing, V→VI transition):** The Core-Memory membrane is crossed a second time by a second vortex (or by a higher winding-number vortex). This second crossing creates the two-strand (or higher) braid structure of Region VI.

---

## The Membrane Sequence as a Directed Graph

The five transition membranes form a **directed graph** of the ICHTB development path:

```
A-state → [M_fwd,core] → Region II → [M_core,mem] → Region III
                                                          ↓
                                               [M_mem,core junction]
                                                          ↓
                                               Region IV → [M_core,apex] → Region V → [M_mem,core ×2] → Region VI
```

The directed graph has one path: A-state → I → II → III → IV → V → VI. Each arrow is a membrane crossing. The development sequence of Chapter 15 (the six-fan lock logic) maps exactly onto this directed graph — each fan step corresponds to a membrane crossing in the sequence.

The correspondence:

| Fan step (Section 15.3) | Membrane | Region transition |
|---|---|---|
| Step 1: Core activation | $\mathcal{M}_{\text{fwd,core}}$ | I → II |
| Step 3: Expansion bloom | $\mathcal{M}_{\text{core,exp}}$ | (Internal to II) |
| Step 4: Memory vortex | $\mathcal{M}_{\text{core,mem}}$ | II → III |
| Steps 4–5: Junction coupling | $\mathcal{M}_{\text{mem,core}}$ reverse | III → IV |
| Step 5: Apex lock | $\mathcal{M}_{\text{core,apex}}$ | IV → V |
| Step 6: Compression soliton | $\mathcal{M}_{\text{core,comp}}$ | (Internal to III/IV) |

The directed graph makes explicit the linear ordering of the survival regions — they cannot be reached out of order (you cannot access Region V without passing through Regions II, III, and IV, because each requires the membrane crossings of the preceding regions as preconditions).

