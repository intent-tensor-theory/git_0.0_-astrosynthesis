# Appendix C: Membrane Mathematics — Inter-Pyramid Boundary Conditions

This appendix provides a self-contained reference for the complete ICHTB membrane formalism: geometry, junction conditions at faces, edges, and vertices, the Zone Exchange Zone model, and connections to prior mathematics. For derivations see Chapters 2 and 6; for zone metrics and the master equation see Appendix B.

---

## C.1 Membrane Geometry

The ICHTB membrane $\mathcal{M}$ is the union of **12 triangular faces** — the faces of the cuboctahedron formed by connecting the center i₀ to every edge of the enclosing unit cube.

### Explicit Construction

Unit cube centered at the origin, corners at $C_k = (\pm\tfrac{1}{2}, \pm\tfrac{1}{2}, \pm\tfrac{1}{2})$, i₀ at $(0,0,0)$. Each membrane triangle $\Delta_k$ is the convex hull of i₀ and one cube edge $C_aC_b$:

$$
\Delta_k = \mathrm{conv}\{i_0,\, C_a,\, C_b\}
$$

Unit normal to $\Delta_k$:

$$
\hat{n}_k = \frac{\mathbf{C}_a \times \mathbf{C}_b}{|\mathbf{C}_a \times \mathbf{C}_b|}
\tag{C.1}
$$

### The 12 Faces with Zone Assignments

| Face | Adjacent zones | Normal direction $\hat{n}_k$ | Type |
|------|---------------|------------------------------|------|
| $\Delta_1$ | Forward (+X) / Expansion (+Y) | $\hat{x}+\hat{y}$ | Amplifying |
| $\Delta_2$ | Forward (+X) / Apex (+Z) | $\hat{x}+\hat{z}$ | Amplifying |
| $\Delta_3$ | Forward (+X) / Memory (−Y) | $\hat{x}-\hat{y}$ | Damping |
| $\Delta_4$ | Forward (+X) / Core (−Z) | $\hat{x}-\hat{z}$ | Damping |
| $\Delta_5$ | Expansion (+Y) / Apex (+Z) | $\hat{y}+\hat{z}$ | Amplifying |
| $\Delta_6$ | Expansion (+Y) / Memory (−Y) | $\hat{y}-\hat{y}'$ | Neutral |
| $\Delta_7$ | Expansion (+Y) / Core (−Z) | $\hat{y}-\hat{z}$ | Damping |
| $\Delta_8$ | Apex (+Z) / Compression (−X) | $-\hat{x}+\hat{z}$ | Damping |
| $\Delta_9$ | Apex (+Z) / Memory (−Y) | $-\hat{y}+\hat{z}$ | Neutral |
| $\Delta_{10}$ | Compression (−X) / Memory (−Y) | $-\hat{x}-\hat{y}$ | Neutral |
| $\Delta_{11}$ | Compression (−X) / Core (−Z) | $-\hat{x}-\hat{z}$ | Strongly damping |
| $\Delta_{12}$ | Memory (−Y) / Core (−Z) | $-\hat{y}-\hat{z}$ | Damping |

*Normals are given as unnormalized direction vectors; divide by $\sqrt{2}$ for unit normals.*

### Geometric Data (Unit Cube)

$$
\text{Area of each } \Delta_k = \frac{\sqrt{2}}{8}
\tag{C.2}
$$

$$
\text{Total membrane area} = 12 \times \frac{\sqrt{2}}{8} = \frac{3\sqrt{2}}{2} \approx 2.121
\tag{C.3}
$$

### Topological Data of $\mathcal{M} = \bigcup_{k=1}^{12}\Delta_k$

| Quantity | Value |
|---------|-------|
| Vertices | 9 (i₀ + 8 cube corners) |
| Edges | 24 (12 spokes from i₀ + 12 cube edges) |
| Faces | 12 triangles |
| Euler characteristic $\chi = V - E + F$ | $9 - 24 + 12 = -3$ |
| Independent 1-cycles $H_1(\mathcal{M})$ | $\mathbb{Z}^4$ (four independent loops) |

The four independent 1-cycles are the locations where non-trivial phase winding $n \in \mathbb{Z}$ can accumulate. Solid angle subtended by all 12 faces as seen from i₀: $\approx 6.74$ sr out of $4\pi \approx 12.57$ sr — nearly half the view from i₀ is membrane.

---

## C.2 The Membrane as a Distributional Source

Let $\Omega^\pm$ be the two zone volumes on either side of a membrane face $\Delta$ with normal $\hat{n}$ pointing from $\Omega^-$ into $\Omega^+$. The step-function metric across $\Delta$:

$$
\mathcal{M}^{ij}(\mathbf{x}) = \mathcal{M}^{ij}_+ H_+(\mathbf{x}) + \mathcal{M}^{ij}_-(1-H_+(\mathbf{x}))
$$

where $H_+(\mathbf{x})$ is the Heaviside function selecting $\Omega^+$, with $\nabla H_+ = \hat{n}\,\delta_\Delta$.

Expanding the divergence term in the master equation in the distributional sense:

$$
\nabla_i(\mathcal{M}^{ij}(\mathbf{x})\nabla_j\Phi) = H_+\nabla_i(\mathcal{M}^{ij}_+\nabla_j\Phi) + (1-H_+)\nabla_i(\mathcal{M}^{ij}_-\nabla_j\Phi) + \underbrace{\llbracket\mathcal{M}^{ij}n_i\nabla_j\Phi\rrbracket}_{\text{membrane source}}\,\delta_\Delta
\tag{C.4}
$$

The delta-function term is the **membrane source**:

$$
\boxed{\sigma(\mathbf{x}) \equiv \llbracket\mathcal{M}^{ij}n_i\partial_j\Phi\rrbracket_\Delta = \left(\mathcal{M}^{ij}_+ - \mathcal{M}^{ij}_-\right)n_i\partial_j\Phi\big|_\Delta}
\tag{C.5}
$$

This is non-zero whenever $\mathcal{M}^{ij}_+ \neq \mathcal{M}^{ij}_-$ — i.e., at every ICHTB zone boundary. The membrane is **self-activating**: the source is larger where the field gradient is larger at the membrane, creating a feedback between the field configuration and the membrane coupling.

---

## C.3 Junction Conditions at a Single Face

At any point $\mathbf{p}$ in the interior of face $\Delta_k$ (away from edges and vertices), the collapse field satisfies four conditions:

**Condition 1 — Field continuity (Dirichlet):**
$$
\llbracket\Phi\rrbracket_{\Delta_k} = 0
\tag{C.6}
$$
The field is single-valued at the membrane. No infinite energy densities permitted.

**Condition 2 — Normal flux jump (Robin):**
$$
\left[D\,\mathcal{M}^{ij}_+\,n_i\partial_j\Phi_+ - D\,\mathcal{M}^{ij}_-\,n_i\partial_j\Phi_-\right]_\mathbf{p} = \sigma(\mathbf{p})\,\Phi(\mathbf{p})
\tag{C.7}
$$
The jump in metric-weighted normal gradient equals the surface conductance $\sigma$ times the field value. When $\sigma = 0$: transparent membrane (no flux discontinuity). When $\sigma > 0$: membrane sources field amplitude. When $\sigma \to \infty$: membrane is opaque ($\partial_n\Phi = 0$, Neumann wall).

**Condition 3 — Phase consistency:**
$$
\llbracket\theta\rrbracket_{\Delta_k} = 2\pi n_k, \qquad n_k \in \mathbb{Z}
\tag{C.8}
$$
Phase is single-valued modulo $2\pi$. A non-zero integer $n_k$ indicates a **vortex line** with winding number $n_k$ passing through the face. The global phase conservation law:
$$
\sum_{k=1}^{12} n_k\,(\text{signed}) = 0
\tag{C.9}
$$
Topological charge is conserved: the sum of vortex winding numbers threading all 12 faces is zero.

**Condition 4 — Amplitude non-negativity:**
$$
A|_{\Omega^\pm} \geq 0
\tag{C.10}
$$
Special case: $A = 0$ at the membrane is a nodal surface.

---

## C.4 Transmission and Reflection at a Membrane

**Transmission coefficient** for a plane wave normally incident on $\Delta_k$ from $\Omega^-$:

$$
T_{-\to+} = \frac{4D^2\,\mathcal{M}^{nn}_-\,\mathcal{M}^{nn}_+\,k_-\,k_+}{\left(D\,\mathcal{M}^{nn}_-\,k_- + D\,\mathcal{M}^{nn}_+\,k_+\right)^2 + \sigma^2}
\tag{C.11}
$$

where $\mathcal{M}^{nn}_\pm = \mathcal{M}^{ij}_\pm n_in_j$ and $k_\pm$ are the wavenumbers in each zone.

At $\sigma = 0$: reduces to the standard step-potential transmission formula.
At $\sigma \to \infty$: $T \to 0$ (total reflection).

**Reflection coefficient:** $R = 1 - T$ (energy conservation).

**CTS Snell's law** (oblique incidence, angle $\theta_\pm$ to the membrane normal):

$$
\sqrt{\mathcal{M}^{tt}_-}\,\sin\theta_- = \sqrt{\mathcal{M}^{tt}_+}\,\sin\theta_+
\tag{C.12}
$$

where $\mathcal{M}^{tt}$ is the tangential metric component. Total internal reflection when:
$$
\mathcal{M}^{tt}_-\sin^2\theta_- > \mathcal{M}^{tt}_+
\tag{C.13}
$$

The effective **refractive index** of zone $k$: $\quad n_k = \sqrt{\mathcal{M}^{tt}_k}$.

---

## C.5 The Zone Exchange Zone (ZEZ)

The sharp-membrane limit is the idealization. Physically, the metric transitions over a layer of thickness $\ell \sim \xi = \sqrt{D/\kappa}$. The smooth interpolation:

$$
\mathcal{M}^{ij}(\mathbf{x}) = \mathcal{M}^{ij}_- + \frac{\mathcal{M}^{ij}_+ - \mathcal{M}^{ij}_-}{1 + e^{-d(\mathbf{x})/\ell}}
\tag{C.14}
$$

where $d(\mathbf{x})$ is the signed distance from the membrane (positive toward $\Omega^+$). The **ZEZ** is the layer $|d| \lesssim 2\ell$.

**ZEZ resonance condition** for reflectionless transmission:

$$
\frac{\sqrt{\mathcal{M}^{nn}_+ - \mathcal{M}^{nn}_-}\;A_0\,k_\perp\,\ell}{\sqrt{2D}} = \frac{n\pi}{2}, \qquad n \in \mathbb{Z}
\tag{C.15}
$$

When satisfied: excitation passes without reflection. When not satisfied: partial reflection — the membrane is a mode-selective filter.

**Consequence:**
- A states (small $A_0$): satisfy (C.15) easily → propagate freely across all zones
- B states (large $A_0 \sim \Phi_B$): typically do not → confined to home zone by reflection

**ZEZ energy flux** through face $\Delta_k$:

$$
\dot{E}_k = -D\int_{\Delta_k}\mathrm{Re}\!\left(\Phi^*\,\llbracket\mathcal{M}^{ij}n_i\partial_j\Phi\rrbracket\right)d^2S
\tag{C.16}
$$

**Membrane energy conservation:**
$$
\sum_{k=1}^{12}\dot{E}_k = 0
\tag{C.17}
$$

**Phase mixing in the ZEZ:** The varying metric injects a phase source as the field traverses the transition layer:

$$
\partial_t\theta\big|_{\text{ZEZ}} \ni D\,(\partial_d\mathcal{M}^{dd})\,(\partial_d A / A)
\tag{C.18}
$$

This is the mechanism by which zone exchange occurs: the ZEZ converts the directional character of an excitation from one zone's signature to the adjacent zone's.

---

## C.6 The Singularity Hierarchy

The ICHTB membrane has three levels of singularity — face interiors, edges, and vertices — each requiring its own junction formalism.

### Level 1 — Face Interiors (12 faces)

The generic case. Two zones meet at a surface. Conditions: (C.6)–(C.10). The full face junction formalism of §C.3 applies.

### Level 2 — Edges (24 edges of the cuboctahedron)

At each edge, **three zones** meet simultaneously. There are 8 spokes (from i₀ to cube corners, each shared by 3 membrane triangles) and the cuboctahedron's own 24 edges.

**Three-way continuity:**
$$
\Phi_\alpha(\mathbf{q}) = \Phi_\beta(\mathbf{q}) = \Phi_\gamma(\mathbf{q}) \equiv \Phi(\mathbf{q})
\tag{C.19}
$$

**Kirchhoff flux balance:**
$$
\sum_{k \in \{\alpha,\beta,\gamma\}} D_k\,\mathcal{M}^{ij}_k\,n^{(k)}_i\partial_j\Phi\Big|_{\mathbf{q}} = \sigma_{\mathrm{edge}}\,\Phi(\mathbf{q})
\tag{C.20}
$$

The three normals satisfy the geometric constraint $\sum_k \omega_k\hat{n}^{(k)} = \mathbf{0}$ where $\omega_k$ is the opening angle of zone $k$'s wedge. For the ideal cuboctahedron all opening angles are equal: $\omega_k = 2\pi/3$ (120°), giving an isotropically symmetric triple junction.

**Compatibility (regular edge, no topological defect):**
$$
\sigma_{\alpha\beta} + \sigma_{\beta\gamma} + \sigma_{\gamma\alpha} = 0
\tag{C.21}
$$
When violated: a **topological defect line** is nucleated along the spoke/edge.

**Edge classification by zone signs:**

| Type | Zone signs | Count | Character |
|------|-----------|-------|-----------|
| Type I | +, mixed, mixed (one positive) | 8 | Local attractor for A states |
| Type II | +, +, + (all positive) | 4 | Maximum amplification lines |
| Type III | −, mixed, mixed (one negative) | 8 | Local repeller |
| Type IV | −, −, − (all negative) | 4 | Maximum damping lines |

**Edge-restricted master equation** (1D effective theory along edge arc length $s$):

$$
\partial_t\phi(s) = D_e\,\partial_s^2\phi - \Lambda_e(\partial_s\phi)^2 + \gamma_e|\phi|^2\phi - \kappa_e\phi
\tag{C.22}
$$

where $D_e = \tfrac{1}{3}\sum_k D_k\mathcal{M}^{ss}_k$. This has the same form as the 3D master equation — CTS is self-similar across scales. Supports **edge solitons** (1.B states localized to the edge), more stable than bulk solitons due to 1D confinement.

### Level 3 — Vertices (12 vertices of the cuboctahedron)

#### The 6 Square Vertices (four-zone junctions)

Four membrane faces meet at each square vertex. Four zones contact the vertex: always two positive and two negative (checker pattern).

**Four-way continuity:**
$$
\Phi_1(\mathbf{v}) = \Phi_2(\mathbf{v}) = \Phi_3(\mathbf{v}) = \Phi_4(\mathbf{v})
\tag{C.23}
$$

**Four-flux balance:**
$$
\sum_{k=1}^{4} D_k\,\mathcal{M}^{ij}_k\,n^{(k)}_i\partial_j\Phi\Big|_{\mathbf{v}} = \sigma_{\mathrm{sq}}\,\Phi(\mathbf{v})
\tag{C.24}
$$

Checker pattern: positive and negative contributions approximately cancel → square vertices are **saddle points** of the ICHTB, unstable equilibria equally pulled by amplifying and damping zones.

#### The 8 Triangular Vertices (three-zone junctions)

The 8 cube corners. Three zones meet. Two types by sign parity:

**All-positive vertex** $(+X,+Y,+Z)$ and its 4 octahedral copies — all three zones amplifying. **Maximum-amplification point** of the ICHTB. Supports **vertex breathers**: the effective 0D equation

$$
\dot{A}_v = \Sigma_v A_v + \Gamma_v|A_v|^2 A_v - K_v A_v
\tag{C.25}
$$

is the Duffing oscillator with periodic solutions $A_v(t) = A_0\,\mathrm{cn}(\omega t, k)$ (Jacobi elliptic functions).

**All-negative vertex** $(−X,−Y,−Z)$ — all three zones damping. **Maximum-damping point**. Pure drain; no persistent oscillation.

Mixed-parity vertices: one of each sign type; two meet; one balanced.

#### The i₀ Vertex (the extreme junction)

All 12 membrane triangles share i₀. All six zones simultaneously converge. The resolution: at i₀, $A(i_0) \to 0$, so all membrane source terms $\sigma_k|_{i_0} = 0$. The six zone operators all agree on $\Phi = 0$ at i₀. The membrane imposes a **quantization condition** on the angular field modes near i₀:

$$
\Phi(r, \Omega) \approx r^\nu\,\psi(\Omega)\,e^{i\pi/2} + O(r^{\nu+1})
\tag{C.26}
$$

The 12-fold membrane geometry selects the allowed angular modes $\psi(\Omega)$ — only harmonics consistent with the cuboctahedral symmetry group $O_h$ are permitted.

---

## C.7 Complete Singularity Count

| Locus | Count | Zones meeting | Formalism | Physics |
|-------|-------|--------------|-----------|---------|
| Face interiors $\Delta_k$ | 12 | 2 | Conditions (C.6)–(C.10) | Transmission, reflection, vortex threading |
| Cuboctahedron edges | 24 | 3 | Triple-junction (C.19)–(C.21) | Defect nucleation, edge solitons |
| Square vertices | 6 | 4 | Four-flux balance (C.23)–(C.24) | Saddle points |
| Triangular vertices | 8 | 3 | Three-flux balance (C.25) | Max amplification/damping; vertex breathers |
| i₀ vertex | 1 | 6 | All six zones; $A = 0$ | Pre-emergence degeneracy; mode selection |

**Cuboctahedron Euler characteristic:** $\chi = V - E + F = 12 - 24 + 12 = 0$ (same as a torus). Topological excitations (vortices, knots) are stabilized by topological invariants of the same type that characterize the ICHTB's Euler structure.

**Corner regularity** (Kondrat'ev 1967): the worst-case singularity exponent at triangular vertices is $s^* = \pi/\omega_{\max} = 3/2$, giving $H^{3/2-\varepsilon}$ Sobolev regularity — Hölder continuous but not $C^2$ at vertices.

---

## C.8 Connections to Prior Mathematics

| Prior work | Condition used in CTS | Key parallel |
|-----------|----------------------|--------------|
| **Rankine-Hugoniot** (1870s) | Flux jump $\llbracket D\mathcal{M}^{ij}n_i\partial_j\Phi\rrbracket = \sigma\Phi$ | CTS flux jump ↔ RH momentum-flux conservation; moving membranes = shocks |
| **Maxwell/Fresnel** (1823, 1865) | Transmission coefficient (C.11); Snell's law (C.12) | $\sqrt{\mathcal{M}^{tt}_k}$ ↔ refractive index $n_k$; identical functional form |
| **Israel GR junction** (1966) | Flux jump ↔ extrinsic curvature jump | $D\mathcal{M}^{ij}n_i\partial_j\Phi$ ↔ $\mathcal{K}_{\mu\nu}$; $\sigma\Phi$ ↔ $8\pi G S_{\mu\nu}$ |
| **Lions-Magenes PDE** (1972) | Existence/uniqueness of weak solutions | CTS transmission problem has unique $H^1$ solution for any $L^2$ data |
| **Kondrat'ev corners** (1967) | Vertex regularity exponent $s^* = 3/2$ | $H^{3/2-\varepsilon}$ at triangular vertices |
| **Diehl surface field theory** (1986) | Surface universality classes | $\sigma > 0$ = ordinary; $\sigma = 0$ = special; $\sigma < 0$ = extraordinary transition |
| **Cardy BCFT** (1988) | 2D boundary conformal field theory at criticality | Triangular faces at critical $g$ governed by BCFT; Cardy states classify membrane BCs |

---

## C.9 Summary Formulas

**All junction conditions at a glance:**

| Location | Continuity | Flux balance |
|----------|-----------|--------------|
| Face interior | $\llbracket\Phi\rrbracket = 0$ | $\llbracket D\mathcal{M}^{ij}n_i\partial_j\Phi\rrbracket = \sigma\Phi$ |
| Edge (3 zones) | $\Phi_\alpha = \Phi_\beta = \Phi_\gamma$ | $\sum_k D_k\mathcal{M}^{ij}_kn^{(k)}_i\partial_j\Phi = \sigma_e\Phi$ |
| Square vertex (4 zones) | $\Phi_1 = \cdots = \Phi_4$ | $\sum_{k=1}^4 D_k\mathcal{M}^{ij}_kn^{(k)}_i\partial_j\Phi = \sigma_{\mathrm{sq}}\Phi$ |
| Triangular vertex (3 zones) | $\Phi_\alpha = \Phi_\beta = \Phi_\gamma$ | $\sum_{k=1}^3 D_k\mathcal{M}^{ij}_kn^{(k)}_i\partial_j\Phi = \sigma_{\mathrm{tri}}\Phi$ |
| i₀ vertex (6 zones) | $\Phi(i_0) = 0$ | All $\sigma_k|_{i_0} = 0$ automatically |

**Phase conservation (global):** $\displaystyle\sum_{k=1}^{12}n_k = 0$

**Membrane energy conservation:** $\displaystyle\sum_{k=1}^{12}\dot{E}_k = 0$

---

*See also: Appendix A (Master Equation), Appendix B (Zone Operator Reference), Appendix G (Notation), Chapter 2 (membrane as first expanse), Chapter 6 (edge-case mathematics).*
