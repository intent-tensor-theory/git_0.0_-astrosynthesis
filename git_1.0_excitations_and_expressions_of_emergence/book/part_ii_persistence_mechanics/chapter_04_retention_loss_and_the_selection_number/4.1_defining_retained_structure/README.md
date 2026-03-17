# 4.1 Defining Retained Structure

## 4.1.1 Why retained structure must be defined

The persistence framework introduced earlier relies on the quantity
$$
S = \frac{R}{\dot R,t_{ref}}
$$
where
(R) represents retained structure
$$
$\dot R$ represents the rate of structural loss
$$
(t_{ref}) represents a persistence horizon.
For this framework to be meaningful, the quantity (R) must be defined in a way that applies to a wide range of physical systems.
Thus the first task of persistence mechanics is to define what constitutes structural retention.

## 4.1.2 Structural organization as constrained energy

A useful interpretation of retained structure is energy stored in constrained configurations.
Let
$$
E_{tot}
$$
represent the total energy of a system.
This energy can be divided into two components:
$$
E_{tot} = E_{rand} + E_{struct}.
$$
Where
(E_{rand}) represents energy distributed randomly across degrees of freedom
(E_{struct}) represents energy stored in organized configurations.
We define retained structure as
$$
R = E_{struct}.
$$
Thus structural retention corresponds to energy that is prevented from dispersing by constraints.

## 4.1.3 Energy functional representation

For systems described by fields, structural energy can often be written as an energy functional
$$
E[\Phi].
$$
For the Collapse Tension Substrate the functional introduced earlier was
$$
E[\Phi]
\int
\left(
a |\nabla \Phi|^2
+
u (\nabla^2\Phi)^2
+
r \Phi^2
+
s \Phi^4
\right)
d^3x.
$$
Each term represents a different structural contribution.
Thus the retained structure becomes
$$
R = E[\Phi].
$$

## 4.1.4 Local structural density

It is often useful to describe retained structure locally.
Define the structural density
$$
\rho_R(\mathbf{x})
$$
such that
$$
R = \int \rho_R(\mathbf{x}),d^3x.
$$
For the CTS field
$$
\rho_R =
a|\nabla\Phi|^2
+
u(\nabla^2\Phi)^2
+
r\Phi^2
+
s\Phi^4.
$$
Regions where
$$
\rho_R
$$
is large correspond to concentrated structural organization.

## 4.1.5 Structural energy in discrete systems

For discrete objects such as particles or molecules, retained structure can be expressed as binding energy.
For example, in a bound system
$$
R = E_{binding}.
$$
Binding energy represents the energy required to separate the components of the system.
Thus binding energy directly measures structural persistence.

## 4.1.6 Structural measures beyond energy

Although energy is a convenient measure of structural retention, other quantities can also contribute.
Examples include:
structural measure
example system
topological charge
vortices
circulation
fluid flow
magnetic flux
superconductors
information content
ordered systems

In general the retained structure can be written
$$
R = \sum_i R_i
$$
where each (R_i) corresponds to a different retention channel.

## 4.1.7 Retention channels

The collapse ladder introduced in Chapter 3 identified several retention mechanisms:
retention channel
structural form
amplitude
scalar field energy
gradient tension
spatial variation
circulation
rotational flow
curvature
closed boundaries

Thus
$$
R =
R_{scalar}
+
R_{grad}
+
R_{circ}
+
R_{curv}.
$$
Each additional channel increases the total retained structure.

## 4.1.8 Structural coherence

A structure persists not only because it contains energy but also because that energy is organized coherently.
Define a coherence measure
$$
C
$$
that quantifies the alignment of structural degrees of freedom.
Then the effective retained structure becomes
$$
R_{eff} = C R.
$$
If coherence is lost, the effective retained structure decreases even if total energy remains constant.

## 4.1.9 Scaling behavior

Retained structure often scales with system size.
For a structure of characteristic length
$$
L
$$
various retention channels scale differently:
mechanism
scaling
volume energy
(L^3)
surface energy
(L^2)
line energy
(L)

These scaling laws strongly influence which structures remain stable at different sizes.

## 4.1.10 Structural persistence threshold

Using the retained structure definition, the persistence condition becomes
$$
S = \frac{R}{\dot R t_{ref}}.
$$
If
$$
R
$$
is large compared to the loss term, the structure persists.
Thus the magnitude of retained structure directly controls the selection number.

## 4.1.11 Interpretation

Retained structure represents the organized energy or order stored within a configuration.
Structures that accumulate large retained structure are more resistant to collapse.
This quantity therefore serves as the numerator of the persistence equation.

## 4.1.12 Summary

Retained structure is defined as the energy or order stored in organized configurations of a system.
For field systems this can be expressed through energy functionals such as
$$
R = E[\Phi].
$$
For discrete systems it corresponds to quantities such as binding energy or topological invariants.
This quantity forms the foundation of the persistence framework.

Defining Loss Rate
This next section derives the mathematical form of the structural loss rate ( $\dot R ), completing the components needed to compute the selection number.$

