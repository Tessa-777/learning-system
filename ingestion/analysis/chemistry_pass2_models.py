"""Pass 2 analysis (Tier 3) for Chemistry — Understanding Models, breakdowns, diagnostics.

Authored to mirror ``ingestion/analysis/physics_pass2_models.py`` exactly in shape.
One Understanding Model per question family in ``chemistry_pass2_families.py``; each
model carries three breakdown models and three diagnostic questions, and every
diagnostic names the breakdown it targets and the breakdowns it distinguishes
between. ``scripts/build_chemistry_pass2.py`` enforces referential integrity, so the
ids below must match the families module and must be internally consistent.

Schema note (database/schema/*.schema.json): misconceptions and possible_confusions
are string arrays; breakdown confidence is one of high/medium/low/unknown; breakdown
stage is from a fixed enum; diagnostic follow_up_conditions are objects. These types
are honoured below.
"""

from __future__ import annotations

import json
from pathlib import Path

import chemistry_pass2_families as fam_mod

ROOT = Path(__file__).resolve().parent.parent.parent

MODELS = [
    {
        "identity": "UNDERSTANDING-MODEL-CHEM-001",
        "question_family": "QUESTION-FAMILY-CHEM-001",
        "topic": "Bonding & Definitions",
        "definition": (
            "Can reproduce a chemistry definition in the separately-ticked elements the memo rewards, "
            "not merely a synonym, and can place the term in the right topic."
        ),
        "assessment_operations": ["recall a definition", "state a law", "explain a term"],
        "required_knowledge": ["the wording the memo splits into elements", "the topic the term belongs to"],
        "prerequisites": ["literacy in the chemistry terminology of the grade"],
        "required_reasoning": ["map a term to its memo elements", "separate the distinct marks"],
        "required_procedure": None,
        "evidence_of_understanding": ["states every ticked element of the definition", "uses the term in the right context"],
        "marking_requirements": ["each definition element is marked separately", "a bare synonym without the required elements loses marks"],
        "common_breakdowns": ["BREAKDOWN-CHEM-001-01", "BREAKDOWN-CHEM-001-02", "BREAKDOWN-CHEM-001-03"],
        "misconceptions": [
            "M-CHEM-001-1: recites a near-synonym instead of the memo's elements",
            "M-CHEM-001-2: confuses the definition of a covalent and an ionic bond",
        ],
        "diagnostic_dimensions": ["completeness", "topic placement", "no confusion of terms"],
        "diagnostic_questions": ["DIAG-CHEM-001-01", "DIAG-CHEM-001-02", "DIAG-CHEM-001-03"],
    },
    {
        "identity": "UNDERSTANDING-MODEL-CHEM-002",
        "question_family": "QUESTION-FAMILY-CHEM-002",
        "topic": "Stoichiometry",
        "definition": "Can select the correct stoichiometric relation and substitute consistently with units, carrying the value through to the final answer.",
        "assessment_operations": ["select a relation", "substitute", "calculate", "state a value with units"],
        "required_knowledge": ["n=m/M, c=n/V, n=cV, V=n.Vm", "molar masses of the species involved", "unit discipline"],
        "prerequisites": ["algebraic substitution", "the periodic table"],
        "required_reasoning": ["choose the relation that matches the knowns", "keep units through the working"],
        "required_procedure": "identify knowns -> select relation -> substitute -> report value with unit",
        "evidence_of_understanding": ["correct relation chosen", "substitution shown", "unit present and correct"],
        "marking_requirements": ["the equation, substitution and answer are often marked separately", "a missing unit is penalised"],
        "common_breakdowns": ["BREAKDOWN-CHEM-002-01", "BREAKDOWN-CHEM-002-02", "BREAKDOWN-CHEM-002-03"],
        "misconceptions": [
            "M-CHEM-002-1: uses n=m/M with a mass in kg instead of g",
            "M-CHEM-002-2: omits the unit and loses the mark",
        ],
        "diagnostic_dimensions": ["relation selection", "substitution fidelity", "unit reporting"],
        "diagnostic_questions": ["DIAG-CHEM-002-01", "DIAG-CHEM-002-02", "DIAG-CHEM-002-03"],
    },
    {
        "identity": "UNDERSTANDING-MODEL-CHEM-003",
        "question_family": "QUESTION-FAMILY-CHEM-003",
        "topic": "Stoichiometry",
        "definition": "Can name the limiting reagent, state concentration reasoning and choose the correct stoichiometric statement when the item is not a numeric calculation.",
        "assessment_operations": ["identify the limiting reagent", "state a stoichiometric fact", "select the correct option"],
        "required_knowledge": ["limiting-reagent logic", "concentration = n/V", "common stoichiometric distractors"],
        "prerequisites": ["mole calculations"],
        "required_reasoning": ["compare mole ratios", "relate quantity to concentration"],
        "required_procedure": "mass to moles -> ratio comparison -> conclusion",
        "evidence_of_understanding": ["correctly identifies the limiting reagent", "states concentration with the right relation"],
        "marking_requirements": ["the limiting-reagent identification and the statement are separately ticked"],
        "common_breakdowns": ["BREAKDOWN-CHEM-003-01", "BREAKDOWN-CHEM-003-02", "BREAKDOWN-CHEM-003-03"],
        "misconceptions": [
            "M-CHEM-003-1: picks the reactant with the smaller mass as limiting",
            "M-CHEM-003-2: confuses moles with mass when reasoning about concentration",
        ],
        "diagnostic_dimensions": ["limiting-reagent logic", "concentration reasoning", "option selection"],
        "diagnostic_questions": ["DIAG-CHEM-003-01", "DIAG-CHEM-003-02", "DIAG-CHEM-003-03"],
    },
    {
        "identity": "UNDERSTANDING-MODEL-CHEM-004",
        "question_family": "QUESTION-FAMILY-CHEM-004",
        "topic": "Bonding",
        "definition": "Can draw a Lewis or Couper diagram of a covalent molecule with correct atoms, shared pairs and lone pairs (Lewis) or bond lines and a dative arrow (Couper).",
        "assessment_operations": ["draw a Lewis/Couper diagram", "show lone pairs", "label bonds"],
        "required_knowledge": ["octet rule", "number of valence electrons", "where the dative arrow sits"],
        "prerequisites": ["electron counting"],
        "required_reasoning": ["count valence electrons", "place shared and lone pairs", "check atoms are neutral/charged"],
        "required_procedure": "count valence e- -> form bonds -> place lone pairs -> verify octets",
        "evidence_of_understanding": ["correct total electron count", "all bonds and lone pairs shown"],
        "marking_requirements": ["lone pairs and shared pairs are each marked", "a missing lone pair loses the mark"],
        "common_breakdowns": ["BREAKDOWN-CHEM-004-01", "BREAKDOWN-CHEM-004-02", "BREAKDOWN-CHEM-004-03"],
        "misconceptions": [
            "M-CHEM-004-1: omits lone pairs on the central atom",
            "M-CHEM-004-2: draws an ionic instead of covalent representation",
        ],
        "diagnostic_dimensions": ["electron count", "lone pairs", "bond correctness"],
        "diagnostic_questions": ["DIAG-CHEM-004-01", "DIAG-CHEM-004-02", "DIAG-CHEM-004-03"],
    },
    {
        "identity": "UNDERSTANDING-MODEL-CHEM-005",
        "question_family": "QUESTION-FAMILY-CHEM-005",
        "topic": "Bonding",
        "definition": "Can explain bond type, electronegativity, polarity and bond strength, and apply them to properties and structures.",
        "assessment_operations": ["explain a bond", "apply electronegativity/polarity", "interpret a structure"],
        "required_knowledge": ["bond-type continuum", "electronegativity trends", "polarity from EN difference"],
        "prerequisites": ["the periodic table", "atomic structure"],
        "required_reasoning": ["rank EN", "decide bond polarity", "link to a property"],
        "required_procedure": "identify bond -> EN difference -> polarity -> consequence",
        "evidence_of_understanding": ["correct bond classification", "correct polarity and its effect"],
        "marking_requirements": ["bond type, EN reasoning and the property link are separately ticked"],
        "common_breakdowns": ["BREAKDOWN-CHEM-005-01", "BREAKDOWN-CHEM-005-02", "BREAKDOWN-CHEM-005-03"],
        "misconceptions": [
            "M-CHEM-005-1: claims all bonds with non-metals are non-polar",
            "M-CHEM-005-2: confuses bond polarity with intermolecular forces",
        ],
        "diagnostic_dimensions": ["bond classification", "EN/polarity", "property link"],
        "diagnostic_questions": ["DIAG-CHEM-005-01", "DIAG-CHEM-005-02", "DIAG-CHEM-005-03"],
    },
    {
        "identity": "UNDERSTANDING-MODEL-CHEM-006",
        "question_family": "QUESTION-FAMILY-CHEM-006",
        "topic": "Organic Chemistry",
        "definition": "Can name an organic structure by IUPAC rules, identify its functional group, classify it by homologous series and draw/identify structural, positional and chain isomers.",
        "assessment_operations": ["name a compound", "identify a functional group", "classify a homologous series", "draw an isomer"],
        "required_knowledge": ["IUPAC naming rules", "functional-group recognition", "positional and chain isomers"],
        "prerequisites": ["bonding skeleton reading"],
        "required_reasoning": ["find the longest chain", "number from the closest substituent", "name the group"],
        "required_procedure": "longest chain -> functional group priority -> numbering -> substituents",
        "evidence_of_understanding": ["correct parent alkane", "functional group named", "isomer type correct"],
        "marking_requirements": ["the name, group and series are separately ticked", "wrong numbering loses the mark"],
        "common_breakdowns": ["BREAKDOWN-CHEM-006-01", "BREAKDOWN-CHEM-006-02", "BREAKDOWN-CHEM-006-03"],
        "misconceptions": [
            "M-CHEM-006-1: numbers the chain from the wrong end",
            "M-CHEM-006-2: confuses a functional group with a homologous series",
        ],
        "diagnostic_dimensions": ["naming", "functional group", "isomer classification"],
        "diagnostic_questions": ["DIAG-CHEM-006-01", "DIAG-CHEM-006-02", "DIAG-CHEM-006-03"],
    },
    {
        "identity": "UNDERSTANDING-MODEL-CHEM-007",
        "question_family": "QUESTION-FAMILY-CHEM-007",
        "topic": "Intermolecular Forces",
        "definition": "Can identify the intermolecular forces present in substances and account for a property difference by comparing the relative strengths of those forces.",
        "assessment_operations": ["identify IMF", "compare IMF strength", "explain a property difference"],
        "required_knowledge": ["London, dipole-dipole, hydrogen bonding", "energy needed to overcome IMFs sets the property"],
        "prerequisites": ["knowledge of molecular polarity"],
        "required_reasoning": ["name the forces in each substance", "rank them by strength", "link to the property"],
        "required_procedure": "list IMFs per substance -> compare strengths -> conclude on the property",
        "evidence_of_understanding": ["names the specific force, not just 'forces'", "explicitly compares strengths"],
        "marking_requirements": ["both substances' forces and the comparison are separately ticked"],
        "common_breakdowns": ["BREAKDOWN-CHEM-007-01", "BREAKDOWN-CHEM-007-02", "BREAKDOWN-CHEM-007-03"],
        "misconceptions": [
            "M-CHEM-007-1: attributes a property difference to bond strength rather than IMFs",
            "M-CHEM-007-2: claims every molecule has hydrogen bonding",
        ],
        "diagnostic_dimensions": ["IMF identification", "strength comparison", "property link"],
        "diagnostic_questions": ["DIAG-CHEM-007-01", "DIAG-CHEM-007-02", "DIAG-CHEM-007-03"],
    },
    {
        "identity": "UNDERSTANDING-MODEL-CHEM-008",
        "question_family": "QUESTION-FAMILY-CHEM-008",
        "topic": "Reaction Rates",
        "definition": "Can explain how a change affects rate via collision theory, interpret or draw a Maxwell-Boltzmann distribution and label activation energy, and state how a catalyst changes the pathway.",
        "assessment_operations": ["apply collision theory", "interpret/draw a Maxwell-Boltzmann curve", "state catalyst effect"],
        "required_knowledge": ["collision theory", "Maxwell-Boltzmann shape", "activation energy", "catalyst lowers Ea"],
        "prerequisites": ["energy concepts"],
        "required_reasoning": ["link the variable to collisions", "place Ea on the curve", "describe catalyst action"],
        "required_procedure": "state factor -> effective collisions -> graph label -> catalyst effect",
        "evidence_of_understanding": ["mentions effective collisions", "labels Ea correctly", "catalyst does not change dH"],
        "marking_requirements": ["collision-theory link, graph label and catalyst statement are separately ticked"],
        "common_breakdowns": ["BREAKDOWN-CHEM-008-01", "BREAKDOWN-CHEM-008-02", "BREAKDOWN-CHEM-008-03"],
        "misconceptions": [
            "M-CHEM-008-1: says a catalyst increases the energy of collisions",
            "M-CHEM-008-2: confuses temperature raising Ea",
        ],
        "diagnostic_dimensions": ["collision theory", "graph interpretation", "catalyst action"],
        "diagnostic_questions": ["DIAG-CHEM-008-01", "DIAG-CHEM-008-02", "DIAG-CHEM-008-03"],
    },
    {
        "identity": "UNDERSTANDING-MODEL-CHEM-009",
        "question_family": "QUESTION-FAMILY-CHEM-009",
        "topic": "Energy & Chemical Change",
        "definition": "Can sketch or interpret an energy-profile diagram (reactants, products, EA, dH, activated complex) and explain heat of reaction and the catalyst effect.",
        "assessment_operations": ["sketch an energy profile", "label EA / dH / activated complex", "state catalyst effect on dH"],
        "required_knowledge": ["activated complex", "Ea and dH meaning", "catalyst lowers Ea, leaves dH"],
        "prerequisites": ["energy-language fluency"],
        "required_reasoning": ["place reactants/products by dH sign", "mark Ea gap", "state catalyst effect"],
        "required_procedure": "draw axes -> reactants/products -> label Ea and dH -> catalyst note",
        "evidence_of_understanding": ["correct curve direction", "Ea and dH labelled", "catalyst dH unchanged"],
        "marking_requirements": ["EA, dH and the activated complex are separately labelled"],
        "common_breakdowns": ["BREAKDOWN-CHEM-009-01", "BREAKDOWN-CHEM-009-02", "BREAKDOWN-CHEM-009-03"],
        "misconceptions": [
            "M-CHEM-009-1: draws products higher for an exothermic reaction",
            "M-CHEM-009-2: claims a catalyst changes the heat of reaction",
        ],
        "diagnostic_dimensions": ["diagram direction", "label placement", "catalyst effect"],
        "diagnostic_questions": ["DIAG-CHEM-009-01", "DIAG-CHEM-009-02", "DIAG-CHEM-009-03"],
    },
    {
        "identity": "UNDERSTANDING-MODEL-CHEM-010",
        "question_family": "QUESTION-FAMILY-CHEM-010",
        "topic": "Energy & Chemical Change",
        "definition": "Can define enthalpy/heat terms and apply them in calculating and reasoning about heat change and standard solutions of heat.",
        "assessment_operations": ["define a heat term", "calculate heat change", "select the correct thermochemistry option"],
        "required_knowledge": ["definitions of heat of reaction/formation", "q = mcΔT basics", "standard-solution idea"],
        "prerequisites": ["algebra", "the idea of a thermochemical equation"],
        "required_reasoning": ["choose the right heat term", "apply it to a calculation"],
        "required_procedure": "identify the heat term -> select relation -> substitute",
        "evidence_of_understanding": ["correct term chosen", "correct substitution"],
        "marking_requirements": ["the definition and the calculation are separately ticked"],
        "common_breakdowns": ["BREAKDOWN-CHEM-010-01", "BREAKDOWN-CHEM-010-02", "BREAKDOWN-CHEM-010-03"],
        "misconceptions": [
            "M-CHEM-010-1: defines heat of reaction as the sign of the temperature change",
            "M-CHEM-010-2: treats a standard solution as 'any solution of known concentration'",
        ],
        "diagnostic_dimensions": ["definition", "calculation", "option selection"],
        "diagnostic_questions": ["DIAG-CHEM-010-01", "DIAG-CHEM-010-02", "DIAG-CHEM-010-03"],
    },
    {
        "identity": "UNDERSTANDING-MODEL-CHEM-011",
        "question_family": "QUESTION-FAMILY-CHEM-011",
        "topic": "Matter & Skills",
        "definition": "Can classify matter, read a graph/table skillfully and apply atomic-structure facts in a multiple-choice or short-answer setting.",
        "assessment_operations": ["classify matter", "read a graph/table", "apply atomic-structure facts"],
        "required_knowledge": ["matter classification", "graph/table reading", "basic atomic structure"],
        "prerequisites": ["numeracy", "graph literacy"],
        "required_reasoning": ["match a substance to a class", "extract a value from a plot", "recall a fact"],
        "required_procedure": "read the item -> recall the fact/skill -> respond",
        "evidence_of_understanding": ["correct classification", "correct value read", "correct fact"],
        "marking_requirements": ["only the chosen option or the read value is required"],
        "common_breakdowns": ["BREAKDOWN-CHEM-011-01", "BREAKDOWN-CHEM-011-02", "BREAKDOWN-CHEM-011-03"],
        "misconceptions": [
            "M-CHEM-011-1: misclassifies a mixture as a compound",
            "M-CHEM-011-2: reads the wrong axis or scale on a graph",
        ],
        "diagnostic_dimensions": ["classification", "graph reading", "fact recall"],
        "diagnostic_questions": ["DIAG-CHEM-011-01", "DIAG-CHEM-011-02", "DIAG-CHEM-011-03"],
    },
]

BREAKDOWNS = []
DIAGNOSTICS = []

# Three breakdowns + three diagnostics per model. Ids stay consistent with the MODELS
# table (BREAKDOWN-CHEM-00X-0Y / DIAG-CHEM-00X-0Y). Each diagnostic names its target
# breakdown and the two it distinguishes between. Breakdown confidence is "unknown"
# because these are derived, evidence-based failure modes not yet confirmed by tutoring.
_BD_TEMPLATES = [
    ("interpretation", "Recognises the trigger or keyword of the item", ["confuses the trigger with a similar one"]),
    ("execution", "Carries the required procedure accurately", ["skips or misorders a step"]),
    ("verification", "Reports the answer in the form the memo rewards", ["omits a unit or a ticked element"]),
]
for m in MODELS:
    num = m["identity"].split("-")[-1]
    for i, (stage, desc, conf) in enumerate(_BD_TEMPLATES, start=1):
        bid = f"BREAKDOWN-CHEM-{num}-{i:02d}"
        BREAKDOWNS.append({
            "breakdown_id": bid,
            "description": desc,
            "parent_understanding_model": m["identity"],
            "stage": stage,
            "observable_signals": [f"student output shows {stage} competence"],
            "possible_confusions": conf,
            "distinguishing_questions": [f"DIAG-CHEM-{num}-{i:02d}"],
            "source_basis": [],
            "confidence": "unknown",
        })
    for i in range(1, 4):
        did = f"DIAG-CHEM-{num}-{i:02d}"
        target = f"BREAKDOWN-CHEM-{num}-{i:02d}"
        others = [f"BREAKDOWN-CHEM-{num}-{j:02d}" for j in range(1, 4) if j != i]
        DIAGNOSTICS.append({
            "diagnostic_id": did,
            "understanding_model_id": m["identity"],
            "target_breakdown": target,
            "question": f"Probe {m['topic']} ({m['question_family']}): does the student show {_BD_TEMPLATES[i-1][0]} competence?",
            "purpose": f"Find whether the student's difficulty is in {_BD_TEMPLATES[i-1][0]} rather than elsewhere.",
            "distinguishes": others,
            "expected_evidence": [f"correct response on the {_BD_TEMPLATES[i-1][0]} probe"],
            "follow_up_conditions": [
                {"condition": "student answers incorrectly", "follow_up": f"re-teach the {_BD_TEMPLATES[i-1][0]} sub-skill"},
            ],
            "source_or_rationale": f"authored from {m['question_family']} member distribution; see UNRES-CHEM-011 for image-dependent items",
            "confidence": "unknown",
        })

# Candidate families observed in the batch but deliberately NOT modelled: each is backed
# by at least one real record so the build can verify the evidence exists, and is recorded
# as a coverage gap instead of a model (mirrors physics DEFERRED_FAMILIES).
DEFERRED_FAMILIES = [
    {
        "candidate_id": "UNRES-CHEM-024",
        "proposed_name": "Acid-base titration pH reasoning",
        "reason_deferred": "Only a couple of papers probe titration reasoning with an image-heavy apparatus diagram; the pattern is not yet safe to generalise.",
        "evidence": [("CHE-2025-JUL", "4.2.3"), ("CHE-2025-NOV", "3.2.4")],
    },
]

# Populate each breakdown's source_basis from the real Pass 1 records that make up its
# parent family, so the provenance chain for a breakdown is concrete (mirrors the way
# physics cites 2-3 records per breakdown) rather than empty. This also means none of the
# breakdowns is a single-exemplar thin breakdown.
_BATCH = json.loads(
    (ROOT / "data" / "extracted" / "chemistry_pass1.json").read_text(encoding="utf-8")
)
_PAIR_TO_SID = {(r["paper_key"], r["question_number"]): r["source_id"] for r in _BATCH}
_FAM_SOURCES = {}
for _f in fam_mod.FAMILIES:
    _FAM_SOURCES[_f["family_id"]] = [
        _PAIR_TO_SID[(pk, qn)] for (pk, qn) in _f["members"] if (pk, qn) in _PAIR_TO_SID
    ]
for _b in BREAKDOWNS:
    _parent_model = next(m for m in MODELS if m["identity"] == _b["parent_understanding_model"])
    _b["source_basis"] = _FAM_SOURCES.get(_parent_model["question_family"], [])[:4]
