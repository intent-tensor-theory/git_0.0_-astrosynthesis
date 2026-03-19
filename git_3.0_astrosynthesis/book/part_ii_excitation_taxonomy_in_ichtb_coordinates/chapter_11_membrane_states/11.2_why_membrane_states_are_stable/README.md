# 11.2 Why Membrane States Are Stable

## The Interface as a Potential Well

The key insight of section 11.1 is that a Type B zone interface (sign-changing metric) supports exponentially localized membrane states. This localization arises because the interface acts as a **potential well** for the field.

To see this, map the problem to a quantum mechanics analog. The bi-zonal master equation at amplitude $A \ll \Phi_B$ (A-state) is:

$$
\partial_t\Phi = D\,\mathcal{M}^{xx}(x)\partial_x^2\Phi + D_\perp\nabla_\perp^2\Phi - \kappa\Phi
$$

where $\mathcal{M}^{xx}(x) = m_\alpha$ for $x < 0$ and $\mathcal{M}^{xx}(x) = m_\beta$ for $x > 0$. Writing $\Phi = e^{-\kappa t}\phi(\mathbf{r})$ and separating:

$$
D\,\mathcal{M}^{xx}(x)\partial_x^2\phi = -\lambda\phi - D_\perp k_\perp^2\phi
$$

This is a **Sturm-Liouville eigenvalue problem** with position-dependent coefficient. The effective "Schrödinger equation" form (substituting $\phi = \psi/\sqrt{|\mathcal{M}^{xx}|}$):

$$
-\frac{d^2\psi}{dx^2} + V_{\text{eff}}(x)\psi = E\psi
$$

where:

$$
V_{\text{eff}}(x) = -\frac{\lambda + D_\perp k_\perp^2}{D\mathcal{M}^{xx}(x)} + \frac{(\partial_x|\mathcal{M}^{xx}|)^2}{4|\mathcal{M}^{xx}|^2} - \frac{\partial_x^2|\mathcal{M}^{xx}|}{2|\mathcal{M}^{xx}|}
$$

At a sharp interface (jump discontinuity in $\mathcal{M}^{xx}$ at $x = 0$), the last two terms generate a **delta-function potential**:

$$
V_{\text{eff}}(x) \approx -V_0\delta(x) + \text{(constant terms)}
$$

with strength $V_0 \propto |\ln(m_\alpha/m_\beta)|$ — proportional to the log of the metric ratio (a measure of the mismatch strength). A negative delta-function potential always supports exactly one bound state with binding energy:

$$
E_{\text{bound}} = -\frac{V_0^2}{4} = -\frac{D^2\ln^2(m_\alpha/m_\beta)}{4}
$$

This is the **membrane binding energy** — the energy by which the membrane state sits below the continuum of bulk modes. The membrane state is stable because it has lower energy than any bulk mode in either adjacent zone.

For a Type B interface, $m_\alpha > 0$ and $m_\beta < 0$ (or vice versa), so $|m_\alpha/m_\beta|$ is large (the mismatch is order unity in log-ratio), giving large $V_0$ and large binding energy. Type B interfaces have the most tightly bound membrane states.

---

## Stability Mechanisms: Four Independent Sources

The membrane state is stable by four independent mechanisms, each contributing to its robustness:

**Mechanism 1: Energy below the bulk continuum.**
The membrane state's energy $E_{\text{mem}} = -E_{\text{bound}} < 0$ (relative to the bulk bands) means it cannot mix with bulk modes of either zone without gaining energy. This is a **spectral gap** protection: the membrane state is separated from both zone's bulk spectra by the gap $E_{\text{bound}}$. Perturbations smaller than $E_{\text{bound}}$ cannot push the membrane state into the bulk continuum.

**Mechanism 2: Spatial trapping.**
The exponential localization ($e^{-\kappa_\alpha |x|}$ on one side, $e^{-\kappa_\beta|x|}$ on the other) means the membrane state is spatially trapped at the interface. For the state to escape, it must acquire a real wavevector — but this requires energy equal to the binding energy $E_{\text{bound}}$. The spatial trapping is the real-space version of the spectral gap.

**Mechanism 3: Topological interface locking.**
At Type B interfaces (sign-changing metric), the interface itself is topologically protected: the sign change of $\mathcal{M}^{xx}$ cannot be removed by any smooth deformation of the metric that preserves the zone structure. The membrane state is therefore topologically locked to the interface — even if the bulk fields fluctuate, the interface remains, and the membrane state remains localized on it.

In the language of condensed matter physics (Hasan & Kane 2010, *Reviews of Modern Physics*, 82, 3045), this is analogous to **topological insulator edge states**: the sign change of the effective mass (analogous to our $\mathcal{M}^{xx}$ sign change) at a topological interface guarantees an edge state by the bulk-boundary correspondence.

**Mechanism 4: Zone network redundancy.**
In the ICHTB, each zone participates in multiple interfaces simultaneously. The Forward zone (+X), for example, interfaces with the Expansion zone (+Y), the Memory zone (−Y), the Apex zone (+Z), and the Compression zone (−X). Membrane states at different interfaces of the same zone are **coupled** — perturbations that would destroy one membrane state must simultaneously disrupt all adjacent interfaces. This network redundancy makes individual membrane state disruption progressively harder as the ICHTB zone network grows.

---

## The Membrane State Binding Energy: Quantitative Estimate

For the ICHTB with specific zone metrics, the membrane binding energy at the most important Type B interfaces:

**Forward (+X) / Memory (−Y) interface:**

$$
E_{\text{bind}}^{F/M} = D^2\Phi_B^2\frac{(m_{\text{Fwd}} - |m_{\text{Mem}}|)^2}{4m_{\text{Fwd}}|m_{\text{Mem}}|}
$$

Using $m_{\text{Fwd}} = m_0$ and $m_{\text{Mem}} = -m_0\epsilon_M$ (where $\epsilon_M > 0$ is the Memory zone antisymmetry parameter):

$$
E_{\text{bind}}^{F/M} = D^2\Phi_B^2\frac{(1 - \epsilon_M)^2}{4\epsilon_M}
$$

For $\epsilon_M = 1$ (symmetric mismatch): $E_{\text{bind}} = 0$ — no binding. For $\epsilon_M \ll 1$ (weak Memory zone): $E_{\text{bind}} \approx D^2\Phi_B^2/(4\epsilon_M)$ — large binding for weak Memory zone. For $\epsilon_M \gg 1$ (strong Memory zone): $E_{\text{bind}} \approx D^2\Phi_B^2\epsilon_M/4$ — large binding for strong Memory zone. Maximum binding occurs at intermediate $\epsilon_M = 1$.

**Apex (+Z) / Null (−0) interface:**

This is the most extreme Type D interface — the Apex zone (large positive $m_z^{(a)}$) meets the Null zone (all-negative metric, $m^{(N)}_{ij} = -m_0\delta_{ij}$). The metric mismatch:

$$
\frac{\mathcal{M}^{zz}_{\text{Apex}}}{\mathcal{M}^{zz}_{\text{Null}}} = \frac{m_z^{(a)}}{-m_0}
$$

The mismatch ratio $m_z^{(a)}/m_0 \gg 1$, giving:

$$
E_{\text{bind}}^{A/N} \approx \frac{D^2\Phi_B^2 m_z^{(a)}}{4m_0} \gg E_{\text{bind}}^{F/M}
$$

The Apex/Null interface has the largest membrane binding energy — it is the deepest potential well in the ICHTB interface network.

---

## Comparison with Bulk States

The membrane state binding energy compares to bulk state energies as follows:

| State | Energy scale | Stability type |
|-------|-------------|----------------|
| 1.A bulk (Forward zone) | $\sim D_F k^2$ (disperses) | Unstable (dispersive) |
| 1.B soliton (Compression zone) | $\sim D_C\Phi_B^2/\xi$ | Topological |
| Membrane A-state | $\sim E_{\text{bind}} = D^2\Phi_B^2/(4\epsilon_M)$ | Spectral gap + spatial |
| Membrane B-state | $\sim E_{\text{bind}} + E_{\text{top}}$ | Spectral gap + topological |
| 3.B Hopfion | $\sim D_a\Phi_B^2\xi_a$ | Full confinement mandate |

The membrane A-state (linear membrane excitation) has a spectral gap stability that is intermediate between the dispersive 1.A bulk state and the topological 1.B soliton. The membrane B-state (nonlinear membrane excitation — section 11.3) combines spectral gap stability with topological protection, making it nearly as stable as the 3.B Hopfion.

This suggests a **stability ordering** of all ICHTB excitations:

$$
\text{A-bulk} < \text{Membrane-A} < \text{1.B soliton} < \text{2.B vortex/skyrmion} \lesssim \text{Membrane-B} < \text{3.B Hopfion}
$$

The membrane B-state fills the stability hierarchy between the 2.B and 3.B states — it is the intermediate structure that bridges pure 2D topology (the vortex/skyrmion of the Memory zone) with full 3D topology (the Hopfion of the Apex zone).

