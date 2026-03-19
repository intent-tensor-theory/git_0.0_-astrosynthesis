# 14.1 Derivation from ICHTB Dynamics

## The Central Question of Persistence Mechanics

Chapters 12 and 13 established two key quantities: the retained structure $R$ (how much organized field the ICHTB contains) and the loss rate $\dot{R}$ (how fast that structure is being lost). The natural question is: will the ICHTB maintain its structure long enough to complete the collapse process?

The **Selection Number** $S$ answers this question with a single dimensionless quantity:

$$
S = \frac{R}{\dot{R}\,t_{\text{ref}}}
$$

Interpretation: $S$ is the ratio of the current retained structure $R$ to the structure that would be lost in one reference time $t_{\text{ref}}$ at the current loss rate $\dot{R}$. If $S > 1$: the ICHTB retains more than it loses per reference period — it is **supercritical**, persisting and potentially growing. If $S < 1$: it loses more than it retains — **subcritical**, decaying. If $S = 1$: exact balance — the **critical** state.

The reference time $t_{\text{ref}}$ is the externally imposed timescale of the collapse process — the time available for the ICHTB to complete its organizational task before the external drive ends or the collapse window closes. Section 14.2 gives its geometric derivation.

---

## Derivation from the Master Equation

Start from the ICHTB master equation:

$$
\partial_t\Phi = D\sum_{i,j}\mathcal{M}^{ij}(\mathbf{r})\partial_i\partial_j\Phi - \kappa(\mathbf{r})\Phi + f_{\text{nonlin}}[\Phi]
$$

Multiply both sides by $\Phi^*$ and integrate over the ICHTB volume. Using the energy functional of section 12.1:

$$
\frac{dR}{dt} = -2\int_{\text{ICHTB}}\kappa(\mathbf{r})|\Phi|^2\,d^3r + 2\int_{\text{ICHTB}}\text{Re}(\Phi^* f_{\text{nonlin}})\,d^3r + \oint_{\partial\text{ICHTB}}\mathbf{J}^E\cdot d\mathbf{S}
$$

The three terms are:
1. **Dissipation:** $-2\int\kappa|\Phi|^2 d^3r < 0$ — always negative, reduces $R$
2. **Nonlinear gain:** $2\int\text{Re}(\Phi^* f_{\text{nonlin}}) d^3r$ — can be positive (gain) or negative (saturation)
3. **Boundary flux:** $\oint\mathbf{J}^E\cdot d\mathbf{S}$ — can be positive (input from external drive) or negative (loss through boundaries)

Define the net loss rate:

$$
\dot{R} \equiv -\frac{dR}{dt} = 2\int\kappa|\Phi|^2 d^3r - 2\int\text{Re}(\Phi^* f_{\text{nonlin}}) d^3r - \oint\mathbf{J}^E\cdot d\mathbf{S}
$$

Now define the **instantaneous Selection Number**:

$$
S(t) \equiv \frac{R(t)}{\dot{R}(t)\,t_{\text{ref}}}
$$

The time evolution of $S$:

$$
\frac{dS}{dt} = \frac{1}{t_{\text{ref}}}\left(\frac{\dot{R}_{\text{actual}}}{\dot{R}} - \frac{R\ddot{R}}{\dot{R}^2}\right)
$$

where $\dot{R}_{\text{actual}} = -dR/dt$ and $\ddot{R} = d^2R/dt^2$. For a system with steady decay ($\ddot{R} = 0$): $dS/dt = \dot{R}_{\text{actual}}/(\dot{R}t_{\text{ref}}) = -1/t_{\text{ref}} < 0$ — $S$ decreases at rate $1/t_{\text{ref}}$. The interpretation: if the loss rate is constant, $S$ counts down from its initial value $S_0$ to zero in time $t_{\text{ref}}$. Initial $S_0 > 1$ gives $R > 0$ when $t = t_{\text{ref}}$; initial $S_0 < 1$ gives $R = 0$ before $t = t_{\text{ref}}$.

---

## The Selection Equation

The dynamics of $R(t)$ under the combined dissipation, gain, and boundary conditions can be written in a simplified form. For the ICHTB operating near the B-state (the relevant regime for persistence), use the approximation that the field is uniformly at amplitude $\bar{\Phi}$ with $\bar{\Phi}$ evolving slowly:

$$
\frac{d\bar{\Phi}^2}{dt} = 2(\gamma\bar{\Phi}^2 - \kappa)\bar{\Phi}^2 = 2\bar{\Phi}^2\left(\frac{\bar{\Phi}^2}{\Phi_B^2} - 1\right)\kappa
$$

This is the **logistic equation** for $\bar{\Phi}^2$: below $\Phi_B$, the amplitude grows (gain > loss); above $\Phi_B$, it decays (loss > gain). The equilibrium at $\bar{\Phi}^2 = \Phi_B^2$ is the B-state.

For the retained structure $R \propto \bar{\Phi}^2$ (in the homogeneous approximation):

$$
\frac{dR}{dt} = 2\kappa\left(\frac{R}{R_B} - 1\right)R
$$

where $R_B = \int\mathcal{E}(\Phi_B)\,d^3r$ is the retained structure at the B-state. The loss rate:

$$
\dot{R} = -\frac{dR}{dt} = 2\kappa\left(1 - \frac{R}{R_B}\right)R
$$

This is positive (net loss) when $R < R_B$ and negative (net gain) when $R > R_B$. The B-state is the fixed point $\dot{R} = 0$.

The Selection Number in the homogeneous approximation:

$$
S = \frac{R}{\dot{R}\,t_{\text{ref}}} = \frac{R}{2\kappa(1 - R/R_B)R\,t_{\text{ref}}} = \frac{1}{2\kappa(1 - R/R_B)t_{\text{ref}}}
$$

For $R \to R_B^-$ (approaching the B-state from below): $S \to +\infty$ (the ICHTB is about to reach the B-state — infinite persistence in the sense that the loss rate goes to zero). For $R \ll R_B$ (far below B-state): $S \approx 1/(2\kappa t_{\text{ref}})$. The condition $S > 1$ becomes:

$$
S = \frac{1}{2\kappa(1 - R/R_B)t_{\text{ref}}} > 1 \iff t_{\text{ref}} < \frac{1}{2\kappa(1 - R/R_B)}
$$

The ICHTB is supercritical ($S > 1$) when the reference time $t_{\text{ref}}$ is shorter than the time to reach the B-state at the current loss rate — i.e., when the collapse window closes before the ICHTB has time to fully decay. This makes physical sense: a short reference time (rapid collapse) allows less structured ICHTBs to "get away with" less retention, while a long reference time requires higher $S$ to survive the collapse window.

---

## The Universal S Formula

Combining the zone contributions (section 12.1) with the inter-zone coupling (section 12.2) and the anchor effects (section 13.2), the full Selection Number:

$$
S = \frac{\sum_\alpha R_\alpha + R_{\text{membrane}}}{\left(\sum_\alpha\Gamma_\alpha R_\alpha\right)t_{\text{ref}}} = \frac{R}{\bar{\Gamma}R\,t_{\text{ref}}} = \frac{1}{\bar{\Gamma}\,t_{\text{ref}}}
$$

where $\bar{\Gamma} = \dot{R}/R$ is the **effective loss rate** (the $R$-weighted average of zone loss rates):

$$
\bar{\Gamma} = \frac{\sum_\alpha\Gamma_\alpha R_\alpha}{\sum_\alpha R_\alpha}
$$

This is the central result:

$$
\boxed{S = \frac{1}{\bar{\Gamma}\,t_{\text{ref}}}}
$$

The Selection Number is the ratio of the characteristic decay time $\tau_{\text{eff}} = 1/\bar{\Gamma}$ to the reference time $t_{\text{ref}}$:

$$
S = \frac{\tau_{\text{eff}}}{t_{\text{ref}}}
$$

**Supercritical** ($S > 1$): the ICHTB decays slower than the collapse proceeds — it persists. **Subcritical** ($S < 1$): the ICHTB decays faster than the collapse proceeds — it dissolves before completion. **Critical** ($S = 1$): $\tau_{\text{eff}} = t_{\text{ref}}$ — the ICHTB decays on exactly the collapse timescale.

The effective loss rate $\bar{\Gamma}$ is the $R$-weighted average: zones with more retained structure contribute more to the average. Since the anchored zones (Apex, Core) carry most of the retained structure and have the smallest $\Gamma_\alpha$, the effective loss rate $\bar{\Gamma}$ is dominated by the anchor zones, giving:

$$
\bar{\Gamma} \approx \frac{\Gamma_{\text{apex}}R_{\text{apex}} + \Gamma_{\text{core}}R_{\text{core}}}{R_{\text{apex}} + R_{\text{core}}} \approx \Gamma_{\text{apex}} \approx 0 \quad (\text{for 3.B lock})
$$

For the 3.B locked ICHTB: $\bar{\Gamma} \approx \Gamma_{\text{lock}} \approx \kappa e^{-395}$, giving $S \approx e^{395}/(\kappa t_{\text{ref}}) \to \infty$ for any finite $t_{\text{ref}}$. The 3.B lock is always supercritical — always $S \gg 1$.

