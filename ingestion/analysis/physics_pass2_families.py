"""Pass 2 analysis (Tier 2/3) for Physics — question families.

Authored from the Physics Pass 1 batch in ``data/extracted/physics_pass1.json``
(4 papers, 238 question records). Every family cites member question records by
(paper_key, question_number); ``scripts/build_physics_pass2.py`` resolves these
to Pass 1 ``source_id`` values and refuses to emit a family whose members do not
exist in the batch, whose members overlap another family, or that has fewer than
two members (TWO_PASS_PROMPTS: a family with one member is a single_exemplar and
belongs in unresolved_items).

Members are a partition: each extracted question record is assigned to at most
one family, so family membership is a classification decision, not a count that
can be inflated by re-using the same evidence.
"""

# (paper_key, question_number)
FAMILIES = [
    {
        "family_id": "QUESTION-FAMILY-PHY-001",
        "name": "State a physics term to the memo's two-part definition",
        "definition": (
            "The student must reproduce a definition or law in the exact elements the marking "
            "guidelines reward, not merely a synonym. Across the batch these items are worth 1-2 "
            "marks and the memo consistently splits the definition into two separately marked "
            "elements (e.g. 'opposes motion' + 'parallel to the contact surface')."
        ),
        "topics": ["Mechanics-Forces", "Mechanics-Motion", "Electric Circuits", "Work Energy Power"],
        "assessment_operations": ["recall a definition", "state a law", "explain a term"],
        "distinguishing_features": [
            "command verbs: Define / State / Explain what is meant by / What is",
            "1-2 marks, no calculation space provided",
            "memo answer is a phrase split into two ticked elements, often annotated 'AON' "
            "(any other correct wording accepted)",
            "the same term recurs across years with near-identical memo wording "
            "(velocity, friction, Newton's first law, work-energy theorem)",
        ],
        "typical_marks_range": [1, 2],
        "members": [
            ("PHY-2019-MY", "2.1.1"), ("PHY-2019-MY", "3.1.1"), ("PHY-2019-MY", "4.1.1"),
            ("PHY-2019-MY", "4.2.1"), ("PHY-2019-MY", "5.1"), ("PHY-2019-MY", "5.2"),
            ("PHY-2019-MY", "7.1"), ("PHY-2019-MY", "7.3"),
            ("PHY-2021-NOV", "2.1.2"), ("PHY-2021-NOV", "3.1"), ("PHY-2021-NOV", "4.3.1"),
            ("PHY-2021-NOV", "5.2"), ("PHY-2021-NOV", "5.4"), ("PHY-2021-NOV", "6.1.1"),
            ("PHY-2021-NOV", "6.2.3"), ("PHY-2021-NOV", "7.1.1"), ("PHY-2021-NOV", "7.2.1"),
            ("PHY-2023-MY", "2.1"), ("PHY-2023-MY", "3.1"), ("PHY-2023-MY", "5.1"),
            ("PHY-2023-MY", "6.1"), ("PHY-2023-MY", "7.1.2"), ("PHY-2023-MY", "7.2.1"),
            ("PHY-2023-MY", "8.1"), ("PHY-2023-MY", "8.3"), ("PHY-2023-MY", "8.5"),
            ("PHY-2023-MY", "9.1"), ("PHY-2023-MY", "9.2"),
            ("PHY-2023-MY", "4.1"),
            ("PHY-2025-NOV", "1.1.1"), ("PHY-2025-NOV", "2.1"), ("PHY-2025-NOV", "3.2"),
            ("PHY-2025-NOV", "4.5"), ("PHY-2025-NOV", "5.1"), ("PHY-2025-NOV", "5.4"),
            ("PHY-2025-NOV", "6.1.1"), ("PHY-2025-NOV", "9.1"),
        ],
    },
    {
        "family_id": "QUESTION-FAMILY-PHY-002",
        "name": "Substitute into a data-sheet equation and carry the answer through",
        "definition": (
            "A mechanics/energy calculation in which the competence is choosing the correct "
            "equation, substituting with a consistent sign convention and units, and reporting "
            "the final value. The memos mark the equation, the substitution and the answer as "
            "separate marks, and frequently mark a sign or unit separately."
        ),
        "topics": ["Mechanics-Motion", "Mechanics-Forces", "Work Energy Power"],
        "assessment_operations": ["select an equation", "substitute", "calculate", "state a value with units"],
        "distinguishing_features": [
            "command verbs: Calculate / Determine",
            "3-5 marks with the memo showing equation -> substitution -> answer",
            "memo frequently annotates 'must show that the acceleration is negative' or marks a "
            "unit separately",
            "later sub-parts are marked 'coe'/'COE' (consistent with an earlier answer), so the "
            "method mark is separable from the accuracy mark",
        ],
        "typical_marks_range": [3, 5],
        "members": [
            ("PHY-2019-MY", "2.1.3"), ("PHY-2019-MY", "2.1.4"), ("PHY-2019-MY", "2.1.5"),
            ("PHY-2019-MY", "2.2.2"), ("PHY-2019-MY", "2.2.3"), ("PHY-2019-MY", "2.2.4"),
            ("PHY-2019-MY", "3.1.3"), ("PHY-2019-MY", "3.2.1"),
            ("PHY-2021-NOV", "2.1.3"), ("PHY-2021-NOV", "2.1.5"), ("PHY-2021-NOV", "2.2.1"),
            ("PHY-2021-NOV", "2.2.2"), ("PHY-2021-NOV", "3.4"), ("PHY-2021-NOV", "3.5"),
            ("PHY-2021-NOV", "3.6"), ("PHY-2021-NOV", "3.10"), ("PHY-2021-NOV", "4.3.2"),
            ("PHY-2021-NOV", "4.3.3"), ("PHY-2021-NOV", "5.3"), ("PHY-2021-NOV", "6.2.2"),
            ("PHY-2023-MY", "2.2"), ("PHY-2023-MY", "2.3"), ("PHY-2023-MY", "2.4"),
            ("PHY-2023-MY", "2.6.1"), ("PHY-2023-MY", "2.6.2"), ("PHY-2023-MY", "2.6.3"),
            ("PHY-2023-MY", "3.2"), ("PHY-2023-MY", "3.3"), ("PHY-2023-MY", "4.5"),
            ("PHY-2023-MY", "4.6"),
            ("PHY-2023-MY", "5.3"), ("PHY-2023-MY", "6.4"), ("PHY-2023-MY", "6.5"),
            ("PHY-2025-NOV", "1.2"), ("PHY-2025-NOV", "2.2"), ("PHY-2025-NOV", "2.3"),
            ("PHY-2025-NOV", "3.3"),
        ],
    },
    {
        "family_id": "QUESTION-FAMILY-PHY-003",
        "name": "Read and interpret a motion graph (value, interval, gradient, area)",
        "definition": (
            "The student must extract information from a given velocity-time or position-time "
            "graph: read a value or interval, identify where the sign changes, compare gradients, "
            "or describe the motion a section represents. No new graph is drawn."
        ),
        "topics": ["Mechanics-Motion", "Mechanics-Motion graphs"],
        "assessment_operations": ["read a graph", "interpret a gradient", "interpret an area", "describe motion"],
        "distinguishing_features": [
            "a graph is printed on the paper and the answer is read off it",
            "asks 'during which interval', 'at which point', 'state the magnitude at t = ...', "
            "'describe the motion between ...'",
            "memo answers are short (an interval label, a value, or a two-element description "
            "such as 'decreasing velocity' + 'up')",
        ],
        "typical_marks_range": [1, 4],
        "members": [
            ("PHY-2019-MY", "2.1.2"), ("PHY-2019-MY", "3.1.2"), ("PHY-2019-MY", "3.1.6"),
            ("PHY-2021-NOV", "3.2"), ("PHY-2021-NOV", "3.3"), ("PHY-2021-NOV", "3.7"),
            ("PHY-2023-MY", "4.2"), ("PHY-2023-MY", "4.3"), ("PHY-2023-MY", "4.4"),
            ("PHY-2023-MY", "4.8"),
            ("PHY-2025-NOV", "1.1.2"), ("PHY-2025-NOV", "1.1.3"), ("PHY-2025-NOV", "1.1.4"),
        ],
    },
    {
        "family_id": "QUESTION-FAMILY-PHY-004",
        "name": "Construct a graph representation from a description or another graph",
        "definition": (
            "The student must produce a sketch graph (a-t from v-t, x-t from v-t, v-t from a "
            "description, or a circuit quantity against a changing resistance) with the correct "
            "shape, sign, labelled points and relative steepness."
        ),
        "topics": ["Mechanics-Motion graphs", "Electric Circuits"],
        "assessment_operations": ["sketch a graph", "label axes and key values", "translate between representations"],
        "distinguishing_features": [
            "command verbs: Draw / Sketch a ... graph",
            "3-5 marks, and the memo allocates marks per graph feature (shape, labelled times, "
            "relative gradient, sign convention) rather than for a single answer",
            "memos explicitly allow a mirrored/reflected graph or deduct for an inconsistent "
            "sign convention",
        ],
        "typical_marks_range": [3, 5],
        "members": [
            ("PHY-2019-MY", "2.2.5"), ("PHY-2019-MY", "3.1.7"), ("PHY-2019-MY", "3.1.8"),
            ("PHY-2019-MY", "7.6"),
            ("PHY-2021-NOV", "3.8"), ("PHY-2021-NOV", "6.1.5"),
            ("PHY-2023-MY", "4.7"),
            ("PHY-2025-NOV", "1.1.5"), ("PHY-2025-NOV", "2.7"),
        ],
    },
    {
        "family_id": "QUESTION-FAMILY-PHY-005",
        "name": "Draw a labelled force diagram (free-body or vector addition)",
        "definition": (
            "The student must draw the forces on a stated object as arrows with correct "
            "direction, correct relative length and correct labels, or close a vector triangle "
            "for forces in equilibrium."
        ),
        "topics": ["Mechanics-Forces", "Mechanics-Vectors"],
        "assessment_operations": ["identify the forces on an object", "draw and label arrows", "show relative magnitude"],
        "distinguishing_features": [
            "command verbs: Draw a (fully) labelled free-body diagram / triangle of forces / "
            "vector addition diagram",
            "2-5 marks, one mark per force, and the memo penalises extra or missing arrows "
            "('dot and weight ONLY', 'minus 1 for angle not shown')",
            "several memos require the relative length of arrows to be drawn correctly "
            "('FN must be longer than Fg', 'Tension force > Friction force')",
        ],
        "typical_marks_range": [2, 5],
        "members": [
            ("PHY-2019-MY", "3.1.4"), ("PHY-2019-MY", "4.2.4"), ("PHY-2019-MY", "5.4"),
            ("PHY-2021-NOV", "2.1.4"), ("PHY-2021-NOV", "3.9"), ("PHY-2021-NOV", "4.1"),
            ("PHY-2021-NOV", "5.1"),
            ("PHY-2023-MY", "5.2"), ("PHY-2023-MY", "6.2"),
            ("PHY-2025-NOV", "2.5"), ("PHY-2025-NOV", "3.1"),
        ],
    },
    {
        "family_id": "QUESTION-FAMILY-PHY-006",
        "name": "Apply Newton's second law to a system of connected bodies",
        "definition": (
            "Two or more bodies are linked (string over a pulley, or a pulled crate and its "
            "load). The student must write Fnet = ma for each body or for the whole system, keep "
            "one consistent direction convention, and solve the simultaneous equations for "
            "acceleration and tension."
        ),
        "topics": ["Mechanics-Forces"],
        "assessment_operations": ["isolate each body", "write Fnet = ma per body", "solve simultaneously", "interpret the sign"],
        "distinguishing_features": [
            "a pulley/string or a towing arrangement links two masses, often one on an incline",
            "4-6 marks; the memo shows two separate equations and then their combination",
            "memos accept either the two-body method or the whole-system method for the same marks",
            "the tension answer is usually marked 'coe' from the acceleration",
        ],
        "typical_marks_range": [4, 6],
        "members": [
            ("PHY-2021-NOV", "5.5"), ("PHY-2021-NOV", "5.6"),
            ("PHY-2023-MY", "6.6"), ("PHY-2023-MY", "7.1.1"),
            ("PHY-2025-NOV", "4.3"),
        ],
    },
    {
        "family_id": "QUESTION-FAMILY-PHY-007",
        "name": "Resolve a force acting at an angle into components",
        "definition": (
            "A force is applied at a stated angle to the horizontal (or two forces act at "
            "angles). The student must resolve into perpendicular components, use the correct "
            "trigonometric ratio for the required direction, and combine components to get a "
            "magnitude and a direction."
        ),
        "topics": ["Mechanics-Vectors", "Mechanics-Forces"],
        "assessment_operations": ["resolve a vector", "choose sin or cos correctly", "combine components", "give a direction or bearing"],
        "distinguishing_features": [
            "an angle is printed on the diagram (12 degrees, 18/72 degrees, 30 degrees, 40 degrees)",
            "the memo shows the component expressions before the final magnitude",
            "for resultants the memo awards a separate mark for the bearing/direction statement",
            "normal-force items on a horizontal surface require subtracting the vertical "
            "component (FN = Fg - F sin theta)",
        ],
        "typical_marks_range": [2, 6],
        "members": [
            ("PHY-2019-MY", "4.1.2"), ("PHY-2019-MY", "4.2.2"),
            ("PHY-2023-MY", "6.3"),
            ("PHY-2025-NOV", "3.4"), ("PHY-2025-NOV", "4.7"),
        ],
    },
    {
        "family_id": "QUESTION-FAMILY-PHY-008",
        "name": "Predict a qualitative change, then justify it with a named relationship",
        "definition": (
            "The student must choose INCREASE / DECREASE / REMAIN THE SAME (or YES / NO, or the "
            "sign of a quantity) and then justify the choice by naming a relationship and "
            "carrying a causal chain through it. The prediction alone never earns full marks."
        ),
        "topics": ["Electric Circuits", "Mechanics-Forces", "Mechanics-Motion", "Electrostatics"],
        "assessment_operations": ["predict a direction of change", "quote a relationship", "reason causally", "evaluate a stated claim"],
        "distinguishing_features": [
            "the paper prints 'Circle: INCREASES, DECREASES or NO CHANGE' (or GREATER THAN / "
            "LESS THAN / EQUAL TO) and then a separate sub-part asking for the reason",
            "prediction is worth 1 mark and the justification 2-4 marks",
            "memos award one mark per link in the causal chain and require the formula to be "
            "named ('I = V/R', 'Vemf = Vinternal + Vexternal', 'Ff = mu FN')",
            "some items ask the student to critique another person's reasoning (2023 Q6.7)",
        ],
        "typical_marks_range": [1, 4],
        "members": [
            ("PHY-2019-MY", "5.3.2"), ("PHY-2019-MY", "7.7.1"), ("PHY-2019-MY", "7.7.2"),
            ("PHY-2021-NOV", "5.7"), ("PHY-2021-NOV", "6.1.4"), ("PHY-2021-NOV", "7.1.6"),
            ("PHY-2021-NOV", "7.1.7"), ("PHY-2021-NOV", "7.2.2"),
            ("PHY-2023-MY", "2.5"), ("PHY-2023-MY", "6.7"), ("PHY-2023-MY", "8.7"),
            ("PHY-2023-MY", "8.8"), ("PHY-2023-MY", "9.3"), ("PHY-2023-MY", "9.4"),
            ("PHY-2025-NOV", "4.1"), ("PHY-2025-NOV", "4.2"), ("PHY-2025-NOV", "4.4"),
            ("PHY-2025-NOV", "6.2.1"), ("PHY-2025-NOV", "6.2.2"), ("PHY-2025-NOV", "8.2"),
            ("PHY-2025-NOV", "8.3"), ("PHY-2025-NOV", "9.5"),
        ],
    },
    {
        "family_id": "QUESTION-FAMILY-PHY-009",
        "name": "Analyse a resistor network (reduce, then apply Ohm / power / emf)",
        "definition": (
            "A circuit with series and/or parallel resistors, meters and sometimes internal "
            "resistance. The student must reduce the network to an equivalent resistance, then "
            "apply V = IR, P = VI / P = I2R / P = V2/R or emf = I(Rext + r) in the right order, "
            "carrying intermediate values forward."
        ),
        "topics": ["Electric Circuits"],
        "assessment_operations": ["identify series and parallel groupings", "reduce to an equivalent resistance", "apply Ohm's law / power / emf equations", "carry intermediate values forward"],
        "distinguishing_features": [
            "a circuit diagram with two or more resistors, a switch, an ammeter and/or voltmeter",
            "the memo marks the equivalent-resistance step separately from the current/voltage step",
            "later parts are marked 'coe' from earlier ones",
            "the 2025 items add internal resistance, requiring emf = I(Rext + r) and the "
            "lost-voltage idea",
        ],
        "typical_marks_range": [2, 5],
        "members": [
            ("PHY-2019-MY", "7.2"), ("PHY-2019-MY", "7.4.1"), ("PHY-2019-MY", "7.4.2"),
            ("PHY-2019-MY", "7.5.1"), ("PHY-2019-MY", "7.5.2"),
            ("PHY-2021-NOV", "7.1.2"), ("PHY-2021-NOV", "7.1.3"), ("PHY-2021-NOV", "7.1.4"),
            ("PHY-2021-NOV", "7.1.5"),
            ("PHY-2023-MY", "8.2"), ("PHY-2023-MY", "8.4"), ("PHY-2023-MY", "8.6"),
            ("PHY-2023-MY", "9.5"),
            ("PHY-2025-NOV", "8.1"), ("PHY-2025-NOV", "9.2"), ("PHY-2025-NOV", "9.3"),
            ("PHY-2025-NOV", "9.4"),
        ],
    },
    {
        "family_id": "QUESTION-FAMILY-PHY-010",
        "name": "Investigation: hypothesise, plot data, find the gradient and its physical meaning",
        "definition": (
            "A practical or simulated investigation. The student must state a hypothesis in the "
            "correct variable order, complete a data table, plot a graph to the memo's marking "
            "criteria (heading, labels/units, scale, plotting, line of best fit), determine the "
            "gradient with a unit, identify the physical quantity the gradient represents, and "
            "use it to find an unknown."
        ),
        "topics": ["Experimental Investigation", "Mechanics-Gravitation"],
        "assessment_operations": ["state a hypothesis", "complete a table", "plot a graph", "calculate a gradient", "interpret the gradient physically"],
        "distinguishing_features": [
            "a data table and a graph grid are printed, sometimes on a separate answer sheet",
            "the memo itemises graph marks: heading, labels and unit, scale, plotting (x2), "
            "line of best fit",
            "gradient items require a unit and a tolerance ('plus or minus 10%')",
            "the gradient is then equated to a physical quantity (1/(G m1 m2), g) to find an "
            "unknown - the highest-mark step in the chain",
            "memo note 'order matters' on hypothesis and relationship wording",
        ],
        "typical_marks_range": [1, 7],
        "members": [
            ("PHY-2019-MY", "6.1"), ("PHY-2019-MY", "6.2"), ("PHY-2019-MY", "6.3"),
            ("PHY-2019-MY", "6.4"), ("PHY-2019-MY", "6.5"),
            ("PHY-2021-NOV", "8.1.1"), ("PHY-2021-NOV", "8.1.2"), ("PHY-2021-NOV", "8.2"),
            ("PHY-2021-NOV", "8.3"), ("PHY-2021-NOV", "8.4"), ("PHY-2021-NOV", "8.5"),
            ("PHY-2021-NOV", "8.6"), ("PHY-2021-NOV", "8.7"),
            ("PHY-2025-NOV", "6.1.2"), ("PHY-2025-NOV", "6.1.3"),
        ],
    },
    {
        "family_id": "QUESTION-FAMILY-PHY-011",
        "name": "Photon and energy-level quantisation calculations",
        "definition": (
            "Using a hydrogen energy-level diagram or a stated wavelength, the student must use "
            "E = hf and E = hc/lambda, take energy differences between levels, and convert "
            "between joules and electron volts."
        ),
        "topics": ["Waves Sound Light"],
        "assessment_operations": ["count possible transitions", "take an energy difference between levels", "apply E = hf or E = hc/lambda", "convert J to eV"],
        "distinguishing_features": [
            "an energy-level diagram or a wavelength in nm is given",
            "the final answer is often required in eV, and the memo marks the conversion step",
            "the identical item set recurs in 2021 Q9 and 2023 Q10 (same diagram, same three "
            "questions), and reappears in 2025 Q7 as a laser comparison",
        ],
        "typical_marks_range": [2, 4],
        "members": [
            ("PHY-2021-NOV", "9.1"), ("PHY-2021-NOV", "9.2"), ("PHY-2021-NOV", "9.3"),
            ("PHY-2021-NOV", "9.4"), ("PHY-2021-NOV", "9.5"),
            ("PHY-2023-MY", "10.1"), ("PHY-2023-MY", "10.2"), ("PHY-2023-MY", "10.3"),
            ("PHY-2025-NOV", "7.1"), ("PHY-2025-NOV", "7.2"),
        ],
    },
    {
        "family_id": "QUESTION-FAMILY-PHY-012",
        "name": "Multiple-choice single-step concept application",
        "definition": (
            "A four-option multiple-choice item worth 2 marks in which one physics idea must be "
            "applied once (vector addition limits, sign of acceleration, Newton's third law "
            "partner, elevator scale reading, brightness in series vs parallel). No working is "
            "required and the memo gives only the correct letter."
        ),
        "topics": ["Mechanics-Vectors", "Mechanics-Motion", "Mechanics-Forces", "Electric Circuits", "Work Energy Power"],
        "assessment_operations": ["apply one concept", "eliminate distractors", "select an option"],
        "distinguishing_features": [
            "always 2 marks, always four options A-D, answered on a separate answer sheet",
            "the memo records only the letter (with two ticks) - there is no method mark and no "
            "distractor analysis, so no marking evidence exists for why the wrong options are wrong",
            "the MCQ block is Question 1 in 2019, 2021 and 2023 but is absent from the 2025 paper",
            "many items depend on a diagram that is only present as an image",
        ],
        "typical_marks_range": [2, 2],
        "members": [
            ("PHY-2019-MY", "1.1"), ("PHY-2019-MY", "1.2"), ("PHY-2019-MY", "1.3"),
            ("PHY-2019-MY", "1.4"), ("PHY-2019-MY", "1.5"), ("PHY-2019-MY", "1.6"),
            ("PHY-2019-MY", "1.7"), ("PHY-2019-MY", "1.8"),
            ("PHY-2021-NOV", "1.1"), ("PHY-2021-NOV", "1.2"), ("PHY-2021-NOV", "1.3"),
            ("PHY-2021-NOV", "1.4"), ("PHY-2021-NOV", "1.5"), ("PHY-2021-NOV", "1.6"),
            ("PHY-2021-NOV", "1.7"), ("PHY-2021-NOV", "1.8"), ("PHY-2021-NOV", "1.9"),
            ("PHY-2021-NOV", "1.10"),
            ("PHY-2023-MY", "1.1"), ("PHY-2023-MY", "1.2"), ("PHY-2023-MY", "1.3"),
            ("PHY-2023-MY", "1.4"), ("PHY-2023-MY", "1.5"), ("PHY-2023-MY", "1.6"),
            ("PHY-2023-MY", "1.7"),
        ],
    },
    {
        "family_id": "QUESTION-FAMILY-PHY-013",
        "name": "Identify the Newton's-third-law partner of a named force",
        "definition": (
            "Given a specific force (usually the weight of an object), the student must name the "
            "reaction force with both the interacting bodies reversed and the direction, or state "
            "that two interacting bodies experience equal magnitudes of force."
        ),
        "topics": ["Mechanics-Forces", "Mechanics-Momentum"],
        "assessment_operations": ["identify the interacting pair", "reverse the bodies", "state the direction", "state equal magnitude"],
        "distinguishing_features": [
            "asks for 'the reaction force, with direction, of the weight of ...' or 'which cart "
            "experiences the greater force'",
            "2 marks: one for naming the force with the correct pair of bodies, one for the "
            "direction or the equal-magnitude statement",
            "the distractor pattern in the MCQ form is the normal force, which is NOT the "
            "third-law partner of the weight",
        ],
        "typical_marks_range": [1, 2],
        "members": [
            ("PHY-2019-MY", "5.5"), ("PHY-2023-MY", "7.1.3"), ("PHY-2025-NOV", "5.3"),
        ],
    },
    {
        "family_id": "QUESTION-FAMILY-PHY-014",
        "name": "Conservation of momentum and impulse-momentum in a collision",
        "definition": (
            "For a collision between two bodies the student must state conservation of linear "
            "momentum for an isolated system, set up the momentum equation with a sign "
            "convention, use the elastic-collision condition, solve for both final velocities "
            "with directions, and use dp = F dt to find the force during contact."
        ),
        "topics": ["Mechanics-Momentum"],
        "assessment_operations": ["state a conservation principle", "set a sign convention", "solve simultaneous conservation equations", "apply impulse = change in momentum"],
        "distinguishing_features": [
            "two carts/bodies with opposite velocities and a stated collision time",
            "the 6-mark item requires BOTH conservation equations; the memo also shows the "
            "relative-velocity shortcut as an accepted alternative",
            "direction must be stated with every final velocity",
            "an evaluation item asks why magnetic bumpers improve the experiment",
        ],
        "typical_marks_range": [1, 6],
        "members": [
            ("PHY-2025-NOV", "5.2"), ("PHY-2025-NOV", "5.5"), ("PHY-2025-NOV", "5.6"),
        ],
        # NOTE: the two definitional items of this competence (5.1 conservation of linear
        # momentum, 5.4 impulse) are members of QUESTION-FAMILY-PHY-001, because the
        # competence being assessed there is stating the term to the memo criteria. Family
        # membership is a partition, so they are not double-counted here.
    },
]

FAMILIES += [
    {
        "family_id": "QUESTION-FAMILY-PHY-015",
        "name": "Explain a physical situation in words using a named principle",
        "definition": (
            "A written explanation, usually 2-4 marks, in which the student must account for an "
            "observation or justify a proposal by naming a physics principle and carrying it "
            "through the specific situation. No calculation is required, but the memo ticks each "
            "reasoning link separately."
        ),
        "topics": ["Mechanics-Forces", "Work Energy Power", "Mechanics-Motion"],
        "assessment_operations": ["explain a phenomenon", "justify a proposal", "link a principle to a situation"],
        "distinguishing_features": [
            "command verbs: Explain / Why / Briefly explain / Explain why",
            "the memo awards one mark per reasoning link and the links must be in a stated order "
            "(2019 memo 6.1: 'order matters')",
            "the answer must name the principle (inertia, Newton's first law, component of a force, "
            "energy gain/loss) and not merely restate the question",
            "a recurring sub-pattern is the load in an accelerating vehicle explained through "
            "inertia (2019 Q5.3.1 and 2021 Q4.2 use almost the same four-mark chain)",
        ],
        "typical_marks_range": [2, 4],
        "members": [
            ("PHY-2019-MY", "3.1.5"), ("PHY-2019-MY", "4.2.3"), ("PHY-2019-MY", "4.2.5"),
            ("PHY-2019-MY", "5.3.1"),
            ("PHY-2021-NOV", "4.2"), ("PHY-2021-NOV", "4.3.4"), ("PHY-2021-NOV", "6.1.2"),
            ("PHY-2021-NOV", "6.1.3"),
            ("PHY-2025-NOV", "3.5"),
        ],
    },
    {
        "family_id": "QUESTION-FAMILY-PHY-016",
        "name": "Distinguish scalar from vector descriptions of the same motion",
        "definition": (
            "Given one described motion, the student must separate the scalar account (distance, "
            "speed) from the vector account (displacement, velocity), illustrate both with the "
            "positions given, and report a velocity with its direction."
        ),
        "topics": ["Mechanics-Motion"],
        "assessment_operations": ["distinguish scalar and vector quantities", "apply both to one motion", "state a direction"],
        "distinguishing_features": [
            "a route with two or more legs and named positions (A, B, C) is given",
            "the memo marks the definition AND its application to the given positions separately",
            "the velocity answer requires a magnitude and a compass direction or bearing",
        ],
        "typical_marks_range": [2, 5],
        "members": [
            ("PHY-2019-MY", "3.2.2"), ("PHY-2019-MY", "3.2.3"), ("PHY-2021-NOV", "2.1.1"),
        ],
    },
]
