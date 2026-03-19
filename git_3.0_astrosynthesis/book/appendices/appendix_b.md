# Appendix B: Zone Operator Reference and PDE Catalog

This appendix is a compact reference for the six ICHTB zones: their operators, zone metrics, reduced PDEs, linear modes, and the 12 membrane interfaces between them. For derivations, see Chapters 3, 5, and 6. For excitation taxonomy, see Chapters 7–11.

---

## B.1 Zone Quick-Reference Table

| Zone | Axis | Operator $\hat{\mathcal{O}}_k$ | Operator order | Character | Physical role | A/B states |
|------|------|-------------------------------|----------------|-----------|---------------|------------|
| Apex | +Z | $\partial_t\Phi$ | First (temporal) | Oscillatory | Rate of temporal change; recursion velocity | — (process) |
| Core | −Z | $\mathbf{1}\cdot\Phi$ | Zero | Static | Pre-emergence anchor; $\Phi \to i_0$ | 3.B ceiling |
| Forward | +X | $\nabla_x\Phi$ | First (spatial) | Propagating | Signal transport along $\hat{x}$ | 1.A, 1.B |
| Compression | −X | $-\nabla^2\Phi$ | Second, negative | Focusing | Localization; matter concentration | 3.A, 3.B |
| Expansion | +Y | $+\nabla^2\Phi$ | Second, positive | Spreading | Bloom growth; radial spread | 2.A |
| Memory | −Y | $\nabla\times\mathbf{F}$ | First (antisymmetric) | Circulating | Topological phase storage | 2.A, 2.B |

**Zone geometry:** Each zone is a square pyramid with apex at i₀ and base equal to one face of the unit cube. Volume of each pyramid = $\frac{1}{6}$ of the cube. Zone membership criterion: $\mathbf{x} \in P_k$ iff $\hat{n}_k \cdot \mathbf{x} = \max_j |\hat{n}_j \cdot \mathbf{x}|$. This is the Voronoi partition of the cube with generators at the six face centers (§3.3).

---

## B.2 Zone Metrics

The ICHTB metric field $\mathcal{M}^{ij}(\mathbf{x})$ is piecewise constant within each zone. The zone metric $\mathcal{M}^{ij}_k$ has a dominant eigenvalue in the direction associated with the zone's operator, and suppressed values in the remaining directions. Let $m_+ \gg 1$ be the amplified metric component and $m_0 \ll 1$ be the suppressed components. Explicit forms in the standard basis $\{\hat{x}, \hat{y}, \hat{z}\}$:

### Apex (+Z)
$$
\mathcal{M}^{ij}_{\text{Apex}} = \begin{pmatrix} m_0 & 0 & 0 \\ 0 & m_0 & 0 \\ 0 & 0 & m_+ \end{pmatrix}
$$
Amplifies $\partial_z$ (temporal proxy); suppresses $x$- and $y$-diffusion.

### Core (−Z)
$$
\mathcal{M}^{ij}_{\text{Core}} \approx \begin{pmatrix} m_0 & 0 & 0 \\ 0 & m_0 & 0 \\ 0 & 0 & m_0 \end{pmatrix}
$$
All components suppressed; no spatial operator dominates. The $-\kappa\Phi$ damping term is unchallenged. This is the zone of the fixed point $\Phi^* = i_0$.

### Forward (+X)
$$
\mathcal{M}^{ij}_{\text{Fwd}} = \begin{pmatrix} m_+ & 0 & 0 \\ 0 & m_0 & 0 \\ 0 & 0 & m_0 \end{pmatrix}
$$
Amplifies diffusion along $\hat{x}$; transverse diffusion suppressed. Produces highly anisotropic (rod-like) transport.

### Compression (−X)
$$
\mathcal{M}^{ij}_{\text{Comp}} = \begin{pmatrix} m_+ & 0 & 0 \\ 0 & m_+ & 0 \\ 0 & 0 & m_+ \end{pmatrix}
$$
All spatial components amplified, but the Compression zone operator is $-\nabla^2$ — the sign of the metric interaction with the diffusion term is reversed (the diffusion term $D\nabla_i(\mathcal{M}^{ij}\nabla_j\Phi)$ acts as $-D m_+ \nabla^2\Phi$ in the Compression zone because the zone geometry drives the field toward its maximum, not away from it).

### Expansion (+Y)
$$
\mathcal{M}^{ij}_{\text{Exp}} = \begin{pmatrix} m_0 & 0 & 0 \\ 0 & m_+ & 0 \\ 0 & 0 & m_0 \end{pmatrix}
$$
Amplifies diffusion in $\hat{y}$; produces preferential spreading in the Expansion direction.

### Memory (−Y)
$$
\mathcal{M}^{ij}_{\text{Mem}} = \begin{pmatrix} m_0 & -m_A & 0 \\ m_A & m_0 & 0 \\ 0 & 0 & m_0 \end{pmatrix}
$$
The off-diagonal antisymmetric components $\pm m_A$ couple orthogonal gradient components, producing rotational rather than translational field dynamics (curl behavior). The antisymmetric part $\mathcal{M}^{[ij]}_{\text{Mem}} = m_A\,\epsilon^{ij3}$ acts as a magnetic-field-like term.

---

## B.3 Reduced PDE in Each Zone

The CTS master equation restricted to zone $k$ (using the zone's specific metric $\mathcal{M}^{ij}_k$):

$$
\partial_t\Phi = D\,\nabla_i(\mathcal{M}^{ij}_k\,\nabla_j\Phi) - \Lambda\,\mathcal{M}^{ij}_k(\nabla_i\Phi)(\nabla_j\Phi) + \gamma|\Phi|^2\Phi - \kappa\Phi
$$

### Apex (+Z) — Temporal Evolution Zone

$$
\partial_t\Phi \approx D\,m_+\,\partial_z^2\Phi - \Lambda\,m_+(\partial_z\Phi)^2 + \gamma|\Phi|^2\Phi - \kappa\Phi
$$

Dominant dynamics along $\hat{z}$ only; transverse terms suppressed by $m_0/m_+ \ll 1$. In the Apex zone, the field changes fastest in time — it is the zone of rapid phase advance ($\partial_t\theta$ is largest here).

### Core (−Z) — Pre-Emergence Anchor

$$
\partial_t\Phi \approx D\,m_0\,\nabla^2\Phi - \Lambda\,m_0|\nabla\Phi|^2 + \gamma|\Phi|^2\Phi - \kappa\Phi \approx \gamma|\Phi|^2\Phi - \kappa\Phi
$$

Spatial terms are $O(m_0)$ and negligible. The Core dynamics reduce to the **local ODE**:

$$
\partial_t\Phi = (\gamma|\Phi|^2 - \kappa)\Phi
$$

Fixed points: $\Phi = 0$ (stable vacuum) and $|\Phi|^2 = \kappa/\gamma = |\Phi_B|^2$ (B-state threshold). The Core zone governs which fixed point the field approaches.

### Forward (+X) — Propagation Zone

$$
\partial_t\Phi \approx D\,m_+\,\partial_x^2\Phi - \Lambda\,m_+(\partial_x\Phi)^2 + \gamma|\Phi|^2\Phi - \kappa\Phi
$$

Effectively one-dimensional along $\hat{x}$. In the linear limit ($\gamma, \Lambda \to 0$):

$$
\partial_t\Phi = D\,m_+\,\partial_x^2\Phi - \kappa\Phi \quad \Rightarrow \quad \omega = D\,m_+\,k^2 + i\kappa \text{ (damped diffusion wave)}
$$

With flux coupling $\Lambda > 0$: supports soliton solutions (1.B states) via balance between $D\,m_+\,\partial_x^2\Phi$ (spreading) and $-\Lambda\,m_+(\partial_x\Phi)^2$ (focusing).

### Compression (−X) — Focusing Zone

$$
\partial_t\Phi \approx -D\,m_+\,\nabla^2\Phi - \Lambda\,m_+|\nabla\Phi|^2 + \gamma|\Phi|^2\Phi - \kappa\Phi
$$

The negative sign of the Laplacian drives the field toward concentration at its local maximum. The Compression zone is linearly **stable** to amplitude perturbations (the $-\nabla^2$ drives peaks inward, not outward) and supports localized stationary states.

### Expansion (+Y) — Growth Zone

$$
\partial_t\Phi \approx D\,m_+\,\nabla^2\Phi - \Lambda\,m_+|\nabla\Phi|^2 + \gamma|\Phi|^2\Phi - \kappa\Phi
$$

The positive Laplacian makes the Expansion zone linearly **unstable** for modes with $D\,m_+\,q^2 > \kappa$: such modes grow exponentially until saturated by the cubic term $\gamma|\Phi|^2\Phi$. This is the zone of bloom: without nonlinear saturation, growth is unbounded.

Linear instability threshold wavevector: $q_c = \sqrt{\kappa / (D\,m_+)}$ — modes with $q < q_c$ are unstable.

### Memory (−Y) — Rotational Storage Zone

$$
\partial_t\Phi \approx D\,\partial_i([\mathcal{M}^{ij}_{\text{Mem}}]\partial_j\Phi) - \Lambda\,\mathcal{M}^{ij}_{\text{Mem}}(\partial_i\Phi)(\partial_j\Phi) + \gamma|\Phi|^2\Phi - \kappa\Phi
$$

The antisymmetric metric components $\pm m_A$ generate rotational field dynamics. Expanding the diffusion term:

$$
D\,\nabla_i(\mathcal{M}^{ij}_{\text{Mem}}\nabla_j\Phi) = D\,m_0\,\nabla^2\Phi + D\,m_A\,(\partial_x\partial_y - \partial_y\partial_x)\Phi = D\,m_0\,\nabla^2\Phi + D\,m_A\,[\nabla\times\nabla]\Phi
$$

In polar coordinates $(r, \phi)$ in the $xy$-plane, the Memory zone PDE naturally supports phase-winding solutions $\Phi \sim f(r)e^{in\phi}$ — the 2.B vortex states with winding number $n \in \mathbb{Z}$.

---

## B.4 Linear Modes and Dispersion Relations

In the linear limit ($\Lambda = 0$, $\gamma = 0$, small $|\Phi|$), the master equation in each zone has plane-wave solutions $\Phi \propto e^{i(\mathbf{k}\cdot\mathbf{x} - \omega t)}$ with dispersion relation:

$$
-i\omega = D\,\mathcal{M}^{ij}_k\,k_i k_j - \kappa
$$

Zone-by-zone dispersion relations (leading-order in $m_+$):

| Zone | Dominant dispersion | Character |
|------|--------------------|-----------|
| Apex (+Z) | $-i\omega = D\,m_+\,k_z^2 - \kappa$ | Diffusion along $\hat{z}$ only |
| Core (−Z) | $-i\omega = D\,m_0\,k^2 - \kappa \approx -\kappa$ | Spatially flat; pure decay |
| Forward (+X) | $-i\omega = D\,m_+\,k_x^2 - \kappa$ | 1D diffusion wave along $\hat{x}$ |
| Compression (−X) | $-i\omega = -D\,m_+\,k^2 - \kappa$ | All modes stable (negative definite) |
| Expansion (+Y) | $-i\omega = D\,m_+\,k^2 - \kappa$ | Unstable for $k < k_c = \sqrt{\kappa/Dm_+}$ |
| Memory (−Y) | $-i\omega = D\,m_0\,k^2 + iD\,m_A\,(k_x k_y - k_y k_x) - \kappa$ | Rotation-coupled; complex $\omega$ |

The **coherence length** $\xi = \sqrt{D/\kappa}$ sets the crossover scale in every zone. Modes with spatial scale $\ell \gg \xi$ are damping-dominated; modes with $\ell \ll \xi$ are diffusion-dominated.

---

## B.5 Excitation Taxonomy in Zone Terms

| Class | Name | Dimensions | Linear/NL | Primary zone(s) | Secondary zone(s) | Bloom shape |
|-------|------|------------|-----------|-----------------|-------------------|-------------|
| 1.A | Linear rod | 1D | Linear | Forward (+X) | — | Gaussian cylinder along $\hat{x}$ |
| 1.B | Soliton | 1D | Nonlinear | Forward (+X) | Compression (−X) | $\text{sech}(x/\xi_s)$ profile, non-spreading |
| 2.A | Linear disc | 2D | Linear | Expansion (+Y) | Memory (−Y) | $J_0(k r_\perp)$ Bessel disc |
| 2.B | Vortex sheet | 2D | Nonlinear | Memory (−Y) | Expansion (+Y) | Ring with winding number $n$; $\Phi \sim f(r)e^{in\phi}$ |
| 3.A | Linear volume | 3D | Linear | All (uniform) | — | Spherical harmonics $j_\ell(kr)Y_\ell^m$ |
| 3.B | Topological knot | 3D | Nonlinear | Core (−Z) + All | — | Hopfion; linked phase field lines |

**Amplitude criterion separating A from B:** $|\Phi|^2 \ll \kappa/\gamma$ (A state) vs. $|\Phi|^2 \sim \kappa/\gamma = |\Phi_B|^2$ (B state).

**Soliton width (1.B):**
$$
\xi_s = \sqrt{\frac{2D\,m_+}{\gamma\,A_0^2}}
\tag{B.1}
$$

**Vortex core radius (2.B):**
$$
r_v \approx \xi = \sqrt{\frac{D}{\kappa}}
\tag{B.2}
$$

**3.B Hopf invariant:** $H = \frac{1}{16\pi^2}\int \mathbf{F}\cdot(\nabla\times\mathbf{F})\,d^3x \in \mathbb{Z}$, where $\mathbf{F}$ is the field-phase flux vector.

---

## B.6 The 12 Membrane Interfaces

The six zones share 12 triangular membrane faces (the faces of the cuboctahedron). Opposite zones (+X/−X, +Y/−Y, +Z/−Z) are **not** adjacent — they never share a membrane.

### Zone Adjacency Table

| Membrane | Zone $\alpha$ | Zone $\beta$ | Operator pair | Junction sign $s_{\alpha\beta}$ | Physical effect |
|----------|--------------|--------------|---------------|-------------------------------|-----------------|
| F1 | Forward (+X) | Expansion (+Y) | $\nabla_x$ / $+\nabla^2$ | $+1$ | Amplifying: signal reinforces bloom |
| F2 | Forward (+X) | Apex (+Z) | $\nabla_x$ / $\partial_t$ | $+1$ | Amplifying: signal accelerates |
| F3 | Forward (+X) | Memory (−Y) | $\nabla_x$ / $\nabla\times$ | $-1$ | Damping: circulation drains directional signal |
| F4 | Forward (+X) | Core (−Z) | $\nabla_x$ / $\mathbf{1}$ | $-1$ | Damping: signal drains toward vacuum |
| F5 | Expansion (+Y) | Apex (+Z) | $+\nabla^2$ / $\partial_t$ | $+1$ | Amplifying: bloom reinforces temporal growth |
| F6 | Expansion (+Y) | Memory (−Y) | $+\nabla^2$ / $\nabla\times$ | $0$ | Neutral: bloom ↔ circulation exchange |
| F7 | Expansion (+Y) | Core (−Z) | $+\nabla^2$ / $\mathbf{1}$ | $-1$ | Damping: bloom drains to vacuum |
| F8 | Apex (+Z) | Compression (−X) | $\partial_t$ / $-\nabla^2$ | $-1$ | Damping: temporal growth meets compression |
| F9 | Apex (+Z) | Memory (−Y) | $\partial_t$ / $\nabla\times$ | $0$ | Neutral: time ↔ rotation exchange |
| F10 | Compression (−X) | Memory (−Y) | $-\nabla^2$ / $\nabla\times$ | $0$ | Neutral: saddle junction |
| F11 | Compression (−X) | Core (−Z) | $-\nabla^2$ / $\mathbf{1}$ | $-1$ | Strongly damping: double negative |
| F12 | Memory (−Y) | Core (−Z) | $\nabla\times$ / $\mathbf{1}$ | $-1$ | Damping: circulation drains to vacuum |

**Most amplifying path:** Forward → Expansion → Apex → (cycle). Three consecutive $+1$ junctions; the engine of A-state bloom dynamics.

**Most damping path:** Compression → Core. The drain through which B-state excitations return energy to the pre-emergence vacuum.

---

## B.7 Membrane Junction Conditions

At the interior of any membrane face separating zones $\alpha$ and $\beta$, two conditions hold:

**Condition 1 — Field continuity (Dirichlet):**
$$
\Phi_\alpha(\mathbf{p}) = \Phi_\beta(\mathbf{p})
\tag{B.3}
$$

**Condition 2 — Normal flux jump (Neumann/Robin):**
$$
\left[D\,\mathcal{M}^{ij}_\beta\,n_i\partial_j\Phi_\beta - D\,\mathcal{M}^{ij}_\alpha\,n_i\partial_j\Phi_\alpha\right]_{\mathbf{p}} = \sigma(\mathbf{p})\,\Phi(\mathbf{p})
\tag{B.4}
$$

where $\hat{n}$ is the unit normal to the membrane at $\mathbf{p}$ pointing from $\alpha$ into $\beta$, and $\sigma(\mathbf{p})$ is the membrane surface conductance.

**Transmission coefficient** for a plane wave normally incident from zone $\alpha$:
$$
T_{\alpha\to\beta} = \frac{4D^2\,\mathcal{M}^{nn}_\alpha\,\mathcal{M}^{nn}_\beta\,k_\alpha\,k_\beta}{\left(D\,\mathcal{M}^{nn}_\alpha\,k_\alpha + D\,\mathcal{M}^{nn}_\beta\,k_\beta\right)^2 + \sigma^2}
\tag{B.5}
$$

where $k_\alpha, k_\beta$ are the wavenumbers in each zone and $\mathcal{M}^{nn} = \mathcal{M}^{ij}n_in_j$ is the normal metric component.

**CTS Snell's law** (oblique incidence at angle $\theta_\alpha$ to the membrane normal):
$$
\sqrt{\mathcal{M}^{tt}_\alpha}\,\sin\theta_\alpha = \sqrt{\mathcal{M}^{tt}_\beta}\,\sin\theta_\beta
\tag{B.6}
$$

where $\mathcal{M}^{tt}$ is the tangential metric component. Total internal reflection occurs when $\sin\theta_\beta > 1$, i.e., $\mathcal{M}^{tt}_\alpha\sin^2\theta_\alpha > \mathcal{M}^{tt}_\beta$.

### Junction Condition by Operator Type

| Case | Operator pair | Flux conditions |
|------|---------------|-----------------|
| A | $+\nabla^2$ / $-\nabla^2$ (Expansion / Compression) | Symmetric: both sides contribute normal flux |
| B | Second-order / First-order (e.g., Expansion / Forward) | Asymmetric: only second-order side contributes flux |
| C | First-order / Zero-order (any zone / Core) | Continuity only: no flux jump possible |

---

## B.8 Zone Exchange Zones (ZEZ)

Each membrane has a **Zone Exchange Zone** — a transition layer of thickness $\sim \ell$ on either side, within which the metric interpolates smoothly between the two zone values:

$$
\mathcal{M}^{ij}(\mathbf{x}) = \mathcal{M}^{ij}_\alpha + \frac{\mathcal{M}^{ij}_\beta - \mathcal{M}^{ij}_\alpha}{1 + e^{-d(\mathbf{x})/\ell}}
\tag{B.7}
$$

where $d(\mathbf{x})$ is signed distance from the membrane and $\ell \sim \xi = \sqrt{D/\kappa}$.

**ZEZ resonance condition** for reflectionless passage through the membrane:
$$
\frac{\sqrt{\mathcal{M}^{nn}_\beta - \mathcal{M}^{nn}_\alpha}\,A_0\,k_\perp\,\ell}{\sqrt{2D}} = \frac{n\pi}{2}, \quad n \in \mathbb{Z}
\tag{B.8}
$$

When satisfied: excitation passes through without reflection (transparent membrane for that mode). When not satisfied: partial reflection — the membrane acts as a zone-selective filter.

**A states** (small $A_0$) satisfy (B.8) easily → propagate freely across all zones.

**B states** (large $A_0 \sim \Phi_B$) typically do not satisfy (B.8) → reflected at zone boundaries → localized to home zone.

**Net energy flux through membrane face $\Delta_k$:**
$$
\dot{E}_k = -D\int_{\Delta_k}\mathrm{Re}\!\left(\Phi^*\,\llbracket\mathcal{M}^{ij}n_i\partial_j\Phi\rrbracket\right)d^2S
\tag{B.9}
$$

**Membrane energy conservation:**
$$
\sum_{k=1}^{12}\dot{E}_k = 0
\tag{B.10}
$$

Energy flows between zones through the membranes; the total membrane source is zero.

---

## B.9 Zone Identifiers in Hat-Counting Notation

Each point $\mathbf{x} \in P_k$ in the ICHTB carries a **hat-counting address** specifying which zones have been traversed from i₀. The first level of the address is the home zone symbol:

| Hat symbol | Zone | Axis |
|------------|------|------|
| $\hat{+}$ | Apex | +Z |
| $\hat{-}$ | Core | −Z |
| $\hat{>}$ | Forward | +X |
| $\hat{<}$ | Compression | −X |
| $\hat{\uparrow}$ | Expansion | +Y |
| $\hat{\circlearrowleft}$ | Memory | −Y |

The full hat-counting address encodes the complete zone-traversal history from i₀ to $\mathbf{x}$ — see Appendix D for the full navigation rules.

---

*See also: Appendix A (Master Equation derivation), Appendix D (Hat-Counting and zone navigation), Appendix G (Notation and conventions), Chapter 3 (Six zones), Chapter 5 (Master equation), Chapter 6 (Edge-case mathematics).*
