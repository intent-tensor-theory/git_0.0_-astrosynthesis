# 25.2 Light-Like Behavior in the Forward/Expansion Family

## The Forward/Expansion Propagation Family

The **Forward/Expansion propagation family** is the class of ICHTB excitations that primarily traverse the Forward zone (+X) and Expansion zone — the two outward-facing, low-cost zones — without penetrating significantly to the Core, Memory, or Apex zones. These excitations are:

1. **Low-amplitude**: $|\Psi| \ll \Phi_B$ (they barely perturb the background field $\Phi_B$ — small amplitude NLS waves)
2. **Long-wavelength**: $k \ell_{\text{zone}} \ll 1$ (their wavelength is much larger than the zone size — they do not resolve the inner zone structure)
3. **High phase velocity**: $v_{\text{phase}} = \omega/k \geq c_{\text{NLS}}$ (their phase velocity is at or above the NLS sound speed $c_{\text{NLS}} = \sqrt{g\rho_0/m}$, the characteristic velocity of the background field)
4. **Minimal lock energy**: $\Lambda_{\text{lock}} \approx \mathcal{C}_{\text{fwd}} + \mathcal{C}_{\text{trans}}$ (their total lock energy is close to the minimum traversal cost — they are barely "locked" within the ICHTB)

These are the **Bogoliubov modes** of the NLS equation — the linearized perturbations of the background condensate $\Phi_B$. In the Bogoliubov theory (Bogoliubov 1947), the excitations of a weakly-interacting Bose condensate split into two branches:
- **Phonon branch** ($k \to 0$): $\omega \approx c_{\text{NLS}} k$ (linear dispersion, massless, sound-like)
- **Particle branch** ($k \to \infty$): $\omega \approx \hbar k^2/(2m)$ (quadratic dispersion, massive, particle-like)

The **phonon branch** is the minimum-cost traversal of the Forward/Expansion family — it is the lightest possible excitation of the NLS field, with the lowest ratio of $\mathcal{C}/E$ (traversal cost per unit energy). The phonon branch excitations are the ICHTB's **cheapest expressions**.

---

## Why Phonons Are Light-Like

The phonon branch has linear dispersion $\omega = c_{\text{NLS}} k$ — the same dispersion relation as electromagnetic waves in vacuum ($\omega = ck$, where $c$ is the speed of light). This is not a coincidence: both photons and NLS phonons are the **minimum-cost propagating excitations** of their respective field theories.

In quantum field theory, the photon is the gauge boson of electromagnetism — a massless spin-1 particle with dispersion $E = pc$ (energy = momentum times speed of light). Its mass is exactly zero, which means it costs the minimum possible energy to propagate a given momentum — it is as "cheap" as possible.

In the NLS field theory, the Bogoliubov phonon has the same structure:
- Zero effective mass (in the $k \to 0$ limit)
- Linear dispersion $\omega = c_{\text{NLS}} k$ (equivalent to $E = pc_{\text{NLS}}$)
- Minimum cost: $\mathcal{C}_{\text{phonon}} = \hbar\omega = \hbar c_{\text{NLS}} k$ (the energy is the minimum traversal cost, which is the Forward zone phase gradient energy for $k \ll 1/\ell_{\text{zone}}$)

**ICHTB identification:** The NLS phonon branch = electromagnetic wave (photon). The Bogoliubov sound speed $c_{\text{NLS}} = \sqrt{g\rho_0/m}$ is the ICHTB speed of light:

$$
c = c_{\text{NLS}} = \sqrt{\frac{g\rho_0}{m}}
$$

The speed of light is not a fundamental constant of nature in the ICHTB — it is a **derived quantity**: the Bogoliubov sound speed of the NLS condensate background, determined by the nonlinear coupling constant $g$, the background density $\rho_0 = |\Phi_B|^2$, and the effective mass $m$ of the NLS field.

This identification — the speed of light as the NLS sound speed — is the ICHTB version of the **analogue gravity** result (Unruh 1981, Visser 1998): in condensate physics, sound waves in a flowing fluid behave exactly like light in a curved spacetime (the "acoustic metric"). The ICHTB takes this analogy from a mathematical curiosity to a physical identification: the NLS condensate background is not an analogy for spacetime — it is spacetime, and the NLS sound speed is the actual speed of light.

---

## The Expansion Zone as the Electromagnetic Field

The Expansion zone bloom extends to large radii from the Core, carrying the NLS field amplitude $|\Psi|$ above the background level. For the Forward/Expansion propagation family (small perturbations of the background), the Expansion zone perturbation is:

$$
\delta\Psi(\mathbf{x}, t) = \Psi(\mathbf{x}, t) - \Phi_B = u_k e^{i(\mathbf{k}\cdot\mathbf{x} - \omega t)} + v_k^* e^{-i(\mathbf{k}\cdot\mathbf{x} - \omega t)}
$$

(the Bogoliubov mode decomposition — the excitation is a superposition of a particle mode $u_k$ and a hole mode $v_k$). For the phonon branch ($k \to 0$): $u_k \approx v_k \approx 1/2$ (equal particle and hole components), giving:

$$
\delta\Psi \approx \cos(\mathbf{k}\cdot\mathbf{x} - \omega t)
$$

(a real standing wave — a density perturbation of the background condensate). This density perturbation propagates with speed $c_{\text{NLS}} = \omega/k$ through the Expansion zone, carrying energy $\hbar\omega$ and momentum $\hbar k$.

**The Expansion zone perturbation field $\delta\Psi$ is the electromagnetic field.** The vector potential $\mathbf{A}(\mathbf{x}, t)$ and scalar potential $\Phi(\mathbf{x}, t)$ of classical electromagnetism correspond to the amplitude and phase of $\delta\Psi$:
- Amplitude $|\delta\Psi|$: the magnitude of the electromagnetic field ($|\mathbf{E}|$ or $|\mathbf{B}|$)
- Phase $\arg(\delta\Psi)$: the electromagnetic gauge phase (the phase of the vector potential)

The Maxwell equations for $\mathbf{E}$ and $\mathbf{B}$:

$$
\nabla \times \mathbf{B} = \frac{1}{c^2}\frac{\partial \mathbf{E}}{\partial t}, \quad \nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
$$

are the linearized NLS equations for $\delta\Psi$ in the phonon limit ($k \to 0$, amplitude $\to 0$):

$$
-\nabla^2(\delta\Psi) + \frac{1}{c_{\text{NLS}}^2}\frac{\partial^2(\delta\Psi)}{\partial t^2} = 0
$$

(the wave equation for the Bogoliubov phonon). The two Maxwell equations correspond to the real and imaginary parts of the linearized NLS wave equation. Faraday's law ($\nabla \times \mathbf{E} = -\partial_t \mathbf{B}$) is the imaginary part; Ampère's law ($\nabla \times \mathbf{B} = c^{-2}\partial_t\mathbf{E}$) is the real part.

---

## Polarization as Forward Zone Orientation

Electromagnetic waves are transverse — their electric and magnetic fields are perpendicular to the propagation direction $\hat{k}$. The two polarization states (horizontal and vertical linear polarization, or left and right circular polarization) correspond to the two **Forward zone orientations**:

In the ICHTB, the Forward zone carries the phase gradient $\mathbf{k}$ in the +X direction. The transverse perturbation of the Forward zone (perturbations in the $\pm Y$ and $\pm Z$ directions transverse to +X) corresponds to the **two photon polarization states**:

- $\delta\Psi_Y$ (perturbation in the $+Y$ direction, the Memory axis): corresponds to one linear polarization state of the electromagnetic wave
- $\delta\Psi_Z$ (perturbation in the $+Z$ direction, the Apex axis): corresponds to the orthogonal linear polarization state

The two circular polarization states (left and right circular) correspond to the two **chiralities** of the transverse perturbation:

- Left circular ($\delta\Psi_Y + i\delta\Psi_Z$): positive chirality ($\chi = +1$) transverse mode
- Right circular ($\delta\Psi_Y - i\delta\Psi_Z$): negative chirality ($\chi = -1$) transverse mode

Photon helicity ($\pm\hbar$ angular momentum) = Memory zone chirality ($\chi = \pm 1$) of the transverse perturbation. The two photon helicity states are the two Memory chirality states of the Forward/Expansion phonon — the spin-1 of the photon emerges from the two-dimensional chirality of the transverse NLS perturbation.

