# 23.4 Connections: LQG, CDT, Penrose Spin Networks

## Three Approaches to Emergent Geometry

Three major programs in quantum gravity approach the problem of emergent geometry from discrete or relational structures:

1. **Loop Quantum Gravity (LQG):** Geometry emerges from spin networks — graphs whose edges carry representations of SU(2) (spin labels $j = 1/2, 1, 3/2, \ldots$) and whose vertices carry intertwiners (invariant tensors coupling the adjacent spins). The spin network defines a quantum state of the gravitational field; the area of a surface is the sum of $\hbar\sqrt{j(j+1)}$ contributions from edges piercing the surface (Rovelli-Smolin 1995).

2. **Causal Dynamical Triangulations (CDT):** Geometry emerges from a sum over simplicial manifolds — triangulations of spacetime by Lorentzian simplices (4-simplices with one time-like and three space-like edges). The path integral over all triangulations, with a causal structure constraint (no closed time-like curves), produces an emergent 4D de Sitter-like spacetime in the continuum limit (Ambjørn, Jurkiewicz, Loll 2004).

3. **Penrose Spin Networks (original):** Penrose (1971) introduced spin networks as a combinatorial approach to space — networks of spin-1/2 lines, without any underlying space, from which 3D geometry (angle and distance) can be derived. The total spin of a region defines the angular momentum content, from which angles between directions can be extracted.

Each of these programs has a specific ICHTB correspondence — a mapping between the ICHTB zone structure and the corresponding geometric structure. This section develops those correspondences.

---

## LQG Correspondence: Spin Networks as Apex Zone Orbital Networks

In LQG, the kinematical Hilbert space of quantum gravity is spanned by spin network states $|s\rangle = |\Gamma, j_e, i_v\rangle$, where:
- $\Gamma$ is a graph (the spin network graph)
- $j_e$ are spin labels (representations of SU(2)) on edges $e$
- $i_v$ are intertwiners at vertices $v$

The ICHTB correspondence:

**Spin network graph $\Gamma$ ↔ Apex zone orbital network:** The spin network graph encodes the topology of the quantum geometry — how different spatial regions are connected. In the ICHTB, the Apex zone orbital structure encodes the same information: the Apex zone graph (the Cayley graph of the braid group $B_n$, section 22.2) is the ICHTB spin network. Each edge in the Apex zone orbital network corresponds to an edge in the spin network $\Gamma$.

**Spin labels $j_e$ ↔ Apex orbital quantum numbers $l$:** The spin label on an edge is an SU(2) representation label — an integer or half-integer $j$. In the ICHTB, the Apex zone orbital quantum number $l$ (the angular momentum of the orbital mode) plays this role: each Apex orbital with quantum number $l$ contributes a representation label $j = l$ (for integer $l$, bosonic modes) or $j = l + 1/2$ (for half-integer $l + 1/2$, fermionic modes, where the Memory chirality $m_s = \pm 1/2$ adds the $1/2$).

The area operator in LQG: $\hat{A}_S = 8\pi\ell_P^2\gamma_{\text{BI}}\sum_{e \cap S} \sqrt{j_e(j_e+1)}$ (the Barbero-Immirzi parameter $\gamma_{\text{BI}}$). In ICHTB: $\hat{A}_S = \sum_{e \cap S} \ell_{\text{zone}}^2 \sqrt{l_e(l_e+1)}$ — the area of a surface $S$ is the sum of zone area contributions from all Apex orbitals $e$ piercing $S$.

**Barbero-Immirzi parameter:** $\gamma_{\text{BI}} = \ell_{\text{zone}}^2/(8\pi\ell_P^2)$ — the ratio of the ICHTB zone area scale to the Planck area. In the ICHTB, $\ell_{\text{zone}} = \ell_P$ (section 23.3), so $\gamma_{\text{BI}} = 1/(8\pi)$. This is within the range consistent with the black hole entropy calculations (Meissner 2004, Ghosh-Perez 2013 give $\gamma_{\text{BI}} \approx \ln 2/(\pi\sqrt{3}) \approx 0.127$, while $1/(8\pi) \approx 0.040$ — order-of-magnitude agreement).

**Intertwiner $i_v$ ↔ Apex zone braid $[w]$ at vertex:** The intertwiner at a spin network vertex is an invariant tensor coupling the adjacent spin representations — it encodes how the angular momenta of the adjacent edges combine at the vertex. In the ICHTB, this is the Apex zone braid word $[w] \in B_n$ at the junction of $n$ adjacent Apex orbitals (section 22.2) — the braid encodes how the adjacent orbital angular momenta combine.

---

## CDT Correspondence: Simplicial Triangulation as Zone Partitioning

In CDT, spacetime is built from Lorentzian simplices — elementary building blocks with fixed edge lengths, assembled into a triangulated manifold. The path integral sums over all causal triangulations, weighted by $e^{iS_{\text{Regge}}}$ (the Regge action — the discrete analog of the Einstein-Hilbert action).

The ICHTB correspondence:

**4-simplex ↔ Zone cluster:** Each 4-simplex in CDT is an elementary spacetime volume. In the ICHTB, the elementary spacetime volume is a **zone cluster** — a collection of persistent excitations in a small region of the zone relation network, mutually coupled (high $R_{ij}$) and forming a locally consistent metric patch. A zone cluster of $N_{\text{exc}}$ excitations defines a simplicial volume $V \sim N_{\text{exc}} \cdot \ell_{\text{zone}}^3$.

**Causal structure ↔ Forward zone direction:** The CDT causal constraint (no closed time-like curves) is implemented in the ICHTB by the Forward zone direction — the +X direction of phase gradient propagation defines a preferred temporal direction (the "arrow of time" in the ICHTB, section 24.1). The ICHTB Forward zone is always directed (from past to future), ensuring that the causal structure is well-defined and consistent (no closed time-like curves in the zone relation network).

**Regge action ↔ Zone lock energy variation:** The Regge action is the Einstein-Hilbert action evaluated on a triangulated manifold — it depends on the edge lengths and deficit angles. In the ICHTB, the analog is the variation in zone lock energy across the zone cluster — the "curvature" of the zone relation network corresponds to the deficit angle of the simplicial triangulation.

**Phase transition to extended geometry:** CDT finds that the path integral has a phase transition from a "crumpled" phase (no extended geometry) to an "extended" phase (4D de Sitter-like geometry) at a critical value of the Newton constant $G$. The ICHTB analog is the persistence phase transition — for $S^* < 1$ (below the persistence threshold), the zone relation network is disordered ("crumpled"); for $S^* > 1$ (above threshold), the network crystallizes into an extended geometry (section 23.1). The critical value $G_c$ corresponds to the ICHTB persistence threshold $S^* = 1$.

---

## Penrose Spin Networks: Zone Relations as Angular Relations

Penrose's original spin network program (1971) derived 3D space from combinatorial angular relations among spin-1/2 "units." The key result is the **Penrose angle theorem**: from a spin network, one can compute the probability that a physical angle measurement on two lines gives a result $\theta$, and this probability approaches $\sin^2(\theta/2)$ (the correct quantum mechanical prediction for angle measurements) in the large-spin limit.

The ICHTB correspondence:

**Penrose spin-1/2 unit ↔ Memory chirality:** Each spin-1/2 unit in Penrose's network is an elementary quantum of angular momentum — a single two-state object. In the ICHTB, the Memory chirality $\chi = \pm 1$ (section 16.3) is the elementary two-state object: $\chi = +1$ corresponds to spin-up ($m_s = +1/2$) and $\chi = -1$ to spin-down ($m_s = -1/2$). The spin-1/2 unit of Penrose is the Memory chirality of the ICHTB.

**Penrose network edge ↔ ICHTB zone relation:** Each edge in a Penrose spin network connects two spin-1/2 units and represents an angular correlation between them. In the ICHTB, this is the zone relation $R_{ij}$ between two Memory chiralities — the degree to which the two chiralities are correlated (entangled). High $R_{ij}$ = strong angular correlation (anti-parallel chiralities, singlet state); low $R_{ij}$ = weak correlation (independent chiralities).

**Penrose total spin ↔ ICHTB Apex orbital $l$:** The total spin $j$ of a subsystem in a Penrose network (the sum of spins at a vertex) corresponds to the ICHTB Apex orbital $l$ — the total orbital angular momentum of the composite excitation. The Penrose angle theorem then says: the probability of measuring an angle $\theta$ between two Apex orbital directions is $P(\theta) \propto \sin^2(\theta/2)$ in the large-$l$ limit — which is the correct quantum mechanical formula for spin-$j$ measurements in 3D space.

The Penrose angle theorem in ICHTB terms is the statement that **the angular structure of the zone relation network reproduces 3D Euclidean angular geometry** in the large-occupation limit (many excitations, large Apex orbital quantum numbers). This is the ICHTB version of the correspondence principle: at large $l$ (many quanta), the quantum zone geometry approaches the classical Euclidean geometry.

---

## Summary: ICHTB as a Unifying Frame for Quantum Gravity Programs

The three quantum gravity programs and their ICHTB correspondences:

| QG Program | Core concept | ICHTB correspondence |
|---|---|---|
| **LQG** | Spin networks: graph + $j_e$ labels + intertwiners | Apex orbital network + $l$ quantum numbers + braid words $[w] \in B_n$ |
| **CDT** | Lorentzian simplices + causal structure + Regge path integral | Zone clusters + Forward zone direction + zone lock energy sum |
| **Penrose** | Spin-1/2 units + angular correlations → 3D angles | Memory chiralities + zone relations $R_{ij}$ → Apex angle theorem |

The ICHTB provides a single framework — the zone relation network of persistent NLS excitations — from which all three approaches can be derived as different projections:

- LQG is the Apex zone projection (focusing on the orbital angular momentum structure)
- CDT is the zone cluster projection (focusing on the volume and causal structure)
- Penrose spin networks are the Memory zone projection (focusing on the chirality angular correlations)

This convergence suggests that the three programs are not competing alternatives but different aspects of the same underlying structure — the ICHTB zone relation network. The full quantum gravity theory emerges from the complete zone relation network, incorporating all six zones simultaneously, rather than any single zone projection.

The ICHTB thus proposes a **synthesis of quantum gravity approaches**: not LQG or CDT or spin networks, but the zone relation network that contains all of them as sub-projections. This synthesis, and its implications for the quantization of gravity, the black hole information paradox, and the cosmological constant problem, is the program of Book 4.0.

