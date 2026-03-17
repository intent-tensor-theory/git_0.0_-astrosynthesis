# 8.9 The Excitation Ledger Format

## 8.9.1 Purpose of the ledger

Chapters 7 and 8 established that the CTS energy functional generates a large spectrum of possible excitations:
waves
phase-locked packets
vortices
rings
chiral primitives
shells
braids
However, the persistence framework requires that these excitations be systematically compared in order to determine which structures survive.
To accomplish this we introduce the CTS excitation ledger.
The ledger is a structured table that records the key parameters of every excitation class.

## 8.9.2 Required structural quantities

Every excitation can be characterized by three fundamental energy quantities:
Formation energy
$$
E_{form}
$$
Energy required to produce the excitation from the vacuum.

Locking energy
$$
E_{lock}
$$
Energy stored in stabilizing mechanisms such as
circulation
curvature
shell locking
braid topology.

Total energy
$$
E_{total} = E_{form} + E_{lock}.
$$
This quantity determines the abundance of the excitation.

## 8.9.3 Structural ratios

Two dimensionless ratios are especially useful for comparing excitations.
Lock ratio
$$
\Lambda_{lock}
\frac{E_{lock}}{E_{form}}.
$$
This ratio measures how strongly the excitation is stabilized relative to the energy required to create it.
Large values indicate strong internal locking.

Expression ratio
$$
\Lambda_{expr}
\frac{E_{form}}{E_{lock}+\epsilon_0}.
$$
Here ( $\epsilon_0) is a small regularization constant.$
This ratio measures how easily the excitation can form relative to its stabilizing energy.

## 8.9.4 Persistence quantities

To evaluate survival we must also record persistence parameters.
These include:
parameter
meaning
(R)
retained structural energy
$$
$\dot R$
$$
structural loss rate
(t_{ref})
persistence horizon
(D)
drift stability factor
(T_{obj})
topology factor

Using these parameters the persistence number becomes
$$
S_* =
\mathcal{E}{shell}
\mathcal{E}
D
T{obj}
\frac{R}{\dot R,t_{ref}}.
$$
This value determines whether the excitation survives.

## 8.9.5 Characteristic size

Each excitation also possesses a characteristic spatial scale
$$
L_*.
$$
From Chapter 7 we derived
$$
L_*^2 =
\frac{-a + \sqrt{a^2 + 12m^2u}}{6m^2}.
$$
This length determines the approximate physical size of the excitation.

## 8.9.6 Abundance relation

The expected abundance of an excitation class is given by
$$
A_i
\propto
\exp!\left(
-\frac{E_{total}}{T_{eff}}
\right).
$$
Here (T_{eff}) represents the effective fluctuation energy of the substrate.
Thus low-energy excitations appear frequently while high-energy structures remain rare.

## 8.9.7 Formal ledger entry

Each entry in the CTS excitation ledger therefore takes the form
$$
\mathcal{L}i =
\left(
\text{type},
E{form},
E_{lock},
E_{total},
\Lambda_{lock},
\Lambda_{expr},
L_,
T_{obj},
S_
\right).
$$
This structure allows all excitation classes to be compared quantitatively.

## 8.9.8 Example ledger entries

A simplified example of the ledger is shown below.
excitation
(E_{form})
(E_{lock})
(T_{obj})
persistence
wave
very low
none
1
low
phase-locked mode
low
small
~1
moderate
vortex
moderate
moderate
>1
moderate
ring
moderate
high
>1
high
chiral primitive
high
high
>>1
high
shell
very high
very high
>>1
extremely high
braid
extremely high
extremely high
>>1
extremely high

## 8.9.9 Ledger as a classification system

The excitation ledger serves as a classification system for emergent structures.
By comparing ledger entries we can determine
which excitations form easily
which excitations persist longest
which excitations dominate the substrate.
This classification naturally produces the CTS survival map introduced later.

## 8.9.10 Relation to the survival map

Plotting the ledger parameters in phase space produces the survival map axes:
$$
x = \Lambda_{lock}
$$
$$
y = \mathcal{R}_{eff}
$$
where
$$
\mathcal{R}_{eff}
D T_{obj}
\frac{R}{\dot R t_{ref}}.
$$
The survival boundary is
$$
S_* = 1.
$$
Excitations above this line persist.

## 8.9.11 Interpretation

The ledger reveals an important principle:
structures that are cheap to form dominate the background, while structures that are strongly locked dominate persistence.
Thus the CTS universe contains two dominant structural populations:
abundant, low-energy excitations (waves)
rare but extremely persistent structures (braids, shells).

## 8.9.12 Role of the ledger in CTS theory

The excitation ledger is the central computational framework of CTS theory.
It allows the theory to move beyond qualitative descriptions of emergence and toward quantitative predictions about structural populations.
Future work can populate the ledger with detailed numerical calculations derived from the CTS functional.

## 8.9.13 Summary

The CTS excitation ledger records the structural parameters of every excitation supported by the substrate.
Each entry includes formation energy, locking energy, topology factor, persistence number, and characteristic size.
This ledger provides the mathematical framework needed to classify and compare emergent structures.

Chapter 8 Complete
We have now completed the full excitation classification.

Formation Energy
This chapter begins the quantitative derivation of the energy quantities used in the excitation ledger.

