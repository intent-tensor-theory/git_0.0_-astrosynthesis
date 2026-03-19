# 6.1 Full Membrane Boundary Conditions

## Why Boundary Conditions Need Their Own Chapter

Chapter 2 introduced the ICHTB membrane as the boundary between zones — the 12 triangular faces of the cuboctahedron that separate the six pyramidal zones from each other and from the exterior. Section 2.3 stated the membrane junction conditions in schematic form: the field is continuous across each membrane, and the normal derivative jumps by an amount proportional to the surface source.

That schematic is adequate for single-membrane crossings in the interior of a face. But the ICHTB is a polyhedron with edges (where two faces meet) and vertices (where three or more faces meet). At those singular loci the schematic conditions are incomplete — they say nothing about what happens when the field simultaneously intersects two or three membranes at once.

This chapter provides the complete, exact boundary condition formalism — the mathematics of every membrane configuration the collapse field can encounter in the ICHTB.

---

## Single-Membrane Conditions (Interior of a Face)

Consider a point $\mathbf{p}$ in the interior of one of the 12 triangular faces. At $\mathbf{p}$, the membrane separates exactly two zones: call them zone $\alpha$ (on one side) and zone $\beta$ (on the other). Let $\hat{n}$ be the unit normal to the membrane at $\mathbf{p}$ pointing from $\alpha$ into $\beta$.

The collapse field $\Phi$ satisfies the master equation in each zone separately. At the membrane, two conditions are required (one for each side of the second-order spatial operator).

**Condition 1 — Continuity of the field:**
$$
\Phi_\alpha(\mathbf{p}) = \Phi_\beta(\mathbf{p})
$$

The field has no jump across the membrane. This ensures the field is single-valued at the interface — there is no ambiguity in $\Phi$ at the membrane itself. This is the Dirichlet-type condition.

**Condition 2 — Jump in the normal flux:**
$$
\left[D_\beta\mathcal{M}^{ij}_\beta n_i\partial_j\Phi_\beta - D_\alpha\mathcal{M}^{ij}_\alpha n_i\partial_j\Phi_\alpha\right]_{\mathbf{p}} = \sigma(\mathbf{p})\Phi(\mathbf{p})
$$

The jump in the **normal component of the metric-weighted gradient** (the "flux" in the sense of generalized diffusion) equals a surface source $\sigma(\mathbf{p})$ times the field value at the membrane. The source $\sigma$ is the **membrane surface conductance** — a property of the membrane itself, independent of the field. This is the Neumann-type (or Robin-type) condition.

The two conditions together are called the **transmission conditions** or **Sturm-Liouville junction conditions** for the ICHTB membrane. They are identical in structure to the junction conditions for quantum-mechanical wave functions at a delta-function potential barrier (a result well known since Bethe 1935 and standard in quantum mechanics textbooks).

---

## The Surface Source $\sigma$

The membrane surface conductance $\sigma(\mathbf{p})$ can in general depend on the membrane face (there are 12 faces, each potentially with a different $\sigma$), on the position within the face, and (in the dynamical metric case of section 5.2) on the local field amplitude. For the present chapter we treat $\sigma$ as a fixed parameter.

The physical interpretation of $\sigma$:
- $\sigma = 0$: The membrane is **transparent** — zero surface source, no discontinuity in normal flux. The field passes through as if the membrane were not there (but the metric still changes discontinuously at the face, so the zone operators still differ on the two sides).
- $\sigma > 0$: The membrane is a **source** — the normal flux jumps upward across the membrane, effectively injecting field amplitude into the normal direction at the interface. Positive $\sigma$ amplifies the field near the membrane.
- $\sigma < 0$: The membrane is a **sink** — the normal flux jumps downward, effectively draining field amplitude from the interface region. Negative $\sigma$ localizes excitations to the zone interior.
- $|\sigma| \to \infty$: The membrane is **opaque** (a Dirichlet wall for the flux) — the normal derivative is zero on both sides ($\partial_n\Phi = 0$ at the wall). The field cannot have any normal gradient at the membrane.

The **transmission coefficient** $T_\alpha^\beta$ for a plane wave incident on the membrane from zone $\alpha$ at normal incidence is:

$$
T_\alpha^\beta = \frac{4D_\alpha D_\beta k_\alpha k_\beta}{(D_\alpha k_\alpha + D_\beta k_\beta)^2 + \sigma^2}
$$

where $k_\alpha, k_\beta$ are the wavenumbers in the two zones. This formula is the exact CTS analog of the quantum-mechanical transmission coefficient across a delta-function barrier — at $\sigma = 0$ it reduces to the standard step-potential transmission formula, and for $\sigma \to \infty$ it gives $T \to 0$ (total reflection).

---

## The Metric Jump at the Membrane

The metric $\mathcal{M}^{ij}$ is piecewise constant in each zone (the zone metric) but jumps discontinuously at the membrane. In section 2.4 this jump was smoothed with a sigmoid transition. For the exact boundary condition analysis, we take the sharp-membrane limit — the metric jumps discontinuously exactly at the membrane face.

At the membrane separating zones $\alpha$ and $\beta$, the metric jump is:

$$
\Delta\mathcal{M}^{ij} = \mathcal{M}^{ij}_\beta - \mathcal{M}^{ij}_\alpha
$$

This jump contributes an additional source term in the weak (distributional) form of the master equation. Writing the master equation with the distributional metric (using $\theta(\hat{n}\cdot(\mathbf{x}-\mathbf{p}))$ for the Heaviside function selecting zone $\beta$):

$$
\partial_t\Phi = D\partial_i\left[(\mathcal{M}^{ij}_\alpha + \Delta\mathcal{M}^{ij}\cdot\theta)\partial_j\Phi\right] + \ldots
$$

Expanding the derivative:

$$
= D\mathcal{M}^{ij}_\alpha\partial_i\partial_j\Phi + D\theta\Delta\mathcal{M}^{ij}\partial_i\partial_j\Phi + D\delta(\hat{n}\cdot(\mathbf{x}-\mathbf{p}))\Delta\mathcal{M}^{ij}n_i\partial_j\Phi + \ldots
$$

The delta-function term is the **membrane contribution from the metric jump alone** — even with zero surface source $\sigma = 0$, the metric discontinuity generates a surface source proportional to $\Delta\mathcal{M}^{ij}n_i\partial_j\Phi$. This is the **geometric membrane source** — the contribution to the junction condition that comes purely from the ICHTB geometry, not from any material property of the membrane.

The complete Condition 2, including the geometric source, becomes:

$$
\left[D_\beta\mathcal{M}^{ij}_\beta - D_\alpha\mathcal{M}^{ij}_\alpha\right]n_i\partial_j\Phi\Big|_{\mathbf{p}} = (\sigma + D\,\Delta\mathcal{M}^{ij}n_in_j/|\hat{n}|)\Phi(\mathbf{p})
$$

In many practical cases $D_\alpha = D_\beta = D$ (the diffusion coefficient is the same in both zones, only the metric changes), and the condition simplifies to:

$$
D\left[\mathcal{M}^{ij}_\beta - \mathcal{M}^{ij}_\alpha\right]n_i\partial_j\Phi\Big|_{\mathbf{p}} = \sigma\Phi(\mathbf{p})
$$

where the $\sigma$ on the right now absorbs the geometric contribution.

---

## Normal vs. Tangential Decomposition

At the membrane, it is useful to decompose all tensors into normal ($\hat{n}$) and tangential ($\hat{t}_1, \hat{t}_2$, the two tangent vectors to the membrane face) components.

The metric jump decomposes as:

$$
\Delta\mathcal{M}^{ij} = \Delta\mathcal{M}^{nn}n^in^j + \Delta\mathcal{M}^{n1}(n^it_1^j + t_1^in^j) + \Delta\mathcal{M}^{11}t_1^it_1^j + \ldots
$$

The **normal component** $\Delta\mathcal{M}^{nn}$ determines the transmission/reflection coefficient for normally incident waves. The **tangential components** $\Delta\mathcal{M}^{11}, \Delta\mathcal{M}^{22}$ govern the **refraction** of obliquely incident waves — the CTS generalization of Snell's law.

The CTS Snell's law: for a wave incident at angle $\theta_\alpha$ to the membrane normal on the $\alpha$ side, the transmitted angle $\theta_\beta$ satisfies:

$$
\sqrt{\mathcal{M}^{tt}_\alpha}\sin\theta_\alpha = \sqrt{\mathcal{M}^{tt}_\beta}\sin\theta_\beta
$$

where $\mathcal{M}^{tt}$ is the tangential metric component. This is the exact analog of optical Snell's law $n_\alpha\sin\theta_\alpha = n_\beta\sin\theta_\beta$ with the refractive index replaced by $n = \sqrt{\mathcal{M}^{tt}}$ — the square root of the tangential zone metric.

Total internal reflection occurs when $\sin\theta_\beta > 1$, i.e., when $\mathcal{M}^{tt}_\alpha\sin^2\theta_\alpha > \mathcal{M}^{tt}_\beta$. A field excitation propagating in a zone with large tangential metric (e.g., Forward zone +X, where $\mathcal{M}^{xx}$ is large along the propagation direction) is totally internally reflected from zones with smaller tangential metric. The ICHTB acts as a **selective optical cavity** — certain zone-to-zone paths support transmission, others do not.

