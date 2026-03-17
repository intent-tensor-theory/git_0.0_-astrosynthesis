# 1.2 The Failure of Particle-First Explanation

## 1.2.1 Statement of the assumption

Modern physics often begins with the assumption that particles are fundamental.
The explanatory structure is typically written

$$
\text{particles} \rightarrow \text{atoms} \rightarrow \text{molecules} \rightarrow \text{matter}
$$

Particles are treated as the primitive building blocks of reality.
Examples include:

- electrons
- quarks
- photons
- gluons

Within this framework, higher-level structures are described as combinations of these primitives.
However this approach contains an implicit assumption: particles themselves persist.
This assumption must be examined mathematically.

## 1.2.2 Particles as excitations

In modern field theory, a particle is not an independent object but an excitation of a field.
Let $\psi(\mathbf{x}, t)$ be a field.
Particles correspond to solutions of the field equation derived from the Lagrangian $\mathcal{L}(\psi, \partial_\mu \psi)$.
The action is

$$
S = \int \mathcal{L} \, d^4x.
$$

Applying the Euler–Lagrange equation gives

$$
\frac{\partial \mathcal{L}}{\partial \psi} - \partial_\mu \left( \frac{\partial \mathcal{L}}{\partial(\partial_\mu \psi)} \right) = 0.
$$

Particle states are mode solutions of these equations.
Thus a particle is mathematically equivalent to a stable excitation mode of a dynamical system.

## 1.2.3 Mode decay

Consider a simple excitation amplitude $A(t)$.
If the excitation loses energy over time, its evolution may follow

$$
\frac{dA}{dt} = -\gamma A.
$$

The solution is

$$
A(t) = A(0)\, e^{-\gamma t}.
$$

The parameter $\gamma$ is the decay constant.
The lifetime of the excitation is

$$
\tau = \frac{1}{\gamma}.
$$

Thus persistence depends on the ratio between excitation strength and decay rate.

## 1.2.4 Structural retention for a particle

Let $R_p$ represent the structural content of a particle.
In many cases this corresponds to its rest energy

$$
E = mc^2.
$$

Let $\dot{R}_p$ represent the rate at which the particle loses structural energy.
Examples include:

- radiative decay
- scattering interactions
- annihilation processes

The persistence condition from Section 1.1 becomes

$$
S_p = \frac{R_p}{\dot{R}_p \, t_{ref}}.
$$

## 1.2.5 Particle stability condition

Substituting into the selection framework, particle persistence requires

$$
S_p = \frac{R_p}{\dot{R}_p \, t_{ref}} \geq 1.
$$

This means the particle must retain its structural energy longer than the time horizon relevant for observation.

## 1.2.6 Particle lifetimes

The decay rate of a particle is often expressed as $\Gamma$, the decay width.
The lifetime is

$$
\tau = \frac{1}{\Gamma}.
$$

Substituting $R_p = mc^2$ and $\dot{R}_p = \Gamma mc^2$ into the selection number:

$$
S_p = \frac{mc^2}{\Gamma \, mc^2 \, t_{ref}} = \frac{1}{\Gamma \, t_{ref}}.
$$

Thus particle persistence depends entirely on the ratio between decay rate and observation horizon.

## 1.2.7 Classification of particle stability

Using the selection number, particle types fall into three categories.

**Stable particles** — $\Gamma \approx 0$, so $S_p \gg 1$.
Examples:

- photon (in vacuum)
- proton (extremely long lifetime)

**Long-lived particles** — $\Gamma \, t_{ref} \ll 1$, so $S_p \gg 1$ for most observation horizons.

**Short-lived particles** — $\Gamma \, t_{ref} \gtrsim 1$, so $S_p \lesssim 1$.
Examples:

- muons
- many hadronic resonances

## 1.2.8 Implication

Particles therefore satisfy the same persistence condition derived in Section 1.1.
They are not fundamental objects in a logical sense.
They are persistent solutions of a deeper dynamical system.
Thus the explanatory hierarchy must be rewritten.
Instead of

$$
\text{particles} \rightarrow \text{structure}
$$

the correct logical order is

$$
\text{substrate dynamics} \rightarrow \text{candidate excitations} \rightarrow \text{persistence filtering} \rightarrow \text{particles}.
$$

Particles appear after the survival filter, not before it.

## 1.2.9 Mathematical consequence

Let $\mathcal{E}$ be the set of all possible excitation modes of a substrate.
Each excitation $\sigma_i$ has a selection number $S_i$.
The persistent subset is

$$
\mathcal{E}_{persist} = \{ \sigma_i \mid S_i \geq 1 \}.
$$

Particles are members of this subset.
They are survivors of the excitation landscape.

## 1.2.10 Conclusion

The particle-first view assumes stability without explaining it.
However persistence requires satisfying the selection condition

$$
S = \frac{R}{\dot{R} \, t_{ref}} \geq 1.
$$

Thus particles themselves must be understood as persistent excitation modes.
This forces us to look deeper than the particle level and examine the substrate that generates those excitations.

---

*Transition to Section 1.3:*
If particles are persistent excitations rather than primitives, then emergence must be understood as a selection process within a space of possible configurations.
The next section introduces the mathematics of that configuration space and shows how observable structures arise as a filtered subset of it.
