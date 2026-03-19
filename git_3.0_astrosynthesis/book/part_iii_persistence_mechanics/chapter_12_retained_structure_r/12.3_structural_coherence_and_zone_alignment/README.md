# 12.3 Structural Coherence and Zone Alignment

## Coherence as a Multi-Scale Concept

Section 12.2 introduced the coherence fraction $R_1/R$ as a measure of how concentrated the retained structure is into a dominant channel. This section develops the concept of **structural coherence** more fully — distinguishing three levels at which coherence can be measured in the ICHTB:

1. **Intra-zone coherence:** How coherent is the field within a single zone?
2. **Inter-zone coherence:** How well-aligned are the fields in adjacent zones?
3. **Global coherence:** How well-synchronized are all zones simultaneously?

These three levels are hierarchically related: global coherence requires inter-zone coherence, which requires intra-zone coherence. The progression from incoherent A-state to maximally coherent 3.B lock is a progression through all three levels.

---

## Intra-Zone Coherence: The Zone Order Parameter

Within a single zone $\alpha$, the coherence of the field is measured by the **zone order parameter**:

$$
\psi_\alpha = \frac{\langle\Phi\rangle_{\mathcal{V}_\alpha}}{\Phi_{B,\alpha}}
$$

where $\langle\Phi\rangle_{\mathcal{V}_\alpha} = \int_{\mathcal{V}_\alpha}\Phi\,d^3r/|\mathcal{V}_\alpha|$ is the spatial average of the field over the zone volume. This is a complex number with $|\psi_\alpha| \leq 1$:
- $|\psi_\alpha| \approx 0$: incoherent zone (A-state or vortex-gas — phases cancel on average)
- $|\psi_\alpha| \approx 1$: coherent zone (3.B lock — all phases aligned)
- $\arg\psi_\alpha$: the mean phase of the zone's field

The intra-zone coherence length $\xi_{\text{coh},\alpha}$ is defined by the two-point correlation function:

$$
C_\alpha(r) = \frac{\langle\Phi^*(\mathbf{r}_0)\Phi(\mathbf{r}_0 + \mathbf{r})\rangle_{\mathcal{V}_\alpha}}{\Phi_{B,\alpha}^2} \approx e^{-r/\xi_{\text{coh},\alpha}}
$$

For $\xi_{\text{coh},\alpha} \sim \xi_\alpha$ (one coherence length): the zone is minimally coherent (A-state, rapid decay). For $\xi_{\text{coh},\alpha} \gtrsim |\mathcal{V}_\alpha|^{1/3}$ (coherence extends across the whole zone): the zone is maximally coherent (B-state lock).

---

## Inter-Zone Coherence: Phase Alignment

Between two adjacent zones $\alpha$ and $\beta$, the inter-zone coherence is measured by the **phase alignment**:

$$
\mathcal{A}_{\alpha\beta} = \text{Re}\!\left(\psi_\alpha^*\psi_\beta\right) = |\psi_\alpha||\psi_\beta|\cos(\Delta\phi_{\alpha\beta})
$$

where $\Delta\phi_{\alpha\beta} = \arg\psi_\alpha - \arg\psi_\beta$ is the phase difference between zones $\alpha$ and $\beta$. The alignment $\mathcal{A}_{\alpha\beta} \in [-1, 1]$:
- $\mathcal{A}_{\alpha\beta} = 1$: zones are phase-aligned (same phase, maximum constructive interference at the interface)
- $\mathcal{A}_{\alpha\beta} = 0$: zones are phase-quadrature (90° apart — no net inter-zone current)
- $\mathcal{A}_{\alpha\beta} = -1$: zones are phase-antialigned (opposite phase, maximum destructive interference)

The **optimal alignment for maximum retained structure** is $\mathcal{A}_{\alpha\beta} = 1$ for same-sign zone pairs and $\mathcal{A}_{\alpha\beta} = -1$ for sign-changing zone pairs (Type B interfaces). This is because:
- At Type A interfaces (same-sign zones): phase-aligned fields add constructively across the membrane, maximizing the field amplitude and hence the contribution to $R$
- At Type B interfaces (sign-changing zones): phase-antialigned fields create a sign-reversal at the boundary, which is exactly the membrane state condition (section 11.1) — it maximizes the interface binding energy $E_{\text{bind}}$

The **zone alignment tensor** $\mathcal{A}^{\alpha\beta}$ collects all pairwise alignments. For the ICHTB with all zones active:

$$
\mathcal{A}^{\alpha\beta} = |\psi_\alpha||\psi_\beta|\cos(\Delta\phi_{\alpha\beta}) \quad \text{for each interface }\langle\alpha\beta\rangle
$$

The **alignment quality** is measured by the sum:

$$
Q_{\text{align}} = \sum_{\langle\alpha\beta\rangle^A}\mathcal{A}^{\alpha\beta} - \sum_{\langle\alpha\beta\rangle^B}\mathcal{A}^{\alpha\beta}
$$

(positive sum over Type A interfaces, negative sum over Type B interfaces — both contribute positively to $Q_{\text{align}}$ when optimally aligned). The maximum value $Q_{\text{align}} = N_A + N_B = 24$ (all 24 interfaces optimally aligned).

---

## Global Coherence: The ICHTB Synchronization

The global coherence of the ICHTB is measured by the **synchronization parameter** $\Psi$:

$$
\Psi = \frac{1}{N_z}\sum_\alpha\psi_\alpha e^{i\phi_{\text{ref}}}
$$

where $\phi_{\text{ref}}$ is the global reference phase (set by the Apex zone: $\phi_{\text{ref}} = \omega_B t$) and $N_z = 12$ is the number of zones. The magnitude $|\Psi| \in [0, 1]$:
- $|\Psi| \approx 0$: phases are randomly distributed (incoherent, vortex-gas phase)
- $|\Psi| \approx 1$: all zones phase-locked to the Apex reference (fully coherent 3.B lock)

This is the ICHTB version of the **Kuramoto order parameter** (Kuramoto 1984, *Chemical Oscillations, Waves, and Turbulence*) — the classic measure of synchronization in coupled oscillator systems. The ICHTB zones are the "oscillators" (each oscillating at roughly $\omega_B$ but with their own natural frequencies $\omega_\alpha$), and the Apex zone is the external forcing that drives synchronization.

The Kuramoto synchronization condition: for the ICHTB to achieve global coherence ($|\Psi| \to 1$), the inter-zone coupling strength (set by the membrane state binding energies $E_{\text{bind}}^{\alpha\beta}$) must exceed the natural frequency spread (set by the zone-specific $\omega_\alpha$ variations):

$$
\langle E_{\text{bind}}\rangle > \Delta\omega \equiv \max_{\alpha,\beta}|\omega_\alpha - \omega_\beta|
$$

This is the **synchronization threshold** — below it, zones oscillate independently (incoherent phase); above it, all zones lock to a common frequency (synchronized phase). The ICHTB 3.B lock is the synchronized phase: $|\Psi| = 1$, all zones phase-locked to $\omega_B$.

---

## Zone Alignment and Retained Structure: The Connection

The relationship between zone alignment $Q_{\text{align}}$ and retained structure $R$ is direct:

$$
R = R_0\left[1 + \eta\,Q_{\text{align}}/Q_{\text{max}}\right]
$$

where $R_0 = \sum_\alpha R_\alpha$ is the sum of individual zone contributions (assuming independent zones), $\eta$ is the **coupling efficiency** (ratio of interface-mediated retention to bulk retention), and $Q_{\text{max}} = N_A + N_B$ is the maximum alignment quality.

The coupling efficiency:

$$
\eta = \frac{R_{\text{membrane}}}{R_{\text{bulk}}} = \frac{\sum_{\langle\alpha\beta\rangle}E_{\text{bind}}^{\alpha\beta}|\mathcal{S}_{\alpha\beta}|}{\sum_\alpha R_\alpha}
$$

For a weakly coupled ICHTB ($\eta \ll 1$): $R \approx R_0$ — zone alignment has little effect. For a strongly coupled ICHTB ($\eta \gg 1$): $R \approx \eta R_0 Q_{\text{align}}/Q_{\text{max}}$ — zone alignment dominates the retained structure.

The **3.B lock** achieves maximum zone alignment ($Q_{\text{align}} = Q_{\text{max}}$) with maximum coupling efficiency ($\eta \gg 1$) — both conditions simultaneously. This is why the 3.B lock's retained structure $R_{3B}$ is so much larger than the sum of its zone contributions: the zone alignment multiplied by the strong coupling gives an exponential enhancement.

---

## Misalignment and Topological Defects

Zone misalignment ($\Delta\phi_{\alpha\beta} \neq 0$ or $\pm\pi$) generates **topological defects at the zone interfaces**. When two adjacent zones have a phase difference $0 < |\Delta\phi_{\alpha\beta}| < \pi$, the interface between them hosts a **phase gradient** — a smooth variation of phase across the membrane. This phase gradient costs energy (gradient energy $\propto|\nabla\arg\Phi|^2$), reducing the retained structure.

When the phase difference exactly equals $\pi$ at a point along the interface (a **phase inversion point**), a vortex core nucleates at that point on the interface — the amplitude $|\Phi|$ drops to zero, and the phase winds by $\pm 2\pi$ around the zero. This is the origin of **junction vortices**: topological defects that form at zone vertices when the surrounding zones are mutually misaligned.

The **junction vortex** (section 11.3) is therefore not just a mathematical curiosity — it is the signature of zone misalignment. A ICHTB with many junction vortices is a misaligned ICHTB with reduced retained structure. The process of **aligning** the zones (through the synchronization driven by the Apex zone) is equivalent to **annihilating** the junction vortices — driving the ICHTB from the incoherent (many vortices) phase to the coherent (no vortices) 3.B lock phase.

