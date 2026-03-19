# 21.3 Drip Lines as Zone Boundary Failure

## The Nuclear Drip Lines

The **proton drip line** and **neutron drip line** are the boundaries in the $(Z, N)$ plane beyond which nuclei are unbound — they "drip" nucleons (protons or neutrons spontaneously emitted). The proton drip line is the boundary to the left of the valley of stability (proton-rich side); the neutron drip line is the boundary to the right (neutron-rich side).

Beyond the drip lines:
- **Proton drip line:** A nucleus with $Z > Z_{\text{drip}}$ (for fixed $N$) is proton-unbound — the last proton has positive separation energy and spontaneously separates from the nucleus.
- **Neutron drip line:** A nucleus with $N > N_{\text{drip}}$ (for fixed $Z$) is neutron-unbound — the last neutron has positive separation energy and spontaneously leaves.

In ICHTB terms, the drip lines are the **zone boundary failure** conditions — the conditions where a specific zone membrane fails to maintain the composite excitation, allowing one constituent topological charge to leak out of the ICHTB.

---

## Zone Boundary Failure: The General Concept

**Zone boundary failure** occurs when the field amplitude at a zone membrane falls below the membrane's activation threshold — the threshold for sustaining the transmission of topological charge across the membrane. When the membrane fails, the topological charge "leaks" out of the zone into the adjacent (lower-energy) zone.

For a composite excitation with $A = Z + N$ total vortex charges in the Memory zone, the membrane failure condition is:

$$
|\Phi_{\alpha\beta}|_{\text{threshold}} > |\Phi_{\alpha\beta}|_{\text{actual}}
$$

(the actual field amplitude at the membrane falls below the required threshold for sustaining the transmission). When this happens, one or more vortex charges are no longer contained within the zone — they "drip" through the membrane into the external environment.

---

## Proton Drip Line as Forward Zone Membrane Failure

The **proton drip line** corresponds to **Forward zone membrane failure**: the Forward zone (+X) can no longer sustain the repulsive phase gradient created by too many positive-chirality ($\chi = +1$) vortices.

The Forward zone Coulomb repulsion creates a phase gradient $k_{\text{Coulomb}} \propto Z/A^{1/3}$ in the Forward zone (section 21.1). As $Z$ increases at fixed $A$, this phase gradient grows. The Forward zone membrane $\mathcal{M}_{\text{fwd,core}}$ can sustain up to a maximum phase gradient $k_{\text{max}} = 1/\xi_f$ (the inverse coherence length of the Forward zone field). When:

$$
k_{\text{Coulomb}} = \frac{a_C Z}{D\Phi_B^2 A^{1/3}} > k_{\text{max}} = \frac{1}{\xi_f}
$$

the Forward zone membrane fails — the phase gradient exceeds the membrane's capacity, and the excess phase-gradient energy is released by ejecting one proton ($\chi = +1$ vortex) from the Memory zone through the Core and Forward zones into the external environment.

The **proton drip condition** (proton separation energy $S_p = 0$):

$$
E_B(A, Z) - E_B(A-1, Z-1) = 0
$$

In ICHTB zone terms:

$$
\Lambda_{\text{fwd}}^{(\text{Coulomb})}(A,Z) - \Lambda_{\text{fwd}}^{(\text{Coulomb})}(A-1,Z-1) = \Lambda_{\text{core}}(A) - \Lambda_{\text{core}}(A-1)
$$

(the Forward zone repulsion energy of the last proton equals the Core zone binding energy gained by removing it — at the drip line, these are exactly equal). Solving for the drip-line $Z$:

$$
Z_{\text{drip}}(N) \approx \frac{a_V - a_S A^{-1/3} + a_A(1 - 2N/A)}{a_C/A^{1/3} + a_A/A}
$$

(the proton drip line from the SEMF condition $S_p = 0$, which is equivalently the Forward zone membrane failure condition in ICHTB terms).

The proton drip line lies to the left of the valley of stability (proton-rich side). Below the drip line (insufficient $Z$): the Forward zone membrane is intact, all protons are contained. Beyond the drip line (excess $Z$): the Forward zone membrane fails and protons "drip" out.

---

## Neutron Drip Line as Memory Zone Boundary Saturation

The **neutron drip line** corresponds to **Memory zone boundary saturation**: the Memory zone can no longer accommodate additional $\chi = -1$ (neutron-like) vortices because it has reached its maximum vortex density.

The Memory zone can support a maximum vortex density determined by the Kosterlitz-Thouless criterion: the vortex density cannot exceed one vortex per coherence area $\xi^2$ (one vortex per KT vortex core):

$$
\rho_{\text{vortex}} = \frac{N}{R_{\text{mem}}^2} \leq \rho_{\text{max}} = \frac{1}{\xi^2}
$$

When $N > N_{\text{drip}} = R_{\text{mem}}^2/\xi^2$ (for fixed ICHTB size), the Memory zone is **saturated** — it cannot accommodate another neutron-like vortex. Additional neutrons would have to go into the next higher Memory zone orbital, which has positive energy (above the B-state) — i.e., the last neutron is unbound.

The Memory zone saturation condition is equivalent to the vortex filling fraction reaching 1 (all KT vortex sites occupied). In nuclear physics, this is the analog of the **Pauli blocking** of the last neutron orbital: all lower-energy neutron orbitals are filled, and the next neutron must go into a continuum state (unbound).

**Memory zone saturation in zone terms:**

$$
N_{\text{drip}} \approx \frac{\pi R_{\text{mem}}^2}{\xi^2} = \pi\left(\frac{R_{\text{mem}}}{\xi}\right)^2
$$

(the number of KT vortex sites in the Memory zone disc of radius $R_{\text{mem}}$). For a Memory zone of radius $R_{\text{mem}} = 10\xi$: $N_{\text{drip}} \approx 314$ — a large composite (would correspond to a nucleus with $A \sim 600$, near the predicted neutron drip line for such mass numbers).

---

## Drip Line Asymmetry: Why Proton Drip $\neq$ Neutron Drip

The proton drip line and neutron drip line are **asymmetric** — the neutron drip line extends to much larger $N/Z$ ratios than the proton drip line does to large $Z/N$ ratios. For example, at $Z = 20$ (calcium): the proton drip line is at $N \approx 12$ (just 8 excess protons), but the neutron drip line is at $N \approx 60$ (40 excess neutrons). The ICHTB explanation:

**Proton drip (Forward zone failure):** The Coulomb repulsion $\propto Z^2/A^{1/3}$ grows quadratically with $Z$, limiting the proton excess quickly. The Forward zone membrane has a finite capacity for the repulsive phase gradient; it fails at relatively small $Z$ excess.

**Neutron drip (Memory zone saturation):** The Memory zone asymmetry energy $\propto (N-Z)^2/A$ grows only quadratically in the imbalance and is suppressed by $A$. The Memory zone can accommodate a much larger vortex imbalance before saturating — the KT vortex capacity is large and grows with the zone area. This allows a much larger neutron excess before the neutron drip line is reached.

The asymmetry is a direct consequence of the different zone mechanisms: Forward zone failure (Coulomb) is a **phase gradient** mechanism (fast-growing with $Z$), while Memory zone saturation is a **density** mechanism (growing slowly with $N$ as long as there is space). The faster-growing mechanism (proton Coulomb) produces a tighter drip line; the slower mechanism (neutron density) produces a wider drip line.

---

## Terra Incognita: Beyond the Drip Lines

Beyond the drip lines, the ICHTB composite excitations are **unbound** in the traditional sense — but they may still exist as **resonance states**: short-lived configurations where the unbound topological charge is temporarily held in the ICHTB before escaping. These are the nuclear analogs of nuclear resonances (unbound states above the particle threshold).

In ICHTB terms, resonance states beyond the drip lines are **Region III or Region IV configurations** (section 18.3, 18.4) in the survival map — partially closed structures that persist for a finite time ($S^* \lesssim 1$, marginally below threshold) before the leaking vortex escapes through the failing zone membrane.

The lifetime of such resonance states:

$$
\tau_{\text{res}} = \hbar/\Gamma_{\text{decay}} = \hbar/(|E_{\text{bound}}|/\hbar) \approx \hbar^2/|E_{\text{bound}}|
$$

(where $E_{\text{bound}} < 0$ is the negative separation energy — the configuration is unbound by $|E_{\text{bound}}|$). For $|E_{\text{bound}}| \sim 1$ MeV: $\tau_{\text{res}} \sim 10^{-21}$ s — a very short-lived nuclear resonance. These are the configurations that ICHTB explores in the region beyond the drip lines, where zone boundary failure is partial and temporary rather than complete and permanent.

