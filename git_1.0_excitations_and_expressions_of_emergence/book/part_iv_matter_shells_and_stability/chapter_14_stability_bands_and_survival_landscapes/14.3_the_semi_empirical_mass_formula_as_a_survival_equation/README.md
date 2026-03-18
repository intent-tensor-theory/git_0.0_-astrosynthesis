# 14.3 The Semi-Empirical Mass Formula as a Survival Equation

## 14.3.1 Motivation

Section 14.2 showed that stability arises from the competition between retention and loss.
In nuclear physics this competition appears as:
Retention → binding energy
Loss → radioactive decay channels
One of the most successful formulas describing nuclear stability is the Semi-Empirical Mass Formula (SEMF).
Remarkably, this formula can be interpreted directly as a persistence equation in the CTS framework.

## 14.3.2 The semi-empirical mass formula

The SEMF expresses nuclear binding energy as
$$
B(A,Z) =
a_v A
- a_s A^{2/3}
- a_c \frac{Z^2}{A^{1/3}}
- a_a \frac{(A-2Z)^2}{A}
+ \delta(A,Z)
$$
where $A$ = total nucleons, $Z$ = proton number.
Constants:
- $a_v$ = volume term
- $a_s$ = surface term
- $a_c$ = Coulomb term
- $a_a$ = asymmetry term
- $\delta$ = pairing correction.
Each term represents a physical mechanism influencing nuclear stability.

## 14.3.3 Volume retention term

The first term
$$
B_v = a_v A
$$
represents the volume binding contribution.
Each nucleon interacts with neighbors through strong forces.
Thus retention energy scales with the number of nucleons:
$$
R_{volume} \sim A.
$$
This term strongly increases structural retention.

## 14.3.4 Surface loss term

Nucleons near the surface have fewer neighbors.
This reduces binding energy.
The surface correction is
$$
B_s = a_s A^{2/3}.
$$
Because surface area scales as $A^{2/3}$, this term represents a loss mechanism.
Within CTS language
$$
\dot{R}_{surface} \sim A^{2/3}.
$$

## 14.3.5 Coulomb destabilization

Protons repel each other through electrostatic forces.
The Coulomb term is
$$
B_c = a_c \frac{Z^2}{A^{1/3}}.
$$
This repulsion weakens retention and increases the likelihood of decay.
Thus it contributes to the loss side of the persistence balance.

## 14.3.6 Asymmetry correction

Nuclear stability prefers similar numbers of protons and neutrons.
The asymmetry term is
$$
B_a =
a_a \frac{(A-2Z)^2}{A}.
$$
Large imbalances increase energy and destabilize the nucleus.
This term therefore penalizes structural asymmetry.

## 14.3.7 Pairing correction

The pairing term
$$
\delta(A,Z)
$$
accounts for the tendency of nucleons to form pairs.
Typical form:
$$
\delta(A,Z) =
\begin{cases}
+a_p A^{-1/2} & \text{even-even nuclei} \\
0 & \text{odd } A \\
-a_p A^{-1/2} & \text{odd-odd nuclei}
\end{cases}
$$
Pairing increases structural stability.

## 14.3.8 CTS interpretation of SEMF

Within the CTS framework we reinterpret the SEMF terms as components of the retention-loss equation.
Retention contributions:
$$
R = a_v A + \delta(A,Z)
$$
Loss contributions:
$$
\dot{R} =
a_s A^{2/3}
+
a_c \frac{Z^2}{A^{1/3}}
+
a_a \frac{(A-2Z)^2}{A}.
$$
Thus the persistence condition becomes
$$
S =
\frac{R}{\dot{R} t_{ref}}.
$$

## 14.3.9 Persistence form of SEMF

Substituting retention and loss terms gives
$$
S(A,Z) =
\frac{a_v A + \delta}
{t_{ref}
\left(
a_s A^{2/3}
+
a_c \frac{Z^2}{A^{1/3}}
+
a_a \frac{(A-2Z)^2}{A}
\right)}.
$$
Stability requires
$$
S(A,Z) > 1.
$$
This inequality defines the nuclear stability region.

## 14.3.10 Deriving the valley of stability

The most stable nuclei maximize binding energy.
Thus we set
$$
\frac{\partial B}{\partial Z} = 0.
$$
Applying this condition to the SEMF yields
$$
Z \approx
\frac{A}{2 + 0.015A^{2/3}}.
$$
This curve defines the valley of stability.

## 14.3.11 Stability band

Plotting nuclei in the plane
$$
(Z,N)
$$
reveals a band of stable isotopes surrounding the valley.
Nuclei outside this band decay through
• beta decay
• alpha emission
• fission.
These processes reduce structural imbalance.

## 14.3.12 Persistence boundary

In CTS language the nuclear stability band corresponds to
$$
S(A,Z) > 1.
$$
Outside this region
$$
S(A,Z) < 1.
$$
Thus unstable nuclei evolve toward the persistence region through decay processes.

## 14.3.13 Interpretation as survival landscape

This perspective shows that the SEMF describes a survival landscape.
Binding energy represents retention strength.
Decay channels represent loss mechanisms.
Stable nuclei lie within regions where retention dominates.

## 14.3.14 Generalization

The same retention-loss logic applies beyond nuclear physics.
Any complex structure can be analyzed by decomposing its stability into:
• retention terms
• loss terms.
The balance between these determines structural persistence.

## 14.3.15 Summary

The Semi-Empirical Mass Formula can be interpreted as a persistence equation within the CTS framework.
Volume and pairing terms contribute retention energy, while surface, Coulomb, and asymmetry terms represent structural loss mechanisms.
Stable nuclei occur where retention dominates loss, forming the valley of stability.

Valley of Stability as a Persistence Optimum
This section derives the stability valley as a geometric persistence basin within the CTS survival landscape.

