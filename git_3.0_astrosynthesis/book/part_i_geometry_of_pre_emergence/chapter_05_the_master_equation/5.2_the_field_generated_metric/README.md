# 5.2 The Field-Generated Metric

## The Metric Is Not Given — It Is Earned

Section 5.1 derived the master equation treating the ICHTB metric $\mathcal{M}^{ij}(\mathbf{x})$ as a fixed background structure — a prescribed tensor field that varies between zone values across the membranes. This is the **quenched approximation**: the metric is frozen, the field evolves on it.

The quenched approximation is accurate for A states and weak B states (small amplitude relative to the B-state threshold $\sqrt{\kappa/\gamma}$). But for strong B states — and especially for 3.B topological knots — the field amplitude is large enough that the field itself **generates curvature**, modifying the metric it evolved on.

This is the CTS version of general relativity's central insight: the metric is not a fixed backdrop but a dynamical variable determined self-consistently with the matter (field) it governs. In GR, the Einstein field equations $G_{\mu\nu} = 8\pi G\, T_{\mu\nu}$ couple the curvature tensor $G_{\mu\nu}$ (geometry) to the stress-energy tensor $T_{\mu\nu}$ (matter). In the CTS, the analogous coupling is between the zone metric $\mathcal{M}^{ij}$ (ICHTB geometry) and the field energy-momentum tensor $T^{ij}[\Phi]$ (CTS matter).

---

## The Stress-Energy Tensor of the CTS Field

For any field theory with action $S = \int \mathcal{L}(\Phi, \nabla\Phi)\,d^3x\,dt$, the stress-energy tensor is defined via the variation of the action with respect to the metric:

$$
T^{ij} = -2\frac{\delta \mathcal{L}}{\delta \mathcal{M}_{ij}} + \mathcal{M}^{ij}\mathcal{L}
$$

For the CTS master equation, the associated Lagrangian density (in the static limit, treating $\partial_t\Phi = 0$) is:

$$
\mathcal{L}_{\text{CTS}} = D\,\mathcal{M}^{ij}\nabla_i\Phi^*\nabla_j\Phi - \kappa|\Phi|^2 + \frac{\gamma}{2}|\Phi|^4
$$

The CTS stress-energy tensor is:

$$
T^{ij}[\Phi] = D\left(\nabla^i\Phi^*\nabla^j\Phi + \nabla^j\Phi^*\nabla^i\Phi\right) - \mathcal{M}^{ij}\left[D\,\mathcal{M}^{kl}\nabla_k\Phi^*\nabla_l\Phi - \kappa|\Phi|^2 + \frac{\gamma}{2}|\Phi|^4\right]
$$

The trace $T^{ii} = T = \mathcal{M}_{ij}T^{ij}$ gives the pressure:

$$
T = D(3-2)\mathcal{M}^{ij}\nabla_i\Phi^*\nabla_j\Phi - 3\kappa|\Phi|^2 + \frac{3\gamma}{2}|\Phi|^4
$$

For a uniform B state ($\nabla\Phi = 0$, $|\Phi|^2 = \kappa/\gamma$):

$$
T = -3\kappa\frac{\kappa}{\gamma} + \frac{3\gamma}{2}\left(\frac{\kappa}{\gamma}\right)^2 = -\frac{3\kappa^2}{\gamma} + \frac{3\kappa^2}{2\gamma} = -\frac{3\kappa^2}{2\gamma} < 0
$$

A uniform B state has **negative trace** — it generates negative pressure, which in the CTS context means it pulls the zone geometry inward toward the Core. B states are gravitating objects in the CTS metric sense.

---

## The Metric Evolution Equation

The self-consistent coupling between the field and the metric is governed by the **metric evolution equation** — the CTS analog of the Einstein equations. The natural coupling, consistent with the ICHTB zone structure and dimensional analysis, is:

$$
\frac{\partial\mathcal{M}^{ij}}{\partial t} = -\beta\left[T^{ij}[\Phi] - \frac{T}{6}\mathcal{M}^{ij}\right] + \mu\nabla^2\mathcal{M}^{ij}
$$

The first term (coefficient $\beta$) drives the metric toward alignment with the field stress-energy: where the field is strong, the metric stiffens (increases) in the direction of the field gradient, amplifying the effect of the dominant zone operator. The second term (coefficient $\mu$) diffuses the metric, preventing sharp metric gradients from developing (which would represent unphysical metric singularities).

This is a **reaction-diffusion equation for the metric**: the stress-energy reacts with the zone geometry, and the geometry diffuses to maintain smoothness.

The **backreaction parameter** is:

$$
\epsilon = \frac{\beta\kappa}{\gamma\mu} \cdot \frac{|\Phi_B|^2}{L^{-2}}
$$

When $\epsilon \ll 1$ (small backreaction): the quenched approximation is valid, the metric is essentially fixed, and the zones are stable. When $\epsilon \sim 1$ (strong backreaction): the field significantly deforms the zone geometry, and the metric evolution must be solved simultaneously with the field evolution. When $\epsilon \gg 1$ (dominant backreaction): the field has "eaten" the geometry — the zone structure is primarily determined by the field configuration rather than the pre-existing ICHTB.

The $\epsilon \gg 1$ regime is the **CTS analog of strong gravity**: a field configuration so energetically concentrated that it reshapes the geometry it lives in. In this regime, the ICHTB is no longer a fixed box — it is a dynamical object that breathes and deforms in response to the field excitations it contains.

---

## The Field-Generated Zone Boundary

The most dramatic consequence of metric backreaction: the zone boundaries (membranes) can **move**.

In the quenched approximation, the membrane positions are fixed by the ICHTB geometry — the 12 triangular faces at fixed locations in space. With backreaction, the metric $\mathcal{M}^{ij}(\mathbf{x}, t)$ evolves in time, and the zones are defined as the regions where a particular operator dominates. As the metric changes, the boundaries between zones shift.

A strong B-state excitation in the Forward zone (+X) generates a large $T^{xx}$ component in the stress-energy. This stiffens $\mathcal{M}^{xx}$ in the vicinity of the excitation. As $\mathcal{M}^{xx}$ increases locally, the Forward zone expands — the boundary between the Forward zone and adjacent zones moves outward. The Forward zone "grows" in response to the strong field in it.

This is the CTS version of **gravitational lensing**: just as a massive object bends the geometry of spacetime so that light paths curve toward it, a strong CTS excitation deforms the ICHTB geometry so that the zone boundaries curve toward the strong field region. The excitation attracts the geometry to itself.

---

## Fixed Points of the Coupled System

The full coupled field-metric system:

$$
\partial_t\Phi = D\nabla_i(\mathcal{M}^{ij}\nabla_j\Phi) - \Lambda\mathcal{M}^{ij}\nabla_i\Phi\nabla_j\Phi + \gamma|\Phi|^2\Phi - \kappa\Phi
$$

$$
\partial_t\mathcal{M}^{ij} = -\beta\left[T^{ij}[\Phi] - \frac{T}{6}\mathcal{M}^{ij}\right] + \mu\nabla^2\mathcal{M}^{ij}
$$

has two important fixed points:

**1. The vacuum fixed point:** $\Phi = 0$, $\mathcal{M}^{ij} = \mathcal{M}^{ij}_{\text{ICHTB}}$ (the undisturbed zone metrics). This is the pre-emergence state — the ICHTB at i₀ with no field excitation. It is stable when all A-state and B-state thresholds are above the noise floor.

**2. The condensate fixed point:** $\Phi = \Phi_B$ (a B-state configuration), $\mathcal{M}^{ij} = \mathcal{M}^{ij}_B(\Phi_B)$ (the self-consistently deformed metric). This is the post-emergence state — a persistent field configuration that has reshaped its own geometric environment to become self-sustaining. The condensate fixed point is stable when $\epsilon \gtrsim \epsilon_c$ (some critical backreaction).

The transition between these two fixed points — from vacuum to condensate, from pre-emergence to persistent structure — is a **phase transition of the coupled field-metric system**. It is the mathematical description of emergence itself.

The order of this transition depends on the sign of the leading nonlinear term in the free energy expansion around the vacuum: for the CTS parameters $\{D, \Lambda, \gamma, \kappa, \beta, \mu\}$, it can be first-order (discontinuous jump in $|\Phi_B|$, like condensation) or second-order (continuous growth of $|\Phi_B|$ from zero, like a ferromagnetic transition). The transition order determines whether emergence is sudden (first-order: a single discontinuous event) or gradual (second-order: a smooth growth from nothing).

