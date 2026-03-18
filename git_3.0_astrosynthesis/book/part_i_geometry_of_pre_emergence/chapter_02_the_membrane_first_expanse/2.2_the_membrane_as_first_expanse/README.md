# 2.2 The Membrane as First Expanse

## From Point to Surface: The First Dimensional Transition

i₀ is zero-dimensional: a point. The first geometric object that can extend from a point while maintaining contact with it is a **line**. The first object that can enclose a region while anchored at a point is a **surface**. The membrane is this surface — the first two-dimensional extent of the CTS field from its imaginary anchor.

The transition from zero-dimensional (i₀) to two-dimensional (membrane) is not mediated by a one-dimensional intermediate. There are no "spokes" connecting i₀ to the cube's edges independently of the membrane triangles. The membrane **is** the collection of triangular planes that simultaneously:

1. Connect i₀ to each of the 12 cube edges
2. Partition the surrounding 3D volume into 6 distinguishable zones
3. Carry the boundary conditions that govern field continuity and flux across zone interfaces

This is the first **expanse** — the first time the CTS field has geometric extent rather than being localized at a point.

---

## The 12 Membrane Triangles: Explicit Geometry

For a unit cube centered at the origin with vertices at $(\pm\frac{1}{2}, \pm\frac{1}{2}, \pm\frac{1}{2})$ and i₀ at the center $(0, 0, 0)$:

The 12 edges of the cube connect adjacent corner vertices. Label the corners $C_k$ for $k = 1, \ldots, 8$. The 12 edges are:

| Edge | Shared by zones | Membrane normal direction |
|------|----------------|--------------------------|
| $C_1C_2$: top-front edge | +Z (Apex) ∩ +X (Forward) | $\hat{n} \parallel \hat{x} + \hat{z}$ |
| $C_2C_3$: top-right edge | +Z (Apex) ∩ +Y (Expansion) | $\hat{n} \parallel \hat{y} + \hat{z}$ |
| $C_3C_4$: top-back edge | +Z (Apex) ∩ −X (Compression) | $\hat{n} \parallel -\hat{x} + \hat{z}$ |
| $C_4C_1$: top-left edge | +Z (Apex) ∩ −Y (Memory) | $\hat{n} \parallel -\hat{y} + \hat{z}$ |
| $C_5C_6$: bottom-front | −Z (Core) ∩ +X (Forward) | $\hat{n} \parallel \hat{x} - \hat{z}$ |
| $C_6C_7$: bottom-right | −Z (Core) ∩ +Y (Expansion) | $\hat{n} \parallel \hat{y} - \hat{z}$ |
| $C_7C_8$: bottom-back | −Z (Core) ∩ −X (Compression) | $\hat{n} \parallel -\hat{x} - \hat{z}$ |
| $C_8C_5$: bottom-left | −Z (Core) ∩ −Y (Memory) | $\hat{n} \parallel -\hat{y} - \hat{z}$ |
| $C_1C_5$: front-right | +X (Forward) ∩ +Y (Expansion) | $\hat{n} \parallel \hat{x} + \hat{y}$ |
| $C_2C_6$: back-right | +X (Forward) ∩ −Y (Memory) | $\hat{n} \parallel \hat{x} - \hat{y}$ |
| $C_3C_7$: front-left | −X (Compression) ∩ +Y (Expansion) | $\hat{n} \parallel -\hat{x} + \hat{y}$ |
| $C_4C_8$: back-left | −X (Compression) ∩ −Y (Memory) | $\hat{n} \parallel -\hat{x} - \hat{y}$ |

Each membrane triangle $\Delta_k$ is the convex hull of $\{i_0, C_{a}, C_{b}\}$ where $C_a C_b$ is the $k$-th edge. In Cartesian coordinates, the $k$-th membrane plane contains the origin and has unit normal:

$$
\hat{n}_k = \frac{\mathbf{v}_{a} \times \mathbf{v}_{b}}{|\mathbf{v}_{a} \times \mathbf{v}_{b}|}
$$

where $\mathbf{v}_{a}$ and $\mathbf{v}_{b}$ are the position vectors of the two edge vertices.

---

## The Membrane as a 2-Complex

The full membrane $\mathcal{M}$ is the union of all 12 triangular faces:

$$
\mathcal{M} = \bigcup_{k=1}^{12} \Delta_k
$$

This union has the topology of a **2-dimensional simplicial complex** in $\mathbb{R}^3$. Its geometric properties:

- **Total area**: Each triangle has legs of length $\frac{1}{2}$ (from center to face midpoint) and $\frac{\sqrt{2}}{2}$ (half a face diagonal), giving area $\frac{\sqrt{2}}{8}$ per triangle; total membrane area $A_\mathcal{M} = \frac{12\sqrt{2}}{8} = \frac{3\sqrt{2}}{2} \approx 2.12$ for a unit cube.
- **Shared vertex**: All 12 triangles share the single vertex i₀. The link of i₀ in $\mathcal{M}$ is a 1-complex: the 1-skeleton of the cube (12 edges, 8 vertices). 
- **Boundary**: $\partial\mathcal{M} = $ the 12 edges of the cube (each edge is the "outer" boundary of one membrane triangle). The membrane has no inner boundary — i₀ is an interior vertex, not a boundary vertex.
- **Euler characteristic**: $\chi(\mathcal{M}) = V - E + F = 9 - 20 + 12 = 1$ (where $V = 1 + 8 = 9$ includes i₀, $E = 12_{cube} + 12_{spokes} - 4 \times 0 = ?$...) 

Let me be precise: the 2-complex $\mathcal{M}$ has:
- Vertices: i₀ plus 8 cube corners = **9 vertices**
- Edges: 12 spoke edges (i₀ to each corner) + 12 cube edges = **24 edges**
- Faces: 12 membrane triangles

$$
\chi(\mathcal{M}) = 9 - 24 + 12 = -3
$$

This Euler characteristic tells us that the membrane is a non-trivial topological space — it has holes. Specifically, $\chi = -3$ implies $H_0 = \mathbb{Z}$, $H_1 = \mathbb{Z}^4$ — the membrane has four independent 1-cycles (loops). These cycles are the topological degrees of freedom available for phase winding — they are the locations where non-trivial winding numbers $n \in \mathbb{Z}$ can accumulate.

---

## The Field on the Membrane

The collapse field $\Phi = Ae^{i\theta}$ is defined throughout the ICHTB volume, including on the membrane. But the membrane is special: **it is where the zone operators change**. On the membrane, the zone-dependent diffusion tensor $\mathcal{M}^{ij}$ transitions from the value appropriate to one zone to the value appropriate to the adjacent zone.

The field $\Phi$ itself must be **continuous** across the membrane (no singular energy densities). The normal derivative $\partial_n\Phi$ may be **discontinuous** — this discontinuity is precisely the membrane's content. It is a surface source or sink in the field equation.

Writing the field equation on either side of a membrane face $\Delta_k$ with normal $\hat{n}_k$:

$$
[\![\Phi]\!]_{\Delta_k} = \Phi\big|_{\text{zone }+} - \Phi\big|_{\text{zone }-} = 0 \qquad \text{(continuity)}
$$

$$
[\![\mathcal{M}^{ij}n_i\partial_j\Phi]\!]_{\Delta_k} = \sigma_k(\Phi) \qquad \text{(flux jump condition)}
$$

where $\sigma_k(\Phi)$ is the surface source density at membrane face $k$, and $[\![\cdot]\!]$ denotes the jump across the membrane. When $\sigma_k = 0$, the flux is continuous: the membrane is transparent. When $\sigma_k \neq 0$, the membrane acts as a source or sink: it injects or absorbs field flux, coupling the dynamics of the two adjacent zones.

The membrane source term $\sigma_k$ is the new physics of Book 3.0. Books 1.0 and 2.0 treated the zones as independent regions; the membrane coupling $\sigma_k$ is the mechanism by which they are not.

