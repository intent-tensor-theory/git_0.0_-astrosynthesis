# 7.1 The A/B Split as a Zone Property

## Part II: From Geometry to Excitations

Part I built the ICHTB from the ground up: the imaginary anchor i₀ (Chapter 1), the membrane (Chapter 2), the six zones (Chapter 3), the hat-counting address system (Chapter 4), the master equation (Chapter 5), and the full junction formalism for every singular locus (Chapter 6). The geometry is complete.

Part II uses that geometry. The question is no longer what the ICHTB is, but what it does — what kinds of excitations it supports, how those excitations are classified, and what the classification means physically.

The fundamental division of all excitations into two types — **A states** (linear, propagating, transient) and **B states** (nonlinear, self-sustaining, persistent) — is not a property of the excitations themselves but a property of **where in the ICHTB they live**. The A/B split is a zone property.

---

## The A/B Split: Amplitude Relative to the Zone Threshold

Recall from section 5.1 the four parameters of the master equation: diffusion coefficient $D$, flux coupling $\Lambda$, cubic coefficient $\gamma$, damping rate $\kappa$. From these, the natural amplitude scale is the B-state amplitude:

$$
\Phi_B = \sqrt{\frac{\kappa}{\gamma}}
$$

Any field excitation with local amplitude $A(\mathbf{x}) = |\Phi(\mathbf{x})|$ can be compared to $\Phi_B$ at every point. The **A/B split** is:

$$
\text{A state:} \quad A(\mathbf{x}) \ll \Phi_B \text{ everywhere in the excitation}
$$
$$
\text{B state:} \quad A(\mathbf{x}) \sim \Phi_B \text{ somewhere in the excitation (at the core)}
$$

This definition is amplitude-based — it says nothing directly about zones. But the six ICHTB zones have very different effective $\Phi_B$ values because the zone metrics $\mathcal{M}^{ij}_k$ enter the effective parameters in each zone. The **effective B-state amplitude** in zone $k$ is:

$$
\Phi_B^{(k)} = \sqrt{\frac{\kappa_k}{\gamma_k}} = \sqrt{\frac{\kappa}{\gamma}} \cdot \left(\frac{\mathcal{M}^{(k)}_{\text{characteristic}}}{\mathcal{M}_0}\right)^{-1/2}
$$

where $\mathcal{M}^{(k)}_{\text{characteristic}}$ is the dominant metric component in zone $k$ and $\mathcal{M}_0$ is the reference (Core zone) metric.

In zones where the metric is large (the "active" zones — Forward, Expansion, Apex), the effective $\kappa_k$ is large (the zone metric amplifies the damping term) and therefore $\Phi_B^{(k)} = \sqrt{\kappa_k/\gamma_k}$ is larger — a higher amplitude is required to enter the B-state regime. In the Core zone (metric near the unit value), the effective threshold is at the base value $\Phi_B$.

---

## Zone-Specific A/B Thresholds

The threshold for B-state behavior depends on which zone an excitation occupies:

| Zone | Metric character | Effective $\Phi_B^{(k)}$ | A-state dominates | B-state accessible |
|------|-----------------|--------------------------|-------------------|--------------------|
| Forward (+X) | Large $\mathcal{M}^{xx}$ | High threshold | Easily; small signals propagate | Only strong pulses |
| Expansion (+Y) | Large isotropic | High threshold | Naturally; bloom is A-state | Only at large radius |
| Apex (+Z) | Temporal amplification | Medium threshold | At low phase velocity | Near phase lock |
| Compression (−X) | Inverted curvature | Low threshold | Only briefly | Most naturally |
| Memory (−Y) | Antisymmetric | Very low threshold | Only at small amplitude | Most easily |
| Core (−Z) | Near-identity | Base threshold $\Phi_B$ | Near-vacuum | At $A \sim \Phi_B$ |

The pattern: **positive-operator zones have high B-state thresholds** (linear behavior is the default; strong nonlinearity is required to enter B-state). **Negative-operator zones have low B-state thresholds** (nonlinear behavior is accessible at moderate amplitude; these zones are naturally nonlinear).

This asymmetry is not coincidental — it is the zone-operator assignment doing its job. The positive zones (+X, +Y, +Z) are the "linear workspace" of the ICHTB: they support A-state signals and blooms by default, with B states as the exception. The negative zones (−X, −Y, −Z) are the "nonlinear workshop": B states arise naturally here, and pure A-state behavior requires special conditions (very small amplitude, careful preparation).

---

## The A/B Split as a Zone Map

This gives a direct identification: the A/B split maps onto the positive/negative zone dichotomy.

$$
\text{A states} \longleftrightarrow \text{Positive zones: } {+X, +Y, +Z}
$$
$$
\text{B states} \longleftrightarrow \text{Negative zones: } {-X, -Y, -Z}
$$

This is an approximate statement, valid for moderate amplitudes. The exact statement: the **A-state domain** of the ICHTB is the union of the positive zones (where the master equation is dominated by the positive-operator terms), and the **B-state domain** is the union of the negative zones (where the nonlinear terms dominate).

The membranes between positive and negative zones are the **A-to-B transitions** — the surfaces in the ICHTB where an excitation crosses from linear to nonlinear character. From section 6.2, these membranes are always **damping junctions** (sign $-1$) — the crossing from positive to negative zone costs energy, consistent with the interpretation that B-state formation requires the field to "invest" energy into its nonlinear structure.

---

## Why the A/B Split Is Binary

The A/B split is binary — not a continuum. There is no "half-A, half-B" state. This is because the split corresponds to whether the field is below or above the bifurcation point of the effective 0D equation (the Duffing oscillator of section 6.4, in the vertex-localized limit):

$$
\dot{A} = \Sigma A + \Gamma A^3 - KA
$$

For $A < A_*$ (A state): the linear term $(\Sigma - K)A$ dominates and $A \to 0$ (exponential decay to vacuum). For $A > A_*$ (B state): the cubic term $\Gamma A^3$ prevents further decay and the amplitude stabilizes at $A = A_B = \sqrt{(K-\Sigma)/\Gamma}$.

The **bifurcation point** $A = A_*$ is the unstable fixed point of this equation — the exact threshold between A and B behavior. Below it, the field decays (A state). Above it, the field persists (B state). There is no stable state between $A = 0$ and $A = A_B$ — the intermediate amplitude regime is the unstable basin boundary, not a stable equilibrium.

This binary character is what gives the A/B split its sharpness — it is a mathematical bifurcation, not a fuzzy classification.

---

## The A/B Split and the Imaginary Axis

There is one more layer to the A/B zone correspondence: the **imaginary structure** of the ICHTB.

In Chapter 1, i₀ was introduced as the imaginary recursion anchor — the point at the "bottom" of the ICHTB from which all structure emerges. The imaginary axis (the axis of purely imaginary field values, $\Phi \in i\mathbb{R}$) runs from i₀ through the Core zone (−Z) upward toward the Apex zone (+Z).

The **A states** live primarily on the real part of $\Phi$: $\Phi \approx A e^{i\theta}$ with $\theta \approx 0$ (phase near zero). Real-$\Phi$ excitations are the propagating signals — they carry information along the real axis.

The **B states** have significant imaginary content: $\Phi = A e^{i\theta}$ with $\theta \neq 0$, and the phase $\theta$ is itself a dynamical variable that contributes to the self-sustaining character of the B state. Vortex B states (2.B) are entirely phase-organized — their amplitude is roughly constant but their phase winds around a loop. Topological knot B states (3.B) have phase organized into Hopf-linked loops.

The A/B split therefore has an additional geometric interpretation: **A states are real-axis excitations; B states are complex-plane (phase-involving) excitations**. Moving from the real axis into the complex plane — "picking up imaginary content" — is the geometric act of transitioning from A to B character.

The imaginary content is sourced by i₀ (the imaginary anchor). B states are excitations that have "picked up some of i₀" — they carry a memory of the imaginary pre-existence. A states are "as real as possible" — they minimize their imaginary content and propagate cleanly through the real part of the ICHTB.

