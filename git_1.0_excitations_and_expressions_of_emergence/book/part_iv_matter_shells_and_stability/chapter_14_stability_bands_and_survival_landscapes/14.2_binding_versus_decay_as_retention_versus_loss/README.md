# 14.2 Binding Versus Decay as Retention Versus Loss

## 14.2.1 Motivation

The CTS framework defines persistence through the competition between retention and loss.
Earlier we defined the selection number
$$
S = \frac{R}{\dot{R},t_{ref}}
$$
where
• (R) = retained structure
• ( $\dot{R}) = rate of structural loss$
• (t_{ref}) = persistence horizon.
This equation captures a universal principle:
structures survive when retention mechanisms dominate loss mechanisms.
In physical systems this principle appears as the competition between binding energy and decay processes.

## 14.2.2 Binding energy

Binding energy represents the energy required to disassemble a structure into its constituents.
For a system of components with masses (m_i), the binding energy is
$$
B =
\left(\sum_i m_i - M\right)c^2
$$
where (M) is the mass of the bound system.
Binding energy therefore measures the strength of structural retention.

## 14.2.3 Decay processes

Structures may lose integrity through decay mechanisms such as
• particle emission
• structural fragmentation
• radiation.
Each decay process has an associated rate
$$
\lambda_i.
$$
The total decay rate becomes
$$
\lambda_{total} = \sum_i \lambda_i.
$$

## 14.2.4 Lifetime

The lifetime of a structure is determined by the inverse decay rate
$$
\tau = \frac{1}{\lambda_{total}}.
$$
Long lifetimes correspond to small decay rates.
Thus
$$
\tau \propto \frac{1}{\dot{R}}.
$$

## 14.2.5 Retention-loss balance

Within the CTS framework we interpret
Retention energy
$$
R \sim B
$$
Loss rate
$$
\dot{R} \sim \lambda_{total}.
$$
Thus the persistence number becomes
$$
S \sim \frac{B}{\lambda_{total} t_{ref}}.
$$
Structures remain stable when
$$
S > 1.
$$

## 14.2.6 Energy barriers

Decay processes often require overcoming an energy barrier.
Let the barrier height be
$$
E_b.
$$
The probability of crossing the barrier follows an Arrhenius-like law
$$
\Gamma \sim e^{-E_b/T}.
$$
Thus large energy barriers dramatically reduce decay rates.

## 14.2.7 Metastability

Some structures are not perfectly stable but persist for long times because decay barriers are large.
Such systems are metastable.
Mathematically
$$
S \gtrsim 1
$$
but not extremely large.
Metastable systems lie near stability boundaries.

## 14.2.8 Stability landscapes

Binding versus decay can be visualized as an energy landscape.
Stable structures correspond to valleys where
$$
E_{bind}
$$
is large and decay pathways are blocked by high barriers.
Unstable structures lie near peaks or shallow valleys.

## 14.2.9 Nuclear example

The nuclear stability band illustrates this principle.
Binding energy per nucleon
$$
\frac{B}{A}
$$
reaches a maximum near
$$
A \approx 56.
$$
Nuclei far from this region exhibit higher decay rates.

## 14.2.10 CTS interpretation

Within CTS language:
Retention energy corresponds to
$$
E_{lock}.
$$
Loss corresponds to
$$
\dot{R}.
$$
Thus stability arises when
$$
E_{lock} \gg E_{loss}.
$$

## 14.2.11 Persistence condition

Substituting these quantities into the selection equation yields
$$
S_* =
\mathcal{E}{shell}
\mathcal{E}
D
T{obj}
\frac{E_{lock}}{\dot{R}t_{ref}}.
$$
This generalized expression describes persistence across structural scales.

## 14.2.12 Stability boundaries

The stability boundary occurs when
$$
S_* = 1.
$$
Below this threshold
$$
S_* < 1
$$
structures decay rapidly.
Above the threshold
$$
S_* > 1
$$
structures persist.

## 14.2.13 Structural interpretation

This principle explains why stable structures occupy bands rather than isolated points.
Small changes in parameters alter the balance between retention and loss.
Thus stability appears as continuous regions within parameter space.

## 14.2.14 Universal principle

The retention-versus-loss balance applies across many systems:
system
retention
loss
atoms
binding energy
ionization
nuclei
nuclear binding
radioactive decay
vortices
circulation
dissipation
shells
curvature locking
deformation

Each system survives when retention exceeds loss.

## 14.2.15 Summary

Stability arises from the competition between retention energy and decay mechanisms.
Structures persist when binding energy dominates loss processes.
Within the CTS framework this principle appears as the requirement
$$
S_* > 1.
$$
This retention-versus-loss balance forms the mathematical foundation for stability bands in physical systems.

The Semi-Empirical Mass Formula as a Survival Equation
This section connects the nuclear binding energy formula to the CTS persistence framework and derives how the valley of stability emerges mathematically.

