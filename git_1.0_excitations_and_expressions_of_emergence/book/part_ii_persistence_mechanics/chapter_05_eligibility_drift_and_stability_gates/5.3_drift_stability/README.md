# 5.3 Drift Stability

## 5.3.1 Structural drift in configuration space

Even when a configuration satisfies both

$$
\mathcal{E}(\sigma)=1
$$

and

$$
S>1,
$$

the structure may still fail to persist if it drifts through configuration space toward regions of higher dissipation.
Thus persistence requires not only retention and eligibility, but also dynamical stability.
We call this requirement drift stability.

## 5.3.2 Configuration space dynamics

Let the system be described by configuration coordinates

$$
\mathbf{q} = (q_1, q_2, \dots, q_n).
$$

The evolution of the system in configuration space can be written

$$
\frac{d\mathbf{q}}{dt} = \mathbf{F}(\mathbf{q}).
$$

Here $\mathbf{F}$ represents the dynamical flow vector.
A configuration persists only if the flow does not carry it into a region where structural loss dominates.

## 5.3.3 Attractors and repellers

In dynamical systems, configurations can behave in three ways:

| Behavior | Description |
|---|---|
| attractor | trajectories converge |
| repeller | trajectories diverge |
| neutral | trajectories drift |

Persistent structures correspond to attractor states.
Mathematically, an attractor occurs when small perturbations decay.

## 5.3.4 Linear stability analysis

Consider a small perturbation $\delta\mathbf{q}$ around a configuration $\mathbf{q}_0$.
Linearizing the dynamical system gives

$$
\frac{d}{dt}(\delta\mathbf{q}) = J(\mathbf{q}_0)\,\delta\mathbf{q}.
$$

Here $J$ is the Jacobian matrix

$$
J_{ij} =
\frac{\partial F_i}{\partial q_j}.
$$

## 5.3.5 Stability criterion

The eigenvalues of the Jacobian determine stability.
Let $\lambda_i$ be the eigenvalues of $J$.
The configuration is stable if

$$
\text{Re}(\lambda_i) < 0
$$

for all eigenvalues.
In this case perturbations decay exponentially.

## 5.3.6 Drift instability

If any eigenvalue satisfies

$$
\text{Re}(\lambda_i) > 0,
$$

perturbations grow.
The system moves away from the configuration.
Thus the structure drifts toward another region of configuration space.
Such configurations cannot persist even if

$$
S>1.
$$

## 5.3.7 Drift stability factor

To incorporate this effect into persistence mechanics we define the drift stability factor $D$.
This quantity measures how strongly the configuration is anchored to a stable attractor.
One convenient definition is

$$
D = \exp(-\Lambda)
$$

where

$$
\Lambda = \max_i \bigl(\text{Re}(\lambda_i)\bigr).
$$

Thus:

| Condition | $D$ |
|---|---|
| stable attractor | $D \approx 1$ |
| weakly stable | $0 < D < 1$ |
| unstable | $D \approx 0$ |

## 5.3.8 Physical interpretation

Drift stability measures the restoring strength of structural forces.
Examples include:

| System | Restoring mechanism |
|---|---|
| vortex | circulation conservation |
| soliton | nonlinear dispersion balance |
| atomic orbit | electromagnetic binding |
| molecular bond | potential well |

These mechanisms anchor the configuration in phase space.

## 5.3.9 Drift stability and persistence

Including drift stability modifies the persistence equation.
The corrected persistence number becomes

$$
S_* =
\mathcal{E}(\sigma)\,
D\,
\frac{R}{\dot{R}\,t_{ref}}.
$$

Persistence requires

$$
S_* \geq 1.
$$

Thus three conditions must be satisfied simultaneously:

- eligibility
- drift stability
- retention exceeding loss

## 5.3.10 Stability landscape

The system can be visualized as moving through a stability landscape defined by the structural energy $E(\mathbf{q})$.
Stable configurations occur near local minima of this landscape.
The restoring force is

$$
\mathbf{F} = -\nabla E.
$$

Thus drift stability corresponds to curvature of the energy surface.

## 5.3.11 Energy curvature criterion

For a configuration at $\mathbf{q}_0$ the second derivative matrix

$$
H_{ij} =
\frac{\partial^2 E}{\partial q_i \partial q_j}
$$

defines the Hessian matrix.
Stability requires $H$ to be positive definite.
This ensures that the configuration lies in an energy minimum.

## 5.3.12 Structural anchoring

When the Hessian is positive definite, perturbations produce restoring forces.
Thus

$$
\delta E \approx
\frac{1}{2}\,
\delta\mathbf{q}^T
H\,
\delta\mathbf{q}.
$$

Positive curvature prevents the configuration from drifting.
This anchoring effect allows persistent structures to remain localized.

## 5.3.13 Summary

Drift stability ensures that configurations remain localized in configuration space.
The stability condition is determined by the eigenvalues of the Jacobian or the curvature of the energy landscape.
This effect is captured by the drift stability factor $D$.
Including this factor modifies the persistence equation to

$$
S_* =
\mathcal{E}\,D\,
\frac{R}{\dot{R}\,t_{ref}}.
$$

*Transition to Section 5.4:* Six-Fan Lock Logic and Shell Admissibility derives the geometric locking conditions required for multi-channel structural stability.
