# 19.2 Mathematics of Each Transition at Its Interface

## The General Framework

Each transition between survival regions is governed by a set of **interface equations** — the field-theoretic boundary conditions at the transition membrane, combined with the topological and kinetic conditions that must be satisfied for the transition to occur. This section derives the mathematics of each of the five transitions.

The general interface conditions at membrane $\mathcal{M}_{\alpha\beta}$ (derived in section 11.1):

$$
\Phi_\alpha\Big|_{\mathcal{M}} = \Phi_\beta\Big|_{\mathcal{M}} \quad (\text{amplitude continuity})
$$
$$
D_\alpha\nabla_n\Phi_\alpha\Big|_{\mathcal{M}} = D_\beta\nabla_n\Phi_\beta\Big|_{\mathcal{M}} \quad (\text{current continuity})
$$

where $\nabla_n$ is the normal derivative (outward from each zone). These two conditions, together with the asymptotic form of the field in each zone (B-state plus perturbation), determine the transmission and reflection amplitudes at each membrane.

---

## Transition I→II: Forward-to-Core Membrane

**Interface:** $\mathcal{M}_{\text{fwd,core}}$, between the Forward zone (+X) and Core zone (+0).

The Forward zone field has the form of a propagating wave in the +X direction:

$$
\Phi_{\text{fwd}}(x) = \Phi_{B,f}e^{i\omega t}\left[1 + A_{\text{inc}}e^{ik_f x} + A_{\text{ref}}e^{-ik_f x}\right]
$$

(B-state background plus incident and reflected amplitude waves, wavenumber $k_f = \sqrt{2\kappa_f/D_f}$). The Core zone field, on the other side of the membrane, is the evanescent decay from the Core center:

$$
\Phi_{\text{core}}(x) = \Phi_{B,c}e^{i\omega t}\left[1 + A_{\text{trans}}\cosh(k_c x)\right]
$$

(B-state plus hyperbolic cosine for the Core's spatial profile, $k_c = \sqrt{2\kappa_c/D_c}$).

Applying the interface conditions at $x = x_{\mathcal{M}}$:

$$
A_{\text{trans}} = \frac{2k_f/D_f}{k_f/D_f + k_c/D_c}\frac{\Phi_{B,f}}{\Phi_{B,c}} A_{\text{inc}}
$$

$$
A_{\text{ref}} = \frac{k_f/D_f - k_c/D_c}{k_f/D_f + k_c/D_c} A_{\text{inc}}
$$

The **transmission coefficient** (power fraction entering Core):

$$
T_{I\to II} = \frac{4(k_f/D_f)(k_c/D_c)}{(k_f/D_f + k_c/D_c)^2} \cdot \frac{\Phi_{B,f}^2}{\Phi_{B,c}^2}
$$

The I→II transition occurs when $|A_{\text{inc}}| > |A_{\text{inc}}|_{\text{thresh}} = \epsilon_c\Phi_{B,c}/A_{\text{trans,unit}}$ — when the transmitted amplitude exceeds the Core activation threshold $\epsilon_c\Phi_{B,c}$. This gives the minimum incident wave amplitude for Core activation:

$$
\Phi_{\text{fwd,thresh}} = \frac{\epsilon_c\Phi_{B,c}}{|A_{\text{trans,unit}}|} = \frac{\epsilon_c\Phi_{B,c}(k_f/D_f + k_c/D_c)}{2k_f/D_f}
$$

**Physical interpretation:** The I→II transition is analogous to quantum mechanical tunneling through a potential step. The Forward zone wave approaches the Core "barrier" (the amplitude mismatch $\Phi_{B,c} > \Phi_{B,f}$ is a potential step upward). Below threshold: the wave is reflected and the Core remains inactive (Region I). Above threshold: the wave transmits and activates the Core (Region II).

---

## Transition II→III: Core-to-Memory Membrane

**Interface:** $\mathcal{M}_{\text{core,mem}}$, between the Core (+0) and Memory zone (−Y).

The II→III transition is a **topological event**, not merely a linear wave transmission. The transition occurs when the Core amplitude field at the Core-Memory membrane exceeds the **vortex nucleation threshold** in the Memory zone — the energy that must be supplied to create a vortex-antivortex pair and separate one vortex to form the stable Memory zone vortex.

The field at the Core-Memory membrane:

$$
\Phi_{\text{core,mem}} = \Phi_{B,c}e^{i\omega t}\left[1 + A_{\text{core,mem}}e^{ik_c r}\right]
$$

(propagating outward from the Core center toward the Memory zone). The Memory zone field at the membrane:

$$
\Phi_{\text{mem}}(r,\theta) = \Phi_{B,m}e^{i\omega t}\left[1 + f(r)e^{i n_{\text{wind}}\theta}\right]
$$

(vortex ansatz, where $f(r) \to 0$ as $r \to 0$ and $f(r) \to$ const as $r \to R_{\text{mem}}$).

The vortex nucleation condition (from Ginzburg-Landau theory applied to the Memory zone):

$$
\left|\Phi_{\text{core,mem}}\right| > \Phi_{\text{KT}} \equiv \Phi_{B,m}\sqrt{1 - \frac{T_{\text{eff}}}{T_{\text{KT}}}}
$$

When the Core field at the Core-Memory membrane exceeds the KT amplitude $\Phi_{\text{KT}}$, the Memory zone undergoes the KT transition: free vortices spontaneously nucleate and the Memory zone enters the topologically ordered phase ($T_{\text{eff}} < T_{KT}$, single stable vortex present).

The **vortex nucleation action** (the Euclidean action for vortex pair creation in the Memory zone):

$$
S_{\text{nucleate}} = \frac{\pi D_m\Phi_{B,m}^2}{T_{\text{eff}}}\ln\!\left(\frac{R_{\text{mem}}}{\xi}\right) - \frac{\pi}{2}\mu_{\text{chem}}
$$

(the vortex energy minus the chemical potential driving nucleation, normalized by $T_{\text{eff}}$). When $S_{\text{nucleate}} < 0$ (the chemical potential term dominates): nucleation is spontaneous. This occurs when:

$$
\mu_{\text{chem}} > 2D_m\Phi_{B,m}^2\ln(R_{\text{mem}}/\xi) = 2E_{\text{vortex,half}}
$$

The II→III transition is therefore driven by the **chemical potential of the Core field** at the Core-Memory membrane — it triggers vortex nucleation when the Core amplitude exceeds the KT threshold.

---

## Transition III→IV: Junction Vortex Formation

**Interface:** $\mathcal{M}_{\text{mem,core}}$ (same as above, reverse direction).

The III→IV transition is a **reverse membrane coupling** event: the Memory zone vortex (established in III) drives a phase winding back through the Core-Memory membrane, inducing a junction vortex.

The junction vortex formation condition: the Memory zone vortex phase winding $e^{i\chi\theta}$ at the Core-Memory membrane must exceed the junction threshold — the amplitude of the phase winding that the Core can accommodate without phase slip:

$$
|\nabla_\theta\arg\Phi_{\text{mem}}|\Big|_{\mathcal{M}} = \frac{\chi}{r_{\text{junc}}} > k_{\text{junc,thresh}} = \frac{1}{\xi_c}
$$

(the phase gradient at the membrane must exceed the inverse coherence length for the junction vortex to form). When this condition is met, the Core field acquires a vortex:

$$
\Phi_{\text{core}}(\mathbf{r}) = \Phi_{B,c}\frac{r}{\sqrt{r^2 + \xi_c^2}}\exp(i\chi\theta)\exp(i\omega_B t)
$$

The **junction vortex formation action**:

$$
S_{\text{junction}} = \frac{E_{\text{junc}}}{T_{\text{eff}}} = \frac{\pi\sigma_{\text{mem,core}}\xi^2\ln(r_{\text{core}}/\xi)}{T_{\text{eff}}}
$$

The junction vortex forms spontaneously when $S_{\text{junction}} < 0$ (at low effective temperature) or by thermal fluctuation when $S_{\text{junction}} \sim 1$. For $T_{\text{eff}} \ll E_{\text{junc}}$: the junction forms spontaneously (zero action barrier — it is the energetically preferred state once the Memory vortex exists).

**Physical interpretation:** The junction vortex formation is the ICHTB analog of a **Josephson junction** (Josephson 1962). The Core-Memory membrane acts as the weak link; the Memory vortex provides the phase difference; the Core carries the resulting supercurrent. The junction vortex is the topological defect associated with the quantized phase slip across the junction.

---

## Transition IV→V: Core-to-Apex Membrane Lock

**Interface:** $\mathcal{M}_{\text{core,apex}}$, between the Core (+0) and Apex (+Z) zone.

The IV→V transition is the **Apex phase lock** — the Core's temporal oscillation at $\omega_B$ drives through the Core-Apex membrane and establishes full coherence in the Apex zone.

The Core-Apex coupling equation (derived from the Apex zone dynamics, section 13.2):

$$
\frac{d\psi_{\text{apex}}}{dt} = -i\langle E_{\text{bind}}\rangle\psi_{\text{apex}} - \Delta\omega\,\psi_{\text{apex}} + K_{\text{core,apex}}\Phi_{\text{core,apex}}
$$

where $\Phi_{\text{core,apex}} = \Phi_{\text{core}}|_{\mathcal{M}_{\text{core,apex}}}$ is the Core field amplitude at the Core-Apex membrane, and $K_{\text{core,apex}}$ is the coupling constant.

The Apex phase lock occurs when $T_{\text{obj}} = |\psi_{\text{apex}}|/\Phi_{B,\text{apex}} \to 1$. Setting $d\psi_{\text{apex}}/dt = 0$ (lock condition):

$$
\psi_{\text{apex}}^{(\text{lock})} = \frac{K_{\text{core,apex}}\Phi_{\text{core,apex}}}{i\langle E_{\text{bind}}\rangle + \Delta\omega}
$$

The lock amplitude:

$$
T_{\text{obj}}^{(\text{lock})} = \frac{K_{\text{core,apex}}|\Phi_{\text{core,apex}}|}{\Phi_{B,\text{apex}}\sqrt{\langle E_{\text{bind}}\rangle^2 + \Delta\omega^2}}
$$

Full lock ($T_{\text{obj}} = 1$) requires:

$$
K_{\text{core,apex}}|\Phi_{\text{core,apex}}| \geq \Phi_{B,\text{apex}}\sqrt{\langle E_{\text{bind}}\rangle^2 + \Delta\omega^2}
$$

This is the **lock condition** for the IV→V transition: the Core-Apex coupling must be strong enough to drive the Apex to full amplitude despite the detuning $\Delta\omega$ from the natural Apex frequency. The minimum Core amplitude at the Core-Apex membrane for full lock:

$$
|\Phi_{\text{core,apex}}|_{\text{min}} = \frac{\Phi_{B,\text{apex}}\sqrt{\langle E_{\text{bind}}\rangle^2 + \Delta\omega^2}}{K_{\text{core,apex}}}
$$

---

## Transition V→VI: Second Membrane Crossing

**Interface:** $\mathcal{M}_{\text{mem,core}}$ (second crossing).

The V→VI transition is the second crossing of the Core-Memory membrane, which occurs when a second vortex nucleates in the Memory zone. The condition for the second vortex nucleation is the same as the first (II→III transition), but now the effective temperature $T_{\text{eff}}$ is reduced because the first vortex has already partially ordered the Memory zone field. The second nucleation action:

$$
S_{\text{nucleate}}^{(2)} = \frac{2\pi D_m\Phi_{B,m}^2}{T_{\text{eff}}}\ln\!\left(\frac{R_{\text{mem}}}{\xi}\right) - \frac{\pi}{2}\mu_{\text{chem}}^{(2)}
$$

(factor of 2 because the second vortex must form at radius $r \sim \xi$ from the first, where the phase gradient from the first vortex is already at maximum). The second vortex forms when $S_{\text{nucleate}}^{(2)} < 0$, requiring a larger chemical potential:

$$
\mu_{\text{chem}}^{(2)} > 4D_m\Phi_{B,m}^2\ln(R_{\text{mem}}/\xi)
$$

(twice the threshold for the first vortex). This is why Region VI composites require higher $\Lambda_{\text{lock}}$ than Region V particles — the second membrane crossing needs more driving amplitude.

