# 6.3 Triple-Junction Points — Where Three Pyramids Meet

## The Cuboctahedron's Edges

The cuboctahedron has 24 edges — line segments where two triangular faces meet. At each edge, two membrane faces intersect, and therefore three zones (on either side of each face, plus the wedge between the two faces) come into contact along a line. These are the **triple-junction lines** of the ICHTB.

More precisely: at a cuboctahedron edge, the edge is shared by exactly two triangular faces. Each face is a membrane separating two zones. But the edge itself is adjacent to three zones: the two zones on either side of each face, minus the one zone shared between the two faces (since the edge is at the corner of two faces, there is always one zone that borders both faces). The three zones at an edge are: the zone on the outer side of face 1, the zone on the outer side of face 2, and the zone shared by both faces at the inner wedge.

For a concrete example: consider the edge where the Expansion (+Y) / Forward (+X) membrane meets the Expansion (+Y) / Apex (+Z) membrane. The edge is shared by both faces. Three zones touch this edge: Forward (+X), Expansion (+Y), and Apex (+Z). The Expansion zone is the "inner wedge" zone — it is on the interior side of both membranes.

At the interior of a membrane face, two zones meet, and the conditions of section 6.1 apply. At an edge, three zones simultaneously meet, and the conditions must account for all three at once.

---

## The Triple-Junction Condition

Let three zones $\alpha$, $\beta$, $\gamma$ meet at a point (or line) $\mathbf{q}$. The field must satisfy:

**Condition 1 — Three-way continuity:**
$$
\Phi_\alpha(\mathbf{q}) = \Phi_\beta(\mathbf{q}) = \Phi_\gamma(\mathbf{q}) \equiv \Phi(\mathbf{q})
$$

All three zone fields must agree at the junction point. This extends the two-zone continuity of section 6.1 to three zones simultaneously.

**Condition 2 — Flux balance (Kirchhoff's law for field flux):**
$$
\sum_{k \in \{\alpha,\beta,\gamma\}} D_k\mathcal{M}^{ij}_k n^{(k)}_i\partial_j\Phi\Big|_{\mathbf{q}} = \sigma_{\text{edge}}\Phi(\mathbf{q})
$$

where $\hat{n}^{(k)}$ is the outward normal from zone $k$ at the junction point, and $\sigma_{\text{edge}}$ is the **edge surface conductance** — a parameter of the edge (a line singularity, stronger than the face surface conductance $\sigma$ of section 6.1 which is associated with a surface).

The flux balance condition is the **Kirchhoff current law** for the collapse field: the total outward flux from all three zones at the junction must balance the edge source. This is the direct generalization of the two-zone flux jump condition: instead of "flux out of $\alpha$ minus flux into $\beta$ equals source," the three-zone version is "total flux out of all three zones equals edge source."

**Derivation:** The edge source appears because the edge is a line singularity of the metric $\mathcal{M}^{ij}(\mathbf{x})$ — not just a jump discontinuity (surface source) but a **corner singularity** (edge source, stronger singularity, edge = intersection of two surface jumps). The distributional form of the master equation, when integrated over a thin wedge-shaped neighborhood of the edge, yields the flux balance condition automatically from the divergence theorem applied to the metric-weighted gradient.

---

## The Edge-Geometry Factor

The three zone normals at an edge are not independent. They satisfy the geometric constraint:

$$
\sum_{k \in \{\alpha,\beta,\gamma\}} \omega_k\hat{n}^{(k)} = \mathbf{0}
$$

where $\omega_k$ is the opening angle of zone $k$ at the edge (the dihedral angle of zone $k$'s wedge at the edge). This is a consequence of the cuboctahedron geometry: the three normal vectors at an edge are coplanar (they all lie in the plane perpendicular to the edge direction $\hat{e}$) and sum to zero when weighted by the opening angles.

For the ICHTB cuboctahedron, all triangular faces have the same shape (equilateral triangles in the ideal case), so all opening angles are equal: $\omega_\alpha = \omega_\beta = \omega_\gamma = 2\pi/3$ (120° sectors). The three normal vectors at each edge point 120° apart from each other in the plane perpendicular to the edge.

The balanced 120° geometry means the flux balance condition (Kirchhoff's law) simplifies: with equal opening angles and equal diffusion coefficients $D_k = D$, the three-zone junction is **isotropically symmetric** — no zone is privileged at the edge. The field at the edge is equally influenced by all three adjacent zones.

This 120° symmetry has a name in the theory of grain boundaries: it is the **triple-point equilibrium condition** (Herring 1951, *Physical Review*, 82, 87), familiar from metallurgy as the condition for a stable grain boundary junction. In metallurgy it means the three grain boundary surface tensions are equal. In the CTS it means the three zone metrics are equally weighted at the edge junction.

---

## The 24 Edges of the ICHTB: A Classification

The ICHTB has 24 edges. These fall into distinct symmetry classes based on which three zones meet:

**Type I — One positive, two mixed (8 edges):** These edges have one all-positive zone (+X, +Y, or +Z) meeting two zones of opposite sign. Example: Forward (+X), Expansion (+Y), Memory (−Y). The flux balance at these edges has a net positive contribution from the positive zone. These edges are **local attractors** for A-state excitations — signal passing near a Type I edge is pulled toward the positive zone's amplification.

**Type II — All three positive (4 edges):** Edges where all three zones are positive-operator zones. In the cuboctahedron, the three positive-operator zones (+X, +Y, +Z) form a triangle — their mutual edges are these four Type II edges. At these edges, all three flux contributions are amplifying. These edges are **maximum-amplification points** of the ICHTB — any field excitation passing through a Type II edge gets the maximum possible boost from the geometry.

**Type III — One negative, two mixed (8 edges):** The mirror image of Type I — one negative zone (−X, −Y, or −Z) meeting two mixed-sign zones. These are **local repellers** — the negative zone drains field energy at the edge.

**Type IV — All three negative (4 edges):** The mirror image of Type II — all three negative zones (−X, −Y, −Z). These are **maximum-damping points**, where all three zones simultaneously drain field amplitude. A B-state excitation that survives passage through a Type IV edge has overcome the maximum possible geometric damping — it is the toughest test of excitation persistence.

The distribution of edge types across the cuboctahedron is symmetric under the full octahedral symmetry group $O_h$ — the same group that is the symmetry of the cube and the cuboctahedron. This ensures that the ICHTB has no preferred direction — A-state excitations can propagate in any direction through the cubic symmetry group without systematic bias.

---

## The Edge as a 1D Field Theory

At each edge (a line segment of finite length in the ICHTB), the collapse field satisfies an **effective 1D field theory** — a field equation restricted to the edge direction. This 1D theory is derived by integrating the 3D master equation over the cross-sectional wedge perpendicular to the edge, keeping only the edge-direction coordinate $s$ (arc length along the edge).

The result is the **edge-restricted master equation**:

$$
\partial_t\phi(s) = D_e\partial_s^2\phi(s) - \Lambda_e(\partial_s\phi)^2 + \gamma_e|\phi|^2\phi - \kappa_e\phi
$$

where the edge parameters $\{D_e, \Lambda_e, \gamma_e, \kappa_e\}$ are the three-zone averages of the bulk parameters:

$$
D_e = \frac{1}{3}\sum_k D_k\mathcal{M}^{ss}_k, \quad \kappa_e = \frac{1}{3}\sum_k\kappa_k + \sigma_{\text{edge}}/\ell
$$

Here $\mathcal{M}^{ss}_k$ is the edge-direction component of zone $k$'s metric, and $\ell$ is the edge length.

The edge-restricted master equation is the same form as the 3D master equation — the CTS structure is **self-similar across scales**. The edge supports 1D versions of all the same A and B state excitations as the 3D interior. In particular, the edge supports 1D solitons (1.B states localized to the edge) — these are **edge solitons**, qualitatively different from bulk solitons because they are one-dimensionally confined to the ICHTB geometry.

Edge solitons have lower energy than bulk solitons (they are confined to a 1D sub-manifold rather than spreading in 3D) and are therefore **more stable** — they have less phase space to decay into. The ICHTB edges are preferred locations for robust 1.B excitations.

