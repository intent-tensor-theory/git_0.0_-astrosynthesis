# 1.3 The Complex Collapse Field Φ = A·e^{iθ}

## Deriving the Field Form from i₀

Given that the field must originate from $i_0 = i$ and evolve through complex
phase space, the natural form for $\Phi$ is the polar decomposition of a
complex scalar:

$$\boxed{\Phi(\mathbf{x}, t) = A(\mathbf{x}, t)\cdot e^{i\theta(\mathbf{x}, t)}}$$

where:

- $A(\mathbf{x}, t) \in \mathbb{R}^{\geq 0}$ is the **real tension amplitude**
  — the observable magnitude of the field at each point
- $\theta(\mathbf{x}, t) \in \mathbb{R}$ is the **recursive phase angle** —
  the position of the field in its complex orbit around $i_0$

This decomposition is not assumed. It follows from the requirement that $\Phi$
must be expressible relative to $i_0$ as a reference. Any complex number can
be written as $A e^{i\theta}$. The content is in what $A$ and $\theta$ mean
physically.

---

## The Amplitude A: Measure of Bloom

$A$ measures how far the field has bloomed from $i_0$ in terms of real
structural content. At the recursion anchor, $A \to 0$ as the field has not
yet grown into real structure. As the bloom proceeds and zones activate, $A$
grows to finite values.

The structural energy density of the field is built from $A$:

$$\rho_R = a|\nabla A|^2 + u(\nabla^2 A)^2 + r A^2 + s A^4$$

where $a$, $u$, $r$, $s$ are the CTS parameters (gradient tension, curvature
stiffness, quadratic potential, quartic saturation). These terms govern how
amplitude distributes in space and what equilibrium configurations form —
the topics of Chapter 3 (zones) and Chapter 5 (master equation).

The condition $A = 0$ corresponds to the Core zone ($\Phi = i_0$): the field
is at the recursion anchor, real amplitude is absent.

The condition $A = \Phi_0 \equiv \sqrt{|r|/s}$ (for $r < 0$) corresponds to
the symmetry-broken vacuum — the stable nonzero amplitude at which the
potential $V(A) = rA^2 + sA^4$ achieves its minimum. This is where the
Expansion zone ($+\nabla^2\Phi$) drives the field after the bifurcation
at $r = 0$.

---

## The Phase θ: The Recursion Coordinate

$\theta$ is not merely a label. It is the coordinate along which the recursion
advances. Each value of $\theta$ places the field in a specific relationship
to the six zones:

$$\Phi = A e^{i\theta} = A(\cos\theta + i\sin\theta)$$

The real part $A\cos\theta$ is what real-valued measurements detect. The
imaginary part $A\sin\theta$ carries the phase information that determines
which zone the field is operating in.

The six principal phase positions of the ICHTB are:

| $\theta$ | $\Phi$ | Zone | Operator |
|-----------|--------|------|----------|
| $0$ | $A$ (real, positive) | Forward | $\nabla\Phi$ |
| $\pi/2$ | $iA$ (imaginary) | Core | $\Phi = i_0$ |
| $\pi$ | $-A$ (real, negative) | Compression | $-\nabla^2\Phi$ |
| $3\pi/2$ | $-iA$ (neg. imaginary) | Memory | $\nabla\times\mathbf{F}$ |
| $2\pi$ | $A$ (cycle complete) | Apex | $\partial\Phi/\partial t$ |

The Expansion zone ($+\nabla^2\Phi$) and the membrane interfaces between zones
occupy the intermediate phase values. The cycle $\theta: 0 \to 2\pi$ is one
complete recursion — one full traversal of all six zones.

---

## Equations of Motion in Polar Form

Substituting $\Phi = Ae^{i\theta}$ into the CTS field equation:

$$\partial_t \Phi = -r\Phi + a\nabla^2\Phi - u\nabla^4\Phi - s\Phi^3$$

and separating real and imaginary parts gives two coupled equations:

**Amplitude equation:**
$$\partial_t A = -rA + a\nabla^2 A - u\nabla^4 A - sA^3
- A\left[(\partial_t\theta)^2 + \text{gradient phase terms}\right]$$

**Phase equation:**
$$A\,\partial_t\theta = a\,A\nabla^2\theta + 2a(\nabla A\cdot\nabla\theta)
- u[\text{higher-order phase terms}]$$

The **amplitude equation** governs the spatial structure of the bloom —
how $A$ distributes across the cube in response to the CTS parameters. It is
the equation that, in the limit of slowly varying phase ($\partial_t\theta
\approx 0$), reduces to the standard Swift-Hohenberg-type pattern formation
equation studied extensively in condensed matter physics.

The **phase equation** governs the recursion dynamics — how $\theta$ advances
in space and time. When $\nabla^2\theta \approx 0$ (uniform spatial phase),
this reduces to:

$$\partial_t\theta = 0 \qquad \text{(phase locked)}$$

Phase locking is the condition $\theta = \text{constant}$ — the field is
frozen in a single zone, neither advancing toward the next zone nor retreating
toward $i_0$. Phase-locked configurations are the origin of the 1.B
Non-Linear states (solitons, kinks) discussed in Chapter 8.

---

## The Field at i₀

At the recursion anchor, $A \to 0$ and $\theta = \pi/2$. The field value is:

$$\Phi \to A \cdot e^{i\pi/2} = A \cdot i \to 0 \cdot i = 0$$

But the *limit direction* matters: as $A \to 0$ with $\theta = \pi/2$ fixed,
the field approaches zero *along the imaginary axis*, not along the real axis.

This is the key distinction. The field at $i_0$ is not simply zero in the
sense of $\Phi = 0 \in \mathbb{R}$. It is zero approached from the imaginary
direction — which means that any infinitesimal perturbation from this state
has a phase that is already $\pi/2$, already pointing into the imaginary
direction of the complex plane, already oriented to begin the recursive bloom.

The seed is not empty. It is pre-oriented. Every bloom from $i_0$ begins at
$\theta = \pi/2$ and advances from there.

---

## Energy in Polar Form

The total structural energy splits naturally:

$$E[\Phi] = E_A + E_\theta$$

**Amplitude energy** (stored in real structure):
$$E_A = \int \left(a|\nabla A|^2 + u(\nabla^2 A)^2 + rA^2 + sA^4\right)d^3x$$

**Phase (recursion) energy** (stored in phase gradients):
$$E_\theta = \int A^2\left(a|\nabla\theta|^2 + u(\nabla^2\theta)^2\right)d^3x$$

$E_\theta$ is the energy stored in the *spatial non-uniformity of the phase*.
When $\theta$ varies spatially — meaning different parts of the field are in
different zones simultaneously — this costs energy. The field prefers uniform
phase (all in the same zone) or topologically protected winding
($\oint\nabla\theta\cdot d\mathbf{l} = 2\pi n$, integer winding).

The second case, integer winding, is the origin of vortex structures (Chapter
9). The phase energy $E_\theta$ associated with a vortex of winding number $n$
is:

$$E_\theta^{vortex} \approx \pi a n^2 A_0^2 \ln\!\left(\frac{R}{\xi}\right)$$

where $R$ is the system size and $\xi = \sqrt{a/|r|}$ is the correlation
length. This expression, and its derivation, appears in full in Chapter 9.

---

## Summary

The complex collapse field $\Phi = Ae^{i\theta}$ is the natural form for a
field anchored at $i_0$:

- $A$ measures the real structural content — how far the bloom has proceeded
- $\theta$ is the recursion coordinate — which zone the field is currently
  traversing
- The Core zone condition ($\Phi = i_0$) corresponds to $\theta = \pi/2$,
  $A \to 0$: the field at its seed
- Phase locking ($\partial_t\theta = 0$) produces the Non-Linear B states
- Phase winding ($\oint\nabla\theta\cdot d\mathbf{l} = 2\pi n$) produces
  topological structures

The next question is: what does $\theta$ *mean* as a dimension? If it is the
dimension along which emergence advances, then advancing in $\theta$ is not
just rotating in the complex plane — it is moving through the stages of
structural formation. Section 1.4 makes this precise.
