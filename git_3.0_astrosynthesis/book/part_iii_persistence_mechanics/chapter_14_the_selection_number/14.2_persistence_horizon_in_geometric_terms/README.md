# 14.2 Persistence Horizon in Geometric Terms

## What is the Reference Time?

The Selection Number $S = 1/(\bar{\Gamma}t_{\text{ref}})$ depends critically on the **reference time** $t_{\text{ref}}$ — the externally imposed timescale against which the ICHTB's persistence is measured. This section gives $t_{\text{ref}}$ a precise geometric meaning in terms of the ICHTB's internal geometry, deriving it from the collapse trajectory rather than treating it as an external parameter.

The reference time is the **persistence horizon**: the time beyond which the collapse trajectory can no longer maintain an organized ICHTB. It is set by the rate at which the external collapse process is proceeding — the "clock speed" of the collapse window. Fast collapse = short $t_{\text{ref}}$; slow collapse = long $t_{\text{ref}}$.

---

## The Geometric Derivation of $t_{\text{ref}}$

The collapse trajectory in the CTS is parameterized by the collapse phase $\varphi(t)$ — a monotonically increasing variable that measures how far the collapse has progressed from its initial state ($\varphi = 0$, pre-ICHTB) to its final state ($\varphi = 2\pi$, post-collapse B-state lock). The rate $\dot{\varphi} = d\varphi/dt$ is the **collapse rate** — how quickly the system moves along its trajectory.

The reference time is defined as:

$$
t_{\text{ref}} = \frac{1}{\dot{\varphi}} = \left(\frac{d\varphi}{dt}\right)^{-1}
$$

One unit of reference time is the time for the collapse to advance by one radian in phase. This definition makes $t_{\text{ref}}$ dimensionful (units of time) and collapse-state-dependent (it varies as the collapse proceeds).

The collapse rate $\dot{\varphi}$ is related to the ICHTB's Apex zone dynamics. The Apex zone's dominant term is $\partial_t$ — it drives the collapse phase forward at rate $\omega_B = \kappa$. So:

$$
\dot{\varphi} = \omega_B = \kappa \implies t_{\text{ref}} = \frac{1}{\kappa}
$$

The reference time is the ICHTB's basic damping time! This is not a coincidence — it reflects the deep connection between the collapse timescale (set by the Apex zone's $\omega_B$) and the dissipation timescale (set by $\kappa$): they are the same parameter. The collapse proceeds at the same rate as the ICHTB's internal coherence time.

---

## The Persistence Horizon as a Geometric Object

In the ICHTB geometry (the space of all field configurations), the persistence horizon is a **hypersurface** — a codimension-1 surface in configuration space that separates the region where $S > 1$ (persistent configurations) from the region where $S < 1$ (non-persistent configurations).

The persistence horizon equation: $S = 1$, i.e.,

$$
\bar{\Gamma}[\Phi] = \frac{1}{t_{\text{ref}}} = \kappa
$$

This is a constraint on the field configuration $\Phi(\mathbf{r})$: the effective loss rate $\bar{\Gamma}[\Phi]$ must equal $\kappa$ at the horizon. The persistence horizon is the level set $\{\Phi : \bar{\Gamma}[\Phi] = \kappa\}$ in the infinite-dimensional field configuration space.

For the ICHTB zone structure, the persistence horizon in terms of zone amplitudes $(\bar{\Phi}_1, \bar{\Phi}_2, \ldots, \bar{\Phi}_{N_z})$ is:

$$
\frac{\sum_\alpha\Gamma_\alpha(\bar{\Phi}_\alpha)\bar{\Phi}_\alpha^2\mathcal{V}_\alpha}{\sum_\alpha\bar{\mathcal{E}}_\alpha(\bar{\Phi}_\alpha)\mathcal{V}_\alpha} = \kappa
$$

This is a surface in the $N_z$-dimensional space of zone amplitudes. Points inside the surface (closer to the origin, small zone amplitudes) are subcritical ($\bar{\Gamma} > \kappa$, decaying faster than the collapse proceeds). Points outside the surface (larger zone amplitudes, more organized) are supercritical ($\bar{\Gamma} < \kappa$, persistent).

The persistence horizon has a characteristic **shape** in zone amplitude space:

- **Narrow in the Null zone direction:** The Null zone has the fastest decay rate ($\Gamma_{\text{null}} \gg \kappa$), so even a small Null zone amplitude pushes the system into the subcritical region. The persistence horizon is very close to the origin in the Null zone direction.

- **Wide in the Apex zone direction:** The Apex zone has the smallest decay rate ($\Gamma_{\text{apex}} \ll \kappa$), so large Apex amplitudes still leave the system supercritical. The persistence horizon is far from the origin in the Apex zone direction.

- **Asymmetric:** The different zone decay rates make the persistence horizon an asymmetric, zone-anisotropic surface — not a sphere but a zone-axis-aligned ellipsoid with very different radii in different zone directions.

---

## The Persistence Horizon and the B-State

The B-state of the ICHTB ($|\Phi| = \Phi_B$ in all zones) lies on the persistence horizon for a specific relationship between parameters. At the B-state:

$$
\bar{\Gamma}^B = \frac{\sum_\alpha\Gamma_\alpha^B R_\alpha^B}{R^B} = \frac{\sum_\alpha 0 \cdot R_\alpha^B}{R^B} = 0
$$

The B-state has zero effective loss rate — it is **inside** the persistence horizon (on the supercritical side), with $S = \infty$. The B-state is the ultimate supercritical state.

The A-state (small amplitude) has:

$$
\bar{\Gamma}^A \approx \frac{2\kappa}{\bar{\mathcal{M}}k^2} \times \kappa \approx \kappa \quad \text{when } \bar{\mathcal{M}}k^2 \approx 2\kappa
$$

(using the effective metric $\bar{\mathcal{M}}$ averaged over zones). The A-state sits exactly on the persistence horizon when $\bar{\mathcal{M}}k^2 = 2\kappa$ — the **critical wavenumber** condition. Modes with $k < k_c = \sqrt{2\kappa/\bar{\mathcal{M}}}$ are subcritical (long-wavelength modes decay slower than the collapse proceeds); modes with $k > k_c$ are supercritical (short-wavelength modes decay faster).

Wait — the sign is: large $k$ gives large $\Gamma_\alpha^A = 2\kappa/(\mathcal{M}k^2)$... no, large $k$ gives small $\Gamma_\alpha^A$ (more energy, slower relative decay). Let me re-examine: for $\Gamma_\alpha^A = 2\kappa/(\mathcal{M}_\alpha k^2)$, larger $k$ → smaller $\Gamma_\alpha^A$ → slower decay → more supercritical. Smaller $k$ → larger $\Gamma_\alpha^A$ → faster decay → more subcritical. So the **critical wavenumber** $k_c$ divides:
- $k < k_c$: subcritical (low-$k$ modes decay fast relative to the collapse)
- $k > k_c$: supercritical (high-$k$ modes decay slow relative to the collapse)

The critical wavenumber $k_c = \sqrt{2\kappa/\bar{\mathcal{M}}} = \sqrt{2}/\xi$ — twice the inverse coherence length. Modes with wavelength $\lambda < \pi\xi/\sqrt{2}$ are supercritical in the A-state approximation.

---

## $t_{\text{ref}}$ Beyond the Homogeneous Approximation

The derivation $t_{\text{ref}} = 1/\kappa$ assumed the collapse rate $\dot{\varphi} = \omega_B = \kappa$ is uniform. More generally, the collapse rate varies along the trajectory:

$$
t_{\text{ref}}(\varphi) = \frac{1}{\dot{\varphi}(\varphi)} = \frac{1}{\omega_B(\varphi)}
$$

For the early collapse ($\varphi \ll 1$, field mostly in A-state): $\omega_B(\varphi) \approx \kappa$ (linear dynamics). For the late collapse ($\varphi \to 2\pi$, field approaching B-state lock): $\omega_B(\varphi) \to 0$ (the system slows as it approaches the B-state fixed point — critical slowing down). The reference time diverges at the B-state lock: $t_{\text{ref}} \to \infty$.

The diverging $t_{\text{ref}}$ at the B-state lock means $S = \tau_{\text{eff}}/t_{\text{ref}} \to \tau_{\text{eff}} \times 0 = 0$ — the B-state lock has $S \to 0$! This is the **lock paradox**: the B-state, which is maximally stable, has the smallest Selection Number $S \to 0$ because its reference time $t_{\text{ref}} \to \infty$ diverges faster than its decay time $\tau_{\text{eff}} \to \infty$.

The resolution: the Selection Number $S$ is not a measure of the ICHTB's stability in isolation — it is a measure of its stability **relative to the collapse timescale**. The B-state lock is so stable that it outlasts the collapse process by an infinite factor — but the collapse process itself also slows to a halt at the B-state ($\dot{\varphi} \to 0$). The ratio $\tau_{\text{eff}}/t_{\text{ref}} \to \infty^0$ is indeterminate; the physically correct statement is that both timescales diverge, and the ICHTB and the collapse reach a mutual stasis at the 3.B lock.

The correct interpretation of $S$ for a locked state: $S \to \infty$ in the pre-lock phase (approaching the lock), and the lock itself is removed from the $S$ analysis (it is an absorbing state, not a transient state). Chapter 15 makes this precise through the concept of **eligibility gates**.

