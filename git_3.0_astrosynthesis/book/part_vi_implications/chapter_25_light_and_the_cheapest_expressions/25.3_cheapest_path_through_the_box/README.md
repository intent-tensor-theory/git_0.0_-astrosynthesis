# 25.3 The Cheapest Path Through the Box

## Fermat's Principle in the ICHTB

**Fermat's principle** (Fermat 1662) states that light travels between two points along the path that takes the least time. In the ICHTB, the equivalent principle is: the cheapest excitation traverses the ICHTB along the path that minimizes the total zone traversal cost $\mathcal{C} = \sum_\alpha \mathcal{C}_\alpha$ (section 25.1).

These are the same principle in different language. Fermat's principle (least time) = ICHTB minimum traversal cost, because:
- Time elapsed = path length / phase velocity = $L/v_{\text{phase}}$
- Phase velocity $v_{\text{phase}} = \omega/k \propto 1/k$ (for the phonon branch, $v_{\text{phase}} = c_{\text{NLS}}$ = constant)
- Traversal cost $\mathcal{C}_{\text{fwd}} \propto k^2 \propto 1/v_{\text{phase}}^2$ (higher momentum = higher cost)
- Minimizing $\mathcal{C}$ = minimizing $k$ = maximizing $v_{\text{phase}}$ = minimizing travel time

For the NLS phonon (minimum-cost excitation): $v_{\text{phase}} = c_{\text{NLS}}$ (constant, independent of $k$ in the linear phonon limit). The cheapest path is then the **straight-line path** — any deviation from a straight line adds path length (and therefore traversal cost), so the minimum-cost path is the geodesic of the emergent geometry (section 23.1).

**Fermat's principle = geodesic principle = minimum traversal cost:** all three are equivalent statements of the same ICHTB variational principle.

---

## The Cheapest Path as a Geodesic

The cheapest path through the ICHTB zone structure is the geodesic of the emergent metric $g_{\mu\nu}$ (section 23.1). In a homogeneous background ($\rho_{\text{exc}} = \text{const}$): $g_{\mu\nu} = \delta_{\mu\nu}$ (flat metric), and the geodesic is a straight line. In a non-homogeneous background ($\rho_{\text{exc}} \neq \text{const}$): $g_{\mu\nu} \neq \delta_{\mu\nu}$ (curved metric), and the geodesic is curved — the cheapest path bends toward regions of higher excitation density (lower traversal cost, since the zone coupling constants $D_\alpha$ are larger where $\rho_{\text{exc}}$ is larger).

The bending of the cheapest path toward regions of higher excitation density is **gravitational lensing** in ICHTB language. The photon (NLS phonon) follows the geodesic of the emergent metric, which bends near massive bodies (regions of high excitation density) — exactly as predicted by general relativity.

The deflection angle of a light ray (NLS phonon) passing a mass $M$ (excitation cluster of density $\rho_{\text{exc}} = M/V$):

$$
\alpha_{\text{deflect}} = \frac{4GM}{c^2 b}
$$

(the Einstein deflection formula, where $b$ is the impact parameter). In ICHTB terms: this is the angle by which the minimum-cost traversal path bends due to the gradient in the excitation density $\rho_{\text{exc}}(r) \propto M/r^2$ near the mass. The factor 4 (vs. the Newtonian prediction of 2) comes from the contribution of both the temporal ($g_{00}$) and spatial ($g_{ij}$) components of the metric to the deflection — in the ICHTB, both the Forward zone (temporal) and the Expansion zone (spatial) contribute equally to the geodesic bending.

---

## The Light Cone as the Cheapest Surface

The **light cone** of an event $P$ (in standard physics: the set of all spacetime points that can communicate with $P$ via light signals) is, in ICHTB terms, the **cheapest surface** — the set of all points reachable from $P$ via minimum-cost traversals (phonon paths with $v_{\text{phase}} = c_{\text{NLS}}$).

Points inside the light cone (time-like separation from $P$): reachable via massive excitations ($v_{\text{phase}} < c_{\text{NLS}}$, higher traversal cost). Points outside the light cone (space-like separation from $P$): not reachable by any excitation (the traversal cost would be imaginary — exponentially suppressed tunneling amplitude). The light cone surface itself is the boundary between reachable and unreachable — it is where the traversal cost transitions from real (positive) to imaginary.

The **causal structure** of spacetime (the light cone structure) is the ICHTB minimum-cost surface. This gives a clean derivation of why causality is related to the speed of light: the light speed $c_{\text{NLS}}$ is the minimum traversal cost velocity — no excitation can propagate faster than $c_{\text{NLS}}$ without paying an imaginary traversal cost (which would correspond to exponentially suppressed tunneling, not classical propagation).

---

## Refraction, Reflection, and Zone Boundary Effects

When a minimum-cost excitation (NLS phonon) encounters a **zone boundary** — a region where the traversal cost function $\mathcal{C}(\mathbf{x})$ changes discontinuously — the cheapest path changes direction. This is the ICHTB version of refraction and reflection:

**Refraction (Snell's law):** When the NLS phonon crosses a zone boundary where the background density changes from $\rho_1$ to $\rho_2$ (equivalently, $c_{\text{NLS},1}$ to $c_{\text{NLS},2}$), the minimum-cost path bends to satisfy Snell's law:

$$
\frac{\sin\theta_1}{c_{\text{NLS},1}} = \frac{\sin\theta_2}{c_{\text{NLS},2}}
$$

(the ratio of the sine of the incidence angle to the NLS sound speed is conserved — the Snell's law of the ICHTB). This is exactly the familiar Snell's law of optics, with the NLS sound speeds playing the role of the optical refractive indices.

**Total internal reflection:** When $c_{\text{NLS},1} > c_{\text{NLS},2}$ (the phonon is going from a slow medium to a fast medium) and $\sin\theta_1 > c_{\text{NLS},1}/c_{\text{NLS},2}$ (the incidence angle exceeds the critical angle): total internal reflection occurs — the phonon cannot penetrate the zone boundary and is reflected back. In ICHTB terms: the traversal cost in medium 2 is imaginary for the phonon at this angle — exponentially suppressed tunneling rather than propagation.

**Zone membrane effects:** At an ICHTB zone membrane $\mathcal{M}_{\alpha\beta}$ (the boundary between zones $\alpha$ and $\beta$): the traversal cost has a specific discontinuity determined by the membrane activation threshold $\Lambda_{\text{threshold}}$ (section 16.5). The phonon can cross the membrane freely if $\hbar\omega > \Lambda_{\text{threshold}}$ (sufficient energy to activate the membrane); it is reflected if $\hbar\omega < \Lambda_{\text{threshold}}$ (insufficient energy). This is the ICHTB version of the **photoelectric effect** (Einstein 1905): light is absorbed by a material only if the photon energy $\hbar\omega$ exceeds the work function $\phi = \Lambda_{\text{threshold}}$ (the minimum energy required to eject an electron from the material surface). The work function is the activation threshold of the Core zone membrane — the energy barrier that the Forward zone phonon must overcome to penetrate to the Core zone and eject an electron (a Memory zone topological charge).

---

## Massive Excitations as Costly Paths

Non-phonon excitations — those with significant Core, Memory, or Apex zone lock energy — are the "costly paths" through the ICHTB. They travel at $v_{\text{phase}} < c_{\text{NLS}}$ (sub-luminal, since they must carry extra lock energy in addition to the Forward zone traversal cost). Their dispersion relation (in the ICHTB Bogoliubov language):

$$
\omega^2 = c_{\text{NLS}}^2 k^2 + \left(\frac{\hbar k^2}{2m}\right)^2 \frac{1}{c_{\text{NLS}}^2}
$$

Wait — the correct Bogoliubov dispersion for the full (not just phonon) branch:

$$
\omega^2 = c_{\text{NLS}}^2 k^2 + \left(\frac{\hbar k^2}{2m}\right)^2
$$

In the $k \to \infty$ limit: $\omega \approx \hbar k^2/(2m)$ (free-particle, massive). In the relativistic form: $E^2 = (pc)^2 + (m_{\text{eff}}c^2)^2$ where $m_{\text{eff}} c^2 = \hbar^2/(2m\xi^2) = \mu|\Psi_0|^2$ (the effective mass from the nonlinear term). This is the **Klein-Gordon dispersion relation** — the dispersion relation for a massive relativistic scalar field. The ICHTB Bogoliubov dispersion in the massive limit is the Klein-Gordon equation:

$$
\left(\frac{1}{c^2}\frac{\partial^2}{\partial t^2} - \nabla^2 + \frac{m_{\text{eff}}^2 c^2}{\hbar^2}\right)\delta\Psi = 0
$$

The "mass" $m_{\text{eff}}$ is the **zone traversal cost** of the non-phonon excitation: it is the lock energy required to maintain the Core/Memory zone structure while propagating — the cost of being a persistent, localized excitation rather than a cheap, propagating wave. Massive particles pay a higher traversal cost than massless ones; their paths through the ICHTB are "more expensive" than the geodesic light paths.

This is the ICHTB derivation of the relativistic energy-momentum relation $E^2 = p^2c^2 + m^2c^4$: the energy of a massive excitation is the sum of its kinetic energy (Forward zone traversal cost $\propto p^2c^2$) and its rest energy (Core/Memory/Apex zone lock energy $\propto m^2c^4$).

