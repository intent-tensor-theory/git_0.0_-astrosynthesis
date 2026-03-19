# 26.2 Landau-Ginzburg Models

## The Landau-Ginzburg Framework

Lev Landau developed the phenomenological theory of phase transitions in 1937 (Landau 1937), identifying the **order parameter** — a field that is zero in the disordered phase and non-zero in the ordered phase — as the central concept. Vitaly Ginzburg extended this to spatially inhomogeneous systems in 1950 (Ginzburg and Landau 1950), producing the **Ginzburg-Landau (GL) theory** for superconductivity — a field theory for the order parameter $\Psi(\mathbf{x})$ with the free energy functional:

$$
\mathcal{F}[\Psi] = \int d^3x \left[ \frac{\hbar^2}{2m^*}|\nabla\Psi|^2 + \alpha(T)|\Psi|^2 + \frac{\beta}{2}|\Psi|^4 \right]
$$

where:
- $\Psi(\mathbf{x})$: the GL order parameter (the superconducting condensate wavefunction)
- $\alpha(T) = a(T - T_c)$: the temperature-dependent coefficient (negative below $T_c$, positive above)
- $\beta > 0$: the nonlinear coupling constant
- $|\nabla\Psi|^2/2m^*$: the gradient energy (kinetic energy of spatial variation)

The GL free energy is minimized by the **uniform order parameter** $|\Psi_0|^2 = -\alpha/\beta = a(T_c - T)/\beta$ (for $T < T_c$) — the condensate density below the superconducting transition.

---

## ICHTB and Landau-Ginzburg: The Identification

The ICHTB NLS field $\Psi(\mathbf{x}, t)$ and its energy functional:

$$
\mathcal{E}[\Psi] = \int d^3x \left[ \frac{\hbar^2}{2m}|\nabla\Psi|^2 + V(\mathbf{x})|\Psi|^2 + \frac{g}{2}|\Psi|^4 \right]
$$

**is** the Ginzburg-Landau free energy functional, with the identification:
- $m^* = m$ (the NLS effective mass)
- $\alpha(T) \to -\mu$ (the NLS chemical potential — negative in the condensed phase, playing the role of $\alpha$ below $T_c$)
- $\beta \to g$ (the NLS nonlinear coupling constant = GL quartic coupling)
- $V(\mathbf{x}) \to 0$ (homogeneous case: no external potential)

The ICHTB is, in fact, a **time-dependent Ginzburg-Landau (TDGL) theory** — the GL theory promoted to a fully dynamical field theory via the NLS equation $i\hbar\partial_t\Psi = (-\hbar^2\nabla^2/2m - \mu + g|\Psi|^2)\Psi$. The NLS equation is the TDGL equation with a specific (conservative, Hamiltonian) time evolution — no dissipation in the equation of motion itself (dissipation enters only through the zone boundary conditions and Apex zone radiation, not through the field equation).

---

## What GL Captures and What It Misses

The GL theory captures the **bulk thermodynamics** of phase transitions — the phase diagram, the order parameter profile, the coherence length $\xi = \hbar/\sqrt{2m|\mu|}$, and the London penetration depth $\lambda_L = \sqrt{m^*c^2/(4\pi n_s e^2)}$ in superconductors. It captures the **vortex solutions** — the GL equation admits vortex solutions with winding number $n \in \mathbb{Z}$, coherence length $\xi$ core size, and logarithmic energy $E_n = \pi n^2 \hbar^2 \rho_s/m \ln(L/\xi)$ (for a vortex in a system of size $L$ with superfluid density $\rho_s$).

What GL does **not** capture:

1. **The zone structure:** GL is a homogeneous theory — the order parameter $\Psi$ is defined globally with a single free energy functional. The ICHTB adds **zone differentiation** — different regions of the excitation carry qualitatively different physical functions (Core = topological anchor, Memory = chirality storage, Expansion = long-range coupling, etc.). GL has no analog of the six-zone architecture.

2. **The stability score $S^*$:** GL describes whether a vortex exists (topological stability) but not *how stable* it is as a function of environmental perturbations, lock energy, and zone integrity. The ICHTB stability score integrates all zone contributions into a single quantitative measure of survival probability.

3. **The box constraint:** GL is defined on an infinite (or periodic) domain. The ICHTB explicitly incorporates the **finite box geometry** — the physical boundary conditions at the Transition zone, the asymptotic behavior as $r \to r_{\text{max}}$, and the zone cascade from Forward (large-scale) to Core (small-scale). The box is not a technical convenience — it is the physical container that defines the ICHTB as a self-contained system.

4. **The Forward zone:** GL has no equivalent of the Forward zone — the zone that carries the phase gradient $\mathbf{k}$ and connects the excitation to external influences (incoming fields, measurements). The Forward zone is the interface between the excitation and its environment; GL treats the environment only as a heat bath (through $T$ in $\alpha(T)$), not as a directed influence.

5. **The Apex zone:** GL has angular momentum in vortex solutions (the phase winds by $2\pi n$ around the core), but does not develop the Apex zone as a distinct region with its own angular dynamics and radiation modes. The ICHTB explicitly identifies the Apex zone's $l(l+1)/R_a^2$ kinetic energy, its coupling to the Memory zone chirality, and its role as the primary energy export channel.

---

## The GL Vortex and the ICHTB Core Zone

In GL theory, the vortex of winding number $n$ has the asymptotic structure:
- $|\Psi(r)| \approx |\Psi_0|\tanh(r/\xi\sqrt{n})$ as $r \to 0$ (amplitude rises from 0 at the core)
- $\arg\Psi = n\phi$ (phase winds $2\pi n$ around the core)
- Core size $\sim n\xi$ (larger winding number = larger core)
- Energy: $E_n = \pi n^2 \hbar^2 \rho_s/m \ln(L/\xi)$ (logarithmic in system size)

The ICHTB Core zone is the $r < \xi_c$ region of the GL vortex — the coherence length core where the amplitude is suppressed below $\Phi_B$. The ICHTB adds:

- **The Core zone lock energy** $\Lambda_{\text{core}} = 2\mu\Phi_B^2 \pi \xi_c^2 h$ (the energy of the amplitude suppression in the core, from the nonlinear term — GL has this but calls it the "condensation energy")
- **The Core activation threshold** $\Lambda_{\text{threshold}}^{(\text{core})} = \sqrt{2}\mu\Phi_B^2$ (the minimum energy required to create a new vortex core — the Higgs mass from section 25.4)
- **The Core zone boundary** $\mathcal{M}_{\text{core-memory}}$ (the zone membrane at $r = \xi_c$ between Core and Memory zones — GL does not identify this as a distinct boundary with its own physical character)

The ICHTB Core zone is not new physics relative to GL — it is the same physics, but **named, functionally characterized, and connected to the full zone architecture** in a way that GL's global treatment obscures.

---

## TDGL and the Dissipative Extension

The **time-dependent Ginzburg-Landau (TDGL) equation** adds phenomenological dissipation to the GL free energy minimization:

$$
\Gamma \frac{\partial\Psi}{\partial t} = -\frac{\delta\mathcal{F}}{\delta\Psi^*} = \left(\frac{\hbar^2\nabla^2}{2m^*} - \alpha - \beta|\Psi|^2\right)\Psi
$$

where $\Gamma$ is a phenomenological relaxation coefficient. This is the **dissipative** (non-Hamiltonian) version of GL — it drives $\Psi$ toward the minimum of $\mathcal{F}$, with no oscillatory behavior.

The NLS equation (ICHTB) is the $\Gamma \to i\hbar$ limit of TDGL — the **non-dissipative** (Hamiltonian) version. In the NLS equation, $\partial_t\Psi \propto -i\delta\mathcal{E}/\delta\Psi^*$ (with factor $i$) rather than $\partial_t\Psi \propto -\delta\mathcal{F}/\delta\Psi^*$ (TDGL). The $i$ makes all the difference: NLS is conservative (energy is conserved), while TDGL is dissipative (free energy decreases monotonically).

The ICHTB recovers dissipation not from the field equation (which is conservative) but from the **zone boundary conditions** — the Apex zone open boundaries (section 24.1) allow energy to flow out, introducing an effective non-Hermitian term in the zone Hamiltonian. This is the ICHTB mechanism for dissipation without TDGL — it is derived from the zone structure rather than postulated as a phenomenological $\Gamma$.

