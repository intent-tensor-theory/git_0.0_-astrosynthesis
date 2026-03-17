# 4.4 Derivation of the Selection Number

## 4.4.1 Objective

Previous sections introduced three quantities:
retained structure (R)
structural loss rate ( $\dot R)$
persistence horizon (t_{ref})
We now derive the selection number
$$
S
$$
as the dimensionless parameter controlling structural persistence.

## 4.4.2 Time evolution of retained structure

Let
$$
R(t)
$$
represent the retained structure of a configuration.
The general evolution equation is
$$
\frac{dR}{dt} = -\dot R.
$$
In many systems structural loss is proportional to the existing structure.
Thus
$$
\frac{dR}{dt} = -\Gamma R.
$$
The parameter
$$
\Gamma
$$
represents the effective decay constant.

## 4.4.3 Solution of the decay equation

Solving the differential equation
$$
\frac{dR}{dt} = -\Gamma R
$$
gives
$$
R(t) = R_0 e^{-\Gamma t}.
$$
Thus retained structure decreases exponentially over time.
The characteristic lifetime of the structure is
$$
\tau = \frac{1}{\Gamma}.
$$

## 4.4.4 Structural survival condition

Suppose a structure must persist over the time interval
$$
t_{ref}.
$$
The remaining structure after this interval is
$$
R(t_{ref}) = R_0 e^{-\Gamma t_{ref}}.
$$
Persistence requires that a significant fraction of the original structure remain.
A natural threshold occurs when
$$
\Gamma t_{ref} = 1.
$$
At this point the structure decays by a factor
$$
e^{-1}.
$$

## 4.4.5 Dimensionless persistence parameter

Define a dimensionless parameter
$$
S = \frac{1}{\Gamma t_{ref}}.
$$
Using
$$
\Gamma = \frac{\dot R}{R},
$$
this becomes
$$
S = \frac{R}{\dot R,t_{ref}}.
$$
This expression is the selection number.

## 4.4.6 Interpretation of the numerator

The numerator
$$
R
$$
represents the structural content stored in the configuration.
Larger values of (R) correspond to more organized energy or information.
Thus increasing (R) increases persistence.

## 4.4.7 Interpretation of the denominator

The denominator
$$
\dot R,t_{ref}
$$
represents the structural content lost during the persistence horizon.
Thus the selection number compares retained structure with structure lost during the relevant time interval.

## 4.4.8 Persistence regimes

The persistence condition follows directly.
Ephemeral regime
$$
S < 1
$$
Loss dominates retention.
The structure decays before the persistence horizon.

Critical regime
$$
S = 1
$$
Retention balances loss.
The structure lies at the threshold of persistence.

Persistent regime
$$
S > 1
$$
Retention dominates.
The structure survives beyond the persistence horizon.

## 4.4.9 Alternative form using lifetime

Using the structural lifetime
$$
\tau = \frac{1}{\Gamma},
$$
the selection number becomes
$$
S = \frac{\tau}{t_{ref}}.
$$
Thus persistence simply compares the lifetime of a structure with the time horizon over which it must survive.

## 4.4.10 Structural interpretation

The selection number can be interpreted as a survival ratio.
If
$$
S \gg 1,
$$
the structure remains largely intact during the persistence horizon.
If
$$
S \ll 1,
$$
the structure disappears rapidly.

## 4.4.11 Application to multiple retention channels

If structural retention contains several channels
$$
R = \sum_i R_i
$$
and loss processes include several mechanisms
$$
\dot R = \sum_j \dot R_j,
$$
then the selection number becomes
$$
S =
\frac{\sum_i R_i}
{\left(\sum_j \dot R_j\right) t_{ref}}.
$$
Thus multiple retention channels increase persistence while multiple loss channels decrease it.

## 4.4.12 Summary

The selection number is derived by comparing retained structure with structural loss during the persistence horizon.
The final expression is
$$
S = \frac{R}{\dot R,t_{ref}}.
$$
This dimensionless parameter determines whether a configuration survives long enough to participate in further structural evolution.

Interpreting Subcritical, Critical, and Supercritical Emergence
This section analyzes how the selection number determines transitions between ephemeral fluctuations and persistent structures.

