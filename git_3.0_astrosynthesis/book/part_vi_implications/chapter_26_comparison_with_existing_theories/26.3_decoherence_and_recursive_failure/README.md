# 26.3 Decoherence and Recursive Failure

## Quantum Decoherence: The Standard Account

**Decoherence** (Zeh 1970, Zurek 1982, 1991, 2003) is the process by which a quantum system loses its quantum coherence — the ability to exhibit interference — through entanglement with its environment. The standard account:

A system $S$ is initially in a superposition $|\psi\rangle = c_0|0\rangle + c_1|1\rangle$. When $S$ interacts with an environment $E$ (initially in state $|E_0\rangle$), the combined state evolves to:

$$
(c_0|0\rangle + c_1|1\rangle)|E_0\rangle \to c_0|0\rangle|E_0\rangle + c_1|1\rangle|E_1\rangle
$$

(the environment records which state the system is in). After tracing over the environment, the **reduced density matrix** of $S$ is:

$$
\rho_S = \text{Tr}_E[|\Psi_{SE}\rangle\langle\Psi_{SE}|] = |c_0|^2|0\rangle\langle 0| + |c_1|^2|1\rangle\langle 1| + c_0c_1^*|0\rangle\langle 1|\langle E_1|E_0\rangle + c.c.
$$

The off-diagonal terms (the interference terms) are suppressed by $\langle E_1|E_0\rangle \to 0$ as the environment grows — for a large environment, $|E_0\rangle$ and $|E_1\rangle$ become nearly orthogonal. The result is a **classical mixture** — the system appears to be in state $|0\rangle$ with probability $|c_0|^2$ or $|1\rangle$ with probability $|c_1|^2$, with no quantum interference.

Decoherence explains why we observe classical outcomes for macroscopic systems: their environments are so large that coherence is lost almost instantly. Decoherence does not solve the measurement problem (it explains why interference is not observed, but not why a specific outcome is obtained), but it explains the appearance of classicality.

---

## ICHTB Decoherence: Zone Membrane Leakage

In the ICHTB, decoherence is **zone membrane leakage** — the process by which the Forward zone (external interface zone, carrying the phase gradient of external influence) leaks its phase coherence into the Memory zone (internal coherence storage zone), corrupting the Memory zone's phase record.

The ICHTB decoherence process:

1. **Incoming perturbation:** An external field (another excitation, an environmental fluctuation) enters the ICHTB through the Forward zone (+X face). The Forward zone absorbs the incoming field's phase information into its phase gradient $\mathbf{k}_{\text{incoming}}$.

2. **Forward-Memory coupling:** The Forward zone couples to the Memory zone through the zone membrane $\mathcal{M}_{\text{fwd-mem}}$. If the incoming perturbation is strong enough to activate this membrane (energy $> \Lambda_{\text{threshold}}^{(\text{fwd-mem})}$), the Memory zone's phase coherence is disturbed.

3. **Memory zone dephasing:** The Memory zone's chirality record ($\chi = \pm 1$, the topological charge that encodes the system's quantum state) is perturbed by the incoming Forward zone phase. If the perturbation is large enough, the chirality can flip ($\chi \to -\chi$), constituting a **decoherence event** — the quantum state has been "read" and collapsed by the environment.

4. **Zone coherence loss:** After a decoherence event, the Memory zone's phase record is no longer in the original superposition — it has been collapsed to one of the two chirality states by the environmental perturbation. The excitation's $S^*$ drops (section 21.5 — zone coherence enters $S^*$), reflecting the loss of internal quantum coherence.

The **decoherence time** in the ICHTB:

$$
\tau_{\text{decohere}} = \frac{\Lambda_{\text{threshold}}^{(\text{fwd-mem})}}{P_{\text{env}}}
$$

where $P_{\text{env}}$ is the power of environmental perturbations reaching the Forward zone. High $\Lambda_{\text{threshold}}^{(\text{fwd-mem})}$ (strong zone membrane) = long decoherence time. Large $P_{\text{env}}$ (strong environment) = short decoherence time. This matches the standard result: decoherence is faster for larger, more strongly coupled systems.

---

## Recursive Failure: When Decoherence Is Catastrophic

The standard decoherence account treats decoherence as a **loss of quantum coherence** — the system becomes classical but remains intact as a system. In the ICHTB, decoherence can trigger a more drastic process: **recursive failure** — a cascade of zone failures that dissolves the entire excitation.

Recursive failure occurs when:
1. Decoherence event in the Memory zone disturbs the Memory zone's phase gradient
2. This disturbs the Memory-Core zone coupling (the Memory zone can no longer maintain the Core zone's topological singularity)
3. The Core zone amplitude rises toward $\Phi_B$ (partial Core dissolution)
4. As the Core amplitude rises, the topological charge $n$ can change (topological transition)
5. If $n \to 0$ (complete Core dissolution), the entire vortex structure collapses
6. Collapse releases the Core zone lock energy $\Lambda_{\text{core}}$ as a burst of Expansion zone radiation
7. The released energy perturbs surrounding excitations, potentially triggering further decoherence events in neighboring excitations — recursive failure propagates

This is the ICHTB model of **measurement-induced collapse** — the "collapse of the wave function" is a recursive failure cascade triggered by the Forward zone decoherence event. The collapse is real (not merely apparent classicality) — it is the actual dissolution of the topological zone structure.

The difference from standard decoherence:
- Standard decoherence: the system becomes classical (the density matrix loses off-diagonal terms) but the quantum state persists in a mixture
- ICHTB recursive failure: the topological zone structure actually dissolves (the vortex ceases to exist)

These are not contradictory — standard decoherence is the **weak** limit (perturbation below $\Lambda_{\text{threshold}}^{(\text{core})}$, no Core zone dissolution), while ICHTB recursive failure is the **strong** limit (perturbation above $\Lambda_{\text{threshold}}^{(\text{core})}$, Core dissolution and excitation annihilation).

---

## Zurek's Pointer States and ICHTB Zone Eigenstates

Wojciech Zurek (1981, 1991) identified the **pointer states** (or **einselected states**) — the specific quantum states that are least affected by decoherence. Pointer states are the eigenstates of the system-environment coupling Hamiltonian — they are selected by the environment (hence "einselection") as the preferred classical basis.

In ICHTB language: pointer states = **zone eigenstates** — the zone configurations that are stable under Forward zone perturbations. These are the excitations with maximum $\Lambda_{\text{threshold}}^{(\text{fwd-mem})}$ — the strongest Forward-Memory zone membranes, most resistant to decoherence from environmental perturbations.

The ICHTB zone eigenstates are determined by the Memory zone's chirality spectrum — the eigenstates of the Memory zone chirality operator $\hat{\chi} = \pm 1$. These correspond to the two pointer states of a two-level system: $|\chi = +1\rangle$ and $|\chi = -1\rangle$ (the two stable topological charge states of the Memory zone). Environmental perturbations cannot continuously rotate between these states — they can only flip $\chi \to -\chi$ (a discrete jump), and this flip requires energy $> \Lambda_{\text{threshold}}^{(\text{fwd-mem})}$.

Zurek's einselection: environmental coupling selects the pointer states as the preferred classical basis. ICHTB einselection: the zone membrane activation threshold $\Lambda_{\text{threshold}}^{(\text{fwd-mem})}$ selects the chirality eigenstates $|\pm 1\rangle$ as the preferred stable configurations — all other superpositions are unstable against environmental Forward zone perturbations.

