# 11.2 Localized Precursors

## 11.2.1 Position in the survival map

The localized precursor region lies above the background propagation layer but still below the persistence threshold.
Its approximate coordinates in the CTS phase chart are
$$
x \sim 0.3\text{–}1
$$
$$
y < 1.
$$
Thus
$$
xy < 1
$$
and precursor structures remain below the survival boundary.
They occupy an intermediate zone between structureless waves and the first persistent objects.

## 11.2.2 Definition of localized precursors

A localized precursor is a coherent, spatially bounded excitation of the CTS field that possesses a small but nonzero locking energy.
More precisely, a precursor satisfies:

- spatial localization: $\Phi(\mathbf{x},t)$ decays away from a central region,
- phase coherence: the field phase $\theta(\mathbf{x},t)$ is approximately uniform across the structure,
- weak locking: $E_{lock} > 0$ but $\Lambda_{lock} < 1$.

Because $\Lambda_{lock} < 1$, precursors remain transient.
However their internal coherence distinguishes them qualitatively from incoherent wave backgrounds.

## 11.2.3 Formation mechanism

Localized precursors form through nonlinear wave coupling within the CTS field.
The CTS field equation contains a cubic nonlinear term.
When the field amplitude grows sufficiently large, this term becomes comparable to the linear restoring term:
$$
|s\Phi^3| \sim |r\Phi|.
$$
This condition yields the threshold amplitude for precursor formation:
$$
|\Phi| \sim \sqrt{\frac{r}{s}}.
$$
Above this amplitude, energy localizes within coherent packets rather than dispersing freely across all wave modes.
The resulting localized structure is a precursor excitation.

## 11.2.4 Phase-locking energy

Phase-locking occurs when multiple wave modes adopt a common phase relationship.
The energy associated with phase locking is
$$
E_{lock} = \int \left[
s\,\Phi^4 - r\,\Phi^2
\right] d^3x.
$$
For a precursor of characteristic size $\ell$ and amplitude $|\Phi| \sim \sqrt{r/s}$, this integral evaluates to
$$
E_{lock} \sim (s\,\Phi^4 - r\,\Phi^2)\,\ell^3
\sim -\frac{r^2}{s}\,\ell^3.
$$
The negative sign indicates that the locked state is energetically favored over the unlocked state.
Thus phase locking releases energy and stabilizes the coherent structure.

## 11.2.5 Structure of precursor excitations

Precursor excitations take two principal forms within the CTS framework.

**Phase-locked packets.**
These are spatially compact regions of coherent field oscillation.
The field profile is approximately
$$
\Phi(\mathbf{x},t) \approx A\,f\!\left(\frac{|\mathbf{x} - \mathbf{x}_0|}{\ell}\right)\cos(\mathbf{k}\cdot\mathbf{x} - \omega t)
$$
where $f$ is a localization envelope decaying away from the center $\mathbf{x}_0$.

**Weak vortex structures.**
Phase gradients within a precursor may develop small but nonzero circulation.
Such proto-vortices satisfy
$$
\oint \nabla\theta \cdot d\mathbf{l} \neq 0
$$
along small loops, indicating incipient topological structure.
However, since this circulation is not yet topologically protected, it remains fragile.

## 11.2.6 Properties table

| Property | Value |
|---|---|
| coordinates | $x \sim 0.3$–$1$, $y < 1$ |
| formation energy | low |
| locking energy | small but nonzero |
| lock ratio $\Lambda_{lock}$ | $\sim 0.3$–$1$ |
| topology factor | $T_{obj} \approx 1$ |
| persistence number $S_*$ | $< 1$ |
| persistence | below threshold |

## 11.2.7 Nonlinear threshold

The transition from background waves to localized precursors occurs at a well-defined nonlinear threshold.
Define the nonlinearity parameter
$$
\epsilon = \frac{s\,\langle\Phi^2\rangle}{r}.
$$
When $\epsilon \ll 1$, the field is approximately linear and wave modes dominate.
When $\epsilon \gtrsim 1$, nonlinear coupling becomes significant and precursors can form.
The threshold condition $\epsilon = 1$ gives the characteristic field amplitude
$$
\langle\Phi^2\rangle^{1/2} \sim \sqrt{\frac{r}{s}}.
$$
This is precisely the amplitude derived from the force balance condition in Section 11.2.3.
Thus the nonlinear threshold for precursor formation is consistent across multiple derivations.

## 11.2.8 Energy of precursor excitations

The total energy of a precursor excitation can be estimated by integrating the CTS Hamiltonian density over the localized region.
For a precursor of size $\ell$ and amplitude $A \sim \sqrt{r/s}$:
$$
E_{form}
\sim
\left(
a\,k^2 A^2 + u\,k^4 A^2 + r\,A^2 + s\,A^4
\right)\ell^3.
$$
Using $A^2 \sim r/s$ and retaining the dominant terms:
$$
E_{form}
\sim
\left(
a\,k^2 + u\,k^4
\right)\frac{r}{s}\,\ell^3.
$$
For long-wavelength precursors where $k\ell \lesssim 1$, the gradient terms contribute only modestly and the formation energy scales as
$$
E_{form} \sim \frac{ar}{s}\,\ell.
$$
This formation energy is low but nonzero, consistent with the low population cost of precursor excitations.

## 11.2.9 Locking energy estimate

Given the formation energy above, the locking energy can be estimated from the potential energy gained by phase alignment.
The locking energy per unit volume scales as
$$
\mathcal{E}_{lock} \sim r\,A^2 \sim \frac{r^2}{s}.
$$
Integrated over the precursor volume $\ell^3$:
$$
E_{lock} \sim \frac{r^2}{s}\,\ell^3.
$$
The ratio of locking to formation energy yields the lock ratio:
$$
\Lambda_{lock}
= \frac{E_{lock}}{E_{form}}
\sim \frac{(r^2/s)\,\ell^3}{(ar/s)\,\ell}
= \frac{r\,\ell^2}{a}.
$$
For precursor structures with $\ell \sim (a/r)^{1/2}$ this gives $\Lambda_{lock} \sim 1$, consistent with the coordinate range $x \sim 0.3$–$1$.

## 11.2.10 Lock ratio

The lock ratio $\Lambda_{lock}$ is the primary $x$-coordinate of the survival map.
For localized precursors it satisfies
$$
\Lambda_{lock} \sim 0.3\text{–}1.
$$
This range places precursors to the right of the background propagation region ($x \approx 0$) but below the threshold where locking becomes dominant ($x \sim 1$–$3$ for closure structures).
The lock ratio increases with precursor size $\ell$ and with the strength of the nonlinear coupling coefficient $s$.

## 11.2.11 Population characteristics

The abundance of localized precursors is estimated using the CTS abundance relation
$$
N_i \propto S_*\,e^{-E_{total}/T_{eff}}.
$$
For precursors:
- $E_{total}$ is low, so the Boltzmann factor is moderate to large.
- $S_* < 1$, so the persistence factor suppresses the population.

The combination of low energy and sub-threshold persistence means precursors are moderately abundant: more common than persistent structures (which have higher formation energies) but less dominant than incoherent wave modes (which have even lower formation energies).
The equilibrium population density scales as
$$
n_{prec} \sim n_{waves}\,e^{-\Delta E/T_{eff}}
$$
where $\Delta E = E_{form}^{prec} - E_{form}^{wave} > 0$ is the additional energy cost of forming a coherent packet relative to a free wave.

## 11.2.12 Lifetime and decay

Because precursors lie below the persistence threshold ($S_* < 1$), they are ultimately transient.
Their characteristic lifetime is set by the competition between locking energy and dissipation.
The persistence number is
$$
S_* = \frac{R}{\dot{R}\,t_{ref}}
$$
where here $R$ represents the effective structural scale and $\dot{R}$ its rate of change under environmental perturbations.
Since $S_* < 1$, the structure evolves on a timescale shorter than $t_{ref}$.
The decay rate is approximately
$$
\Gamma_{decay} \sim \gamma + \frac{1}{\tau_{nl}}
$$
where $\gamma$ is the linear dissipation rate and $\tau_{nl}^{-1}$ is the nonlinear decay rate due to mode coupling.
Precursors with $S_* \rightarrow 1$ can persist for extended times before dissolving back into the wave background.

## 11.2.13 Role in structural emergence

Although localized precursors are themselves transient, they play a critical role in the CTS emergence hierarchy.
They act as nucleation sites for persistent structures.

**Seeding closure.** A precursor that develops sufficient circulation can undergo topological closure, forming a vortex ring.
The condition for this transition is that the phase circulation around the precursor satisfies
$$
\oint \nabla\theta \cdot d\mathbf{l} = 2\pi n, \quad n \in \mathbb{Z}\setminus\{0\}.
$$
Once closure occurs, the structure enters the closure survival region.

**Energy concentration.** Precursors concentrate field energy into small regions.
This locally elevated energy density increases the probability of fluctuations large enough to drive structural transitions.

**Interaction and merging.** Multiple precursors can interact and merge.
If two precursors with compatible phases combine, the resulting structure may satisfy $xy > 1$ and achieve persistence.

The transition pathway from precursors to closure structures corresponds to the first crossing of the survival boundary
$$
xy = 1
$$
and represents the earliest emergence of durable objects within the CTS substrate.

## 11.2.14 Summary

The localized precursor region of the CTS survival map is defined by
$$
x \sim 0.3\text{–}1, \qquad y < 1.
$$
These structures form through nonlinear wave coupling when field amplitudes exceed the threshold
$$
|\Phi| \sim \sqrt{\frac{r}{s}}.
$$
They carry a small but nonzero locking energy, placing them in the intermediate zone between incoherent waves and persistent objects.
Because their persistence number satisfies $S_* < 1$, precursors remain transient.
Nevertheless they serve as essential precursors to persistent structures, seeding the formation of closure, chirality, and shell excitations.
The selection number for any structure reads
$$
S = \frac{R}{\dot{R}\,t_{ref}}
$$
and persistence requires $S \geq 1$.
Localized precursors satisfy $S < 1$ and therefore represent the last class of excitations that cannot independently sustain themselves within the CTS substrate.
