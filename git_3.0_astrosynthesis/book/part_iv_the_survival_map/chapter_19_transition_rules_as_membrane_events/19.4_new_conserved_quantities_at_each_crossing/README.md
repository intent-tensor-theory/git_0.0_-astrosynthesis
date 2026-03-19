# 19.4 New Conserved Quantities at Each Crossing

## The Conservation Hierarchy

The central claim of this section: **each membrane crossing generates exactly one new conserved quantity**, which is added to the set of conserved charges of the ICHTB configuration. The conserved quantities accumulate as the configuration progresses through the survival regions, building up the full quantum number set identified in section 16.4.

This is the **conservation hierarchy** of the ICHTB:

| Transition | New conserved quantity | Symbol | Physical meaning |
|---|---|---|---|
| A-state → Region I | Propagation current | $J_x$ | Momentum in +X direction |
| I → II | Core amplitude | $N_{\text{core}}$ | "Particle number" of Core excitation |
| II → III | Vortex winding number | $n_{\text{wind}} = \pm 1$ | Spin magnitude |
| III → IV | Chirality | $\chi = \pm 1$ | Spin projection |
| IV → V | Hopf invariant | $H \in \mathbb{Z}$ | Particle identity (baryon/lepton number) |
| V → VI | Composite winding | $n_{\text{comp}} \geq 2$ | Composite number / generation |

Each conserved quantity is a **Noether charge** associated with a symmetry broken or established at the corresponding membrane crossing. The membrane crossing breaks the symmetry of the "lower" region and establishes the symmetry of the "higher" region — the new conserved charge is the Noether charge of the higher-region symmetry.

---

## Region I: The Propagation Current $J_x$

The A-state → Region I transition establishes the **propagation current** $J_x$ — the Noether current of the U(1) phase symmetry in the Forward zone:

$$
J_x = D_f\Phi_{B,f}^2 k_f = \text{const}
$$

(the product of the diffusion coefficient, B-state amplitude squared, and phase wavenumber — the field-theoretic momentum density in the +X direction). $J_x$ is conserved because the Forward zone B-state respects the translation symmetry in the +X direction: $\Phi_{\text{fwd}}(x,t) \to \Phi_{\text{fwd}}(x + a, t)$ is a symmetry of the Forward zone Lagrangian for constant $a$. The Noether charge of this symmetry is $J_x$.

$J_x$ is the ICHTB analog of **momentum**. In the survival map, the $J_x$ value labels horizontal lines in the Region I portion of the diagram — configurations with the same $J_x$ are at the same wavenumber $k_f$ (same "energy" for a massless mode).

---

## I→II Transition: Core Amplitude $N_{\text{core}}$

The I→II transition (Core activation) establishes the **Core occupation number** $N_{\text{core}}$ — the Noether charge associated with the U(1) phase symmetry of the Core zone field:

$$
N_{\text{core}} = \frac{1}{\mathcal{V}_{\text{core}}}\int_{\mathcal{V}_{\text{core}}}|\Phi_{\text{core}}|^2\,d^3r
$$

(the spatially averaged squared amplitude in the Core zone, normalized to the zone volume). Once the Core activates (I→II crossing), $N_{\text{core}} > \epsilon_c^2\Phi_{B,c}^2$ — the Core occupation number is above its threshold and conserved against small perturbations (stable against thermal deactivation above the I→II irreversibility threshold).

$N_{\text{core}}$ is the ICHTB analog of **"particle number"** in the Core zone — it measures how much B-state field is present in the Core, and it is approximately conserved once the Core is locked. The approximate conservation reflects the fact that the Core is not perfectly isolated (it exchanges energy with adjacent zones via the membranes), but for amplitudes well above the I→II threshold, the Core amplitude varies only slowly.

**Noether symmetry:** The U(1) phase symmetry $\Phi_{\text{core}} \to e^{i\phi}\Phi_{\text{core}}$ (global phase rotation of the Core field). This symmetry is broken at the Core-Forward membrane (which couples the Core phase to the Forward phase gradient), but the approximately conserved $N_{\text{core}}$ is the residual Noether charge.

---

## II→III Transition: Vortex Winding Number $n_{\text{wind}}$

The II→III transition (Memory vortex nucleation) establishes the **vortex winding number** $n_{\text{wind}} \in \mathbb{Z}$ as an exactly conserved topological charge:

$$
n_{\text{wind}} = \frac{1}{2\pi}\oint_C\nabla\arg\Phi_{\text{mem}}\cdot d\mathbf{l} \in \mathbb{Z}
$$

(integer-valued, exact). This is the Memory zone's topological charge — the winding number of the phase around the vortex core. It is **exactly conserved** (not merely approximately): it cannot change without a topological defect creation/annihilation event (vortex-antivortex pair creation, section 19.3).

$n_{\text{wind}}$ is conserved by **topological protection** — it is invariant under all continuous deformations of the field that do not cross the vortex core. The symmetry associated with $n_{\text{wind}}$ conservation is the **homotopy group** $\pi_1(U(1)) = \mathbb{Z}$ — the topological invariant of the Memory zone field, which maps the closed path $C$ to $\mathbb{Z}$ via the winding number.

$n_{\text{wind}}$ is the ICHTB analog of **spin magnitude** (or rather, the magnitude of the angular momentum projection). For the fundamental excitation: $|n_{\text{wind}}| = 1$ (spin-1/2 in the correspondence of section 16.4, where $m_s = \chi/2 = n_{\text{wind}}/2$).

**Physical significance:** The emergence of $n_{\text{wind}}$ as a conserved charge at the II→III crossing explains why spin is a conserved quantum number: it is the topological charge of the Memory zone vortex, protected by the homotopy group of the Memory zone U(1) field.

---

## III→IV Transition: Chirality $\chi$

The III→IV transition (junction vortex formation) establishes **chirality** $\chi = \pm 1$ as a conserved charge:

$$
\chi = \text{sgn}(n_{\text{wind}}) = \begin{cases} +1 & \text{(CCW vortex)} \\ -1 & \text{(CW vortex)} \end{cases}
$$

Wait — chirality $\chi = \text{sgn}(n_{\text{wind}})$ is already determined by $n_{\text{wind}}$ at the II→III crossing. Why is it a "new" conserved quantity at III→IV?

The answer is subtle: at the II→III crossing, $n_{\text{wind}}$ is conserved but **locally** — only in the Memory zone. The chirality is not yet globally conserved because it is not yet coupled to the other zones. An equivalent but opposite-chirality excitation could form independently in an adjacent zone without violating the Memory zone conservation law. The chirality is a **local** conserved charge of the Memory zone.

At the III→IV crossing (junction vortex formation), the chirality becomes **globally** conserved — the junction vortex couples the Memory zone chirality to the Core, and through the Core to all other zones. A chirality-flip event would now require changing the junction vortex sign, which requires energy $E_{\text{junc}} \gg T_{\text{eff}}$ (above the irreversibility threshold). The chirality transitions from local conservation to global conservation at the III→IV crossing.

**Noether symmetry:** The $\mathbb{Z}_2$ symmetry of parity ($\mathbf{r} \to -\mathbf{r}$) is explicitly broken by the junction vortex — the junction vortex has a definite chirality and is not parity-symmetric. The chirality $\chi$ is the **parity charge** — the Noether charge of the $\mathbb{Z}_2$ parity symmetry that is broken by the junction vortex.

---

## IV→V Transition: Hopf Invariant $H$

The IV→V transition (Apex lock) establishes the **Hopf invariant** $H \in \mathbb{Z}$ as a conserved topological charge:

$$
H = \frac{1}{(2\pi)^2}\int_{\text{ICHTB}}\mathbf{A}\cdot\mathbf{B}\,d^3r \in \mathbb{Z}
$$

(quantized to an integer only when $T_{\text{obj}} = 1$, section 16.2). Before the Apex lock: $H$ is continuous and non-quantized (a partial Hopf charge). After the Apex lock: $H$ is quantized and exactly conserved.

$H$ is the most fundamental conserved charge of the ICHTB — it is the charge that distinguishes particles from vacuum, and $H = +1$ from $H = -1$ (particle from antiparticle). It is conserved by the full 3D topological protection of the Hopf fibration.

**Noether symmetry:** The Hopf invariant is the Noether charge of the **global U(1)$\times$U(1)$\times$U(1) symmetry** of the three-component Hopf map $\Phi: S^3 \to S^2$ — the three-toroidal symmetry of the Hopf fiber bundle. The Apex lock establishes this symmetry as a global property of the ICHTB, quantizing $H$.

**Physical identification:** $H$ is the ICHTB analog of **baryon number** (for $H = 1, 3, \ldots$) or **lepton number** (for $H = 1$ in the lepton sector). The conservation of $H$ is the ICHTB explanation for the conservation of baryon number and lepton number in the Standard Model — they are Hopf invariants, topologically protected by the zone geometry.

---

## V→VI Transition: Composite Winding $n_{\text{comp}}$

The V→VI transition (second vortex nucleation) establishes the **composite winding number** $n_{\text{comp}} \in \mathbb{Z}_{\geq 2}$ as a conserved charge:

$$
n_{\text{comp}} = \sum_{i} n_{\text{wind}}^{(i)}
$$

(the total winding number summed over all Memory zone vortices). For a two-vortex composite: $n_{\text{comp}} = 2$ (if both have the same chirality) or $n_{\text{comp}} = 0$ (if opposite chiralities — a dimer with zero net winding but nonzero braiding).

The composite winding is conserved by the same topological protection as $n_{\text{wind}}$, but now applied to the multi-vortex configuration. For a dimer ($n_{\text{comp}} = 0$): the conserved charge is not the winding number but the **orbital angular momentum** of the dimer (the angular momentum of the relative motion of the two vortices around each other).

**Physical identification:** $n_{\text{comp}}$ is the ICHTB analog of **generation number** or **compositeness** — it distinguishes the fundamental excitations (Region V, $n_{\text{comp}} = 1$) from their composites (Region VI, $n_{\text{comp}} \geq 2$). The three generations of the Standard Model (electron, muon, tau) may correspond to $n_{\text{comp}} = 1, 2, 3$ in the ICHTB classification — the three stable multi-vortex configurations of increasing winding.

---

## The Complete Conservation Hierarchy

The full set of conserved charges, organized by the crossing that generates them:

$$
\underbrace{J_x}_{\text{Region I}} \xrightarrow{\text{I→II}} \underbrace{N_{\text{core}}}_{\text{Region II}} \xrightarrow{\text{II→III}} \underbrace{n_{\text{wind}}}_{\text{Region III}} \xrightarrow{\text{III→IV}} \underbrace{\chi}_{\text{Region IV}} \xrightarrow{\text{IV→V}} \underbrace{H}_{\text{Region V}} \xrightarrow{\text{V→VI}} \underbrace{n_{\text{comp}}}_{\text{Region VI}}
$$

Each arrow is a membrane crossing; each new symbol is a conserved charge generated by that crossing. The charges are **nested** — each higher region's charges include all the lower-region charges plus the new one. A Region V particle has $J_x$, $N_{\text{core}}$, $n_{\text{wind}}$, $\chi$, and $H$ all simultaneously conserved. A Region VI composite has all six charges conserved simultaneously.

This nested conservation hierarchy is the ICHTB version of the **symmetry breaking sequence** of the Standard Model — each membrane crossing is a symmetry-breaking event that generates a new conserved charge, analogous to the Higgs mechanism generating mass, or the QCD color charge being confined within hadrons. The full set of Standard Model quantum numbers (baryon number, lepton number, spin, helicity, generation) emerges from the five membrane crossings of the ICHTB survival map.

**Part IV conclusion:** Chapter 19 closes Part IV by identifying the transition rules between the six survival regions as membrane crossing events, deriving the mathematics of each transition, establishing the irreversibility conditions for each crossing, and showing that each crossing generates exactly one new conserved charge. The survival map (Chapters 17–19) is now complete: a six-region phase diagram with a universal survival hyperbola $\Lambda_{\text{lock}} \cdot S^* = 1$, five sequential membrane transitions, and a nested hierarchy of six conserved charges. Part V uses this framework to identify the specific zone configurations corresponding to the known particles of the Standard Model.

