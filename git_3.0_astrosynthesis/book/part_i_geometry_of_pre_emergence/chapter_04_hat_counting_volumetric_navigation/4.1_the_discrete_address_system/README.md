# 4.1 The Discrete Address System

## The Navigation Problem

The ICHTB is a continuous volume. Any point $\mathbf{x}$ in the cube has real-valued coordinates $(x, y, z)$. But the physical meaning of a location in the ICHTB is not determined by its coordinates alone — it is determined by its **relationship to i₀**, specifically by the path of zone crossings required to reach it from the center.

Two points with different coordinates but the same zone membership have qualitatively identical field dynamics — they are governed by the same dominant operator. Two points that are geometrically adjacent but on opposite sides of a membrane are governed by entirely different operators. The coordinate system $(x, y, z)$ does not carry this information efficiently; it treats the membrane boundaries as unremarkable surfaces, no different from any other level set.

A navigation system designed for the ICHTB should do the opposite: it should make the zone structure primary and the coordinate position secondary. Such a system assigns each location in the ICHTB a **discrete address** based on the sequence of zone decisions required to reach it from i₀. This is **hat counting** — a recursive, zone-aware labeling of the ICHTB volume.

---

## The Recursive Zone Subdivision

The ICHTB structure is self-similar: if you place a new i₀ at any point inside a zone, that point sits at the center of its own local ICHTB, which inherits the zone structure of the parent ICHTB at a finer scale. This recursive property allows the entire ICHTB volume to be addressed to arbitrary precision by a sequence of zone labels — a **zone tree**.

**Level 0**: The single ICHTB volume. Address: $()$ — the empty address, representing "all of the ICHTB." This is i₀ itself.

**Level 1**: Choose one of the six zones. This divides the ICHTB into six regions. The address of a region is a single zone label: one of $\{+Z, -Z, +X, -X, +Y, -Y\}$, which we can abbreviate numerically as $\{1, 2, 3, 4, 5, 6\}$.

So the address $(3)$ means "the region corresponding to zone +X" — the entire Forward pyramid.

**Level 2**: Within each Level-1 region, subdivide again. The sub-ICHTB inside the Forward pyramid ($+X$ zone) has its own six sub-zones. Address $(3, 2)$ means "within the Forward zone, the sub-region corresponding to sub-zone $-Z$ (Core)."

**Level $n$**: The address is a sequence of $n$ zone labels:

$$
\mathbf{a} = (a_1, a_2, \ldots, a_n), \qquad a_k \in \{1, 2, 3, 4, 5, 6\}
$$

This is a **base-6 numeral** of length $n$. The full system of addresses is a base-6 **tree** — the **zone tree** of the ICHTB.

---

## What the Address Encodes

An address $\mathbf{a} = (a_1, a_2, \ldots, a_n)$ encodes:

1. **The zone hierarchy**: $a_1$ is the coarsest zone (the Level-1 zone), $a_n$ is the finest. Reading left to right is reading from the outside in — from the face of the cube to the vicinity of i₀.

2. **The membrane crossing history**: Consecutive elements $a_k, a_{k+1}$ that are **different zones** signal that the path to this address crosses a membrane at Level $k$. Consecutive elements that are the **same zone** signal a path that stays within one zone at Level $k$.

3. **The topological charge environment**: Certain address patterns correspond to locations near membrane edges (Type 1 junctions) or cube vertex points (Type 2 junctions). These can be read directly from the address without converting back to coordinates.

4. **The zone depth**: The number of distinct zone labels in $\mathbf{a}$ (ignoring repeats) counts how many zone transitions the field at this location has undergone on its path from i₀. This is the **emergence depth** — a single integer that summarizes how far along the 1.A → 3.B emergence sequence the field at this address has traveled.

---

## From Address to Coordinates

The mapping from address to coordinates is explicit. For a unit ICHTB:

**Level-1 address $(k)$** maps to the pyramid $P_k$. The zone face center $\mathbf{f}_k$ is the midpoint of the addressed region:

$$
\mathbf{x}\big|_{(k)} \approx \mathbf{f}_k = (\pm\tfrac{1}{2}, 0, 0), \; (0, \pm\tfrac{1}{2}, 0), \; \text{or } (0, 0, \pm\tfrac{1}{2})
$$

**Level-2 address $(k, j)$** maps to a sub-pyramid inside $P_k$. The sub-ICHTB inside $P_k$ has its own center at $\mathbf{f}_k$ and faces toward the six sub-directions relative to $\mathbf{f}_k$. The Level-2 address maps to a sub-region centered approximately at:

$$
\mathbf{x}\big|_{(k,j)} \approx \mathbf{f}_k + \frac{1}{2}\mathbf{R}_k\,\hat{n}_j
$$

where $\mathbf{R}_k$ is the rotation matrix that aligns the sub-ICHTB z-axis with the $k$-th zone normal direction.

**General level-$n$ address**: The coordinate is the result of $n$ successive zone-center steps, each at half the scale of the previous:

$$
\mathbf{x}\big|_{(a_1, \ldots, a_n)} = \sum_{k=1}^{n} \frac{1}{2^k}\,\mathbf{R}_{a_1 \cdots a_{k-1}}\,\hat{n}_{a_k}
$$

This is a **base-6 fractional expansion** of the position vector — a convergent series that approaches the exact coordinate as $n \to \infty$. Every point in the ICHTB has a unique infinite-length address (except for points on membrane boundaries, which have two addresses corresponding to the two zones they border).

---

## The Precision of the Address

The address of length $n$ locates a point to within a spatial resolution of $2^{-n}$ (in units of the ICHTB scale $L$). For reference:

| Level $n$ | Spatial resolution | Number of distinct addresses |
|-----------|-------------------|------------------------------|
| 1 | $L/2$ | 6 |
| 2 | $L/4$ | 36 |
| 3 | $L/8$ | 216 |
| 10 | $L/1024 \approx 10^{-3}L$ | $6^{10} \approx 6 \times 10^7$ |
| 20 | $L/10^6$ | $6^{20} \approx 3.7 \times 10^{15}$ |
| 52 | $\sim$ Planck scale (if $L = 1$ m) | $6^{52} \approx 10^{40}$ |

The address system is not merely a navigational convenience. It is a **measurement theory**: to know where something is in the ICHTB is to know the sequence of zone decisions that led to it from i₀. This is the information-theoretic complement to the geometric coordinates — it tells you not just where a thing is, but the story of how it got there from the center.

---

## The Hat Metaphor

The name "hat counting" comes from the visual representation of a level-$n$ address as a sequence of nested hats: each zone decision places a "hat" on the address, and the total number of hats is the depth. The topmost hat is the finest-scale decision ($a_n$, the innermost zone label); the bottommost hat is the coarsest ($a_1$, the outermost zone label).

Reading an address from top to bottom (fine to coarse) is reading the field's history from its most recent zone decision back to its first. Reading bottom to top (coarse to fine) is following the field's journey from i₀ outward to the present location. Both readings are valid; they emphasize different aspects of the same discrete position.

The metaphor also connects to the **hat basis** of combinatorics: in combinatorial problems involving hats (each object wearing a "hat" that encodes its classification), the hat sequence is read from the outside in. In the ICHTB, the hats are zone labels, the objects are spatial locations, and reading the hats gives the zone path from i₀ to the location.

