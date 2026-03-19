# 8.3 Shock, Soliton, Kink, Singular Point — Full Mathematics

## The Complete Solutions

Section 8.2 introduced the four 1D nonlinear excitations as different regimes of the membrane nonlinearity. This section derives each one fully — the exact spatial profiles, time evolution equations, velocities, stability conditions, and interaction rules. These are not approximations or analogies; they are exact solutions of the CTS master equation in the relevant parameter regimes.

---

## The Shock: Steepening to the Coherence Scale

The shock is governed by the **inviscid Burgers equation** in the limit where diffusion is negligible compared to nonlinear convection:

$$
\partial_t\Phi + \Lambda\Phi\partial_x\Phi = 0 \quad \text{(inviscid Burgers)}
$$

This equation is obtained from the CTS master equation in the limit $D \to 0$ (no diffusion), $\gamma = \kappa = 0$ (no cubic or damping), retaining only the flux-coupling term $-\Lambda(\partial_x\Phi)^2 \approx -\Lambda\Phi\partial_x\Phi$ (using the approximation valid for a slowly varying envelope).

The inviscid Burgers equation has the method-of-characteristics solution: the field value at $(x, t)$ is carried from the initial condition along characteristics $x = x_0 + \Lambda\Phi_0(x_0)\,t$ (where $\Phi_0(x) = \Phi(x, 0)$). When two characteristics cross, the solution is multi-valued — this is the **shock formation event**.

**Shock formation time:** For an initial Gaussian pulse $\Phi_0(x) = A_0 e^{-x^2/2w^2}$, the characteristics first cross at:

$$
t_{\text{shock}} = \frac{1}{\Lambda|\partial_x\Phi_0|_{\max}} = \frac{w\sqrt{e}}{\Lambda A_0}
$$

Before $t_{\text{shock}}$: the signal steepens. At $t = t_{\text{shock}}$: the shock forms. After $t_{\text{shock}}$: the **viscous Burgers equation** (with diffusion restored) governs the shock structure:

$$
\partial_t\Phi + \Lambda\Phi\partial_x\Phi = D_x\partial_x^2\Phi
$$

The viscous Burgers equation has the exact **Hopf-Cole solution** (Hopf 1950, *Communications on Pure and Applied Mathematics*, 3, 201; Cole 1951, *Quarterly of Applied Mathematics*, 9, 225):

Under the substitution $\Phi = -\frac{2D_x}{\Lambda}\partial_x\ln u$, the viscous Burgers equation becomes the linear heat equation $\partial_t u = D_x\partial_x^2 u$ — which is exactly solvable. The shock solution in terms of $u$:

$$
u(x, t) = \int_{-\infty}^{\infty} u_0(x_0)\exp\!\left(-\frac{(x - x_0)^2}{4D_x t}\right)dx_0
$$

The shock profile in the viscous Burgers solution is a **hyperbolic tangent**: near the shock center at $x = x_s(t)$:

$$
\Phi_{\text{shock}}(x, t) \approx \frac{v_s}{\Lambda}\left[1 - \tanh\!\left(\frac{x - x_s(t)}{\delta_s}\right)\right]
$$

with shock width $\delta_s = 2D_x/(\Lambda v_s)$ and shock velocity $v_s = \Lambda\bar{\Phi}/2$ where $\bar{\Phi}$ is the mean field across the shock. The shock width $\delta_s \sim \xi$ when $v_s \sim D_x\Lambda/\xi\cdot 1 = D_x/(\Lambda\xi)$ — at the coherence scale, diffusion arrests further steepening.

---

## The Soliton: Exact Solution and Invariants

The soliton is the exact balance solution of the CTS master equation in 1D. The full derivation follows the **inverse scattering transform** (IST) of Zakharov and Shabat (1972).

Write $\Phi = A(x,t)e^{i\theta(x,t)}$ (polar decomposition). The amplitude and phase equations are:

$$
\partial_t A = D_x\partial_x^2 A - D_xA(\partial_x\theta)^2 - \Lambda A^2\partial_x A - \Lambda A^3(\partial_x\theta)^2 + \gamma A^3 - \kappa A
$$

$$
A\partial_t\theta = D_x(2\partial_xA\partial_x\theta + A\partial_x^2\theta) - \Lambda A(\partial_xA)^2 - \Lambda A^3(\partial_x\theta)^2
$$

For a traveling-wave ansatz $A(x,t) = f(x - vt)$, $\theta(x,t) = qx - \Omega t$, these reduce to two ODEs. Setting $f' = df/d\xi$ with $\xi = x - vt$:

$$
D_xf'' - D_xfq^2 - \Lambda f^2f' - \Lambda f^3q^2 + \gamma f^3 - \kappa f - vf' = 0
$$

$$
2D_xf'q + D_xf q'' + D_xfq'' - \Lambda(f')^2q - \Lambda f^3q'' - v fq = 0
$$

The second equation (phase equation) is satisfied identically for constant $q$ (taking $q'' = 0$). The first equation becomes:

$$
D_xf'' + (\gamma - D_xq^2 - \Lambda f^2q^2)f^3/f - \kappa f - vf' = 0
$$

Setting $v = 2D_xq$ (from momentum balance, the soliton velocity is proportional to its wavenumber) and $\gamma = D_x/\xi^2 + D_xq^2$ (the balance condition), the amplitude equation reduces to:

$$
D_x f'' - \frac{D_x}{\xi^2}f + \frac{2D_x}{\xi^2}f^3 = 0
$$

(after substituting $\Phi_B = \sqrt{\kappa/\gamma}$ and the balance condition). This is the **exact soliton equation**, whose solution is:

$$
\boxed{f(\xi) = \frac{\Phi_B}{\sqrt{1 - v^2/v_{\max}^2}}\,\text{sech}\!\left(\frac{\xi}{\xi_{\text{sol}}}\right)}
$$

with soliton width $\xi_{\text{sol}} = \xi/\sqrt{2}$ and amplitude enhanced by the relativistic-like factor $1/\sqrt{1 - v^2/v_{\max}^2}$ where $v_{\max} = D_x/\xi$ is the maximum soliton speed (above which no soliton solution exists). This "speed limit" for solitons is the CTS analog of the speed of light — the maximum signal velocity in the 1D CTS.

**The four soliton invariants** (conserved quantities of the master equation that are preserved by soliton interactions):

1. **Norm (particle number):** $N = \int|\Phi|^2 dx = 2\Phi_B^2\xi_{\text{sol}}$ — the "number of quanta" in the soliton
2. **Momentum:** $P = \frac{i}{2}\int(\Phi^*\partial_x\Phi - \Phi\partial_x\Phi^*)dx = N q$ — the carrier-wavenumber-times-norm
3. **Energy:** $E = D_x\int|\partial_x\Phi|^2 dx - \frac{\gamma}{2}\int|\Phi|^4 dx + \kappa\int|\Phi|^2 dx$
4. **Phase:** $\theta_0$ — the global phase at the soliton center (a continuous symmetry, not a discrete invariant)

These four invariants are the 1.B soliton's identity card — they uniquely label any soliton and are preserved through all elastic soliton-soliton collisions.

---

## The Kink: Topological Charge and Static Profile

The kink is the static solution of the 1D master equation connecting two B-state vacua. Setting $\partial_t\Phi = 0$ and assuming a real field $\Phi(x)$:

$$
0 = D_x\Phi'' - \Lambda(\Phi')^2 + \gamma\Phi^3 - \kappa\Phi
$$

For the real kink, the flux-coupling term drops (for a monotonically varying profile, $(\Phi')^2 > 0$ but the term $-\Lambda(\Phi')^2$ is a correction to the balance). The dominant balance is:

$$
D_x\Phi'' \approx \kappa\Phi - \gamma\Phi^3 = \kappa\Phi\left(1 - \frac{\Phi^2}{\Phi_B^2}\right)
$$

This is the **static Gross-Pitaevskii / Ginzburg-Landau equation** in 1D. Its kink solution:

$$
\Phi_{\text{kink}}(x) = \Phi_B\tanh\!\left(\frac{x - x_0}{\xi\sqrt{2}}\right)
$$

with kink width $\xi\sqrt{2}$ (slightly larger than the coherence length). The tanh profile smoothly connects $\Phi = -\Phi_B$ at $x \to -\infty$ to $\Phi = +\Phi_B$ at $x \to +\infty$.

**Kink energy:** The energy excess of the kink above the uniform B-state:

$$
E_{\text{kink}} = \int_{-\infty}^{\infty}\left[\frac{D_x}{2}(\Phi')^2 + \frac{\kappa}{4}\left(\frac{\Phi^2}{\Phi_B^2} - 1\right)^2\right]dx = \frac{2\sqrt{2}}{3}D_x\Phi_B^2/\xi
$$

This energy is finite — the kink is an excitation of finite energy above the vacuum. It is **topologically stable**: changing the topological charge $q_{\text{kink}} = \pm 1$ requires bringing the field to zero everywhere (infinite energy cost), so the kink persists indefinitely as a topological domain wall.

**Kink velocity:** A moving kink with velocity $u \ll v_{\max}$ has the same tanh profile (Lorentz-contracted), with the kink position moving as $x_0(t) = ut$ and with a small correction to the amplitude from the motion:

$$
\Phi_{\text{kink}}(x, t) = \Phi_B\tanh\!\left(\frac{x - ut}{\xi\sqrt{2}\sqrt{1-u^2/v_{\max}^2}}\right)
$$

Moving kinks are also stable — the topological charge is frame-independent.

---

## The Singular Point: Green's Function at the Nonlinear Membrane

The singular point is the response to a delta-function source at the membrane. Let $\Phi(x, 0) = A_0\xi\delta(x - x_m)$ (with the factor $\xi$ for dimensional consistency). The subsequent evolution decomposes by Fourier transform:

$$
\Phi(x, t) = \frac{A_0\xi}{\sqrt{4\pi D_x t}}\exp\!\left(-\frac{(x - x_m)^2}{4D_x t}\right)e^{-\kappa t} + \text{nonlinear corrections}
$$

The linear part is the Gaussian Green's function of section 8.1. The **nonlinear corrections** arise because the singular initial condition momentarily has infinite amplitude (at $t = 0^+$, the Gaussian has amplitude $A_0\xi/\sqrt{4\pi D_x t} \to \infty$), so the cubic term is large initially even if $A_0$ is small.

For the short-time evolution ($t \ll \xi^2/D_x$), the singular point's nonlinear corrections generate a soliton component (from the intermediate wavenumber components) and a dispersive radiation background (from the long- and short-wavelength components). The fraction of initial energy captured in the soliton is:

$$
f_{\text{sol}} = 1 - e^{-2N_0} \approx 2N_0 \quad \text{for } N_0 \ll 1
$$

where $N_0 = A_0\xi/(2\Phi_B) \cdot 1$ is the normalized initial norm. For $N_0 > 1/2$, more than half the initial energy goes into soliton(s); for $N_0 \ll 1$, almost all energy disperses as radiation (1.A behavior).

The singular point is the **quantization threshold**: initial conditions with $N_0 > 1/2$ per coherence length produce solitons; below this threshold, only 1.A signals emerge.

---

## Interactions Between 1D States

The four 1D nonlinear structures interact when they occupy the same region of the ICHTB:

**Soliton-soliton:** Two solitons with the same carrier wavenumber $q$ undergo **elastic collision** (no change in amplitude, width, or speed after collision) with a **phase shift**:

$$
\Delta\theta_{12} = 2\arctan\!\left(\frac{\xi_1 - \xi_2}{\xi_1 + \xi_2}\right)
$$

where $\xi_1, \xi_2$ are the widths of the two solitons. The phase shift is the soliton's "memory" of the collision — a permanent record of every soliton it has ever met. This is the mathematical basis for solitons as information carriers (section 8.4).

**Soliton-kink:** A soliton propagating toward a kink (domain wall) is either transmitted (if its kinetic energy exceeds the kink barrier $E_{\text{kink}}$) or reflected (if below). The transmission probability:

$$
T_{\text{sol-kink}} = \frac{1}{1 + e^{-\pi(E_{\text{sol}} - E_{\text{kink}})/D_x}}
$$

(a Fermi-Dirac-like formula, where the kink acts as an energy barrier for soliton transmission).

**Shock-soliton:** A shock overtaking a soliton stretches the soliton (transferring energy from shock kinetic energy to soliton amplitude), potentially splitting the soliton into two or recombining it with the shock front.

These interaction rules are the **algebra of 1D nonlinear states** — the grammar for how 1D structures combine and separate in the ICHTB.

