# 21.1 The Semi-Empirical Mass Formula as ICHTB Zone Energy Balance

## The SEMF and Its Terms

The **Semi-Empirical Mass Formula** (SEMF, also called the Bethe-Weizsäcker formula, 1935) expresses the binding energy of an atomic nucleus with $Z$ protons and $N$ neutrons (mass number $A = Z + N$) as:

$$
E_B(A, Z) = a_V A - a_S A^{2/3} - a_C\frac{Z(Z-1)}{A^{1/3}} - a_A\frac{(N-Z)^2}{A} + \delta(A, Z)
$$

where:
- $a_V A$: **volume term** (bulk binding energy, proportional to number of nucleons)
- $-a_S A^{2/3}$: **surface term** (reduction for nucleons at the nuclear surface)
- $-a_C Z(Z-1)/A^{1/3}$: **Coulomb term** (electrostatic repulsion among protons)
- $-a_A(N-Z)^2/A$: **asymmetry term** (Pauli exclusion penalty for $N \neq Z$)
- $\delta(A,Z)$: **pairing term** (extra binding for even-even nuclei)

with empirical constants $a_V \approx 15.8$ MeV, $a_S \approx 18.3$ MeV, $a_C \approx 0.714$ MeV, $a_A \approx 23.2$ MeV.

Each term in the SEMF corresponds to a specific ICHTB zone contribution to the total lock energy $\Lambda_{\text{lock}}$ of the composite excitation.

---

## Volume Term → Core Zone Energy

The **volume term** $a_V A$ is the dominant binding energy — it grows with the number of nucleons $A$ and represents the saturation property of the nuclear force (each nucleon binds to its neighbors, independent of the total number).

**ICHTB identification:** The volume term corresponds to the **Core zone lock energy**:

$$
a_V A \leftrightarrow \Lambda_{\text{core}} = \frac{\gamma^2}{12\mu}\mathcal{V}_{\text{core}}
$$

The Core zone is the ICHTB analog of the nuclear bulk — it contributes lock energy proportional to its volume $\mathcal{V}_{\text{core}}$. For a multi-nucleon composite (Region VI with $n_{\text{comp}} = A$), the Core zone volume scales with the number of constituent topological charges: $\mathcal{V}_{\text{core}} \propto A$ (each additional nucleon adds a vortex to the Memory zone, which extends the effective Core volume). Therefore $\Lambda_{\text{core}} \propto A$ — exactly the $A$-scaling of the volume term.

The constant $a_V = \gamma^2/(12\mu) \times (\mathcal{V}_{\text{core}}/A)$ is the volume lock energy per nucleon — determined by the NLS nonlinear coupling constants $\gamma$ and $\mu$ of the Core zone.

---

## Surface Term → Expansion Zone Energy

The **surface term** $-a_S A^{2/3}$ is negative — it reduces the binding energy. It represents the fact that nucleons at the nuclear surface are less bound than interior nucleons (they have fewer neighbors). The surface area scales as $A^{2/3}$ (for a sphere of volume $\propto A$).

**ICHTB identification:** The surface term corresponds to the **Expansion zone energy cost**:

$$
-a_S A^{2/3} \leftrightarrow -\Lambda_{\text{exp}} = -D\Phi_B^2\frac{r_{\text{bloom}}^2}{4\xi_\perp^2}\mathcal{A}_{\text{exp}}
$$

The Expansion zone bloom has area $\mathcal{A}_{\text{exp}} \propto r_{\text{bloom}}^2 \propto A^{2/3}$ (the bloom radius scales as the nuclear radius $r \propto A^{1/3}$, giving area $\propto A^{2/3}$). The Expansion zone energy is a **cost** — it is the energy "wasted" by the field spreading transversely rather than contributing to the Core binding. Therefore it appears with a negative sign in the lock energy balance (the Expansion zone energy reduces the net available lock energy for binding).

The constant $a_S = D\Phi_B^2/(4\xi_\perp^2) \times (\mathcal{A}_{\text{exp}}/A^{2/3})$ — the Expansion energy cost per unit surface.

---

## Coulomb Term → Forward Zone Repulsion

The **Coulomb term** $-a_C Z(Z-1)/A^{1/3}$ is negative — it reduces binding due to electrostatic repulsion between the $Z$ protons. The $Z(Z-1)/2$ factor counts proton pairs; $A^{1/3}$ is the nuclear radius.

**ICHTB identification:** The Coulomb term corresponds to the **Forward zone phase gradient energy**:

$$
-a_C\frac{Z(Z-1)}{A^{1/3}} \leftrightarrow -\Lambda_{\text{fwd}}^{(\text{Coulomb})} = -D\Phi_B^2 k_{\text{Coulomb}}^2 \mathcal{V}_{\text{fwd}}
$$

Each proton (chirality $\chi = +1$, shell coherence phase $\theta_{\text{shell}} \neq 0$) contributes a phase gradient in the Forward zone through its shell coherence. When $Z$ protons share the same ICHTB, their Forward zone phase gradients add with the same sign (all protons have the same charge phase), creating a **repulsive** phase gradient energy that scales as $Z^2$ for large $Z$ (reduced to $Z(Z-1)$ for the exact pair count). The nuclear radius $A^{1/3}$ appears because the phase gradient $k_{\text{Coulomb}} \propto 1/R \propto A^{-1/3}$ (the Coulomb phase gradient decreases as the nuclear volume increases).

The constant $a_C = De^2/(4\pi\epsilon_0\hbar c) \times$ (ICHTB geometry factor) — the Coulomb energy coefficient, which involves the fundamental charge $e$ coupling of the shell coherence phase to the electromagnetic field (the Josephson relation of section 16.4 and 18.5).

---

## Asymmetry Term → Memory Zone Vortex Balance

The **asymmetry term** $-a_A(N-Z)^2/A$ is negative — it penalizes asymmetry between neutron and proton numbers. At $N = Z$, the asymmetry term vanishes; for $N \neq Z$, it reduces binding.

**ICHTB identification:** The asymmetry term corresponds to the **Memory zone vortex imbalance energy**:

$$
-a_A\frac{(N-Z)^2}{A} \leftrightarrow -\Lambda_{\text{mem}}^{(\text{asym})} = -D_m\Phi_B^2\frac{(N_+ - N_-)^2}{n_{\text{comp}}}
$$

where $N_+ = Z$ (number of $\chi = +1$ chirality vortices, corresponding to protons) and $N_- = N$ (number of $\chi = -1$ chirality vortices, corresponding to neutrons). The Memory zone energy is minimized when the vortices are evenly distributed between the two chiralities ($N_+ = N_-$, i.e., $Z = N$). Any imbalance ($N_+ \neq N_-$, i.e., $Z \neq N$) creates a vortex pressure asymmetry in the Memory zone — a net torque on the zone that reduces the efficiency of the Apex lock.

The scaling $(N-Z)^2/A$: the numerator $(N-Z)^2$ is the squared imbalance; the denominator $A$ (the total vortex count $n_{\text{comp}}$) appears because the fractional imbalance $(N-Z)/A$ is what matters for the Memory zone vortex pressure (not the absolute imbalance).

The constant $a_A = D_m\Phi_B^2 \times$ (Memory zone geometry factor) — the asymmetry energy per unit of fractional imbalance squared.

---

## Pairing Term → Apex Zone Braid Pairing

The **pairing term** $\delta(A, Z)$ is:

$$
\delta(A, Z) = \begin{cases} +a_P/A^{1/2} & \text{even-even nuclei} \\ 0 & \text{odd-A nuclei} \\ -a_P/A^{1/2} & \text{odd-odd nuclei} \end{cases}
$$

It is positive for even-even nuclei (extra binding), negative for odd-odd, and zero for odd-$A$.

**ICHTB identification:** The pairing term corresponds to **Apex zone braid pairing** — the extra binding energy when the braid word $w \in B_3$ (section 16.4) is a symmetric (self-pairing) braid:

$$
\delta(A,Z) \leftrightarrow \Lambda_{\text{apex}}^{(\text{pair})} = \pm E_{\text{pair}}/\sqrt{A}
$$

For even-even nuclei: the braids pair — each $+\chi$ vortex pairs with a $-\chi$ vortex in the Apex zone, forming a **Cooper pair analog** (a pair of opposite-chirality vortices bound in the Apex zone through the junction vortex mechanism). The Cooper pair has binding energy $E_{\text{pair}} > 0$, adding to the total lock energy (positive $\delta$).

For odd-$A$ nuclei: one vortex is unpaired — it cannot form a Cooper pair and contributes no pairing energy ($\delta = 0$).

For odd-odd nuclei: two unpaired vortices (one $+\chi$ and one $-\chi$, but from different shell occupations) — their interaction is repulsive (antiparallel unpaired vortices repel in the Memory zone through their diverging phase gradients), giving negative $\delta$.

The $A^{-1/2}$ scaling: the Cooper pair binding energy decreases as $A^{-1/2}$ because the vortex density in the Memory zone decreases as $A$ increases (the individual vortices spread out, reducing their overlap and hence their pairing energy).

---

## The SEMF as ICHTB Zone Energy Balance

The complete identification:

$$
E_B(A, Z) = \underbrace{a_V A}_{\Lambda_{\text{core}}} - \underbrace{a_S A^{2/3}}_{\Lambda_{\text{exp}}} - \underbrace{a_C\frac{Z(Z-1)}{A^{1/3}}}_{\Lambda_{\text{fwd}}^{(\text{Coulomb})}} - \underbrace{a_A\frac{(N-Z)^2}{A}}_{\Lambda_{\text{mem}}^{(\text{asym})}} + \underbrace{\delta(A,Z)}_{\Lambda_{\text{apex}}^{(\text{pair})}}
$$

Every term in the SEMF is a zone energy contribution. The SEMF is not merely a phenomenological formula but a **zone energy balance** — the sum of lock energy contributions from all six ICHTB zones, each with a specific scaling in $A$ and $Z$ determined by the zone geometry.

The ICHTB thus provides a **structural derivation** of the SEMF: the five terms are not arbitrary phenomenological fits but consequences of the zone geometry (volume → Core, surface → Expansion, Coulomb → Forward, asymmetry → Memory, pairing → Apex braid). The empirical constants $a_V, a_S, a_C, a_A, a_P$ are the zone coupling constants in disguise — their numerical values are determined by the ICHTB geometry parameters $D_\alpha$, $\Phi_{B,\alpha}$, $R_a$, etc.

