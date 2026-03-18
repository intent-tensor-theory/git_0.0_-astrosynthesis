# Chapter 1: Construction

## 1.1 Start With a Cube

Begin with a cube of side length **ℓ**. Label the six faces not by names — not "top," "front," "left" — but leave them anonymous for now. They will earn their names from what the field does on them, not from where they sit.

The cube has:

- 8 corner vertices
- 12 edges
- 6 faces
- 1 center

The center is the problem.

---

## 1.2 Why the Center Cannot Be Zero

In classical Cartesian geometry, the center of a cube is the origin **0** — a point in real three-dimensional space. It exists. You can place a ruler there. The coordinates (0, 0, 0) reference a real location.

The ICHTB center is different. Call it **i₀**.

$$i_0 \in \mathbb{C}, \quad i_0 \notin \mathbb{R}^3$$

**i₀ is not a location. It is a recursion anchor.**

The distinction matters for the following reason: if the center were a real point, it would need to participate in the field Φ as a boundary condition — a fixed real value that the surrounding field references. But the ICHTB is a *self-generating* structure. Nothing is fixed from outside. The center must be the seed from which the field grows, not a constraint imposed on it.

An imaginary scalar serves this role precisely. It sits outside the real domain of the field, making it unreachable as a physical position while remaining fully reachable as a recursion origin. The field can "refer back" to i₀ without i₀ ever becoming a location the field must match.

Formally: placing i₀ at the imaginary unit gives the complex collapse field its natural form:

$$\Phi(\vec{x}, t) = A(\vec{x}, t)\cdot e^{i\theta(\vec{x}, t)}$$

where **A** is the real tension amplitude and **θ** is the recursion phase angle. The imaginary axis is not just notation — it is the dimension along which recursion advances.

---

## 1.3 The Six Pyramids

Draw a line from i₀ to the center of each face. This divides the cube into **six square pyramids**:

| Pyramid | Base Face | Apex |
|---------|-----------|------|
| P₊ᵧ | +Y face | i₀ |
| P₋ᵧ | −Y face | i₀ |
| P₊ₓ | +X face | i₀ |
| P₋ₓ | −X face | i₀ |
| P₊₂ | +Z face | i₀ |
| P₋₂ | −Z face | i₀ |

Each pyramid has:

$$V_{\text{pyramid}} = \frac{1}{3} \cdot \ell^2 \cdot \frac{\ell}{2} = \frac{\ell^3}{6}$$

Six pyramids together:

$$6 \times \frac{\ell^3}{6} = \ell^3$$

The six pyramids fill the cube exactly, with no overlap and no gaps. This is not a coincidence — it is the geometric fact that makes the ICHTB a closed system.

---

## 1.4 Odd and Even Cubes: Where Does i₀ Sit?

When the cube is discretized into a lattice of voxels, two cases arise depending on whether the number of voxels along each side is odd or even.

**Odd-length cube** (e.g., 5×5×5):

The lattice has a central voxel. i₀ lives *inside* that voxel:

$$L = 2n+1, \quad \vec{x}_{i_0} = (0, 0, 0)_{\text{voxel-center}}$$

Node set: {−2, −1, 0, 1, 2}. The voxel at index 0 is the anchor.

**Even-length cube** (e.g., 4×4×4):

No central voxel exists. i₀ sits in the gap between the 8 central voxels:

$$L = 2n, \quad \vec{x}_{i_0} = \left(\frac{1}{2}, \frac{1}{2}, \frac{1}{2}\right)_{\text{inter-voxel}}$$

This is called the **recursive gap** position. The recursion anchor floats between nodes, meaning no single voxel owns it.

**Collapse Parity Law:**

$$C_{\text{odd}} = \text{Anchor Node} \qquad C_{\text{even}} = \text{Recursive Gap}$$

Both cases support the same six recursive zones and the same 12-point, 12-line closure structure. The parity only determines whether i₀ is addressable as a discrete voxel.

---

## 1.5 The 12 Lines

From i₀, six lines run outward to the face centers. Six more run between face-center-pair intersections. Together these form **12 canonical lines** — the skeletal frame of the ICHTB.

Each line is a vector:

$$\vec{L}_k(t) = \vec{r}_{\Delta_k}(t) - \vec{r}_{i_0}$$

| Line | From → To | Collapse Role |
|------|-----------|---------------|
| L₁ | i₀ → Δ₁ (+Y) | ∇Φ direction |
| L₂ | i₀ → Δ₂ (−Y) | ∇×**F** loop axis |
| L₃ | i₀ → Δ₃ (+X) | +∇²Φ diffusion arm |
| L₄ | i₀ → Δ₄ (−X) | −∇²Φ compression arm |
| L₅ | i₀ → Δ₅ (+Z) | ∂Φ/∂t emergence axis |
| L₆ | i₀ → Δ₆ (−Z) | Scalar anchor axis |
| L₇–L₁₂ | Between face intersections | Curvature continuity edges |

All 12 lines evolve under the same curvent dynamics (see Chapter 2).

---

## 1.6 The 12 Points

The 12 intersection points **P₀ through P₁₁** are where recursive planes meet. They are not arbitrary — each one is the junction of two planes plus one edge, and each carries a tension direction vector:

$$P_k = \Delta_i \cap \Delta_j \cap \mathcal{E}_{ij}$$

$$\vec{T}_{P_k} = \sum_{\Delta_i \in \text{Adj}(P_k)} \hat{n}_{\Delta_i}$$

| Point | Connects | Function |
|-------|----------|----------|
| P₀ | Center / all Δᵢ | Scalar anchor i₀ |
| P₁ | Δ₁ ∩ Δ₂ | Forward–Memory vector shift |
| P₂ | Δ₁ ∩ Δ₃ | Outflow hinge |
| P₃ | Δ₂ ∩ Δ₄ | Curl convergence |
| P₄ | Δ₄ ∩ Δ₆ | Tension funnel tip |
| P₅ | Δ₃ ∩ Δ₅ | Emergence lock gate |
| P₆ | Δ₅ ∩ Δ₆ | Curvature loop close |
| P₇ | Δ₂ ∩ Δ₆ | Loop root pin |
| P₈ | Δ₃ ∩ Δ₆ | Radial permission node |
| P₉ | Δ₁ ∩ Δ₅ | Shell directive |
| P₁₀ | Δ₄ ∩ Δ₅ | Collapse curvature node |
| P₁₁ | Δ₁ ∩ Δ₄ | Push–pull anchor |

The full point identity:

$$\mathcal{P}_k = \left\{ \vec{r}_k,\; \Delta_i,\; \Delta_j,\; \mathcal{E}_{ij},\; \vec{T}_{P_k},\; f_k(\Phi, \mathcal{M}_{ij}, \rho_q) \right\}$$

Each point is not just a position but a complete recursive identity: location, adjacency, tension direction, and field function.

---

## 1.7 What Has Been Built

The construction so far gives us:

- A cube with an imaginary center i₀
- Six pyramidal zones, each responsible for a region of the interior
- 12 lines defining the collapse skeleton
- 12 intersection points carrying tension identity

No field has been placed yet. No operators have been defined. The construction is purely geometric — the container that the physics will inhabit. Chapter 2 defines what each zone actually *does*.
