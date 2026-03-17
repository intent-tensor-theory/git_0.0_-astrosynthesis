# 4.2 Defining Loss Rate

## 4.2.1 Structural degradation

In the persistence framework, the numerator of the selection number
$$
S = \frac{R}{\dot R,t_{ref}}
$$
measures retained structure. The denominator must therefore measure the rate at which that structure is destroyed.
Define the structural loss rate
$$
\dot R = -\frac{dR}{dt}.
$$
This quantity represents the rate at which organized structure degrades due to dissipative processes.

## 4.2.2 Sources of structural loss

Structural degradation arises from a variety of physical processes. The most common include:
loss mechanism
physical example
diffusion
smoothing of gradients
viscous dissipation
decay of vortices
radiation
energy emission
scattering
particle interactions
thermal noise
random fluctuations

Each of these processes reduces the structural energy stored in a configuration.

## 4.2.3 Loss as dissipation

For systems described by an energy functional
$$
E[\Phi],
$$
the structural loss rate corresponds to the rate at which energy dissipates.
Define
$$
R = E[\Phi].
$$
Then
$$
\dot R = -\frac{dE}{dt}.
$$
If the system follows gradient-descent dynamics
$$
\partial_t \Phi = -\frac{\delta E}{\delta \Phi},
$$
the energy decreases according to
$$
\frac{dE}{dt}
\int
\frac{\delta E}{\delta \Phi}
\partial_t \Phi , d^3x.
$$
Substituting the field equation gives
$$
\frac{dE}{dt}

\int
\left(
\frac{\delta E}{\delta \Phi}
\right)^2
d^3x.
$$
Thus
$$
\dot R =
\int
\left(
\frac{\delta E}{\delta \Phi}
\right)^2
d^3x.
$$
This expression is always positive, confirming that structural energy dissipates.

## 4.2.4 Diffusive loss

One of the most common loss processes is diffusion.
The diffusion equation is
$$
\partial_t \Phi = D\nabla^2 \Phi.
$$
For a Fourier mode
$$
\Phi_k(t)
\Phi_k(0)e^{-Dk^2t},
$$
the decay rate becomes
$$
\Gamma = Dk^2.
$$
Thus the structural loss rate for gradient structures is approximately
$$
\dot R \sim \Gamma R.
$$
Small-scale structures with large (k) decay rapidly.

## 4.2.5 Viscous loss in circulation

Circulating structures such as vortices lose energy through viscosity.
The vorticity equation is
$$
\partial_t \boldsymbol{\omega}
\nabla \times (\mathbf{v} \times \boldsymbol{\omega})
+
\nu\nabla^2 \boldsymbol{\omega}.
$$
The second term represents viscous diffusion.
The decay rate for a vortex of size (L) is approximately
$$
\Gamma \sim \frac{\nu}{L^2}.
$$
Thus larger vortices persist longer.

## 4.2.6 Surface relaxation

Closed structures lose energy through curvature smoothing.
The curvature evolution equation is
$$
\partial_t H = -\kappa \nabla^2 H.
$$
Here
$$
\kappa
$$
represents curvature mobility.
The decay rate for curvature modes scales approximately as
$$
\Gamma \sim \frac{\kappa}{L^3}.
$$
Thus larger closed structures experience slower relaxation.

## 4.2.7 General loss law

Many physical systems exhibit exponential structural decay.
In this case
$$
\frac{dR}{dt} = -\Gamma R.
$$
The solution is
$$
R(t) = R_0 e^{-\Gamma t}.
$$
Thus
$$
\dot R = \Gamma R.
$$
The decay constant ( $\Gamma) determines the rate of structural loss.$

## 4.2.8 Loss timescale

Define the structural lifetime
$$
\tau = \frac{1}{\Gamma}.
$$
This represents the characteristic time over which structural energy decreases significantly.
If
$$
t_{ref} \ll \tau,
$$
the structure appears stable.
If
$$
t_{ref} \gg \tau,
$$
the structure decays quickly.

## 4.2.9 Loss channels

Just as retained structure can have multiple channels, loss can also occur through multiple mechanisms.
Define
$$
\dot R =
\sum_i \dot R_i
$$
where each term represents a different dissipation process.
Examples include
diffusive loss
radiative loss
viscous loss
thermal degradation.
These contributions combine to determine the total loss rate.

## 4.2.10 Effective decay rate

The effective decay rate is defined as
$$
\Gamma_{eff} =
\frac{\dot R}{R}.
$$
Substituting this definition into the persistence condition gives
$$
S =
\frac{1}{\Gamma_{eff} t_{ref}}.
$$
Thus persistence depends entirely on the ratio between structural lifetime and the observation horizon.

## 4.2.11 Interpretation

Structural loss represents the universal tendency of organized configurations to degrade over time.
Without retention mechanisms, loss processes would drive all systems toward equilibrium.
The persistence framework therefore interprets emergence as the outcome of competition between retention and loss.

## 4.2.12 Summary

Structural loss rate is defined as
$$
\dot R = -\frac{dR}{dt}.
$$
For many systems this corresponds to exponential decay
$$
\dot R = \Gamma R.
$$
The effective decay rate ( $\Gamma) determines how quickly structure dissipates.$
Together with retained structure (R), the loss rate forms the denominator of the persistence equation.

Defining the Persistence Horizon
This section introduces the timescale (t_{ref}) and derives how observational timescales influence structural persistence.

