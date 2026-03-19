# 8.1 1.A — Linear: Forward Zone Propagation

## The Simplest Excitation

The 1.A state is the simplest non-trivial excitation of the CTS master equation: a small-amplitude ($A \ll \Phi_B$), one-dimensional, propagating wave confined to the Forward zone (+X). Everything in this section is linear — the nonlinear terms ($-\Lambda(\nabla\Phi)^2$ and $+\gamma|\Phi|^2\Phi$) are negligible at small amplitude, and the master equation reduces to a linear diffusion-advection equation.

The Forward zone is dominated by the operator $\partial_x\Phi$ — a first-order directional derivative along $\hat{x}$. In the full metric:

$$
\mathcal{M}^{ij}_{+X} = \begin{pmatrix} m_x & 0 & 0 \\ 0 & m_\perp & 0 \\ 0 & 0 & m_\perp \end{pmatrix}, \quad m_x \gg m_\perp
$$

The Forward zone metric is strongly anisotropic: the $\hat{x}$ component $m_x$ is large (it amplifies transport along $\hat{x}$) while the transverse components $m_\perp$ are small. This anisotropy makes the Forward zone the directional propagation zone — signals travel along $\hat{x}$ and diffuse only weakly in the transverse directions.

---

## The Linear CTS Equation in the Forward Zone

In the small-amplitude, Forward-zone limit, the master equation becomes:

$$
\partial_t\Phi = D\left[m_x\partial_x^2\Phi + m_\perp(\partial_y^2 + \partial_z^2)\Phi\right] - \kappa\Phi
$$

Define the anisotropy ratio $\eta = m_\perp/m_x \ll 1$. Setting the effective forward diffusivity $D_x = Dm_x$:

$$
\partial_t\Phi = D_x\partial_x^2\Phi + \eta D_x(\partial_y^2 + \partial_z^2)\Phi - \kappa\Phi
$$

For $\eta \to 0$ (perfectly anisotropic Forward zone), the transverse diffusion vanishes and the equation reduces to pure 1D diffusion in $x$ plus damping.

---

## Dispersion Relation

Seeking plane-wave solutions $\Phi = A_0 e^{i(kx + k_\perp r_\perp - \omega t)}$ where $r_\perp = \sqrt{y^2 + z^2}$ is the transverse radius:

$$
-i\omega = -D_x k^2 - \eta D_x k_\perp^2 - \kappa
$$

The **dispersion relation** is:

$$
\omega(k, k_\perp) = iD_x k^2 + i\eta D_x k_\perp^2 + i\kappa
$$

This is purely imaginary — the Forward zone 1.A state is a **purely diffusive mode**: it does not oscillate in time, it only decays (positive imaginary part of $\omega$ means exponential decay in time for the convention $e^{-i\omega t}$). The 1.A signal is not a wave in the traditional sense (no real part of $\omega$) — it is a diffusing pulse.

Wait — this is the Forward zone at rest. If the master equation includes an advective drift (from a non-zero background field $\Phi_0$ in the Apex zone), the dispersion relation acquires a real part:

$$
\omega(k) = v_g k + iD_x k^2 + i\kappa
$$

where $v_g$ is the group velocity set by the Apex zone coupling. In this case, the 1.A signal is a **dispersive wave packet**: it propagates at speed $v_g$ while simultaneously spreading (diffusive broadening $\sim \sqrt{D_x t}$) and decaying ($\sim e^{-\kappa t}$).

The **phase velocity** is $v_\phi = \omega/k = v_g + i(D_x k + \kappa/k)$ — complex, reflecting the simultaneous propagation and decay. The **group velocity** is $\partial\omega/\partial k = v_g + 2iD_x k$ — the imaginary part gives the rate of spreading of the wave packet envelope.

For the general case, the 1.A dispersion relation is written in normalized variables $\tilde{k} = k\xi$, $\tilde{\omega} = \omega\tau = \omega/\kappa$:

$$
\tilde{\omega} = \tilde{v}_g\tilde{k} + i\tilde{k}^2 + i
$$

with $\tilde{v}_g = v_g\tau/\xi = v_g/(D_x\xi^{-1})$ the normalized group velocity. The single dimensionless group $\tilde{v}_g$ controls the character of propagation in the Forward zone.

---

## The Signal Green's Function

The response of the Forward-zone field to a point source perturbation at $(\mathbf{x}_0, t_0) = (0, 0)$ — a delta-function initial condition $\Phi(x, 0) = \Phi_0\delta(x)$ — is the **Green's function** $G(x, t)$:

$$
G(x, t) = \frac{\Phi_0}{\sqrt{4\pi D_x t}}\exp\!\left(-\frac{(x - v_g t)^2}{4D_x t}\right)\exp(-\kappa t)
$$

This is a **Gaussian pulse** that:
1. **Propagates** at speed $v_g$ (the center of the Gaussian moves as $x_c = v_g t$)
2. **Spreads** diffusively (the width grows as $\sigma(t) = \sqrt{2D_x t}$)
3. **Decays** exponentially (the peak amplitude falls as $e^{-\kappa t}/\sqrt{4\pi D_x t}$)

The **signal arrival time** at position $x = L$ (the far end of the Forward zone, at the zone membrane) is $t_{\text{arr}} = L/v_g$. The **signal amplitude at arrival**:

$$
G(L, L/v_g) = \frac{\Phi_0}{\sqrt{4\pi D_x L/v_g}}\exp\!\left(-\frac{\kappa L}{v_g}\right)
$$

The factor $\exp(-\kappa L/v_g)$ is the **attenuation factor**: signals traversing the Forward zone are attenuated by $e^{-\kappa L/v_g}$. For a signal to reach the far membrane without decaying below the noise floor $\Phi_{\text{noise}}$, the zone must satisfy:

$$
L < L_{\max} = \frac{v_g}{\kappa}\ln\!\left(\frac{\Phi_0}{\Phi_{\text{noise}}\sqrt{4\pi D_x/v_g}}\right)
$$

This is the **CTS signal range** — the maximum distance over which a 1.A signal can propagate in the Forward zone before it decays below detectability. It is analogous to the range of a radio signal, the attenuation length of light in a medium, or the mean free path of a particle.

---

## Hardware Logic Gates: The Forward Zone as Signal Processor

The chapter heading uses the phrase "hardware logic gates" for the 1.A state. This warrants explanation.

In the linear regime, the Forward zone supports superposition: if $\Phi_1$ and $\Phi_2$ are both 1.A signals, then $\Phi_1 + \Phi_2$ is also a valid 1.A signal (linearity). This means the Forward zone can carry multiple simultaneous signals without interference. It is the **bus** of the ICHTB — the directional transport layer.

But the Forward zone does more than carry: at the membrane junctions (section 6.2), the transmission conditions filter signals by wavenumber. A membrane with surface conductance $\sigma$ has a transmission coefficient:

$$
T(k) = \frac{4D_x^2k^2}{(2D_xk)^2 + \sigma^2}
$$

Low-$k$ (long-wavelength) components are suppressed (they see a large effective barrier relative to their momentum), while high-$k$ (short-wavelength) components are transmitted. The membrane is a **high-pass spatial filter** — it passes fine detail and attenuates coarse structure.

Combined with the Forward zone's damping (which attenuates high-$k$ components faster, since they decay as $e^{-D_xk^2t}$), the system is a **bandpass filter**: it preferentially transmits intermediate wavenumbers $k \sim 1/\xi$, attenuating both very long and very short wavelengths.

This bandpass behavior is the CTS version of a hardware logic gate: the ICHTB geometry selects which frequency/wavenumber components of a signal are transmitted to the next zone, effectively performing a spatial filtering operation on every signal that passes through the Forward zone. Each membrane junction is a "gate" with its own filter characteristic $T(k; \sigma)$.

A sequence of Forward zone passes through multiple membranes (a multi-zone signal path) applies multiple bandpass filters in series — the result is a shaped, filtered signal whose frequency content has been sculpted by the ICHTB geometry. This is the 1.A state's role in information processing: passive, linear, geometric signal filtering.

---

## Anisotropy and Signal Directionality

The strong anisotropy $m_x \gg m_\perp$ of the Forward zone has a direct consequence: signals propagate much faster along $\hat{x}$ than in any transverse direction. The **anisotropy cone** — the surface at which the signal amplitude has dropped to $1/e$ of its on-axis value — is an oblate ellipsoid:

$$
\frac{(x - v_g t)^2}{2D_x t} + \frac{y^2 + z^2}{2\eta D_x t} = 1
$$

The major axis (along $\hat{x}$) has radius $\sqrt{2D_x t}$; the minor axes (transverse) have radius $\sqrt{2\eta D_x t} \ll \sqrt{2D_x t}$. The signal is **beam-like**: it remains focused along $\hat{x}$ and spreads only slowly in the transverse directions.

This is the geometric explanation for why the Forward zone is the "signal zone" — the metric anisotropy makes signals directional by construction. There is no need to impose boundary conditions to keep a signal on-axis; the zone metric does it automatically.

In contrast, in the Expansion zone (+Y) where the metric is isotropic ($m_x = m_y = m_z = m_{\text{Exp}}$), the signal spreads equally in all directions — the Gaussian blob is spherical, not ellipsoidal. The transition from Forward zone to Expansion zone is the transition from beam-like directional propagation to isotropic bloom — exactly the 1.A-to-2.A transition described in section 7.3.

