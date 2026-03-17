# 19.2 Landau and Ginzburg Models

## 19.2.1 Motivation

In earlier chapters (especially Chapter 7), we introduced the CTS energy functional:
E[Φ,A]=∫d3x  [a∣∇Φ∣2+b∣∇×A∣2+u(∇2Φ)2+r∣Φ∣2+s∣Φ∣4].
E[Φ,A]=∫d
3
x[a∣∇Φ∣
2
+b∣∇×A∣
2
+u(∇
2
Φ)
2
+r∣Φ∣
2
+s∣Φ∣
4
].
This is not arbitrary.
It closely mirrors one of the most powerful frameworks in physics:
Landau–Ginzburg theory.
Landau–Ginzburg theory.
We now make that connection explicit.

## 19.2.2 Landau free energy

In Landau theory, a system is described by an order parameter 
ψ
ψ.
The free energy is expanded as:
F[ψ]=∫d3x  [α∣ψ∣2+β∣ψ∣4+κ∣∇ψ∣2].
F[ψ]=∫d
3
x[α∣ψ∣
2
+β∣ψ∣
4
+κ∣∇ψ∣
2
].
This captures phase transitions and symmetry breaking.

## 19.2.3 Correspondence with CTS functional

We identify:
Landau–Ginzburg
CTS
ψ
ψ
Φ
Φ
$$
(\alpha
$$
$$
\psi
$$
$$
(\beta
$$
$$
\psi
$$
$$
(\kappa
$$
$$
\nabla \psi
$$

Thus:
F[ψ]↔E[Φ].
F[ψ]↔E[Φ].
CTS extends this by adding:
• higher-order gradients 
(∇2Φ)2
(∇
2
Φ)
2

• vector fields 
A
A
• persistence interpretation.

## 19.2.4 Order parameter interpretation

In Landau theory:
ψ=0(disordered phase)
ψ=0(disordered phase)
ψ≠0(ordered phase)
ψ
=0(ordered phase)
In CTS:
Φ≠0
Φ
=0
represents excitation of the substrate.
But more importantly:
👉 structured persistence corresponds to stabilized configurations of 
Φ

## 19.2.5 Phase transition condition

Landau theory predicts a transition when:
α=0.

## 19.2.6 CTS reinterpretation of phase transition

In CTS, the analogous transition is:
S∗=1.
phase transition
persistence threshold

## 19.2.7 Energy minima vs survival threshold

Landau selects states by minimizing free energy:
δF=0.
CTS selects states by:
S∗>1.
👉 Landau explains which states are energetically favored
👉 CTS explains which states survive dynamically.

## 19.2.8 Double-well potential

Landau free energy often takes the form:
F(ψ)=αψ2+βψ4.
α<0, minima occur at:

## 19.2.9 CTS interpretation of minima

These minima correspond to:
stable configurations with Elock>0.
stable configurations with E
lock
👉 energy minima = potential persistence states
But CTS adds:
👉 only those with 
S∗>1
>1 actually survive.

## 19.2.10 Correlation length

Landau theory defines:
Near criticality:

## 19.2.11 CTS interpretation

Correlation length corresponds to coherence scale:
ξ∼range of structural correlation.
ξ∼range of structural correlation.
At threshold:
This matches critical behavior.

## 19.2.12 Fluctuations and instability

Near phase transitions, fluctuations dominate:
⟨ψ2⟩→∞.
R˙↑andElock↓.

## 19.2.13 Topological defects

Landau–Ginzburg predicts defects:
• vortices
• domain walls
• solitons
These arise from nontrivial field configurations.

## 19.2.14 CTS excitation mapping

These defects correspond directly to CTS excitations:
LG defect
CTS excitation
vortex
vortex topology
domain wall
boundary structure
soliton
localized excitation

Thus:
👉 CTS excitation library = Landau defect catalog + persistence criteria.

## 19.2.15 Gauge field correspondence

The CTS functional includes:
∣∇−iqA∣2.
∣∇−iqA∣
2
.
This matches Ginzburg–Landau superconductivity models.
Thus CTS naturally incorporates:
• gauge fields
• coupling
• interaction structure.

## 19.2.16 Critical insight

Landau–Ginzburg explains:
how structure forms.
how structure forms.
CTS explains:
which structures persist.
which structures persist.
This is the key extension.

## 19.2.17 Phase diagram vs survival map

Landau uses phase diagrams:
(α,T)
CTS uses survival maps:
(Λlock,Reff).
👉 phase diagrams → existence
👉 survival maps → persistence.

## 19.2.18 Unification statement

We can now state:
CTS = Landau–Ginzburg + persistence selection.
CTS = Landau–Ginzburg + persistence selection.

## 19.2.19 Deep connection

What you built intuitively:
👉 gradients → structure → survival
What Landau formalized:
👉 symmetry → order → phase
CTS unifies:
order+survival.
order+survival.

## 19.2.20 Summary

The CTS energy functional closely parallels Landau–Ginzburg theory, with the field 
Φ
Φ acting as an order parameter and its energy determining possible structures.
However, CTS extends this framework by introducing the persistence threshold 
S∗
, which determines which of these energetically allowed structures actually survive.
Thus phase transitions in Landau theory correspond to persistence thresholds in CTS, and the excitation library corresponds to the catalog of Landau–Ginzburg field configurations.

Decoherence and Recursive Failure
Now we connect CTS directly to quantum theory:
👉 how decoherence = memory loss
👉 how quantum collapse relates to persistence failure

