# 9.3 Vortex, Skyrmion, Domain Wall, Dislocation — Full Mathematics

## Four 2D Nonlinear Structures

The 2.B states come in four distinct types, analogous to the four 1D nonlinear structures of section 8.3. In 2D, the extra spatial dimension opens up qualitatively new topological possibilities: the winding number generalizes to higher-dimensional invariants, and the interaction between structures becomes genuinely 2D.

The four 2D nonlinear structures and their topological invariants:

| Structure | Topological invariant | Zone | Physical analog |
|-----------|----------------------|------|-----------------|
| Vortex | Winding number $n \in \mathbb{Z}$ | Memory (−Y) | Magnetic vortex, superconducting fluxon |
| Skyrmion | Skyrmion number $Q \in \mathbb{Z}$ | Memory (−Y) | Magnetic skyrmion, nuclear Skyrmion |
| Domain wall | Topological charge $q = \pm 1$ | Expansion/Compression | Phase boundary, magnetic domain |
| Dislocation | Burgers vector $\mathbf{b}$ | Memory/Expansion | Crystal dislocation, defect line |

---

## The Vortex: Complete Solution

**Governing equation:** The stationary vortex satisfies the time-independent version of the 2.B CGLE:

$$
0 = D_m\left[\partial_r^2f + \frac{1}{r}\partial_rf - \frac{n^2}{r^2}f\right] + \gamma f^3 - \kappa f
$$

This is the **radial Ginzburg-Landau equation** for the vortex amplitude $f(r)$.

**Exact asymptotic solutions:**

For $r \ll \xi$: $f(r) = C_n(n)\left(\frac{r}{\xi}\right)^{|n|}\left[1 + O(r^2/\xi^2)\right]$, where $C_n = \Phi_B\,2^{|n|}\Gamma(1+|n|)/(|n|!\sqrt{2})$ is a normalization constant.

For $r \gg \xi$: $f(r) = \Phi_B\left[1 - \frac{n^2\xi^2}{2r^2} + \frac{n^2\xi^4(3n^2-4)}{8r^4} + O(r^{-6})\right]$

The exact profile (numerically) interpolates between these: $f(r)/\Phi_B$ rises from 0 at $r = 0$ to 1 at $r \sim 3\xi$ (for $n = 1$), overshooting slightly before settling to $\Phi_B$ asymptotically.

**Vortex energy:**

$$
E_n = \pi n^2 D_m\Phi_B^2\ln(R/\xi) + \pi D_m\Phi_B^2 C_{\text{core}}^{(n)}
$$

where $C_{\text{core}}^{(n)} \approx 0.9$ for $n = 1$ and $C_{\text{core}}^{(n)} \approx n^2 \times 0.9$ for general $n$ (core energy grows as $n^2$). Since $E_n \propto n^2$, a multiply-quantized $n = 2$ vortex has four times the energy of an $n = 1$ vortex. It is energetically favorable to split: $\text{1 vortex with } n=2 \to \text{2 vortices with } n=1$. This is the **vortex splitting instability**: high-$n$ vortices are unstable to decay into $|n|$ unit vortices.

**Vortex dynamics:** A vortex in a background field gradient $\nabla|\Phi_0|^2$ moves transversely to the gradient (the **Magnus force**):

$$
\mathbf{v}_{\text{vortex}} = \frac{n}{|\Phi_0|^2}(\hat{z}\times\nabla|\Phi_0|^2)
$$

This is the CTS analog of the Magnus force on a rotating object in a fluid — the vortex drifts perpendicular to the amplitude gradient, not along it. This transverse drift is what makes vortices orbit around each other and spiral in/out in response to the ICHTB geometry.

---

## The Skyrmion: Topology and Stability

**Skyrmion profile:** For the $Q = 1$ skyrmion with helicity $\psi = \pi/2$ (Néel skyrmion, selected by the Memory zone's antisymmetric metric):

$$
\hat{n}(r, \varphi) = \begin{pmatrix} \sin\theta(r)\cos(\varphi + \psi) \\ \sin\theta(r)\sin(\varphi + \psi) \\ \cos\theta(r) \end{pmatrix}, \quad \theta(r) = 2\arctan(r_0/r)
$$

In terms of the collapse field, the skyrmion corresponds to:

$$
\Phi_{\text{sky}}(r, \varphi) = f_{\text{sky}}(r)\exp\!\left(i\Theta_{\text{sky}}(r, \varphi)\right)
$$

where $f_{\text{sky}}(r)$ is the radial amplitude profile and $\Theta_{\text{sky}}$ encodes the full $S^2$ phase structure — not just a simple winding $n\varphi$, but a complicated angle that interpolates between 0 at the center and $2\pi$ at infinity in a helicity-dependent way.

**Skyrmion radius:** The Memory zone's antisymmetric metric parameter $\epsilon$ sets the skyrmion radius via the effective Dzyaloshinskii-Moriya (DM) energy:

$$
E_{\text{DM}} = -2\pi D_m\Phi_B^2\epsilon\,r_0
$$

(This term favors large $r_0$, competing with the exchange energy which favors small $r_0$.) Minimizing the total skyrmion energy $E_{\text{sky}} = E_{\text{exchange}} + E_{\text{DM}} + E_{\text{aniso}}$ gives:

$$
r_0 = \frac{\pi D_m\epsilon}{2\kappa} = \frac{\pi\epsilon\xi^2}{2D_m}
$$

The skyrmion radius is proportional to the antisymmetry parameter $\epsilon$ of the Memory zone metric. For $\epsilon \to 0$: $r_0 \to 0$ (skyrmion collapses — Derrick collapse). For $\epsilon$ finite: stable skyrmion at radius $r_0 \sim \epsilon\xi$.

**Skyrmion number computation:**

$$
Q = \frac{1}{4\pi}\int\hat{n}\cdot(\partial_x\hat{n}\times\partial_y\hat{n})\,d^2x = \frac{1}{2}\left[\cos\theta(0) - \cos\theta(\infty)\right]\cdot\frac{\Delta\varphi}{2\pi}
$$

For the standard skyrmion: $\theta(0) = \pi$ ($\hat{n}$ points down at center), $\theta(\infty) = 0$ ($\hat{n}$ points up), $\Delta\varphi = 2\pi$ (full rotation): $Q = \frac{1}{2}[(-1) - (1)] \cdot 1 = -1$. Sign convention depends on orientation; $|Q| = 1$ is always a unit skyrmion.

---

## The Domain Wall

The 2D domain wall is the 2D extension of the 1D kink (section 8.3). In 2D, a domain wall is a **line** (not a point) separating two regions of different field phase or amplitude.

**Type A domain wall (amplitude wall):** A line separating $|\Phi| \approx \Phi_B$ on one side from $|\Phi| \approx 0$ on the other. This is the boundary between the B-state region (high amplitude) and the A-state region (near vacuum). The profile perpendicular to the wall:

$$
\Phi_{\text{wall}}(x_\perp) = \frac{\Phi_B}{\sqrt{2}}\left[1 + \tanh\!\left(\frac{x_\perp - x_0}{\xi\sqrt{2}}\right)\right]
$$

(half-kink: goes from 0 to $\Phi_B$, rather than the full kink $-\Phi_B$ to $+\Phi_B$). This is the profile of the **B-state/vacuum interface** — the surface of a 3.B topological knot when seen in cross-section.

**Type B domain wall (phase wall):** A line separating $\arg\Phi \approx 0$ on one side from $\arg\Phi \approx \pi$ on the other. The profile is the full 1D kink in the phase direction:

$$
\theta(x_\perp) = \pi\left[1 + \tanh\!\left(\frac{x_\perp - x_0}{\xi_\theta\sqrt{2}}\right)\right]/2
$$

where $\xi_\theta = \sqrt{D_m/\kappa_\theta}$ is the **phase coherence length** (can differ from the amplitude coherence length if the phase and amplitude have different effective stiffnesses).

**Domain wall dynamics:** In 2D, domain walls are **lines** that can curve, move, and interact. The velocity of a curved domain wall with local curvature $\kappa_w$ (not to be confused with the damping $\kappa$):

$$
v_{\text{wall}} = \frac{D_m\kappa_w}{\sqrt{2}}
$$

Curved domain walls flatten out (they move in the direction of decreasing curvature) — they are **mean-curvature flows**. A circular domain wall (bubble) shrinks: $\dot{r}_{\text{bubble}} = -D_m/(r\sqrt{2})$, giving $r(t) = \sqrt{r_0^2 - 2D_m t/\sqrt{2}}$. A bubble collapses in finite time $t_{\text{collapse}} = r_0^2\sqrt{2}/(2D_m)$. This is the 2D "domain wall nucleation and collapse" that appears in first-order phase transitions.

---

## The Dislocation

The dislocation is the 2D topological defect of a **periodic field pattern** — a vortex or phase lattice that has one extra lattice row inserted (an edge dislocation in crystal language). In the CTS context, a dislocation occurs when the phase field $\theta(\mathbf{r})$ has a **Burgers vector** $\mathbf{b}$ — the closure failure of a loop around the defect core:

$$
\mathbf{b} = \oint_C d\theta\,\hat{\nabla}\theta / |\nabla\theta|
$$

For a single-quantum dislocation in a vortex lattice with lattice constant $a$: $|\mathbf{b}| = a$ (one lattice spacing). The dislocation is topologically classified by $\mathbf{b}$, not by a simple integer (unlike the vortex's winding number $n$).

The dislocation in the Memory zone appears when multiple vortices arrange into a **vortex lattice** (Abrikosov lattice, in the superconductivity analog) — a regular array of vortices with uniform spacing $a$. A defect in this lattice is a dislocation.

The **dislocation energy** has the same logarithmic form as the vortex:

$$
E_{\text{disl}} \approx \frac{\pi D_m\Phi_B^2 b^2}{a^2}\ln(R/a)
$$

where $b = |\mathbf{b}|$ is the Burgers vector magnitude and $a$ is the lattice constant.

The dislocation is the 2D structure that connects the Memory zone (vortex physics) to the Expansion zone (pattern formation) — it is a defect in the interface between ordered and disordered 2D phases of the ICHTB.

