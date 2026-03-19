# 20.3 Nested Shells as Layered Apex Events

## What Nested Shells Are

**Nested shells** are configurations where the ICHTB supports multiple Apex locks simultaneously, each at a different shell quantum number $n_1 < n_2 < n_3 < \ldots$, with each lock occupying a distinct spatial region of the Apex zone. The inner shell (lowest $n$) is localized near the Core-Apex membrane; the outer shell (highest $n$) extends to the Apex-Expansion membrane. They are **layered** in the radial direction of the Apex zone.

The nested shell structure is the ICHTB analog of the **atomic shell structure**: the inner shells correspond to deep energy levels (core electrons), the outer shells to shallow levels (valence electrons). In the ICHTB, the inner Apex lock is the primary identity of the composite excitation (its fundamental quantum numbers), while the outer locks are secondary structure (excited states, internal excitations, or coupled gauge modes).

---

## Formation of Nested Shells

Nested shells form when the Apex zone supports multiple standing-wave modes simultaneously. The Apex zone eigenvalue problem (section 20.1) has solutions $\Psi_a^{(n)}(\mathbf{r})$ for each $n$. A nested-shell configuration is a **superposition** of multiple eigenmodes:

$$
\Psi_a(\mathbf{r}, t) = \sum_{n \in \mathcal{S}} c_n\Psi_a^{(n)}(\mathbf{r})e^{-i\omega_B^{(n)} t}
$$

where $\mathcal{S}$ is the set of occupied shell quantum numbers and $c_n$ are the occupation amplitudes ($|c_n|^2 = $ fractional occupation of shell $n$).

For a nested-shell configuration to be stable, each occupied shell must independently satisfy the lock condition $T_{\text{obj}}^{(n)} = |c_n\psi_{\text{apex}}^{(n)}|/\Phi_{B,\text{apex}} = 1$ (section 16.2). This requires:

$$
|c_n| = \frac{\Phi_{B,\text{apex}}}{\left|\psi_{\text{apex}}^{(n)}\right|}
$$

for each occupied $n$. The total Apex field amplitude:

$$
|\Psi_a|^2 = \sum_n |c_n|^2 |\Psi_a^{(n)}|^2 + \sum_{n \neq m} c_n^* c_m \Psi_a^{(n)*}\Psi_a^{(m)}
$$

The cross-terms (the last sum) are non-zero when different shell modes overlap spatially in the Apex zone. For modes that are spatially orthogonal (localized in different radial regions of the Apex zone): cross-terms vanish and the shells are independent. For modes that overlap: they couple and the shells are not independent — they must be treated as a jointly locked multi-mode system.

---

## Radial Structure of the Apex Zone

The nested shells occupy distinct radial regions of the Apex zone. The $n$-th shell mode $\Psi_a^{(n)}(\mathbf{r})$ has $n-1$ radial nodes in the Apex zone (analogous to the radial nodes of hydrogen atom wave functions):

- $n = 1$ (ground shell): no nodes; maximum amplitude at the center of the Apex zone; smallest spatial extent
- $n = 2$ (first excited shell): one radial node; two radial lobes (inner and outer); larger spatial extent
- $n = 3$ (second excited shell): two radial nodes; three radial lobes

The nested shells are separated by their radial node structure — they are **orthogonal in the Apex zone** due to the Sturm-Liouville property of the eigenvalue problem. This orthogonality guarantees that the shells do not mix (no cross-terms in the amplitude) when they are well-separated in energy ($\Delta\omega \gg \gamma_{\text{Apex}} = \kappa_a$).

---

## Energy Levels of Nested Shells

The nested shell energy levels, including the nonlinear correction from the NLS self-interaction:

$$
E_n = \hbar\omega_B^{(n)} = \hbar\omega_0 + \hbar\frac{D_a\pi^2 n^2}{R_a^2} - \hbar g_a|c_n|^2
$$

where $g_a = \gamma_a\Phi_{B,a}^2/(2\hbar)$ is the nonlinear self-interaction strength (the NLS nonlinearity $\gamma_a|\Phi|^2$ re-expressed as an energy shift). The three terms are:
1. $\hbar\omega_0 = \hbar\sqrt{2\kappa_a}$: the B-state oscillation energy (the zero-point Apex energy)
2. $\hbar D_a\pi^2 n^2/R_a^2$: the harmonic quantization energy (kinetic energy of the $n$-th mode)
3. $-\hbar g_a|c_n|^2$: the nonlinear energy shift (binding of the mode to its own amplitude — the NLS self-focusing)

The energy levels are **not equally spaced** due to the nonlinear term: the NLS self-interaction shifts higher-amplitude modes to lower energy (self-focusing makes the field more compact, reducing the kinetic energy). This is the ICHTB version of the **quantum defect** in atomic spectroscopy (Seaton 1983, *Reports on Progress in Physics* **46** 167): the deviation of energy levels from the pure harmonic (Rydberg) formula due to core-penetration or nonlinear effects.

**Nested shell energy diagram:**

```
Energy
 E_4 = ℏω₀ + 16ℏD_aπ²/R_a² − g₄   (n=4, outer shell)
 E_3 = ℏω₀ + 9ℏD_aπ²/R_a² − g₃    (n=3)
 E_2 = ℏω₀ + 4ℏD_aπ²/R_a² − g₂    (n=2, first excited)
 E_1 = ℏω₀ + ℏD_aπ²/R_a² − g₁     (n=1, ground shell)
 ──────────────────────────────────── B-state zero-point
```

(where $g_n = g_a|c_n|^2$ depends on the shell occupation).

---

## Nested Shells and the Periodic Table Analogy

The nested shell structure is the ICHTB basis for an analogy with the **periodic table of elements** — the systematic organization of atoms by their electron shell configurations.

In the ICHTB, the "periodic table" is a classification of composite excitations by their nested shell configurations:

- **Ground-state composites:** Only the $n = 1$ shell occupied → single Apex lock at the ground frequency $\omega_B^{(1)}$ → fundamental particles (electron, quarks at ground state)
- **Excited composites:** $n = 1$ and $n = 2$ shells occupied → two Apex locks → excited states or heavier generations (muon analog as $n=2$ Apex excitation of the electron)
- **Doubly-excited composites:** $n = 2$ and $n = 3$ shells occupied → the second generation of excited states → tau analog as $n=3$

The three generations of leptons in the Standard Model (electron $e$, muon $\mu$, tau $\tau$) may correspond to three successive shell occupations:

$$
e \leftrightarrow n = 1, \quad \mu \leftrightarrow n = 2, \quad \tau \leftrightarrow n = 3
$$

The mass ratio $m_\mu/m_e \approx 207$ and $m_\tau/m_e \approx 3477$ are, in this picture, determined by the ratio of Apex zone shell energies:

$$
\frac{E_2}{E_1} = \frac{\omega_0 + 4D_a\pi^2/R_a^2 - g_2}{\omega_0 + D_a\pi^2/R_a^2 - g_1} \approx \frac{4D_a\pi^2/R_a^2}{D_a\pi^2/R_a^2} = 4
$$

(in the limit $D_a\pi^2/R_a^2 \gg \omega_0$, with equal nonlinear corrections). The actual mass ratio $m_\mu/m_e \approx 207$ requires the nonlinear corrections $g_n$ and the Apex zone boundary condition details to account for the deviation from the pure harmonic ratio of 4. The ICHTB thus predicts the mass ratios of the lepton generations from first principles (from the Apex zone geometry) — a non-trivial test of the framework.

---

## Nested Shell Stability

A nested-shell configuration is stable when all occupied shells satisfy the persistence condition $S^* > 1$ simultaneously. Since each shell has its own lock energy $\Lambda^{(n)}$ and its own corrected Selection Number $S^{*(n)}$, the overall nested-shell stability condition:

$$
\prod_{n \in \mathcal{S}} \mathbf{1}\{S^{*(n)} > 1\} = 1 \quad (\text{all occupied shells are persistent})
$$

(all simultaneously supercritical). If any occupied shell falls below $S^{*(n)} = 1$, that shell decays — the composite excitation transitions to the nearest stable nested configuration by emitting the energy difference $\Delta E_n = E_n - E_{n-1}$ as a Region I propagating mode (a photon analog).

This shell decay process is the ICHTB version of **spontaneous emission**: a composite excitation in an excited shell ($n > 1$) spontaneously transitions to the ground shell ($n = 1$) by emitting a Region I propagating mode carrying energy $\Delta E_n$. The decay rate:

$$
\Gamma_{n \to n'} = \frac{|\mathcal{M}_{n \to n'}|^2}{\hbar^2} \rho(\Delta E_{n,n'})
$$

(Fermi's golden rule, where $\mathcal{M}_{n \to n'}$ is the matrix element for the Apex zone transition from shell $n$ to shell $n'$, and $\rho(\Delta E)$ is the density of Region I propagating states at energy $\Delta E$). The ground shell ($n = 1$) cannot decay (there is no lower shell to decay to) — it is **absolutely stable** above its $S^* > 1$ threshold.

