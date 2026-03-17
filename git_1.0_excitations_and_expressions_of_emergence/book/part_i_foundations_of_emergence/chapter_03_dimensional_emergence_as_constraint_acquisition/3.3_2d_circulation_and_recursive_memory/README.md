# 3.3 2D: Circulation and Recursive Memory

## 3.3.1 From gradients to rotational structure

In the previous section the substrate developed gradients
$$
\nabla \Phi \neq 0
$$
which introduced directional bias.
However gradients alone do not form closed or persistent structures. Gradients tend to dissipate through diffusion unless an additional stabilizing mechanism appears.
The next structural stage arises when gradients interact in such a way that circulation develops.
Circulation corresponds to rotational flow within the substrate.

## 3.3.2 Velocity field representation

To analyze circulation we introduce a vector field
$$
\mathbf{v}(\mathbf{x},t)
$$
representing the transport of structural content across the substrate.
This velocity field may arise from gradient-driven flows of the scalar field.
A simple relation is
$$
\mathbf{v} = -\kappa \nabla \Phi
$$
where
$$
\kappa
$$
is a transport coefficient.
This relation shows how gradients produce directed motion.

## 3.3.3 Curl and circulation

Circulation appears when the velocity field develops nonzero curl.
The curl operator is defined as
$$
\nabla \times \mathbf{v}.
$$
If
$$
\nabla \times \mathbf{v} = 0
$$
the flow is purely gradient-driven and contains no rotational structure.
If
$$
\nabla \times \mathbf{v} \neq 0
$$
rotational motion exists.
Such regions correspond to vortical structures.

## 3.3.4 Circulation integral

Circulation around a closed curve (C) is defined as
$$
\Gamma
\oint_C
\mathbf{v}\cdot d\mathbf{l}.
$$
Using Stokes’ theorem this becomes
$$
\Gamma
\int_S
(\nabla \times \mathbf{v})\cdot d\mathbf{S}.
$$
Thus nonzero curl produces finite circulation.

## 3.3.5 Vorticity

Define the vorticity vector
$$
\boldsymbol{\omega}
\nabla \times \mathbf{v}.
$$
This quantity measures the local rotational strength of the flow.
Regions where
$$
|\boldsymbol{\omega}| > 0
$$
contain circulating motion.
Such regions represent the earliest form of 2D structural closure in the substrate.

## 3.3.6 Energy of circulation

Circulating flows store kinetic energy.
Define the circulation energy
$$
E_{circ}
\frac{1}{2}
\int
\rho |\mathbf{v}|^2
d^3x.
$$
Here
$$
\rho
$$
represents an effective density associated with structural transport.
This energy contributes to retained structure.

## 3.3.7 Structural retention with circulation

The total retained structure now includes three contributions:
$$
R =
\alpha_0 \int \Phi^2 d^3x
+
\alpha_1 \int |\nabla\Phi|^2 d^3x
+
\alpha_2 \int |\mathbf{v}|^2 d^3x.
$$
Circulation therefore provides an additional channel for storing organized structure.

## 3.3.8 Persistence of vortices

Rotational structures can resist collapse more effectively than pure gradients.
In many physical systems vortices possess topological stability.
The circulation
$$
\Gamma
$$
may remain approximately conserved.
Thus vortices can persist even when surrounding gradients dissipate.

## 3.3.9 Recursive memory

Circulating motion has an important consequence.
Because the flow loops back on itself, structural information can circulate repeatedly.
Define the recurrence time
$$
T_{cycle}
\frac{L}{v}
$$
where
$$
L
$$
is the circumference of the circulation path.
During each cycle the structural configuration revisits previous states.
This process creates recursive memory.

## 3.3.10 Persistence condition for circulation

Using the selection number
$$
S =
\frac{R}{\dot R t_{ref}},
$$
and the retention measure including circulation energy,
$$
R =
\alpha_0 ||\Phi||^2
+
\alpha_1 ||\nabla\Phi||^2
+
\alpha_2 ||\mathbf{v}||^2,
$$
we see that vortical structures may achieve
$$
S \ge 1
$$
if the circulation energy exceeds dissipative losses.

## 3.3.11 Emergent vortex structures

Several classes of persistent structures can arise from circulation.
Examples include:
structure
defining property
vortex line
circulation around a core
vortex ring
closed loop circulation
vortex sheet
extended rotational layer

These objects represent the first self-reinforcing dynamical structures in the CTS.

## 3.3.12 Dimensional interpretation

Circulation requires two spatial directions.
The rotational plane defines a two-dimensional structure.
Thus circulation corresponds to the 2D stage of dimensional emergence.
In this stage the substrate supports closed loops of structural transport.

Summary
The third stage of dimensional emergence occurs when interacting gradients produce circulation.
Rotational structures store energy through
$$
E_{circ} =
\frac{1}{2}
\int \rho |\mathbf{v}|^2 d^3x.
$$
Circulation introduces recursive memory and increases structural persistence.
These properties allow vortical structures to survive longer than simple gradient configurations.

3D: Curvature Closure and Boundary Formation
This next section derives how circulating structures close into bounded volumes, forming the first true structural objects.

No additional sections beyond the Table of Contents.
