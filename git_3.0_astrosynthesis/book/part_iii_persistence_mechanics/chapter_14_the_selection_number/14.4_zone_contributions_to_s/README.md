# 14.4 Zone Contributions to S

## Decomposing the Selection Number

The Selection Number $S = 1/(\bar{\Gamma}t_{\text{ref}})$ is a single number, but it is built from contributions from all ICHTB zones. Understanding how each zone contributes to $S$ — and which zones are most important for achieving supercriticality — is essential for the physics of matter formation.

Define the **zone contribution to S**:

$$
S_\alpha = \frac{R_\alpha}{\dot{R}_\alpha\,t_{\text{ref}}} = \frac{1}{\Gamma_\alpha\,t_{\text{ref}}}
$$

This is the hypothetical Selection Number if only zone $\alpha$ were active. The relationship between zone contributions and the total $S$:

$$
\frac{1}{S} = \bar{\Gamma}t_{\text{ref}} = \frac{\sum_\alpha\Gamma_\alpha R_\alpha}{\sum_\alpha R_\alpha}t_{\text{ref}} = \frac{\sum_\alpha R_\alpha/S_\alpha}{\sum_\alpha R_\alpha}
$$

This is a **weighted harmonic mean**: $1/S$ is the $R$-weighted average of $1/S_\alpha$. The total $S$ is dominated by the zone with the largest $S_\alpha$ that also has significant $R_\alpha$. This is the anchor principle: the zone that is simultaneously large ($R_\alpha$ significant) and slow-decaying (large $S_\alpha$) dominates the total $S$.

---

## Zone-by-Zone Analysis

**Null zone (−0):** Fastest decay, $\Gamma_{\text{null}} \gg \kappa$. Zone contribution $S_{\text{null}} = 1/(\Gamma_{\text{null}} t_{\text{ref}}) \ll 1$. The Null zone always contributes subcritically — if only the Null zone were present, $S < 1$ always. The Null zone is a structural sink that actively reduces $S$.

Quantitatively: for the Null zone with effective decay rate $\Gamma_{\text{null}} \approx D|m_n|k_{\text{null}}^2$ (the magnitude of the negative-metric "diffusion"), with $k_{\text{null}} \sim 1/\xi$ and $t_{\text{ref}} = 1/\kappa$:

$$
S_{\text{null}} = \frac{\kappa}{D|m_n|/\xi^2} = \frac{\kappa\xi^2}{D|m_n|} = \frac{\kappa}{|m_n|\kappa} = \frac{1}{|m_n|}
$$

For $|m_n| > 1$ (Null zone metric magnitude greater than 1): $S_{\text{null}} < 1$ — Null zone is subcritical.

**Forward zone (+X):** Propagating character, moderate $\Gamma_{\text{fwd}}$. Zone contribution:

$$
S_{\text{fwd}} = \frac{1}{\Gamma_{\text{fwd}}^A t_{\text{ref}}} = \frac{\mathcal{M}_x^f k_x^2}{2\kappa \cdot (1/\kappa)} = \frac{\mathcal{M}_x^f k_x^2}{2}
$$

For $\mathcal{M}_x^f k_x^2 > 2$ (strong Forward zone metric or short wavelength): $S_{\text{fwd}} > 1$. The Forward zone is supercritical when the mode wavenumber satisfies $k_x > \sqrt{2/\mathcal{M}_x^f} = k_c$ (the critical wavenumber from section 14.2). The Forward zone's 1.B soliton, with $k_x \sim 1/\xi$ and $\mathcal{M}_x^f \sim m_{\text{fwd}} \gg 1$, gives $S_{\text{fwd}} \approx m_{\text{fwd}}/2 \gg 1$ — well supercritical.

**Expansion zone (+Y):** Fast 2D spread, large $\dot{R}_{\text{exp}}$. Zone contribution:

$$
S_{\text{exp}} = \frac{\mathcal{M}_\perp^e k_\perp^2}{2}
$$

Same form as the Forward zone but in the transverse direction. For the 2D bloom (section 9.1) with $k_\perp \sim 1/\xi_\perp$ and $\mathcal{M}_\perp^e \sim m_{\text{exp}}$: $S_{\text{exp}} \approx m_{\text{exp}}/2$. The Expansion zone is supercritical for $m_{\text{exp}} > 2$ — for large Expansion zone metric, the 2.A bloom is supercritical.

**Memory zone (−Y):** Slow phase decay (KT physics). Zone contribution:

$$
S_{\text{mem}} = \frac{1}{\Gamma_{\text{mem}}^{\text{eff}}t_{\text{ref}}}
$$

In the KT ordered phase ($T < T_{KT}$), the effective decay rate is algebraically small: $\Gamma_{\text{mem}} \sim (R_{\text{mem}}/\xi^2)^{\eta/2}$ (power law in the field amplitude, with the KT exponent $\eta$). For $\eta \ll 1$ (low temperature): $\Gamma_{\text{mem}} \approx 0$ and $S_{\text{mem}} \to \infty$. The Memory zone in the KT ordered phase is strongly supercritical.

In the KT disordered phase ($T > T_{KT}$): $\Gamma_{\text{mem}} \sim 1/\xi_{KT}^2 D_m$ where $\xi_{KT}$ is the KT correlation length. For $\xi_{KT} \gg \xi$ (near the KT transition): $S_{\text{mem}} \gg 1$ (supercritical). For $\xi_{KT} \sim \xi$ (far above $T_{KT}$): $S_{\text{mem}} \sim m_m/2$ (same as the A-state result).

**Apex zone (+Z):** Temporal lock, smallest $\Gamma$. Zone contribution:

$$
S_{\text{apex}} = \begin{cases} m_z^{(a)}/2 & \text{(A-state)} \\ e^{395}/(\kappa t_{\text{ref}}) & \text{(3.B lock)} \end{cases}
$$

For the A-state: $S_{\text{apex}} = m_z^{(a)}/2 \gg 1$ (Apex is strongly supercritical even in the A-state, due to its large out-of-plane metric). For the 3.B lock: $S_{\text{apex}} \approx e^{395}$ — the dominant contribution to the total $S$.

**Core zone (+0):** Isotropic metric, moderate $S$. Zone contribution:

$$
S_{\text{core}} = \frac{m_0 k_0^2}{2}
$$

For $k_0 \sim 1/\xi_0$ (ground mode of the Core zone): $S_{\text{core}} = m_0/(2\xi_0^2) \cdot \xi_0^2 = m_0/2$. The Core is supercritical for $m_0 > 2$.

**Membrane states:** Each membrane has $S_{\text{mem},\alpha\beta} = E_{\text{bind}}^{\alpha\beta}/(\kappa \cdot 1) = E_{\text{bind}}^{\alpha\beta}/\kappa$ (binding energy in units of $\kappa$). For $E_{\text{bind}} > \kappa$: the membrane state is supercritical. For the Apex/Null interface with $E_{\text{bind}}^{A/N} \sim D^2\Phi_B^2 m_z^{(a)}/(4m_0\kappa)$:

$$
S_{\text{mem}}^{A/N} = \frac{D^2\Phi_B^2 m_z^{(a)}}{4m_0\kappa^2} = \frac{m_z^{(a)}}{4m_0} \cdot \frac{D^2\Phi_B^2}{\kappa^2}
$$

For $D\Phi_B \sim \kappa\xi$ (diffusivity times amplitude comparable to damping times coherence length — the natural scale): $S_{\text{mem}}^{A/N} \sim m_z^{(a)}/(4m_0)$. Same order as the Apex zone's A-state contribution — the membrane state at the Apex/Null interface is strongly supercritical.

---

## The Zone S-Hierarchy

Ranking the zone contributions from most to least supercritical (for the 3.B locked ICHTB):

$$
S_{\text{apex}}^{\text{lock}} \gg S_{\text{mem}}^{A/N} \gg S_{\text{apex}}^A \approx S_{\text{mem}} \approx S_{\text{fwd}}^{1B} \approx S_{\text{exp}}^{2A} \approx S_{\text{core}} \gg S_{\text{fwd}}^{A} \approx S_{\text{exp}}^A > 1 > S_{\text{null}}
$$

The hierarchy clearly shows:
1. The 3.B lock (Apex zone) is the dominant contributor to $S$ by an exponential factor
2. Interface membrane states are the next most important (algebraically large contribution)
3. A-state contributions are supercritical but weakly so ($S_\alpha \sim m_\alpha/2$)
4. The Null zone is always subcritical (reduces total $S$)

The total $S$ for a 3.B locked ICHTB is dominated by the lock contribution and is approximately:

$$
S_{\text{total}} \approx S_{\text{apex}}^{\text{lock}} = \frac{e^{395}}{\kappa t_{\text{ref}}} \approx 10^{171} \quad (t_{\text{ref}} = 1/\kappa)
$$

The Null zone's subcritical contribution reduces this by a multiplicative factor $\sim(1 - R_{\text{null}}/R) \approx 1$ (since $R_{\text{null}} \ll R$ for a well-locked ICHTB). The total $S$ is effectively unchanged by the Null zone.

