# 1.1 Why Origin Stories Are Not Enough

## 1.1.1 The traditional explanatory structure

Most physical explanations are built around an origin narrative.
One begins by assuming a set of primitive entities and then describes how larger structures form from them.
Symbolically, the explanatory chain is written

$$
\mathcal{P}_0 \rightarrow \mathcal{P}_1 \rightarrow \mathcal{P}_2 \rightarrow \cdots
$$

where $\mathcal{P}_0$ represents fundamental primitives (particles, fields, spacetime points, etc.),
and $\mathcal{P}_n$ represents progressively more complex structures.

For example:

$$
\text{quarks} \rightarrow \text{nucleons} \rightarrow \text{atoms} \rightarrow \text{molecules}.
$$

This framework assumes that once a structure forms, its continued existence is implicitly explained
by the dynamics that produced it. However this assumption hides an important mathematical question:

> **Why does the structure persist rather than disappear?**

---

## 1.1.2 Formation versus persistence

Let a candidate structure be denoted $\sigma$ and let $N_\sigma(t)$ represent the amount or
amplitude of that structure at time $t$.

Two competing processes determine the evolution of $N_\sigma$:

- **Formation processes**
- **Loss processes**

Let $F_\sigma$ be the formation rate and $L_\sigma$ be the loss rate.
Then the simplest population equation is

$$
\frac{dN_\sigma}{dt} = F_\sigma - L_\sigma.
$$

This equation immediately shows that formation alone does not determine survival.
Even if $F_\sigma > 0$, the structure may still vanish if

$$
L_\sigma \ge F_\sigma.
$$

Thus a structure may appear but never accumulate.

---

## 1.1.3 Retained structure

Instead of counting structures directly, it is often more useful to measure their retained
structural content. Define $R_\sigma(t)$ as the amount of organized structure contained
in configuration $\sigma$.

Examples include:

| System | Structural measure |
|--------|--------------------|
| Wave | Coherent amplitude |
| Particle | Rest energy |
| Vortex | Circulation |
| Atom | Binding energy |

The rate of structural loss is

$$
\dot{R}_\sigma = -\frac{dR_\sigma}{dt}.
$$

This quantity represents how quickly the structure degrades.

---

## 1.1.4 Persistence horizon

Not all time intervals are equally relevant.
A structure that survives for $10^{-30}\,\text{s}$ is very different from one that survives for
$10^{10}\,\text{years}$.

Thus we introduce a reference persistence horizon $t_{ref}$.
This parameter defines the timescale over which survival matters for the phenomenon being studied.

---

## 1.1.5 Derivation of the persistence condition

A structure is meaningful only if its retained structure exceeds the amount lost during the
relevant time horizon. Mathematically,

$$
R_\sigma \gtrsim \dot{R}_\sigma \, t_{ref}.
$$

Rearranging,

$$
\frac{R_\sigma}{\dot{R}_\sigma \, t_{ref}} \gtrsim 1.
$$

Define the **selection number**

$$
\boxed{S_\sigma = \frac{R_\sigma}{\dot{R}_\sigma \, t_{ref}}.}
$$

Thus the persistence condition becomes

$$
S_\sigma \ge 1.
$$

---

## 1.1.6 Interpretation of the selection number

The dimensionless quantity $S_\sigma$ measures the balance between retained structure and
structural loss. Three regimes follow immediately.

**Subcritical regime** — $S_\sigma < 1$

Loss dominates retention. The structure dissolves before it becomes significant.

**Critical regime** — $S_\sigma = 1$

Retention and loss balance. The structure exists at the threshold of persistence.

**Supercritical regime** — $S_\sigma > 1$

Retention dominates. The structure can accumulate and persist.

---

## 1.1.7 Why origin narratives are incomplete

An origin narrative typically describes $F_\sigma$ but not the ratio

$$
\frac{R_\sigma}{\dot{R}_\sigma}.
$$

Thus it answers the question *How can a structure appear?* but not *Why does the structure remain?*

Two structures produced by the same process may have drastically different survival outcomes
depending on their loss rates. For example:

| | $F$ | $L$ | $dN/dt$ |
|---|-----|-----|---------|
| Structure A | 100 | 99 | 1 |
| Structure B | 5 | 1 | 4 |

Structure B dominates despite being produced less frequently, because it survives better.

---

## 1.1.8 Persistence filtering

Let $\Omega$ be the space of all possible configurations of the substrate.
Each configuration $\sigma_i \in \Omega$ has a selection number $S_i$.

Define the persistence subset

$$
\Omega_{persist} = \{ \sigma_i \in \Omega \mid S_i \ge 1 \}.
$$

The structures that populate the observable world are drawn from this subset. Thus

$$
\Omega_{obs} \subseteq \Omega_{persist}.
$$

This means the universe of observed structures is a filtered subset of the universe of possible
structures.

---

## 1.1.9 Limiting cases

**Infinite retention** — If $\dot{R} \rightarrow 0$, then $S \rightarrow \infty$.
Such structures would be perfectly stable.

**Rapid decay** — If $\dot{R} \rightarrow \infty$, then $S \rightarrow 0$.
Such structures cannot persist.

**Vanishing structure** — If $R \rightarrow 0$, then $S \rightarrow 0$.
Fluctuations without organized structure cannot survive.

---

## 1.1.10 The persistence principle

We can now state the central principle of the framework:

> *Emergence is controlled by persistence rather than by formation alone.*

Formally,

$$
\boxed{S = \frac{R}{\dot{R}\, t_{ref}}}
$$

with threshold

$$
\boxed{S_{crit} = 1.}
$$

Structures with $S < 1$ remain ephemeral fluctuations.
Structures with $S \ge 1$ enter the domain of durable existence.

---

## 1.1.11 Implication for physical theory

If persistence determines which structures populate reality, then the task of an emergence theory
is to determine:

1. The space of possible structures
2. The retention mechanisms available to them
3. The loss processes acting against them
4. The resulting selection numbers

Thus the problem of emergence becomes a quantitative survival problem.

---

*Transition to §1.2:* The next section applies this logic to one of the most common assumptions
in physics — that particles are the fundamental starting point of explanation. If persistence
determines which structures endure, then particles themselves must satisfy the persistence
condition. Particles cannot be the beginning of the story — they must be solutions to the
survival filter.
