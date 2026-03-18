# Chapter 4: Hat Counting

The Master Equation describes continuous field evolution. The Hat Counting system describes the same space discretely — as a lattice of addressable positions. The two descriptions are dual: every continuous field configuration corresponds to a hat-counting state, and every hat-counting navigation step corresponds to a continuous path through the field.

---

## 4.1 What Is a Hat?

A **hat** is a small pyramid. Specifically: each of the six cube faces is divided into a regular 2D grid. At each grid cell, a miniature pyramid extrudes outward from the face, pointing away from i₀. The pyramid's height is not fixed — it is computed from the local field value.

The name "hat" comes from the shape: a square base on the face, rising to a point. From above (looking at a face), the grid looks like a field of tents or hat-brims.

The hat system converts the continuous interior of the ICHTB into a discrete, navigable address space. Every point in the box can be reached by specifying which face, which grid cell, and how deep into the interior you are.

---

## 4.2 The Four-Index Address

Every position in the ICHTB has a unique address:

$$\text{Address} = (k,\; u,\; v,\; h)$$

| Index | Range | Meaning |
|-------|-------|---------|
| k | {+X, −X, +Y, −Y, +Z, −Z} | Which face (which zone) |
| u | [−n/2, n/2] | Horizontal position on that face |
| v | [−n/2, n/2] | Vertical position on that face |
| h | [0, H_k(u,v)] | Depth level (how far into the interior) |

The maximum depth H_k(u,v) varies across the face — it is determined by the **hat count tensor**.

---

## 4.3 The Hat Count Tensor

For each face k, the hat count at position (u, v) is:

$$\mathcal{H}_k(u,v) = \left\lfloor \alpha_k \cdot f_k(u,v) + \beta_k \right\rfloor$$

where:

- **α_k**: face-specific amplitude (how tall hats can grow on this face)
- **f_k(u,v)**: curvent-aligned activation pattern (the "shape" of the hat field on this face)
- **β_k**: base height offset (minimum hat height — all cells have at least this many levels)
- **⌊·⌋**: floor function — hats are discrete, fractional levels do not exist

The activation pattern f_k(u,v) is the key design choice. Different patterns produce different geometry:

**Radial activation** (used on +Y, Forward Tension):
$$f_{Y+}(u,v) = \sqrt{u^2 + v^2}$$
Hats are tallest at the corners and shortest at the center. Corresponds to gradient flow outward from center.

**Sinusoidal activation** (used on +Z, Apex):
$$f_{Z+}(u,v) = \sin\!\left(\frac{\pi u}{n}\right)\cdot\cos\!\left(\frac{\pi v}{n}\right)$$
A wave pattern — hats are tall in some regions and short in others. Corresponds to the standing-wave structure of the lock condition.

**Uniform activation** (baseline, used for Core Δ₆):
$$f_{Z-}(u,v) = 1$$
All hats equal height. The Core has no spatial variation by definition.

---

## 4.4 Converting Hat Address to Cartesian

Given a hat address (k, u, v, h), the corresponding 3D Cartesian position (x, y, z) is given by the **face transform** T_k:

**For the +Z face (Apex, Δ₅)**:
$$\vec{T}_{Z+}(u, v, h) = \left(d\cdot u,\; d\cdot v,\; \frac{\ell}{2} + h\cdot d\right)$$

**For the −Z face (Core, Δ₆)**:
$$\vec{T}_{Z-}(u, v, h) = \left(d\cdot u,\; d\cdot v,\; -\frac{\ell}{2} - h\cdot d\right)$$

**For the +Y face (Forward, Δ₁)**:
$$\vec{T}_{Y+}(u, v, h) = \left(d\cdot u,\; \frac{\ell}{2} + h\cdot d,\; d\cdot v\right)$$

**For the −Y face (Memory, Δ₂)**:
$$\vec{T}_{Y-}(u, v, h) = \left(d\cdot u,\; -\frac{\ell}{2} - h\cdot d,\; d\cdot v\right)$$

**For the +X face (Expansion, Δ₃)**:
$$\vec{T}_{X+}(u, v, h) = \left(\frac{\ell}{2} + h\cdot d,\; d\cdot u,\; d\cdot v\right)$$

**For the −X face (Compression, Δ₄)**:
$$\vec{T}_{X-}(u, v, h) = \left(-\frac{\ell}{2} - h\cdot d,\; d\cdot u,\; d\cdot v\right)$$

Here **d** is the grid spacing (the physical distance between adjacent hat-grid cells and between hat levels). For a cube of side ℓ with n grid cells per face:

$$d = \frac{\ell}{n}$$

---

## 4.5 Navigating the Box

Hat counting makes the ICHTB traversable. Start at i₀ (the origin in hat space: no face, no position). To reach any point:

1. **Choose a face** k — enter one of the six zones
2. **Choose (u,v)** — pick a position on that face's grid
3. **Choose h** — descend into the interior to depth h
4. **Apply T_k** — convert to Cartesian if needed for field evaluation

Movement between adjacent hats:

- **Lateral move**: (k, u, v, h) → (k, u±1, v, h) or (k, u, v±1, h) — stays on same face, same depth
- **Depth move**: (k, u, v, h) → (k, u, v, h±1) — moves toward or away from i₀
- **Face crossing**: Moving off the edge of one face into an adjacent face — requires a coordinate transformation between face frames

Face crossings are topologically non-trivial — the adjacent face shares an edge but has a different normal direction. The crossing condition:

**Edge from +Y to +X** (shared edge at u=+n/2 on Y-face meets v=+n/2 on X-face):
$$\vec{T}_{Y+}(n/2, v, h) = \vec{T}_{X+}(u, v', h')$$

requires matching the Cartesian coordinates, which gives the mapping between the two face frames.

---

## 4.6 Hat Depth and Field Value

The hat depth h at position (u, v) on face k is not just a navigation parameter — it encodes a field value. Deeper hats correspond to higher local tension |Φ|.

The correspondence:

$$h = \mathcal{H}_k(u,v) \quad \longleftrightarrow \quad |\Phi(\vec{T}_k(u,v,h))| = \alpha_k \cdot f_k(u,v) + \beta_k$$

This means you can read off the field strength at any surface point simply by counting hats. Conversely, if you evaluate the Master Equation at a point and get Φ, you can convert it back to a hat height and know where in the discrete grid that field value lives.

This duality — between continuous field values and discrete hat heights — is what makes the hat system more than just a coordinate system. It is a *measurement protocol*: hat counting is how you quantify the ICHTB without losing the discrete structure that makes navigation meaningful.

---

## 4.7 Total Hat Count: The Volume Invariant

The **total hat count** across all faces is:

$$\mathcal{H}_{\text{total}} = \sum_{k} \sum_{u,v} \mathcal{H}_k(u,v)$$

This sum is a discrete approximation to the volume integral of the field:

$$\mathcal{H}_{\text{total}} \approx \int_{\partial\text{ICHTB}} |\Phi| \, dA$$

When the field reaches a stable shell configuration (see Chapter 5), 𝓗_total becomes approximately constant — the field stops growing globally even as it shifts locally. **Stable shell ↔ constant total hat count.**

This gives a practical closure criterion: run the Master Equation forward in time, compute 𝓗_total at each step. When 𝓗_total stops changing, the recursion has locked.

---

## 4.8 The Hat System as a Collapse Lattice

The hat system is a recursive lattice — not a fixed grid imposed from outside, but a grid that *the field builds for itself*.

The hat heights 𝓗_k(u,v) are computed from f_k(u,v), which is the curvent-aligned activation. As the field evolves (and the curvent **C** updates via its own equation), the activation patterns shift, which shifts the hat heights, which changes the effective lattice.

The lattice adapts to the field. The field adapts to the lattice. This is the discrete version of the same recursion that the continuous Master Equation describes.

**Key insight**: The hat counting system is the ICHTB seen from the outside — the field as it appears to an external observer who can only count discrete features. The Master Equation is the ICHTB seen from the inside — the continuous self-referential dynamics. Both descriptions are the same system.
