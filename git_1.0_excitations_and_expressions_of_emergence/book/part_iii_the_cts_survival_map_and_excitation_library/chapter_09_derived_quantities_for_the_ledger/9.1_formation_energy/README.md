# 9.1 Formation Energy

## 9.1.1 Motivation

The CTS excitation ledger introduced in Chapter 8 requires several quantitative quantities for each excitation class. The first and most fundamental of these is the formation energy.
Formation energy measures the energetic cost required to create an excitation from the vacuum state of the Collapse Tension Substrate.
Formally, the formation energy determines how easily a structure can appear in the substrate.

## 9.1.2 Definition

Let the CTS vacuum configuration be
Φ=Φ0.\Phi = \Phi_0.Φ=Φ0​.
Let an excitation be represented by a field configuration
Φ=Φ0+δΦ.\Phi = \Phi_0 + \delta\Phi.Φ=Φ0​+δΦ.
The formation energy is defined as the difference between the energy of the excitation and the vacuum energy:
Eform=E[Φ]−E[Φ0]\boxed{ E_{form} = E[\Phi] - E[\Phi_0] }Eform​=E[Φ]−E[Φ0​]​
where E[Φ]E[ $\Phi]E[$

## 9.1.3 CTS energy functional

Recall the CTS functional
$$
E[,A]=d3x[a(iqA)2+bA2+u(2)2+r2+s4].E[\Phi,\mathbf A] = \int d^3x \left[ a|$\nabla - iq\mathbf A$\Phi|^2 + b|\nabla\times\mathbf A|^2 + u$\nabla^2\Phi$^2 + r|\Phi|^2 + s|\Phi|^4 \right].E[
$$
To compute formation energy we substitute the excitation configuration into this expression.

## 9.1.4 Energy density decomposition

The energy density can be written as
E=Egrad+Ecurv+Epot+Egauge.\mathcal{E} = \mathcal{E}_{grad} + \mathcal{E}_{curv} + \mathcal{E}_{pot} + \mathcal{E}_{gauge}.E=Egrad​+Ecurv​+Epot​+Egauge​.

## 9.1.5 Formation energy of wave excitations

For small-amplitude wave excitations
$$
=Aei(kxt),\Phi = A e^{i$\mathbf{k}\cdot x-\omega t$},
$$
the dominant contribution is gradient energy.
Thus
Here VVV is the spatial volume of the wave.
Because AAA can be arbitrarily small, wave formation energy can approach zero.
This explains why wave modes dominate the background excitation population.

## 9.1.6 Formation energy of vortex excitations

For vortex structures the dominant energy contribution arises from phase gradients.
Using the vortex ansatz
$$
(r,)=f(r)ein,\Phi(r,\theta)=f(r)e^{in\theta},
$$
the gradient energy density becomes
Egrad≈a[(dfdr)2+n2r2f2].\mathcal{E}_{grad} \approx a\left[ \left$\frac{df}{dr}\right$^2 + \frac{n^2}{r^2}f^2 \right].Egrad​≈a[(drdf​)2+r2n2​f2].
Integrating yields the approximate vortex formation energy
Eformvortex≈πan2Φ02ln⁡ ⁣(Rξ).E_{form}^{vortex} \approx \pi a n^2 \Phi_0^2 \ln\!\left$\frac{R}{\xi}\right$.Eformvortex​≈πan2Φ02​ln(ξR​).
Thus vortex formation energy grows logarithmically with system size.

## 9.1.7 Formation energy of vortex rings

A vortex filament bent into a ring of radius RRR has energy
Eformring≈ρΓ2Rln⁡ ⁣(8Rξ).E_{form}^{ring} \approx \rho\Gamma^2 R \ln\!\left$\frac{8R}{\xi}\right$.Eformring​≈ρΓ2Rln(ξ8R​).
$$
\Gamma
$$

$$
\rho
$$

The energy scales approximately linearly with ring radius.

## 9.1.8 Formation energy of shell structures

For shell excitations the dominant energy contribution comes from surface tension.
For a spherical shell of radius RRR
Eformshell=4πσR2.E_{form}^{shell} = 4\pi\sigma R^2.Eformshell​=4πσR2.
Additional curvature energy contributes
Ecurv=4πκc.E_{curv} = 4\pi\kappa_c.Ecurv​=4πκc​.
This quadratic scaling explains why shell structures require significantly larger formation energy.

## 9.1.9 Formation energy scaling law

Different excitation classes therefore exhibit distinct scaling behavior.
excitation
formation energy scaling
$$
EA2E\sim A^2E
$$
$$
Eln(R/)E\sim \ln(R/\xi)E
$$
$$
ERln(R/)E\sim R\ln(R/\xi)E
$$
$$
ER2E\sim R^2E
$$
$$
ENRE\sim N RE
$$

These scaling laws determine how difficult it is to form each structure.

## 9.1.10 Formation energy and abundance

From the abundance relation
Ai∝e−Eform/Teff,A_i \propto e^{-E_{form}/T_{eff}},Ai​∝e−Eform​/Teff​,
structures with small formation energy appear frequently.
Thus the substrate naturally contains many low-energy excitations.
High-energy structures appear rarely.

## 9.1.11 Formation versus locking

Formation energy does not determine persistence by itself.
A structure may be cheap to form but easy to destroy.
This motivates the introduction of locking energy, which will be derived in the next section.
The interplay between formation and locking energy determines the position of each excitation in the survival map.

## 9.1.12 Ledger entry parameter

For each excitation type we record
EformE_{form}Eform​
as the first quantity in the ledger entry
Li=(type,Eform,Elock,Etotal,… ).\mathcal{L}_i = $\text{type}, E_{form}, E_{lock}, E_{total}, \dots$.Li​=(type,Eform​,Elock​,Etotal​,…).
This parameter controls the excitation’s abundance in the substrate.

## 9.1.13 Summary

Formation energy is the energetic cost required to create an excitation from the CTS vacuum.
It is computed directly from the CTS energy functional.
Different excitation classes exhibit characteristic formation-energy scaling laws, which determine how frequently they appear within the substrate.

 Lock Energy
This section derives the stabilizing energy contributions that allow excitations to resist structural decay.

