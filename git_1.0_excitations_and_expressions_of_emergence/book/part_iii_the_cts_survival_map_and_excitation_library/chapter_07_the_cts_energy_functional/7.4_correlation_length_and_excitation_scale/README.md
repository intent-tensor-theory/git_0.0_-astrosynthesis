# 7.4 Correlation Length and Excitation Scale

## 7.4.1 Why scale must be derived

The previous section showed that the CTS functional admits vacuum bifurcation and domain formation. But persistent structures are not characterized only by whether they exist. They are also characterized by size, coherence length, and excitation scale.
To classify CTS excitations, we therefore need to derive the characteristic spatial scale associated with the field parameters.
That scale is determined by the correlation length.

## 7.4.2 Linearized fluctuation equation

Start from the scalar CTS functional

$$
E[\Phi] = \int d^3x \left[ a|\nabla\Phi|^2 + u\left(\nabla^2\Phi\right)^2 + r\Phi^2 + s\Phi^4 \right].
$$

Let the field fluctuate around a vacuum value

$$
\Phi(\mathbf{x}) = \Phi_0 + \delta\Phi(\mathbf{x}).
$$

To leading order, the fluctuation dynamics are controlled by the quadratic terms in $\delta\Phi$.
The linearized operator is

$$
\mathcal{L} = -a\nabla^2 + u\nabla^4 + m^2,
$$

where the effective mass parameter is determined by the curvature of the potential at the vacuum.

## 7.4.3 Effective mass

The local potential is $V(\Phi) = r\Phi^2 + s\Phi^4$.
Its second derivative is

$$
\frac{d^2V}{d\Phi^2} = 2r + 12s\Phi^2.
$$

Evaluating at the vacuum:

- Symmetric phase: $\Phi_0 = 0$ gives $m^2 = 2r$.
- Broken phase: $\Phi_0 = \pm\sqrt{-r/(2s)}$ gives $m^2 = 4|r|$.

Since the broken phase requires $r < 0$, this gives a positive effective mass.
Thus the broken vacuum supports stable fluctuations with positive effective mass.

## 7.4.4 Fourier-space dispersion relation

Expand fluctuations in Fourier modes:

$$
\delta\Phi(\mathbf{x}) = \int \tilde{\Phi}(\mathbf{k})\, e^{i\mathbf{k}\cdot\mathbf{x}} \, d^3k.
$$

Acting on a Fourier mode, the operator becomes

$$
\mathcal{L}(k) = ak^2 + uk^4 + m^2.
$$

Thus the quadratic fluctuation energy is

$$
E^{(2)} = \int d^3k\; \left( ak^2 + uk^4 + m^2 \right) |\tilde{\Phi}(\mathbf{k})|^2.
$$

This expression determines which wavelengths are energetically costly and which are favored.

## 7.4.5 Correlation function

The two-point correlation function is defined as

$$
G(\mathbf{x}-\mathbf{y}) = \langle \delta\Phi(\mathbf{x})\,\delta\Phi(\mathbf{y}) \rangle.
$$

In Fourier space, the propagator takes the form

$$
\tilde{G}(k) = \frac{1}{ak^2 + uk^4 + m^2}.
$$

This is the propagator of scalar fluctuations in the CTS substrate.
The characteristic length scale is determined by the location of the poles of this denominator.

## 7.4.6 Correlation length without curvature term

If the curvature term is neglected at long wavelength, so that $uk^4 \ll ak^2$, the propagator reduces to the Ornstein–Zernike form.
The correlation length is then

$$
\boxed{ \xi = \sqrt{\frac{a}{m^2}} }
$$

Explicitly:

- Symmetric phase: $\xi = \sqrt{a/(2r)}$
- Broken phase: $\xi = \sqrt{a/(4|r|)}$

This length gives the typical size over which the field remains coherent.

## 7.4.7 Critical divergence

As the system approaches the bifurcation point $r \to 0$, the effective mass tends to zero: $m^2 \to 0$, and therefore

$$
\xi \to \infty.
$$

This divergence means fluctuations become correlated across arbitrarily large scales near criticality.
This is one of the defining signatures of phase transition behavior in the CTS substrate.

## 7.4.8 Curvature-controlled excitation scale

When the higher-order curvature term is important, the relevant scale is modified.
The fluctuation denominator becomes

$$
ak^2 + uk^4 + m^2.
$$

To estimate the preferred nonzero scale, compare gradient and curvature terms: $ak^2 \sim uk^4$.
Solving gives $k^2 \sim a/u$, so the associated structural length is

$$
\boxed{ \ell_* \sim \sqrt{\frac{u}{a}} }
$$

This is the intrinsic curvature-stabilized excitation scale of the substrate.
It sets the approximate size of localized patterns and precursor objects.

## 7.4.9 Competing scales

The CTS therefore contains two important length scales:

- Correlation length $\xi$, which measures the extent of coherent fluctuations.
- Curvature scale $\ell_*$, which measures the size favored by curvature stabilization.

These scales play different roles:

- $\xi$ controls the range of field coherence
- $\ell_*$ controls localized structural size

## 7.4.10 Excitation energy estimate

For a localized excitation of characteristic size $L$, the various energy contributions scale as

$$
E_{grad} \sim a \frac{\Phi_0^2}{L^2} L^3 = a\Phi_0^2 L, \qquad E_{curv} \sim u \frac{\Phi_0^2}{L^4} L^3 = u\Phi_0^2 \frac{1}{L}, \qquad E_{mass} \sim m^2 \Phi_0^2 L^3.
$$

Thus the total excitation energy scales approximately as

$$
E(L) \sim a\Phi_0^2 L + u\Phi_0^2 \frac{1}{L} + m^2\Phi_0^2 L^3.
$$

This equation shows how different terms dominate at different sizes.

## 7.4.11 Optimal excitation size

To estimate the preferred excitation size, minimize $E(L)$ with respect to $L$:

$$
\frac{dE}{dL} \sim a\Phi_0^2 - u\Phi_0^2 \frac{1}{L^2} + 3m^2\Phi_0^2 L^2.
$$

Setting this equal to zero:

$$
a - \frac{u}{L^2} + 3m^2 L^2 = 0.
$$

Multiplying by $L^2$ gives

$$
3m^2 L^4 + aL^2 - u = 0.
$$

Setting $X = L^2$:

$$
3m^2 X^2 + aX - u = 0.
$$

Thus the preferred excitation size is

$$
\boxed{ L_*^2 = \frac{-a + \sqrt{a^2 + 12m^2 u}}{6m^2} }
$$

This gives the characteristic size of finite CTS excitations.

## 7.4.12 Limiting cases

Near-critical regime: $m^2 \to 0$.
Expand the square root:

$$
\sqrt{a^2 + 12m^2 u} \approx a + \frac{6m^2 u}{a}.
$$

So near criticality, $L_*^2 \approx u/a$, meaning the curvature scale dominates.

Strong-mass regime: $m^2 \gg a^2/u$.
The excitation size $L_*$ shrinks as the mass scale grows.
This means heavier or more strongly restoring phases support smaller localized objects.

## 7.4.13 Interpretation in CTS language

The CTS substrate does not support arbitrary excitation sizes. Its parameters select preferred scales.

- $a$ controls gradient tension
- $u$ controls curvature stabilization
- $m^2$ controls vacuum restoring force

Together these determine:

- how far structural coherence extends
- how large localized excitations can become
- which scales dominate the excitation ledger

Thus correlation length and excitation scale are not external assumptions. They are derived directly from the energy functional.

## 7.4.14 Connection to persistence mechanics

Once a characteristic excitation size $L_*$ is known, it can be inserted into the retention and loss formulas from earlier chapters.
For example:

- circulation loss scales like $\nu/L_*^2$
- curvature relaxation scales like $\kappa/L_*^3$

Thus the energy functional determines the scale, and the scale determines the persistence number.
This is the bridge between formation mechanics and survival mechanics.

## 7.4.15 Summary

The CTS energy functional determines two key structural scales:

$$
\xi = \sqrt{\frac{a}{m^2}}
$$

for long-range correlation, and

$$
\ell_* \sim \sqrt{\frac{u}{a}}
$$

for curvature-stabilized localization.
More generally, the preferred excitation size is

$$
L_*^2 = \frac{-a + \sqrt{a^2 + 12m^2 u}}{6m^2}.
$$

These scales govern the size and energy of emergent CTS excitations.

---

## 7.5.1 Relation to Landau, Ginzburg, Higgs-Like, and Topological Functionals

This section compares the CTS energy functional to established functional frameworks and shows exactly where it overlaps and where it departs.

In standard field theory the same mathematical structure describes:

- particle fields
- condensed matter phases.

In CTS the same mathematics is interpreted as describing the substrate of emergence itself.
Thus the excitations of the functional correspond to persistent structural expressions of the substrate.

## 7.5.12 Connection to the persistence equation

Once solutions of the CTS functional are obtained, their energies determine the retained structure $R$.
The persistence condition then evaluates which excitations survive.
Thus:

- energy functional → candidate structures
- persistence mechanics → survival of structures

This two-layer process defines the full emergence mechanism.

## 7.5.13 Summary

The CTS energy functional shares mathematical structure with several major theoretical frameworks:

- Landau phase transitions
- Ginzburg–Landau superconductivity
- Higgs symmetry breaking
- Swift–Hohenberg pattern formation
- topological field theory.

The novel feature of the CTS framework is the interpretation of this unified functional as describing the dynamical substrate from which persistent structures emerge.
