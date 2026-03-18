# 4.3 Defining the Persistence Horizon

## 4.3.1 The missing component of persistence

The selection number derived earlier is

$$
S = \frac{R}{\dot{R}\,t_{ref}}
$$

where $R$ is retained structure, $\dot{R}$ is structural loss rate, and $t_{ref}$ is the persistence horizon. The first two quantities describe properties of the structure itself. The third quantity describes the timescale over which persistence is evaluated. Thus persistence is not an absolute concept. It depends on the relevant observational or dynamical timescale.

## 4.3.2 Definition of the persistence horizon

The persistence horizon $t_{ref}$ represents the time interval over which the survival of a structure must be evaluated. Formally,

$$
t_{ref} = \text{characteristic timescale relevant to the phenomenon}.
$$

If a structure survives longer than $t_{ref}$, it is considered persistent for that context.

## 4.3.3 Relation to structural lifetime

Let the structural lifetime be

$$
\tau = \frac{1}{\Gamma}
$$

where $\Gamma$ is the effective decay rate. The persistence condition becomes

$$
S = \frac{1}{\Gamma\,t_{ref}}.
$$

Thus persistence depends on the ratio

$$
\frac{\tau}{t_{ref}}.
$$

## 4.3.4 Persistence regimes

Three regimes arise depending on the relative magnitudes of $\tau$ and $t_{ref}$.

**Subcritical regime:** $\tau < t_{ref}$

The structure decays faster than the relevant observation time. Thus $S < 1$. The configuration appears ephemeral.

**Critical regime:** $\tau = t_{ref}$

The structure persists for approximately the duration of the reference horizon. Thus $S = 1$. This represents the persistence threshold.

**Supercritical regime:** $\tau > t_{ref}$

The structure survives significantly longer than the relevant timescale. Thus $S > 1$. The structure appears stable.

## 4.3.5 Scale dependence of persistence

The persistence horizon depends strongly on the physical scale being considered. Examples include:

| System | Reference timescale |
|---|---|
| Atomic collisions | $10^{-15}$ s |
| Chemical reactions | $10^{-6}$ s |
| Biological processes | Seconds to years |
| Cosmological structures | Billions of years |

A structure that is persistent at one scale may be ephemeral at another. Thus persistence is inherently scale-dependent.

## 4.3.6 Dynamic horizons

In many systems the persistence horizon is not fixed but evolves with time. For example, in expanding systems the relevant timescale may grow according to

$$
t_{ref}(t) = \alpha\,t.
$$

This situation occurs in cosmological dynamics where the age of the system sets the observational horizon.

## 4.3.7 Multiple persistence horizons

Complex systems may contain several competing timescales. Let

$$
t_1,\, t_2,\, \dots,\, t_n
$$

represent characteristic timescales of different processes. The effective persistence horizon becomes

$$
t_{ref} = \min(t_1, t_2, \dots, t_n).
$$

The shortest relevant timescale determines whether structures appear persistent.

## 4.3.8 Persistence in fluctuating environments

In environments with stochastic fluctuations, structural lifetime may vary randomly. Define the expected lifetime $\langle \tau \rangle$. The persistence condition then becomes

$$
S = \frac{\langle \tau \rangle}{t_{ref}}.
$$

Structures persist when their average lifetime exceeds the persistence horizon.

## 4.3.9 Horizon and structural hierarchy

Different structural levels correspond to different persistence horizons. Examples include:

| Structure | Persistence horizon |
|---|---|
| Wave fluctuations | Oscillation period |
| Vortex structures | Circulation time |
| Closed structures | Boundary relaxation time |
| Atoms | Electronic orbital timescale |

Thus the persistence horizon naturally adapts to the structural level being considered.

## 4.3.10 Effective persistence measure

Combining lifetime and horizon gives

$$
S = \frac{\tau}{t_{ref}}.
$$

This ratio provides a universal measure of persistence across different physical systems. Structures with $S \gg 1$ appear stable. Structures with $S \ll 1$ appear transient.

## 4.3.11 Interpretation

The persistence horizon acts as a temporal filter that determines whether structural configurations appear stable. Retention and loss describe the intrinsic properties of a structure, while the persistence horizon describes the external context in which that structure is evaluated. Together these quantities determine the selection number.

## 4.3.12 Summary

The persistence horizon $t_{ref}$ represents the timescale over which survival is measured. Combining this quantity with the structural lifetime

$$
\tau = \frac{1}{\Gamma}
$$

gives the persistence condition

$$
S = \frac{\tau}{t_{ref}}.
$$

Structures persist when their lifetime exceeds the relevant observational horizon.

*Transition to Section 4.4:* This section formally derives the selection number equation from the combined definitions of retained structure, loss rate, and persistence horizon.
