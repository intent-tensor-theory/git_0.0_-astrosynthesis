# 3.4 3D: Curvature Closure and Boundary Formation

## 3.4.1 From circulation to closure

The previous section showed that interacting gradients can generate circulating flows within the Collapse Tension Substrate.
Circulation creates rotational structures such as vortex lines and rings.
However circulation alone does not necessarily produce a bounded object. Circulating flows may still disperse unless they develop a mechanism that closes the structure in three dimensions.
The next stage of emergence therefore occurs when circulating structures acquire curvature closure.
Closure produces the first finite spatial boundaries.

## 3.4.2 Curvature definition

Curvature measures the deviation of a curve or surface from a straight configuration.
For a curve parameterized by arc length $s$, curvature is defined as
$$
\kappa = \left| \frac{d^2 \mathbf{x}}{ds^2} \right|.
$$
When
$$
\kappa = 0
$$
the path is straight.
When
$$
\kappa > 0
$$
the path bends.
Curvature allows circulating structures to fold into closed shapes.

## 3.4.3 Surface curvature

In three dimensions, boundaries form surfaces rather than curves.
The curvature of a surface is characterized by the principal curvatures $k_1$ and $k_2$.
From these we define the mean curvature
$$
H = \frac{k_1 + k_2}{2}
$$
and the Gaussian curvature
$$
K = k_1 k_2.
$$
These quantities determine the geometric stability of closed surfaces.

## 3.4.4 Energy cost of curvature

Curved surfaces store structural energy.
A common curvature energy functional is
$$
E_{curv} =
\int
\kappa_c H^2
\, dA
$$
where $\kappa_c$ is a curvature stiffness coefficient.
This energy penalizes sharp curvature and stabilizes smooth boundaries.

## 3.4.5 Closure condition

A closed structure requires the boundary surface to satisfy
$$
\oint_S dA < \infty.
$$
This means the structure encloses a finite region of the substrate.
Typical closed geometries include:

- spheres
- toroidal structures
- closed vortex rings

Closure transforms circulating flows into bounded structural objects.

## 3.4.6 Boundary formation

Define a boundary surface $\Sigma$ separating two regions of the substrate.
Across the boundary the scalar field may change rapidly:
$$
|\nabla \Phi|_{\Sigma} \gg 0.
$$
This sharp transition forms a structural interface.
The interface energy can be written
$$
E_{surf} = \sigma \int_{\Sigma} dA
$$
where $\sigma$ is the surface tension.

## 3.4.7 Retained structure with closure

The retained structure now includes multiple contributions:
$$
R =
\alpha_0 \int \Phi^2 d^3x
+
\alpha_1 \int |\nabla\Phi|^2 d^3x
+
\alpha_2 \int |\mathbf{v}|^2 d^3x
+
\alpha_3 \int H^2 dA.
$$
The final term represents structural energy stored in curvature.
Closure therefore adds another channel of structural retention.

## 3.4.8 Topological protection

Closed structures often possess topological invariants.
For example a vortex ring may carry a conserved circulation
$$
\Gamma =
\oint_C \mathbf{v}\cdot d\mathbf{l}.
$$
Such invariants prevent the structure from continuously deforming into a trivial state.
Topological protection therefore increases persistence.

## 3.4.9 Persistence condition for closed structures

Using the selection number
$$
S = \frac{R}{\dot{R}\,t_{ref}},
$$
closure increases the numerator through additional energy storage mechanisms.
At the same time topological constraints can reduce loss processes.
Thus closed structures are more likely to satisfy
$$
S \geq 1.
$$
This marks the appearance of true structural objects.

## 3.4.10 Emergent volumetric objects

Once closure occurs, the substrate supports bounded volumes.
Examples include:

| Structure | Description |
|-----------|-------------|
| spherical domain | closed scalar configuration |
| vortex ring | toroidal circulation |
| soliton bubble | localized field region |

These objects represent persistent structural units.

## 3.4.11 Dimensional interpretation

Closure requires three spatial dimensions.
The boundary surface encloses a volume
$$
V = \int d^3x.
$$
Thus closure corresponds to the 3D stage of dimensional emergence.
At this stage the substrate supports objects that occupy finite regions of space.

## 3.4.12 Structural significance

Closure marks a fundamental transition in the emergence process.

Before closure:

- structures are extended patterns
- gradients and flows remain open

After closure:

- structures possess boundaries
- internal structure can be protected from external collapse

This transition allows persistent objects to form.

## 3.4.13 Summary

The fourth stage of dimensional emergence occurs when circulating structures develop curvature closure.
Closed boundaries store energy through surface curvature
$$
E_{curv} = \int \kappa_c H^2 \, dA.
$$
Closure produces bounded volumes and introduces topological protection.
These properties allow the formation of the first durable structural objects.

*Transition to Section 3.5:* The next section mathematically compares the persistence properties of scalar states, gradients, circulation, and closed structures.
