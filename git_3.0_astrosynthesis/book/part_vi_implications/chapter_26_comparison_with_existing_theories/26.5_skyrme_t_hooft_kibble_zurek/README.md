# 26.5 Skyrme, 't Hooft, Kibble-Zurek — Topological Foundations

## Tony Skyrme and Topological Solitons

**Tony Skyrme** (1961, 1962) proposed that baryons (protons and neutrons) are **topological solitons** — stable, localized field configurations characterized by a conserved topological charge (the **baryon number** $B$) that cannot be changed by smooth field deformations. The **Skyrme model** (or **Skyrmion**) is a nonlinear sigma model for the pion field $U(\mathbf{x}) \in SU(2)$ (a unit quaternion field) with the Lagrangian:

$$
\mathcal{L}_{\text{Skyrme}} = \frac{f_\pi^2}{16}\text{Tr}(L_\mu L^\mu) + \frac{1}{32e^2}\text{Tr}([L_\mu, L_\nu]^2)
$$

where $L_\mu = U^\dagger\partial_\mu U$ (the left-invariant Maurer-Cartan form on $SU(2)$) and $f_\pi$, $e$ are constants. The topological charge (baryon number) is:

$$
B = \frac{1}{24\pi^2}\int d^3x \,\epsilon^{ijk}\text{Tr}(L_i L_j L_k) \in \mathbb{Z}
$$

(an integer winding number of the map $U: S^3_{\text{space}} \to SU(2) = S^3$ — the degree of the map from physical space to the group manifold, integrated over all space). A baryon ($B = 1$) is a Skyrmion — a localized field configuration with one unit of winding.

---

## ICHTB and the Skyrme Model: Deep Resonance

The Skyrme model and the ICHTB are the closest existing frameworks to each other among all the theories compared in this chapter. The resonances are deep:

| Skyrme model | ICHTB |
|---|---|
| Topological charge $B \in \mathbb{Z}$ (baryon number = winding number) | Memory zone winding number $n \in \mathbb{Z}$ |
| Skyrmion as stable soliton ($B \neq 0$ topologically protected) | Vortex as durable object ($n \neq 0$ topologically protected) |
| Field $U \in SU(2)$ (unit quaternion = 4-component complex field) | NLS field $\Psi \in \mathbb{C}$ (1-component complex field, but multi-zone structure) |
| Pion field (Goldstone boson of chiral symmetry breaking) | Forward/Expansion phonon (Goldstone boson of $U(1)$ symmetry breaking: $\Psi \to e^{i\theta}\Psi$) |
| Skyrme term ($[L_\mu, L_\nu]^2$) stabilizes soliton against collapse | Zone membrane activation threshold stabilizes vortex against Core dissolution |
| $B=1$ Skyrmion: hedgehog configuration (point symmetry group) | $n=1$ ICHTB vortex: cylindrical symmetry (Memory zone + Apex zone angular structure) |
| Multi-baryon ($B > 1$) Skyrmions | $n > 1$ ICHTB vortex clusters (Region VI braids: three $n=1$ charges in $\Delta^2 \in B_3$) |
| Rational map approximation for $B > 1$: angular dependence factored | Apex zone angular structure: $Y_l^m(\hat{r})$ spherical harmonics for multi-charge composites |

The **critical difference:** the Skyrme model uses $SU(2)$-valued fields (four real degrees of freedom) while the ICHTB uses $U(1)$-valued fields (two real degrees of freedom). The Skyrme model's richness comes from the $SU(2) \cong S^3$ topology; the ICHTB's richness comes from the **zone architecture** (the six-zone structure that the single complex field $\Psi$ organizes into).

In the Skyrme model: the baryon is topologically protected by the $\pi_3(SU(2)) = \mathbb{Z}$ homotopy group (the third homotopy group of the group manifold $S^3$). In the ICHTB: the vortex is topologically protected by $\pi_1(S^1) = \mathbb{Z}$ (the first homotopy group of the $U(1)$ phase circle) — a winding in 2D rather than 3D.

The ICHTB is, in a sense, a **dimensional reduction** of the Skyrme model — it achieves equivalent baryon stability with a simpler field ($U(1)$ vs $SU(2)$) by adding the zone architecture as a structural supplement. The zone structure compensates for the lower-dimensional topology by providing multiple distinct stability mechanisms (Core lock, Memory chirality, Apex angular momentum) that together give the vortex the same robustness as a Skyrmion.

---

## Gerard 't Hooft: Topology in Field Theory

**Gerard 't Hooft** has contributed foundational insights into the role of topology in gauge field theories, relevant to the ICHTB at several points:

**1. Magnetic monopoles (1974):** 't Hooft showed that any Grand Unified Theory (GUT) predicts magnetic monopoles as topological solitons — stable field configurations with $\pi_2(G/H) \neq 0$ (non-trivial second homotopy group of the broken symmetry). In ICHTB terms: monopoles would correspond to $n=1$ configurations in a theory with $\pi_2$ topology — a higher-dimensional analog of the ICHTB $\pi_1$ vortex. The ICHTB does not produce monopoles (its topology is $\pi_1 = \mathbb{Z}$, not $\pi_2$), but 't Hooft's monopole analysis is the 3D analog of the ICHTB's 2D vortex stability.

**2. Instantons (1976):** 't Hooft computed the instanton contributions to Yang-Mills field theories — the topological tunneling events that allow $\theta$-vacuum transitions and generate the strong CP problem. In ICHTB terms: instantons are **Core zone topological transitions** — events where the Core zone amplitude passes through zero (the topological singularity) and the winding number $n$ changes. The ICHTB vortex-antivortex annihilation event (section 26.3: recursive failure topological transition $n \to 0$) is the NLS analog of a 't Hooft instanton.

**3. Large-$N$ expansion (1974):** 't Hooft's planar diagram expansion of $SU(N)$ gauge theories in the large-$N$ limit provides a systematic expansion in $1/N$ (the inverse number of colors). This connects to the ICHTB multi-charge braids: the Region VI braid $\Delta^2 \in B_3$ uses three charges (three "colors"), and the $1/N$ expansion organizes the braid contributions by number of charge strands. The ICHTB's color number ($N_c = 3$) is fixed, but 't Hooft's large-$N$ technique provides a systematic way to compute the multi-charge zone interactions.

**4. 't Hooft anomaly matching (1980):** 't Hooft's anomaly matching conditions require that global anomalies (inconsistencies in the quantization of chiral symmetries) match between the UV (high-energy, short-distance) and IR (low-energy, long-distance) descriptions of a field theory. In ICHTB: anomaly matching = zone integrity constraint — the zone membrane activation thresholds must be consistent with each other across all zone scales (Core to Expansion). A violation of ICHTB zone integrity is the analog of a 't Hooft anomaly mismatch.

---

## Kibble-Zurek: Defect Formation and the Zone Density

**Tom Kibble** (1976) and **Wojciech Zurek** (1985) independently developed the **Kibble-Zurek mechanism** — the theory of topological defect formation during phase transitions. When a system is cooled through a symmetry-breaking phase transition, different regions of the system independently choose their order parameter direction. Where regions with incompatible choices meet, topological defects form (vortices in 2D, strings in 3D, monopoles in 3D for appropriate topologies).

The Kibble-Zurek mechanism predicts the **density of defects** formed during a quench (rapid cooling through $T_c$):

$$
n_{\text{defect}} \sim \xi_{\text{KZ}}^{-d}
$$

where $d$ is the dimension and $\xi_{\text{KZ}}$ is the **Kibble-Zurek length** — the characteristic correlation length at the time when the system falls out of equilibrium during the quench:

$$
\xi_{\text{KZ}} = \xi_0 \left(\frac{\tau_Q}{\tau_0}\right)^{\nu/(1+z\nu)}
$$

where $\xi_0$ is the zero-temperature correlation length, $\tau_Q$ is the quench rate, $\tau_0$ is the microscopic relaxation time, $\nu$ is the correlation length exponent, and $z$ is the dynamic critical exponent.

---

## Kibble-Zurek and the ICHTB Background

The ICHTB background field $\Phi_B$ was established (in the ICHTB's cosmological prehistory, section 13.1) by a phase transition — the NLS condensation of the background field from a disordered, high-temperature state. The Kibble-Zurek mechanism determines:

**1. The initial vortex density:** At the moment of condensation, vortices nucleated spontaneously wherever the background phase gradient was discontinuous (Kibble-Zurek defect formation). The initial vortex density:

$$
n_{\text{vortex,initial}} \sim \xi_{\text{KZ}}^{-3} = \xi_0^{-3}\left(\frac{\tau_Q}{\tau_0}\right)^{-3\nu/(1+z\nu)}
$$

determines the **number density** of durable objects in the ICHTB — the initial number of topological charges created during the cosmological condensation. Slow quench ($\tau_Q \to \infty$): $\xi_{\text{KZ}} \to \infty$, very few defects (adiabatic limit). Fast quench ($\tau_Q \to 0$): $\xi_{\text{KZ}} \to 0$, very many defects (impulse limit).

**2. The correlation length as zone size:** The Kibble-Zurek correlation length $\xi_{\text{KZ}}$ at the time of the phase transition sets the initial zone size — the healing length $\xi_c$ of the earliest vortices (the Core zone size). Subsequent evolution (cooling, expansion) modifies the zone sizes, but the initial Kibble-Zurek scale sets the order of magnitude.

**3. The coarsening dynamics:** After the phase transition, vortices and antivortices annihilate on a timescale $\tau_{\text{coarsen}} \sim n^{-1/2}/v_{\text{vortex}}$ (the time for nearby opposite-charge vortices to find each other and annihilate). The surviving vortices (those far enough from antivortices to survive the coarsening) become the stable durable objects of the ICHTB. The Kibble-Zurek mechanism followed by coarsening explains why the ICHTB has a finite, non-zero density of durable objects — enough to populate the particle spectrum, but not so many that all vortices immediately annihilate.

The Kibble-Zurek mechanism has been experimentally verified in superfluid helium (Hendry et al. 1994), liquid crystals (Chuang et al. 1991), superconductors (Monaco et al. 2002), Bose-Einstein condensates (Weiler et al. 2008), and ion traps (Zurek et al. 2005). The ICHTB's claim that the same mechanism generates the initial population of fundamental particles connects well-established condensed matter physics to fundamental particle physics.

