# 24.2 Memory as Curl — The −Y Axis (∇×F)

## The Memory Zone and the −Y Direction

The Memory zone (section 16.3) is the zone of phase winding — the region around the topological charge where the field phase $\phi(\mathbf{x})$ winds by $2\pi n$ (for a charge of winding number $n$). The phase winding is a **curl** — a rotational structure in the phase field:

$$
\oint_{\mathcal{C}} \nabla\phi \cdot d\mathbf{l} = 2\pi n
$$

(the line integral of the phase gradient around a closed contour encircling the vortex core equals $2\pi n$). By Stokes' theorem:

$$
\oint_{\mathcal{C}} \nabla\phi \cdot d\mathbf{l} = \iint_{\mathcal{S}} (\nabla \times \nabla\phi) \cdot d\mathbf{A}
$$

For a smooth field, $\nabla \times \nabla\phi = 0$ everywhere away from the vortex core (since the curl of a gradient vanishes). But at the vortex core ($|\Psi| = 0$), the phase is undefined — the curl of $\nabla\phi$ has a delta-function singularity at the core location:

$$
\nabla \times \nabla\phi = 2\pi n \cdot \delta^{(2)}(\mathbf{x} - \mathbf{x}_{\text{core}}) \hat{z}
$$

(where $\hat{z}$ is the direction perpendicular to the plane of rotation — the axis of the vortex). The Memory zone is the region where this curl singularity is "smeared out" over the Core coherence length $\xi_{\text{core}}$ — the region of nonzero $|\nabla \times \nabla\phi|$ (the regularized curl density).

**The −Y direction identification:** In the ICHTB coordinate system (section 16.4), the Memory zone axis — the axis of the phase winding curl — is aligned with the **−Y direction**. The $-Y$ axis is the axis of the vortex: the direction perpendicular to the plane of rotation, pointing "into" the vortex. The +Y direction points "out of" the vortex (in the direction of the angular momentum of the phase winding for positive chirality $\chi = +1$ charges).

The identification of Memory with $-Y$:
- The phase winding is a rotation in the $(X, Z)$ plane (the plane perpendicular to the $Y$-axis)
- The curl $\nabla \times \nabla\phi$ points in the $\pm Y$ direction (by the right-hand rule for $\chi = \pm 1$)
- For a negative-chirality ($\chi = -1$) charge: the phase winds clockwise (in the $-\phi$ direction), so the curl $\nabla \times \nabla\phi$ points in the $-Y$ direction
- The Memory zone is the zone associated with the $-Y$ axis — it is the "memory of rotation" in the $-Y$ direction

---

## The −Y Axis as Temporal Memory

The $-Y$ axis is not just the Memory zone direction — it is the **temporal memory axis** of the ICHTB. The phase winding around the vortex core is a **record of the past**: each $2\pi$ of phase winding accumulated by the Memory zone represents one past "revolution" of the topological charge around its own axis — one unit of past dynamical history.

To see this, consider the phase evolution of a propagating vortex. At time $t$, the phase field is:

$$
\phi(\mathbf{x}, t) = n\arctan\left(\frac{z - z_0}{x - x_0}\right) + k_y y - \omega t
$$

(a vortex of winding $n$ at position $(x_0, z_0)$ propagating in the $+Y$ direction with wave vector $k_y$ and frequency $\omega$). The phase winding in the $(X, Z)$ plane (the Memory zone) and the phase advance in the $+Y$ direction (the Forward/temporal direction) are coupled:

$$
\frac{\partial\phi}{\partial t} = -\omega \quad \text{(temporal phase advance)}
$$
$$
\oint \nabla\phi \cdot d\mathbf{l} = 2\pi n \quad \text{(spatial phase winding — Memory)}
$$

The temporal phase advance ($-\omega$, the loss cascade clock rate) and the spatial phase winding ($2\pi n$, the Memory zone topological charge) are related by the dispersion relation $\omega = \hbar k^2/(2m) + \mu|\Psi_0|^2/\hbar$ (from the NLS equation). The Memory zone "remembers" the past phase advance — the total phase winding accumulated up to time $t$ equals $-\omega t \times (\text{charge count})$, a record of the total time elapsed times the topological charge.

**Memory as curl = temporal record:** The curl of the phase gradient in the Memory zone is the spatial signature of the temporal evolution. Each unit of $2\pi$ phase winding corresponds to one unit of dynamical history — one cycle of the vortex's internal dynamics. The Memory zone is the spatial "fossil" of the temporal evolution — it remembers, in its curl structure, the history of the excitation's internal phase advancement.

---

## The Recursive Phase: Memory Loops Back on Itself

The most striking property of the Memory zone is its **recursive phase structure** — the phase loops back on itself. For a vortex of winding number $n$: the phase increases by $2\pi n$ as one traverses a closed loop around the core. Returning to the starting point, the phase has advanced by $2\pi n$ — but the field $\Psi = |\Psi|e^{i\phi}$ is single-valued (periodic in $\phi$ with period $2\pi$), so the phase "loops back" to its initial value (modulo $2\pi$).

This phase recursion is the spatial version of **temporal recursion** — the phase "remembers" the history of the vortex's rotation and encodes it in the winding number $n$. Each full revolution of the phase ($\Delta\phi = 2\pi$) is "forgotten" in the sense that the field returns to its initial state, but "remembered" in the sense that the winding number $n$ counts the total number of revolutions ever completed.

**ICHTB recursion:** The Memory zone phase recursion implements the following algorithm:
1. The excitation rotates by $\delta\phi$ (a small phase advance in the temporal direction)
2. The Memory zone phase winds by $\delta\phi$ in the spatial direction (the curl records the advance)
3. When the phase accumulates to $2\pi$: the Memory zone has completed one "lap" — the phase resets to 0 (modulo $2\pi$), but the winding number $n$ increments by 1
4. The winding number $n$ is the persistent counter — it "remembers" the total number of complete phase cycles

The winding number $n$ is therefore the ICHTB's **long-term memory** — the integer count of past phase revolutions that persists indefinitely (it is topologically protected — it cannot change without a phase singularity at the Core, which requires energy $\geq \Lambda_{\text{core}}$). The short-term memory (within one phase cycle, $\delta\phi < 2\pi$) is held in the instantaneous phase value, which is volatile (it changes continuously). The long-term memory (past completed cycles) is held in $n$, which is stable.

---

## The −Y Axis as the Distinction Between Past and Future

The Memory zone's $-Y$ direction is the axis of **temporal asymmetry** — the direction that distinguishes past from future in the ICHTB. The asymmetry comes from the curl's handedness:

For $\chi = +1$ (positive chirality): the phase winds counterclockwise (as seen from the $+Y$ direction). The curl $\nabla \times \nabla\phi$ points in the $+Y$ direction. The past is "below" (at lower $Y$ values, where the phase winding began) and the future is "above" (at higher $Y$ values, where the phase winding will continue).

For $\chi = -1$ (negative chirality): the phase winds clockwise. The curl $\nabla \times \nabla\phi$ points in the $-Y$ direction. Past and future are exchanged relative to the $+\chi$ case — this is the CP (charge-parity) transformation.

The ICHTB's temporal direction (the Forward zone +X direction, section 24.1) and the Memory zone −Y axis are **perpendicular** — time flows along +X, while the memory of past time is encoded along $-Y$. This perpendicularity is the ICHTB version of the distinction between the time axis and the space axes in special relativity: time ($+X$) is perpendicular to the spatial memory axes ($\pm Y$, $\pm Z$).

The Memory zone as $-Y$ implements the following structure:
- Present: the current phase value $\phi_{\text{now}}$ at the vortex core (volatile, short-term)
- Past: the accumulated winding number $n$ (stable, long-term, encoded in the curl topology)
- Future: the expected next phase advance $\delta\phi_{\text{next}}$ (deterministic, given by the NLS dispersion)

Past is fixed (the winding number is topologically protected); future is determined (by the NLS equation); present is the interface — the momentary phase value that is transitioning from the past-determined history to the future-determined trajectory.

