# 3.4 Bloom Shape and Excitation Type

## What "Bloom" Means

The CTS field $\Phi = Ae^{i\theta}$ radiates outward from i₀. The spatial pattern of the amplitude $A(\mathbf{x})$ as it extends through the ICHTB zones is the **bloom** — the shape that the field takes as it fills the volume. Different physical excitations produce different bloom shapes, and the bloom shape directly encodes which zones are active, at what amplitude, and with what coupling across the membranes.

"Bloom" is chosen deliberately over "profile" or "distribution." A bloom opens from a center — it has directionality, asymmetry, and a history of expansion. It is not a static snapshot but the record of how the field opened from i₀ outward. The bloom shape is the CTS field's autobiography written in amplitude and phase across the ICHTB.

---

## Three Dimensional Classes, Two Behavioral Classes

The A/B state taxonomy (Book 1.0, Chapter 8) classifies all CTS excitations into six classes based on two independent criteria:

**Dimensional class** (how many spatial dimensions the excitation occupies):
- **1D**: Field is effectively constant in two directions, varies only along one axis (a rod or ray)
- **2D**: Field varies in two directions, constant (or periodic) in the third (a sheet or disc)
- **3D**: Field varies in all three directions (a volume)

**Behavioral class** (whether the dominant dynamics are linear or nonlinear):
- **A (linear)**: Amplitude small enough that $\gamma\Phi^3 \ll \kappa\Phi$; the CTS master equation linearizes; superposition holds
- **B (nonlinear)**: Amplitude large enough that the cubic term $\gamma\Phi^3$ competes with the linear terms; the field is self-modifying

These combine to give six classes: **1.A, 1.B, 2.A, 2.B, 3.A, 3.B**.

---

## The Bloom Shape of Each Class

### 1.A — Linear Rod

The simplest bloom: a narrow cylinder of activated field extending along a single zone axis (typically Forward, +X).

$$
\Phi_{1.A}(\mathbf{x}) = A_0\,\text{sech}\!\left(\frac{x}{\ell_x}\right)\exp\!\left(-\frac{y^2 + z^2}{2\sigma_\perp^2}\right)e^{i(kx - \omega t)}
$$

Bloom shape: elongated along $\hat{x}$, Gaussian-narrow in $\hat{y}$ and $\hat{z}$. Only the Forward zone is substantially activated. Membrane crossings to Expansion and Memory zones carry minimal energy.

**Example physical analog:** A photon propagating along one axis. The electromagnetic field is a 1.A state — linear, propagating, one-dimensional, governed by the gradient operator in the Forward zone.

### 1.B — Soliton

A nonlinear rod with self-consistent shape stabilized by the balance of dispersion (Forward zone, diffusive spread) and self-focusing (Compression zone, nonlinear pulling):

$$
\Phi_{1.B}(\mathbf{x}) = A_0\,\text{sech}\!\left(\frac{x - v_s t}{\xi_s}\right)e^{i(k_s x - \omega_s t)}
$$

where $\xi_s = \sqrt{2D\mathcal{M}^{xx}/\gamma A_0^2}$ is the soliton width set by the balance between diffusion coefficient $D$ and cubic nonlinearity $\gamma$.

Bloom shape: compact along $\hat{x}$ (not spreading), narrow in transverse directions. Activates both Forward zone (propagation) and Compression zone (focusing) simultaneously. The membrane between +X and −X zones is crossed with significant energy flow — the soliton is sustained by an ongoing exchange between propagation and compression.

**Example physical analog:** A nerve impulse (Hodgkin-Huxley, 1952), a fiber-optic soliton (Hasegawa & Tappert, 1973). These are 1.B states in the CTS taxonomy.

### 2.A — Linear Sheet / Disc

A planar field pattern activated primarily in the Expansion zone (+Y). The field varies in two dimensions and is uniform (or slowly varying) in the third.

$$
\Phi_{2.A}(\mathbf{x}) = A_0\,J_0\!\left(\frac{r_\perp}{\ell_{xy}}\right)e^{i(\mathbf{k}\cdot\hat{\rho} - \omega t)}, \qquad r_\perp = \sqrt{x^2 + y^2}
$$

where $J_0$ is the Bessel function of zeroth order (the natural radially symmetric mode in the Expansion zone).

Bloom shape: disc in the $xy$-plane, Bessel-function radial profile. The Expansion zone (+Y) is primary; the Memory zone (−Y) provides the rotational structure that stabilizes the circular pattern.

**Example physical analog:** A ripple on a 2D surface (water wave in the gravity-wave limit), a 2D plasma oscillation, a cosmic string in the transverse plane.

### 2.B — Vortex Sheet

A nonlinear planar pattern with topological winding — the circulation structure of the Memory zone made manifest in a two-dimensional cross-section.

$$
\Phi_{2.B}(\mathbf{x}) = A_0\,f(r)\,e^{in\phi}, \qquad f(r) \to \begin{cases} 0 & r \to 0 \\ A_0 & r \to \infty \end{cases}
$$

where $f(r)$ is the Abrikosov-Nielsen-Olesen vortex profile satisfying:

$$
f'' + \frac{f'}{r} - \frac{n^2 f}{r^2} + \kappa f\left(1 - \frac{\gamma f^2}{\kappa}\right) = 0
$$

This is the **vortex equation** — derived independently in the contexts of superconducting magnetic flux tubes (Abrikosov, 1957; Nobel Prize 2003), cosmic strings (Kibble, 1976), and superfluid vortices (Onsager, 1949; Feynman, 1955).

Bloom shape: ring-shaped in 2D with a nodal point at $r = 0$ (where $A = 0$). The bloom has a hole: i₀ maps to a zero-amplitude core at the center of the vortex. Winding number $n$ counts how many times the phase wraps as you circle the nodal point.

**Zone activation:** Memory zone (−Y, curl) primary; Expansion zone (+Y, Laplacian) secondary; membrane between them carries the topological flux.

### 3.A — Linear Volume

A field that varies in all three spatial directions but remains in the linear regime. The natural modes are the spherical harmonics:

$$
\Phi_{3.A}(\mathbf{x}) = A_0\,j_\ell(kr)\,Y_\ell^m(\theta, \phi)\,e^{-i\omega t}
$$

where $j_\ell$ is the spherical Bessel function and $Y_\ell^m$ is the spherical harmonic of degree $\ell$ and order $m$. These are the standing wave modes of the full ICHTB volume.

Bloom shape: spherical harmonic structure — multiple lobes, nodal surfaces, angular nodes. All six zones are simultaneously activated at amplitudes determined by the angular quantum numbers $(\ell, m)$.

**Zone activation:** All six zones active; zone-specific amplitudes determined by the orientation of the spherical harmonic nodes relative to the zone axes.

### 3.B — Topological Knot (Maximum Persistence)

The most complex bloom: a field configuration with non-trivial topology in all three spatial dimensions. The simplest 3.B state is a **Hopfion** — a field configuration where the phase $\theta$ maps the 3-sphere $S^3$ to the 2-sphere $S^2$ with Hopf invariant $H \neq 0$ (Hopf, 1931):

$$
\Phi_{3.B}(\mathbf{x}) = A_0\,f(r)\,e^{i\theta_{\text{Hopf}}(\mathbf{x})}
$$

where $\theta_{\text{Hopf}}$ is the Hopf phase map. This configuration has the property that **every pair of field lines (pre-image circles of distinct points on $S^2$) is linked** — the field lines form a Hopf fibration, an interlinked family of circles filling all of 3D space.

Bloom shape: the 3.B bloom has no preferred direction — it is topologically symmetric. The amplitude $A_0$ is nonzero everywhere except on nodal lines (the zeros of the field), which form closed loops. These loops link with each other with linking number $H$.

**Zone activation:** All six zones active; the Core zone (−Z) is the most strongly activated because the persistence of the 3.B state requires proximity to the i₀ fixed point. The topological protection comes from the impossibility of continuously deforming the Hopf phase to a trivial phase without passing through a configuration with $A = 0$ everywhere — a catastrophic energy cost.

**Example physical analog:** Ball lightning (hypothetical), proton as a topological soliton (Skyrme, 1961; Nobel context: Skyrme model), atomic nucleus modeled as a Skyrmion field configuration.

---

## The Bloom Progression as Emergence Sequence

Reading the six classes in order — 1.A → 1.B → 2.A → 2.B → 3.A → 3.B — is not merely a taxonomy. It is an **emergence sequence**: the path from the simplest possible field excitation (a traveling wave in one dimension) to the most complex (a topologically protected 3D knot that cannot be destroyed).

Each step in the sequence requires:
1. More zones to be simultaneously active
2. A larger amplitude relative to the linear threshold
3. More membrane crossings to maintain the configuration
4. More topological infrastructure to protect against decay

The bloom shape is the visible record of how far along the emergence sequence a given excitation has traveled. A 1.A state has barely left i₀ — it is a ripple, a signal. A 3.B state has completed the entire emergence journey — it is matter.

This is astrosynthesis in miniature: the invisible process by which a field disturbance at i₀ becomes a persistent structured object in the full 3D ICHTB volume, one zone activation at a time.

