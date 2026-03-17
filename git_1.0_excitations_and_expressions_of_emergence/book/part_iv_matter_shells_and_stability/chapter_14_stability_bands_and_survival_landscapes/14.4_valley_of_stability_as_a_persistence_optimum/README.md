# 14.4 Valley of Stability as a Persistence Optimum

## 14.4.1 Motivation

Section 14.3 showed that the Semi-Empirical Mass Formula (SEMF) produces a stability band in nuclear systems.
This band appears as the valley of stability when nuclei are plotted in the plane
$$
(Z,N)
$$
where
(Z) = proton number
(N) = neutron number.
Within the CTS framework this stability valley can be interpreted as a persistence optimum — a region where the retention–loss balance is maximized.

## 14.4.2 Binding energy per nucleon

To understand the stability valley we examine the binding energy per nucleon
$$
\frac{B}{A}.
$$
Substituting the SEMF expression gives
$$
\frac{B}{A}
a_v
a_s A^{-1/3}
a_c \frac{Z^2}{A^{4/3}}
a_a \frac{(A-2Z)^2}{A^2}
+
\frac{\delta}{A}.
$$
Stable nuclei maximize this quantity.

## 14.4.3 Optimization condition

The optimal proton number occurs where
$$
\frac{\partial B}{\partial Z} = 0.
$$
Differentiating the SEMF yields
$$
-2a_c \frac{Z}{A^{1/3}}
+
4a_a\frac{A-2Z}{A}
= 0.
$$
Solving this equation gives the approximate stability relation.

## 14.4.4 Stability curve

Rearranging the previous expression produces
$$
Z
\approx
\frac{A}{2 + \frac{a_c}{2a_a}A^{2/3}}.
$$
Using typical coefficients
$$
a_c \approx 0.71,
\quad
a_a \approx 23,
$$
the relation becomes
$$
Z \approx \frac{A}{2 + 0.015A^{2/3}}.
$$
This curve traces the center of the nuclear stability valley.

## 14.4.5 Persistence interpretation

Within CTS language the valley corresponds to the region where
$$
S(A,Z)
\frac{R}{\dot{R}t_{ref}}
$$
is maximized.
Retention contributions:
$$
R \sim a_v A.
$$
Loss contributions:
$$
\dot{R}
\sim
a_s A^{2/3}
+
a_c \frac{Z^2}{A^{1/3}}
+
a_a \frac{(A-2Z)^2}{A}.
$$
Thus the valley appears where retention most strongly dominates loss.

## 14.4.6 Stability basin

The valley is not a single curve but a basin in parameter space.
Small deviations from the optimum increase decay probability.
If a nucleus lies outside the basin, decay processes act to move it toward the valley.

## 14.4.7 Beta decay as valley correction

Consider a nucleus with excess neutrons.
The asymmetry term increases energy.
Beta decay converts
$$
n \rightarrow p + e^- + \bar{\nu}_e.
$$
This reduces the asymmetry term and moves the nucleus closer to the valley.
Similarly, proton-rich nuclei undergo
$$
p \rightarrow n + e^+ + \nu_e.
$$
These processes drive nuclei toward the persistence optimum.

## 14.4.8 Decay flow toward persistence

The direction of decay can be interpreted as a gradient flow toward maximum persistence.
Mathematically
$$
\frac{dZ}{dt} \propto -\frac{\partial S}{\partial Z}.
$$
Thus unstable nuclei evolve toward the region where (S) is largest.

## 14.4.9 Heavy nuclei deviation

For very large (A), the Coulomb term becomes dominant.
Electrostatic repulsion increases rapidly
$$
B_c \sim \frac{Z^2}{A^{1/3}}.
$$
This weakens retention and eventually destabilizes heavy nuclei.
Thus the stability valley bends toward higher neutron fractions.

## 14.4.10 Persistence maximum

The valley center corresponds to the maximum of
$$
S(A,Z).
$$
At this point
$$
\nabla S = 0.
$$
This defines the persistence optimum.

## 14.4.11 Stability width

The width of the valley is determined by how rapidly persistence decreases away from the optimum.
Expanding (S) near the optimum gives
$$
S(A,Z)
\approx
S_{max}
\frac{1}{2}
k(Z-Z_0)^2.
$$
This quadratic form defines the basin of stability.

## 14.4.12 Structural interpretation

The valley of stability therefore represents a geometric persistence basin in nuclear parameter space.
Stable nuclei occupy the bottom of the basin.
Unstable nuclei lie on the slopes and decay toward the minimum.

## 14.4.13 CTS perspective

Within the CTS framework nuclear stability becomes an example of a more general rule:
structures evolve toward regions where retention most strongly exceeds loss.
The stability valley therefore represents a persistence optimum within the nuclear survival landscape.

## 14.4.14 Broader implications

Similar persistence basins appear in many physical systems:
system
persistence basin
nuclear physics
valley of stability
atoms
electron shell stability
vortices
circulation conservation
shell structures
curvature locking

Thus the valley-of-stability concept generalizes across scales.

## 14.4.15 Summary

The nuclear valley of stability emerges as the region where binding energy maximizes persistence.
Within the CTS framework it represents a persistence optimum — a basin where retention dominates loss.
Decay processes act to move nuclei toward this basin, reinforcing the universal principle that stable structures occupy regions of maximal persistence.

Drip Lines as Existence Boundaries
This section derives how the limits of nuclear stability correspond to hard persistence boundaries beyond which structures cannot exist.

