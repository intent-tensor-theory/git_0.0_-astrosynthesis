# 3.3 Volume Partitioning — Why Six Fills Exactly

## The Claim

Six square pyramids, each with apex at the cube center i₀ and base equal to one face of the cube, partition the cube into non-overlapping regions whose union is the entire cube. This claim is geometrically obvious but requires a formal proof to establish that the partition is exact — no point is double-counted, no point is missed.

The proof also reveals something non-obvious: the partition is equivalent to a **Voronoi diagram** with respect to the six face-center points, which connects the ICHTB zone structure to one of the most powerful computational geometry constructions in mathematics.

---

## Proof by the Face-Projection Criterion

**Claim:** Every point $\mathbf{x}$ in the closed unit cube $[-\frac{1}{2}, \frac{1}{2}]^3$ (excluding the center i₀) belongs to exactly one pyramid $P_k$, determined by:

$$
P_k = \left\{\mathbf{x} \in \text{cube} \;:\; k = \arg\max_{j \in \{+X,-X,+Y,-Y,+Z,-Z\}} \frac{|\mathbf{x} \cdot \hat{n}_j|}{1} = |\langle\mathbf{x}, \hat{n}_j\rangle| \right\}
$$

More explicitly: the zone containing $\mathbf{x}$ is the one whose face normal $\hat{n}_k$ makes the largest absolute dot product with $\mathbf{x}$:

$$
\mathbf{x} \in P_{+X} \iff |x| \geq |y| \text{ and } |x| \geq |z| \text{ and } x \geq 0
$$
$$
\mathbf{x} \in P_{-X} \iff |x| \geq |y| \text{ and } |x| \geq |z| \text{ and } x \leq 0
$$

and so on for the other four faces, with analogous conditions on $y$ and $z$.

**Proof of coverage:** For any $\mathbf{x} = (x, y, z) \neq \mathbf{0}$, at least one of $|x|, |y|, |z|$ is the maximum (say $|x| = \max$). Then $\mathbf{x}$ belongs to $P_{+X}$ (if $x > 0$) or $P_{-X}$ (if $x < 0$). Every non-origin point is covered.

**Proof of non-overlap (except on boundaries):** If $\mathbf{x}$ satisfies the $P_{+X}$ condition ($|x| \geq |y|$, $|x| \geq |z|$, $x > 0$) with strict inequalities, then it does not satisfy any other zone condition. Points on the boundaries between zones (where two or three coordinates tie for maximum) lie on the membrane faces — exactly on the boundaries between pyramids, which have measure zero and are shared.

Therefore the six pyramids partition the cube exactly, with shared boundaries being the membrane triangles (measure zero). $\square$

---

## Equivalence to the Voronoi Diagram

The face-projection criterion above is equivalent to the **Voronoi diagram** of the six face centers $\{\mathbf{f}_k\}$ within the cube.

The Voronoi cell of face center $\mathbf{f}_k$ is the set of all points $\mathbf{x}$ in the cube that are closer to $\mathbf{f}_k$ than to any other face center:

$$
V_k = \left\{\mathbf{x} \in \text{cube} \;:\; |\mathbf{x} - \mathbf{f}_k| \leq |\mathbf{x} - \mathbf{f}_j| \text{ for all } j \neq k\right\}
$$

**Claim:** $V_k = P_k$ for each zone $k$.

**Proof (for $k = +X$):** The face center is $\mathbf{f}_{+X} = (\frac{1}{2}, 0, 0)$. For a point $\mathbf{x} = (x, y, z)$:

$$
|\mathbf{x} - \mathbf{f}_{+X}|^2 = (x - \tfrac{1}{2})^2 + y^2 + z^2
$$

$$
|\mathbf{x} - \mathbf{f}_{-X}|^2 = (x + \tfrac{1}{2})^2 + y^2 + z^2
$$

$|\mathbf{x} - \mathbf{f}_{+X}| \leq |\mathbf{x} - \mathbf{f}_{-X}|$ iff $(x - \frac{1}{2})^2 \leq (x + \frac{1}{2})^2$ iff $x \geq 0$.

$$
|\mathbf{x} - \mathbf{f}_{+Y}|^2 = x^2 + (y - \tfrac{1}{2})^2 + z^2
$$

$|\mathbf{x} - \mathbf{f}_{+X}| \leq |\mathbf{x} - \mathbf{f}_{+Y}|$ iff $(x - \frac{1}{2})^2 + y^2 \leq x^2 + (y - \frac{1}{2})^2$ iff $-x + \frac{1}{4} + y^2 \leq y^2 - y + \frac{1}{4}$ iff $y \leq x$.

Similarly, $|\mathbf{x} - \mathbf{f}_{+X}| \leq |\mathbf{x} - \mathbf{f}_{+Z}|$ iff $z \leq x$, and $|\mathbf{x} - \mathbf{f}_{+X}| \leq |\mathbf{x} - \mathbf{f}_{-Y}|$ iff $-y \leq x$, i.e., $x \geq -|y|$.

Combining: $\mathbf{x} \in V_{+X}$ iff $x \geq 0$, $x \geq y$, $x \geq -y$, $x \geq z$, $x \geq -z$ — which is exactly $x \geq 0$ and $x = \max(|x|, |y|, |z|)$, which is the face-projection criterion for $P_{+X}$. $\square$

The Voronoi diagram of the six face centers of a cube is exactly the decomposition of the cube into six pyramids, each anchored at the cube center. The ICHTB zone structure is therefore a **Voronoi partition** — one of the most natural and well-studied geometric decompositions in mathematics.

---

## The Wigner-Seitz Connection

The Voronoi cell of a lattice site $\mathbf{R}$ in a crystal is called the **Wigner-Seitz cell** — the set of all points closer to $\mathbf{R}$ than to any other lattice site. For the cubic (simple cubic) lattice, the Wigner-Seitz cell is a cube. For the face-centered cubic (FCC) lattice, it is a truncated octahedron.

What we have constructed is the Voronoi diagram of the **body** points (the face centers $\mathbf{f}_k$) within the container (the cube). This is not the same as the Wigner-Seitz cell, but it uses the same mathematical structure. The connection to solid-state physics is direct: the six ICHTB zones correspond to the six directions of the nearest-neighbor bonds in a simple cubic crystal, and the membrane triangles correspond to the bisector planes between nearest neighbors — exactly the faces of the Wigner-Seitz cell boundary.

The **Brillouin zone** of the simple cubic lattice (Brillouin, 1930) is also a cube — in reciprocal space — with its six faces corresponding to the six Bragg reflection planes at wavevectors $k = \pm\pi/a$ along each axis. The ICHTB zone boundary (the membrane) is the CTS analog of the Brillouin zone boundary: it is the surface in the ICHTB where the field dynamics change character, just as the Brillouin zone boundary is the surface in reciprocal space where electron dynamics change character (Bragg reflection, band gaps).

---

## Volume Fractions and the CTS Energy Budget

Each pyramid has volume $\frac{1}{6}$ of the total cube volume. But the energetic importance of each zone is not uniform — it depends on the amplitude of the CTS field $\Phi$ in each zone and on the zone metric $\mathcal{M}^{ij}$.

The total CTS energy in zone $k$ is:

$$
E_k = \int_{P_k} \left[D\,\mathcal{M}^{ij}_k\,\partial_i\Phi^*\partial_j\Phi + \kappa|\Phi|^2 - \frac{\gamma}{2}|\Phi|^4\right]d^3x
$$

Since each pyramid occupies the same volume, zones are energetically distinguished purely by the magnitude of $\mathcal{M}^{ij}_k$ and the field amplitude in them. A zone with a larger metric coefficient concentrates more energy per unit volume. The ICHTB is not energetically uniform — the zone metrics introduce a natural **energy landscape** even before any field configuration is specified.

The total CTS energy:

$$
E_{\text{total}} = \sum_{k=1}^{6} E_k + E_{\text{membrane}}
$$

where $E_{\text{membrane}}$ is the energy stored in the ZEZ transition regions across the 12 membrane faces. The membrane energy is typically small ($\sim \xi/L$ times the bulk energy, where $L$ is the ICHTB scale) but is precisely the energy that governs zone-to-zone transitions — it is the energy **between** zones, not in them.

