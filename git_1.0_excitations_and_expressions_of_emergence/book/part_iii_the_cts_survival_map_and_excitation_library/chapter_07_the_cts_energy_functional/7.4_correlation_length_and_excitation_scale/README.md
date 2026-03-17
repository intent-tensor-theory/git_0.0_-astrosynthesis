# 7.4 Correlation Length and Excitation Scale

## 7.4.1 Why scale must be derived

The previous section showed that the CTS functional admits vacuum bifurcation and domain formation. But persistent structures are not characterized only by whether they exist. They are also characterized by size, coherence length, and excitation scale.
To classify CTS excitations, we therefore need to derive the characteristic spatial scale associated with the field parameters.
That scale is determined by the correlation length.

## 7.4.2 Linearized fluctuation equation

Start from the scalar CTS functional
$$
E[]=d3x[a2+u(2)2+r2+s4].E[\Phi] = \int d^3x \left[ a|\nabla\Phi|^2 + u$\nabla^2\Phi$^2 + r\Phi^2 + s\Phi^4 \right].E[
$$
Let the field fluctuate around a vacuum value
Φ(x)=Φ0+δΦ(x).\Phi$\mathbf{x}$ = \Phi_0 + \delta\Phi$\mathbf{x}$.Φ(x)=Φ0​+δΦ(x).
To leading order, the fluctuation dynamics are controlled by the quadratic terms in δΦ $\delta\Phi$
The linearized operator is
$$
L=a2+u4+m2\mathcal{L} = - a\nabla^2 + u\nabla^4 + m^2L=
$$
where the effective mass parameter is determined by the curvature of the potential at the vacuum.

## 7.4.3 Effective mass

The local potential is
$$
V()=r2+s4.V$\Phi$=r\Phi^2+s\Phi^4.V(
$$
Its second derivative is
d2VdΦ2=2r+12sΦ2.\frac{d^2V}{d\Phi^2} = 2r+12s\Phi^2.dΦ2d2V​=2r+12sΦ2.
Evaluating at the vacuum:
Symmetric phase: Φ0=0\Phi_0=0Φ0​=0
m2=2r.m^2 = 2r.m2=2r.
Since the broken phase requires r<0r<0r<0, this gives
m2=4∣r∣.m^2 = 4|r|.m2=4∣r∣.
Thus the broken vacuum supports stable fluctuations with positive effective mass.

## 7.4.4 Fourier-space dispersion relation

Expand fluctuations in Fourier modes:
$$
(x)=~(k)eikxd3k.\delta\Phi$\mathbf{x}$ = \int \tilde{\Phi}$\mathbf{k}$ e^{i\mathbf{k}\cdot\mathbf{x}} \,d^3k.
$$
Acting on a Fourier mode, the operator becomes
$$
L(k)=ak2+uk4+m2.\mathcal{L}(k) = a k^2 + u k^4 + m^2.L(k)=ak2+uk4+m2.
$$
Thus the quadratic fluctuation energy is
$$
E(2)=d3k(ak2+uk4+m2)~(k)2.E^{(2)} =\int d^3k\; \left( a k^2 + u k^4 + m^2 \right) |\tilde{\Phi}$\mathbf{k}$|^2.E(2)=
$$
This expression determines which wavelengths are energetically costly and which are favored.

## 7.4.5 Correlation function

The two-point correlation function is defined as
$$
G(xy)=(x)(y).G$\mathbf{x}-\mathbf{y}$ = \langle \delta\Phi$\mathbf{x}$\delta\Phi$\mathbf{y}$ \rangle.G(x
$$
In Fourier space,
This is the propagator of scalar fluctuations in the CTS substrate.
The characteristic length scale is determined by the location of the poles of this denominator.

## 7.4.6 Correlation length without curvature term

If the curvature term is neglected at long wavelength, so that
uk4≪ak2,u k^4 $\ll a k^2,uk4$
This is the standard Ornstein–Zernike form.
The correlation length is then
ξ=am2\boxed{ \xi = \sqrt{\frac{a}{m^2}} }ξ=m2a​​​
or explicitly:
Symmetric phase
Broken phase
This length gives the typical size over which the field remains coherent.

## 7.4.7 Critical divergence

As the system approaches the bifurcation point,
$$
r0,r\to 0,r
$$
the effective mass tends to zero:
$$
m20.m^2\to 0.m2
$$
$$
.\xi \to \infty.
$$
This divergence means fluctuations become correlated across arbitrarily large scales near criticality.
This is one of the defining signatures of phase transition behavior in the CTS substrate.

## 7.4.8 Curvature-controlled excitation scale

When the higher-order curvature term is important, the relevant scale is modified.
The fluctuation denominator becomes
ak2+uk4+m2.a k^2 + u k^4 + m^2.ak2+uk4+m2.
To estimate the preferred nonzero scale, compare gradient and curvature terms:
ak2∼uk4.a k^2 $\sim u k^4.ak2$
Solving gives
Thus the associated structural length is
ℓ∗∼ua\boxed{ \ell_* \sim \sqrt{\frac{u}{a}} }ℓ∗​∼au​​​
This is the intrinsic curvature-stabilized excitation scale of the substrate.
It sets the approximate size of localized patterns and precursor objects.

## 7.4.9 Competing scales

The CTS therefore contains two important length scales:
Correlation length
which measures the extent of coherent fluctuations.
Curvature scale
which measures the size favored by curvature stabilization.
These scales play different roles:
$$
\xi
$$

ℓ∗\ell_*ℓ∗​ controls localized structural size

## 7.4.10 Excitation energy estimate

For a localized excitation of characteristic size LLL, the various energy contributions scale as
Egrad∼aΦ02L2L3=aΦ02LE_{grad} \sim a \frac{\Phi_0^2}{L^2} L^3 = a\Phi_0^2 LEgrad​∼aL2Φ02​​L3=aΦ02​L Ecurv∼uΦ02L4L3=uΦ021LE_{curv} \sim u \frac{\Phi_0^2}{L^4} L^3 = u\Phi_0^2 \frac{1}{L}Ecurv​∼uL4Φ02​​L3=uΦ02​L1​ Emass∼m2Φ02L3.E_{mass} \sim m^2 \Phi_0^2 L^3.Emass​∼m2Φ02​L3.
Thus the total excitation energy scales approximately as
E(L)∼aΦ02L+uΦ021L+m2Φ02L3.E(L) \sim a\Phi_0^2 L + u\Phi_0^2 \frac{1}{L} + m^2\Phi_0^2 L^3.E(L)∼aΦ02​L+uΦ02​L1​+m2Φ02​L3.
This equation is extremely important because it shows how different terms dominate at different sizes.

## 7.4.11 Optimal excitation size

To estimate the preferred excitation size, minimize E(L)E(L)E(L) with respect to LLL:
dEdL∼aΦ02−uΦ021L2+3m2Φ02L2.\frac{dE}{dL} \sim a\Phi_0^2 - u\Phi_0^2 \frac{1}{L^2} + 3m^2\Phi_0^2 L^2.dLdE​∼aΦ02​−uΦ02​L21​+3m2Φ02​L2.
Set this equal to zero:
a−uL2+3m2L2=0.a - \frac{u}{L^2} + 3m^2 L^2 =0.a−L2u​+3m2L2=0.
Multiplying by L2L^2L2 gives
3m2L4+aL2−u=0.3m^2 L^4 + aL^2 - u = 0.3m2L4+aL2−u=0.
X=L2.X=L^2.X=L2.
3m2X2+aX−u=0.3m^2 X^2 + aX - u = 0.3m2X2+aX−u=0.
Thus the preferred excitation size is
L∗2=−a+a2+12m2u6m2\boxed{ L_*^2 = \frac{-a + \sqrt{a^2 + 12m^2u}}{6m^2} }L∗2​=6m2−a+a2+12m2u​​​
and therefore
This gives the characteristic size of finite CTS excitations.

## 7.4.12 Limiting cases

$$
Near-critical regime: m20m^2\to 0m2
$$
Expand the square root:
a2+12m2u≈a+6m2ua.\sqrt{a^2 + 12m^2u} \approx a + \frac{6m^2u}{a}.a2+12m2u​≈a+a6m2u​.
So near criticality,
The curvature scale dominates.

Strong-mass regime: m2≫a2/um^2 $\gg a^2/um2$
So the excitation shrinks as the mass scale grows.
This means heavier or more strongly restoring phases support smaller localized objects.

## 7.4.13 Interpretation in CTS language

The CTS substrate does not support arbitrary excitation sizes. Its parameters select preferred scales.
aaa controls gradient tension

uuu controls curvature stabilization

m2m^2m2 controls vacuum restoring force

Together these determine:
how far structural coherence extends

how large localized excitations can become

which scales dominate the excitation ledger

Thus correlation length and excitation scale are not external assumptions. They are derived directly from the energy functional.

## 7.4.14 Connection to persistence mechanics

Once a characteristic excitation size L∗L_*L∗​ is known, it can be inserted into the retention and loss formulas from earlier chapters.
For example:

circulation loss scales like ν/L∗2\nu/L_*^2ν/L∗2​

curvature relaxation scales like κ/L∗3\kappa/L_*^3κ/L∗3​

Thus the energy functional determines the scale, and the scale determines the persistence number.
This is the bridge between formation mechanics and survival mechanics.

## 7.4.15 Summary

The CTS energy functional determines two key structural scales:
ξ=am2\xi = \sqrt{\frac{a}{m^2}}ξ=m2a​​
for long-range correlation, and
for curvature-stabilized localization.
More generally, the preferred excitation size is
L∗2=−a+a2+12m2u6m2.L_*^2 = \frac{-a + \sqrt{a^2 + 12m^2u}}{6m^2}.L∗2​=6m2−a+a2+12m2u​​.
These scales govern the size and energy of emergent CTS excitations.

 Relation to Landau, Ginzburg, Higgs-Like, and Topological Functionals
This section compares the CTS energy functional to established functional frameworks and shows exactly where it overlaps and where it departs.

particle fields

condensed matter phases.

In CTS the same mathematics is interpreted as describing the substrate of emergence itself.
Thus the excitations of the functional correspond to persistent structural expressions of the substrate.

## 7.5.12 Connection to the persistence equation

Once solutions of the CTS functional are obtained, their energies determine the retained structure RRR.
The persistence condition then evaluates which excitations survive.
Thus
energy functional → candidate structures
persistence mechanics → survival of structures
This two-layer process defines the full emergence mechanism.

## 7.5.13 Summary

The CTS energy functional shares mathematical structure with several major theoretical frameworks:
Landau phase transitions

Ginzburg–Landau superconductivity

Higgs symmetry breaking

Swift–Hohenberg pattern formation

topological field theory.

The novel feature of the CTS framework is the interpretation of this unified functional as describing the dynamical substrate from which persistent structures emerge.

 CTS Functional as the Generator of the Excitation Library
This final section of Chapter 7 shows how the energy functional generates the full spectrum of CTS excitations that populate the survival map.

