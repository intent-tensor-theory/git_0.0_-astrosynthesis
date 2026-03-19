# 6.5 Prior Work: Israel, Rankine-Hugoniot, Interface Field Theory

## The Mathematical Heritage of Singular Interfaces

Chapters 2, 5, and 6 have developed the ICHTB membrane junction conditions from first principles, applying them to the specific six-zone geometry of the collapse field. The formalism — continuity conditions, normal flux jumps, edge triple junctions, vertex multi-zone junctions — is exactly the CTS treatment of what mathematicians and physicists call **interface problems** or **transmission problems**.

This body of mathematics has a long and distinguished history, developed independently in fluid dynamics, electromagnetism, general relativity, and materials science. This section traces the key antecedents, clarifies exactly how the CTS formalism relates to each prior work, and identifies where the CTS extends or departs from the prior literature.

---

## Rankine-Hugoniot Jump Conditions (1870s)

The oldest rigorous treatment of jump conditions at an interface appears in fluid dynamics, developed independently by William Rankine (1870, "On the Thermodynamic Theory of Waves of Finite Longitudinal Disturbance," *Philosophical Transactions of the Royal Society*, 160, 277) and Pierre-Henri Hugoniot (1887, *Journal de l'École Polytechnique*, 57, 3).

Rankine and Hugoniot were studying **shock waves** in compressible fluids — surfaces of discontinuity in fluid density and velocity where the fluid transitions abruptly from pre-shock to post-shock state. Across a shock, the fluid equations in bulk form (conservation of mass, momentum, energy) are supplemented by the Rankine-Hugoniot jump conditions:

$$
[\![\rho(u - v_s)]\!] = 0 \quad \text{(mass flux conserved)}
$$
$$
[\![\rho u(u - v_s) + p]\!] = 0 \quad \text{(momentum flux conserved)}
$$
$$
[\![\rho e(u - v_s) + pu]\!] = 0 \quad \text{(energy flux conserved)}
$$

where $[\![f]\!] = f_{\text{post}} - f_{\text{pre}}$ denotes the jump in quantity $f$ across the shock, $u$ is the fluid velocity, $v_s$ is the shock velocity, $\rho$ is the density, $p$ is the pressure, and $e$ is the specific internal energy.

The CTS flux jump condition $[\![D\mathcal{M}^{ij}n_i\partial_j\Phi]\!] = \sigma\Phi$ is structurally identical to the Rankine-Hugoniot momentum condition: the jump in the metric-weighted gradient flux (CTS) corresponds to the jump in the pressure-augmented momentum flux (RH). The surface source $\sigma\Phi$ in the CTS plays the role of the surface pressure (the pressure of the membrane itself) in the Rankine-Hugoniot context.

**Key difference:** The Rankine-Hugoniot conditions apply to **moving discontinuities** (the shock travels through the fluid). The ICHTB membranes are static in the quenched approximation (fixed zone boundaries) but can move in the backreaction regime of section 5.2. The moving-membrane CTS junction conditions are exactly the Rankine-Hugoniot conditions applied to the metric discontinuity surface — with the membrane velocity $v_m$ replacing the shock velocity $v_s$. This connection allows the full power of compressible flow theory (Riemann solvers, entropy conditions, Lax conditions) to be applied to the ICHTB membrane dynamics.

---

## Electromagnetic Interface Conditions (Maxwell 1865, Fresnel 1823)

Long before Rankine and Hugoniot, Augustin-Jean Fresnel derived the reflection and transmission coefficients for light at an optical interface (Fresnel 1823, "Mémoire sur la loi des modifications que la réflexion imprime à la lumière polarisée," *Académie des sciences*). Maxwell's electromagnetic theory (Maxwell 1865, *Philosophical Transactions of the Royal Society*, 155, 459) provides the rigorous derivation: at an interface between two dielectrics with permittivities $\epsilon_\alpha$ and $\epsilon_\beta$, the **electromagnetic junction conditions** are:

- **Tangential E continuous:** $[\![\mathbf{E} \times \hat{n}]\!] = 0$
- **Normal D discontinuous by surface charge:** $[\![\mathbf{D} \cdot \hat{n}]\!] = \rho_s$
- **Tangential H continuous:** $[\![\mathbf{H} \times \hat{n}]\!] = \mathbf{K}$ (surface current)
- **Normal B continuous:** $[\![\mathbf{B} \cdot \hat{n}]\!] = 0$

The CTS Condition 1 (continuity of $\Phi$) is the analog of the tangential E continuity — the field (playing the role of the potential) is continuous. The CTS Condition 2 (flux jump) is the analog of the normal D discontinuity — the flux (field gradient weighted by the zone metric, analogous to $\epsilon \mathbf{E}$) jumps by the surface source.

The **Fresnel transmission coefficient** derived from Maxwell's conditions:

$$
T = \frac{2n_\alpha\cos\theta_\alpha}{n_\alpha\cos\theta_\alpha + n_\beta\cos\theta_\beta}
$$

is the electromagnetic analog of the CTS transmission coefficient from section 6.1. Both have the same functional form: the transmitted amplitude depends on the ratio of the impedances ($n\cos\theta$ in optics, $D\mathcal{M}^{nn}k$ in the CTS) on both sides of the interface.

**Key difference:** Maxwell's conditions hold for a vector field ($\mathbf{E}, \mathbf{B}$); the CTS conditions hold for a scalar (complex) field $\Phi$. The CTS conditions are therefore simpler (no polarization effects, no TE/TM distinction), but the anisotropic ICHTB metric $\mathcal{M}^{ij}$ introduces some of the same physics through the direction-dependent diffusion.

---

## Israel Junction Conditions in General Relativity (1966)

Werner Israel's 1966 paper "Singular Hypersurfaces and Thin Shells in General Relativity" (*Il Nuovo Cimento B*, 44, 1) is the general-relativistic treatment of the same junction problem. At a hypersurface $\Sigma$ embedded in a spacetime with metric $g_{\mu\nu}$, the Israel conditions govern the jump in the extrinsic curvature $\mathcal{K}_{\mu\nu}$ of $\Sigma$:

$$
[\![\mathcal{K}_{\mu\nu} - h_{\mu\nu}\mathcal{K}]\!] = -8\pi G\,S_{\mu\nu}
$$

where $h_{\mu\nu}$ is the induced metric on $\Sigma$, $\mathcal{K} = h^{\mu\nu}\mathcal{K}_{\mu\nu}$ is the trace, and $S_{\mu\nu}$ is the surface stress-energy tensor.

The CTS flux jump condition maps to the Israel condition as follows:

| CTS quantity | GR quantity |
|-------------|-------------|
| $D\mathcal{M}^{ij}n_i\partial_j\Phi$ | $\mathcal{K}_{\mu\nu}$ (extrinsic curvature = "normal derivative of the metric") |
| $[\![D\mathcal{M}^{ij}n_i\partial_j\Phi]\!]$ | $[\![\mathcal{K}_{\mu\nu}]\!]$ |
| Surface source $\sigma\Phi$ | Surface stress-energy $8\pi G S_{\mu\nu}$ |
| Zone metric jump $\Delta\mathcal{M}^{ij}$ | Metric jump $(g_{+\mu\nu} - g_{-\mu\nu})|_\Sigma$ |

The CTS membrane formalism is a scalar-field analog of the Israel thin-shell formalism. The Israel conditions were developed for applications in cosmology (bubble nucleation, braneworld models) and black hole physics (shell collapse, wormholes). The CTS applies the same structural formalism to the ICHTB zone boundaries.

**Extensions:** Israel considered hypersurfaces in a fixed spacetime. The CTS, with metric backreaction (section 5.2), is the dynamical generalization: the metric evolves in response to the field (CTS = dynamical backreaction) just as the spacetime geometry evolves in response to the shell stress-energy in GR. The CTS metric evolution equation $\partial_t\mathcal{M}^{ij} = -\beta T^{ij}[\Phi] + \mu\nabla^2\mathcal{M}^{ij}$ is the analog of the Einstein field equations, and the Israel conditions become dynamic: the surface source $S_{\mu\nu}$ generates metric backreaction which moves the membrane.

---

## Transmission Problems in Elliptic PDE Theory (Ladyzhenskaya 1950s, Lions 1972)

The rigorous mathematical theory of junction conditions at interfaces for elliptic partial differential equations — known as **transmission problems** or **interface problems** — was developed by Olga Ladyzhenskaya (see her 1958 book *Boundary Value Problems of Mathematical Physics*) and later by Jacques-Louis Lions and Enrico Magenes (*Non-Homogeneous Boundary Value Problems and Applications*, Springer, 1972).

A transmission problem for an elliptic operator $L$ (the spatial part of the master equation) with discontinuous coefficients across a surface $\Sigma$ is:

$$
L\Phi = f \text{ in } \Omega\setminus\Sigma
$$
$$
[\![\Phi]\!]_\Sigma = 0, \quad [\![\partial_n\Phi]\!]_\Sigma = g
$$

Lions-Magenes proved: for Lipschitz domains and measurable, bounded coefficients, the transmission problem has a unique weak solution in $H^1(\Omega)$ (the Sobolev space of square-integrable functions with square-integrable first derivatives) whenever $f \in L^2(\Omega)$ and $g \in H^{-1/2}(\Sigma)$.

For the CTS, this means: the master equation with ICHTB membranes (the transmission problem with six zones and 12 interface faces) has a **unique weak solution** in $H^1$ for any initial data and any smooth driving. The existence and uniqueness of solutions to the CTS master equation is guaranteed by the Lions-Magenes theorem — the ICHTB boundary conditions are not exotic, they fall squarely within the well-studied class of elliptic transmission problems with the standard functional-analytic theory.

The regularity of the solution near the edges and vertices (sections 6.3 and 6.4) requires more refined analysis — the Lions-Magenes theorem guarantees $H^1$ regularity up to faces, but edges and vertices introduce **corner singularities** (Kondrat'ev 1967, *Transactions of the Moscow Mathematical Society*, 16, 209) where the solution may have weaker regularity. The corner singularity exponents at the ICHTB edges and vertices are determined by the eigenvalues of the Laplacian in the wedge sector — a classical computation that gives the strength of the algebraic singularity at the corner.

For the ICHTB cuboctahedron, the worst-case corner singularity exponent (at the all-positive or all-negative triangular vertex, where the three zone metrics differ most strongly) is:

$$
s^* = \frac{\pi}{\omega_{\max}} = \frac{\pi}{2\pi/3} = \frac{3}{2}
$$

where $\omega_{\max} = 2\pi/3$ is the maximum opening angle at a triangular vertex. This means the field has $H^{3/2-\epsilon}$ regularity near the triangular vertices — not quite $H^2$ (which would allow classical pointwise second derivatives), but well above $H^1$ (which guarantees the energy integral converges). The corner singularity is mild: the field is Hölder continuous but not $C^2$ at the vertices.

---

## Interface Field Theory (Diehl 1986; Cardy 1988)

In statistical field theory, the study of **interface critical phenomena** — phase transitions occurring at a surface or interface rather than in the bulk — was developed by H.W. Diehl (1986, "Field-Theoretical Approach to Critical Behaviour at Surfaces," *Phase Transitions and Critical Phenomena*, Vol. 10) and John Cardy (1988, "Is There a c-Theorem in Four Dimensions?" and subsequent works on boundary conformal field theory).

Diehl classified the possible surface universality classes for an order parameter field with a Ginzburg-Landau bulk theory. At a surface (or interface), the field can satisfy:
- **Ordinary transition:** $\Phi|_\Sigma = 0$ (Dirichlet)
- **Special transition:** $\partial_n\Phi|_\Sigma = 0$ (Neumann)
- **Extraordinary transition:** $\Phi|_\Sigma \neq 0$ before the bulk orders (surface orders first)

The CTS membrane with surface source $\sigma$:
- $\sigma \to \infty$: approaches the Ordinary (Dirichlet) transition
- $\sigma = 0$: is the Special (Neumann) transition
- $\sigma < 0$: supports the Extraordinary transition (the membrane orders first)

The CTS membrane physics is described by Diehl's surface universality class with surface enhancement $\sigma$. The critical behavior at the membrane (the divergence of the membrane correlation length as parameters approach the surface critical point) follows the surface critical exponents computed by Diehl for the O(n) universality class — with $n = 2$ (the two-component complex field $\Phi = \Phi_1 + i\Phi_2$) matching the XY model surface exponents.

Cardy's boundary conformal field theory (BCFT) provides the exact solution of 2D interface problems at criticality using conformal invariance. The ICHTB triangular membrane faces are 2D objects — in the critical limit, their dynamics is governed by BCFT, and Cardy's classification of boundary conditions (the Cardy states in 2D CFT) applies to the CTS membrane faces.

---

## Summary: The CTS in the Context of Prior Work

The ICHTB membrane formalism is not isolated mathematics invented for the CTS. It is the natural synthesis of six independent lines of interface mathematics, each with experimental confirmation in their own domain:

| Field | Authors | Key result used in CTS |
|-------|---------|----------------------|
| Fluid dynamics | Rankine, Hugoniot (1870s) | Jump conditions = flux conservation; moving membranes = shocks |
| Optics | Fresnel (1823), Maxwell (1865) | Transmission coefficient; Snell's law analog |
| General relativity | Israel (1966) | Extrinsic curvature jump = surface stress; backreaction |
| Elliptic PDE theory | Ladyzhenskaya, Lions-Magenes (1950s–72) | Existence/uniqueness of transmission problem solutions |
| Corner singularities | Kondrat'ev (1967) | Vertex regularity; $H^{3/2-\epsilon}$ regularity at triangular vertices |
| Surface field theory | Diehl (1986), Cardy (1988) | Surface universality classes; BCFT at membranes |

The CTS junction formalism is fully grounded in the existing mathematical literature. Every condition derived in sections 6.1–6.4 is a known result applied to the specific geometry of the ICHTB. The ICHTB's novelty is not in its junction conditions — it is in the geometry that determines which conditions apply where, and in the six-zone operator structure that assigns physical meaning to each condition.

