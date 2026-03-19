# Appendix D: Hat-Counting Navigation System — Complete Algorithm

This appendix is the complete reference for the hat-counting address system: definitions, encoding rules, the forward algorithm (address → coordinates), the inverse algorithm (field → address), parity structure, the zone navigation graph, bloom-to-address correspondence, and the zone activation map. For derivations see Chapter 4; for zone operators see Appendix B.

---

## D.1 The Address System

### Definition

Every point $\mathbf{x}$ in the ICHTB is assigned a **hat-counting address** — a finite or infinite sequence of zone labels that encodes its location relative to i₀ via the sequence of zone decisions required to reach it from the center.

$$
\mathbf{a} = (a_1,\, a_2,\, \ldots,\, a_n), \qquad a_k \in \{+Z,\,-Z,\,+X,\,-X,\,+Y,\,-Y\}
\tag{D.1}
$$

Numerically abbreviate the six zone labels as:

| Label | Zone | Operator | Numeric |
|-------|------|----------|---------|
| $+Z$ | Apex | $\partial_t\Phi$ | 1 |
| $-Z$ | Core | $\mathbf{1}$ | 2 |
| $+X$ | Forward | $\nabla_x\Phi$ | 3 |
| $-X$ | Compression | $-\nabla^2\Phi$ | 4 |
| $+Y$ | Expansion | $+\nabla^2\Phi$ | 5 |
| $-Y$ | Memory | $\nabla\times$ | 6 |

The **opposite zone** of zone $k$ (the zone on the anti-parallel axis) is denoted $\bar{k}$: $\overline{+Z}=-Z$, $\overline{+X}=-X$, $\overline{+Y}=-Y$, and vice versa.

### Level Structure

**Level 0:** The empty address $()$ — i₀ itself. All zone operators simultaneously degenerate. $A(i_0) \to 0$.

**Level 1:** Address $(k)$ — the entire pyramid $P_k$. Six addresses total.

**Level $n$:** Address $(a_1,\ldots,a_n)$ — a sub-region at depth $n$. Total addresses at level $n$: $6^n$.

**The zone tree:** The full address system forms a regular $6$-ary tree — the **zone tree** of the ICHTB. Every finite address is a node; every infinite address is a leaf (a single point).

### What the Address Encodes

| Component | How to read it |
|-----------|----------------|
| Zone hierarchy | $a_1$ = coarsest zone (outermost); $a_n$ = finest (innermost near i₀) |
| Membrane crossings | Consecutive $a_k \neq a_{k+1}$ = membrane crossed at level $k$ |
| Emergence depth | Count of distinct zone labels in $\mathbf{a}$ (ignoring repeats) |
| Topological environment | Patterns near spoke edges or cube-vertex junctions readable directly |
| Excitation class | Address pattern (see §D.6) identifies 1.A through 3.B |

### Spatial Precision

| Depth $n$ | Spatial resolution | Addresses |
|-----------|-------------------|-----------|
| 1 | $L/2$ | 6 |
| 2 | $L/4$ | 36 |
| 3 | $L/8$ | 216 |
| 10 | $L/1024$ | $\approx 6\times10^7$ |
| 20 | $L/10^6$ | $\approx 3.7\times10^{15}$ |
| 52 | $\sim$ Planck (for $L = 1$ m) | $\approx 10^{40}$ |

---

## D.2 Forward Algorithm: Address → Coordinates

Given a depth-$n$ address $(a_1,\ldots,a_n)$, the representative coordinate is:

$$
\mathbf{x}\big|_{(a_1,\ldots,a_n)} = \sum_{k=1}^{n} \frac{1}{2^k}\,\mathbf{R}_{a_1\cdots a_{k-1}}\,\hat{n}_{a_k}
\tag{D.2}
$$

where $\hat{n}_{a_k}$ is the unit normal of zone $a_k$ and $\mathbf{R}_{a_1\cdots a_{k-1}}$ is the rotation aligning the sub-ICHTB's $z$-axis with the $(k-1)$-th level zone normal. This is a convergent base-6 fractional expansion; the exact coordinate is recovered as $n \to \infty$.

**Level-1 explicit coordinates:**

| Address | Zone | Center $\mathbf{f}_k$ |
|---------|------|----------------------|
| $(+Z)$ | Apex | $(0,\, 0,\, +\tfrac{1}{2})$ |
| $(-Z)$ | Core | $(0,\, 0,\, -\tfrac{1}{2})$ |
| $(+X)$ | Forward | $(+\tfrac{1}{2},\, 0,\, 0)$ |
| $(-X)$ | Compression | $(-\tfrac{1}{2},\, 0,\, 0)$ |
| $(+Y)$ | Expansion | $(0,\, +\tfrac{1}{2},\, 0)$ |
| $(-Y)$ | Memory | $(0,\, -\tfrac{1}{2},\, 0)$ |

---

## D.3 Inverse Algorithm: Coordinates → Address

Given a point $\mathbf{x} \in \text{ICHTB}$, compute the address to depth $n$:

```
PROCEDURE HatAddress(x, n):
  address = []
  center = i₀ = (0,0,0)
  scale = 1

  FOR k = 1 TO n:
    // Find the zone containing x relative to current center
    // Zone criterion: maximum |dot(x - center, n̂_j)| over six zone normals
    scores = { j : |dot(x - center, n̂_j)| for j in 1..6 }
    a_k = argmax(scores)

    // Append zone to address
    address.append(a_k)

    // Descend: new center is the face-center of chosen zone
    center = center + (scale/2) * n̂_{a_k}
    scale  = scale / 2

  RETURN address
```

**Explicit zone criterion at each level:** Point $\mathbf{x}$ is in zone $k$ relative to current center $\mathbf{c}$ iff:

$$
k = \arg\max_{j} \left|(\mathbf{x} - \mathbf{c}) \cdot \hat{n}_j\right|
\tag{D.3}
$$

with ties resolved in favor of the zone with lower index (tie occurs only on membrane boundaries, which have two valid addresses).

---

## D.4 Parity Structure (Even/Odd Lattice)

### Definition

The **zone parity** of address $\mathbf{a} = (a_1,\ldots,a_n)$:

$$
p(\mathbf{a}) = \left(\sum_{k=1}^{n} s(a_k)\right) \bmod 2
\tag{D.4}
$$

where $s(a_k) = 0$ for positive-axis zones ($+Z,+X,+Y$) and $s(a_k) = 1$ for negative-axis zones ($-Z,-X,-Y$).

Address is **even** if $p = 0$, **odd** if $p = 1$.

### Level-Parity Table

| Level $n$ | Parity | Sublattice |
|-----------|--------|-----------|
| 0 (i₀) | even | $\mathcal{L}_\text{even}$ |
| 1 | odd | $\mathcal{L}_\text{odd}$ |
| 2 | even | $\mathcal{L}_\text{even}$ |
| $n$ | even if $n$ even, odd if $n$ odd | alternates |

### Physical Consequences

| Parity class | Operator type | Field character | Analogy |
|-------------|--------------|----------------|---------|
| Even ($p=0$) | Parity-even: $\nabla^2$, $\mathbf{1}$ | Scalar-like | Boson-like |
| Odd ($p=1$) | Parity-odd: $\nabla$, $\nabla\times$ | Vector-like | Fermion-like |

Every membrane triangle $\Delta_k$ separates two odd-sublattice zones (both Level-1). The membrane occupies the midpoint of the even–odd bond, making $\sigma_k(\mathbf{x}) = -\sigma_k(R_k\mathbf{x})$ (odd under zone-swapping reflection). This antisymmetry immediately implies the membrane energy conservation:
$$
\sum_{k=1}^{12}\dot{E}_k = 0
\tag{D.5}
$$

**Position/momentum duality:** Amplitude $A$ lives on the even sublattice; phase gradient $\nabla\theta$ lives on the odd sublattice. These are conjugate variables — the geometric origin of the Heisenberg uncertainty relation $\Delta A \cdot \Delta(\nabla\theta) \geq \tfrac{1}{2}$.

---

## D.5 Zone Navigation Graph

The zone navigation graph encodes which zone-to-zone transitions are possible at each step (which zones share a membrane):

### Adjacency Table

| Zone | Adjacent zones (share a membrane) | NOT adjacent |
|------|------------------------------------|-------------|
| Apex (+Z) | Forward, Compression, Expansion, Memory | Core (−Z) |
| Core (−Z) | Forward, Compression, Expansion, Memory | Apex (+Z) |
| Forward (+X) | Apex, Core, Expansion, Memory | Compression (−X) |
| Compression (−X) | Apex, Core, Expansion, Memory | Forward (+X) |
| Expansion (+Y) | Apex, Core, Forward, Compression | Memory (−Y) |
| Memory (−Y) | Apex, Core, Forward, Compression | Expansion (+Y) |

**Key property:** Opposite zones ($+Z/-Z$, $+X/-X$, $+Y/-Y$) are **never adjacent** — they do not share a membrane. Travelling from a zone to its opposite requires a minimum of **2 hops** through an intermediate zone.

### Graph Distances

| From | To | Minimum hops | Example path |
|------|----|-------------|--------------|
| Any zone | Same zone | 0 (self-loop) | — |
| Any zone | Any adjacent zone | 1 | direct crossing |
| Any zone | Opposite zone | 2 | via any shared neighbor |
| i₀ | Any 3.B configuration | ≥ 6 | must visit all 6 zones |

**Diameter** of the navigation graph: 2 (every pair of distinct zones is at most 2 hops apart).

### Zone Transition Energy Costs

At each membrane crossing from zone $\alpha$ to adjacent zone $\beta$, the energy cost is:

$$
\Delta E_{\alpha\to\beta} = D\int_{\Delta_{\alpha\beta}} \left(\mathcal{M}^{ij}_\beta - \mathcal{M}^{ij}_\alpha\right) n_i\partial_j\Phi\cdot\Phi^*\, d^2S
\tag{D.6}
$$

Crossings along the amplifying membranes (junction sign $s_{\alpha\beta} = +1$, see Appendix B §B.6) have $\Delta E < 0$ (spontaneous). Crossings along damping membranes ($s_{\alpha\beta} = -1$) have $\Delta E > 0$ (require energy input).

---

## D.6 Bloom-to-Address Correspondence

Every excitation class has a characteristic address pattern:

### 1.A — Linear Traveling Wave

**Address pattern:** Single zone, depth 1–2; same zone repeated.

$$
\mathbf{a}_{1.A} = (+X), \text{ or } (+X,\,+X), \text{ etc.}
$$

**Diagnostic:** The depth-1 zone is identical at all points along the bloom axis. Translational symmetry along the propagation direction means the address doesn't change as you slide along $\hat{x}$ — only as you move transversely. All energy in one zone: $f_{+X} \approx 1$.

---

### 1.B — Soliton

**Address pattern:** Alternating Forward / Compression.

$$
\mathbf{a}_{1.B} = (+X,\,-X,\,+X,\,-X,\,\ldots)
$$

**Diagnostic:** Alternating $+X/-X$ at successive depths. Length of alternating subsequence = nonlinearity depth. More alternations → tighter, more nonlinear soliton. Energy split: $f_{+X} \approx f_{-X} \approx \tfrac{1}{2}$.

---

### 2.A — Linear Disc / Bessel Mode

**Address pattern:** Two adjacent zones at depth 1; consistent zone at depth 2.

$$
\mathbf{a}_{2.A} = (+Y,\,-Y) \text{ or } (+X,\,+Y), \text{ etc.}
$$

**Diagnostic:** Two distinct zones at depth 1, spanning a 2D plane. The pair of depth-1 zones defines the plane of the disc. Energy in three mutually adjacent zones.

---

### 2.B — Vortex Sheet

**Address pattern:** Memory zone dominant at depth 1; angular winding in depth-2+ sequence.

$$
\mathbf{a}_{2.B} = (-Y,\, [+Z \to +X \to -Z \to -X \to\cdots])
$$

**Diagnostic:** $-Y$ at depth 1. Depth-2 address cycles through all four zones adjacent to Memory exactly $|n|$ times as you trace a closed loop around the vortex axis — the winding number $n$ is directly readable from the address cycle count.

---

### 3.A — Spherical Standing Mode

**Address pattern:** All six zones present at depth 1; depth-2 follows zone-adjacency selection rules.

**Diagnostic:** All 6 zones in the depth-1 pattern. The depth-2 transitions obey the adjacency graph (§D.5) — only adjacent zone pairs appear at consecutive levels. The angular quantum numbers $(\ell,m)$ determine which zone pairs dominate at depth 2.

---

### 3.B — Topological Knot (Hopfion)

**Address pattern:** All six zones at depth 1; depth-2 through depth-$n$ form a closed cycle visiting all zones.

**Diagnostic:** Closed zone trajectory in the depth-2+ sequence. Reading the depth-$k$ address as you trace any loop around the excitation center, the zone sequence cycles through all six zones exactly $|H|$ times. The Hopf invariant $H$ equals this cycle count — directly readable from the address without converting to coordinates.

$$
H = \text{(winding number of depth-2 zone sequence around any enclosing loop)}
\tag{D.7}
$$

The address is **topologically irreducible**: no cyclic reordering or deletion of adjacent identical labels can shorten it. This irreducibility is the address-space definition of topological protection.

---

### Address Summary Table

| Class | Depth | Zone pattern | $f_k$ on $\Delta^5$ | Topological invariant |
|-------|-------|-------------|---------------------|-----------------------|
| 1.A | 1–2 | Single zone repeated | Vertex: $(1,0,0,0,0,0)$ | None |
| 1.B | 2+ | $+X/-X$ alternating | Edge: $(f,0,f,0,0,0)$ | None |
| 2.A | 2 | Two adjacent zones | Face: $(0,f,f,f,0,0)$ | None |
| 2.B | 3+ | $-Y$ + winding cycle | Face: $(0,f,0,f,f,0)$ | Winding number $n$ |
| 3.A | 3+ | All 6 at depth 1 | Interior: $\propto|Y_\ell^m|^2$ | None |
| 3.B | 6+ | All 6, closed cycle | Interior: $(\tfrac{1}{6},\ldots,\tfrac{1}{6})$ | Hopf invariant $H$ |

---

## D.7 Zone Activation Map

For any field $\Phi(\mathbf{x})$, the **zone activation fraction** of zone $k$:

$$
f_k = \frac{E_k}{E_\text{total}}, \qquad E_k = \int_{P_k}\left[D\mathcal{M}^{ij}_k\partial_i\Phi^*\partial_j\Phi + \kappa|\Phi|^2 - \frac{\gamma}{2}|\Phi|^4\right]d^3x
\tag{D.8}
$$

The vector $(f_{+Z}, f_{-Z}, f_{+X}, f_{-X}, f_{+Y}, f_{-Y})$ is a point on the 5-simplex $\Delta^5$ (six non-negative numbers summing to $\approx 1$, with a small membrane correction $f_\text{membrane} \ll 1$).

**Reading the simplex position:**
- **Vertex of $\Delta^5$:** all energy in one zone → 1.A
- **Edge of $\Delta^5$:** energy split between two zones → 1.B (opposite zone pair)
- **Face of $\Delta^5$:** energy in three zones → 2.A, 2.B
- **Interior near vertex:** unequal multi-zone → 3.A
- **Interior near centroid** $(f_k \approx \tfrac{1}{6}$ for all $k)$: → **3.B** — the most democratic excitation, no preferred zone

The 3.B state's equal energy distribution explains its maximal persistence: no zone is dominant, so no single-zone perturbation can disrupt it. Destroying a 3.B state requires simultaneously reducing energy in all six zones — an entropically suppressed, energetically expensive coordinated perturbation.

---

## D.8 The Selection Number in Address Terms

The CTS selection number $S = R/(\dot{R}\,t_\text{ref})$ has a natural hat-counting interpretation:

$$
S \approx \frac{L_\text{hat}}{\ell_\text{transition}} = \frac{L \cdot 2^{-n}}{\xi}
\tag{D.9}
$$

where $L_\text{hat} \sim L \cdot 2^{-n}$ is the spatial scale of the depth-$n$ address and $\xi = \sqrt{D/\kappa}$ is the membrane coherence length (ZEZ thickness).

$S$ measures how many coherence lengths fit inside the addressed region — equivalently, how many hat-levels of structure are above the membrane resolution scale.

| Address depth $n$ | $S$ | Excitation | Persistence |
|-------------------|-----|-----------|-------------|
| 1–2 | Low | 1.A, 1.B | Transient |
| 3–4 | Medium | 2.A, 2.B | Moderate |
| 5–6 | High | 3.A, 3.B | Maximum |

Depth and $S$ increase together: deeper addresses → more membrane crossings required to destroy the structure → higher persistence.

---

## D.9 Measurement Protocol: Identifying Excitation Class

Given an observed field configuration $\Phi(\mathbf{x})$, the following three-step protocol identifies its class without coordinate reconstruction:

**Step 1 — Measure zone activation fractions $\{f_k\}$:**
Compute $E_k$ via (D.8) for each zone. Locate the point $(f_1,\ldots,f_6)$ on $\Delta^5$. This identifies the rough class (1.A through 3.B) via §D.7.

**Step 2 — Measure depth-2 address pattern at multiple points:**
Apply the inverse algorithm (§D.3) at points sampled across the excitation. Identify which zone pairs appear at depth 2. This specifies spatial structure within the identified class (propagation direction for 1.A; disc plane for 2.A; vortex axis for 2.B).

**Step 3 — Measure zone trajectory under a closed loop:**
Trace a closed path encircling the excitation center. Record the depth-2 zone label at each point. Count complete cycles through all zones:
- For 2.B: winding number $n$ = number of times depth-2 cycles through Memory's four adjacent zones
- For 3.B: Hopf invariant $H$ = number of complete 6-zone cycles (D.7)

Steps 1–3 constitute a **complete, non-redundant classification** of any CTS excitation. The hat-counting address is the ICHTB's native coordinate system — the one in which physics is most transparent.

---

## D.10 Connections to Prior Mathematics

| System | Connection to hat counting |
|--------|---------------------------|
| **Base-6 numeration** | Address = base-6 fractional expansion of position (D.2) |
| **Voronoi diagrams** | Zone at each level = Voronoi cell of face-center generators (§3.3) |
| **Wavelet decomposition** | Address system = multi-scale zone-aware wavelet basis; zone operators are the mother wavelets (Grossmann & Morlet 1984; Mallat 1989) |
| **Bipartite (checkerboard) lattice** | Even/odd sublattice = $\mathcal{L}_\text{even}/\mathcal{L}_\text{odd}$ (§D.4) |
| **Wigner-Seitz / Brillouin zones** | Zone boundaries ↔ Brillouin zone faces; membrane ↔ Bragg reflection planes |
| **Fundamental group** | 3.B address irreducibility = non-trivial element of $\pi_1$ of zone adjacency graph |
| **Iterated function systems** | Zone tree = IFS attractor under six contractions $\mathbf{x} \mapsto \mathbf{f}_k + \tfrac{1}{2}(\mathbf{x} - \mathbf{f}_k)$ |

The hat-counting address is also the natural setting for the **CTS renormalization group**: integrating out the finest-scale zones (largest $n$) and renormalizing the remaining coarser-scale structure is precisely the wavelet-basis RG used in condensed matter physics (Wilson 1971; White DMRG 1992). The zone tree is the CTS's built-in RG decimation structure.

---

*See also: Appendix B (Zone operators), Appendix C (Membrane mathematics), Appendix E (Excitation Ledger with ICHTB addresses), Chapter 4 (Hat counting), Chapter 3 (Six zones).*
