#!/usr/bin/env python3
"""
scaffold_30.py
Builds the complete Book 3.0 directory structure with stub README files.
Run from repo root: python3 scaffold_30.py
"""
from pathlib import Path

ROOT = Path("git_3.0_astrosynthesis/book")

# ── Structure definition ───────────────────────────────────────────────────────
# Each chapter: (number, slug, title, summary, [(section_slug, section_title), ...])

PARTS = [
    {
        "num": "I",
        "slug": "part_i_geometry_of_pre_emergence",
        "title": "The Geometry of Pre-Emergence",
        "chapters": [
            (1, "chapter_01_i0_the_imaginary_recursion_anchor",
             "i₀ — The Imaginary Recursion Anchor",
             "Establishes the imaginary center i₀ as the CTS pre-emergence seed. "
             "Why the center cannot be a real point. The complex collapse field "
             "Φ = A·e^{iθ} and recursive phase as the dimension along which emergence advances.",
             [
                 ("1.1_why_the_center_cannot_be_real",
                  "Why the Center Cannot Be Real"),
                 ("1.2_i0_as_cts_origin",
                  "i₀ as CTS Origin — The Pre-Emergence Seed of Nothing"),
                 ("1.3_the_complex_collapse_field",
                  "The Complex Collapse Field Φ = A·e^{iθ}"),
                 ("1.4_recursive_phase_as_the_dimension_of_emergence",
                  "Recursive Phase as the Dimension of Emergence"),
                 ("1.5_prior_work_and_connections",
                  "Prior Work and Connections"),
             ]),
            (2, "chapter_02_the_membrane_first_expanse",
             "The Membrane — First Expanse from i₀",
             "The membrane is the first mathematical object connected to i₀ — before "
             "directions exist, there is a boundary. Inter-pyramid interface mathematics, "
             "zone-exchange zones, and the full edge-case formalism.",
             [
                 ("2.1_before_directions_exists_there_is_a_boundary",
                  "Before Directions Exist, There Is a Boundary"),
                 ("2.2_the_membrane_as_first_expanse",
                  "The Membrane as First Expanse from i₀"),
                 ("2.3_inter_pyramid_interface_mathematics",
                  "Inter-Pyramid Interface Mathematics"),
                 ("2.4_zone_exchange_zones",
                  "Zone-Exchange Zones — Where Adjacent Operators Meet"),
                 ("2.5_edge_case_formalism",
                  "Edge-Case Formalism"),
             ]),
            (3, "chapter_03_the_six_zones_the_bloom_outward",
             "The Six Zones — The Bloom Outward",
             "The cube, six pyramids with apexes at i₀, blooming outward through the membrane. "
             "Each zone operator, its PDE, its physical role. "
             "Volume partitioning: why six pyramids fill the cube exactly.",
             [
                 ("3.1_the_cube_and_six_pyramids",
                  "The Cube and Six Pyramids"),
                 ("3.2_zone_operators",
                  "Zone Operators — The Grammar of Field Behavior"),
                 ("3.3_volume_partitioning",
                  "Volume Partitioning — Why Six Fills Exactly"),
                 ("3.4_the_bloom_shape_and_excitation_type",
                  "Bloom Shape and Excitation Type"),
                 ("3.5_prior_work_and_connections",
                  "Prior Work and Connections"),
             ]),
            (4, "chapter_04_hat_counting_volumetric_navigation",
             "Hat Counting — Volumetric Navigation of the Bloom",
             "The discrete address system for any point in the ICHTB. "
             "Odd vs even lattice cases, volumetric navigation from i₀ outward, "
             "and how bloom shape encodes excitation type.",
             [
                 ("4.1_the_discrete_address_system",
                  "The Discrete Address System"),
                 ("4.2_odd_vs_even_lattice",
                  "Odd vs Even Lattice — Where i₀ Sits"),
                 ("4.3_navigating_from_i0_outward",
                  "Navigating from i₀ Outward"),
                 ("4.4_bloom_shape_encodes_excitation_type",
                  "Bloom Shape Encodes Excitation Type"),
             ]),
            (5, "chapter_05_the_master_equation",
             "The Master Equation",
             "Full derivation of ∂Φ/∂t = D∇ᵢ(𝓜ⁱʲ∇ⱼΦ) − Λ𝓜ⁱʲ∇ᵢΦ∇ⱼΦ + γΦ³ − κΦ "
             "from ICHTB geometry. Each term located in the box. "
             "The field-generated metric 𝓜ⁱʲ — geometry crystallizing from recursive tension.",
             [
                 ("5.1_derivation_from_ichtb_geometry",
                  "Derivation from ICHTB Geometry"),
                 ("5.2_the_field_generated_metric",
                  "The Field-Generated Metric 𝓜ⁱʲ"),
                 ("5.3_each_term_located_in_the_box",
                  "Each Term Located in the Box"),
                 ("5.4_dimensional_analysis_and_limits",
                  "Dimensional Analysis and Limits"),
                 ("5.5_connections_to_existing_mathematics",
                  "Connections to Existing Mathematics"),
             ]),
            (6, "chapter_06_edge_case_mathematics",
             "Edge Case Mathematics — A Dedicated Treatment",
             "Full membrane boundary condition formalism. Junction conditions between "
             "zone operators. Triple-junction points where three pyramids meet at an edge. "
             "The 12-edge and 8-vertex special cases. "
             "Connections: Israel junction conditions, Rankine-Hugoniot, interface field theory.",
             [
                 ("6.1_full_membrane_boundary_conditions",
                  "Full Membrane Boundary Conditions"),
                 ("6.2_junction_conditions_between_zone_operators",
                  "Junction Conditions Between Zone Operators"),
                 ("6.3_triple_junction_points",
                  "Triple-Junction Points — Where Three Pyramids Meet"),
                 ("6.4_the_12_edge_and_8_vertex_special_cases",
                  "The 12-Edge and 8-Vertex Special Cases"),
                 ("6.5_prior_work_israel_rankine_hugoniot",
                  "Prior Work: Israel, Rankine-Hugoniot, Interface Field Theory"),
             ]),
        ],
    },
    {
        "num": "II",
        "slug": "part_ii_excitation_taxonomy_in_ichtb_coordinates",
        "title": "The Excitation Taxonomy in ICHTB Coordinates",
        "chapters": [
            (7, "chapter_07_reading_the_box",
             "Reading the Box as an Excitation Address System",
             "The A/B split (Linear/Non-Linear) as a zone property. "
             "How the 1D→2D→3D ladder maps to movement through the box. "
             "The progression from signal to matter as a trajectory through ICHTB space.",
             [
                 ("7.1_the_ab_split_as_a_zone_property",
                  "The A/B Split as a Zone Property"),
                 ("7.2_the_1d_2d_3d_ladder_in_the_box",
                  "The 1D→2D→3D Ladder in the Box"),
                 ("7.3_from_signal_to_matter",
                  "From Signal to Matter — A Trajectory Through ICHTB Space"),
             ]),
            (8, "chapter_08_1d_states_in_the_box",
             "1D States in the Box",
             "1.A (Linear): Forward zone (∇Φ) carrying undisturbed propagation — hardware logic gates. "
             "1.B (Non-Linear): first membrane events — shock, soliton, kink, singular point "
             "as zone-edge phenomena. Full dispersion relations, soliton solutions, kink profiles.",
             [
                 ("8.1_1a_linear_forward_zone_propagation",
                  "1.A — Linear: Forward Zone Propagation"),
                 ("8.2_1b_nonlinear_first_membrane_events",
                  "1.B — Non-Linear: First Membrane Events"),
                 ("8.3_shock_soliton_kink_singular_point",
                  "Shock, Soliton, Kink, Singular Point — Full Mathematics"),
                 ("8.4_persistence_of_1d_states",
                  "Persistence of 1D States in ICHTB Terms"),
             ]),
            (9, "chapter_09_2d_states_in_the_box",
             "2D States in the Box",
             "2.A (Linear): Expansion/Compression plane — surface harmonics, membrane transmission. "
             "2.B (Non-Linear): Memory zone (∇×F) — vortex, skyrmion, domain wall, dislocation "
             "as curl-phase structures. Winding numbers, Skyrmion number, Burgers vector, helicity.",
             [
                 ("9.1_2a_linear_expansion_compression_plane",
                  "2.A — Linear: Expansion/Compression Plane"),
                 ("9.2_2b_nonlinear_memory_zone",
                  "2.B — Non-Linear: Memory Zone (∇×F)"),
                 ("9.3_vortex_skyrmion_domain_wall_dislocation",
                  "Vortex, Skyrmion, Domain Wall, Dislocation — Full Mathematics"),
                 ("9.4_topological_protection_in_2d",
                  "Topological Protection in 2D — Why These Structures Survive"),
             ]),
            (10, "chapter_10_3d_states_in_the_box",
             "3D States in the Box",
             "3.A (Linear): volumetric flows spanning multiple zones. "
             "3.B (Non-Linear): Apex zone (∂Φ/∂t) — toroidal vortex, triple braid, "
             "Hopf fibration, flux tube as shell emergence locks. "
             "Linking numbers, Hopf invariant, flux quantization, braid group relations.",
             [
                 ("10.1_3a_linear_volumetric_flows",
                  "3.A — Linear: Volumetric Flows Across Zones"),
                 ("10.2_3b_nonlinear_apex_zone_locks",
                  "3.B — Non-Linear: Apex Zone Locks (∂Φ/∂t)"),
                 ("10.3_toroidal_vortex_triple_braid_hopf_flux_tube",
                  "Toroidal Vortex, Triple Braid, Hopf Fibration, Flux Tube — Full Mathematics"),
                 ("10.4_the_confinement_mandate",
                  "The Confinement Mandate — Why 3D Locks Are Near-Permanent"),
             ]),
            (11, "chapter_11_membrane_states",
             "Membrane States — Excitations at Zone Interfaces",
             "Structures that straddle two or more zones simultaneously. "
             "Why these are among the most stable configurations. "
             "Edge-case excitations as ancestors of composite matter. "
             "Junction excitation modes, interface solitons, edge-localized states.",
             [
                 ("11.1_structures_straddling_multiple_zones",
                  "Structures Straddling Multiple Zones"),
                 ("11.2_why_membrane_states_are_stable",
                  "Why Membrane States Are Stable"),
                 ("11.3_interface_solitons_and_edge_localized_states",
                  "Interface Solitons and Edge-Localized States"),
                 ("11.4_membrane_states_as_ancestors_of_composite_matter",
                  "Membrane States as Ancestors of Composite Matter"),
             ]),
        ],
    },
    {
        "num": "III",
        "slug": "part_iii_persistence_mechanics",
        "title": "Persistence Mechanics — Grounded in ICHTB Geometry",
        "chapters": [
            (12, "chapter_12_retained_structure_r",
             "Retained Structure R — Zone Contributions",
             "Energy partitioned by zone. "
             "R = R_core + R_forward + R_memory + R_expansion + R_compression + R_apex + R_membrane. "
             "Connections: Noether's theorem, conserved charges, Hamiltonian decomposition.",
             [
                 ("12.1_energy_partitioned_by_zone",
                  "Energy Partitioned by Zone"),
                 ("12.2_multi_channel_retention",
                  "Multi-Channel Retention in ICHTB Terms"),
                 ("12.3_structural_coherence_and_zone_alignment",
                  "Structural Coherence and Zone Alignment"),
                 ("12.4_connections_noether_conserved_charges",
                  "Connections: Noether, Conserved Charges, Hamiltonian"),
             ]),
            (13, "chapter_13_loss_rate_rdot",
             "Loss Rate Ṙ — Zone-Specific Decay",
             "Different zones decay at different rates. "
             "Core is slowest (Φ=i₀ anchor), Apex is locked (∂Φ/∂t drives shell formation). "
             "Forward and Expansion zones are fastest losers. Decay spectra and mode lifetimes.",
             [
                 ("13.1_zone_specific_decay_rates",
                  "Zone-Specific Decay Rates"),
                 ("13.2_core_and_apex_as_anchors",
                  "Core and Apex as Structural Anchors"),
                 ("13.3_diffusion_and_dissipation_by_zone",
                  "Diffusion and Dissipation by Zone"),
                 ("13.4_effective_decay_rate_and_lifetime",
                  "Effective Decay Rate and Structural Lifetime"),
             ]),
            (14, "chapter_14_the_selection_number",
             "The Selection Number S = R / Ṙ t_ref",
             "Full derivation of S from ICHTB dynamics. "
             "Persistence horizon t_ref in geometric terms. "
             "Three regimes: subcritical, critical, supercritical. "
             "Connections: Lyapunov stability, thermodynamic free energy, information decay.",
             [
                 ("14.1_derivation_from_ichtb_dynamics",
                  "Derivation from ICHTB Dynamics"),
                 ("14.2_persistence_horizon_in_geometric_terms",
                  "Persistence Horizon in Geometric Terms"),
                 ("14.3_three_regimes",
                  "Three Regimes — Subcritical, Critical, Supercritical"),
                 ("14.4_zone_contributions_to_s",
                  "Zone Contributions to S"),
                 ("14.5_connections_lyapunov_free_energy_information",
                  "Connections: Lyapunov, Free Energy, Information Decay"),
             ]),
            (15, "chapter_15_eligibility_drift_stability",
             "Eligibility, Drift, and Stability Gates",
             "Zone admissibility as structural eligibility. "
             "Drift as movement through ICHTB configuration space. "
             "Six-fan lock logic in zone terms. "
             "The corrected persistence condition S* = ℰ_shell · ℰ · D · T_obj · R / (Ṙ t_ref).",
             [
                 ("15.1_zone_admissibility_as_eligibility",
                  "Zone Admissibility as Structural Eligibility"),
                 ("15.2_drift_in_ichtb_configuration_space",
                  "Drift in ICHTB Configuration Space"),
                 ("15.3_six_fan_lock_logic",
                  "Six-Fan Lock Logic in Zone Terms"),
                 ("15.4_the_corrected_persistence_condition",
                  "The Corrected Persistence Condition"),
             ]),
            (16, "chapter_16_topology_and_objecthood",
             "Topology and Objecthood in ICHTB Terms",
             "Closure = a structure completing a loop back to the membrane. "
             "Topology factor T_obj located geometrically in the Apex zone. "
             "The objecthood threshold: when the box locks a configuration permanently. "
             "Chirality, braiding, and shell coherence in ICHTB coordinates.",
             [
                 ("16.1_closure_as_loop_back_to_membrane",
                  "Closure as a Loop Back to the Membrane"),
                 ("16.2_topology_factor_in_the_apex_zone",
                  "Topology Factor T_obj in the Apex Zone"),
                 ("16.3_objecthood_threshold",
                  "The Objecthood Threshold"),
                 ("16.4_chirality_braiding_shell_coherence",
                  "Chirality, Braiding, and Shell Coherence in ICHTB Terms"),
             ]),
        ],
    },
    {
        "num": "IV",
        "slug": "part_iv_the_survival_map",
        "title": "The Survival Map — ICHTB Edition",
        "chapters": [
            (17, "chapter_17_the_phase_chart_with_ichtb_coordinates",
             "The Phase Chart with ICHTB Coordinates",
             "Λ_lock axis: lock energy partitioned by zone. "
             "S* axis: persistence with zone-specific multipliers. "
             "The survival hyperbola xy = 1 in ICHTB geometry. "
             "Excitation classes plotted by zone address.",
             [
                 ("17.1_lambda_lock_axis_by_zone",
                  "The Λ_lock Axis — Lock Energy Partitioned by Zone"),
                 ("17.2_s_star_axis_zone_multipliers",
                  "The S* Axis — Zone-Specific Persistence Multipliers"),
                 ("17.3_the_survival_hyperbola",
                  "The Survival Hyperbola xy = 1 in ICHTB Geometry"),
             ]),
            (18, "chapter_18_the_six_survival_regions_as_ichtb_zones",
             "The Six Survival Regions as ICHTB Zones",
             "Background propagation → Forward/Expansion dominant. "
             "Localized precursors → first membrane engagement. "
             "Closure survival → Memory zone activation. "
             "Chirality survival → Memory + membrane coupling. "
             "Shell survival → Apex zone lock. "
             "Composite survival → multi-zone braid states.",
             [
                 ("18.1_background_propagation_region",
                  "Region I — Background Propagation"),
                 ("18.2_localized_precursors_region",
                  "Region II — Localized Precursors"),
                 ("18.3_closure_survival_region",
                  "Region III — Closure Survival"),
                 ("18.4_chirality_survival_region",
                  "Region IV — Chirality Survival"),
                 ("18.5_shell_survival_region",
                  "Region V — Shell Survival"),
                 ("18.6_composite_survival_region",
                  "Region VI — Composite Survival"),
             ]),
            (19, "chapter_19_transition_rules_as_membrane_events",
             "Transition Rules as Membrane Events",
             "Every region crossing is a membrane crossing. "
             "Mathematics of each transition at its inter-pyramid interface. "
             "Why transitions are irreversible above certain amplitudes. "
             "New conserved quantity introduced at each membrane crossing.",
             [
                 ("19.1_every_transition_is_a_membrane_crossing",
                  "Every Transition Is a Membrane Crossing"),
                 ("19.2_mathematics_of_each_transition",
                  "Mathematics of Each Transition at Its Interface"),
                 ("19.3_irreversibility_above_threshold",
                  "Irreversibility Above Threshold Amplitude"),
                 ("19.4_new_conserved_quantities_at_each_crossing",
                  "New Conserved Quantities at Each Crossing"),
             ]),
        ],
    },
    {
        "num": "V",
        "slug": "part_v_matter_shells_and_stability",
        "title": "Matter, Shells, and Stability",
        "chapters": [
            (20, "chapter_20_shells_as_apex_zone_locks",
             "Shells as Apex Zone Locks",
             "Shell emergence as the defining event of the +Z Apex zone. "
             "Multi-fan lock logic in zone terms. "
             "Nested shells as layered Apex events. "
             "Orbital-like persistence from shell logic.",
             [
                 ("20.1_shell_emergence_and_the_apex_zone",
                  "Shell Emergence and the Apex Zone"),
                 ("20.2_multi_fan_lock_in_zone_terms",
                  "Multi-Fan Lock Logic in Zone Terms"),
                 ("20.3_nested_shells",
                  "Nested Shells as Layered Apex Events"),
                 ("20.4_orbital_like_persistence",
                  "Orbital-Like Persistence from Shell Logic"),
             ]),
            (21, "chapter_21_stability_bands_in_ichtb_terms",
             "Stability Bands in ICHTB Terms",
             "The Semi-Empirical Mass Formula reread as ICHTB zone energy balance. "
             "Valley of stability as persistence optimum in zone space. "
             "Drip lines as zone boundary failure. "
             "The periodic table as a survival chart across ICHTB zone combinations.",
             [
                 ("21.1_semf_as_zone_energy_balance",
                  "SEMF as ICHTB Zone Energy Balance"),
                 ("21.2_valley_of_stability_in_zone_space",
                  "Valley of Stability as Persistence Optimum in Zone Space"),
                 ("21.3_drip_lines_as_zone_boundary_failure",
                  "Drip Lines as Zone Boundary Failure"),
                 ("21.4_periodic_table_as_survival_chart",
                  "The Periodic Table as a Survival Chart"),
             ]),
            (22, "chapter_22_composite_structures_as_multi_zone_states",
             "Composite Structures as Multi-Zone States",
             "Pair and triple-braid structures occupying multiple zones simultaneously. "
             "Composite thresholds in ICHTB terms. "
             "Why composite forms are rarer. "
             "When composite survival becomes favored — zone energy conditions.",
             [
                 ("22.1_multi_zone_occupation",
                  "Multi-Zone Occupation — What Composite Means in the Box"),
                 ("22.2_pair_and_triple_braid_structures",
                  "Pair and Triple-Braid Structures"),
                 ("22.3_composite_thresholds",
                  "Composite Thresholds in ICHTB Terms"),
                 ("22.4_when_composite_survival_is_favored",
                  "When Composite Survival Is Favored"),
             ]),
        ],
    },
    {
        "num": "VI",
        "slug": "part_vi_implications",
        "title": "Implications",
        "chapters": [
            (23, "chapter_23_emergent_geometry_from_the_box",
             "Emergent Geometry from the Box",
             "How spatial geometry crystallizes from stable zone relations. "
             "Distance as stabilized relational separation between persistent zone structures. "
             "Connections: loop quantum gravity, causal dynamical triangulation, Penrose spin networks.",
             [
                 ("23.1_geometry_from_stable_zone_relations",
                  "Geometry from Stable Zone Relations"),
                 ("23.2_distance_as_relational_separation",
                  "Distance as Stabilized Relational Separation"),
                 ("23.3_proto_geometry_in_ichtb_terms",
                  "Proto-Geometry in ICHTB Terms"),
                 ("23.4_connections_lqg_cdt_spin_networks",
                  "Connections: LQG, CDT, Penrose Spin Networks"),
             ]),
            (24, "chapter_24_emergent_time_the_memory_axis",
             "Emergent Time — The −Y Memory Axis",
             "Time as ordered loss through the box. "
             "Memory as curl — ∇×F and the recursive phase that loops back on itself. "
             "Entropy as coherence degradation across zones. "
             "The second law in ICHTB language.",
             [
                 ("24.1_time_as_ordered_loss_through_the_box",
                  "Time as Ordered Loss Through the Box"),
                 ("24.2_memory_as_curl_the_minus_y_axis",
                  "Memory as Curl — The −Y Axis (∇×F)"),
                 ("24.3_entropy_as_coherence_degradation",
                  "Entropy as Coherence Degradation Across Zones"),
                 ("24.4_the_second_law_in_ichtb_language",
                  "The Second Law in ICHTB Language"),
             ]),
            (25, "chapter_25_light_and_the_cheapest_expressions",
             "Light and the Cheapest Expressions",
             "Wave modes as the minimum-cost zone traversal. "
             "Why light-like behavior belongs to the Forward/Expansion propagation family. "
             "The cheapest path through the box. "
             "Background recurrence vs durable objecthood.",
             [
                 ("25.1_minimum_cost_zone_traversal",
                  "Minimum-Cost Zone Traversal"),
                 ("25.2_light_like_behavior_in_forward_expansion",
                  "Light-Like Behavior in the Forward/Expansion Family"),
                 ("25.3_cheapest_path_through_the_box",
                  "The Cheapest Path Through the Box"),
                 ("25.4_propagation_vs_objecthood",
                  "Background Recurrence vs Durable Objecthood"),
             ]),
            (26, "chapter_26_comparison_with_existing_theories",
             "Comparison with Existing Theories",
             "Thermodynamics and dissipative structure (Prigogine). "
             "Landau-Ginzburg models. Decoherence and recursive failure. "
             "Nuclear stability and retention theory. Complex systems and survival selection. "
             "Topological solitons (Skyrme). 't Hooft on topology in field theory. "
             "Kibble-Zurek on defect formation. What ICHTB adds and where it remains incomplete.",
             [
                 ("26.1_thermodynamics_and_dissipative_structures",
                  "Thermodynamics and Dissipative Structures — Prigogine"),
                 ("26.2_landau_ginzburg_models",
                  "Landau-Ginzburg Models"),
                 ("26.3_decoherence_and_recursive_failure",
                  "Decoherence and Recursive Failure"),
                 ("26.4_nuclear_stability_and_retention_theory",
                  "Nuclear Stability and Retention Theory"),
                 ("26.5_skyrme_t_hooft_kibble_zurek",
                  "Skyrme, 't Hooft, Kibble-Zurek — Topological Foundations"),
                 ("26.6_what_ichtb_adds_and_where_it_remains_incomplete",
                  "What ICHTB Adds and Where It Remains Incomplete"),
             ]),
        ],
    },
]

APPENDICES = [
    ("appendix_a", "A", "Master Equation — Full Derivation"),
    ("appendix_b", "B", "Zone Operator Reference and PDE Catalog"),
    ("appendix_c", "C", "Membrane Mathematics — Inter-Pyramid Boundary Conditions"),
    ("appendix_d", "D", "Hat-Counting Navigation System — Complete Algorithm"),
    ("appendix_e", "E", "Excitation Ledger with ICHTB Addresses"),
    ("appendix_f", "F", "The Phase Chart and Survival Map"),
    ("appendix_g", "G", "Notation, Symbols, and Conventions"),
    ("appendix_h", "H", "Glossary of ICHTB and CTS Terms"),
    ("appendix_i", "I", "Key Figures and Their Contributions"),
]

# ── Build ──────────────────────────────────────────────────────────────────────

def write(path, content):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  wrote {path}")

# Index
write(ROOT / "index.md", """\
# Astrosynthesis
## The Complete Account of Structural Emergence

**Book 3.0** — The first account in which the narrative of 1.0 and the ICHTB
mechanics of 2.0 are written together as a single complete and mathematically
correct work.

---

- [Preface](00_preface/README.md)
- [Part I: The Geometry of Pre-Emergence](part_i_geometry_of_pre_emergence/README.md)
- [Part II: The Excitation Taxonomy in ICHTB Coordinates](part_ii_excitation_taxonomy_in_ichtb_coordinates/README.md)
- [Part III: Persistence Mechanics — Grounded in ICHTB Geometry](part_iii_persistence_mechanics/README.md)
- [Part IV: The Survival Map — ICHTB Edition](part_iv_the_survival_map/README.md)
- [Part V: Matter, Shells, and Stability](part_v_matter_shells_and_stability/README.md)
- [Part VI: Implications](part_vi_implications/README.md)
- [Conclusion](conclusion/README.md)
- [Appendices](appendices/README.md)
""")

# Preface
write(ROOT / "00_preface" / "README.md", """\
# Preface

## What Astrosynthesis Is

Photosynthesis describes an invisible process — light absorbed by a leaf,
converted into the structure of a plant. You cannot see it happen. You only
see the result: growth, mass, form where there was none.

Astrosynthesis is the same idea applied to the deepest level of reality.
It describes the invisible process by which structure itself becomes possible —
how nothing organizes into something, how pre-geometric recursion seeds the
emergence of dimension, form, and matter.

## What 1.0 and 2.0 Established

Book 1.0 told the narrative correctly: the Collapse Tension Substrate,
the persistence framework, the excitation taxonomy, the survival map.
It got the story right.

Book 2.0 built the mechanics: the Inverse Heisenberg Cartesian Tensor Box,
the imaginary center i₀, the six zones, the master equation, hat-counting.
It got the address system right.

## What 3.0 Says for the First Time

Neither book was written against the other. 3.0 is the first account where
the narrative and the mathematics are aligned from the first page — where
every claim in the story has an address in the box, and every address in
the box has a role in the story.

This is also the first account that includes the membrane mathematics:
the inter-pyramid interfaces that originate from i₀ and govern all
zone-to-zone transitions. That piece was missing from both prior accounts.

## On Mathematical Rigor and Credit

This book is math-heavy by design. Every structural claim is supported by
equations that can be solved. Where the mathematics was developed by others —
from Noether to Skyrme to 't Hooft to Prigogine — we say so explicitly and
give full credit. We are not claiming anyone got science wrong. We are
following the mathematics where it leads and reporting what it says about
the deep process of emergence.

*Content to be completed.*
""")

# Conclusion
write(ROOT / "conclusion" / "README.md", """\
# Conclusion: Astrosynthesis

*The invisible process that makes structure possible — stated completely for the first time.*

*Content to be completed.*
""")

# Appendices index
app_lines = "# Appendices\n\n"
for slug, letter, title in APPENDICES:
    app_lines += f"- [Appendix {letter}: {title}]({slug}.md)\n"
write(ROOT / "appendices" / "README.md", app_lines)

for slug, letter, title in APPENDICES:
    write(ROOT / "appendices" / f"{slug}.md",
          f"# Appendix {letter}: {title}\n\n*Content to be completed.*\n")

# Parts, Chapters, Sections
for part in PARTS:
    part_path = ROOT / part["slug"]

    # Part README
    ch_list = "\n".join(
        f"- [Chapter {ch}: {title}]({slug}/README.md)"
        for ch, slug, title, _, __ in part["chapters"]
    )
    write(part_path / "README.md",
          f"# Part {part['num']}: {part['title']}\n\n{ch_list}\n")

    for ch_num, ch_slug, ch_title, ch_summary, sections in part["chapters"]:
        ch_path = part_path / ch_slug

        # Section links for chapter README
        sec_links = "\n".join(
            f"- [{sec_slug.split('_', 1)[0].upper()} {sec_title}]"
            f"({sec_slug}/README.md)"
            for sec_slug, sec_title in sections
        )
        write(ch_path / "README.md",
              f"# Chapter {ch_num}: {ch_title}\n\n"
              f"> {ch_summary}\n\n"
              f"## Sections\n\n{sec_links}\n")

        # Section stubs
        for sec_slug, sec_title in sections:
            write(ch_path / sec_slug / "README.md",
                  f"# {sec_slug.split('_', 1)[0].upper()} {sec_title}\n\n"
                  f"*Content to be completed.*\n")

print("\nScaffold complete.")
print(f"Root: {ROOT}")
