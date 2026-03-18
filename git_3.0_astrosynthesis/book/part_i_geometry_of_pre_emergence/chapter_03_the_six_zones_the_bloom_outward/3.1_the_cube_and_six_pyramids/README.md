# 3.1 The Cube and Six Pyramids

## The Choice of Geometry

After i₀ and the membrane come the zones — the six directional regions into which the ICHTB volume is partitioned. The first question is the most basic one: why six? Why a cube? Why not a sphere, a tetrahedron, an icosahedron?

The answer is not arbitrary. The CTS master equation involves three independent second-order operations: the gradient $\nabla\Phi$, the Laplacian $\nabla^2\Phi$, and the time derivative $\partial_t\Phi$. Three operations, two orientations each (positive and negative), gives exactly six distinct directional modes. The geometry of the enclosing volume must provide exactly six faces with mutually perpendicular normals — one face for each mode — so that each mode has a unique outward direction associated with it.

Among all convex polyhedra, only the **rectangular parallelepiped** (of which the cube is the regular special case) has exactly six faces with three pairs of parallel, anti-parallel normals. The cube is the unique regular solid satisfying this constraint. The tetrahedron has four faces (too few for six independent modes). The octahedron has eight. The icosahedron has twenty. Only the cube has exactly six faces with orthogonal face normals.

This is why the ICHTB is a cube: the mathematics of second-order partial differential equations in three dimensions has exactly three independent operators in each sign orientation, and the cube is the natural geometric host for that algebraic structure.

---

## The Six Pyramids: Explicit Construction

Fix a unit cube centered at the origin, with face centers at:

$$
\mathbf{f}_{\pm X} = (\pm\tfrac{1}{2}, 0, 0), \quad \mathbf{f}_{\pm Y} = (0, \pm\tfrac{1}{2}, 0), \quad \mathbf{f}_{\pm Z} = (0, 0, \pm\tfrac{1}{2})
$$

and i₀ at the center $(0, 0, 0)$. Each pyramid $P_k$ is the convex hull of i₀ and one square face of the cube:

$$
P_{+X} = \text{conv}\left\{i_0,\; (\tfrac{1}{2}, \pm\tfrac{1}{2}, \pm\tfrac{1}{2})\right\}
$$

with five vertices in total: the apex at i₀ and the four corners of the $x = +\frac{1}{2}$ face. Similarly for the other five pyramids.

Each pyramid has:
- **One apex**: i₀ at the origin
- **One square base**: a face of the cube with side length 1
- **Four triangular sides**: the membrane faces connecting i₀ to each edge of the base face
- **Height**: $\frac{1}{2}$ (distance from i₀ to the face center $\mathbf{f}_k$)
- **Volume**: $V_P = \frac{1}{3} \times \text{base area} \times \text{height} = \frac{1}{3} \times 1 \times \frac{1}{2} = \frac{1}{6}$

The total volume of the cube is 1 (unit cube), and $6 \times \frac{1}{6} = 1$. The six pyramids fill the cube exactly — no gaps, no overlaps. This will be proved formally in section 3.3.

---

## The Zone Names and Assignments

Each pyramid is named by the direction of its face center from i₀:

| Zone | Symbol | Face direction | Face center | Physical role |
|------|--------|---------------|-------------|---------------|
| Apex | +Z | $+\hat{z}$ | $(0, 0, +\frac{1}{2})$ | Temporal evolution |
| Core | −Z | $-\hat{z}$ | $(0, 0, -\frac{1}{2})$ | Pre-emergence anchor |
| Forward | +X | $+\hat{x}$ | $(+\frac{1}{2}, 0, 0)$ | Propagation / gradient |
| Compression | −X | $-\hat{x}$ | $(-\frac{1}{2}, 0, 0)$ | Focusing / negative Laplacian |
| Expansion | +Y | $+\hat{y}$ | $(0, +\frac{1}{2}, 0)$ | Growth / positive Laplacian |
| Memory | −Y | $-\hat{y}$ | $(0, -\frac{1}{2}, 0)$ | Rotation / curl storage |

The Z-axis is distinguished: Apex (+Z) carries the time derivative operator and Memory (−Z, the Core) is the persistence anchor where $\Phi \to i_0$. This reflects the special role of the CTS temporal direction relative to the three spatial ones.

The X and Y axes carry the second-order spatial operators: Forward/Compression carry gradient and negative Laplacian (opposite signs of $\nabla^2$), Expansion/Memory carry positive Laplacian and curl. The pairing of $\pm$ faces with $\pm$ versions of the same operator is exact.

---

## The Solid Angle Structure

From i₀, each face subtends a solid angle. For a square face of side 1 at distance $\frac{1}{2}$ from the center, the solid angle is:

$$
\Omega_{\text{face}} = 4\arctan\left(\frac{ab}{4r\sqrt{a^2 + b^2 + 4r^2}}\right)\bigg|_{a=b=1,\, r=1/2} = 4\arctan\left(\frac{1}{4 \cdot \frac{1}{2} \cdot \sqrt{1+1+1}}\right)
$$

$$
= 4\arctan\left(\frac{1}{2\sqrt{3}}\right) \approx 4 \times 0.2810 \approx 1.124 \text{ sr}
$$

The total solid angle subtended by all six faces: $6 \times 1.124 \approx 6.745 \text{ sr}$. But the total solid angle around any interior point is $4\pi \approx 12.566 \text{ sr}$. This discrepancy ($4\pi - 6\Omega_{\text{face}} \approx 5.82 \text{ sr}$) is the total solid angle subtended by the membrane — the 12 triangular faces collectively occupy approximately 46% of the sky as seen from i₀.

This is a key structural fact: from the perspective of i₀, **nearly half the field of view is membrane**. The zones do not dominate the view from the center — the zone boundaries (the membrane) are almost as prominent as the zones themselves. The ICHTB is not primarily a directional structure; it is primarily an interfacial structure. The membrane is not an afterthought attached to the zones — it is co-dominant with them from the perspective of i₀.

---

## Why the Apex Axis Is Vertical

The assignment of +Z to the Apex (temporal) zone and −Z to the Core (pre-emergence anchor) reflects a conventional choice that aligns with physics notation: time is vertical, space is horizontal. This matches the standard Minkowski spacetime diagram convention (timelike axis vertical, spacelike axes horizontal).

But the choice also has physical content: the CTS temporal direction $\partial_t\Phi$ is the direction of increasing phase $\theta$ (from section 1.4, $v_\theta = \partial_t\theta$ is the recursion velocity, and phase increases as the system evolves forward in time). The Apex zone is the zone where this increase is most concentrated — where $\partial_t\Phi$ dominates the dynamics.

The Core (−Z), sitting directly below the Apex, is the zone where time has not yet begun — where the field is pinned to the pre-emergence value $\Phi \to i_0$. The Core is the "past" of the ICHTB in the same sense that the origin of a Minkowski diagram is the past of all future-directed worldlines. From the Core, the only direction is upward toward the Apex — toward real temporal evolution, toward the possibility of departure from i₀.

