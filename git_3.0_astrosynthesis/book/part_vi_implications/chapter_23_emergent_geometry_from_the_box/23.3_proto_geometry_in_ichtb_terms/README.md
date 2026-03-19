# 23.3 Proto-Geometry in ICHTB Terms

## What Is Proto-Geometry?

**Proto-geometry** is the structure that exists before full geometric emergence — the precursor structure from which spatial geometry crystallizes. In the ICHTB, proto-geometry is the zone relation network in its raw, pre-crystallization form: a collection of zone relations $\{R_{ij}\}$ among excitations that has not yet settled into a consistent metric structure.

Proto-geometry has the following properties:

1. **Non-metric:** The zone relation network does not yet satisfy the triangle inequality. Two excitations may have $R_{ij} \approx 1$ and $R_{jk} \approx 1$ but $R_{ik} \approx 0$ — violating $d_{ij} + d_{jk} \geq d_{ik}$ (the triangle inequality would be violated). This happens when two excitations are separately close to a third but not close to each other — a non-metric, "anisotropic" zone relation.

2. **Discrete:** The proto-geometry is built from a discrete collection of excitations, not a continuous field. The zone relations form a discrete graph (a finite or countably infinite set of nodes and edges), not a smooth manifold.

3. **Fluctuating:** In the pre-selection phase (before persistence selection has filtered the excitations), the zone relations fluctuate rapidly — excitations form and dissolve, and the zone relation network changes on the time scale $T_{\text{zone}}$. The proto-geometry is not static.

4. **Higher-dimensional:** Before the persistence selection, the zone relation network does not necessarily have the dimensionality of the final emergent 3-manifold. It may have higher (or lower) effective dimensionality, depending on the distribution of excitations.

Proto-geometry is the ICHTB analog of the **pre-geometric phase** in quantum gravity — the phase before spacetime emerges from the fundamental degrees of freedom (spin networks in LQG, simplicial complexes in CDT, etc.).

---

## Zone Directions as Geometric Directions

The six ICHTB zones (Core, Memory, Expansion, Forward, Apex, Transition) correspond to six geometric directions in the proto-geometry. Before the full 3D geometry crystallizes, the zone directions are the only "directions" that exist in the proto-geometric structure.

**Core zone direction:** The inward direction — the direction of increasing field amplitude, toward the amplitude maximum. In the crystallized geometry, this corresponds to the radial direction in polar coordinates centered on the excitation.

**Memory zone direction:** The azimuthal direction — the direction of increasing phase winding, around the vortex core. In the crystallized geometry, this corresponds to the tangential/angular direction around the excitation's core.

**Expansion zone direction:** The outward direction — the direction of decreasing field amplitude, away from the amplitude maximum into the background. In the crystallized geometry, this corresponds to the outward radial direction (opposite to the Core zone direction).

**Forward zone direction:** The propagation direction — the direction of the phase gradient (the group velocity of the excitation). In the crystallized geometry, this corresponds to the time direction (since propagating excitations move through space in the +X direction, identifying the Forward zone with the spacetime future lightcone direction).

**Apex zone direction:** The orbital direction — the direction of the orbital angular momentum of Apex zone modes. In the crystallized geometry, this corresponds to the axis of rotation of the excitation, which becomes a preferred direction in 3D space.

**Transition zone direction:** The gradient direction — the direction of the transition from Core to background amplitudes. In the crystallized geometry, this corresponds to the direction of the field gradient, which is typically radial (same as Core) but may be anisotropic for non-spherical excitations.

These six zone directions are **not independent** — they satisfy the constraint that the three spatial directions in $\mathbb{R}^3$ span the same space as the six zone directions. Specifically, the six zone directions are combinations of the three Cartesian directions:
- Core: $-\hat{r}$ (inward radial)
- Expansion: $+\hat{r}$ (outward radial)
- Memory: $\hat{\phi}$ (azimuthal)
- Apex: $\hat{z}$ (angular momentum axis)
- Forward: $\hat{v}$ (propagation direction, a combination of $\hat{x}, \hat{y}, \hat{z}$)
- Transition: varies (gradient direction)

The three independent Cartesian directions $(\hat{x}, \hat{y}, \hat{z})$ emerge from the five independent zone directions (the six zone directions span a 3D space, so three are independent). The dimensionality of the emergent geometry (3D) is fixed by the number of independent zone directions — the ICHTB has three independent spatial zone directions, producing a 3-dimensional emergent geometry.

---

## Dimensional Reduction from Zone Count

The ICHTB has six zones but the emergent geometry is 3-dimensional. How does dimensional reduction occur? The answer is the zone redundancy conditions — two pairs of zones are related by conjugate symmetry:

1. **Core ↔ Expansion (amplitude conjugate):** The Core zone (inward) and Expansion zone (outward) are opposite ends of the same amplitude profile — they are conjugate in the sense that the Core zone maximum determines the Expansion zone far-field behavior. Together they contribute one independent direction (the radial direction), not two.

2. **Memory ↔ Apex (angular momentum conjugate):** The Memory zone (vortex phase winding around the Core) and the Apex zone (orbital angular momentum modes) are angular conjugates — the Memory zone chirality and the Apex zone orbital quantum number are linked by the spin-orbit coupling (section 21.2). Together they contribute one independent angular direction.

3. **Forward ↔ Transition (gradient conjugate):** The Forward zone (propagation phase gradient) and Transition zone (amplitude gradient from Core to background) are gradient conjugates — the Forward zone phase gradient and the Transition zone amplitude gradient together define the full complex gradient of the field. Together they contribute one independent direction (the propagation/gradient direction).

The three conjugate pairs $(Core, Expansion)$, $(Memory, Apex)$, $(Forward, Transition)$ reduce the six zone directions to three independent geometric directions — the three spatial directions of the emergent $\mathbb{R}^3$. This is the ICHTB mechanism of dimensional reduction: six zone directions → three independent spatial directions through three conjugate pairings.

---

## Proto-Geometry and the Planck Scale

The proto-geometry (the pre-crystallization zone relation network) has a natural length scale — the zone coherence length $\ell_{\text{zone}} = \xi_{\text{core}}$, the Core zone coherence length. Below this scale, the concept of distance breaks down (the zone relation is identically 1 for separations $d < \xi_{\text{core}}$, since two excitations within one coherence length are in a merged state). Above this scale, the zone relations vary smoothly and define a metric.

The zone coherence length $\ell_{\text{zone}} = \xi_{\text{core}}$ is the ICHTB analog of the **Planck length** $\ell_P = \sqrt{\hbar G/c^3} \approx 1.6 \times 10^{-35}$ m. Just as the Planck length is the scale below which semiclassical spacetime breaks down in quantum gravity, $\ell_{\text{zone}}$ is the scale below which the emergent metric breaks down in the ICHTB.

In the ICHTB framework, the Planck length is not a fundamental constant but a derived quantity — it is the Core zone coherence length of the NLS field evaluated at the fundamental coupling constants $\gamma$ and $\mu$:

$$
\ell_P = \xi_{\text{core}} = \frac{\hbar}{\sqrt{2m_{\text{eff}}\mu|\Psi_0|^2}}
$$

The Planck scale is the scale where the discrete zone structure of the proto-geometry becomes visible — where the smooth emergent metric breaks down and the discrete zone relation network is exposed. Experiments at the Planck scale would reveal the granular, zone-structured proto-geometry beneath the smooth spacetime of classical physics.

The proto-geometry of the ICHTB thus makes a specific prediction: **spacetime is smooth down to the Planck scale** (below the Core zone coherence length), but the emergent geometry breaks down at $\ell_{\text{zone}} = \ell_P$ — not as a discontinuity but as a gradual transition from metric to non-metric zone relations. This is consistent with current observational constraints (no evidence of Lorentz invariance violation or discrete spacetime structure down to $\sim 10^{-20}$ m, many orders of magnitude above $\ell_P$).

