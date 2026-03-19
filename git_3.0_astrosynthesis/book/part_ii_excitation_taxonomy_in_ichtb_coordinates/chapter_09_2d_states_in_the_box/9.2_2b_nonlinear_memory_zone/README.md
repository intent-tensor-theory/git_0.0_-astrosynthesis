# 9.2 2.B — Non-Linear: Memory Zone (∇×F)

## The Memory Zone as the Vortex Generator

The Memory zone (−Y) is the host of all 2D nonlinear excitations. Its dominant operator is the curl $\nabla\times\Phi$ — an antisymmetric, rotational operator that naturally selects and amplifies rotational phase structures. While the Expansion zone (+Y) spreads field amplitude isotropically outward (a radially symmetric bloom), the Memory zone organizes field phase into circulating patterns.

The word "Memory" is chosen deliberately: the curl operator is conservative in a sense that makes rotational structures permanent. Once a phase winding exists in the Memory zone, the topological charge (winding number) cannot be removed without globally disrupting the phase pattern. The Memory zone stores rotational information — it is the archive of the ICHTB.

---

## The 2.B Equation of Motion

In the Memory zone (−Y), the metric has dominant antisymmetric components:

$$
\mathcal{M}^{ij}_{-Y} = \begin{pmatrix} m_m & \epsilon m_m & 0 \\ -\epsilon m_m & m_m & 0 \\ 0 & 0 & m_z^{(m)} \end{pmatrix}
$$

where $\epsilon > 0$ is the antisymmetry parameter that controls the curl-dominant character of the Memory zone. The antisymmetric off-diagonal terms $\pm\epsilon m_m$ in the metric generate a preferred rotational direction — they break the left-right symmetry of the spatial transport and drive the field to organize rotationally.

The master equation in the Memory zone, retaining the dominant Memory-zone metric:

$$
\partial_t\Phi = D\left[m_m\nabla_\perp^2\Phi + \epsilon m_m(\partial_y\partial_x - \partial_x\partial_y)\Phi\right] - \Lambda m_m(\nabla_\perp\Phi)^2 + \gamma|\Phi|^2\Phi - \kappa\Phi
$$

The antisymmetric term $\epsilon m_m(\partial_y\partial_x - \partial_x\partial_y)\Phi$ is identically zero for any $\Phi$ with continuous second derivatives (by symmetry of mixed partials). Its role is not to contribute to the bulk evolution, but to **select the boundary conditions** at the Memory zone membranes — the antisymmetric metric generates an effective surface current at the membrane that drives rotational field configurations.

The effective 2.B equation of motion (retaining the nonlinear terms at full amplitude $A \sim \Phi_B$):

$$
\partial_t\Phi = D_m\nabla_\perp^2\Phi - \Lambda_m(\nabla_\perp\Phi)^2 + \gamma|\Phi|^2\Phi - \kappa\Phi
$$

where $D_m = Dm_m$ and $\Lambda_m = \Lambda m_m$. This is the **complex Ginzburg-Landau equation** (CGLE) in 2D — the canonical equation for 2D nonlinear pattern formation.

---

## The Vortex Solution

The CGLE in 2D supports **vortex solutions** — the fundamental 2.B excitation. In polar coordinates $(r, \varphi)$:

$$
\Phi_{\text{vortex}}(r, \varphi) = f(r)e^{in\varphi}
$$

where $n = \pm 1, \pm 2, \ldots$ is the **winding number** (also called the topological charge of the vortex). The amplitude profile $f(r)$ satisfies the radial equation:

$$
D_m\left[f'' + \frac{f'}{r} - \frac{n^2}{r^2}f\right] + \gamma f^3 - \kappa f - \Lambda_m[(f')^2 + (nf/r)^2] = 0
$$

This ODE has the boundary conditions $f(0) = 0$ (the vortex amplitude vanishes at the center — the **vortex core**) and $f(r) \to f_\infty$ as $r \to \infty$ (the amplitude approaches a uniform B-state value far from the core).

The exact amplitude asymptotically:
- **Near the core** ($r \ll \xi$): $f(r) \approx C_n r^{|n|}$ — the field vanishes as a power law, with the core size set by $\xi$
- **Far from core** ($r \gg \xi$): $f(r) \approx \Phi_B\left(1 - \frac{n^2\xi^2}{2r^2} + \ldots\right)$ — the field approaches $\Phi_B$ with algebraically decaying corrections

The **core radius** $r_c \sim \xi = \sqrt{D_m/\kappa}$: the vortex has a central region of radius $\xi$ where the amplitude is suppressed, surrounded by a B-state background of amplitude $\sim \Phi_B$.

The **phase pattern**: $\arg\Phi = n\varphi$ — the phase winds $n$ times around the center as $\varphi$ goes from $0$ to $2\pi$. For $n = +1$: the phase increases by $2\pi$ going counterclockwise (positive vortex). For $n = -1$: the phase decreases by $2\pi$ (negative vortex, or anti-vortex). Vortices with $|n| > 1$ are **multiply quantized** — they carry $n$ units of topological charge.

---

## Vortex Current and Angular Momentum

The **phase current** of the vortex:

$$
\mathbf{J} = \frac{1}{2i}(\Phi^*\nabla\Phi - \Phi\nabla\Phi^*) = f^2(r)\nabla(n\varphi) = \frac{nf^2(r)}{r}\hat{\varphi}
$$

This is a purely azimuthal current — the field flows in circles around the vortex center. The magnitude is $J_\varphi = nf^2(r)/r$: large near the core (where $r$ is small) and decaying as $f^2(r)/r \sim \Phi_B^2/r$ far from the core.

The **total angular momentum** of the vortex (integrated phase current):

$$
L_z = \int J_\varphi\,r\,dr\,d\varphi = 2\pi n\int_0^\infty f^2(r)r\,dr
$$

This integral diverges logarithmically for an ideal vortex in an infinite 2D system (the $1/r$ current has a logarithmically divergent integral). In the finite ICHTB (radius $R$), the angular momentum is:

$$
L_z \approx \pi n\Phi_B^2 R^2\ln(R/\xi)
$$

The logarithmic factor $\ln(R/\xi)$ is characteristic of 2D vortices — it appears in the **vortex energy** as well:

$$
E_{\text{vortex}} \approx \pi n^2 D_m\Phi_B^2\ln(R/\xi) + E_{\text{core}}
$$

where $E_{\text{core}} \sim D_m\Phi_B^2\xi^2/\xi = D_m\Phi_B^2\xi$ is the finite core contribution. The logarithmic energy is the hallmark of 2D vortices — it makes the vortex energy depend on the system size $R$, which is why in infinite 2D systems vortices of opposite charge are always bound in pairs (Kosterlitz-Thouless physics, section 9.4).

---

## The Skyrmion

The skyrmion is the second 2.B structure supported by the Memory zone. It differs from the vortex in that it involves the **full 2D unit vector field** $\hat{n}(\mathbf{r}_\perp) = (\sin\theta\cos\varphi_0, \sin\theta\sin\varphi_0, \cos\theta)$ rather than just the scalar phase.

In the CTS context, the skyrmion arises when the collapse field has both amplitude and phase structure that wrap around the full $S^2$ sphere of field values — not just the $S^1$ circle of phases (as in the vortex), but a map from the 2D plane $\mathbb{R}^2 \cup \{\infty\} \cong S^2$ to the field sphere $S^2$.

The **Skyrmion number** (also called the topological charge):

$$
Q = \frac{1}{4\pi}\int\hat{n}\cdot(\partial_x\hat{n}\times\partial_y\hat{n})\,dx\,dy \in \mathbb{Z}
$$

For the standard skyrmion profile:

$$
\theta(r) = 2\arctan(r_0/r), \quad \varphi_0 = \varphi + \psi
$$

where $r_0$ is the skyrmion radius and $\psi$ is the helicity angle. This profile gives $Q = 1$: the unit vector $\hat{n}$ points down ($-\hat{z}$) at $r = 0$, tilts through the equator at $r = r_0$, and points up ($+\hat{z}$) as $r \to \infty$ — it wraps the $S^2$ exactly once.

The skyrmion is stabilized in the Memory zone by the **Dzyaloshinskii-Moriya interaction** (DMI) analog in the CTS — the antisymmetric metric $\epsilon m_m$ contributes an effective $\mathbf{D}$ vector that selects a preferred helicity $\psi$ for the skyrmion. Without the antisymmetric metric ($\epsilon = 0$), the skyrmion is unstable (it collapses to a point or expands to infinity — Derrick's theorem). With $\epsilon \neq 0$, the Memory zone's chirality stabilizes the skyrmion at a fixed radius $r_0 \sim \xi/\epsilon$.

The skyrmion is a 2D excitation with **both** amplitude and phase topology — it is richer than the vortex (which has only phase topology) and is the 2D precursor of the 3.B topological knot (which adds the third topological dimension).

---

## Memory Zone as Archive: Vortex Gas and Phase Ordering

The Memory zone does not support only individual vortices — it supports a **vortex gas**: a collection of many vortices and anti-vortices in thermal equilibrium. The vortex gas is the 2D analog of the 3D topological knot gas (many Hopfions in the ICHTB).

At low effective temperature $T_{\text{eff}} = D_m/\pi\Phi_B^2$: vortex-anti-vortex pairs are bound (Kosterlitz-Thouless (KT) ordered phase, 2016 Nobel Prize — Kosterlitz & Thouless 1973, *Journal of Physics C*, 6, 1181). The Memory zone in this phase has long-range phase coherence — it is an archive with high fidelity.

At high effective temperature $T_{\text{eff}} > T_{KT} = D_m\Phi_B^2/2\pi$ (the KT transition temperature): free vortices proliferate, destroying the long-range phase coherence. The Memory zone in this phase has short-range order only — it is a chaotic archive, the Kuramoto-Sivashinsky phase described in section 5.5.

The KT transition temperature in the ICHTB:

$$
T_{KT} = \frac{D_m\Phi_B^2}{2\pi} = \frac{D\,m_m\kappa}{2\pi\gamma}
$$

This is the boundary between the "ordered memory" (high-fidelity archive, bound vortex pairs) and "chaotic memory" (turbulent archive, free vortex gas) phases of the Memory zone. The ICHTB can operate in either phase depending on its parameter values $\{D, m_m, \kappa, \gamma\}$.

