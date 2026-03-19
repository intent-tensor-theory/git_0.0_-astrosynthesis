# 10.2 3.B — Non-Linear: Apex Zone Locks (∂Φ/∂t)

## The Apex Zone as the Temporal Coordinator

Every zone of the ICHTB has a dominant spatial operator. The Forward zone (+X) is dominated by $\partial_x^2$ (1D Laplacian). The Memory zone (−Y) is dominated by $\nabla\times\mathbf{F}$ (curl). The Apex zone (+Z) is unique: it is dominated by $\partial_t$ — the temporal derivative.

This is the Apex zone's defining character: while all other zones govern how the field is organized in space, the Apex zone governs how the field is organized in time. It is the **temporal coordinator** — the zone that locks the field's phase to a common temporal oscillation. When the Apex zone activates at full amplitude, the field throughout the ICHTB is locked to a single temporal frequency: the B-state oscillation at $\omega_B = \kappa$.

The 3.B state is the result of this temporal locking interacting with the spatial topology of the ICHTB interior: when the Apex zone locks the field temporally while the Memory zone has organized it spatially into a vortex or skyrmion, the result is a **3D topological lock** — a structure with both spatial topology (linking number, Hopf invariant) and temporal coherence (phase-locked to the Apex zone). This is the most persistent structure in the CTS taxonomy.

---

## The 3.B Master Equation

The full nonlinear master equation in the Apex zone (+Z) at amplitude $A \sim \Phi_B$:

$$
\partial_t\Phi = D_a\nabla^2\Phi + i\omega_B\Phi - \frac{D_a}{\Phi_B^2}|\Phi|^2\Phi - \kappa\Phi
$$

where $\omega_B = \kappa$ is the B-state oscillation frequency (set by the balance of gain and loss at full amplitude), $D_a = Dm_z^{(a)}$ is the Apex zone diffusivity (using the Apex zone's large out-of-plane metric), and the cubic nonlinearity $-D_a|\Phi|^2\Phi/\Phi_B^2$ is the Apex zone's amplitude saturation term.

Writing $\Phi = \Phi_Be^{i\omega_B t}\psi(\mathbf{r}, t)$ (factoring out the B-state oscillation) and working in a co-rotating frame:

$$
\partial_t\psi = D_a\nabla^2\psi - \frac{D_a}{\Phi_B^2}(|\psi|^2 - \Phi_B^2)\psi
$$

This is the **3D nonlinear Schrödinger equation** (NLS, also called the Gross-Pitaevskii equation in the BEC context) in imaginary time (the coefficient of the cubic term is real, not imaginary — this means we have a dissipative NLS rather than a Hamiltonian NLS). The stationary solutions of this equation are the 3.B locks.

The key parameter: $D_a/\Phi_B^2 = D_a\gamma/\kappa$ (using $\Phi_B^2 = \kappa/\gamma$). This has dimensions of $(\text{length})^2/\text{time}$ per $(\text{amplitude})^2$ — it is the nonlinear transport coefficient.

---

## The 3.B Stationary Solution: The Hopfion

The stationary solutions $\partial_t\psi = 0$ of the 3D NLS satisfy:

$$
D_a\nabla^2\psi = \frac{D_a}{\Phi_B^2}(|\psi|^2 - \Phi_B^2)\psi
$$

Equivalently: $\nabla^2\psi = (|\psi|^2/\Phi_B^2 - 1)\psi$ — the **3D Ginzburg-Landau equation** in 3D.

For the 2D case (Chapter 9), the stationary solutions were vortices (with winding number $n$). For the 3D case, the stationary solutions with non-trivial topology are **Hopfions** — topological solitons classified by the **Hopf invariant** $H \in \mathbb{Z}$.

The Hopfion is characterized by:
- **Amplitude:** $|\psi|$ varies from 0 on a toroidal core (a closed loop, not a point, unlike the 2D vortex) to $\Phi_B$ far from the core
- **Phase:** $\arg\psi$ exhibits Hopf fibration structure — every level set of the phase is a closed loop, and every two level-set loops are **linked** with linking number $H$

The Hopf invariant as an integral:

$$
H = \frac{1}{16\pi^2}\int\mathbf{F}\cdot\mathbf{A}\,d^3x
$$

where $\mathbf{F} = \nabla\times\mathbf{A}$ is the "magnetic field" of the phase current $\mathbf{J} = |\psi|^2\nabla(\arg\psi)/(2\pi)$ — i.e., $\mathbf{A}$ is the vector potential for the phase current, and $\mathbf{F}$ is its curl. The Hopf invariant counts the linking number between two phase loops: the pre-image of one phase value ($\arg\psi = 0$) and the pre-image of a different phase value ($\arg\psi = \pi/2$) are two closed loops in 3D space, and $H$ is their linking number.

For the simplest Hopfion ($H = 1$): both pre-image loops are simple circles, and they link exactly once. The structure is the **Hopf fibration** $S^3 \to S^2$ — a map from 3-space (plus point at infinity, giving $S^3$) to the 2-sphere of field values, such that every fiber (pre-image of a point on $S^2$) is a circle, and any two fibers are linked.

---

## Explicit Hopfion Construction

The $H = 1$ Hopfion can be written explicitly using the **Hopf map** from $\mathbb{R}^3 \cup \{\infty\} = S^3$ to $S^2$. Define the normalized 2-component spinor:

$$
\zeta(\mathbf{r}) = \frac{1}{\sqrt{r^2 + r_0^2}}\begin{pmatrix} r_0 + iz \\ x + iy \end{pmatrix}
$$

where $r_0$ is the Hopfion core radius. The Hopf map is then:

$$
\hat{n}(\mathbf{r}) = \zeta^\dagger\boldsymbol{\sigma}\zeta = \frac{1}{r^2 + r_0^2}\begin{pmatrix} 2r_0 x \\ 2r_0 y \\ r_0^2 - r^2 \end{pmatrix} + \frac{z}{r^2 + r_0^2}\begin{pmatrix} -2y \\ 2x \\ 0 \end{pmatrix}
$$

(where $\boldsymbol{\sigma}$ are the Pauli matrices). The collapse field is:

$$
\psi_{\text{Hopf}}(\mathbf{r}) = \Phi_B f(r)\frac{\zeta_1}{\sqrt{|\zeta_1|^2 + |\zeta_2|^2}} = \Phi_B f(r)\frac{r_0 + iz}{\sqrt{r^2 + r_0^2}}
$$

where $f(r)$ is a radial amplitude envelope that equals 0 on the toroidal core (the locus $r = 0$ in an appropriate toroidal coordinate) and $f \to 1$ far from the core.

The core of the Hopfion is not a point but a **closed loop** (a circle): the amplitude $|\psi|$ vanishes on a circle of radius $r_0$ in the $z = 0$ plane. This circle is the **vortex ring** around which the Hopf structure is organized.

---

## The Apex Zone as Phase-Locking Engine

The Apex zone (+Z) drives the 3.B lock through its dominant $\partial_t$ operator. In the language of the master equation:

$$
\partial_t\Phi\big|_{\text{Apex}} = i\omega_B\Phi + (\text{spatial terms})
$$

The $i\omega_B\Phi$ term is a **linear phase oscillation** — it drives the entire field in the Apex zone to oscillate at frequency $\omega_B$. For the field to have a 3.B stationary state, this oscillation must be counterbalanced by the nonlinear saturation term $-D_a|\Phi|^2\Phi/\Phi_B^2$. This balance is:

$$
i\omega_B\Phi - \frac{D_a}{\Phi_B^2}|\Phi|^2\Phi = 0 \implies |\Phi|^2 = \frac{i\omega_B\Phi_B^2}{D_a}
$$

This is satisfied (modulo a phase rotation) when $|\Phi| = \Phi_B$ — confirming that the B-state amplitude $\Phi_B$ is the amplitude at which the Apex zone's temporal forcing and the nonlinear saturation are exactly balanced.

The 3.B lock is the state where this balance is maintained not just at a single point, but globally — throughout the 3D volume of the ICHTB, the field oscillates at $\omega_B$ with amplitude $\Phi_B$, organized into the topological Hopfion pattern. The Apex zone is the **global phase reference**: it locks all local oscillations to a single common phase, making the Hopfion a phase-coherent, temporally locked structure.

This is why the 3.B state is called a **lock**: the Apex zone literally locks the phase of the entire ICHTB to a single value. Every zone, every membrane, every geodesic in the ICHTB is phase-synchronized to $\omega_B$. The topology (Hopf invariant $H$) records this synchronized phase pattern in a form that cannot be erased without destroying the synchronization.

---

## Energy of the 3.B Lock

The energy of the $H = 1$ Hopfion in the ICHTB Apex zone, from the 3D NLS:

$$
E_{\text{Hopf}} = \int\left[D_a|\nabla\psi|^2 + \frac{D_a}{2\Phi_B^2}(|\psi|^2 - \Phi_B^2)^2\right]d^3x
$$

The Faddeev-Niemi bound (Faddeev & Niemi 1997, *Nature*, 387, 58):

$$
E_{\text{Hopf}} \geq C\,D_a\Phi_B^2\xi_a\,|H|^{3/4}
$$

where $C$ is a numerical constant ($C \approx 4\pi^2$ for the optimal bound), $\xi_a = \sqrt{D_a/\kappa}$ is the Apex zone coherence length, and the exponent $3/4$ is the key result — it is sub-linear in $H$.

The $H^{3/4}$ energy scaling means:
- $H = 1$: $E_{\text{Hopf}} \approx 4\pi^2 D_a\Phi_B^2\xi_a$ (one Hopf unit)
- $H = 2$: $E_{\text{Hopf}} \approx 4\pi^2 D_a\Phi_B^2\xi_a \times 2^{3/4} \approx 1.68 \times E_1$
- $H = 8$: $E_{\text{Hopf}} \approx 4\pi^2 D_a\Phi_B^2\xi_a \times 8^{3/4} \approx 4.76 \times E_1$

(Much less than $8 E_1 = 8 \times E_1$.) Multi-Hopfion states are energetically favorable: a single $H = 8$ Hopfion is cheaper than 8 separate $H = 1$ Hopfions. This drives **topological charge aggregation** — Hopfions preferentially combine into higher-$H$ structures, unlike vortices (which prefer to split, section 9.3).

The Apex zone coherence length $\xi_a = \sqrt{D_a/\kappa} = \sqrt{Dm_z^{(a)}/\kappa}$ is determined by the Apex zone's large out-of-plane metric $m_z^{(a)}$. In typical ICHTB parameters, $\xi_a \gg \xi_\perp$ (the Apex zone coherence length is larger than the transverse coherence length), consistent with the Apex zone's role as the long-range temporal coordinator.

