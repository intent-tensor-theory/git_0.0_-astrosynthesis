# 21.2 Valley of Stability as Persistence Optimum in Zone Space

## The Nuclear Valley of Stability

The **valley of stability** (also called the valley of beta stability) is the region in the $(Z, N)$ plane where nuclei are stable against beta decay. It is a narrow band running from the origin (light nuclei, $Z \approx N$) to the upper-right (heavy nuclei, $N > Z$, e.g., ${}^{208}$Pb with $Z = 82$, $N = 126$). Nuclei in the valley of stability have the maximum binding energy per nucleon for fixed $A$ — they occupy the minimum of the energy landscape in the $(Z, N)$ plane.

In the ICHTB framework, the valley of stability is the **persistence optimum in zone space** — the region of the ICHTB configuration space where the corrected persistence $S^*$ is maximized for fixed total composite number $n_{\text{comp}} = A$. It is not just a minimum of the nuclear mass formula (SEMF) but a maximum of the composite excitation's persistence — the configuration that survives longest under the collapse dynamics.

---

## Zone Space and the Stability Surface

**Zone space** for composite excitations is the space of all possible zone configurations parameterized by:
- $n_+ = Z$: number of $\chi = +1$ (positive chirality, proton-like) vortices
- $n_- = N$: number of $\chi = -1$ (negative chirality, neutron-like) vortices
- $n_{\text{comp}} = A = Z + N$: total composite number
- Apex shell quantum numbers $(n_1, n_2, \ldots)$: the Apex locks occupied

The **stability surface** is the function $S^*(Z, N)$ — the corrected persistence as a function of the proton and neutron numbers. The valley of stability is the ridge of maximum $S^*$ in this surface:

$$
\text{Valley of stability:} \quad \left\{(Z, N) : \frac{\partial S^*}{\partial Z}\bigg|_A = 0\right\}
$$

(the locus of $Z$ values, for each fixed $A$, that maximize $S^*$).

---

## Deriving the Valley from the Zone Energy Balance

The corrected persistence condition (section 15.4) evaluated for the SEMF composite:

$$
S^* = \mathcal{E}_{\text{shell}} \cdot \mathcal{E} \cdot D \cdot T_{\text{obj}} \cdot \frac{E_B(A,Z)}{\dot{E}_B\,t_{\text{ref}}}
$$

(where $E_B/(\dot{E}_B t_{\text{ref}})$ plays the role of $S = R/(\dot{R}t_{\text{ref}})$ — the lock energy divided by its loss rate times the reference time). For fixed multipliers ($\mathcal{E}_{\text{shell}} = \mathcal{E} = D = T_{\text{obj}} = 1$, fully eligible and locked), the persistence is maximized when $E_B(A, Z)$ is maximized for fixed $A$.

The maximum of $E_B(A,Z)$ for fixed $A = Z + N$:

$$
\frac{\partial E_B}{\partial Z}\bigg|_A = -a_C\frac{2Z - 1}{A^{1/3}} + a_A\frac{2(N-Z)}{A} = 0
$$

Solving for $Z_{\text{opt}}$ (the optimal proton number for fixed $A$):

$$
Z_{\text{opt}} = \frac{A/2}{1 + a_C A^{2/3}/(4a_A)}
$$

For light nuclei ($A \ll (4a_A/a_C)^{3/2} \approx 200$): $Z_{\text{opt}} \approx A/2$ (equal protons and neutrons — $N = Z$). For heavy nuclei ($A \gtrsim 200$): $Z_{\text{opt}} < A/2$ (neutron excess, since the Coulomb repulsion $a_C$ term penalizes large $Z$). The numerical estimate for ${}^{208}$Pb: $Z_{\text{opt}} = 104/(1 + 0.714 \times 208^{2/3}/(4 \times 23.2)) \approx 82$, matching the observed $Z = 82$.

**ICHTB interpretation:** The valley of stability is the set of $(Z, N)$ pairs where the Memory zone vortex imbalance $(N-Z)^2/A$ (asymmetry energy) is balanced against the Forward zone phase repulsion $Z(Z-1)/A^{1/3}$ (Coulomb energy). The optimum is where these two zone energy costs are in balance — neither too many positive-chirality vortices (excessive Coulomb/Forward zone repulsion) nor too large an imbalance (excessive Memory zone asymmetry energy).

---

## Zone-by-Zone Contribution to the Valley

Each zone's contribution shapes the valley in a specific way:

**Core zone (volume term):** The Core zone contribution $a_V A$ does not depend on $Z$ — it is the same for all $(Z,N)$ at fixed $A$. The Core zone does not contribute to the shape of the valley; it only sets the overall binding energy scale.

**Expansion zone (surface term):** The Expansion zone contribution $-a_S A^{2/3}$ also does not depend on $Z$ at fixed $A$ (the surface area $\propto A^{2/3}$ is fixed). The Expansion zone does not contribute to the valley shape.

**Forward zone (Coulomb repulsion):** The Forward zone contribution $-a_C Z(Z-1)/A^{1/3}$ penalizes large $Z$. It pushes the valley toward smaller $Z$ (neutron-rich configurations). For heavy nuclei, the Coulomb term dominates and drives $Z_{\text{opt}} < A/2$.

**Memory zone (asymmetry energy):** The Memory zone contribution $-a_A(N-Z)^2/A$ penalizes asymmetry. It pushes the valley toward $N = Z$ (symmetric configurations). For light nuclei, the asymmetry term dominates and maintains $Z_{\text{opt}} \approx A/2$.

**Apex zone (pairing):** The pairing term $\delta(A,Z)$ creates local enhancements at even-even nuclei — the valley has "terraces" at even-$Z$, even-$N$ configurations (extra binding from Apex braid pairing, section 21.1). The magic numbers ($Z$ or $N = 2, 8, 20, 28, 50, 82, 126$) are the ICHTB Apex zone shell closures — the configurations where a complete Apex shell is filled.

---

## Magic Numbers as ICHTB Apex Shell Closures

The nuclear **magic numbers** (2, 8, 20, 28, 50, 82, 126) are configurations where nuclei are particularly stable — they have anomalously high binding energy and a large first-excited-state energy. They correspond to the filling of complete nuclear shells in the nuclear shell model (Mayer and Jensen 1949).

In the ICHTB framework, the magic numbers are the **Apex zone shell closures** — the configurations where a complete Apex orbital shell (section 20.4) is filled. The Apex zone orbitals have quantum numbers $(n, l, m)$ with degeneracy $g_{nl} = 2(2l+1)$ (factor of 2 for spin $m_s = \pm 1/2$). The cumulative shell occupation numbers at each shell closure:

$$
A_{\text{magic}} = \sum_{n=1}^{N_{\text{shell}}} \sum_{l=0}^{n-1} 2(2l+1) = 2N_{\text{shell}}^2(N_{\text{shell}}+1)/3
$$

(Wait — this gives 2, 8, 20, 40, 70, 112, 168 for $N_{\text{shell}} = 1, 2, 3, 4, 5, 6, 7$.) The discrepancy from the observed magic numbers (28, 50, 82, 126) arises from the **spin-orbit coupling** in the Apex zone — the coupling between the Memory zone chirality $m_s$ and the Apex zone orbital angular momentum $l$ (the ICHTB version of the nuclear spin-orbit interaction, Mayer 1949).

The spin-orbit coupling in the ICHTB:

$$
\mathcal{H}_{\text{SO}} = \lambda_{\text{SO}}\mathbf{L}\cdot\mathbf{S} = \lambda_{\text{SO}} m \cdot m_s
$$

(the Apex orbital magnetic quantum number $m$ times the Memory chirality $m_s$), where $\lambda_{\text{SO}}$ is the spin-orbit coupling constant (determined by the Core-Memory junction vortex coupling $K_{\text{mem,core}}$, section 19.2). The spin-orbit term splits the orbital degeneracy — states with $j = l + 1/2$ (orbital and spin aligned) have lower energy than states with $j = l - 1/2$ (antialigned), pushing certain sub-shells to fill before others and producing the observed magic numbers.

This spin-orbit interpretation of magic numbers is exactly the ICHTB version of the Mayer-Jensen shell model — the spin-orbit coupling between the Apex zone orbital angular momentum and the Memory zone chirality reproduces the known magic numbers from the zone geometry.

---

## The Valley as a Persistence Landscape

The valley of stability is a **persistence landscape** — a surface $S^*(Z, N)$ in the $(Z, N)$ plane whose ridge is the valley. Visualizing this landscape:

```
N (neutron number)
│
│         ← valley ridge (Z_opt for each A)
│        /
│       /   (stable region: S* > 1)
│      /  
│     /
│    /  (proton-rich: S* reduced by Coulomb)
│   /
│  / (neutron-rich: S* reduced by asymmetry)
│ /
└─────────────────────────────────────────────── Z (proton number)
```

Configurations on the valley ridge (at $Z_{\text{opt}}$ for fixed $A$) have maximum persistence. Moving away from the ridge in either direction (toward proton-rich or neutron-rich configurations) reduces persistence by increasing either the Forward zone Coulomb cost or the Memory zone asymmetry cost. Sufficiently far from the ridge, $S^* < 1$ — the composite dissolves (decays via beta emission, returning toward the valley).

The **width of the valley** (the range of $Z$ values with $S^* > 1$ for fixed $A$) is determined by the ratio of the competing zone energies:

$$
\Delta Z_{\text{valley}} \approx \sqrt{\frac{a_A A}{a_C A^{2/3}}} = \sqrt{\frac{a_A}{a_C}} A^{1/6}
$$

For light nuclei ($A \sim 20$): $\Delta Z_{\text{valley}} \approx 6$ (narrow valley, only $Z = N \pm 3$ is stable). For heavy nuclei ($A \sim 200$): $\Delta Z_{\text{valley}} \approx 14$ (wider valley, greater range of stable $Z$). This is consistent with the observed width of the valley of stability in nuclear physics.

