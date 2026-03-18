# 4.2 Odd vs Even Lattice

## Parity in the Zone Tree

Every address $(a_1, a_2, \ldots, a_n)$ in the ICHTB zone tree has a natural **parity** — a binary classification that carries structural information about the location's relationship to the membrane network.

Define the **zone parity** of address $\mathbf{a}$ as:

$$
p(\mathbf{a}) = \left(\sum_{k=1}^{n} s(a_k)\right) \mod 2
$$

where $s(a_k)$ is the **sign** of the $k$-th zone label: $+1$ for positive-axis zones ($+X, +Y, +Z$, labels 1, 3, 5) and $-1 \equiv 1$ for negative-axis zones ($-X, -Y, -Z$, labels 2, 4, 6). So:

$$
s(a_k) = \begin{cases} 0 & \text{if } a_k \in \{+Z, +X, +Y\} \\ 1 & \text{if } a_k \in \{-Z, -X, -Y\} \end{cases}
$$

An address is **even** if $p(\mathbf{a}) = 0$ and **odd** if $p(\mathbf{a}) = 1$.

---

## Why Parity Matters: The Bipartite Structure

The ICHTB zone structure partitions into two classes based on this parity, and the parity determines something physical: **whether two adjacent zones are on the same side or opposite sides of the fundamental CTS operator pairs**.

The three operator pairs in the CTS are:
- **Forward / Compression**: $+\nabla$ vs $-\nabla^2$ — opposite operators along the X axis
- **Expansion / Memory**: $+\nabla^2$ vs $\nabla\times$ — opposing tendencies along the Y axis
- **Apex / Core**: $\partial_t$ vs $\mathbf{1}$ — evolution vs. anchor along the Z axis

Adjacent zones in the same **parity class** share a membrane between two zones of the **same operator type** (both gradient, both Laplacian, or both temporal). Adjacent zones in **opposite parity classes** share a membrane between two zones of **opposite operator types** — the most energetically active membrane interface, where the flux jump $\sigma_k$ is largest.

This is the physical content of the parity: it classifies zone boundaries by their energetic activity. Even-to-odd crossings are high-activity interfaces (large $\sigma_k$, strong zone exchange). Even-to-even or odd-to-odd crossings (which occur only along the spoke edges and cube vertex junctions from Chapter 2) are lower-activity interfaces.

---

## The 3D Checkerboard

The parity structure of the ICHTB zone tree maps onto the familiar 3D checkerboard (bipartite cubic lattice). Consider the simple cubic lattice $\mathbb{Z}^3$ — integer triples $(i, j, k)$. Color a lattice site **even** (white) if $i + j + k$ is even, **odd** (black) if $i + j + k$ is odd.

This coloring has the property that every nearest neighbor of an even site is odd, and vice versa. The lattice splits into two interlocking sublattices $\mathcal{L}_{\text{even}}$ and $\mathcal{L}_{\text{odd}}$, neither of which contains two adjacent sites.

Now map the ICHTB zone addresses to cubic lattice sites:

- **Level 1 address** $(a_1)$: maps to six nearest-neighbor sites of the origin. The three positive-axis zones map to $(+1,0,0)$, $(0,+1,0)$, $(0,0,+1)$ (even, since each coordinate sum is 1 — odd, wait...

Let me be precise. In the cubic lattice with origin $(0,0,0)$ (which is even), the six nearest neighbors are $(\pm1, 0, 0)$, $(0, \pm1, 0)$, $(0, 0, \pm1)$ — all with coordinate sum $\pm 1$, which is **odd**. So all six Level-1 zone positions are odd lattice sites.

- **Level 2 addresses** $(a_1, a_2)$: 36 locations. These correspond to the 12 next-nearest-neighbor sites of the cubic lattice at distance $\sqrt{2}$ (if $a_2 \neq \bar{a}_1$, the opposite of $a_1$) or the 6 second-nearest sites at distance 2 (if $a_2 = a_1$, staying in the same zone). The coordinate sum of a level-2 address is $\pm 2$ or $0$ — all **even**. So Level-2 positions are even lattice sites.

The pattern:
- **Odd levels** ($n = 1, 3, 5, \ldots$): positions are on the odd sublattice $\mathcal{L}_{\text{odd}}$
- **Even levels** ($n = 0, 2, 4, \ldots$): positions are on the even sublattice $\mathcal{L}_{\text{even}}$

The ICHTB zone tree navigates alternately between the two sublattices at each level — the 3D checkerboard emerges from the recursive zone-decision structure.

---

## Physical Consequences of Parity

### Fermion-like vs Boson-like Behavior

The even/odd sublattice distinction has a direct analog in quantum field theory: the **fermion/boson distinction** based on spin and the spin-statistics theorem.

Fields on the even sublattice (even-level addresses) couple to their neighbors via operators with **even symmetry** under space reflection — the Laplacian $\nabla^2$ is parity-even ($\nabla^2 \to \nabla^2$ under $\mathbf{x} \to -\mathbf{x}$), as is the identity operator. The Core (−Z) and Apex (+Z) zones are parity-even (they map to themselves under reflection in the $z$-axis if we identify $+Z$ and $-Z$ as paired).

Fields on the odd sublattice (odd-level addresses) couple to neighbors via operators with **odd symmetry** — the gradient $\nabla$ is parity-odd ($\nabla \to -\nabla$ under $\mathbf{x} \to -\mathbf{x}$), as is the curl $\nabla\times$.

This means:
- **Even sublattice**: field excitations are scalar-like or tensor-like (invariant or covariant under parity). These are **boson-like** — spin-0 or spin-2.
- **Odd sublattice**: field excitations are vector-like or pseudovector-like (change sign or acquire extra factor under parity). These are **fermion-like** — spin-$\frac{1}{2}$ or spin-1.

The parity alternation of the zone tree is the CTS origin of the fermion/boson distinction: it is not a separate postulate but a consequence of the alternating operator types at successive levels of the zone tree.

### The Membrane is Always an Even-to-Odd Interface

Every membrane triangle $\Delta_k$ separates two adjacent zones at Level 1. Level-1 zones are all odd-sublattice positions. Two odd positions separated by a membrane... but the membrane itself is reached by a half-step from i₀ (an even-sublattice point). The membrane sits exactly on the even sublattice boundary between two odd sites — it occupies the midpoint of a nearest-neighbor bond, which is a face of the Wigner-Seitz cell.

This is the geometric reason that the membrane source term $\sigma_k$ (the flux discontinuity at the membrane) is odd under the spatial reflection that swaps the two zones: $\sigma_k(\mathbf{x}) = -\sigma_k(R_k\mathbf{x})$ where $R_k$ is the reflection in the membrane plane. Odd functions have zero integral over symmetric domains — which immediately gives the membrane energy conservation constraint:

$$
\sum_{k=1}^{12} \dot{E}_k = 0
$$

derived in section 2.4. This is not an independent constraint — it follows from the parity of the membrane source term, which follows from the odd-sublattice character of the zone positions.

---

## The Odd Lattice as the Momentum Space of the ICHTB

In crystallography, the reciprocal lattice of the even sublattice is the odd sublattice, and vice versa. The even sublattice positions (Levels 0, 2, 4, ...) carry the **amplitude information** ($A$ values, energy densities, scalar field values). The odd sublattice positions (Levels 1, 3, 5, ...) carry the **phase information** ($\nabla\theta$ values, current densities, vector field values).

This is the CTS version of the **position/momentum duality**: amplitude lives on the even lattice, phase gradient lives on the odd lattice. The Heisenberg uncertainty principle $\Delta A \cdot \Delta(\nabla\theta) \geq \frac{1}{2}|[\hat{A}, \widehat{\nabla\theta}]|$ has its geometric origin in the fact that amplitude and phase gradient are on dual sublattices — they cannot be simultaneously specified with arbitrary precision because they live on complementary parts of the zone tree.

This is the CTS derivation of the Heisenberg uncertainty principle from geometry: it is not a fundamental postulate about measurement but a consequence of the bipartite structure of the ICHTB zone tree. Amplitude and phase are on opposite sublattices, and opposite sublattice quantities are conjugate variables in the Fourier sense.

