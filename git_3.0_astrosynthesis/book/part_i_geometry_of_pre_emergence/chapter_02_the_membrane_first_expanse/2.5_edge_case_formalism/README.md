# 2.5 Edge Case Formalism

## Where Three Zones Meet

Every membrane face is shared by exactly two zones. But the ICHTB cube has 8 vertices and 12 edges. At each **vertex** of the cube, three zones meet simultaneously. At each **edge**, two membrane triangles meet. These are the **edge cases** — the degenerate locations where the simple two-zone junction formalism of section 2.3 breaks down.

There are three distinct types:

1. **Edge junctions**: Two membrane triangles meeting along a spoke from i₀ to a cube corner. Here two membranes share a 1D edge, and three distinct zone metrics must be reconciled simultaneously.

2. **Cube vertex junctions**: The cube has 8 vertices, each at the corner of three faces. At each cube vertex, three pyramidal zones meet at a single point. Three distinct zone metrics, three membrane faces, and a single geometric point.

3. **The i₀ vertex**: All 12 membrane triangles share the single vertex i₀. At i₀, all six zones meet simultaneously. This is the extreme degenerate case — the most complex geometric singularity in the entire ICHTB structure.

---

## Type 1: Spoke Edge Junctions

A **spoke** is a line segment from i₀ to one of the 8 cube corners. There are 8 spokes. Each spoke is the shared edge of exactly **three membrane triangles** (the three membrane faces meeting at that cube corner). Along any spoke, three zones touch simultaneously.

Let the three zones meeting at a spoke be labeled $A$, $B$, $C$ with zone metrics $\mathcal{M}^{ij}_A$, $\mathcal{M}^{ij}_B$, $\mathcal{M}^{ij}_C$. The junction conditions at the spoke require simultaneous satisfaction of:

$$
[\![\Phi]\!]_{AB} = 0, \quad [\![\Phi]\!]_{BC} = 0, \quad [\![\Phi]\!]_{CA} = 0
$$

$$
[\![\mathcal{M}^{ij}n_i^{AB}\partial_j\Phi]\!]_{AB} = \sigma_{AB}, \quad [\![\mathcal{M}^{ij}n_i^{BC}\partial_j\Phi]\!]_{BC} = \sigma_{BC}, \quad [\![\mathcal{M}^{ij}n_i^{CA}\partial_j\Phi]\!]_{CA} = \sigma_{CA}
$$

Continuity of $\Phi$ across all three interfaces is compatible only if the field value at the spoke is consistent with all three zones simultaneously. This constrains the field to a **triple-point value** $\Phi_{\text{spoke}}$ satisfying three simultaneous boundary conditions.

The compatibility condition is:

$$
\sigma_{AB} + \sigma_{BC} + \sigma_{CA} = 0
$$

(The total flux at a triple-line junction must sum to zero: no flux can be "created" at the junction itself without violating energy conservation. This is a 1D analog of Kirchhoff's current law at a node.) When this condition is satisfied, the junction is **regular**. When it is violated, the junction is **singular** — a topological defect line is nucleated at the spoke, threading its length with winding number $n \neq 0$.

---

## Type 2: Cube Vertex Junctions

At each of the 8 cube corners, three pyramidal zones meet. But they meet not at a line (like the spoke case) but at a **point** on the cube surface. The three zones touching at corner $C_k$ are the three zones whose faces contain $C_k$ as a vertex.

At a cube vertex, we have three pairs of interfaces: membranes $\Delta_{AB}$, $\Delta_{BC}$, $\Delta_{CA}$ all meeting at the point $C_k$. The analysis is similar to the spoke case but now the junction is point-like rather than line-like. The field value at $C_k$ must be consistent with three simultaneously imposed boundary conditions.

The additional constraint here is angular: the three membrane faces meeting at $C_k$ define three half-planes, and the phase $\theta$ must vary smoothly around $C_k$ when viewed from inside the cube. The angular constraint gives:

$$
\sum_{\text{interfaces at }C_k} n_{\Delta_k} = \text{(total topological charge at }C_k)
$$

When the right-hand side is zero, the vertex is topologically trivial. When it is nonzero, a **point vortex** (in 2D language) or **vortex line termination** (in 3D language) sits at $C_k$.

In physics terms: the 8 cube vertices are the only locations in the ICHTB (other than i₀) where topological charges can be localized on the boundary of the box. They are the natural **monopole positions** of the CTS structure.

---

## Type 3: The i₀ Vertex — The Extreme Junction

The vertex i₀ is shared by all 12 membrane triangles. At i₀, all six zone metrics simultaneously compete. This is not merely a technical complication — it is the **geometric representation of the pre-emergence state**.

At i₀, the field value is:

$$
\Phi(i_0) = A(i_0)\,e^{i\theta(i_0)}, \qquad A(i_0) \to 0, \quad \theta(i_0) = \pi/2
$$

(From Chapter 1: i₀ is the pre-emergence seed with vanishing real amplitude and phase fixed at $\pi/2$.) This boundary condition at i₀ is simultaneously consistent with all six zone operators precisely because the amplitude vanishes: when $A = 0$, the phase $\theta$ is arbitrary (the field is zero regardless of phase). The six zone operators all agree on the value $\Phi = 0$ at i₀, even though they disagree on everything else.

This is the **geometric origin of the pre-emergence degeneracy**: at i₀, all zone distinctions collapse, all membrane source terms vanish ($\sigma_k|_{i_0} = 0$ because $A(i_0) = 0$), and the field is in its maximally degenerate state. The emergence of zone differentiation is driven by the departure from i₀ — as the field amplitude grows away from i₀, the zones and membranes become relevant.

Formally, near i₀ in spherical coordinates $(r, \Omega)$ where $r$ is the distance from i₀ and $\Omega$ is the solid angle:

$$
\Phi(r, \Omega) \approx r^\nu\,\psi(\Omega)\,e^{i\pi/2} + O(r^{\nu+1})
$$

where $\psi(\Omega)$ is a spherical harmonic satisfying the angular part of the CTS equation, and $\nu$ is the scaling exponent determined by the boundary conditions at i₀. The membrane structure selects the **angular modes** $\psi(\Omega)$ — only harmonics consistent with the 12-fold membrane geometry are allowed.

The allowed angular modes form a discrete spectrum — the membrane imposes a quantization condition on the azimuthal structure of the field near i₀. This is the deepest level at which the membrane is "the first structure connected to i₀" — it shapes the field before any zone distinction has emerged.

---

## Summary: The Complete Membrane Formalism

| Structure | Count | Formalism | Physics |
|-----------|-------|-----------|---------|
| Membrane faces $\Delta_k$ | 12 | Two-zone junction conditions (section 2.3) | Zone-to-zone energy and phase transport |
| Spoke edges (Type 1) | 8 | Triple-junction compatibility $\sum\sigma = 0$ | Topological defect line nucleation condition |
| Cube vertex junctions (Type 2) | 8 | Three-zone point junction | Monopole positions; boundary topological charge |
| i₀ vertex (Type 3) | 1 | Six-zone extreme junction; $A(i_0) = 0$ | Pre-emergence degeneracy; angular mode selection |

The complete edge case formalism is the **missing mathematics** of the ICHTB that was left implicit in Books 1.0 and 2.0. Every statement about zone operators in those books assumed smooth, well-defined zones — which requires the membrane boundary conditions to be satisfied. The membrane formalism derived in this chapter is the foundation on which those calculations rest.

Chapter 6 will return to the edge case formalism in full mathematical detail, including the differential geometry of the membrane as an embedded 2-complex, the Israel junction conditions from general relativity, the Rankine-Hugoniot conditions from fluid mechanics, and the surface defect formalism from condensed matter physics. The present chapter establishes the physical picture; Chapter 6 provides the machinery.

