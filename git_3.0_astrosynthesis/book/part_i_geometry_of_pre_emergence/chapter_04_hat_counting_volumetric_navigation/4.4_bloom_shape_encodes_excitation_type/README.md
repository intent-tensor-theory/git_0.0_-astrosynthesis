# 4.4 Bloom Shape Encodes Excitation Type

## Address and Bloom Are Dual Descriptions

Chapter 3 introduced the bloom shape as the spatial amplitude pattern $A(\mathbf{x})$ of a field excitation — the visible record of which zones have been activated and at what intensity. Chapter 4 has developed the hat-counting address system — the discrete zone-path label encoding where in the ICHTB a field configuration lives.

These two descriptions are **dual to each other**: the bloom shape is the continuous spatial representation of the excitation; the hat address is the discrete zone-path representation. Converting between them is the core technical operation of volumetric navigation in the CTS.

The key result of this section: **every distinct bloom shape corresponds to a characteristic hat-address pattern, and vice versa**. Reading the bloom shape tells you the address; reading the address tells you the bloom shape. They are two languages for the same physical object.

---

## The Address Signature of Each Bloom Class

### 1.A — Linear Traveling Wave

Hat address pattern: **single non-repeating zone, maximum depth 1–2.**

$(+X)$ or $(+X, +X)$ — the Forward zone dominates at all levels. The field concentrates all its activity along the $+\hat{x}$ axis. The bloom is a narrow rod pointing in one direction.

**Address diagnostic:** If the depth-1 zone is the same at all points along the axis of the bloom (all pointing to the same face), the excitation is 1.A. The bloom has translational symmetry along its axis — the address doesn't change as you slide along the propagation direction, only as you move transversely.

### 1.B — Soliton

Hat address pattern: **alternating Forward / Compression zones at increasing depth.**

$(+X, -X, +X, -X, \ldots)$ — the address oscillates between Forward and Compression. The bloom is compact along $\hat{x}$ precisely because the Compression sub-zone at each level "pinches" the Forward expansion back. The alternation between these two operator types (gradient and negative Laplacian) is the discrete signature of the soliton balance.

**Address diagnostic:** Alternating $+X / -X$ pattern in the address. The depth of the longest alternating subsequence measures the soliton's nonlinearity — more alternations = tighter, more nonlinear soliton.

### 2.A — Linear Disc (Bessel Mode)

Hat address pattern: **two distinct zones at depth 1, consistent zone at depth 2.**

$(+Y, -Y)$ or $(+X, +Y)$ — two adjacent zones activated at the first level, creating a 2D bloom. The field has extent in two directions simultaneously. The Bessel function profile arises because the Laplacian in the Expansion zone generates radial modes, and the Memory zone contributes the angular structure.

**Address diagnostic:** Two distinct zones appearing at depth 1, both with the same depth-2 sub-zone. The pair of depth-1 zones spans a 2D plane in the ICHTB — the plane of the disc.

### 2.B — Vortex

Hat address pattern: **Memory zone dominant at depth 1, angular winding encoded in depth-2+ addresses.**

$(-Y, \ldots)$ — the Memory zone at depth 1, with the depth-2 addresses tracing the angular rotation around the $-\hat{y}$ axis. The winding number $n$ of the vortex equals the number of complete cycles in the depth-2 address sequence as you go around the vortex core.

**Address diagnostic:** Memory zone at depth 1; the depth-2 sequence encodes the phase winding. A winding number $n$ vortex has a depth-2 address that cycles through all four zones adjacent to the Memory zone exactly $n$ times as you trace a closed loop around the vortex.

### 3.A — Spherical Standing Mode

Hat address pattern: **all six zones present at depth 1; depth-2 addresses follow spherical harmonic selection rules.**

All six zones activated at depth 1 — the address at depth 1 is a full 6-letter alphabet. The depth-2 pattern follows the coupling rules of the angular momentum quantum numbers $(\ell, m)$: the zone $k$ at depth 2 within zone $j$ at depth 1 is constrained by whether $j \to k$ is an allowed operator coupling (a membrane crossing with nonzero $\sigma_k$).

**Address diagnostic:** All six zones present at depth 1. The depth-2 pattern is not arbitrary — it obeys the zone adjacency graph (section 4.3), reflecting the spherical harmonic structure.

### 3.B — Topological Knot (Hopfion)

Hat address pattern: **all six zones present at depth 1; the depth-2 through depth-$n$ addresses form a closed cycle visiting all zones.**

The 3.B state's defining feature in address space is its **closed zone trajectory**: reading the depth-$k$ address at any fixed depth $k$ as you trace a loop around the excitation center, the address sequence cycles through all six zones exactly $|H|$ times (where $H$ is the Hopf invariant). The address is a "word" over the 6-letter zone alphabet with the property that it is **topologically irreducible** — no cyclic reordering of the letters, no deletion of adjacent identical pairs, can reduce it to a shorter word. This is exactly the definition of a non-trivial element of the fundamental group of the zone adjacency graph.

**Address diagnostic:** Closed zone trajectory of length $6|H|$ in the depth-2+ address sequence. The Hopf invariant $H$ can be read directly from the hat-counting address — it is the winding number of the depth-2 zone sequence.

---

## The Zone Activation Map

For any field configuration $\Phi(\mathbf{x})$, define the **zone activation fraction** $f_k$ as the fraction of the total ICHTB energy residing in zone $k$:

$$
f_k = \frac{E_k}{E_{\text{total}}}, \qquad \sum_{k=1}^{6} f_k = 1 - f_{\text{membrane}}
$$

(The membrane stores a small fraction $f_{\text{membrane}} \ll 1$ of the total energy; to leading order $\sum f_k \approx 1$.)

The zone activation map $(f_{+Z}, f_{-Z}, f_{+X}, f_{-X}, f_{+Y}, f_{-Y})$ is a point on the 5-simplex $\Delta^5$ (the simplex of 6 non-negative numbers summing to 1). Different excitation types occupy characteristic regions of $\Delta^5$:

| Class | Characteristic region of $\Delta^5$ |
|-------|--------------------------------------|
| 1.A | Vertex: nearly all energy in one zone ($(1,0,0,0,0,0)$ or similar) |
| 1.B | Edge: energy split between two opposite zones $(f_k, 0, 0, f_{\bar{k}}, 0, 0)$ |
| 2.A | Face: energy in three mutually adjacent zones |
| 2.B | Face: energy in Memory + two adjacent zones, with vortex topology |
| 3.A | Interior: energy spread across all six zones, weight $\propto |Y_\ell^m|^2$ |
| 3.B | Interior: energy approximately equal across all six zones, $f_k \approx \frac{1}{6}$ |

The most striking entry is the 3.B state: **equal energy distribution across all six zones**. A topological knot excitation in the CTS activates all six zone operators with approximately equal weight — it is the maximally democratic excitation, the one that treats all zones equally and therefore cannot be localized in any one zone.

This explains intuitively why 3.B states are the most persistent: they have no preferred zone, no "home" direction, no axis along which they are vulnerable to a targeted perturbation. To destroy a 3.B state, you would need to simultaneously reduce the energy in all six zones — a coordinated perturbation that is entropically unlikely and energetically expensive.

---

## Hat Counting as a Measurement Protocol

The equivalence between bloom shape and hat address is not merely theoretical — it defines a **measurement protocol**. Given any unknown CTS excitation $\Phi(\mathbf{x})$:

1. **Measure the zone activation fractions** $\{f_k\}$. This identifies the rough excitation class (1.A through 3.B).

2. **Measure the depth-2 address pattern** at multiple points. This identifies the spatial structure within the identified class (which direction for 1.A; which plane for 2.A; which vortex axis for 2.B).

3. **Measure the zone trajectory under a closed loop** around the excitation center. This identifies the topological invariants (winding number $n$ for 2.B; Hopf invariant $H$ for 3.B).

Steps 1–3 together constitute a **complete classification of any CTS excitation** using only hat-counting measurements — no coordinate reconstruction required. The hat-counting system is a complete, non-redundant basis for CTS field classification.

This is the volumetric navigation promise delivered: any point in the ICHTB field space has a unique, physically meaningful address that encodes its excitation type, its zone history, its topological charges, and its persistence. The hat-counting address is the ICHTB's native coordinate system — the one in which the physics is most transparent.

