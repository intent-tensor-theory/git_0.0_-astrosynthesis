# 17.3 The Survival Hyperbola $xy = 1$ in ICHTB Geometry

## The Two-Axis Phase Chart

The survival map of the ICHTB is plotted in the $(\Lambda_{\text{lock}}, S^*)$ plane. The horizontal axis $x = \Lambda_{\text{lock}}$ measures the lock energy (the depth of the free energy well, section 17.1). The vertical axis $y = S^*$ measures the corrected persistence (the ratio of structure retained to structure lost, section 17.2).

The fundamental constraint:

$$
xy = \Lambda_{\text{lock}} \cdot S^* = 1
$$

This is the **survival hyperbola** — the curve in the $(\Lambda_{\text{lock}}, S^*)$ plane along which composite excitations are marginally stable (the persistence horizon $S^* = 1$ crossed with the lock energy). Configurations above the hyperbola ($xy > 1$) survive; configurations below ($xy < 1$) dissolve.

Why does the survival condition take the form of a hyperbola? The derivation:

The persistence condition $S^* > 1$ (section 15.4) requires:

$$
\mathcal{E}_{\text{shell}} \cdot \mathcal{E} \cdot D \cdot T_{\text{obj}} \cdot \frac{R}{\dot{R}t_{\text{ref}}} > 1
$$

The retention rate $R/(\dot{R}t_{\text{ref}})$ is inversely proportional to the loss rate $\dot{R}$. The loss rate has two contributions: the **dilution loss** (structure lost as the ICHTB expands, $\propto 1/t_{\text{ref}}$) and the **decay loss** (structure lost as the field decays from B-state, $\propto \kappa$). The dilution loss is the dominant term for the collapse window:

$$
\dot{R} \approx \frac{R}{t_{\text{ref}}}
$$

In this approximation, $S = R/(\dot{R}t_{\text{ref}}) \approx 1$ for all configurations — the basic Selection Number is $\mathcal{O}(1)$ near the threshold. The variation of $S^*$ across the phase chart comes primarily from the multipliers $\mathcal{E}_{\text{shell}}$, $\mathcal{E}$, $D$, $T_{\text{obj}}$.

Now, the lock energy $\Lambda_{\text{lock}}$ is related to the strength of the B-state well:

$$
\Lambda_{\text{lock}} \sim \frac{\gamma^2}{12\mu}\mathcal{V}_{\text{ICHTB}} \propto \Phi_B^4\mathcal{V}_{\text{ICHTB}}
$$

(the free energy density at the B-state minimum times the ICHTB volume). The retention rate:

$$
S \approx \frac{\Lambda_{\text{lock}}}{\dot{\Lambda}_{\text{lock}}\,t_{\text{ref}}}
$$

where $\dot{\Lambda}_{\text{lock}}$ is the rate of lock energy loss (the rate at which the B-state free energy decreases due to expansion). For adiabatic expansion: $\dot{\Lambda}_{\text{lock}} \approx \Lambda_{\text{lock}}/t_{\text{ref}}$, giving $S \approx 1$. For faster-than-adiabatic expansion: $S < 1$. For slower: $S > 1$.

Substituting into the persistence condition and solving for the boundary $S^* = 1$:

$$
\Lambda_{\text{lock}} \cdot \left(\mathcal{E}_{\text{shell}}\mathcal{E}D\,T_{\text{obj}}\right)^{-1} \cdot \frac{1}{t_{\text{ref}}} = \text{const}
$$

On the persistence horizon ($S^* = 1$), the product $\Lambda_{\text{lock}} \cdot S^* = 1$ when the multipliers are folded into the $S^*$ definition. The hyperbola $xy = 1$ is thus the **universally valid persistence boundary** in the 2D projection — it holds regardless of which multipliers are dominant.

---

## The Hyperbola in ICHTB Zone Coordinates

The survival hyperbola $\Lambda_{\text{lock}} \cdot S^* = 1$ has a natural interpretation in ICHTB zone coordinates: it is the set of $(\Lambda_{\text{lock}}, S^*)$ pairs where the product of lock depth and persistence rate is exactly unity.

In zone coordinates, each point on the hyperbola corresponds to a specific zone configuration:

**Deep-low ($\Lambda_{\text{lock}} \gg 1$, $S^* \ll 1$):** Configurations with high lock energy but very poor persistence. These are strongly locked ICHTBs with insufficient retention — they lock deeply but lose structure faster than they retain it. Physically: heavy particles (large $\Lambda_{\text{lock}}$) in a rapidly dissolving medium (small $S^*$). These configurations sit on the hyperbola but are marginally persistent — a small improvement in $S^*$ takes them above the boundary into stable existence.

**Shallow-high ($\Lambda_{\text{lock}} \ll 1$, $S^* \gg 1$):** Configurations with low lock energy but very high persistence. These are lightly locked ICHTBs with excellent retention — they have almost no lock energy but persist almost indefinitely. Physically: massless or near-massless particles (small $\Lambda_{\text{lock}}$) in a very stable medium (large $S^*$). This is the photon-like corner of the diagram.

**Balanced ($\Lambda_{\text{lock}} \sim 1$, $S^* \sim 1$):** Configurations near the center of the diagram, balanced between lock energy and persistence. These are the "generic" massive particles — configurations with typical mass and typical persistence.

The hyperbola $xy = 1$ is the boundary between survival and dissolution. It asymptotes to the axes: as $\Lambda_{\text{lock}} \to \infty$ (infinite mass), the hyperbola approaches $S^* \to 0$ from above (infinitesimally persistent), and as $S^* \to \infty$ (infinitely persistent), the hyperbola approaches $\Lambda_{\text{lock}} \to 0$ from the right (infinitesimally massive).

---

## Zone Curves on the Survival Map

Different zones trace characteristic curves in the $(\Lambda_{\text{lock}}, S^*)$ plane as the zone parameters are varied:

**Memory zone curve:** As $D_m\Phi_{B,m}^2$ (the Memory zone energy density) increases, the vortex energy $\Lambda_{\text{mem}} = \pi D_m\Phi_{B,m}^2\ln(R_{\text{mem}}/\xi)$ increases (moving right on the $\Lambda$ axis), and the Memory zone drift alignment $D_{\text{mem}}$ increases toward 1 (moving up on the $S^*$ axis). The Memory zone curve is an **ascending arc** in the upper-left to lower-right direction — increasing Memory zone coupling moves configurations up and right along the hyperbola.

**Apex zone curve:** As the Apex frequency $\omega_B$ increases, $\Lambda_{\text{apex}} = \hbar\omega_B|\psi_{\text{apex}}|^2\mathcal{V}_{\text{apex}}$ increases (moving right), and $T_{\text{obj}}$ approaches 1 more rapidly (moving up). The Apex zone curve is an ascending arc that eventually saturates at $T_{\text{obj}} = 1$.

**Compression zone curve:** As the soliton energy $E_{\text{kink}}$ increases, $\Lambda_{\text{comp}}$ increases (moving right), and the Compression soliton becomes more stable (moving up). The Compression curve is a steep ascending arc (high sensitivity of $S^*$ to $\Lambda_{\text{comp}}$).

**Forward zone curve:** As the phase gradient $k_{\min}$ increases, $\Lambda_{\text{fwd}} = D\Phi_{B,f}^2 k_{\min}^2\mathcal{V}_{\text{fwd}}$ increases (moving right), but the Forward zone drift alignment $D_{\text{fwd}}$ saturates quickly (moving only slightly up). The Forward curve is a nearly **horizontal** arc — increasing Forward zone structure adds lock energy without greatly improving persistence.

The intersection of these zone curves with the survival hyperbola identifies the critical parameter values for each zone — the minimum zone coupling needed for the composite excitation to survive.

---

## Excitation Classes Plotted by Zone Address

Each type of ICHTB composite excitation occupies a characteristic region of the survival map, determined by its zone address (the dominant zones in its $\Lambda_{\text{lock}}$ partition). The excitation classes:

```
S*
│
∞ ──────────────────────────────────────────────────────────
│                        │ massless bosons          │
│                        │ (Forward-dominant)        │
│                        │ - photon analog           │
│          DISSOLVED      │ - graviton analog         │
│          (xy < 1)       ├───────────────────────────┤
│                        │ light fermions            │
│                        │ (Memory+Apex)             │
│                        │ - electron analog         │
│                        │ - neutrino analog         │
│ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─xy=1 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─│
│                        │ heavy fermions            │
│                        │ (Apex+Compression)        │
│     DISSOLVED          │ - top quark analog        │
│     (below             │ - W/Z boson analog        │
│     hyperbola)         ├───────────────────────────┤
│                        │ scalar composites         │
│                        │ (Core+Compression)        │
│                        │ - Higgs analog            │
│                        │                           │
0 ───────────────────────────────────────────────────── Λ_lock
0                        1                           ∞
                    lock energy threshold
```

The survival map organizes all composite excitations by two properties:
1. **How massive they are** ($\Lambda_{\text{lock}}$, horizontal axis)
2. **How persistent they are** ($S^*$, vertical axis)

All stable particles must be above the hyperbola $xy = 1$. The more massive a particle, the further right it sits on the $\Lambda$ axis; the more persistent, the higher it sits on the $S^*$ axis.

---

## The Hyperbola as a Universal Constraint

The survival hyperbola $\Lambda_{\text{lock}} \cdot S^* = 1$ is a **universal constraint** that applies to all ICHTB composite excitations, independent of their specific zone configuration. It is the ICHTB version of the **uncertainty principle**: the product of lock energy and persistence cannot be less than unity for a surviving object.

This is not an exact analog of Heisenberg's uncertainty principle $\Delta E \cdot \Delta t \geq \hbar/2$ (the ICHTB hyperbola is not a quantum mechanical bound), but it has the same structural form: a product of two conjugate quantities is bounded from below. The lock energy $\Lambda_{\text{lock}}$ and the corrected persistence $S^*$ are the ICHTB analogs of energy and lifetime — deep locks (high $\Lambda_{\text{lock}}$) can survive with low persistence ($S^*$ just above $1/\Lambda_{\text{lock}}$), while shallow locks (low $\Lambda_{\text{lock}}$) require high persistence (large $S^*$) to survive.

This universality is the key result of Chapter 17: **the survival hyperbola is the single organizing principle of the survival map**, and all subsequent chapters (18, 19) use this principle to classify the six survival regions and the transition rules between them.

