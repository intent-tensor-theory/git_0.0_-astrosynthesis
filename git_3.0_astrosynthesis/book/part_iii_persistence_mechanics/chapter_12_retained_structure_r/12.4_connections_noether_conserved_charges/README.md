# 12.4 Connections: Noether, Conserved Charges, Hamiltonian

## The Retained Structure as a Hamiltonian

The retained structure $R$ defined in sections 12.1–12.3 is the ICHTB's **Hamiltonian** — the total energy functional governing the field dynamics. This identification is not merely formal: it makes the entire machinery of Hamiltonian mechanics available for analyzing the ICHTB, and it connects the retained structure directly to the conserved charges guaranteed by Noether's theorem.

The Hamiltonian form of the retained structure:

$$
R[\Phi, \Pi] = \int_{\text{ICHTB}}\left[\frac{|\Pi|^2}{2} + \sum_{i,j}\mathcal{M}^{ij}(\mathbf{r})\partial_i\Phi^*\partial_j\Phi + V(|\Phi|^2, \mathbf{r})\right]d^3r
$$

where $\Pi = \partial_t\Phi^*$ is the canonical momentum conjugate to $\Phi$, and the first term $|\Pi|^2/2$ is the kinetic energy density (absent in the purely dissipative limit but present when the Apex zone's $\partial_t^2\Phi$ term is retained). Hamilton's equations:

$$
\partial_t\Phi = \frac{\delta R}{\delta\Pi^*}, \qquad \partial_t\Pi = -\frac{\delta R}{\delta\Phi^*}
$$

reproduce the ICHTB master equation (section 4.3) in the Hamiltonian formulation — confirming that $R$ is the correct Hamiltonian for the ICHTB dynamics.

---

## Noether's Theorem: Symmetries and Conservation Laws

Every continuous symmetry of the Hamiltonian $R$ gives rise to a conserved quantity (Noether 1918, *Nachrichten der Königlichen Gesellschaft der Wissenschaften zu Göttingen*, 235–257). The ICHTB has several symmetries, each producing a conserved charge:

**1. U(1) phase symmetry: $\Phi \to e^{i\theta}\Phi$**

If the Hamiltonian $R$ is invariant under global phase rotation $\Phi \to e^{i\theta}\Phi$ (which it is, since $R$ depends only on $|\Phi|^2$ and $|\nabla\Phi|^2$, not on $\arg\Phi$ separately), then Noether's theorem gives a conserved charge:

$$
Q = \int_{\text{ICHTB}}\frac{1}{2i}(\Phi^*\partial_t\Phi - \Phi\partial_t\Phi^*)\,d^3r = \int_{\text{ICHTB}}|\Phi|^2\,d^3r
$$

(in the limit where $\partial_t\Phi = i\omega_B\Phi + \ldots$, giving $Q = \omega_B\int|\Phi|^2 d^3r$). This is the **total particle number** or **total charge** of the ICHTB state — identified with the electric charge of the composite excitation (section 11.4). U(1) phase symmetry → charge conservation.

**2. Translational symmetry: $\mathbf{r} \to \mathbf{r} + \mathbf{a}$**

If the ICHTB metric $\mathcal{M}^{ij}(\mathbf{r})$ and potential $V(|\Phi|^2, \mathbf{r})$ are translationally invariant (uniform zones — an idealization), then the conserved charge is the **total momentum**:

$$
\mathbf{P} = -\int_{\text{ICHTB}}\Pi^*\nabla\Phi\,d^3r
$$

In the ICHTB with its zone structure, translational symmetry is broken (each zone has a different metric, and the zone boundaries are at fixed positions). However, within a single zone, translational symmetry holds, and the zone's contribution to the total momentum is a conserved intra-zone momentum. The total momentum is the sum of zone momenta, with corrections for zone-boundary scattering. Translation → momentum conservation (with zone-boundary corrections).

**3. Rotational symmetry: $\mathbf{r} \to \mathbf{R}\mathbf{r}$ (rotation)**

The Apex zone (+Z) has the full rotational symmetry about the $z$-axis (azimuthal symmetry), but not full 3D rotational symmetry (the $z$-axis is distinguished). This $U(1)_{\text{rot}} = SO(2)_z$ symmetry gives the conserved charge:

$$
L_z = \int_{\text{ICHTB}}\Pi^*(x\partial_y - y\partial_x)\Phi\,d^3r
$$

— the $z$-component of **angular momentum**. The full 3D rotational symmetry $SO(3)$ of the Core zone gives all three components of angular momentum ($L_x, L_y, L_z$) as conserved charges within the Core zone. Zone rotational symmetries → angular momentum conservation.

**4. The discrete $\mathbb{Z}_2$ symmetry: $\Phi \to -\Phi$**

The ICHTB master equation has a $\mathbb{Z}_2$ (sign-flip) symmetry: if $\Phi(\mathbf{r}, t)$ is a solution, then $-\Phi(\mathbf{r}, t)$ is also a solution (since the equation contains only odd powers of $\Phi$: the cubic nonlinearity $\gamma|\Phi|^2\Phi$ is odd under $\Phi \to -\Phi$). This discrete symmetry does not give a continuous conserved charge, but it does imply a **conserved parity** — the field configuration can be classified as even ($\Phi = -\Phi$ solutions: $\Phi = 0$, the vacuum) or odd ($\Phi \neq 0$). The topological sectors (characterized by the winding number $n$ or Hopf invariant $H$) are related to this parity: the vacuum ($H = 0$) and the Hopfion ($H \neq 0$) live in different parity sectors.

---

## The Hamiltonian Decomposition of R

The Hamiltonian decomposition of $R$ into zone contributions is directly analogous to the energy decomposition in many-body quantum mechanics:

$$
R = \langle\hat{H}\rangle = \langle\hat{T}\rangle + \langle\hat{V}\rangle + \langle\hat{V}_{\text{int}}\rangle
$$

where $\hat{T}$ is the kinetic energy (gradient terms), $\hat{V}$ is the potential energy (zone-specific potentials), and $\hat{V}_{\text{int}}$ is the inter-zone interaction energy (membrane state contributions).

The **virial theorem** for the ICHTB: for a stationary state (time-independent $\Phi$), the Hamiltonian equations give:

$$
2\langle\hat{T}\rangle = -\langle\mathbf{r}\cdot\nabla V\rangle = d\langle\hat{V}\rangle
$$

where $d$ is the effective dimension of the excitation. This gives:
- For 1D excitations: $2T = V$ → kinetic and potential energies equal (equipartition in 1D)
- For 2D excitations: $T = V$ (same)
- For 3D excitations: $2T = 3V$ — kinetic energy exceeds potential energy by $3/2$

The virial theorem determines the relative contributions of kinetic (gradient) and potential energy to the retained structure $R = T + V$:
- 1D: $R_{1D} = 3V/2$ (gradient terms $= V/2$, potential $= V$)
- 2D: $R_{2D} = 2V$ (gradient $= V$, potential $= V$)
- 3D: $R_{3D} = 5V/3$ (gradient $= 2V/3$, potential $= V$)

For the 3.B Hopfion, these contributions can be evaluated explicitly: the Bogomolny bound $E_H = 4\pi^2 D_a\Phi_B^2\xi_a|H|^{3/4}$ is saturated when the virial condition $2T = 3V$ holds — the Bogomolny Hopfion is the maximum-efficiency packing of retained structure per unit of topological charge.

---

## R as the Interface Between Mathematics and Physics

The retained structure $R$ is more than a technical construct — it is the bridge between the abstract ICHTB geometry (zone metrics, membrane conditions, topological invariants) and the observable physics of the collapse (how long structures persist, how they decay, what signals they emit).

The connections established in this section:
- $R$ is the Hamiltonian → its gradients give the forces and dynamics
- Symmetries of $R$ → Noether charges → physical quantum numbers (charge, momentum, spin)
- Zone decomposition of $R$ → channel decomposition → active channel count $N_{\text{active}}$
- Alignment of zone phases → alignment quality $Q_{\text{align}}$ → total $R$ via coupling efficiency
- Virial theorem → ratio $T/V$ in $R$ → dimension of dominant excitation

These connections will be used throughout Part III to derive the quantitative persistence mechanics — the equations governing how $R$ changes in time, what determines the loss rate $\dot{R}$, and how the selection number $S = R/\dot{R}t_{\text{ref}}$ governs which ICHTB states persist and which decay.

The retained structure $R$ is the ICHTB's central observable — the single number that summarizes everything relevant about the collapse trajectory's capacity to persist and to manifest as detectable structure.

