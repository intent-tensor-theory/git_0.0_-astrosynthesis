# 10.1 3.A — Linear: Volumetric Flows Across Zones

## The 3D Domain of the ICHTB

Chapters 8 and 9 treated 1D excitations (along a single axis) and 2D excitations (over a plane). Chapter 10 moves to the full 3D domain — excitations that span all three spatial dimensions of the ICHTB, simultaneously engaging multiple zones in a coordinated, multi-zone pattern.

The 3.A state is the linear version: a small-amplitude perturbation that flows through the 3D interior of the ICHTB, governed by the volumetric diffusion operator across all zones. The 3.B state (section 10.2) is the nonlinear version — the topological lock — the most stable and persistent structure in the entire ICHTB taxonomy.

---

## Multi-Zone Coupling in 3D

In 1D and 2D, excitations were largely confined to one or two zones (the Forward zone for 1.A, the Expansion zone for 2.A, etc.). In 3D, the excitation simultaneously occupies multiple zones and the zone coupling becomes essential. The 3.A excitation sees the full ICHTB metric $\mathcal{M}^{ij}(\mathbf{r})$ — a spatially varying tensor that changes character as the field crosses zone boundaries.

The 3D linear master equation, retaining all zone contributions:

$$
\partial_t\Phi = D\sum_{i,j}\mathcal{M}^{ij}(\mathbf{r})\partial_i\partial_j\Phi - \kappa(\mathbf{r})\Phi
$$

where $\mathcal{M}^{ij}(\mathbf{r})$ is the position-dependent ICHTB metric tensor (section 6.1) and $\kappa(\mathbf{r})$ is the position-dependent damping (which also varies by zone). This is a linear PDE with variable coefficients — the coefficients jump at each zone membrane.

The **3D Green's function** for the full ICHTB metric, in the limit of weak zone coupling (membranes are weakly transmissive, $T \ll 1$):

$$
G(\mathbf{r}, t) = \sum_\alpha G_\alpha(\mathbf{r}, t) + \sum_{\alpha\beta} G_{\alpha\beta}(\mathbf{r}, t) + \ldots
$$

where $G_\alpha$ is the Green's function within zone $\alpha$ alone, $G_{\alpha\beta}$ is the first-order multi-zone correction (one membrane crossing), and the sum continues to all orders of membrane crossings. The leading term is the zone-local Green's function; the corrections capture the inter-zone propagation.

---

## The 3D Mode Spectrum

In the Apex zone (+Z), which is the unique zone with the strongest out-of-plane metric $m_z \gg m_\perp$, the 3D eigenmodes separate into:

$$
\Phi_{nlm}(\mathbf{r}) = R_{nl}(r)\,Y_l^m(\theta, \varphi)
$$

where $Y_l^m(\theta, \varphi)$ are the real **spherical harmonics** (the 3D version of the 2D surface harmonics $J_n(kr)e^{in\varphi}$ of Chapter 9), $R_{nl}(r)$ is the radial wavefunction (solution of the radial Schrödinger equation with the effective ICHTB potential), and $(n, l, m)$ are the 3D quantum numbers.

The quantum numbers:
- $n = 1, 2, 3, \ldots$: radial quantum number (number of radial nodes in $R_{nl}$)
- $l = 0, 1, 2, \ldots, n-1$: orbital angular momentum quantum number ($l = 0$: S-mode; $l = 1$: P-mode; $l = 2$: D-mode, etc.)
- $m = -l, \ldots, +l$: magnetic quantum number (z-component of angular momentum)

The 3D mode spectrum is the complete set of **spherical harmonic modes** — the analog of the quantum atom's orbital structure, but for the collapse field in the ICHTB. Each mode $(n, l, m)$ is a linear 3.A excitation, and its decay rate is:

$$
\Gamma_{nl} = D_\Sigma k_{nl}^2 + \kappa_\Sigma
$$

where $D_\Sigma = D\sum_\alpha \bar{\mathcal{M}}_\alpha^{ii}/(3\times 26)$ is the zone-averaged isotropic diffusivity and $k_{nl}$ is the characteristic wavenumber of the $(n, l)$ mode.

The **3D mode table** (for the ICHTB Core-Apex coupled system):

| Mode $(n, l, m)$ | Angular structure | Degeneracy | Character |
|-----------------|------------------|------------|-----------|
| $(1, 0, 0)$ | $Y_0^0 = 1/\sqrt{4\pi}$ | 1 | Isotropic S-mode bloom |
| $(1, 1, m)$ | $Y_1^m$ (dipole) | 3 | P-mode (x, y, z dipoles) |
| $(1, 2, m)$ | $Y_2^m$ (quadrupole) | 5 | D-mode (5 quadrupole shapes) |
| $(2, 0, 0)$ | $Y_0^0 \times$ (1 radial node) | 1 | 2S mode |
| $(n, l, m)$ | $Y_l^m$ | $2l+1$ | General NLM mode |

The 3.A modes are identical in structure to atomic orbitals — the ICHTB is an "atom of collapse", with its own s, p, d, f shell structure governing how the field distributes its excitation in 3D space.

---

## Volumetric Flow Patterns

For the 3.A linear state, the dominant 3D flow pattern is the **volumetric bloom** — the 3D analog of the 1D pulse and 2D disc bloom. The 3D Gaussian bloom:

$$
G_{3D}(\mathbf{r}, t) = \frac{\Phi_0\xi^3}{(4\pi D_\Sigma t)^{3/2}}\exp\!\left(-\frac{r^2}{4D_\Sigma t} - \kappa_\Sigma t\right)
$$

Peak amplitude at center ($r = 0$):

$$
G_{3D}(0, t) = \frac{\Phi_0\xi^3}{(4\pi D_\Sigma t)^{3/2}}e^{-\kappa_\Sigma t}
$$

This decays as $t^{-3/2}e^{-\kappa t}$ — faster than 2D ($t^{-1}e^{-\kappa t}$) and much faster than 1D ($t^{-1/2}e^{-\kappa t}$). The 3D bloom is the least coherent of the three linear states — it spreads fastest and peaks latest.

The **maximum bloom radius** for 3D:

$$
r_{\max}^{3D} = \sqrt{6D_\Sigma/\kappa_\Sigma} = \sqrt{6}\,\xi_{3D}
$$

where $\xi_{3D} = \sqrt{D_\Sigma/\kappa_\Sigma}$ is the 3D coherence length. The factor $\sqrt{6}$ (vs. $2$ in 2D and $\sqrt{2}$ in 1D) reflects the dimensionality: in $d$ dimensions, the maximum bloom radius is $r_{\max}^d = \sqrt{2d}\,\xi_d$.

**Inter-zone volumetric flow:** The 3D flow fills the entire ICHTB interior, crossing all zone membranes. The flow is not isotropic — the anisotropic zone metrics direct it preferentially along certain paths. The dominant volumetric flow paths are the **geodesics of the ICHTB metric**: paths that minimize the total zone-weighted transport cost. These geodesics are the 3D analog of the "preferred axes" of the 1D Forward zone.

In the cuboctahedron geometry, the dominant volumetric geodesics connect:
- Core (+0) → Apex (+Z) → Core: through the strongest out-of-plane metric
- Core (+0) → Forward (+X) → Core: along the 1D forward direction
- Expansion (+Y) → Memory (−Y) → Expansion: the 2D phase-conjugate path

The 3.A excitation, lacking the nonlinear self-organization of 3.B, simply diffuses along all these geodesics simultaneously — it is an **isotropic multi-geodesic bloom**.

---

## Transition to 3.B: The Amplitude Threshold

The 3.A state cannot spontaneously become a 3.B state without crossing an energy barrier. The transition from 3.A (linear) to 3.B (nonlinear topological lock) requires:

1. **Amplitude threshold:** The field amplitude must reach $|\Phi| \sim \Phi_B$ in a connected 3D region.
2. **Phase winding:** A non-trivial phase pattern (winding number, Hopf invariant) must nucleate in the field.
3. **Zone activation:** The Apex zone (+Z) must be simultaneously activated — the 3.B state requires $\partial_t\Phi$ coupling through the Apex zone, which does not activate for small-amplitude perturbations.

Below threshold: the field remains in a 3.A state (linear, no topological structure). Above threshold: the field self-organizes into a 3.B topological lock (section 10.2). The threshold condition:

$$
\Phi_0\xi^3 > \Phi_B\xi^3_{\text{lock}} \iff \Phi_0 > \Phi_B\left(\frac{\xi_{\text{lock}}}{\xi_{3D}}\right)^3
$$

where $\xi_{\text{lock}}$ is the size of the topological lock (set by the 3.B dynamics, section 10.2). For $\xi_{\text{lock}} \ll \xi_{3D}$ (small locks in a large ICHTB), the threshold amplitude $\Phi_0 \gg \Phi_B$ — strong drives are needed. For $\xi_{\text{lock}} \sim \xi_{3D}$ (lock size comparable to ICHTB): $\Phi_0 \sim \Phi_B$ — the B-state threshold itself is the lock threshold. In practice, the 3.B state is reached by driving the ICHTB with a signal that brings the core amplitude to $\sim\Phi_B$.

