# 6.2 Junction Conditions Between Zone Operators

## From Single Membranes to Zone-to-Zone Transitions

Section 6.1 treated the field conditions at the interior of a single membrane face — the generic case where exactly one zone boundary separates two zone regions at a point. This gives the full single-interface formalism: continuity of $\Phi$, jump in normal flux, metric-jump geometric source, transmission coefficient, and Snell's law analog.

But the character of the ICHTB membranes is more specific than a generic interface. Each membrane separates two particular zone operators — and the operators have mathematical properties (second-order differential operators with definite sign structure) that impose additional constraints on the junction. This section exploits those operator properties to derive the **operator junction conditions** — conditions that are sharper than the generic field junction conditions because they are aware of which operators are meeting at the interface.

---

## The Six Zone Operators

Each of the six ICHTB zones is dominated by a particular differential operator acting on $\Phi$. From Chapters 3 and 4:

| Zone | Operator $\mathcal{O}_k$ | Character |
|------|--------------------------|-----------|
| Forward (+X) | $\partial_x\Phi$ | First-order, directional |
| Expansion (+Y) | $+\nabla^2\Phi$ | Second-order, elliptic, positive |
| Apex (+Z) | $\partial_t\Phi$ | First-order, temporal |
| Compression (−X) | $-\nabla^2\Phi$ | Second-order, elliptic, negative |
| Memory (−Y) | $\nabla\times\Phi$ | First-order, antisymmetric |
| Core (−Z) | $\mathbf{1}\cdot\Phi$ | Zero-order, identity |

At each membrane, exactly two of these operators meet. The junction condition between operators $\mathcal{O}_\alpha$ and $\mathcal{O}_\beta$ must respect the orders and characters of both operators simultaneously.

---

## The 15 Zone Pairs and Their Membranes

The cuboctahedron has 12 faces. Each face separates one zone from another. The ICHTB zone adjacency is not arbitrary: it is determined by the geometry of the cuboctahedron — specifically, by which pairs of pyramids share a triangular face. The 12 faces and their zone pairings:

In a cuboctahedron with six pyramids (one per axis), each pyramid shares triangular faces with its four "adjacent" pyramids (those at 90° to it). The two pyramids at 180° from each other (opposite zones: +X/−X, +Y/−Y, +Z/−Z) do not share a membrane — they are separated by the interior of the cuboctahedron.

The 12 membrane pairs (each zone borders four others):

| Membrane | Zone $\alpha$ | Zone $\beta$ | Interface type |
|----------|--------------|--------------|----------------|
| Face 1 | Forward (+X) | Expansion (+Y) | First-order / Positive-Laplacian |
| Face 2 | Forward (+X) | Apex (+Z) | First-order / Temporal |
| Face 3 | Forward (+X) | Memory (−Y) | First-order / Curl |
| Face 4 | Forward (+X) | Core (−Z) | First-order / Identity |
| Face 5 | Expansion (+Y) | Apex (+Z) | Positive-Laplacian / Temporal |
| Face 6 | Expansion (+Y) | Memory (−Y) | Positive-Laplacian / Curl |
| Face 7 | Expansion (+Y) | Core (−Z) | Positive-Laplacian / Identity |
| Face 8 | Apex (+Z) | Compression (−X) | Temporal / Negative-Laplacian |
| Face 9 | Apex (+Z) | Memory (−Y) | Temporal / Curl |
| Face 10 | Compression (−X) | Memory (−Y) | Negative-Laplacian / Curl |
| Face 11 | Compression (−X) | Core (−Z) | Negative-Laplacian / Identity |
| Face 12 | Memory (−Y) | Core (−Z) | Curl / Identity |

The six opposite-zone pairs (Forward/Compression, Expansion/Memory, Apex/Core) do **not** share membranes — they are not adjacent in the cuboctahedron. The absence of these membranes is geometrically exact.

---

## Operator-Specific Junction Conditions

The key insight: the order of the zone operator constrains what can be continuous across its membrane. When a second-order operator (Expansion, Compression) meets a first-order operator (Forward, Memory, Apex) at a membrane, the junction conditions have a definite asymmetry — the second-order side has a "flux" (the normal derivative weighted by the metric) that the first-order side does not.

**Case A: Two Second-Order Operators Meet (Expansion / Compression)**

This case does not actually occur as a direct adjacency — +Y and −X are not adjacent in the cuboctahedron. But it appears at edge-meeting points (section 6.3). For reference: when $\mathcal{O}_\alpha = +\nabla^2$ and $\mathcal{O}_\beta = -\nabla^2$ meet at a point, the junction conditions are symmetric:

$$
\Phi_\alpha = \Phi_\beta, \qquad D_\alpha\partial_n\Phi_\alpha = D_\beta\partial_n\Phi_\beta
$$

Two Laplacians of equal and opposite sign at a junction: both sides see the same normal derivative (since the geometry is matched at the junction), but the equations they satisfy have opposite sign — so the field bends away from the membrane on both sides. This is the **saddle junction** — it appears at the intersection of Expansion and Compression zones and governs the saddle-point structure of the ICHTB field.

**Case B: Second-Order / First-Order Operator (Expansion or Compression meets Forward, Apex, Memory)**

The second-order zone contributes a normal derivative to the junction; the first-order zone does not (it has no Laplacian term, so there is no "flux" to match). The conditions are **asymmetric**:

From the Expansion (+Y) side (operator $+\nabla^2$), the second-order junction condition provides:
$$
D_Y\mathcal{M}^{ij}_Y n_i\partial_j\Phi_Y = \text{right-hand side}
$$

From the Forward (+X) side (operator $\partial_x$), the first-order zone has only a first-order equation — it has no second-order spatial term in its dominant operator. The junction condition from the first-order side is therefore:
$$
\Phi_X = \Phi_Y \quad \text{(continuity)}
$$

and the normal flux equation provides **one** constraint that is satisfied automatically by the second-order side; the first-order side contributes no additional constraint. The junction is **one-sided in flux** — only the Expansion zone contributes a normal flux condition.

This asymmetry has a physical consequence: waves crossing from a second-order zone (Expansion) into a first-order zone (Forward) are **refraction-free** in the tangential direction — there is no Snell's law tangential constraint, because the first-order zone has no notion of "angle of propagation" in the same sense as the second-order zone. The wave simply passes through, preserving $\Phi$ at the boundary, and adopts the Forward-zone propagation character (directional, along $\hat{x}$) on the other side.

**Case C: First-Order / Zero-Order Operator (Forward, Memory, or Apex meets Core)**

The Core zone has operator $\mathbf{1}$ — the identity, a zero-order operator. It has no spatial derivative at all. The junction condition from the Core side has no flux — only continuity of $\Phi$. From the first-order side (e.g., Forward):

$$
\Phi_{\text{Fwd}} = \Phi_{\text{Core}} \quad \text{(continuity)}
$$

and that is the **only** junction condition. The first-order zone has no second-order term, so there is no flux to match; the zero-order zone has no derivative term at all. The membrane between any zone and the Core zone is a **pure continuity interface** — no flux jump, no geometric source, just $\Phi$ matching on both sides.

The Core-to-zone membranes are the simplest interfaces in the ICHTB. They are the "transparent walls" of the box — the field passes in and out of the Core zone without any flux discontinuity, simply inheriting the dynamics of whichever non-Core zone it enters.

---

## The Sign Table: Which Junctions Amplify, Which Damp?

The sign of the operator at each zone determines whether the membrane junction is **amplifying** (positive flux jump, field grows at the interface) or **damping** (negative flux jump, field shrinks).

Define the **junction sign** $s_{\alpha\beta}$ as the sign of $(\mathcal{O}_\alpha - \mathcal{O}_\beta)$ at the interface:

| Membrane | $s_{\alpha\beta}$ | Physical effect |
|----------|-------------------|-----------------|
| Forward / Expansion (+X / +Y) | $+1$ | Amplifying: bloom reinforces signal |
| Forward / Memory (+X / −Y) | $-1$ | Damping: circulation drains directional signal |
| Expansion / Apex (+Y / +Z) | $+1$ | Amplifying: bloom reinforces temporal growth |
| Expansion / Core (+Y / −Z) | $-1$ | Damping: bloom drains toward vacuum |
| Apex / Compression (+Z / −X) | $-1$ | Damping: temporal growth meets compression |
| Compression / Memory (−X / −Y) | $0$ | Neutral: both negative operators, saddle junction |
| Compression / Core (−X / −Z) | $-1$ | Strongly damping: double negative |
| Memory / Core (−Y / −Z) | $-1$ | Damping: circulation drains to vacuum |

The pattern: junctions between positive-sign zones (Forward, Expansion, Apex) are amplifying — they reinforce each other at the interface. Junctions between positive and negative zones are damping. Junctions between two negative zones are neutral or strongly damping.

The **most amplifying path** through the ICHTB follows the sequence Forward → Expansion → Apex → (loop) — the three positive-operator zones, connected at three amplifying membranes. This is the A-state excitation cycle: the three positive zones boost each other at every crossing, creating self-reinforcing field growth. This is the geometric mechanism behind bloom dynamics (2.A states) and the Apex acceleration effect (1.A fast signals).

The **most damping path** is Compression → Core — connected at the most negative junction. This is where B-state excitations eventually decay if they lose energy — the Compression → Core path is the drain, returning field energy to the pre-emergence vacuum.

