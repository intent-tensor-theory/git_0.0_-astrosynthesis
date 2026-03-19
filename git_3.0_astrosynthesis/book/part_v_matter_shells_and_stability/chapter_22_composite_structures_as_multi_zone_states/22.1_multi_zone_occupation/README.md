# 22.1 Multi-Zone Occupation — What Composite Means in the Box

## Composite Excitations: A Reprise

A **composite excitation** (introduced as Region VI in section 18.6) is an ICHTB configuration containing more than one topological charge — more than one NLS vortex, brane, or domain wall — simultaneously enclosed within the same box and collectively locked by the zone structure. The individual constituent charges share the six ICHTB zones; they do not each have their own separate box.

The key question of this chapter is: what does it mean, precisely, for multiple topological charges to occupy the same ICHTB zone structure simultaneously? How do they share the zones? What constraints does multi-zone occupation impose? When is a composite more or less stable than the equivalent number of individual (non-composite) charges?

---

## Single vs. Multi-Zone Occupation

For a single topological charge in an ICHTB (a single NLS vortex or soliton), zone occupation is straightforward:

- The charge's amplitude peak sits in the **Core zone** (highest $|\Psi|$).
- Its phase winds through the **Memory zone** (the $2\pi n$ phase cycle around the charge core).
- The **Expansion zone** accommodates its transverse spread.
- The **Forward zone** carries its phase gradient (propagation direction).
- The **Apex zone** supports its orbital angular momentum modes.
- The **Transition zone** provides the gradient bridge between Core and background.

**Multi-zone occupation** means two or more topological charges simultaneously sharing this zone structure. "Sharing" can take three forms:

1. **Separated**: the charges occupy spatially non-overlapping sub-regions within the same zone (like two vortices in the same Memory zone disc, spatially apart).
2. **Overlapping**: the charges' wavefunctions overlap significantly in one or more zones (like two vortices whose Core zones merge, forming a higher-winding vortex).
3. **Entangled**: the charges' zone occupations are quantum-mechanically entangled — the state is a superposition of different zone assignments for different charges (the ICHTB quantum many-body state).

Most physically relevant composites are of type 1 (separated) or type 2 (overlapping). Type 3 (entangled) applies to quantum composites (Cooper pairs, atomic electron pairs) and is handled through the Apex zone braid structure (section 22.2).

---

## Zone Sharing Rules

The zone structure imposes specific rules on how multiple charges can share zones:

**Core zone (unique occupation rule):** The Core zone has a definite location (the amplitude maximum). For separated charges ($d_{\text{vortex}} \gg \xi$, where $d_{\text{vortex}}$ is the inter-vortex separation and $\xi$ is the coherence length), each charge has its own Core zone sub-region. For overlapping charges ($d_{\text{vortex}} \lesssim \xi$), the Core zones merge — the composite has a single merged Core zone at a location between the constituent charge positions, with winding number $n_{\text{merged}} = n_1 + n_2$ (the ICHTB equivalent of a multi-winding vortex).

The **Core zone unique occupation rule**: the Core zone can support at most one amplitude maximum at a given time (the field $|\Psi(\mathbf{x})|$ has a unique global maximum). Multiple charges either have separated local maxima (each in a different Core sub-zone) or merge into a single higher-winding maximum.

**Memory zone (multi-occupation rule):** The Memory zone is a disc of radius $R_m$ (section 16.3). Multiple vortex cores can all lie within the same Memory disc — the Memory zone supports multi-occupation readily. Each additional vortex contributes its $2\pi$ phase winding to the total Memory zone phase circulation, which becomes $2\pi n_{\text{comp}}$ for a composite with $n_{\text{comp}}$ charges. The Memory zone is the natural "hosting" zone for composite excitations — it is the zone that tracks the total topological charge count.

**Expansion zone (flux bundle rule):** The Expansion zone bloom spreads from the Core. For a composite with $n_{\text{comp}}$ charges in a single merged Core (winding $n_{\text{comp}}$), the bloom radius scales as $r_{\text{bloom}} \propto n_{\text{comp}}^{1/2}$ (the Abrikosov flux bundle law — the bloom area scales as the total flux $n_{\text{comp}} \Phi_0$). For separated charges, each charge has its own individual bloom.

**Forward zone (phase gradient superposition):** The Forward zone phase gradient is the sum of individual charges' phase gradients:

$$
\nabla\phi_{\text{fwd}} = \sum_{i=1}^{n_{\text{comp}}} \nabla\phi_{\text{fwd}}^{(i)}
$$

For aligned charges (all moving in the same direction): the phase gradients add constructively — a composite moving as a unit. For anti-aligned charges (moving in opposite directions): the phase gradients cancel — the composite has zero net Forward zone phase gradient (zero net momentum, bound state).

**Apex zone (orbital angular momentum superposition):** The Apex zone orbital angular momentum is the sum of individual charges' orbital angular momenta (subject to Apex braid rules, section 22.2).

---

## What "Composite" Means in the Box

A composite excitation inside an ICHTB box is defined by:

1. **Total topological charge** $n_{\text{comp}} = \sum_i n_i$ (the sum of individual winding numbers)
2. **Zone occupation pattern** $\mathbf{z} = (z_{\text{core}}, z_{\text{mem}}, z_{\text{exp}}, z_{\text{fwd}}, z_{\text{apex}}, z_{\text{trans}})$ where $z_\alpha$ specifies the multi-occupation state of zone $\alpha$
3. **Braid type** $[w] \in B_{n_{\text{comp}}}$ (the braid class of the multi-charge worldline, section 22.2)
4. **Lock energy** $\Lambda_{\text{lock}}^{(\text{comp})} = \sum_\alpha \Lambda_\alpha(\mathbf{z})$ (the sum of zone lock energies, evaluated at the multi-occupation pattern $\mathbf{z}$)

The composite is **stable** (persistent) if:

$$
S^*(\text{comp}) = \frac{\Lambda_{\text{lock}}^{(\text{comp})}}{\dot{\Lambda}_{\text{lock}}^{(\text{comp})} \cdot t_{\text{ref}}} > 1
$$

and **unstable** (dissociating) if $S^* < 1$. The composite is more stable than its constituents if:

$$
S^*(\text{comp}) > n_{\text{comp}} \cdot S^*(\text{individual})
$$

(the composite's total persistence exceeds the sum of constituent persistences — the composite is "greater than the sum of its parts").

---

## The Composite Advantage and the Composite Penalty

**Composite advantage:** A composite may have higher $S^*$ than its constituents if the zone sharing creates additional lock energy (e.g., Apex braid pairing, Cooper pair binding, Core zone merger increasing the depth of the amplitude well). The composite advantage arises from **constructive multi-zone interference** — the constituents' zone contributions reinforce each other.

**Composite penalty:** A composite may have lower $S^*$ than its constituents if the zone sharing creates additional energy costs (e.g., Memory zone vortex repulsion, Forward zone Coulomb repulsion). The composite penalty arises from **destructive multi-zone competition** — the constituents' zone contributions compete with each other, reducing the total lock energy below the sum of individual contributions.

The condition for composite formation (the composite forms spontaneously from individual charges):

$$
\Lambda_{\text{lock}}^{(\text{comp})} > \sum_i \Lambda_{\text{lock}}^{(i)} + \Lambda_{\text{barrier}}
$$

where $\Lambda_{\text{barrier}}$ is the zone activation barrier (the energy cost to bring the individual charges close enough for their zones to overlap and merge). If the composite lock energy exceeds the sum of individual lock energies plus the barrier, the composite forms and persists. Otherwise, the individual charges remain separate.

This composite formation condition is the ICHTB analog of the nuclear binding energy condition: a nucleus is bound if its total mass is less than the sum of its constituent masses ($E_B > 0$). The zone activation barrier $\Lambda_{\text{barrier}}$ is the ICHTB analog of the Coulomb barrier to nuclear fusion.

