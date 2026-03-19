# 24.3 Entropy as Coherence Degradation Across Zones

## Coherence in the ICHTB

The ICHTB excitations are **coherent** — their field configurations $\Psi(\mathbf{x}, t)$ have well-defined phase relationships across the zone structure. The phase winding in the Memory zone, the phase gradient in the Forward zone, and the phase of the Apex orbital modes are all mutually coherent — they are all determined by the same field $\Psi$ and are therefore correlated.

**Coherence** in the ICHTB is measured by the **off-diagonal elements of the reduced density matrix** $\rho(\mathbf{x}, \mathbf{x}') = \langle\Psi^*(\mathbf{x})\Psi(\mathbf{x}')\rangle$ (the two-point field correlation function). Full coherence: $|\rho(\mathbf{x}, \mathbf{x}')| = \sqrt{\rho(\mathbf{x},\mathbf{x})\rho(\mathbf{x}',\mathbf{x}')}$ (the product of the local amplitudes — the maximum possible value). Zero coherence (pure diagonal): $\rho(\mathbf{x}, \mathbf{x}') = 0$ for $\mathbf{x} \neq \mathbf{x}'$ (no phase correlation between different points).

The **entropy** of the ICHTB excitation is the von Neumann entropy of the reduced density matrix:

$$
S = -\text{Tr}(\rho \log \rho) = -\sum_k \lambda_k \log \lambda_k
$$

(where $\lambda_k$ are the eigenvalues of $\rho$). For a pure state (fully coherent): all eigenvalues are 0 except one ($\lambda_1 = 1$), giving $S = 0$. For a maximally mixed state (zero coherence): all eigenvalues are equal ($\lambda_k = 1/N$ for $N$ modes), giving $S = \log N$ (maximum entropy).

**Entropy = coherence degradation:** The entropy increases as the off-diagonal elements of $\rho$ decrease — as the phase correlations between different spatial points (different zones) are lost. This is the ICHTB definition of entropy: the degree to which the zone coherence has been degraded.

---

## Zone-by-Zone Coherence Structure

Each zone has a specific coherence structure:

**Core zone coherence:** The Core zone has amplitude maximum at the vortex core and rapidly decaying amplitude away from the core. The Core zone coherence length is $\xi_{\text{core}}$ — field points within $\xi_{\text{core}}$ of each other are fully coherent ($|\rho(\mathbf{x},\mathbf{x}')| \approx |\Psi_0|^2$ for $|\mathbf{x}-\mathbf{x}'| \ll \xi_{\text{core}}$). Field points separated by $\gg \xi_{\text{core}}$ are incoherent (Core zone does not extend to them).

**Memory zone coherence:** The Memory zone phase winding creates a specific coherence pattern — points at the same radius from the vortex core (at the same Memory zone shell) but different azimuthal angles have a phase difference $n\Delta\phi$. Their coherence: $\rho(\mathbf{x}, \mathbf{x}') \propto e^{in\Delta\phi}$ — they are coherent but phase-shifted. The Memory zone coherence is **angular coherence** — correlations structured by the azimuthal angle.

**Expansion zone coherence:** The Expansion zone bloom extends to radius $r_{\text{bloom}} \gg R_m$. The coherence in the Expansion zone falls off as $|\rho(\mathbf{x},\mathbf{x}')| \propto (r_{\text{bloom}}/|\mathbf{x}-\mathbf{x}'|)^{1/2}$ (power-law decay, characteristic of superfluid phase coherence in 2D — the Kosterlitz-Thouless quasi-long-range order). The Expansion zone coherence is **algebraically decaying** — long-ranged but not perfect.

**Forward zone coherence:** The Forward zone phase gradient creates **directional coherence** — points along the +X direction have a fixed phase relationship $\rho(\mathbf{x}, \mathbf{x}+\delta x\hat{x}) = |\Psi|^2 e^{ik_x\delta x}$ (coherent with phase $k_x\delta x$). Points transverse to +X ($\delta y$ or $\delta z$ displacement) have reduced coherence (determined by the transverse coherence length of the propagating beam).

**Apex zone coherence:** The Apex orbital modes have specific angular coherence patterns — each mode $(n, l, m)$ has angular coherence determined by the spherical harmonics $Y_l^m(\theta, \phi)$. Modes with different $(l, m)$ are orthogonal (incoherent); modes with the same $(l,m)$ are fully coherent.

---

## Coherence Degradation as the Source of Entropy

As the ICHTB excitation evolves, its zone coherence is progressively degraded by the loss cascade (section 24.1). The mechanism:

**Step 1: Apex zone coherence degrades.** The Apex zone orbital modes radiate NLS waves (phonons, photons) as they evolve — this is the spontaneous emission process (section 14.3). Each emitted photon carries away a phase-definite quantum of energy, but it also entangles the ICHTB with the emitted radiation. After tracing over the emitted radiation (which escapes the ICHTB), the Apex zone reduced density matrix loses its off-diagonal elements — the Apex zone coherence is degraded. This creates entropy $\Delta S_{\text{apex}} = k_B \log(n_{\text{modes}})$ per emitted photon.

**Step 2: Memory zone coherence degrades.** The Memory zone phase winding is coupled to the Apex zone through the spin-orbit interaction (section 21.2). As the Apex zone coherence degrades, the Memory zone phase winding becomes correlated with the Apex zone radiation field — the Memory zone is entangled with the emitted radiation. After tracing over the radiation, the Memory zone coherence $|\rho_{\text{mem}}(\theta, \theta')| = |\rho_0| e^{-|\theta-\theta'|^2/2\sigma_\theta^2}$ decreases — the angular coherence length $\sigma_\theta$ shrinks. The Memory zone entropy increases.

**Step 3: Expansion zone coherence degrades.** As the Memory zone coherence length shrinks, the Expansion zone algebraic decay exponent changes — the quasi-long-range order is reduced. In the KT language (section 20.3): the temperature $T$ of the Expansion zone effectively increases (the coherence degradation is equivalent to heating), driving the Expansion zone toward the KT transition. Past the KT transition: the Expansion zone coherence becomes short-ranged (exponentially decaying rather than power-law), and the Expansion zone entropy increases by $\Delta S_{\text{KT}} = k_B\log(L/\xi_{\text{KT}})^2$ (where $L$ is the Expansion zone size and $\xi_{\text{KT}}$ is the new short-range coherence length).

**Step 4: Cascade to background.** The Expansion zone coherence degradation radiates heat into the background NLS field — raising the background temperature $T_{\text{bg}}$ and increasing the background entropy. This is the final step of the cascade — the lock energy has been converted to background heat (random phase fluctuations in the background field).

---

## The ICHTB Entropy Function

The total entropy of the ICHTB excitation is the sum of zone coherence degradations:

$$
S_{\text{ICHTB}} = S_{\text{apex}} + S_{\text{mem}} + S_{\text{exp}} + S_{\text{fwd}} + S_{\text{core}} + S_{\text{trans}}
$$

For a fully coherent excitation (a pure state, $S^* \gg 1$): all zone entropies are zero (the zone density matrices are pure — no decoherence). As $S^*$ decreases toward 1 (the persistence threshold): the zone entropies grow (the zone coherences degrade). At $S^* = 1$ (the threshold): the excitation is marginally coherent — the total zone entropy equals the maximum entropy consistent with maintaining the lock energy above the threshold. Below $S^* < 1$: the total zone entropy exceeds the maximum sustainable value — the lock can no longer be maintained, and the excitation dissolves.

The relationship between the persistence $S^*$ and the zone entropy:

$$
S^* = e^{-S_{\text{ICHTB}}/k_B} \cdot \frac{\Lambda_{\text{lock}}}{\dot{\Lambda}_{\text{lock,0}} \cdot t_{\text{ref}}}
$$

(where $\dot{\Lambda}_{\text{lock,0}}$ is the loss rate at zero entropy — the maximum persistence at full coherence). Zone entropy exponentially suppresses the persistence: each bit of zone entropy ($\Delta S = k_B \log 2$) reduces $S^*$ by a factor of 2. The most persistent excitations are those with the lowest zone entropy — the most coherent configurations.

This is the ICHTB version of the **quantum coherence-decoherence trade-off**: coherent quantum states (pure states, $S = 0$) have maximum persistence; mixed states (decoherent, $S > 0$) have reduced persistence. The persistence criterion $S^* > 1$ selects the most coherent configurations — the ICHTB universe preferentially maintains coherent (low-entropy) excitations and allows incoherent (high-entropy) ones to dissolve.

