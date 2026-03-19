# 17.1 The $\Lambda_{\text{lock}}$ Axis — Lock Energy Partitioned by Zone

## What $\Lambda_{\text{lock}}$ Measures

The **lock energy** $\Lambda_{\text{lock}}$ is the total free energy stored in the ICHTB when the 3.B lock is established — the energy cost (relative to the disordered A-state) of the fully locked configuration. It is the axis along which the qualitative character of the resulting composite excitation is measured: high $\Lambda_{\text{lock}}$ configurations are tightly bound (high-mass), low $\Lambda_{\text{lock}}$ configurations are loosely bound (low-mass or massless in the limit).

The lock energy is not a single number but a **vector** — it decomposes into zone contributions, each measuring the energy stored in that zone's excitation:

$$
\Lambda_{\text{lock}} = \sum_\alpha \Lambda_\alpha = \Lambda_{\text{core}} + \Lambda_{\text{fwd}} + \Lambda_{\text{exp}} + \Lambda_{\text{mem}} + \Lambda_{\text{apex}} + \Lambda_{\text{comp}}
$$

(sum over all six peripheral zones plus the Core; each term is positive). The total lock energy sets the energy scale of the composite excitation:

$$
E_{\text{particle}} \sim \Lambda_{\text{lock}}
$$

in the appropriate units. High-energy particles (heavy fermions, gauge bosons) have large $\Lambda_{\text{lock}}$; light particles (neutrinos, photons) have small $\Lambda_{\text{lock}}$.

---

## Zone-by-Zone Lock Energy Contributions

**Core zone (+0) lock energy $\Lambda_{\text{core}}$:**

The Core stores energy in its uniform B-state amplitude at the ICHTB center:

$$
\Lambda_{\text{core}} = \int_{\mathcal{V}_{\text{core}}}\left(\frac{\kappa}{2}|\Phi|^2 - \frac{\gamma}{4}|\Phi|^4 + \frac{\mu}{6}|\Phi|^6\right)d^3r - \mathcal{F}_A
$$

In the fully locked Core ($|\Phi| = \Phi_{B,\text{core}}$ throughout $\mathcal{V}_{\text{core}}$):

$$
\Lambda_{\text{core}} \approx \left(\frac{\kappa}{2}\Phi_{B,c}^2 - \frac{\gamma}{4}\Phi_{B,c}^4 + \frac{\mu}{6}\Phi_{B,c}^6\right)\mathcal{V}_{\text{core}} = \frac{\gamma^2}{12\mu}\mathcal{V}_{\text{core}}
$$

(evaluating the free energy density at the B-state minimum $\Phi_B^2 = \gamma/\mu$). The Core contribution is purely volumetric — it scales with the Core zone volume $\mathcal{V}_{\text{core}} \propto R_{\text{core}}^3$.

**Forward zone (+X) lock energy $\Lambda_{\text{fwd}}$:**

The Forward zone stores energy in its propagating phase gradient:

$$
\Lambda_{\text{fwd}} = \int_{\mathcal{V}_{\text{fwd}}} D|\nabla\Phi|^2\,d^3r + \mathcal{F}_{B,\text{fwd}}
$$

The dominant contribution is from the phase gradient $|\nabla\arg\Phi|^2 \sim k_{\min}^2 = 1/L_f^2$:

$$
\Lambda_{\text{fwd}} \approx D\Phi_{B,f}^2 k_{\min}^2 \mathcal{V}_{\text{fwd}} = D\Phi_{B,f}^2 \frac{\mathcal{V}_{\text{fwd}}}{L_f^2}
$$

The Forward contribution encodes the **momentum** of the composite excitation — configurations with large $k_{\min}$ (steep phase gradients in the Forward zone) have high $\Lambda_{\text{fwd}}$ and carry more momentum.

**Expansion zone (+Y) lock energy $\Lambda_{\text{exp}}$:**

The Expansion zone stores energy in the 2D phase gradient (the bloom):

$$
\Lambda_{\text{exp}} = D\Phi_{B,e}^2\frac{r_{\text{bloom}}^2}{4\xi_\perp^2}\mathcal{A}_{\text{exp}}
$$

where $\mathcal{A}_{\text{exp}}$ is the Expansion zone area. For a bloom that has spread to $r_{\text{bloom}} \gg \xi_\perp$: $\Lambda_{\text{exp}}$ is large (the bloom stores significant gradient energy). The Expansion contribution encodes the **transverse spread** — configurations with large blooms have high $\Lambda_{\text{exp}}$.

**Memory zone (−Y) lock energy $\Lambda_{\text{mem}}$:**

The Memory zone stores energy in the vortex core and the surrounding phase gradient:

$$
\Lambda_{\text{mem}} = E_{\text{vortex}} = \pi D_m\Phi_{B,m}^2\ln\!\left(\frac{R_{\text{mem}}}{\xi}\right)
$$

(the 2D vortex energy, logarithmically divergent in the thermodynamic limit but regulated by the Memory zone size $R_{\text{mem}}$). The vortex energy is the **spin energy** — it scales logarithmically with the zone size and is determined by the memory zone diffusion coefficient $D_m$ and B-state amplitude $\Phi_{B,m}$.

**Apex zone (+Z) lock energy $\Lambda_{\text{apex}}$:**

The Apex zone stores energy in its temporal coherence:

$$
\Lambda_{\text{apex}} = \hbar\omega_B|\psi_{\text{apex}}|^2\mathcal{V}_{\text{apex}}
$$

(the energy density of the phase-locked Apex field times the zone volume). This is the **rest energy** of the composite excitation — the Apex frequency $\omega_B$ sets the mass through $m \sim \hbar\omega_B/c^2$ (in appropriate units). The Apex contribution is the dominant term for massive particles.

**Compression zone (−X) lock energy $\Lambda_{\text{comp}}$:**

The Compression zone stores energy in the kink soliton (section 8.2):

$$
\Lambda_{\text{comp}} = E_{\text{kink}} = \frac{4}{3}\Phi_{B,c}^2\xi_c D_c k_c
$$

where $\xi_c = 1/k_c$ is the kink width. The kink energy is the **mass energy** in the Compression direction — it is the contribution of the soliton's gradient energy to the total lock energy.

---

## The $\Lambda_{\text{lock}}$ Axis in the Phase Chart

The phase chart (the survival map of Part IV) uses $\Lambda_{\text{lock}}$ as one of its two principal axes. Physically: the $\Lambda_{\text{lock}}$ axis measures how tightly the ICHTB is locked — the "quality" of the 3.B lock in energy terms.

On the $\Lambda_{\text{lock}}$ axis:

- **Low $\Lambda_{\text{lock}}$ (left region):** Weakly locked configurations. The zone B-states are weakly populated ($\Phi_{B,\alpha} \ll \Phi_{B,\max}$), the vortex energy is small (small $D_m$), and the Apex frequency $\omega_B$ is low. These correspond to **light composite excitations** — analogs of massless or near-massless particles (photons, neutrinos, gravitons).

- **Intermediate $\Lambda_{\text{lock}}$ (middle region):** Moderately locked configurations. The zones are fully locked but at moderate amplitudes. These correspond to **light massive particles** — analogs of electrons, muons, and light quarks.

- **High $\Lambda_{\text{lock}}$ (right region):** Strongly locked configurations. All zones are at full B-state amplitude, the vortex energy is maximized, and $\omega_B$ is at the natural frequency of the ICHTB. These correspond to **heavy particles** — analogs of the W/Z bosons, top quark, Higgs boson.

The zone decomposition of $\Lambda_{\text{lock}}$ tells us which zone dominates the lock energy for each type of excitation:

| Excitation type | Dominant zone | Character |
|---|---|---|
| Massless boson (photon) | Forward (+X) | Propagating gradient only |
| Light fermion (electron) | Memory (−Y) + Apex (+Z) | Vortex + temporal lock |
| Heavy fermion (top quark) | Apex (+Z) + Compression (−X) | Maximum temporal + soliton |
| Scalar boson (Higgs) | Core (+0) + Compression (−X) | Volumetric + soliton |
| Graviton | Expansion (+Y) | Maximum transverse bloom |

This table is the qualitative identification of excitation types with their ICHTB zone signatures. The full identification is developed in Chapter 20 (Part V).

---

## Zone Partitioning of $\Lambda_{\text{lock}}$ as a Diagnostic

The zone partition $\{\Lambda_\alpha\}$ is a **diagnostic** for the type of composite excitation — it provides more information than the total $\Lambda_{\text{lock}}$ alone. Two configurations can have the same total lock energy but completely different zone distributions:

**Configuration A:** $\Lambda_{\text{apex}} = 0.9\Lambda_{\text{lock}}$, all other zones small → massless-like (Apex-dominated), high temporal coherence, minimal spatial structure. This is a boson-type excitation.

**Configuration B:** $\Lambda_{\text{mem}} = 0.5\Lambda_{\text{lock}}$, $\Lambda_{\text{apex}} = 0.4\Lambda_{\text{lock}}$, others small → vortex + temporal coherence, the signature of a fermion (spin-1/2 excitation).

**Configuration C:** $\Lambda_{\text{comp}} = 0.6\Lambda_{\text{lock}}$, $\Lambda_{\text{core}} = 0.3\Lambda_{\text{lock}}$, others small → soliton + volumetric, the signature of a scalar (spin-0 excitation).

The zone partition thus specifies the **quantum number content** of the excitation (its spin, statistics, and couplings) beyond what the total energy alone can determine. In the phase chart, different zone partitions correspond to different regions — the chart is not merely a 2D diagram but a 6+1 dimensional map (one energy per zone plus the total $\Lambda_{\text{lock}}$) projected onto 2D for visualization.

