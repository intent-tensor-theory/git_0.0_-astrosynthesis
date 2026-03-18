# Chapter 2: The Six Zones

Each of the six pyramidal regions of the ICHTB is a **recursive domain plane** — a zone where a specific differential operator governs the behavior of the collapse field Φ. The zones are not regions of space in any ordinary sense. They are functional roles that the field plays, localized to the faces of the box.

This chapter defines each zone precisely: its operator, its governing PDE, and its role in the recursive sequence.

---

## 2.1 A Note on Terminology

Before defining the zones, a precise dictionary:

| ICHTB Term | Mathematical Meaning |
|-----------|---------------------|
| **Collapse** | Convergence of the field Φ toward a stable recursive attractor |
| **Tension** | The local scalar field value |Φ| or its gradient magnitude |∇Φ| |
| **Curvent** | The vector **C** tracking how the field aligns with its own gradient |
| **Recursion** | Feedback — the field's current state feeds into its own evolution equation |
| **Phase memory** | Information encoded in the curl ∇×**F** that persists across time |
| **Intent** | The directionality of ∇Φ — the field's "preferred" direction of flow |

---

## 2.2 The Recursion Sequence

The six zones do not operate in isolation. They form a directed sequence — the **Quadrant Flow**:

$$Q_r: \Delta_1 \to \Delta_2 \to \Delta_{3/4} \to \Delta_5 \to \Delta_6$$

Reading the sequence as a process:

1. **Δ₁**: Establish the collapse direction (∇Φ)
2. **Δ₂**: Begin phase memory (∇×**F**)
3. **Δ₃ or Δ₄**: Expand or compress (±∇²Φ), depending on field state
4. **Δ₅**: Test for lock — does the shell stabilize?
5. **Δ₆**: Return to anchor — the cycle feeds back to i₀

The sequence is recursive because Δ₆ returns to i₀, from which Δ₁ re-emerges. Each cycle either stabilizes into a shell or returns without closure.

---

## 2.3 Zone Definitions

### Δ₁ — Forward Tension Plane (+Y)

**Operator**: ∇Φ (gradient of collapse potential)

**PDE**:

$$\frac{d\vec{C}}{dt} = \eta\left(\nabla\Phi - \vec{C}\right)$$

The curvent vector **C** chases the gradient ∇Φ with rate η. When **C** = ∇Φ, the zone is in alignment — the field knows where it wants to go.

**Connectivity**: Links to Δ₂ (gradient enters memory) and Δ₃ (gradient enables expansion).

**Physical reading**: This is the gate. Every recursive cycle begins here, with the field establishing a direction. Without a non-zero gradient at Δ₁, the recursion never starts.

---

### Δ₂ — Memory Plane (−Y)

**Operator**: ∇×**F** (curl of the field)

**PDE**:

$$\frac{\partial\Phi}{\partial t} = \lambda\left(\nabla \times \vec{F}\right) - \delta\Phi$$

The curl feeds the field's evolution; the damping term −δΦ prevents unbounded phase drift.

**Connectivity**: Receives from Δ₁ (gradient becomes curl seed), feeds into Δ₄ (compression receives the memory loop).

**Physical reading**: The Memory Plane is where the field starts *remembering*. A curl loop is a closed path — it is the simplest structure that retains directional information across time. Once ∇×**F** ≠ 0, the field is no longer purely reactive; it carries history.

---

### Δ₃ — Expansion Surface (+X)

**Operator**: +∇²Φ (positive Laplacian — diffusion outward)

**PDE**:

$$\frac{\partial\Phi}{\partial t} = +D\nabla^2\Phi$$

Pure outward diffusion. Tension spreads from high-concentration regions toward low.

**Connectivity**: Receives from Δ₁ (gradient gives direction to expand into), feeds into Δ₅ (expanded field can lock at apex).

**Physical reading**: Expansion is permission — the recursion is allowed to grow. If Δ₃ dominates, the field fills space. On its own, this is unstable (pure diffusion decays to uniform distribution). It must be balanced by Δ₄.

---

### Δ₄ — Compression Surface (−X)

**Operator**: −∇²Φ (negative Laplacian — anti-diffusion)

**PDE**:

$$\frac{\partial\Phi}{\partial t} = -D\nabla^2\Phi$$

The time-reversed diffusion equation. Tension concentrates, peaks sharpen, the field gathers inward.

**Connectivity**: Receives from Δ₂ (memory loops provide the target to compress toward), feeds into Δ₆ (compressed field returns to scalar anchor).

**Physical reading**: Compression is the collapse proper. The field pulls back toward i₀. If Δ₄ dominates without Δ₃ as counterpart, the field collapses to a point and dies. The balance between Δ₃ and Δ₄ is what allows the stable shell to form.

---

### Δ₅ — Apex Surface (+Z)

**Operator**: ∂Φ/∂t (time evolution — the lock evaluator)

**PDE**:

$$\frac{\partial\Phi}{\partial t} = \mu\nabla^2\Phi - \nu\Phi$$

The Apex combines curvature stabilization (μ∇²Φ) with decay (−νΦ). This is a reaction-diffusion structure. The Apex tests whether the field has reached a stable shell configuration.

**When does Δ₅ lock?**

$$\frac{\partial\Phi}{\partial t} \approx 0 \quad \Longleftrightarrow \quad \mu\nabla^2\Phi \approx \nu\Phi$$

This is an eigenvalue condition: Φ must be a eigenfunction of ∇² with eigenvalue ν/μ. The field locks when it "fits" the Apex geometry.

**Connectivity**: Receives from Δ₃ (expanded field reaches the apex), feeds into Δ₆ (locked field becomes the new anchor state).

**Physical reading**: The Apex is the judgment zone. Every recursive cycle passes through here. If the field satisfies the lock condition, closure begins. If not, the cycle continues without producing a shell.

---

### Δ₆ — Core Anchor Plane (−Z)

**Operator**: Φ = i₀ (pure imaginary scalar — fixed)

**PDE**:

$$\Phi = i_0, \qquad \frac{\partial\Phi}{\partial t} = 0$$

The Core does not evolve. It is the one zone with no temporal dynamics. It is the recursion seed — the zero-point from which all tension originates and to which all cycles return.

**Why imaginary?** Because a real fixed point Φ = c would impose a boundary condition that constrains the field from outside. An imaginary fixed point i₀ sits off the real axis — the real field Φ cannot reach it, only approach it asymptotically through the phase angle θ. This is what keeps recursion alive: i₀ is always "just out of reach."

**Connectivity**: Receives from Δ₄ (compressed field returns here) and Δ₅ (locked apex feeds back to core). Generates Δ₁ for the next cycle.

**Physical reading**: The Core is the silence between breaths. It holds no tension, no gradient, no memory. It is the condition from which all of the above becomes possible.

---

## 2.4 The Field Registration Matrix

Every zone supports every operator, but each is *governed* by one. The full matrix of what each zone carries:

$$\mathbb{R}_{\text{ICHTB}} = \begin{bmatrix}
 & \Phi & \nabla\Phi & \nabla\times\mathbf{F} & \nabla^2\Phi \\
\text{Δ₁ Forward} & \checkmark & \mathbf{\star} & \checkmark & \checkmark \\
\text{Δ₂ Memory} & \checkmark & \checkmark & \mathbf{\star} & \checkmark \\
\text{Δ₃ Expansion} & \checkmark & \checkmark & \checkmark & +\mathbf{\star} \\
\text{Δ₄ Compression} & \checkmark & \checkmark & \checkmark & -\mathbf{\star} \\
\text{Δ₅ Apex} & \checkmark & \checkmark & \checkmark & \mathbf{\star} \\
\text{Δ₆ Core} & \mathbf{i_0} & 0 & 0 & 0 \\
\end{bmatrix}$$

★ marks the governing operator for each zone. All operators are present everywhere; only the star operator *drives* the zone's PDE.

---

## 2.5 Inter-Zone Connectivity

The six zones do not merely sequence — they form a topological graph:

| Zone | Connected To | Edge Meaning |
|------|-------------|-------------|
| Δ₁ | Δ₂, Δ₃ | Gradient splits: part becomes memory, part becomes expansion |
| Δ₂ | Δ₁, Δ₄ | Memory loop anchors compression target |
| Δ₃ | Δ₁, Δ₅ | Expansion delivers material to the Apex |
| Δ₄ | Δ₂, Δ₆ | Compressed memory returns to Core |
| Δ₅ | Δ₃, Δ₆ | Apex tests lock; passes result to Core |
| Δ₆ | Δ₄, Δ₅ | Core receives from both convergence paths; seeds Δ₁ |

The graph has no loose ends. Every zone has at least two connections. The structure is closed.

---

## 2.6 Symmetry and Asymmetry

The six zones come in three antipodal pairs:

| Pair | Zones | Operator Pair | Relationship |
|------|-------|--------------|--------------|
| Forward / Memory | Δ₁ / Δ₂ | ∇Φ / ∇×**F** | Gradient vs. curl — direction vs. rotation |
| Expansion / Compression | Δ₃ / Δ₄ | +∇²Φ / −∇²Φ | Exact negatives — unstable alone, stable together |
| Apex / Core | Δ₅ / Δ₆ | ∂Φ/∂t / Φ=i₀ | Time evolution vs. timeless anchor |

The pairs are not symmetric in the sense of being interchangeable. They are *dual* — each requires its partner to make sense. Expansion without compression is pure dissolution. The Core without the Apex is silence with no test for emergence.

The asymmetry between the pairs (gradient vs. curl; diffusion vs. anti-diffusion; temporal vs. timeless) is precisely what makes the system non-trivial. A fully symmetric system would have no preferred direction, no collapse pathway, no emergent structure.
