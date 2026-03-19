# 9.1 2.A — Linear: Expansion/Compression Plane

## The 2D Domain of the ICHTB

Chapter 8 treated the 1D states — excitations organized along a single axis, governed by the Forward and Compression zones. Now we move to the 2D states: excitations organized over a plane, governed by the Expansion zone (+Y) and bounded by the Compression zone (−X).

The 2.A state is the linear 2D excitation — a small-amplitude field that spreads over a surface inside the ICHTB. In section 7.2, this was called the "bloom": an isotropically spreading Gaussian disc. Here we go further, treating the full spectrum of linear 2D modes — not just the ground-state Gaussian bloom, but the complete set of surface harmonics, their dispersion, their transmission through the zone membranes, and the role of the Compression zone in bounding the 2D domain.

---

## The 2D Master Equation in the Expansion Zone

In the Expansion zone (+Y), the metric is isotropic in the $(\hat{x}, \hat{y})$ plane:

$$
\mathcal{M}^{ij}_{+Y} = \begin{pmatrix} m_{\text{Exp}} & 0 & 0 \\ 0 & m_{\text{Exp}} & 0 \\ 0 & 0 & m_z \end{pmatrix}, \quad m_{\text{Exp}} \gg m_z
$$

The large in-plane metric $m_{\text{Exp}}$ amplifies both $\partial_x^2\Phi$ and $\partial_y^2\Phi$, making this zone the natural domain of 2D isotropic spreading. The small out-of-plane metric $m_z$ suppresses $\partial_z^2\Phi$ — the field is essentially confined to the $(\hat{x}, \hat{y})$ plane in this zone.

In the small-amplitude (A-state) limit, the master equation in the Expansion zone:

$$
\partial_t\Phi = D\,m_{\text{Exp}}\nabla_\perp^2\Phi + D\,m_z\partial_z^2\Phi - \kappa\Phi
$$

where $\nabla_\perp^2 = \partial_x^2 + \partial_y^2$ is the 2D Laplacian. Define $D_\perp = Dm_{\text{Exp}}$ and $D_z = Dm_z \ll D_\perp$. The 2D limit ($D_z \to 0$) gives the **2D heat equation with damping**:

$$
\partial_t\Phi = D_\perp\nabla_\perp^2\Phi - \kappa\Phi
$$

This is a well-studied equation whose solutions form the complete 2D theory of the 1.A/2.A states in the Expansion zone.

---

## 2D Mode Spectrum: Surface Harmonics

In polar coordinates $(r, \varphi)$ in the 2D plane, the eigenmodes of the 2D Laplacian $\nabla_\perp^2$ are:

$$
\Phi_{nm}(r, \varphi) = J_n(k_m r)e^{in\varphi}
$$

where $J_n(kr)$ is the Bessel function of the first kind of order $n$ (Bessel 1824), $n = 0, \pm 1, \pm 2, \ldots$ is the **angular quantum number** (number of azimuthal oscillations), and $k_m$ is the $m$-th zero of the Bessel function $J_n(k_m R) = 0$ at the ICHTB membrane radius $R$ (imposing the boundary condition at the zone membrane).

The dispersion relation for 2D modes:

$$
\omega_{nm} = iD_\perp k_m^2 + i\kappa
$$

All modes are purely decaying (imaginary $\omega$, consistent with the A-state character). The **lowest mode** ($n = 0$, $m = 1$): the $J_0(k_1 r)$ mode is the radially symmetric ground state — a smooth dome profile that peaks at $r = 0$ and vanishes at the membrane radius $R$. This is the **2D version of the Gaussian bloom** (for a bounded domain; in an unbounded domain, the Gaussian is the free-space analog).

The angular modes $n \neq 0$ are **petal structures**: $J_n(kr)e^{in\varphi}$ has $2n$ petals arranged symmetrically around the center. These are the 2D surface harmonics — the analog of spherical harmonics on a flat disc. They carry **angular momentum** $L_z = n\hbar$ per quantum of excitation (in the quantum CTS interpretation).

The **2D mode table** for the ICHTB Expansion zone:

| Mode $(n, m)$ | Profile | Angular momentum | Character |
|--------------|---------|-----------------|-----------|
| $(0, 1)$ | $J_0(k_1 r)$ | $0$ | Symmetric bloom |
| $(0, 2)$ | $J_0(k_2 r)$ | $0$ | Bloom with one radial node |
| $(\pm 1, 1)$ | $J_1(k_1 r)e^{\pm i\varphi}$ | $\pm 1$ | Dipole mode |
| $(\pm 2, 1)$ | $J_2(k_1 r)e^{\pm 2i\varphi}$ | $\pm 2$ | Quadrupole mode |
| $(\pm n, m)$ | $J_n(k_m r)e^{\pm in\varphi}$ | $\pm n$ | $2n$-pole, $m$-th radial harmonic |

These modes are the **2.A state spectrum** — the complete set of linear 2D excitations in the ICHTB Expansion zone.

---

## The Compression Zone as Boundary

The Compression zone (−X) plays a dual role in the 2D physics. It is not only the host of 1D nonlinear excitations (Chapter 8) but also the **outer boundary** that confines the 2D bloom — the Expansion zone is the interior, and the Compression zone forms the exterior boundary.

The Expansion/Compression transition does not occur as a direct membrane (opposite zones are not adjacent in the cuboctahedron). Instead, the Expansion zone's outer boundary is formed by the Apex, Memory, and Core zones that surround it. But the Compression zone exerts an effective **negative-curvature pressure** on the 2D modes — the inverted Laplacian $-\nabla^2\Phi$ in the Compression zone acts as a focusing potential for the field, compressing the 2D bloom back toward its center.

The effective potential seen by the 2D field near the Compression-adjacent membrane:

$$
V_{\text{eff}}(r) = -D_x m_{\text{Comp}}\nabla^2\Phi/\Phi \approx D_x m_{\text{Comp}}\,k_\perp^2
$$

This is a positive, wavenumber-dependent potential — it raises the effective energy of high-$k$ (small-scale) modes more than low-$k$ modes. Combined with the Expansion zone's $+\nabla^2\Phi$ spreading, the system has a natural **energy balance**: modes with $k \sim 1/\xi$ experience zero net potential (Expansion spreading cancels Compression focusing), while modes with $k > 1/\xi$ are focused and $k < 1/\xi$ modes spread.

This balance at $k = 1/\xi$ is the 2D analog of the 1D soliton balance condition (section 8.2). But here it applies to a 2D linear mode — it is the condition for a 2.A **stationary** mode (one that neither spreads nor compresses). The $k = 1/\xi$ mode is the **2D critical mode** — the neutral mode between spreading and compression.

---

## Membrane Transmission for 2D Modes

Each 2D mode $(n, m)$ has a different transmission coefficient at the zone membranes, because the azimuthal angular momentum $n$ affects how the mode interacts with the membrane geometry. The transmission coefficient at a membrane with surface conductance $\sigma$, for a mode with angular quantum number $n$:

$$
T_n(k) = \frac{4D_\perp^2 k^2}{4D_\perp^2 k^2 + \sigma^2(1 + n^2/k^2R^2)}
$$

The additional factor $(1 + n^2/k^2R^2)$ reflects the **centrifugal barrier** for angular-momentum-carrying modes: modes with $n \neq 0$ experience an effective barrier proportional to $n^2$ that reduces their transmission relative to the $n = 0$ symmetric mode.

Consequence: the zone membranes are **angular-momentum-selective filters**. The $n = 0$ (symmetric) bloom is most easily transmitted; high-$n$ (high angular momentum) modes are progressively suppressed. The ICHTB preferentially propagates isotropic signals over rotating ones — another expression of the Core zone's preference for the symmetric vacuum.

---

## The 2D Green's Function

The response to a point source $\Phi(\mathbf{r}_\perp, 0) = \Phi_0\xi^2\delta^{(2)}(\mathbf{r}_\perp)$ at the center of the Expansion zone:

$$
G(\mathbf{r}_\perp, t) = \frac{\Phi_0\xi^2}{4\pi D_\perp t}\exp\!\left(-\frac{r_\perp^2}{4D_\perp t} - \kappa t\right)
$$

The **peak amplitude** at the center ($r_\perp = 0$):

$$
G(0, t) = \frac{\Phi_0\xi^2}{4\pi D_\perp t}e^{-\kappa t}
$$

This decays as $1/(t e^{\kappa t})$ — faster than the 3D case ($1/t^{3/2}$) but slower than the 1D case ($1/\sqrt{t}$). The bloom reaches its maximum radius at $t_{\max} = 1/\kappa$ (when the exponential decay begins to dominate the algebraic spreading), giving:

$$
r_{\max} = \sqrt{4D_\perp t_{\max}} = 2\sqrt{D_\perp/\kappa} = 2\xi_\perp
$$

The maximum bloom radius is twice the 2D coherence length $\xi_\perp = \sqrt{D_\perp/\kappa}$. For a bloom to reach the zone membrane (at radius $R$), the coherence length must satisfy $\xi_\perp \gtrsim R/2$. This is the **2D emergence condition** — the same form as the 1D condition but applied to the transverse coherence length.

