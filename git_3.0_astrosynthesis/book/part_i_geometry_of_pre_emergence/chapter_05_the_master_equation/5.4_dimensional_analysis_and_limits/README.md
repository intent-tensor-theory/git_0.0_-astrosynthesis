# 5.4 Dimensional Analysis and Limits

## The Power of Dimensional Reasoning

The CTS master equation has four parameters: $D$, $\Lambda$, $\gamma$, $\kappa$. These parameters carry physical dimensions, and those dimensions severely constrain the behavior of solutions before any calculation is done. Dimensional analysis — Buckingham's Pi theorem (1914, *Physical Review*, 4, 345) — identifies the independent dimensionless groups that govern the system, reducing four dimensional parameters to a smaller set of dimensionless ratios.

The field $\Phi$ has dimensions $[\Phi] = \Phi_0$ (some field amplitude unit). Space has dimension $L$. Time has dimension $T$.

Dimensional assignments from the master equation:

$$
[\partial_t\Phi] = \Phi_0 T^{-1}
$$
$$
[D\nabla^2\Phi] = [D] L^{-2}\Phi_0 = \Phi_0 T^{-1} \implies [D] = L^2 T^{-1}
$$
$$
[\Lambda(\nabla\Phi)^2] = [\Lambda] L^{-2}\Phi_0^2 = \Phi_0 T^{-1} \implies [\Lambda] = L^2 T^{-1} \Phi_0^{-1}
$$
$$
[\gamma|\Phi|^2\Phi] = [\gamma]\Phi_0^3 = \Phi_0 T^{-1} \implies [\gamma] = \Phi_0^{-2} T^{-1}
$$
$$
[\kappa\Phi] = [\kappa]\Phi_0 = \Phi_0 T^{-1} \implies [\kappa] = T^{-1}
$$

---

## Natural Scales

From the four parameters, three natural scales can be constructed:

**Time scale** (the damping time):
$$
\tau = \frac{1}{\kappa}
$$
This is the time for an A-state perturbation to decay to $1/e$ of its initial amplitude.

**Length scale** (the coherence length):
$$
\xi = \sqrt{\frac{D}{\kappa}}
$$
This is the spatial scale over which the field recovers from a localized perturbation. The coherence length sets the minimum size of a CTS structure: no excitation can be localized to a region smaller than $\xi$ without costing infinite energy. The Ginzburg-Landau coherence length from section 1.5 is exactly this scale.

**Field amplitude scale** (the B-state amplitude):
$$
\Phi_B = \sqrt{\frac{\kappa}{\gamma}}
$$
This is the amplitude at which the cubic term exactly balances the linear damping: $\gamma\Phi_B^2 \cdot \Phi_B = \kappa\Phi_B$. All B states have amplitude of order $\Phi_B$.

---

## The Three Dimensionless Groups

With three natural scales ($\tau$, $\xi$, $\Phi_B$), the four parameters reduce to one independent dimensionless group (plus the trivial group $1$). That group is the **CTS coupling constant**:

$$
g = \frac{\Lambda^2\kappa}{\gamma D^2} = \frac{[\Lambda/D]^2}{[\gamma/\kappa]} = \frac{\text{(flux coupling)}^2}{\text{diffusion} \times \text{cubic stabilization}}
$$

When written in terms of natural scales:

$$
g = \frac{\Lambda^2}{\gamma D} \cdot \frac{1}{D} = \left(\frac{\Lambda\Phi_B}{\xi\kappa}\right)^2 \cdot \frac{\xi^2}{\Phi_B^2} = \frac{\Lambda^2}{D\gamma}
$$

All physical behavior of the CTS master equation depends only on the single dimensionless coupling $g$. The four original parameters set the scales ($\tau$, $\xi$, $\Phi_B$) but only $g$ determines which of the following regimes applies.

---

## The Three Limiting Regimes

### Regime 1: $g \to 0$ (Flux Coupling Negligible)

Setting $\Lambda = 0$ (or equivalently $g \to 0$), the master equation reduces to the **complex Ginzburg-Landau equation** (CGLE):

$$
\partial_t\Phi = D\nabla_i(\mathcal{M}^{ij}\nabla_j\Phi) + \gamma|\Phi|^2\Phi - \kappa\Phi
$$

This is one of the most studied equations in nonlinear dynamics. It supports:
- A-state propagating waves (1.A)
- Abrikosov vortices (2.B) in 2D
- Defect turbulence at large spatial scales

The CGLE does **not** support 1.B solitons or 3.B topological knots — these require the flux coupling term. In the $g = 0$ limit, matter formation (3.B states) is impossible.

This is a strong prediction: the existence of topological matter (stable particles) in the CTS requires $g > 0$. Matter is not possible without flux coupling. The coupling constant $g$ is the parameter of existence for stable particles.

### Regime 2: $g \sim 1$ (Balanced Coupling)

When the flux coupling, diffusion, and cubic stabilization are all in balance, the master equation supports the full A/B state taxonomy simultaneously. All six state classes (1.A through 3.B) are accessible. This is the regime of maximum complexity — where the field can be simultaneously:
- Propagating (1.A/B)
- Circulating (2.B)
- Topologically knotted (3.B)

The transition between state classes is governed by the amplitude relative to $\Phi_B$. The dimensionless quantity $a = A/\Phi_B$ (reduced amplitude) determines the class:

| $a$ | Regime | Dominant states |
|-----|--------|-----------------|
| $a \ll 1$ | Linear (A states) | 1.A, 2.A, 3.A |
| $a \sim 1$ | Nonlinear threshold | 1.B, 2.B |
| $a \gg 1$ | Strongly nonlinear | 3.B, phase locking |

### Regime 3: $g \gg 1$ (Flux Coupling Dominant)

When $\Lambda \gg \sqrt{\gamma D}$, the flux coupling term dominates the spatial dynamics. Setting $D \to 0$ and $\gamma \to 0$ while holding $\Lambda$ and $\kappa$ finite, the equation reduces to:

$$
\partial_t\Phi = -\Lambda\mathcal{M}^{ij}(\nabla_i\Phi)(\nabla_j\Phi) - \kappa\Phi
$$

This is a **Hamilton-Jacobi type equation** for the complex field — it describes the propagation of phase fronts under the influence of the flux coupling and damping, with no diffusive spreading. Solutions are **characteristic curves** (rays) in the ICHTB. The field propagates along these rays until it hits a membrane, at which point the junction conditions of Chapter 2 determine the transmission/reflection.

The $g \gg 1$ limit is the **geometric optics** limit of the CTS: field propagation is ray-like, zone boundaries act as optical interfaces (with Snell's law-analog reflection/refraction conditions), and the ICHTB is a six-faced optical cavity.

---

## Recovery of Known Equations in Specific Limits

The master equation unifies several known equations as special cases:

| Limit | Condition | Recovered equation |
|-------|-----------|-------------------|
| Linear, isotropic $\mathcal{M}$ | $\Lambda = \gamma = 0$, $\mathcal{M}^{ij} = \delta^{ij}$ | Heat equation: $\partial_t\Phi = D\nabla^2\Phi - \kappa\Phi$ |
| Nonlinear, isotropic, $\kappa < 0$ | $\Lambda = 0$, $\mathcal{M}^{ij} = \delta^{ij}$, $\kappa < 0$ | Gross-Pitaevskii (BEC): $i\hbar\partial_t\psi = -\frac{\hbar^2}{2m}\nabla^2\psi + g|\psi|^2\psi$ |
| 1D, $\Lambda > 0$, $\mathcal{M}^{xx}$ only | Soliton-supporting limit | Nonlinear Schrödinger equation (NLSE) |
| Static ($\partial_t\Phi = 0$), isotropic | Time-independent limit | Gross-Pitaevskii / Ginzburg-Landau eigenvalue problem |
| $\Phi$ real, 1D, specific parameter ratios | Traveling wave limit | Fisher-KPP reaction-diffusion (front propagation) |
| $\Lambda = 0$, complex $\Phi$, anisotropic $\mathcal{M}$ | Complex GL with ICHTB metric | CGLE on anisotropic medium |

The master equation contains all of these as exact limits. It is not analogous to any of them — it **contains** them. The ICHTB metric $\mathcal{M}^{ij}$ is the additional structure that distinguishes the master equation from any of its limiting forms: it encodes the six-zone geometry that makes the full A/B taxonomy accessible.

---

## Scale Invariance and the RG Flow

The master equation has a **scale invariance** at the critical point $g = g_c$ where the transition between A and B states occurs. Under the rescaling:

$$
\mathbf{x} \to b\mathbf{x}, \quad t \to b^z t, \quad \Phi \to b^{-\eta/2}\Phi
$$

the master equation transforms with critical exponents $(z, \eta)$ determined by the universality class of the phase transition.

For the CTS master equation in the mean-field approximation:

$$
z = 2, \quad \eta = 0, \quad \nu = \frac{1}{2}
$$

These are the **mean-field critical exponents**, the same as the Ginzburg-Landau / Landau-Wilson universality class (Landau 1937; Wilson & Fisher 1972, *Physical Review Letters*, 28, 240). Kenneth Wilson received the Nobel Prize in Physics in 1982 for the renormalization group framework that explains why critical exponents are universal — why systems as different as superconductors, ferromagnets, and superfluids all have the same critical exponents.

The CTS falls in the Wilson-Fisher universality class in 3D (with corrections from the ICHTB geometry that break full rotational symmetry to the cubic symmetry group O_h). This places the CTS transition in the same universality class as the superfluid-normal transition in helium-4 — one of the most precisely measured phase transitions in experimental physics (Lipa et al., 2003, *Physical Review Letters*, 91, 131). The CTS is not outside the scope of known phase transition physics — it is squarely within it, in the most studied universality class.

