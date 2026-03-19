# 16.1 Closure as a Loop Back to the Membrane

## The Geometric Meaning of Closure

In the ICHTB framework, **closure** has a precise geometric meaning: a structure is **closed** if its field configuration contains a closed loop — a closed path in the ICHTB geometry along which the field phase completes a full $2\pi$ winding, returning to its starting value after traveling through a sequence of zones and their membranes.

More formally: a configuration $\Phi$ in the ICHTB is **closed** if there exists a closed path $\gamma: [0,1] \to \text{ICHTB}$ with $\gamma(0) = \gamma(1)$ such that the phase holonomy around $\gamma$ is nontrivial:

$$
\mathcal{H}(\gamma) = \oint_\gamma \nabla\arg\Phi \cdot d\mathbf{l} = 2\pi n, \quad n \in \mathbb{Z}\setminus\{0\}
$$

The winding number $n$ measures how many times the field phase wraps around $2\pi$ as the path $\gamma$ is traversed. A configuration with $n \neq 0$ for some closed path $\gamma$ is topologically closed — it contains a topological defect (a vortex, in 2D; a vortex line, in 3D; a Hopfion, in the full ICHTB volume) that prevents the phase from being continuously unwound to a uniform state.

The key phrase in the chapter overview is **"a structure completing a loop back to the membrane"**: the closed loop must pass through a zone membrane. This is not an arbitrary restriction — it is the condition that distinguishes topological closure (which is durable, resistant to perturbation) from merely kinetic organization (which can unwind without crossing a topological barrier).

---

## Why the Membrane Must Be Crossed

Consider a closed phase loop $\gamma$ that lies entirely within a single zone — say, entirely within the Memory zone. Such a loop can wind around a local vortex core and accumulate a $2\pi$ phase. But because the loop is entirely within the Memory zone, the topological charge is localized within that zone and is unconnected to the other zones. If the Memory zone field is disrupted (by thermal fluctuations, by a passing perturbation), the vortex can annihilate with an antivortex nucleated in the same zone — the topological charge can "escape" within the zone without having to cross any membrane.

Now consider a closed loop $\gamma$ that crosses a zone membrane — passing from the Memory zone (−Y) through the Core (+0) into the Forward zone (+X) and back through the Core into the Memory zone. The phase accumulated in this loop comes from contributions in each zone it passes through:

$$
\mathcal{H}(\gamma) = \int_{\gamma\cap\text{mem}} + \int_{\gamma\cap\text{core}} + \int_{\gamma\cap\text{fwd}} = 2\pi n
$$

For the loop to unwind (to continuously deform to a contractible loop with $\mathcal{H} = 0$), the phase winding in each zone segment must simultaneously unwind — which requires coordinated changes in the field across the zones. Such coordinated multi-zone unwinding requires crossing multiple membranes, each of which has a barrier (the membrane tension $\sigma$, section 11.1). The **topological protection** of a membrane-crossing loop is therefore much stronger than that of a zone-internal loop.

A structure is fully closed (in the ICHTB sense) when its topological charge is supported by loops that cross at least one membrane. In the zone graph language: the topological charge is **non-local** — it is distributed across zone boundaries, not concentrated in a single zone.

---

## The Loop Types and Their Membrane Crossings

The ICHTB zone graph (section 3.1) allows several distinct types of closed loops, characterized by which zones they pass through and which membranes they cross:

**Type-I loops (Memory zone only):** Loops entirely within $\mathcal{V}_{\text{mem}}$. Winding number $n = \pm 1$. Topological protection: weak (single-zone vortex, can annihilate without membrane crossing). These are the **precursor vortices** — the first topological structures to form, before full closure.

**Type-II loops (Memory + Core + Compression):** Loops that pass through the $\mathcal{V}_{\text{mem}} \to \mathcal{V}_{\text{core}} \to \mathcal{V}_{\text{comp}}$ sequence. Winding number $n = \pm 1$. Membrane crossings: 2 (mem→core and core→comp). Topological protection: intermediate. These are the **2.B vortex loops** — the first membrane-crossing topological structures.

**Type-III loops (all six zones + Core):** Loops that traverse the full ICHTB perimeter, passing through all six peripheral zones and the Core. Winding number $n = \pm 1$ (or higher). Membrane crossings: 12 (crossing each of the 12 membrane facets of the cuboctahedron, section 3.3). These are the **3.B Hopf loops** — the maximum-closure topological structures, corresponding to the Hopf invariant of the 3.B configuration.

The hierarchy of closure:
$$\text{Type-I} \subset \text{Type-II} \subset \text{Type-III}$$

Each type is a subset of the next — every Type-III loop configuration contains Type-II loops as sub-loops, and every Type-II contains Type-I loops as sub-loops. The 3.B lock achieves Type-III closure — the maximum topological protection available in the ICHTB geometry.

---

## Closure and the Membrane Return Condition

The phrase "completing a loop **back to the membrane**" encodes a specific geometric condition: the loop must originate at a membrane, pass through the ICHTB interior, and return to the same membrane. This is the **membrane return condition** for closure.

Formally: let $\mathcal{M}_{\alpha\beta}$ be the membrane between zones $\alpha$ and $\beta$. The membrane return condition for a loop $\gamma$ starting and ending at $\mathcal{M}_{\alpha\beta}$:

$$
\gamma(0) \in \mathcal{M}_{\alpha\beta}, \quad \gamma(1) \in \mathcal{M}_{\alpha\beta}, \quad \mathcal{H}(\gamma) = 2\pi n \neq 0
$$

The membrane is a 2D surface within the 3D ICHTB. The loop $\gamma$ starts on this surface, dips into the ICHTB interior (passing through zones), and returns to the same surface. The fact that $\gamma$ ends where it began (both endpoints on $\mathcal{M}_{\alpha\beta}$) means $\gamma$ is a **based loop** — a loop with a fixed base point on the membrane.

The **fundamental group** $\pi_1(\text{ICHTB}\setminus\text{vortex cores})$ classifies all distinct types of membrane-based closed loops. For the cuboctahedral ICHTB with one Hopf vortex structure, $\pi_1 = \mathbb{Z}$ (integers, corresponding to winding number $n$). For a 3.B lock (three-component Hopf structure), $\pi_1 = \mathbb{Z}^3$ (three independent winding numbers, one per Hopf component).

The objecthood of a ICHTB-enclosed configuration is determined by whether it achieves nontrivial elements of this fundamental group — nontrivial membrane-based loops. If $\pi_1$ is trivial ($\mathcal{H}(\gamma) = 0$ for all loops), the configuration is not closed and has no objecthood. If $\pi_1$ is nontrivial ($\mathcal{H}(\gamma) = 2\pi n \neq 0$ for some membrane-based loop $\gamma$), the configuration is closed and achieves objecthood.

---

## Physical Consequences of Closure

The physical consequences of topological closure:

1. **Permanence:** The topological charge $n$ is conserved — it cannot change without crossing a topological barrier (creating or annihilating a topological defect at a membrane). In an undisturbed ICHTB, $n$ is exactly conserved (a topological quantum number).

2. **Discreteness:** The winding number $n \in \mathbb{Z}$ is discrete — it cannot take non-integer values. This is the origin of the discreteness of quantum numbers in the ICHTB framework: the discreteness of spin (half-integer in the fermionic case, integer in the bosonic) traces to the discrete winding numbers of the Memory zone vortex configuration.

3. **Non-local identity:** The closed loop spans multiple zones — the topological charge is non-local. The identity of the particle (its quantum numbers) is encoded non-locally in the ICHTB, not in any single zone. This is the ICHTB realization of the Aharonov-Bohm effect (Aharonov and Bohm 1959, *Phys. Rev.* **115** 485): the phase holonomy around the vortex is measurable even when the field amplitude is zero along the path.

4. **Protection against dissolution:** A closed configuration cannot smoothly deform to the vacuum state — it must first nucleate a topological defect at a membrane, which costs energy $\geq E_{\text{membrane}} = \sigma A_{\text{membrane}}$. This is the ICHTB analog of the energy gap for pair creation: closed configurations (particles) cannot annihilate unless they encounter their topological conjugate (antiparticle) with opposite winding number.

