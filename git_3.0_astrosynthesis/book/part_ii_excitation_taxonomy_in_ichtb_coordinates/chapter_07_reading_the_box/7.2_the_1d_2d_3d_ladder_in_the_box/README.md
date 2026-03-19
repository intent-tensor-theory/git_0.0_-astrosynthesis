# 7.2 The 1D→2D→3D Ladder in the Box

## Three Levels of Spatial Organization

Within each of the A and B state classes, there is a second axis of classification: the **spatial dimensionality** of the excitation. This is not the dimensionality of the ICHTB (which is always 3D) but the dimensionality of the excitation **within** the ICHTB — how many spatial degrees of freedom the excitation actively uses to organize itself.

The three levels are:

- **1D (one-dimensional):** The excitation is organized along a single spatial direction — a tube, a ray, a line. Its cross-section perpendicular to the organizing direction is approximately uniform. The excitation has a "front" and "back" along one axis and extends freely in the transverse directions (or is bounded by the ICHTB geometry).

- **2D (two-dimensional):** The excitation is organized over a surface — a disc, a ring, a vortex sheet. It has internal structure in two spatial dimensions and extends freely in the third (the normal to the surface), or is bounded.

- **3D (three-dimensional):** The excitation occupies a volume — a blob, a knot, a Hopfion. All three spatial degrees of freedom are actively organized, and the excitation has a definite extent in all three directions simultaneously.

Combined with the A/B split, this gives the full **six-class taxonomy**:

| | 1D | 2D | 3D |
|---|---|---|---|
| **A (linear)** | 1.A: signal/wave | 2.A: bloom/disc | 3.A: standing mode |
| **B (nonlinear)** | 1.B: soliton | 2.B: vortex | 3.B: topological knot |

These six classes are not merely descriptive categories — each one corresponds to a definite location in the ICHTB, governed by a specific zone combination.

---

## The Dimensional Ladder as a Zone Axis

The 1D→2D→3D ladder maps to a specific axis through the ICHTB. To identify it, recall the zone operators:

- The **Forward zone (+X)** is the 1D zone: its dominant operator $\partial_x\Phi$ is a directional derivative along $\hat{x}$ — pure 1D structure.
- The **Expansion zone (+Y)** is the 2D zone: its dominant operator $\nabla^2\Phi$ generates isotropic spreading in all directions — but the leading-order expansion of a field from a point source in 2D before reaching 3D involves the $\hat{y}$ transverse plane, the Expansion zone's natural domain.
- The **Apex zone (+Z)** is where the transition from 2D to 3D occurs — the $\hat{z}$ axis carries the excitation from the 2D disc (Expansion zone plane) into full 3D volume.

More precisely, the **dimensional ladder is read in the hat-address system** (Chapter 4). A Level-1 address is a single zone designation — a 1D structure. A Level-2 address combines two zones — a 2D structure. A Level-3 address combines all three positive zones — a 3D structure.

| Dimensional level | Hat address level | Zone combination |
|------------------|------------------|-----------------|
| 1D excitation | Level 1 | Single zone (one axis) |
| 2D excitation | Level 2 | Two zones (two axes) |
| 3D excitation | Level 3 | Three zones (three axes) |

The 1D→2D→3D ladder is exactly the Level-1→Level-2→Level-3 hat address hierarchy. Moving up the ladder means involving more zones — more ICHTB axes — in the excitation's self-organization.

---

## The A-State Ladder (Linear Excitations at Each Level)

**1.A: Signals (1D linear)**

A Level-1 hat address in the positive zone direction: e.g., $(+X)$. The excitation is a propagating wave along $\hat{x}$, governed by the Forward zone operator $\partial_x\Phi$. In the linear (A-state) regime, this is a plane wave:

$$
\Phi_{1.A}(x, t) = A_0 e^{i(kx - \omega t)}e^{-\kappa t/2}
$$

with dispersion relation $\omega = Dk^2$ (diffusive) modified by the Forward zone metric: $\omega = D\mathcal{M}^{xx}_{+X}k^2$. The $e^{-\kappa t/2}$ factor is the damping — A-state signals decay exponentially in time. They exist only transiently.

The signal propagates along a single axis (1D) and decays away from it (the transverse directions are governed by the Core zone, which damps them). This is a **pure directional signal** — the simplest possible CTS excitation.

**2.A: Blooms (2D linear)**

A Level-2 hat address: e.g., $(+X+Y)$. The excitation combines Forward zone propagation with Expansion zone spreading — it is a disc that grows in the plane perpendicular to $\hat{z}$ while propagating along $\hat{x}$ and spreading in $\hat{y}$. The governing equation in the Expansion zone is dominated by $+\nabla^2\Phi$, producing isotropic growth from the origin outward.

In the linear regime, the bloom is a **Gaussian wave packet** in 2D:

$$
\Phi_{2.A}(\mathbf{r}_\perp, t) = \frac{A_0}{\sqrt{4\pi Dt}}\exp\!\left(-\frac{r_\perp^2}{4Dt} - \kappa t\right)
$$

where $\mathbf{r}_\perp$ is the transverse 2D coordinate and $D$ is the Expansion-zone diffusivity. The bloom spreads as $r \sim \sqrt{Dt}$ while decaying overall. This is a transient growing-then-decaying disc — the 2.A state.

**3.A: Standing Modes (3D linear)**

A Level-3 hat address: $(+X+Y+Z)$ — the all-positive vertex. The excitation occupies all three positive zones simultaneously, filling the ICHTB volume. In the linear regime, these are the **normal modes** of the CTS master equation in the ICHTB — standing waves that are eigenfunctions of the spatial operator $D\nabla_i(\mathcal{M}^{ij}\nabla_j)$.

These standing modes are labeled by three quantum numbers (corresponding to the three spatial dimensions) and decay exponentially with rate $\kappa$. They are the CTS analog of the normal modes of a resonant cavity — the harmonics of the box.

---

## The B-State Ladder (Nonlinear Excitations at Each Level)

**1.B: Solitons (1D nonlinear)**

A Level-1 address in the Compression zone (−X): a nonlinear, self-sustaining pulse that propagates along a single axis without dispersion or decay. The soliton balance:

$$
\text{Diffusion spreading} + \text{Nonlinear self-focusing} + \text{Damping} + \text{Gain from cubic} = 0
$$

This balance is achieved when the amplitude profile takes the **sech form**:

$$
\Phi_{1.B}(x, t) = A_{1.B}\,\text{sech}\!\left(\frac{x - vt}{\xi_{1.B}}\right)e^{i(qx - \Omega t)}
$$

with $A_{1.B} \sim \Phi_B$, width $\xi_{1.B} \sim \xi = \sqrt{D/\kappa}$, velocity $v$ determined by the flux coupling $\Lambda$, and phase $\Omega$ determined by the balance condition. The sech profile is the exact 1D soliton solution — it is a Level-1 hat-address excitation in the Compression zone (−X), moving along the $\hat{x}$ axis.

**2.B: Vortices (2D nonlinear)**

A Level-2 address in the Memory zone plane: $(−Y+?)$. The vortex is a 2D nonlinear excitation — a circular phase pattern in the $(\hat{x}, \hat{y})$ plane with a topological winding number $n = \pm 1, \pm 2, \ldots$. The vortex profile:

$$
\Phi_{2.B}(r, \theta) = f(r)e^{in\theta}
$$

where $(r, \theta)$ are polar coordinates in the 2D plane and $f(r)$ is the amplitude profile: $f(0) = 0$ (the vortex core vanishes at the center), $f(r) \to \Phi_B$ as $r \to \infty$. The topological charge $n$ is an integer, invariant under any continuous deformation of the field — this is what makes the vortex persistent.

The Memory zone (−Y) with its antisymmetric operator $\nabla\times$ is the natural host of vortex excitations: the curl operator directly supports rotational phase patterns. The Memory zone is the "vortex zone" of the ICHTB.

**3.B: Topological Knots (3D nonlinear)**

A Level-3 address in the Compression + Memory zone combination: $(−X−Y−Z)$ — the all-negative vertex. The topological knot (Hopfion) is a 3D nonlinear excitation in which the phase field $e^{i\theta(\mathbf{x})}$ forms a Hopf-linked pattern — closed loops of constant phase that are topologically linked to each other (like the links of a chain). The Hopf invariant:

$$
H = \frac{1}{16\pi^2}\int \mathbf{F}\cdot\mathbf{A}\,d^3x
$$

(where $\mathbf{F} = \nabla\times\mathbf{A}$ is the field-strength 2-form of the phase current) is an integer topological invariant that cannot change without cutting and reconnecting the phase loops. The 3.B state is an integer-classified topological excitation — the most rigid of all CTS structures.

---

## The Dimensional Ladder and Energy

The six states are arranged in a natural energy hierarchy. Roughly:

$$
E_{1.A} < E_{2.A} < E_{3.A} < E_{1.B} < E_{2.B} < E_{3.B}
$$

Each step up the ladder costs energy: moving from 1D to 2D to 3D organization requires more degrees of freedom to be coherently structured. Moving from A to B costs additional energy to overcome the bifurcation threshold.

The 3.B state (topological knot) has the highest energy and the highest stability. It is the most expensive to create and the most durable once created — a natural description of what we call **matter**: highly structured, energetically costly, self-sustaining.

The 1.A state (signal) has the lowest energy and the lowest stability (it decays exponentially). It is cheap to create and transient — the description of a **message**: low-energy, propagating, vanishing after delivery.

The ladder from signal to matter is the energy ladder from bottom to top of the taxonomy.

