# 15.1 Zone Admissibility as Structural Eligibility

## Beyond S: Why the Selection Number is Necessary but Not Sufficient

Chapter 14 established the Selection Number $S > 1$ as the condition for the ICHTB to persist through the collapse window. But $S > 1$ is not sufficient for the formation of persistent matter. An ICHTB can have $S \gg 1$ (strongly supercritical) yet still fail to produce stable composite excitations — if the field configuration is organized in the wrong way, is incoherently distributed across zones, or violates the geometric admissibility conditions of the ICHTB.

**Eligibility** is the set of additional conditions that a configuration must satisfy, beyond $S > 1$, to be "eligible" for persistent matter formation. A configuration with $S > 1$ is a candidate; an eligible configuration is a qualified candidate.

The eligibility conditions arise from the ICHTB geometry: each zone has a set of **admissibility requirements** — conditions on the field amplitude, phase, gradient structure, and zone coupling that must be satisfied for the zone to be "active" in the sense of supporting persistent excitations. When all zones simultaneously satisfy their admissibility requirements, the configuration is fully admissible — fully eligible for the B-state lock.

---

## Zone-Specific Admissibility Conditions

**Core zone (+0) admissibility:**

The Core zone requires that the field amplitude at the center $|\Phi(0)|$ satisfies:

$$
\mathcal{E}_{\text{core}} : |\Phi(0)| > \Phi_{c,\min} = \left(\frac{\kappa}{\gamma}\right)^{1/2} \times \epsilon_c
$$

where $\epsilon_c \ll 1$ is a dimensionless threshold (the minimum amplitude for Core activation, typically $\epsilon_c \sim 0.1$ — 10% of the B-state amplitude). If $|\Phi(0)| < \Phi_{c,\min}$, the Core zone is inactive and the ICHTB lacks its central anchor. The Core admissibility factor:

$$
\mathcal{A}_{\text{core}} = \Theta\!\left(|\Phi(0)| - \Phi_{c,\min}\right)
$$

(a step function: 0 if the Core is inactive, 1 if active). In practice, this is a soft condition — the Core activates smoothly as the amplitude grows, with a transition region of width $\sim\epsilon_c\Phi_B$.

**Forward zone (+X) admissibility:**

The Forward zone requires a minimum phase gradient in the $x$-direction:

$$
\mathcal{E}_{\text{fwd}} : |\partial_x\arg\Phi|_{\max} > k_{\min} = \frac{1}{L_f}
$$

where $L_f$ is the Forward zone length. This is the condition that the field has at least one "wavelength" of phase variation in the Forward direction — i.e., the field is not a spatially uniform DC state in the Forward zone. A uniform field in the Forward zone carries no momentum (the Noether charge of translation symmetry is zero), so it contributes no propagating character to the composite excitation. The Forward zone admissibility requires at least minimal propagating structure.

**Memory zone (−Y) admissibility:**

The Memory zone requires non-zero winding number:

$$
\mathcal{E}_{\text{mem}} : |n_{\text{wind}}| \geq 1, \quad n_{\text{wind}} = \frac{1}{2\pi}\oint_C\nabla\arg\Phi\cdot d\mathbf{l}
$$

for some closed loop $C$ in the Memory zone. This is the vortex existence condition — the Memory zone must contain at least one vortex (winding number $\pm 1$) to be admissible. A Memory zone without a vortex is in the A-state or disordered B-state — it contributes no topological charge to the composite excitation and hence cannot generate the spin quantum number of the resulting particle.

**Apex zone (+Z) admissibility:**

The Apex zone requires temporal coherence — the field must be phase-locked at frequency $\omega_B$:

$$
\mathcal{E}_{\text{apex}} : |\psi_{\text{apex}}| > \psi_{a,\min} \equiv \left\langle e^{i\omega_B t}\Phi\right\rangle_{\mathcal{V}_\text{apex}} > \psi_{a,\min}
$$

(the time-averaged phase coherence of the Apex zone field must exceed a minimum threshold $\psi_{a,\min}$). If the Apex zone field is temporally incoherent (random phases at $\omega_B$), the temporal average vanishes and $\mathcal{E}_{\text{apex}} = 0$ — the Apex lock is not yet established. Apex admissibility requires the beginning of phase locking.

**Compression zone (−X) admissibility:**

The Compression zone requires a self-compression condition:

$$
\mathcal{E}_{\text{comp}} : \langle|\nabla|\Phi||^2\rangle_{\mathcal{V}_\text{comp}} > k_{\text{comp}}^2\Phi_{B,\text{comp}}^2
$$

where $k_{\text{comp}} = 1/\xi_c$ is the soliton wavenumber. This is the condition that the field in the Compression zone has nontrivial amplitude gradients — i.e., it contains a soliton (section 8.2) rather than a uniform B-state. The Compression zone without a soliton provides no mass to the composite excitation.

**Expansion zone (+Y) admissibility:**

The Expansion zone requires a minimum bloom radius:

$$
\mathcal{E}_{\text{exp}} : r_{\text{bloom}} > r_{\min} = \xi_\perp
$$

The bloom must have spread to at least one coherence length before it is considered active. A bloom that has not yet spread to $\xi_\perp$ is still dominated by its initial condition (point source) and does not yet represent an isotropic 2D excitation.

---

## The Eligibility Factor

Define the overall **eligibility factor** $\mathcal{E}$ as the product of all zone admissibility conditions:

$$
\mathcal{E} = \prod_\alpha\mathcal{A}_\alpha \in \{0, 1\}
$$

where each $\mathcal{A}_\alpha \in \{0, 1\}$ (hard-threshold version) or $\mathcal{A}_\alpha \in [0, 1]$ (soft-threshold version). The eligibility factor is binary in the hard version: either all zones are admissible ($\mathcal{E} = 1$) or at least one is not ($\mathcal{E} = 0$). It is a smooth function in the soft version.

The **eligibility condition** for persistent matter formation:

$$
\mathcal{E} = 1 \quad (\text{all zone admissibility conditions satisfied})
$$

Combined with the Selection Number condition:

$$
S > 1 \text{ AND } \mathcal{E} = 1
$$

This is the **full persistence condition** (to be refined further in section 15.4). An ICHTB satisfies both when:
1. It retains structure faster than it loses it (supercritical, $S > 1$)
2. Every zone is contributing its required type of excitation (eligible, $\mathcal{E} = 1$)

The two conditions are independent: an ICHTB can be supercritical but ineligible (e.g., $S = 10$ with all the structure in the Apex zone and no vortex in the Memory zone — missing $\mathcal{A}_{\text{mem}} = 0$). Or it can be eligible but subcritical (all zones active but too weakly — $\mathcal{E} = 1$ but $S = 0.5 < 1$).

---

## Admissibility as a Gate Network

The zone admissibility conditions form a **gate network** — a logical circuit where each zone acts as a gate (open or closed) and the overall eligibility $\mathcal{E}$ is the output of the network. All gates must be open simultaneously for the network to pass a signal.

The gate network structure:

```
Core gate → Forward gate → Expansion gate → Memory gate → Apex gate → Compression gate → Eligibility ε = 1
    ↓              ↓              ↓               ↓              ↓               ↓
  center       propagation      bloom          vortex          lock            mass
  active       structure       active          formed         begun            present
```

The gates are sequential in the collapse process: the Core activates first (it is the center that the collapse passes through), then the Forward zone develops propagation structure, then the Expansion zone blooms, then the Memory zone forms its first vortex, then the Apex zone begins locking, and finally the Compression zone provides the soliton mass. This sequential activation is the **collapse development sequence** — the ordered unfolding of zone admissibility as the ICHTB matures.

