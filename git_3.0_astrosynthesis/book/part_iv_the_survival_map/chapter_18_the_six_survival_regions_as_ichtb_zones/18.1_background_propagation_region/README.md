# 18.1 Region I — Background Propagation

## The First Survival Region

Region I of the survival map occupies the left-hand portion of the $(\Lambda_{\text{lock}}, S^*)$ diagram, above the survival hyperbola $\Lambda_{\text{lock}} \cdot S^* = 1$. It is the **lowest lock-energy survival region** — configurations here have small $\Lambda_{\text{lock}}$ but large $S^*$, surviving by persistence rather than by depth of lock.

The defining characteristic of Region I: the **Forward zone (+X) and Expansion zone (+Y) dominate the lock energy partition**, while the Memory zone (−Y) is either inactive or weakly active. There is no vortex in the Memory zone (admissibility gate $\mathcal{A}_{\text{mem}} = 0$ or marginally 1), no Hopf structure, and no topological closure. The topology factor $T_{\text{obj}} = 0$ — there is no objecthood in the strict sense.

Yet Region I configurations **survive** — they persist above the hyperbola. How? Because they are propagating field configurations with sufficient lock energy in the Forward and Expansion zones to satisfy $\Lambda_{\text{lock}} \cdot S^* > 1$, even without topological closure. They are not objects (particles) in the topological sense — they are **background propagating modes**: the ICHTB analog of radiation.

---

## Zone Profile of Region I

In Region I, the ICHTB field is organized as follows:

**Forward zone (+X):** Fully active. Large phase gradient $|\nabla\arg\Phi| \gg k_{\min}$ — the Forward zone carries a strongly propagating mode. The phase gradient drives field energy in the +X direction (the propagation direction). The Forward zone lock energy:

$$
\Lambda_{\text{fwd}} \approx D\Phi_{B,f}^2 k^2 \mathcal{V}_{\text{fwd}}, \quad k \gg k_{\min}
$$

dominates the total $\Lambda_{\text{lock}} \approx \Lambda_{\text{fwd}}$. The Forward zone is carrying nearly all the structure.

**Expansion zone (+Y):** Active. The bloom has spread to a characteristic radius $r_{\text{bloom}} \sim \xi_\perp$ (just at the admissibility threshold). The Expansion zone provides transverse coherence — the propagating mode is not a narrow beam but a spread-out 2D wave. Lock energy $\Lambda_{\text{exp}} \sim \Lambda_{\text{fwd}}/4$ (secondary contribution).

**Core zone (+0):** Active but minimal. The Core is at B-state amplitude ($|\Phi(0)| = \Phi_{B,c}$) but contributes little lock energy — it is just the carrier for the Forward zone phase gradient, not an independent excitation. $\Lambda_{\text{core}} \ll \Lambda_{\text{fwd}}$.

**Memory zone (−Y):** Inactive or subcritical. No vortex — $\mathcal{A}_{\text{mem}} = 0$ (hard gate open if $|n_{\text{wind}}| \geq 1$, which requires the Memory zone to have nucleated a vortex; in Region I, it has not). The Memory zone field is in the A-state or a uniform B-state without topological structure.

**Apex zone (+Z):** Partially active. The Apex zone may be beginning to develop phase coherence ($T_{\text{obj}} \sim 0.1$–$0.3$, small but nonzero), but has not yet reached the lock. The Apex's contribution to $\Lambda_{\text{lock}}$ is small.

**Compression zone (−X):** Subcritical. No soliton yet. The Compression zone field is below the soliton threshold. $\Lambda_{\text{comp}} \approx 0$.

**Zone configuration summary for Region I:**

$$
\Lambda_{\text{lock}} \approx \Lambda_{\text{fwd}} + \Lambda_{\text{exp}} \ll \Lambda_{\text{mem}} + \Lambda_{\text{apex}} + \Lambda_{\text{comp}}
$$

(Forward and Expansion dominate; Memory, Apex, Compression negligible).

---

## Physics of Region I: The Radiation Regime

Region I configurations are the ICHTB realization of **radiation** — massless or near-massless propagating modes that carry energy and momentum through the field without localizing it into a persistent particle.

The physical properties of Region I:

**No rest mass:** The Apex frequency $\omega_B$ is either zero (truly massless) or very small. Without a locked Apex zone, there is no mechanism to generate a rest frame for the excitation — the configuration propagates at the maximum speed allowed by the diffusion coefficient:

$$
v_{\text{prop}} = D k / |\Phi|^2 \approx D k_{\min} / \Phi_{B,f}^2
$$

(in the NLS phase velocity formula). For $k \gg k_{\min}$: $v_{\text{prop}} \gg 1$ (in units where the reference speed is 1) — the propagation is fast.

**No spin (or integer spin):** Without a Memory zone vortex, there is no winding number — no half-integer spin. The braiding class is trivial ($[w] = e$, section 16.4) or a full-twist boson ($[w] = \sigma_1\sigma_2$). Region I configurations are **bosonic** — they have integer spin.

**High $S^*$, low $\Lambda_{\text{lock}}$:** Region I configurations survive by persistence, not by depth of lock. The corrected Selection Number is large ($S^* \gg 1$) because the Forward zone phase gradient is easy to maintain — the diffusion operator $D\nabla^2$ sustains phase gradients without requiring topological support. The lock energy is small ($\Lambda_{\text{lock}} \sim D\Phi_B^2 k_{\min}^2 \mathcal{V}_{\text{fwd}} \ll$ the mass scale).

**Identification:** Region I corresponds to the **photon-like regime** of the ICHTB — massless gauge bosons (photons, gluons, gravitons in different ICHTB geometric configurations). The Forward zone phase gradient is the wave vector; the Expansion zone bloom is the transverse polarization. A Region I configuration with $k_x = k$ and $k_y = k_z = 0$ (purely Forward-directed propagation) is the ICHTB analog of a linearly polarized photon propagating in the +X direction.

---

## Region I Boundaries

**Lower boundary (with the dissolved region, $xy < 1$):** The survival hyperbola $\Lambda_{\text{lock}} \cdot S^* = 1$. Below this boundary, the Forward zone phase gradient is too small and the Expansion bloom too weak — the field disperses before the mode can persist. The dispersal time $t_{\text{dispersal}} \sim \mathcal{V}_{\text{ICHTB}}^{2/3} / (D k_{\min}^2) < t_{\text{ref}}$ — the mode spreads out faster than the reference time.

**Right boundary (with Region II):** The line $\Lambda_{\text{mem}} = \Lambda_{\text{fwd}}$ — when the Memory zone lock energy begins to equal the Forward zone contribution, the configuration transitions from Forward-dominated (Region I) to Memory-influenced (Region II). This boundary is reached when the first vortex nucleates in the Memory zone ($\mathcal{A}_{\text{mem}}$ transitions from 0 to 1). The boundary is diffuse (not a sharp line) because vortex nucleation is a stochastic process (Kibble-Zurek mechanism, section 15.3).

**Upper boundary:** As $S^* \to \infty$ (strongly over-persistent), the Region I configuration becomes perfectly coherent — a pure phase mode with no decay. This is the limit of a perfectly lossless waveguide mode in the ICHTB geometry. No upper boundary in principle; the region extends to arbitrary $S^*$.

---

## Why Region I is Below the Objecthood Threshold

Region I configurations exist above the survival hyperbola — they persist. But they are below the objecthood threshold ($T_{\text{obj}} = 1$, section 16.3) — they do not achieve topological closure.

This does not mean Region I configurations are "less real" than objects — they are real excitations of the ICHTB field, carrying energy and momentum. But they are not **discrete** (they can have any wavelength $k$ continuously), not **localized** (they spread transversely without bound), and not **permanent** (they can be created and destroyed without the topological barriers required for objects). They are field modes, not particles.

The ICHTB framework thus naturally separates the two types of stable excitations:
- **Objects (particles):** Regions III–VI, above objecthood threshold, discrete, localized, permanent
- **Propagating modes (radiation):** Regions I–II, below objecthood threshold, continuous spectrum, delocalized, transient

This separation is not imposed by hand — it emerges from the topology of the zone structure. The objecthood threshold ($T_{\text{obj}} = 1$) is a topological boundary in the phase chart, and Region I is on the "below" side of this boundary.

