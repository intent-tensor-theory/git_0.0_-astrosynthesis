# 7.3 Vacuum Structure and Bifurcation

## 7.3.1 Definition of vacuum states

The vacuum state of a field theory corresponds to a configuration that minimizes the energy functional.
For the CTS scalar functional derived previously,
$$
E[]=d3x[a2+u(2)2+r2+s4],E[\Phi] = \int d^3x \left[ a|\nabla\Phi|^2 + u$\nabla^2\Phi$^2 + r\Phi^2 + s\Phi^4 \right],E[
$$
the vacuum state occurs when the field is spatially uniform:
$$
=0.\nabla \Phi = 0.
$$
Thus the energy density reduces to the potential
$$
V()=r2+s4.V$\Phi$ = r\Phi^2 + s\Phi^4.V(
$$

## 7.3.2 Finding stationary points

Vacuum states occur when
dVdΦ=0.\frac{dV}{d\Phi} = 0.dΦdV​=0.
Computing the derivative gives
dVdΦ=2rΦ+4sΦ3.\frac{dV}{d\Phi} = 2r\Phi + 4s\Phi^3.dΦdV​=2rΦ+4sΦ3.
Setting this equal to zero yields
$$
(2r+4s2)=0.\Phi(2r + 4s\Phi^2) = 0.
$$
Thus the stationary points are
$$
=0\Phi = 0
$$

## 7.3.3 Symmetric vacuum

r>0r > 0r>0
then the only real solution is
$$
=0.\Phi = 0.
$$
In this case the vacuum is symmetric.
The energy minimum occurs at
Vmin=0.V_{min} = 0.Vmin​=0.
This phase corresponds to a uniform CTS substrate without spontaneous structure formation.

## 7.3.4 Broken-symmetry vacuum

r<0r < 0r<0
then two additional minima appear:
Φ=±−r2s.\Phi = \pm \sqrt{\frac{-r}{2s}}.Φ=±2s−r​​.
These states correspond to a bifurcation of the vacuum.
The system spontaneously selects one of the two states.

## 7.3.5 Energy of the broken vacuum

Substituting
into the potential gives
V(Φ0)=−r24s.V$\Phi_0$ = -\frac{r^2}{4s}.V(Φ0​)=−4sr2​.
Thus the broken vacuum has lower energy than the symmetric state.
This means the system naturally evolves toward one of these nonzero field values.

## 7.3.6 Vacuum bifurcation diagram

The potential
$$
V()=r2+s4V$\Phi$ = r\Phi^2 + s\Phi^4V(
$$
changes shape as rrr varies.
Three regimes appear:
r value
vacuum structure
r>0r>0r>0
single minimum at Φ=0 $\Phi=0$
r=0r=0r=0
flat critical point
r<0r<0r<0
two symmetric minima

This behavior represents a pitchfork bifurcation.

## 7.3.7 Physical interpretation

The bifurcation of the vacuum corresponds to the spontaneous emergence of structure within the substrate.
When
r<0r < 0r<0
the uniform state becomes unstable.
The system must choose one of two nonzero field values.
This symmetry breaking produces domains and structural boundaries.

## 7.3.8 Domain formation

Suppose two regions choose opposite vacuum states:
Φ=+Φ0\Phi = +\Phi_0Φ=+Φ0​
The boundary between these regions forms a domain wall.
Domain walls are solutions of the field equation that interpolate between the two vacuum states.

## 7.3.9 Domain wall solution

In one spatial dimension the field equation becomes
ad2Φdx2−rΦ−2sΦ3=0.a \frac{d^2\Phi}{dx^2} - r\Phi - 2s\Phi^3 = 0.adx2d2Φ​−rΦ−2sΦ3=0.
The solution is
is the characteristic wall thickness.

## 7.3.10 Energy of domain walls

The energy per unit area of the domain wall is
σ=∫−∞∞[a(dΦdx)2+V(Φ)−V(Φ0)]dx.\sigma = \int_{-\infty}^{\infty} \left[ a\left$\frac{d\Phi}{dx}\right$^2 + V$\Phi$ - V$\Phi_0$ \right] dx.σ=∫−∞∞​[a(dxdΦ​)2+V(Φ)−V(Φ0​)]dx.
This energy defines the surface tension of the wall.
Domain walls therefore behave like membranes separating regions of different vacuum states.

## 7.3.11 Vacuum fluctuations

Even within a stable vacuum, fluctuations occur.
These fluctuations correspond to small perturbations
Φ=Φ0+δΦ.\Phi = \Phi_0 + \delta\Phi.Φ=Φ0​+δΦ.
Linearizing the energy functional yields an effective mass term
m2=2∣r∣.m^2 = 2|r|.m2=2∣r∣.
The fluctuations obey the wave equation
(∂t2−∇2+m2)δΦ=0.$\partial_t^2 - \nabla^2 + m^2$\delta\Phi = 0.(∂t2​−∇2+m2)δΦ=0.
Thus the vacuum supports propagating excitations.

## 7.3.12 Correlation length

The spatial correlation length of the field is
ξ=1m.\xi = \frac{1}{m}.ξ=m1​.
This length determines the typical scale over which fluctuations are correlated.
Near the critical point
$$
r0r\rightarrow 0r
$$
the correlation length diverges.

## 7.3.13 Critical behavior

As
$$
r0r\rightarrow 0r
$$
the system approaches a critical state.
At this point
fluctuations occur at all scales

the system becomes highly sensitive to perturbations.

Criticality plays an important role in structure formation.

## 7.3.14 CTS interpretation

Within the CTS framework, vacuum bifurcation represents the first stage of structural differentiation in the substrate.
The scalar field separates into domains corresponding to different structural phases.
These domains form the precursors of later topological objects.

## 7.3.15 Relation to persistence mechanics

Vacuum bifurcation generates structures with nonzero retained energy.
Thus
R>0.R > 0.R>0.
Once these structures satisfy the persistence condition
S∗≥1,S_* \ge 1,S∗​≥1,
they become persistent features of the substrate.

## 7.3.16 Summary

The CTS scalar functional produces multiple vacuum states when the quadratic coefficient becomes negative.
This bifurcation creates domain structures and boundaries that serve as seeds for more complex excitations.
Thus vacuum structure provides the first mechanism through which organized patterns emerge within the substrate.

 Correlation Length and Excitation Scale
This section derives how the parameters of the energy functional determine the size and energy of CTS excitations.

