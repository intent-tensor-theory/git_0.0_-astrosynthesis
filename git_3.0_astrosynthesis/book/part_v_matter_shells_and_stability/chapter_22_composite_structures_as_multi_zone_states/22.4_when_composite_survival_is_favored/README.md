# 22.4 When Composite Survival Is Favored

## The Central Question

When does a composite excitation survive — persist with $S^* > 1$ — rather than dissociate into its constituents? This question has three inter-related facets:

1. **Energetic**: Is the composite lock energy greater than the sum of constituent lock energies? ($\Lambda_{\text{comp}} > \sum_i \Lambda_i$)
2. **Geometric**: Does the ICHTB zone configuration support the composite's zone sharing pattern? (Is the composite zone pattern $\mathbf{z}$ compatible with the ICHTB geometry?)
3. **Dynamical**: Does the composite's persistence exceed its dissociation time? ($S^* > 1$ given the lock energy loss rates)

All three must be satisfied simultaneously for a composite to survive. The ICHTB provides a unified framework for all three — zone energy balance (energetic), zone geometry (geometric), and persistence integral (dynamical).

---

## Condition 1: Energetic — When Composite Binding Exceeds the Threshold

The composite is energetically favored when its lock energy exceeds the sum of constituent lock energies by more than the activation barrier:

$$
\Lambda_{\text{lock}}^{(\text{comp})} > \sum_i \Lambda_{\text{lock}}^{(i)} + \Lambda_{\text{barrier}}
$$

The conditions under which this is satisfied:

**Condition 1a — Opposite chirality pairing.** For a pair of charges with $\chi_1 = +1$ and $\chi_2 = -1$ (opposite chirality, analog of particle-antiparticle pairing): the Memory zone vortex imbalance $(N_+ - N_-)^2/n_{\text{comp}} = 0$ (zero asymmetry energy), giving maximum Memory zone lock energy. Combined with Forward zone gradient cancellation (opposite momenta cancel) and Apex Cooper pair binding, the opposite-chirality pair is the most energetically favorable composite configuration.

This explains why **fermion-antifermion pairs** (mesons, in QCD language) are bound: the $\bar{q}q$ pair has $\chi_+ + \chi_- = 0$ (color-neutral, zero Memory asymmetry), Forward zone cancelation, and Apex braid pairing. The meson is energetically preferred over separated quark and antiquark in the strong-coupling regime.

**Condition 1b — Shell closure compatibility.** A composite is energetically favored when its constituent charges collectively occupy complete Apex shell closures. For example, the $\alpha$-particle ($^4$He, $Z=N=2$) has two protons and two neutrons filling the $n=1$ Apex shell — a complete shell closure. The $\alpha$-particle is exceptionally tightly bound (binding energy per nucleon = 7.07 MeV, the local maximum in the $E_B/A$ vs. $A$ curve) because the shell closure gives maximum Apex pairing energy.

**Condition 1c — Zone geometry compatibility.** The composite must fit geometrically within the ICHTB — the merged zone pattern $\mathbf{z}_{\text{merged}}$ must not violate any zone boundary constraint. The key constraint: the merged Memory zone vortex density must not exceed the KT saturation density $1/\xi^2$ (section 21.3). For a composite with $n_{\text{comp}}$ charges in a Memory zone of radius $R_m$:

$$
n_{\text{comp}} \leq \pi R_m^2/\xi^2 \equiv N_{\text{KT,max}}
$$

Composites exceeding this limit are geometrically forbidden — they violate the zone boundary and dissociate (section 21.3 neutron drip line).

---

## Condition 2: Geometric — Zone Configuration Space Constraints

The zone configuration space for composites is constrained by the ICHTB geometry. The allowed composite configurations form a **discrete** set — not all combinations of zone occupations are compatible with a valid ICHTB zone structure.

**Geometric constraint 1 — Core zone merger condition.** Two charges merge their Core zones (forming a higher-winding vortex) if and only if their separation $d < \xi_{\text{core}}$ (within one Core coherence length). If $d > \xi_{\text{core}}$, they have separate Core sub-zones (a separated composite). The merger condition:

$$
d < \xi_{\text{core}} = \hbar/\sqrt{2m_{\text{eff}}\mu|\Psi_0|^2}
$$

(the Core zone coherence length from the NLS parameters $m_{\text{eff}}$, $\mu$, and the background amplitude $|\Psi_0|$). Nuclear composites with $d \sim 1$ fm and $\xi_{\text{core}} \sim 0.5$ fm are typically in the merged Core regime for bound nucleon pairs, but the separated Core regime for the overall nucleus.

**Geometric constraint 2 — Apex orbital exclusion.** By the ICHTB Pauli exclusion (section 20.4): two charges with the same chirality $\chi$ and the same Apex orbital quantum numbers $(n, l, m)$ cannot occupy the same Apex orbital. This is the ICHTB version of the Pauli exclusion principle — it prevents two same-chirality charges from entering the same zone configuration.

Consequence for composites: a composite with $n$ charges of the same chirality requires $n$ distinct Apex orbitals (one per charge). For large $n$ (large nuclei, Fermi gas of electrons in a metal): the charges fill successive Apex orbitals up to the Fermi level — the composite is a **Fermi composite**. For $n$ charges of alternating chirality ($n/2$ of each, Cooper-paired): all charges can occupy the same Apex orbital in the singlet state — the composite is a **Bose composite** (a BEC-like configuration).

**Geometric constraint 3 — Braid feasibility.** Not all braid types in $B_n$ are geometrically accessible within the ICHTB. The allowed braids must satisfy:

- The braid word $w$ has braid closure compatible with the Apex zone topology (the closure of $w$ must be a link in the Apex zone manifold that has the correct Seifert fiber structure)
- The braid is aperiodic (the braid does not repeat with period less than $T_{\text{zone}}$ — the zone traversal time)

For $B_2$: all braids $\sigma_1^k$ are geometrically accessible, but only even $k$ give closed Apex orbits (odd $k$ give open orbits that don't return to the initial configuration — they are not equilibrium states).

For $B_3$: the color-singlet braid $\Delta^2$ is the minimal geometrically closed braid — the minimum number of crossings required to close a three-strand braid into a knot-free (colorless) configuration. This is the ICHTB derivation of why baryons have three quarks: the $\Delta^2 \in B_3$ braid is the minimal closed braid for three charges.

---

## Condition 3: Dynamical — When $S^* > 1$ Despite Energy Loss

Even if the composite is energetically and geometrically favorable, it must also satisfy the dynamical persistence condition $S^* > 1$. The corrected persistence for a composite:

$$
S^*_{\text{comp}} = \mathcal{E}_{\text{shell}} \cdot \mathcal{E} \cdot D \cdot T_{\text{obj}} \cdot \frac{\Lambda_{\text{lock}}^{(\text{comp})}}{\dot{\Lambda}_{\text{lock}}^{(\text{comp})} \cdot t_{\text{ref}}}
$$

The lock energy loss rate $\dot{\Lambda}_{\text{lock}}^{(\text{comp})}$ for a composite includes contributions from:

1. **Radiative loss**: the composite radiates NLS waves (phonons, photons, gluons) as it evolves — losing energy at rate $\dot{\Lambda}_{\text{rad}} \propto a^4 \omega^4 |\Psi|^2$ (dipole radiation, section 14.3).
2. **Dissociation loss**: the composite can thermally dissociate — losing lock energy at rate $\dot{\Lambda}_{\text{dis}} \propto e^{-\Lambda_{\text{bind}}/T_{\text{eff}}}$ (Boltzmann suppression by the binding energy).
3. **Decay loss**: the composite can decay into lighter composites — losing lock energy at rate $\dot{\Lambda}_{\text{decay}} = \Lambda_{\text{lock}}/\tau_{\text{decay}}$ (where $\tau_{\text{decay}}$ is the decay lifetime).

The composite survives ($S^* > 1$) when the total lock energy loss rate is slow enough that:

$$
\tau_{\text{comp}} = \frac{\Lambda_{\text{lock}}^{(\text{comp})}}{\dot{\Lambda}_{\text{lock}}^{(\text{comp)}}} > t_{\text{ref}}
$$

(the composite lifetime exceeds the reference time scale). The composite is stable (essentially permanent) when $\tau_{\text{comp}} \gg t_{\text{ref}}$.

---

## The Five Conditions for Composite Survival

Combining the energetic, geometric, and dynamical conditions, a composite excitation survives if and only if **all five** of the following are satisfied:

1. **Binding**: $\Lambda_{\text{comp}} > \Lambda_{\text{barrier}}$ (zone sharing benefit exceeds activation cost)
2. **Shell compatibility**: the composite occupies complete or near-complete Apex shell configurations (pairing energy is maximized)
3. **Geometric fit**: $n_{\text{comp}} \leq N_{\text{KT,max}}$ (not exceeding Memory zone vortex capacity)
4. **Braid closure**: the composite braid $w \in B_{n_{\text{comp}}}$ is a closed, color-singlet braid (geometrically accessible and confined)
5. **Persistence**: $S^*_{\text{comp}} > 1$ (the composite's lock energy loss rate is slow enough for the composite to persist over the reference time $t_{\text{ref}}$)

Each condition eliminates a class of composite configurations:
- Condition 1 eliminates unbound composites (repulsive zone sharing)
- Condition 2 eliminates magic-number-adjacent composites with broken shell closures
- Condition 3 eliminates composites beyond the drip lines
- Condition 4 eliminates color-charged (gluon-like) partial-braid configurations
- Condition 5 eliminates composites that decay or dissociate too quickly

The composites that survive all five conditions are the **stable composite matter** of the ICHTB universe — the atoms and nuclei in the valley of stability (Part V), the Cooper pairs in superconductors (Chapter 20), the baryons in QCD (this chapter), and the molecular bonds in chemistry (section 21.4).

---

## Why Composite Forms Are Rarer Than Individual Charges

The five conditions together explain why composite excitations are **rarer** than individual (non-composite) charges in a generic ICHTB environment:

- Individual charges have $n_{\text{comp}} = 1$: they automatically satisfy conditions 2–4 (single charge has trivial braid $\mathbf{1} \in B_1$, always shell-compatible, always geometrically fitting)
- Composite charges ($n_{\text{comp}} \geq 2$) must satisfy all five conditions — a much more restrictive set of requirements

For every composite that forms and persists, there are many more attempted composites that fail one or more conditions and dissociate. The **ratio of composites to individuals** in thermal equilibrium is:

$$
\frac{N_{\text{comp}}}{N_{\text{ind}}} \propto e^{(\Lambda_{\text{comp}} - \Lambda_{\text{barrier}} - n_{\text{comp}}\Lambda_{\text{ind}})/T_{\text{eff}}}
$$

(the Boltzmann factor for composite formation). For $\Lambda_{\text{comp}} < \Lambda_{\text{barrier}} + n_{\text{comp}}\Lambda_{\text{ind}}$ (the composite is energetically unfavorable): the exponential is negative and the composite is rare ($N_{\text{comp}}/N_{\text{ind}} \ll 1$). For $\Lambda_{\text{comp}} > \Lambda_{\text{barrier}} + n_{\text{comp}}\Lambda_{\text{ind}}$ (the composite is energetically favorable): the exponential is positive and composites dominate over individuals.

This ratio is the ICHTB version of the **Saha equation** (Saha 1920) for ionization equilibrium — the balance between bound (composite) and free (individual) configurations in a thermal environment. At high temperature ($T_{\text{eff}} \gg \Lambda_{\text{bind}}$): the exponential is suppressed and individuals dominate (ionized plasma). At low temperature ($T_{\text{eff}} \ll \Lambda_{\text{bind}}$): the exponential is enhanced and composites dominate (bound matter — atoms, nuclei, molecules).

The **composite-to-individual transition** as temperature decreases (the ICHTB version of recombination, nucleosynthesis, and condensation) is the topic of Part VI — where the chapter on cosmic structure formation (Chapter 24) addresses how the ICHTB zone hierarchy produces the large-scale matter structure of the universe through sequential composite formation as the temperature falls below successive binding thresholds.

