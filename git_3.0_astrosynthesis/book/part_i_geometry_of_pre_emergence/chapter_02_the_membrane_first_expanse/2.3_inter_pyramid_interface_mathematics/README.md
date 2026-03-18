# 2.3 Inter-Pyramid Interface Mathematics

## Setting Up the Junction Problem

Each of the 12 membrane triangles $\Delta_k$ is a planar interface between two pyramidal zones. We need the complete mathematical description of how the CTS field $\Phi$ behaves at and across this interface. This is a **junction problem** — one of the oldest problems in mathematical physics, with well-developed machinery from three distinct fields: shock wave theory, surface defect physics, and general relativity.

We will develop the CTS junction formalism from first principles, then show the connections.

---

## The Membrane as a Distributional Source

Let $\Omega^+$ and $\Omega^-$ denote the two pyramidal zone volumes on either side of a membrane face $\Delta$ with unit normal $\hat{n}$ pointing from $\Omega^-$ to $\Omega^+$. The CTS master equation in each bulk region is:

$$
\partial_t\Phi = D\nabla_i(\mathcal{M}^{ij}_\pm\nabla_j\Phi) - \Lambda(\mathcal{M}^{ij}_\pm\nabla_i\Phi\nabla_j\Phi) + \gamma\Phi^3 - \kappa\Phi \qquad \text{in }\Omega^\pm
$$

where $\mathcal{M}^{ij}_+$ and $\mathcal{M}^{ij}_-$ are the distinct metric tensors of the two adjacent zones. To write a single equation valid across the entire ICHTB including the membrane, we use the **distributional derivative** approach.

Let $\delta_\Delta(\mathbf{x})$ denote the Dirac delta function supported on $\Delta$:

$$
\int_{\mathbb{R}^3} f(\mathbf{x})\,\delta_\Delta(\mathbf{x})\,d^3x = \int_\Delta f(\mathbf{x})\,d^2S
$$

The gradient of the Heaviside function $H_+(\mathbf{x})$ (which equals 1 in $\Omega^+$ and 0 in $\Omega^-$) is:

$$
\nabla H_+(\mathbf{x}) = \hat{n}\,\delta_\Delta(\mathbf{x})
$$

The full field equation, valid in the distributional sense everywhere including the membrane, is:

$$
\partial_t\Phi = D\nabla_i\left(\mathcal{M}^{ij}(\mathbf{x})\nabla_j\Phi\right) - \Lambda\mathcal{M}^{ij}(\mathbf{x})\nabla_i\Phi\nabla_j\Phi + \gamma\Phi^3 - \kappa\Phi
$$

where $\mathcal{M}^{ij}(\mathbf{x}) = \mathcal{M}^{ij}_+ H_+(\mathbf{x}) + \mathcal{M}^{ij}_-(1 - H_+(\mathbf{x}))$ is the step-function metric. Expanding the divergence term:

$$
\nabla_i(\mathcal{M}^{ij}(\mathbf{x})\nabla_j\Phi) = H_+\nabla_i(\mathcal{M}^{ij}_+\nabla_j\Phi) + (1-H_-)\nabla_i(\mathcal{M}^{ij}_-\nabla_j\Phi) + [\![\mathcal{M}^{ij}n_i\nabla_j\Phi]\!]\,\delta_\Delta
$$

The delta function term is the **membrane source**:

$$
\boxed{\sigma(\mathbf{x}) = [\![\mathcal{M}^{ij}n_i\partial_j\Phi]\!]_\Delta = \left(\mathcal{M}^{ij}_+ - \mathcal{M}^{ij}_-\right)n_i\partial_j\Phi\big|_\Delta}
$$

This is the **inter-pyramid interface flux jump** — it is nonzero whenever the zone metric tensors $\mathcal{M}^{ij}$ differ across the membrane.

---

## The Zone Metrics and Their Jumps

The six ICHTB zone operators assign different metric tensors to each zone based on the dominant CTS operation in that direction. From the ICHTB geometry (Chapter 5 will derive these in full; here we state the relevant result):

| Zone | Label | Dominant operator | $\mathcal{M}^{ij}$ eigenvalue structure |
|------|-------|------------------|----------------------------------------|
| +Z | Apex | $\partial_t\Phi$ | $\text{diag}(m_\perp, m_\perp, m_\parallel)$, $m_\parallel > m_\perp$ |
| −Z | Core | $\Phi = i_0$ | $\text{diag}(m_0, m_0, m_0)$, isotropic |
| +X | Forward | $\nabla\Phi$ | $\text{diag}(m_\parallel, m_\perp, m_\perp)$, $m_\parallel \gg m_\perp$ |
| −X | Compression | $-\nabla^2\Phi$ | $\text{diag}(m_\parallel, m_\perp, m_\perp)$, $m_\parallel \ll m_\perp$ |
| +Y | Expansion | $+\nabla^2\Phi$ | $\text{diag}(m_\perp, m_\parallel, m_\perp)$, $m_\parallel \gg m_\perp$ |
| −Y | Memory | $\nabla\times\mathbf{F}$ | $\text{antisymmetric component}$ |

For two adjacent zones $A$ and $B$, the metric jump at their shared membrane is:

$$
\Delta\mathcal{M}^{ij} = \mathcal{M}^{ij}_A - \mathcal{M}^{ij}_B
$$

The membrane source $\sigma = \Delta\mathcal{M}^{ij}n_i\partial_j\Phi|_\Delta$ is therefore:

- **Zero** when both zones have the same metric (this never happens for distinct adjacent zones in the ICHTB)
- **Proportional to** $\partial_j\Phi$ projected along $\hat{n}$: the source is stronger where the field has larger normal gradients at the membrane

This means the membrane is **self-activating**: wherever the field gradient is large near a zone boundary, the boundary generates a source that further modifies the field, creating a feedback mechanism that is entirely absent from the bulk zone equations.

---

## The Complete Junction Conditions

The full set of junction conditions at any membrane face $\Delta$ with normal $\hat{n}$ and adjacent zones $\Omega^\pm$:

**Condition 1 — Kinematic (continuity):**
$$
[\![\Phi]\!]_\Delta = 0
$$
The field is continuous across the membrane. No infinite energy densities are permitted.

**Condition 2 — Dynamic (flux jump):**
$$
[\![\mathcal{M}^{ij}n_i\partial_j\Phi]\!]_\Delta = \sigma_\Delta(\Phi, \partial_\tau\Phi)
$$
The normal flux jumps by $\sigma_\Delta$, which can depend on the field value and its **tangential** derivatives $\partial_\tau\Phi$ (derivatives parallel to the membrane surface) but not on the normal derivative (which would make the condition implicit and require regularization).

**Condition 3 — Phase consistency:**
$$
[\![\theta]\!]_\Delta = 2\pi n_\Delta, \qquad n_\Delta \in \mathbb{Z}
$$
The phase is single-valued up to integer multiples of $2\pi$. A non-zero $n_\Delta$ indicates a **phase vortex line** passing through the membrane — a topological defect threading the interface.

**Condition 4 — Amplitude positivity:**
$$
A|_{\Omega^+} \geq 0, \quad A|_{\Omega^-} \geq 0
$$
The amplitude (modulus of $\Phi$) is non-negative on both sides. The membrane can have $A = 0$ (a nodal surface) as a special case.

Conditions 1–4 together constitute the **CTS membrane junction system**. They are the "edge case formalism" referenced in Books 1.0 and 2.0 but not derived there.

---

## Phase Vortices Threading the Membrane

Condition 3 introduces the most physically significant membrane phenomenon: a vortex line with winding number $n \neq 0$ that terminates on (or threads through) the membrane.

From section 1.4, a vortex phase profile in 2D polar coordinates $(r, \phi)$ takes the form $\theta(r,\phi) = n\phi$. In 3D, the vortex is a **line** where $A = 0$, and the phase winds by $2\pi n$ around any small circle enclosing the line. When such a vortex line crosses a membrane face $\Delta_k$, the phase jump condition at the crossing point is:

$$
n_{\Delta_k} = n_{\text{vortex}}
$$

The membrane "absorbs" the topological charge of the vortex at the crossing point. This has a topological conservation law: the sum of phase jumps around any closed surface must equal zero (no net topological charge created or destroyed):

$$
\sum_{k} n_{\Delta_k}\,\text{(oriented)} = 0 \qquad \text{(global phase conservation)}
$$

This is the membrane analog of Gauss's law: the total "topological flux" (sum of phase winding numbers threading all membrane faces) is zero. Topological charge can be redistributed among membrane faces by changing the zone dynamics, but the total is conserved.

---

## Connection to Differential Geometry: The Second Fundamental Form

The membrane $\mathcal{M}$ is a piecewise-planar 2-surface in $\mathbb{R}^3$. Each membrane triangle $\Delta_k$ is flat — its intrinsic curvature is zero. But the **extrinsic curvature** of the membrane is concentrated at its edges and vertices, where the flat pieces meet at angles.

The **dihedral angle** $\alpha_k$ at each cube edge (the angle between adjacent membrane triangles meeting at that edge) determines the extrinsic curvature distribution. For a regular cube, this angle is $\arccos(1/\sqrt{3}) \approx 54.74°$ (the angle between adjacent triangular faces meeting at i₀ via the face midpoints — this is the tetrahedral angle). The actual dihedral angle between two membrane triangles meeting at a cube edge is determined by the geometry of the specific edge.

For the cube edge connecting two face-centers of adjacent cube faces, the dihedral angle between the corresponding membrane triangles is:

$$
\alpha = \pi - \arctan\sqrt{2} \approx \pi - 54.74° \approx 125.26°
$$

The concentrated Gaussian curvature at each cube edge is:

$$
K_e = \pi - \alpha_e
$$

and the total Gaussian curvature integrated over the entire membrane is, by the Gauss-Bonnet theorem:

$$
\int_\mathcal{M} K\,dA + \oint_{\partial\mathcal{M}} \kappa_g\,ds = 2\pi\chi(\mathcal{M}) = 2\pi(-3) = -6\pi
$$

This non-zero total curvature means the membrane is **topologically non-trivial** — it cannot be flattened into a plane without cutting. The curvature is locked into the geometry by the requirement that all 12 membrane triangles share a common vertex (i₀) while their outer edges trace the 12 edges of a cube. This topological constraint is the geometric origin of the four independent 1-cycles identified in section 2.2.

