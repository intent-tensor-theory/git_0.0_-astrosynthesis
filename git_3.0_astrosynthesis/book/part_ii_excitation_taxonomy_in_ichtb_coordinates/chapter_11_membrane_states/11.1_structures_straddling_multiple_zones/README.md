# 11.1 Structures Straddling Multiple Zones

## Beyond Single-Zone Excitations

Chapters 8–10 classified excitations by their host zone: 1D excitations in the Forward/Compression zones, 2D excitations in the Expansion/Memory zones, 3D excitations in the Apex zone. Each excitation was primarily localized in one zone, with small corrections from adjacent zones.

Chapter 11 treats a different class: **membrane states** — excitations that are intrinsically multi-zone, simultaneously occupying two or more zones straddled across a zone interface. These structures are not perturbatively localized in one zone with small corrections from others; they are fundamentally bi-zonal or multi-zonal, and their defining properties emerge from the zone boundary itself.

The membrane state is to the zone interface what the vortex is to the Memory zone core: the natural excitation of that region. Just as the Memory zone interior has vortices as its ground-state excitations, the zone interfaces have membrane states as their natural excitations.

---

## What Makes a Membrane State

A membrane state is defined by three properties:

1. **Bi-zonal support:** The field amplitude $|\Phi|$ is significant in two or more adjacent zones simultaneously. Unlike bulk excitations (which have $|\Phi| \ll 1$ at zone boundaries), membrane states peak at or near the zone boundary.

2. **Interface-driven dynamics:** The dominant restoring force is not the bulk metric of either zone but the **impedance mismatch** at the membrane — the discontinuity in $\mathcal{M}^{ij}$ at the zone boundary. The membrane state is the field configuration that extremizes the energy of this impedance mismatch.

3. **Hybrid character:** The membrane state inherits properties from both adjacent zones. A state at the Forward(+X)/Memory(−Y) interface inherits the 1D propagating character of the Forward zone and the 2D rotating character of the Memory zone simultaneously — it is a propagating spiral, a helical mode.

---

## Zone Interface Topology in the ICHTB

The cuboctahedron has 24 triangular faces (but zero — it has 8 triangular and 6 square faces; 14 total) and 24 edges. In the ICHTB zone assignment, the 12 zones share 24 interfaces (each zone has 4 adjacent zones in the cuboctahedral topology). These 24 interfaces group by symmetry:

**Type A interfaces (same-sign zones):** Interfaces between zones of the same sign character (both positive or both negative). Example: Forward (+X) / Expansion (+Y) interface. These interfaces have moderate impedance mismatch — both zones have large positive metric components, so the mismatch is a ratio $m_{\text{Exp}}/m_{\text{Fwd}}$ rather than an order-of-magnitude jump.

**Type B interfaces (sign-crossing zones):** Interfaces between positive and negative zones. Example: Forward (+X) / Compression (−X) interface. These interfaces have large impedance mismatch — the metric changes sign (from large positive to large negative), creating a strong reflecting barrier. Membrane states at Type B interfaces are especially stable because the barrier traps them.

**Type C interfaces (involving the Core +0):** Interfaces between the Core and any of the 12 outer zones. These are special: the Core zone has the isotropic metric (all components equal), so the impedance mismatch with any outer zone is set by the outer zone's anisotropy. The Core interfaces are the "gentle" interfaces of the ICHTB — less reflective but also less trapping.

**Type D interfaces (involving the Null −0):** Interfaces between the Null zone (all negative metric) and adjacent zones. These are the most extreme interfaces — the Null zone has all-negative metric, so any adjacent zone represents a complete sign flip. Null interfaces have the largest impedance mismatch and the deepest membrane-state trapping potential.

---

## The Bi-Zonal Field Ansatz

For a membrane state at the interface between zones $\alpha$ (left side, $x < 0$) and $\beta$ (right side, $x > 0$), the field takes the form:

$$
\Phi_{\text{mem}}(\mathbf{r}) = \begin{cases} A_\alpha(\mathbf{r}_\perp) e^{iq_\alpha x} + \text{c.c.} & x < 0 \\ A_\beta(\mathbf{r}_\perp) e^{iq_\beta x} + \text{c.c.} & x > 0 \end{cases}
$$

where $q_\alpha, q_\beta$ are the wavevectors in zones $\alpha$ and $\beta$ respectively, and $\mathbf{r}_\perp$ is the coordinate along the interface. The continuity conditions at $x = 0$:

$$
\Phi_\alpha\big|_{x=0^-} = \Phi_\beta\big|_{x=0^+}, \qquad \mathcal{M}^{xx}_\alpha\partial_x\Phi_\alpha\big|_{x=0^-} = \mathcal{M}^{xx}_\beta\partial_x\Phi_\beta\big|_{x=0^+}
$$

The second condition is the **flux continuity** — the metric-weighted normal derivative must be continuous. This generalizes the quantum-mechanical wavefunction matching condition and the electromagnetic boundary condition for normal displacement.

For a **membrane-localized state** (one that decays away from the interface into both zones), the wavevectors must be purely imaginary:

$$
q_\alpha = i\kappa_\alpha > 0, \qquad q_\beta = -i\kappa_\beta < 0
$$

so that $e^{iq_\alpha x} = e^{-\kappa_\alpha |x|}$ decays into zone $\alpha$ (for $x < 0$) and $e^{iq_\beta x} = e^{-\kappa_\beta|x|}$ decays into zone $\beta$ (for $x > 0$). The membrane state is exponentially localized at the interface with a decay length $1/\kappa_\alpha$ into zone $\alpha$ and $1/\kappa_\beta$ into zone $\beta$.

The **existence condition** for a membrane-localized state: the flux continuity requires:

$$
-\mathcal{M}^{xx}_\alpha\kappa_\alpha = \mathcal{M}^{xx}_\beta\kappa_\beta
$$

(both sides equal). For this to have a solution with $\kappa_\alpha, \kappa_\beta > 0$, we need $\mathcal{M}^{xx}_\alpha$ and $\mathcal{M}^{xx}_\beta$ to have **opposite signs**. This is exactly the Type B interface condition — the membrane state exists only at sign-changing zone interfaces. At Type A interfaces (same-sign zones), the membrane state cannot be localized and instead becomes a propagating mode (a junction mode, section 11.3).

---

## Counting Membrane States

The ICHTB has 24 zone interfaces. The number of Type B (sign-changing) interfaces:

In the cuboctahedron, the 12 zones partition into 6 positive (+X, +Y, +Z, and three others) and 6 negative (−X, −Y, −Z, and three others), plus the two central zones (+0, −0). For the standard ICHTB zone assignment (Chapter 5–6), the sign-changing interfaces (positive zone adjacent to negative zone) number exactly **12** — half of all interfaces.

Each sign-changing interface supports at least one membrane-localized state (one mode per transverse momentum channel). The total membrane state count:

$$
N_{\text{mem}} = 12 \times N_{\text{transverse modes}} = 12 \times \frac{A_{\text{interface}}}{\xi_\perp^2}
$$

where $A_{\text{interface}} \sim R^2$ is the interface area and $\xi_\perp$ is the transverse coherence length. For a macroscopic ICHTB ($R \gg \xi_\perp$), the membrane state count $N_{\text{mem}} \gg 1$ — there are many transverse modes per interface.

The **12 sign-changing interfaces** of the ICHTB form a structured network that directly mirrors the topological structure of the cuboctahedron. This interface network is what gives the ICHTB its combinatorial richness — not just 6 bulk zones but 12 interface channels between them, each supporting its own class of membrane excitations.

