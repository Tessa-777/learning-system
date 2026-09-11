"""Pass 2 analysis (Tier 2/3) for Physics — Understanding Models, breakdowns, diagnostics.

One Understanding Model per question family defined in ``physics_pass2_families.py``.
``confidence`` is NOT authored here: ``scripts/build_physics_pass2.py`` computes it
from the family's member evidence (TWO_PASS_PROMPTS Pass 2 rule) and refuses
"high" when the supporting questions all come from one paper.

Misconceptions are Tier 3 pedagogical inference unless the memo itself records the
error; each is tagged accordingly.
"""

MODELS = [
    {
        "identity": "UNDERSTANDING-PHY-001",
        "definition": (
            "Understanding a physics term well enough to state it in the elements the marking "
            "guidelines reward - the quantity being related, the relation, and the qualifying "
            "condition - rather than as a loose synonym."
        ),
        "topic": "Physics terminology and laws (cross-topic)",
        "question_family": "QUESTION-FAMILY-PHY-001",
        "assessment_operations": ["recall a definition", "state a law", "explain a term"],
        "required_knowledge": [
            "the exact definitional elements for the recurring terms: velocity, acceleration, "
            "displacement, speed, friction, normal force, resultant force, work, power, "
            "potential difference, emf, resistance, ohmic conductor, diode, knee voltage, "
            "gravitational field, impulse",
            "the three Newton's laws as statements, including 'net or resultant force' in the "
            "first law and 'at constant temperature' in Ohm's law",
            "the work-energy theorem and conservation of linear momentum as worded statements",
        ],
        "prerequisites": [
            "scalar vs vector distinction (needed for velocity, displacement and resultant force)",
            "the idea of a 'net' force as distinct from any single force",
        ],
        "required_reasoning": [
            "identify which two elements the question's term decomposes into",
            "recognise that a definition of a rate must name both the quantity and what it is "
            "per (rate of change of position, work per unit charge, force per unit mass)",
        ],
        "required_procedure": None,
        "evidence_of_understanding": [
            "states both required elements without prompting (e.g. friction: opposes motion AND "
            "parallel to the contact surface)",
            "includes the qualifying condition where the memo requires it (Ohm's law 'at constant "
            "temperature'; conservation of momentum 'of an isolated system'; maximum static "
            "friction 'of a stationary object')",
            "can distinguish the term from a neighbouring one (speed vs velocity, distance vs "
            "displacement, mass vs weight)",
        ],
        "marking_requirements": [
            "the memo splits every definition into two separately ticked elements; one correct "
            "idea alone earns 1 of 2 marks",
            "several memos annotate 'AON' (any other correct wording accepted), so paraphrase is "
            "acceptable if both elements are present",
            "Newton's first law is marked as 'state of rest or uniform velocity' + 'unless acted "
            "on by a net or resultant force'",
            "the work-energy theorem is marked as 'work done by a net force' + 'equals change in "
            "kinetic energy' - omitting 'net' loses a mark",
        ],
        "common_breakdowns": [
            "BREAKDOWN-PHY-001-A", "BREAKDOWN-PHY-001-B", "BREAKDOWN-PHY-001-C",
        ],
        "misconceptions": [
            "[Tier 3 inference] 'velocity and speed are the same thing' - would lose the vector "
            "element the memo requires for velocity",
            "[Tier 3 inference] 'friction always opposes the direction the object is moving' - "
            "the memo requires 'parallel to the surface', which is what makes the incline items work",
            "[Tier 3 inference] 'Ohm's law holds for any component at any time' - the memo's "
            "'constant temperature' element is precisely what this misses",
        ],
        "diagnostic_dimensions": ["recall", "precision of wording", "conceptual boundary"],
        "diagnostic_questions": ["DIAG-PHY-001-A", "DIAG-PHY-001-B", "DIAG-PHY-001-C"],
    },
    {
        "identity": "UNDERSTANDING-PHY-002",
        "definition": (
            "Understanding how to turn a described motion or force situation into one equation "
            "from the data sheet, substitute with a consistent sign convention and units, and "
            "report a physically sensible value."
        ),
        "topic": "Mechanics: motion, forces and energy calculations",
        "question_family": "QUESTION-FAMILY-PHY-002",
        "assessment_operations": ["select an equation", "substitute", "calculate", "state a value with units"],
        "required_knowledge": [
            "the equations of motion (v = u + at, v2 = u2 + 2as, s = ut + 1/2 at2, s = ((u+v)/2)t)",
            "Fnet = ma, Ff = mu FN, Fg = mg, W = Fx cos theta, Ek = 1/2 mv2, Wnet = dEk",
            "that g = 9,8 m.s-2 and that upward/forward must be declared positive before substituting",
        ],
        "prerequisites": [
            "UNDERSTANDING-PHY-001 (definitions of velocity, acceleration, work)",
            "algebraic rearrangement of a formula before substitution",
            "unit conversion (minutes to seconds, km.h-1 to m.s-1, ms to s)",
        ],
        "required_reasoning": [
            "decide which quantity is unknown and which equation contains exactly the knowns given",
            "hold one sign convention across a multi-stage problem (the memo marks a missing "
            "negative sign separately)",
            "recognise when a two-stage problem must be split (cliff height first, then height "
            "above the cliff; two legs of a journey summed)",
        ],
        "required_procedure": (
            "write the equation -> substitute with signs and units -> solve -> state the answer "
            "with a unit and, where the paper asks, to two decimal places"
        ),
        "evidence_of_understanding": [
            "names the equation before substituting rather than producing a bare number",
            "keeps the same sign convention in every line and can explain why a term is negative",
            "checks the answer for physical reasonableness (a braking acceleration must oppose "
            "the motion; a time must be positive)",
            "can say what each symbol stands for in the chosen equation",
        ],
        "marking_requirements": [
            "memos award a separate mark for the equation, the substitution and the final answer "
            "- the method mark survives a substitution error",
            "2019 memo (2.2.3): 'Must show that the acceleration is negative' - the sign is a mark",
            "2021 memo (4.3.2) marks the negative sign explicitly; 2025 memo (2.2) marks 'e&s' "
            "(equation and substitution) separately",
            "later parts are marked 'coe'/'COE' from an earlier answer, so a wrong earlier value "
            "does not zero the later method marks",
            "where the paper says 'show all your working out' (2023 Q7.2.4) the derivation itself "
            "is marked, not only the result",
        ],
        "common_breakdowns": [
            "BREAKDOWN-PHY-002-A", "BREAKDOWN-PHY-002-B", "BREAKDOWN-PHY-002-C", "BREAKDOWN-PHY-002-D",
        ],
        "misconceptions": [
            "[Tier 3 inference] 'acceleration and velocity always have the same sign' - produces "
            "the wrong sign in braking and upward-motion items the memo marks separately",
            "[Tier 3 inference] 'the equation with the most familiar symbols is the right one' - "
            "produces v = u + at where v2 = u2 + 2as is required (no time given)",
            "[memo-evidenced] 2023 memo (2.6.3) requires time in seconds (600 s, not 10 minutes): "
            "unit conversion is a live failure point",
        ],
        "diagnostic_dimensions": ["interpretation", "prerequisite", "strategy", "execution", "verification"],
        "diagnostic_questions": ["DIAG-PHY-002-A", "DIAG-PHY-002-B", "DIAG-PHY-002-C"],
    },
    {
        "identity": "UNDERSTANDING-PHY-003",
        "definition": (
            "Understanding what the shape, sign, gradient and area of a motion graph mean "
            "physically, so that values, intervals and descriptions can be read directly off a "
            "given velocity-time or position-time graph."
        ),
        "topic": "Mechanics: motion graphs",
        "question_family": "QUESTION-FAMILY-PHY-003",
        "assessment_operations": ["read a graph", "interpret a gradient", "interpret an area", "describe motion"],
        "required_knowledge": [
            "on a v-t graph: gradient = acceleration, area = displacement, sign of v = direction",
            "on an x-t graph: gradient = velocity",
            "a direction change corresponds to v crossing zero; a horizontal section means "
            "constant velocity (zero acceleration)",
        ],
        "prerequisites": [
            "UNDERSTANDING-PHY-001 (velocity and acceleration as rates of change)",
            "reading a signed axis and identifying intervals between labelled points",
        ],
        "required_reasoning": [
            "map 'greatest westward velocity' onto 'most negative v', and 'greatest acceleration' "
            "onto 'steepest gradient'",
            "describe motion with two elements: what the velocity is doing AND the direction "
            "(the memos mark these separately)",
            "use the area under a section rather than a single reading when a distance is asked",
        ],
        "required_procedure": None,
        "evidence_of_understanding": [
            "identifies direction-change points as sign changes of v, not as peaks of the graph",
            "explains an interval choice by referring to gradient, not to the height of the line",
            "gives both a velocity statement and a direction when describing motion",
        ],
        "marking_requirements": [
            "2019 memo (3.1.2) and 2021 memo (3.3) each award two marks for a motion description: "
            "one for the velocity/acceleration statement and one for the direction",
            "2025 memo (1.1.4) requires the interval (2 marks) plus 'it has the steepest "
            "gradient' (1 mark) - the reason is separately marked",
            "2023 memo (4.8) requires 'yes' plus 'the maximum height reached decreases' - the "
            "reason must come from the graph",
        ],
        "common_breakdowns": [
            "BREAKDOWN-PHY-003-A", "BREAKDOWN-PHY-003-B", "BREAKDOWN-PHY-003-C",
        ],
        "misconceptions": [
            "[Tier 3 inference] 'the graph is a picture of the path' - a v-t graph going negative "
            "is read as the object moving backwards in space rather than in the negative direction",
            "[Tier 3 inference] 'a steeper line means faster' applied to an a-t graph, or 'a "
            "horizontal line means stationary' applied to a v-t graph",
            "[Tier 3 inference] 'maximum height is where the graph peaks' rather than where v = 0",
        ],
        "diagnostic_dimensions": ["interpretation", "concept", "reasoning"],
        "diagnostic_questions": ["DIAG-PHY-003-A", "DIAG-PHY-003-B", "DIAG-PHY-003-C"],
    },
    {
        "identity": "UNDERSTANDING-PHY-004",
        "definition": (
            "Understanding the correspondence between motion (or a changing circuit quantity) and "
            "its graphical representation well enough to construct the correct graph - shape, "
            "sign, labelled values and relative steepness - rather than to read one."
        ),
        "topic": "Mechanics: motion graphs; Electric circuits",
        "question_family": "QUESTION-FAMILY-PHY-004",
        "assessment_operations": ["sketch a graph", "label axes and key values", "translate between representations"],
        "required_knowledge": [
            "a-t is the gradient of v-t, and x-t is the integral (accumulated area) of v-t",
            "free fall gives a constant a-t value; contact with the ground gives a large spike",
            "curvature: constant acceleration gives a parabolic x-t section",
            "for circuit items: how a quantity varies as a resistance is varied",
        ],
        "prerequisites": [
            "UNDERSTANDING-PHY-003 (reading graphs)",
            "sign conventions for direction",
        ],
        "required_reasoning": [
            "work section by section along the time axis instead of drawing one overall shape",
            "compare gradients between sections (the memo requires 'steeper on the way up than "
            "on the way down')",
            "keep the same direction convention as the given graph when asked to maintain it",
        ],
        "required_procedure": (
            "divide the motion into intervals -> decide the value or shape in each -> plot and "
            "label the boundary times -> check relative steepness and sign"
        ),
        "evidence_of_understanding": [
            "produces the correct sign in each section and can explain why one section is steeper",
            "labels the specific times/values the question asks for rather than a generic curve",
            "can convert back: given their own sketch, state the motion it represents",
        ],
        "marking_requirements": [
            "memos allocate marks per feature, not for one answer: 2021 (3.8) marks the labelled "
            "values, the A-B shape, the B-C shape and the E-F shape separately, and deducts 1 if "
            "the graph is inverted",
            "2023 memo (4.7) marks 'shapes' and 'times' separately and states 'accept the "
            "reflection of this graph'",
            "2025 memo (1.1.5) marks three relative-size comparisons plus labels, and penalises "
            "an inconsistent sign convention by 1",
            "2025 memo (2.7) marks axis labels/units, calculated values shown, and the shape of "
            "each phase of the motion",
        ],
        "common_breakdowns": [
            "BREAKDOWN-PHY-004-A", "BREAKDOWN-PHY-004-B", "BREAKDOWN-PHY-004-C",
        ],
        "misconceptions": [
            "[Tier 3 inference] 'constant velocity means a sloping x-t line of any steepness' - "
            "relative steepness between sections is separately marked",
            "[Tier 3 inference] 'the a-t graph looks like the v-t graph' - shape carried across "
            "without differentiating",
            "[Tier 3 inference] 'the bounce can be ignored' - contact intervals are marked points",
        ],
        "diagnostic_dimensions": ["representation", "reasoning", "execution"],
        "diagnostic_questions": ["DIAG-PHY-004-A", "DIAG-PHY-004-B", "DIAG-PHY-004-C"],
    },
    {
        "identity": "UNDERSTANDING-PHY-005",
        "definition": (
            "Understanding which forces act on a specified object in a specified situation, so "
            "that a free-body or vector-addition diagram can be drawn with the correct arrows, "
            "labels, directions and relative lengths."
        ),
        "topic": "Mechanics: forces and vectors",
        "question_family": "QUESTION-FAMILY-PHY-005",
        "assessment_operations": ["identify the forces on an object", "draw and label arrows", "show relative magnitude"],
        "required_knowledge": [
            "the standard force set: weight, normal force, friction, tension, applied force",
            "that a free-body diagram contains only forces ON the chosen object",
            "friction acts parallel to the contact surface; the normal force is perpendicular to it",
            "Newton's third-law partners are not drawn on the same body",
        ],
        "prerequisites": [
            "UNDERSTANDING-PHY-001 (definitions of friction and normal force)",
            "resolving a weight on an incline into parallel and perpendicular components",
        ],
        "required_reasoning": [
            "choose the system boundary first (the crate, not crate + person) and list only "
            "external forces on it",
            "compare magnitudes from the motion: if the body accelerates upward, the upward "
            "force must be drawn longer",
            "recognise when only one force acts (free fall: 'dot and weight ONLY')",
        ],
        "required_procedure": (
            "state the object -> list contact and field forces -> draw arrows from the object's "
            "centre with correct directions -> label each -> compare lengths against the motion"
        ),
        "evidence_of_understanding": [
            "draws exactly the forces on the named object, with no third-law partners and no "
            "'ma' force",
            "makes relative lengths consistent with the stated acceleration",
            "can justify each arrow by naming the interaction that produces it",
        ],
        "marking_requirements": [
            "one mark per correct, labelled force: 2023 memo (6.2) lists weight, normal force, "
            "F = 120 N, Ff and tension; 2025 memo (3.1) gives an explicit per-force criteria list "
            "including the arrow direction for each",
            "extra or missing arrows are penalised: 2019 memo (3.1.4) says 'dot and weight ONLY'",
            "relative length is marked: 2021 memo (5.1) 'Tension force > Friction force'; "
            "2025 memo (2.5) 'FN must be longer than Fg'",
            "angles are marked: 2019 memo (4.2.4) and 2023 memo (5.2) deduct a mark when the "
            "angle is not shown",
        ],
        "common_breakdowns": [
            "BREAKDOWN-PHY-005-A", "BREAKDOWN-PHY-005-B", "BREAKDOWN-PHY-005-C",
        ],
        "misconceptions": [
            "[Tier 3 inference] 'there is a force in the direction of motion' (an 'ma force' "
            "arrow) - explicitly offered and rejected as an option in 2023 Q1.4",
            "[Tier 3 inference] 'the normal force is always equal to the weight' - false on an "
            "incline and whenever a vertical component of an applied force exists",
            "[Tier 3 inference] 'the reaction force to the weight belongs on the same diagram'",
        ],
        "diagnostic_dimensions": ["concept", "representation", "reasoning"],
        "diagnostic_questions": ["DIAG-PHY-005-A", "DIAG-PHY-005-B", "DIAG-PHY-005-C"],
    },
    {
        "identity": "UNDERSTANDING-PHY-006",
        "definition": (
            "Understanding that connected bodies share a magnitude of acceleration and a tension, "
            "so that Fnet = ma can be written per body (or for the whole system) and solved "
            "simultaneously under one direction convention."
        ),
        "topic": "Mechanics: Newton's second law applied to systems",
        "question_family": "QUESTION-FAMILY-PHY-006",
        "assessment_operations": ["isolate each body", "write Fnet = ma per body", "solve simultaneously", "interpret the sign"],
        "required_knowledge": [
            "an inextensible string transmits the same tension magnitude to both bodies and "
            "constrains them to the same acceleration magnitude",
            "weight components on an incline: mg sin theta down the slope, mg cos theta perpendicular",
            "Ff = mu_k FN for a body on a rough surface",
        ],
        "prerequisites": [
            "UNDERSTANDING-PHY-005 (force diagrams per body)",
            "UNDERSTANDING-PHY-002 (single-body Fnet = ma)",
            "solving two simultaneous linear equations",
        ],
        "required_reasoning": [
            "fix one positive direction for the whole system before writing any equation",
            "decide whether to treat the bodies separately or as one system, and know that the "
            "internal tension cancels in the system method",
            "interpret a negative result as 'the assumed direction was wrong', not as an error",
        ],
        "required_procedure": (
            "draw a force diagram per body -> choose a positive direction -> write Fnet = ma for "
            "each body -> substitute the shared a and T -> solve -> back-substitute for T"
        ),
        "evidence_of_understanding": [
            "writes two equations with the same sign convention and can explain why a is the same "
            "for both bodies",
            "explains why tension is not simply equal to the hanging weight",
            "can solve the problem by the system method and reconcile it with the two-body method",
        ],
        "marking_requirements": [
            "memos mark each body's equation separately before the solution: 2025 memo (4.3) marks "
            "the A equation, the B equation, the equality of the two tensions, a and then T",
            "both routes are accepted for the same marks: 2021 memo (5.5) shows 'OR System:' with "
            "its own mark allocation",
            "the tension answer is marked 'coe' from the candidate's own acceleration "
            "(2021 memo 5.6)",
            "2023 memo (6.6) allocates 6 marks across two body equations, the friction and weight "
            "components and the final comparison with 2 m.s-2",
        ],
        "common_breakdowns": [
            "BREAKDOWN-PHY-006-A", "BREAKDOWN-PHY-006-B", "BREAKDOWN-PHY-006-C",
        ],
        "misconceptions": [
            "[Tier 3 inference] 'tension equals the weight of the hanging mass' - the reason "
            "2025 Q4.1/4.2 asks for the comparison before the calculation",
            "[Tier 3 inference] 'each body has its own acceleration' - the string constraint is missed",
            "[Tier 3 inference] 'friction on the incline acts up the slope in every case' - it "
            "opposes the actual or impending motion",
        ],
        "diagnostic_dimensions": ["concept", "strategy", "execution", "verification"],
        "diagnostic_questions": ["DIAG-PHY-006-A", "DIAG-PHY-006-B", "DIAG-PHY-006-C"],
    },
    {
        "identity": "UNDERSTANDING-PHY-007",
        "definition": (
            "Understanding that a force at an angle has independent perpendicular components, so "
            "that the correct trigonometric ratio can be chosen for the direction required and "
            "components combined into a resultant with a direction."
        ),
        "topic": "Mechanics: vectors and forces at an angle",
        "question_family": "QUESTION-FAMILY-PHY-007",
        "assessment_operations": ["resolve a vector", "choose sin or cos correctly", "combine components", "give a direction or bearing"],
        "required_knowledge": [
            "the component adjacent to the reference angle uses cos, the opposite uses sin",
            "Pythagoras for the magnitude of a resultant and tan-1 for its direction",
            "on a horizontal surface with an upward pull: FN = Fg - F sin theta",
            "a bearing is measured clockwise from north",
        ],
        "prerequisites": [
            "right-angle trigonometry",
            "UNDERSTANDING-PHY-005 (which forces are present)",
        ],
        "required_reasoning": [
            "identify the reference angle and which side of the triangle the required component "
            "lies on, instead of defaulting to one ratio",
            "recognise that only the horizontal component accelerates the body horizontally, while "
            "the vertical component changes the normal force",
            "convert a mathematical angle into the bearing or compass direction the question asks for",
        ],
        "required_procedure": (
            "sketch the triangle -> resolve into x and y -> combine (Pythagoras) -> find the angle "
            "-> express in the requested direction format"
        ),
        "evidence_of_understanding": [
            "justifies the choice of sin or cos by reference to the triangle, not by habit",
            "reduces the normal force when an upward component exists, and can explain why",
            "reports a direction in the form the question requests",
        ],
        "marking_requirements": [
            "2025 memo (3.3) marks FN = Fg - Fy, the substitution (70)(9,8) - (300)sin30, and the "
            "answer - the vertical component is a separate mark",
            "2025 memo (3.4) requires BOTH Fmax(static) and the horizontal component Fx before "
            "awarding the comparison mark",
            "2019 memo (4.1.2) distributes 6 marks over x-components, y-components, magnitude, "
            "angle and the final bearing statement",
            "2019 memo (4.2.2) awards a mark for the component expression, one for its value and "
            "one for identifying it as the resistive force",
        ],
        "common_breakdowns": [
            "BREAKDOWN-PHY-007-A", "BREAKDOWN-PHY-007-B", "BREAKDOWN-PHY-007-C",
        ],
        "misconceptions": [
            "[Tier 3 inference] 'the applied force equals the horizontal force' - the cosine "
            "factor is dropped",
            "[Tier 3 inference] 'the normal force is always mg' even when a rope lifts at an angle",
            "[Tier 3 inference] 'sin and cos are interchangeable' - produces the wrong component "
            "with an otherwise correct method",
        ],
        "diagnostic_dimensions": ["representation", "strategy", "execution"],
        "diagnostic_questions": ["DIAG-PHY-007-A", "DIAG-PHY-007-B", "DIAG-PHY-007-C"],
    },
    {
        "identity": "UNDERSTANDING-PHY-008",
        "definition": (
            "Understanding a relationship well enough to predict the direction of a change when "
            "one quantity is altered, and to justify that prediction by naming the relationship "
            "and carrying the causal chain through it."
        ),
        "topic": "Cross-topic: proportional reasoning in circuits and mechanics",
        "question_family": "QUESTION-FAMILY-PHY-008",
        "assessment_operations": ["predict a direction of change", "quote a relationship", "reason causally", "evaluate a stated claim"],
        "required_knowledge": [
            "I = V/R, V = IR, P = VI = I2R = V2/R, emf = I(Rext + r) and the 'lost voltage' idea",
            "Fnet = ma, Ff = mu FN, and that a net force requires a nonzero resultant",
            "which quantity is held constant in the situation (constant voltage for parallel "
            "branches, constant current for series components)",
        ],
        "prerequisites": [
            "UNDERSTANDING-PHY-009 for circuit items; UNDERSTANDING-PHY-006 for force items",
            "direct and inverse proportionality language",
        ],
        "required_reasoning": [
            "identify the FIRST quantity that changes, then follow the chain to the quantity asked "
            "about (the memos award one mark per link)",
            "hold the correct quantity constant - the same relationship gives opposite answers in "
            "series and parallel (2021 Q7.2.2)",
            "when critiquing a claim, test each of the claim's separate assertions",
        ],
        "required_procedure": (
            "state the change -> name the governing equation -> say which quantity is constant -> "
            "step through the chain -> restate the prediction"
        ),
        "evidence_of_understanding": [
            "names the equation used and identifies the quantity held constant before predicting",
            "gives the intermediate quantity (total current, normal force) rather than jumping to "
            "the answer",
            "can predict correctly in the paired series/parallel case where the answers differ",
        ],
        "marking_requirements": [
            "the prediction is worth 1 mark and the justification 2-4 marks; the justification is "
            "where nearly all the marks are",
            "2019 memo (7.7.2) requires TWO named formulae ('I = V/R' and 'P = I2R with R "
            "constant') for 4 marks",
            "2025 memo (8.3) awards marks for: increase, total current decreases, less voltage "
            "lost internally (Vinternal = Ir), external voltage increases (emf = Vint + Vext)",
            "2021 memo (7.1.7) marks the prediction, the proportionality with R constant, the "
            "formula and the statement about the current through the specific resistor",
            "2023 memo (6.7) requires quantitative correction of two parts of a student's claim "
            "plus a final judgement",
        ],
        "common_breakdowns": [
            "BREAKDOWN-PHY-008-A", "BREAKDOWN-PHY-008-B", "BREAKDOWN-PHY-008-C",
        ],
        "misconceptions": [
            "[Tier 3 inference] 'brighter always means more resistance' - the 2021 Q7.2.2 memo "
            "requires the opposite answer in series and in parallel",
            "[Tier 3 inference] 'a battery's terminal voltage is fixed' - ignores internal "
            "resistance, which is the whole content of the 2025 Q8.3 chain",
            "[Tier 3 inference] 'removing a branch cannot change the others' - parallel-branch "
            "independence over-applied to a circuit with internal resistance",
        ],
        "diagnostic_dimensions": ["concept", "reasoning", "explanation", "verification"],
        "diagnostic_questions": ["DIAG-PHY-008-A", "DIAG-PHY-008-B", "DIAG-PHY-008-C"],
    },
    {
        "identity": "UNDERSTANDING-PHY-009",
        "definition": (
            "Understanding how a resistor network reduces to an equivalent resistance, and how "
            "current, potential difference, power and emf then distribute through it - including "
            "the effect of internal resistance."
        ),
        "topic": "Electric circuits",
        "question_family": "QUESTION-FAMILY-PHY-009",
        "assessment_operations": ["identify series and parallel groupings", "reduce to an equivalent resistance", "apply Ohm's law / power / emf equations", "carry intermediate values forward"],
        "required_knowledge": [
            "Rs = R1 + R2 ... and 1/Rp = 1/R1 + 1/R2 ...",
            "V = IR, P = VI = I2R = V2/R, W = VIt",
            "emf = I(Rext + r); terminal voltage = emf - Ir",
            "an ideal ammeter has negligible resistance (it shorts what it replaces); an ideal "
            "voltmeter draws no current",
        ],
        "prerequisites": [
            "UNDERSTANDING-PHY-001 (definitions of resistance, potential difference, emf, ohmic "
            "conductor)",
            "algebraic manipulation of the parallel-resistance formula (2023 Q8.2 solves for R)",
        ],
        "required_reasoning": [
            "read the diagram to decide which components share the same current and which share "
            "the same potential difference",
            "reduce the network before applying Ohm's law, and keep track of which resistance a "
            "given voltage is across",
            "with internal resistance, recognise that the voltmeter over the battery reads the "
            "terminal voltage, not the emf",
        ],
        "required_procedure": (
            "identify groupings -> reduce step by step -> find the total current -> distribute "
            "voltages and currents -> apply the power or energy equation -> keep units"
        ),
        "evidence_of_understanding": [
            "states which resistors are in parallel and why, before calculating",
            "uses the resistance appropriate to the component being asked about, not the total",
            "explains what happens to the terminal voltage when the current changes",
        ],
        "marking_requirements": [
            "the equivalent-resistance step is marked separately from the current/voltage step: "
            "2021 memo (7.1.2) gives 2 marks for the parallel combination and 2 for the total",
            "the memo allows any of the three power forms (2019 memo 7.5.1: 'allow P = VI, "
            "P = V2/R, P = I2R')",
            "intermediate values carry forward as 'coe' (2021 memo 7.1.4 'coe 7.1.3'; 2023 memo "
            "6.5 'COE 6.4')",
            "2025 memo (9.3, 9.4) requires the internal resistance to be included in emf = I(Rext + r) "
            "before R can be found",
            "2023 memo (8.6) requires the time in seconds (120 s) for W = VIt",
        ],
        "common_breakdowns": [
            "BREAKDOWN-PHY-009-A", "BREAKDOWN-PHY-009-B", "BREAKDOWN-PHY-009-C", "BREAKDOWN-PHY-009-D",
        ],
        "misconceptions": [
            "[Tier 3 inference] 'R = R1 + R2 for every combination' - parallel formula not applied",
            "[Tier 3 inference] 'current is used up as it passes through resistors'",
            "[Tier 3 inference] 'the voltmeter reading is the emf' - internal resistance ignored",
            "[Tier 3 inference] 'replacing a resistor with an ammeter changes nothing' - the "
            "short-circuit consequence required by 2023 Q8.8",
        ],
        "diagnostic_dimensions": ["interpretation", "concept", "strategy", "execution"],
        "diagnostic_questions": ["DIAG-PHY-009-A", "DIAG-PHY-009-B", "DIAG-PHY-009-C"],
    },
    {
        "identity": "UNDERSTANDING-PHY-010",
        "definition": (
            "Understanding the logic of an experimental investigation: what the hypothesis "
            "claims, how the data must be plotted to the marking criteria, what the gradient of "
            "the resulting graph means physically, and how that meaning yields an unknown."
        ),
        "topic": "Experimental investigation; mechanics: gravitation",
        "question_family": "QUESTION-FAMILY-PHY-010",
        "assessment_operations": ["state a hypothesis", "complete a table", "plot a graph", "calculate a gradient", "interpret the gradient physically"],
        "required_knowledge": [
            "independent and dependent variables, and the order a hypothesis must state them in",
            "graph conventions: heading, axis labels with units, a scale that uses the grid, "
            "points plotted, line of best fit",
            "gradient = dy/dx with the unit of the y-axis over the unit of the x-axis",
            "that a straight line through the origin means direct proportionality, and that the "
            "gradient can equal a physical constant (g, or 1/(G m1 m2))",
        ],
        "prerequisites": [
            "UNDERSTANDING-PHY-002 (substitution and units)",
            "reading a table and completing a derived column",
        ],
        "required_reasoning": [
            "identify which column must be transformed before plotting (v2, or 1/r2) to obtain a "
            "straight line",
            "equate the measured gradient to the theoretical expression and solve for the unknown",
            "read a value from the line of best fit rather than from a plotted point",
        ],
        "required_procedure": (
            "state the hypothesis (IV then DV) -> complete the table -> label axes and choose a "
            "scale -> plot -> draw the line of best fit -> take a gradient triangle -> attach the "
            "unit -> equate to the physical expression -> solve"
        ),
        "evidence_of_understanding": [
            "states the hypothesis with the variables in the order the memo requires",
            "chooses and justifies the transformed variable that linearises the data",
            "gives the gradient with a unit and says what physical quantity it represents",
        ],
        "marking_requirements": [
            "graph marks are itemised: 2019 memo (6.4) awards heading, labels/unit, scale, "
            "plotting (x2) and line of best fit; 2021 memo (8.2) awards heading, axis label with "
            "unit, scale, plotting and LOBF across 7 marks",
            "2019 memo (6.1) states 'order matters' for the hypothesis; 2021 memo (8.3) states "
            "'order' for the relationship in words",
            "the gradient must carry a unit (2021 memo 8.5) and a tolerance is allowed "
            "(2025 memo 6.1.3: plus or minus 10%)",
            "2025 memo (6.1.2) flags two specific data points ('check 0,2 & 0,6') as commonly "
            "misplotted, and the paper waives the heading for that item only",
            "the final step equates the gradient to 1/(G m1 m2) (2021 memo 8.6, 8.7) or to g "
            "(2025 memo 6.1.4) - the highest-value reasoning step",
        ],
        "common_breakdowns": [
            "BREAKDOWN-PHY-010-A", "BREAKDOWN-PHY-010-B", "BREAKDOWN-PHY-010-C", "BREAKDOWN-PHY-010-D",
        ],
        "misconceptions": [
            "[Tier 3 inference] 'a hypothesis is a prediction of the outcome' rather than a "
            "statement of the relationship between the two variables",
            "[Tier 3 inference] 'join the plotted points dot-to-dot' instead of a line of best fit",
            "[Tier 3 inference] 'the gradient is a number without units'",
            "[Tier 3 inference] 'the gradient of F against 1/r2 has no physical meaning'",
        ],
        "diagnostic_dimensions": ["interpretation", "representation", "execution", "reasoning"],
        "diagnostic_questions": ["DIAG-PHY-010-A", "DIAG-PHY-010-B", "DIAG-PHY-010-C"],
    },
    {
        "identity": "UNDERSTANDING-PHY-011",
        "definition": (
            "Understanding that atomic energy levels are quantised and negative, so that a "
            "transition releases a photon whose energy is the difference between levels, and "
            "being able to move between energy, frequency, wavelength and electron volts."
        ),
        "topic": "Waves, sound and light: photons and energy levels",
        "question_family": "QUESTION-FAMILY-PHY-011",
        "assessment_operations": ["count possible transitions", "take an energy difference between levels", "apply E = hf or E = hc/lambda", "convert J to eV"],
        "required_knowledge": [
            "E = hf, E = hc/lambda, c = f lambda, and 1 eV = 1,6 x 10^-19 J",
            "the number of distinct transitions from level n is the number of distinct pairs of "
            "levels below it (3 unique frequencies from n = 3)",
            "shorter wavelength means higher frequency and higher photon energy",
            "level energies are quoted relative to the ionisation limit, hence negative",
        ],
        "prerequisites": [
            "UNDERSTANDING-PHY-002 (substitution and unit conversion)",
            "scientific notation arithmetic and powers of ten",
        ],
        "required_reasoning": [
            "identify the two levels involved and take the difference, not a single level value",
            "decide whether the question needs a difference (transition) or a single value "
            "(photon of stated wavelength)",
            "convert to eV only at the end, and check the order of magnitude",
        ],
        "required_procedure": (
            "identify the levels -> dE = E2 - E1 -> convert eV to J -> apply E = hf or "
            "E = hc/lambda -> solve -> convert back to the requested unit"
        ),
        "evidence_of_understanding": [
            "counts transitions by pairing levels rather than by counting levels",
            "explains why the green photon is more energetic than the red at equal beam power",
            "can explain why the tabulated level energies are negative",
        ],
        "marking_requirements": [
            "the eV<->J conversion is a separate mark: 2023 memo (10.2) marks E = hf, the "
            "substitution with (13,6 - 3,4) x 1,6 x 10^-19, and the frequency",
            "2023 memo (10.3) and 2025 memo (7.2) both require the final answer in eV as a "
            "separate mark after the joule value",
            "2025 memo (7.1) awards one mark for 'higher frequency, more energy' and one for "
            "'wavelength inversely proportional to frequency'",
            "the memo for 2021 Q9.2-9.5 is an image and could not be read as text, so the "
            "marking detail for those items is unverified (see unresolved items)",
        ],
        "common_breakdowns": [
            "BREAKDOWN-PHY-011-A", "BREAKDOWN-PHY-011-B", "BREAKDOWN-PHY-011-C",
        ],
        "misconceptions": [
            "[Tier 3 inference] 'a brighter beam has more energetic photons' - the exact "
            "distinction the 2025 Q7.1 memo marks",
            "[Tier 3 inference] 'the photon energy equals the energy of the level it leaves'",
            "[Tier 3 inference] 'negative level energies mean the electron has negative energy "
            "that must be added' without reference to the ionisation reference point",
        ],
        "diagnostic_dimensions": ["concept", "execution", "explanation"],
        "diagnostic_questions": ["DIAG-PHY-011-A", "DIAG-PHY-011-B", "DIAG-PHY-011-C"],
    },
    {
        "identity": "UNDERSTANDING-PHY-012",
        "definition": (
            "Understanding a single concept well enough to apply it once, under time pressure and "
            "without working, and to eliminate the distractors that target the common error."
        ),
        "topic": "Cross-topic concept application (multiple choice)",
        "question_family": "QUESTION-FAMILY-PHY-012",
        "assessment_operations": ["apply one concept", "eliminate distractors", "select an option"],
        "required_knowledge": [
            "the same concept base as the written questions: vector addition limits, sign of "
            "acceleration, Newton's laws, elevator scale readings, series vs parallel brightness, "
            "energy-level transitions",
        ],
        "prerequisites": ["the corresponding written-topic understanding models (PHY-001 to PHY-009)"],
        "required_reasoning": [
            "identify which single idea the item tests before reading the options",
            "test each option against that idea rather than looking for a familiar phrase",
            "handle the paired-table format (two quantities per option) by checking both columns",
        ],
        "required_procedure": None,
        "evidence_of_understanding": [
            "can say why the correct option is right AND why each distractor is wrong",
            "answers consistently with the written questions on the same topic",
        ],
        "marking_requirements": [
            "every MCQ in the batch is worth exactly 2 marks and the memo records only the correct "
            "letter (2019 memo Q1, 2021 memo Q1, 2023 memo Q1) - there is no partial credit and no "
            "method mark",
            "because the memos give no distractor analysis, the knowledge bank cannot state "
            "officially why a wrong option is wrong; any such claim is Tier 3 inference",
            "the MCQ block is absent from the 2025 paper, so this family rests on three papers only",
        ],
        "common_breakdowns": ["BREAKDOWN-PHY-012-A", "BREAKDOWN-PHY-012-B"],
        "misconceptions": [
            "[Tier 3 inference] distractor patterns are not documented in any memo in this batch; "
            "any specific claim about why students choose a wrong option is unprovenanced",
        ],
        "diagnostic_dimensions": ["concept", "verification"],
        "diagnostic_questions": ["DIAG-PHY-012-A", "DIAG-PHY-012-B"],
    },
    {
        "identity": "UNDERSTANDING-PHY-013",
        "definition": (
            "Understanding Newton's third law as a statement about a pair of interacting bodies, "
            "so that the reaction to a named force can be identified by reversing the bodies and "
            "the direction, with equal magnitude."
        ),
        "topic": "Mechanics: Newton's third law",
        "question_family": "QUESTION-FAMILY-PHY-013",
        "assessment_operations": ["identify the interacting pair", "reverse the bodies", "state the direction", "state equal magnitude"],
        "required_knowledge": [
            "the third law pairs forces of the same type acting on different bodies",
            "the reaction to the weight of an object is the gravitational pull of that object on "
            "the Earth, upward",
            "the normal force is NOT the third-law partner of the weight",
            "during a collision both bodies experience forces of equal magnitude",
        ],
        "prerequisites": ["UNDERSTANDING-PHY-001 (statement of Newton's third law)", "UNDERSTANDING-PHY-005"],
        "required_reasoning": [
            "name the two bodies in the given force, then swap them to construct the partner",
            "check that the partner is the same type of force (gravitational with gravitational, "
            "contact with contact)",
        ],
        "required_procedure": None,
        "evidence_of_understanding": [
            "gives the partner force with both bodies named and the direction stated",
            "rejects the normal force as the partner of the weight and can say why",
            "applies equal magnitude to both bodies in a collision regardless of their masses",
        ],
        "marking_requirements": [
            "two marks: the force named with the correct pair of bodies, and the direction "
            "(2019 memo 5.5: 'the box pulling up on the Earth'; 2023 memo 7.1.3: 'the pulling "
            "gravitational force of the 5 kg mass piece on the Earth' + 'upwards')",
            "2025 memo (5.3) requires 'equal magnitude of force' with the Newton III reference",
        ],
        "common_breakdowns": ["BREAKDOWN-PHY-013-A", "BREAKDOWN-PHY-013-B"],
        "misconceptions": [
            "[memo-evidenced] the normal force is offered as a distractor for the reaction to the "
            "weight (2021 Q1.7 option D) and the memo rejects it",
            "[Tier 3 inference] 'the heavier body exerts the greater force in a collision'",
        ],
        "diagnostic_dimensions": ["concept", "explanation"],
        "diagnostic_questions": ["DIAG-PHY-013-A", "DIAG-PHY-013-B"],
    },
    {
        "identity": "UNDERSTANDING-PHY-014",
        "definition": (
            "Understanding momentum as a conserved vector quantity of an isolated system, so that "
            "a collision can be solved with a sign convention, and impulse as the change in "
            "momentum produced by a force over a contact time."
        ),
        "topic": "Mechanics: momentum and impulse",
        "question_family": "QUESTION-FAMILY-PHY-014",
        "assessment_operations": ["state a conservation principle", "set a sign convention", "solve simultaneous conservation equations", "apply impulse = change in momentum"],
        "required_knowledge": [
            "p = mv; total momentum of an isolated system is conserved",
            "for a perfectly elastic collision kinetic energy is also conserved; equivalently the "
            "relative velocity of approach equals the relative velocity of separation",
            "J = F dt = dp = m(vf - vi)",
        ],
        "prerequisites": [
            "UNDERSTANDING-PHY-002 (substitution, units: milliseconds to seconds)",
            "solving two simultaneous equations",
        ],
        "required_reasoning": [
            "declare one positive direction and apply it to both bodies before and after",
            "recognise that two unknowns require two independent equations",
            "interpret a negative final velocity as motion in the declared negative direction",
        ],
        "required_procedure": (
            "state the principle -> set the sign convention -> write the momentum equation -> "
            "write the energy (or relative-velocity) equation -> solve -> state magnitude and "
            "direction -> use dp = F dt for the contact force"
        ),
        "evidence_of_understanding": [
            "explains why the system can be treated as isolated",
            "keeps one sign convention through both equations and states directions at the end",
            "explains why both bodies experience equal-magnitude forces despite different masses",
        ],
        "marking_requirements": [
            "2025 memo (5.2) awards 6 marks across the momentum equation, its substitution, the "
            "energy or relative-velocity equation, the substitution into equation 1, and each "
            "final velocity with its direction",
            "2025 memo (5.5) marks m(vf - vi) = F dt, the substitution with the time in seconds "
            "(0,02 s) and the force",
            "2025 memo (5.6) awards marks for 'interact without physical contact', 'minimal "
            "deformation/friction/sound/heat loss' and 'closer to perfectly elastic'",
            "CAUTION: this family is evidenced by a single paper only (2025); the marking "
            "requirements above must not be generalised to other sittings yet",
        ],
        "common_breakdowns": ["BREAKDOWN-PHY-014-A", "BREAKDOWN-PHY-014-B", "BREAKDOWN-PHY-014-C"],
        "misconceptions": [
            "[Tier 3 inference] 'momentum is conserved as a scalar' - signs dropped",
            "[Tier 3 inference] 'the heavier cart exerts the greater force' - contradicted by "
            "2025 memo 5.3",
            "[Tier 3 inference] 'an elastic collision means the bodies bounce with unchanged speeds'",
        ],
        "diagnostic_dimensions": ["concept", "strategy", "execution"],
        "diagnostic_questions": ["DIAG-PHY-014-A", "DIAG-PHY-014-B"],
    },
]

BREAKDOWNS = [
    # --- PHY-001 definitions ---
    {"breakdown_id": "BREAKDOWN-PHY-001-A", "stage": "prerequisite",
     "description": "The term is not known at all, or is confused with a neighbouring term (speed for velocity, mass for weight), so the answer is a different quantity.",
     "parent_understanding_model": "UNDERSTANDING-PHY-001",
     "observable_signals": ["names a different physical quantity", "cannot give any element of the definition"],
     "possible_confusions": ["speed vs velocity", "distance vs displacement", "mass vs weight", "emf vs potential difference"],
     "distinguishing_questions": ["Ask for the definition of the neighbouring term and compare what the student says"],
     "source_basis": ["physics_2019_internal_paper1_june_q4.2.1", "physics_2023_internal_paper1_june_q2.1"],
     "confidence": "medium"},
    {"breakdown_id": "BREAKDOWN-PHY-001-B", "stage": "explanation",
     "description": "The concept is understood but the answer states only one of the two elements the memo ticks, so it scores 1 of 2.",
     "parent_understanding_model": "UNDERSTANDING-PHY-001",
     "observable_signals": ["gives a correct but incomplete phrase", "omits the qualifier ('parallel to the surface', 'at constant temperature', 'of an isolated system')"],
     "possible_confusions": ["treating the qualifier as optional wording rather than content"],
     "distinguishing_questions": ["Ask what would have to be added to make the statement complete"],
     "source_basis": ["physics_2019_internal_paper1_june_q5.2", "physics_2023_internal_paper1_june_q8.1",
                      "physics_2025_internal_paper1_nov_q5.1"],
     "confidence": "high"},
    {"breakdown_id": "BREAKDOWN-PHY-001-C", "stage": "concept",
     "description": "The student gives a correct-sounding but non-specific answer ('friction slows things down') that does not identify the interaction or the geometry the memo requires.",
     "parent_understanding_model": "UNDERSTANDING-PHY-001",
     "observable_signals": ["answer is true in everyday language but omits the physics relation", "no reference to surfaces, charge, or per-unit quantity"],
     "possible_confusions": ["everyday meaning of the term substituted for the physical definition"],
     "distinguishing_questions": ["Ask which two objects the force acts between and in what direction"],
     "source_basis": ["physics_2021_internal_paper1_nov_q5.2", "physics_2023_internal_paper1_june_q6.1"],
     "confidence": "medium"},

    # --- PHY-002 substitution calculations ---
    {"breakdown_id": "BREAKDOWN-PHY-002-A", "stage": "strategy",
     "description": "The wrong equation is selected, usually one containing a quantity the question does not give (choosing v = u + at when no time is given).",
     "parent_understanding_model": "UNDERSTANDING-PHY-002",
     "observable_signals": ["writes an equation containing an unknown that was never given", "invents a value for the missing quantity"],
     "possible_confusions": ["equation chosen by familiarity rather than by the knowns"],
     "distinguishing_questions": ["Ask which quantities are known and which equation contains only those plus the unknown"],
     "source_basis": ["physics_2021_internal_paper1_nov_q4.3.2", "physics_2023_internal_paper1_june_q2.2"],
     "confidence": "medium"},
    {"breakdown_id": "BREAKDOWN-PHY-002-B", "stage": "execution",
     "description": "The method is right but the sign convention is not held: a deceleration or a downward displacement is substituted as positive.",
     "parent_understanding_model": "UNDERSTANDING-PHY-002",
     "observable_signals": ["all magnitudes positive in a braking or upward-motion problem", "answer's direction contradicts the situation"],
     "possible_confusions": ["treating g and a as always positive"],
     "distinguishing_questions": ["Ask which direction was chosen as positive and what sign each term then takes"],
     "source_basis": ["physics_2019_internal_paper1_june_q2.2.3", "physics_2021_internal_paper1_nov_q4.3.2",
                      "physics_2025_internal_paper1_nov_q2.2"],
     "confidence": "high"},
    {"breakdown_id": "BREAKDOWN-PHY-002-C", "stage": "prerequisite",
     "description": "Units are not converted before substituting (minutes for seconds, km.h-1 for m.s-1, milliseconds for seconds), so the arithmetic is correct but the value is wrong.",
     "parent_understanding_model": "UNDERSTANDING-PHY-002",
     "observable_signals": ["substitutes 10 for 600 s", "answer out by a factor of 60 or 1000"],
     "possible_confusions": ["assuming the given units are already SI"],
     "distinguishing_questions": ["Ask what unit each symbol in the equation must be in"],
     "source_basis": ["physics_2023_internal_paper1_june_q2.6.3", "physics_2023_internal_paper1_june_q8.6",
                      "physics_2025_internal_paper1_nov_q5.5"],
     "confidence": "high"},
    {"breakdown_id": "BREAKDOWN-PHY-002-D", "stage": "interpretation",
     "description": "A multi-stage problem is treated as one step: the intermediate quantity (cliff height, first leg's time, distance already covered) is never found, so the final answer misses a term.",
     "parent_understanding_model": "UNDERSTANDING-PHY-002",
     "observable_signals": ["one equation only where the memo shows two stages", "final answer omits a distance or a time interval the memo adds"],
     "possible_confusions": ["treating the whole journey as a single uniformly accelerated motion"],
     "distinguishing_questions": ["Ask what happens between the start and the moment the question asks about"],
     "source_basis": ["physics_2019_internal_paper1_june_q2.2.4", "physics_2023_internal_paper1_june_q3.3",
                      "physics_2023_internal_paper1_june_q2.3"],
     "confidence": "high"},

    # --- PHY-003 graph reading ---
    {"breakdown_id": "BREAKDOWN-PHY-003-A", "stage": "concept",
     "description": "The graph is read as a picture of the path in space, so a negative section is taken to mean the object is behind its start rather than moving in the negative direction.",
     "parent_understanding_model": "UNDERSTANDING-PHY-003",
     "observable_signals": ["says the object 'went under the ground'", "cannot relate the sign of v to direction"],
     "possible_confusions": ["x-t graph read as a v-t graph", "graph read as a trajectory"],
     "distinguishing_questions": ["Ask what the vertical axis measures and what a negative value of it means"],
     "source_basis": ["physics_2025_internal_paper1_nov_q1.1.2", "physics_2021_internal_paper1_nov_q1.3"],
     "confidence": "medium"},
    {"breakdown_id": "BREAKDOWN-PHY-003-B", "stage": "reasoning",
     "description": "Gradient and value are confused: the highest point on the graph is taken to be the greatest acceleration, or a horizontal section is read as no motion.",
     "parent_understanding_model": "UNDERSTANDING-PHY-003",
     "observable_signals": ["picks the tallest section when asked for greatest acceleration", "reads a horizontal v-t section as stationary"],
     "possible_confusions": ["height of line vs steepness of line"],
     "distinguishing_questions": ["Ask what the steepness of the line represents at that point"],
     "source_basis": ["physics_2025_internal_paper1_nov_q1.1.4", "physics_2019_internal_paper1_june_q3.1.2"],
     "confidence": "medium"},
    {"breakdown_id": "BREAKDOWN-PHY-003-C", "stage": "explanation",
     "description": "The reading is right but the description is incomplete: the student states the velocity change without the direction, losing the second memo mark.",
     "parent_understanding_model": "UNDERSTANDING-PHY-003",
     "observable_signals": ["says 'slowing down' without saying in which direction the motion is"],
     "possible_confusions": ["assuming direction is obvious from the graph"],
     "distinguishing_questions": ["Ask which way the object is moving during that interval"],
     "source_basis": ["physics_2019_internal_paper1_june_q3.1.2", "physics_2021_internal_paper1_nov_q3.3"],
     "confidence": "high"},

    # --- PHY-004 graph construction ---
    {"breakdown_id": "BREAKDOWN-PHY-004-A", "stage": "strategy",
     "description": "The graph is drawn as one overall shape instead of section by section, so intervals with different behaviour are merged.",
     "parent_understanding_model": "UNDERSTANDING-PHY-004",
     "observable_signals": ["a single smooth curve where the memo shows distinct sections", "boundary times not marked"],
     "possible_confusions": ["drawing the 'typical shape' of a motion rather than the one described"],
     "distinguishing_questions": ["Ask how many distinct phases the motion has and what happens at each boundary"],
     "source_basis": ["physics_2021_internal_paper1_nov_q3.8", "physics_2025_internal_paper1_nov_q2.7"],
     "confidence": "medium"},
    {"breakdown_id": "BREAKDOWN-PHY-004-B", "stage": "reasoning",
     "description": "Relative steepness or sign between sections is not carried through, e.g. the a-t graph does not show that deceleration up a slope exceeds acceleration down it.",
     "parent_understanding_model": "UNDERSTANDING-PHY-004",
     "observable_signals": ["all sections drawn with the same slope", "signs inverted in one section"],
     "possible_confusions": ["assuming symmetry where friction breaks it"],
     "distinguishing_questions": ["Ask which section has the larger net force and therefore the steeper gradient"],
     "source_basis": ["physics_2021_internal_paper1_nov_q6.1.5", "physics_2025_internal_paper1_nov_q1.1.5"],
     "confidence": "medium"},
    {"breakdown_id": "BREAKDOWN-PHY-004-C", "stage": "execution",
     "description": "The shape is right but the required values are not labelled, or the direction convention is not the one the question told the student to keep.",
     "parent_understanding_model": "UNDERSTANDING-PHY-004",
     "observable_signals": ["unlabelled axes", "graph mirrored against the instruction to maintain the given direction"],
     "possible_confusions": ["believing labels are presentation rather than content"],
     "distinguishing_questions": ["Ask which values on the graph the examiner needs to see and which direction was defined as positive"],
     "source_basis": ["physics_2023_internal_paper1_june_q4.7", "physics_2019_internal_paper1_june_q3.1.8"],
     "confidence": "high"},

    # --- PHY-005 force diagrams ---
    {"breakdown_id": "BREAKDOWN-PHY-005-A", "stage": "concept",
     "description": "A force is invented in the direction of motion (an 'ma' force), or a third-law partner acting on another body is drawn on the object.",
     "parent_understanding_model": "UNDERSTANDING-PHY-005",
     "observable_signals": ["an arrow labelled 'force of motion' or 'ma'", "the weight's reaction drawn on the same body"],
     "possible_confusions": ["motion implies a force in that direction", "third-law pairs drawn on one body"],
     "distinguishing_questions": ["Ask which other object exerts each arrow on the diagram"],
     "source_basis": ["physics_2023_internal_paper1_june_q1.4", "physics_2019_internal_paper1_june_q5.5"],
     "confidence": "medium"},
    {"breakdown_id": "BREAKDOWN-PHY-005-B", "stage": "concept",
     "description": "The normal force is drawn equal to the weight in a situation where a component of another force or an incline makes them unequal.",
     "parent_understanding_model": "UNDERSTANDING-PHY-005",
     "observable_signals": ["FN drawn the same length as Fg on an incline", "FN = mg written where an applied vertical component exists"],
     "possible_confusions": ["normal force treated as a fixed reaction to weight"],
     "distinguishing_questions": ["Ask what the net force perpendicular to the surface is and what that implies for FN"],
     "source_basis": ["physics_2025_internal_paper1_nov_q3.1", "physics_2023_internal_paper1_june_q6.2"],
     "confidence": "high"},
    {"breakdown_id": "BREAKDOWN-PHY-005-C", "stage": "reasoning",
     "description": "Relative arrow lengths contradict the stated motion: the upward force is not drawn longer when the body accelerates upward.",
     "parent_understanding_model": "UNDERSTANDING-PHY-005",
     "observable_signals": ["equal-length arrows where the memo requires inequality", "no reference to the acceleration when comparing arrows"],
     "possible_confusions": ["assuming all diagrams show equilibrium"],
     "distinguishing_questions": ["Ask what the net force must be given the stated acceleration, and what that means for the arrow lengths"],
     "source_basis": ["physics_2025_internal_paper1_nov_q2.5", "physics_2021_internal_paper1_nov_q3.9"],
     "confidence": "high"},

    # --- PHY-006 connected bodies ---
    {"breakdown_id": "BREAKDOWN-PHY-006-A", "stage": "strategy",
     "description": "Only one body is analysed, so the tension is treated as a known (usually the hanging weight) and the second equation is never written.",
     "parent_understanding_model": "UNDERSTANDING-PHY-006",
     "observable_signals": ["one equation only", "T replaced by mg without justification"],
     "possible_confusions": ["treating a connected system as a single isolated body"],
     "distinguishing_questions": ["Ask how many bodies are accelerating and what each one's equation is"],
     "source_basis": ["physics_2025_internal_paper1_nov_q4.3", "physics_2023_internal_paper1_june_q7.1.1"],
     "confidence": "high"},
    {"breakdown_id": "BREAKDOWN-PHY-006-B", "stage": "execution",
     "description": "The two equations are written with inconsistent direction conventions, so the signs of a and T do not combine correctly.",
     "parent_understanding_model": "UNDERSTANDING-PHY-006",
     "observable_signals": ["both bodies given positive acceleration in opposite directions", "sign errors that do not cancel"],
     "possible_confusions": ["choosing 'down the page' as positive separately for each body"],
     "distinguishing_questions": ["Ask which single direction was chosen as positive for the whole system"],
     "source_basis": ["physics_2025_internal_paper1_nov_q4.3", "physics_2021_internal_paper1_nov_q5.5"],
     "confidence": "medium"},
    {"breakdown_id": "BREAKDOWN-PHY-006-C", "stage": "prerequisite",
     "description": "The incline components or the friction on the sloped body are wrong, so the system equation is set up with the wrong driving force.",
     "parent_understanding_model": "UNDERSTANDING-PHY-006",
     "observable_signals": ["mg used instead of mg sin theta down the slope", "friction omitted or given the wrong direction"],
     "possible_confusions": ["sin/cos swapped on the incline", "friction assumed to oppose the applied force rather than the motion"],
     "distinguishing_questions": ["Ask which component of the weight acts along the slope and which way friction acts"],
     "source_basis": ["physics_2021_internal_paper1_nov_q5.5", "physics_2023_internal_paper1_june_q6.6"],
     "confidence": "high"},

    # --- PHY-007 resolving forces ---
    {"breakdown_id": "BREAKDOWN-PHY-007-A", "stage": "execution",
     "description": "sin and cos are swapped for the required direction, giving a numerically plausible but wrong component.",
     "parent_understanding_model": "UNDERSTANDING-PHY-007",
     "observable_signals": ["uses sin for the adjacent component", "component larger than the force itself is impossible but not noticed"],
     "possible_confusions": ["ratio chosen by habit rather than from the triangle"],
     "distinguishing_questions": ["Ask which side of the triangle the required component is and what the angle is measured from"],
     "source_basis": ["physics_2025_internal_paper1_nov_q3.3", "physics_2023_internal_paper1_june_q6.4"],
     "confidence": "medium"},
    {"breakdown_id": "BREAKDOWN-PHY-007-B", "stage": "concept",
     "description": "The whole applied force is used as the horizontal driving force and the vertical component is ignored, so the normal force and friction are also wrong.",
     "parent_understanding_model": "UNDERSTANDING-PHY-007",
     "observable_signals": ["F used undecomposed in Fnet = ma", "FN = mg despite an angled pull"],
     "possible_confusions": ["treating an angled force as if it acted along the surface"],
     "distinguishing_questions": ["Ask what effect the upward part of the pull has on how hard the surfaces press together"],
     "source_basis": ["physics_2025_internal_paper1_nov_q3.3", "physics_2025_internal_paper1_nov_q3.4"],
     "confidence": "high"},
    {"breakdown_id": "BREAKDOWN-PHY-007-C", "stage": "explanation",
     "description": "The magnitude is right but the direction is not given in the requested form (bearing, compass direction), losing the final mark.",
     "parent_understanding_model": "UNDERSTANDING-PHY-007",
     "observable_signals": ["angle given without a reference direction", "bearing not converted from the mathematical angle"],
     "possible_confusions": ["bearing vs angle to the horizontal"],
     "distinguishing_questions": ["Ask what the angle is measured from and which way it opens"],
     "source_basis": ["physics_2019_internal_paper1_june_q4.1.2", "physics_2023_internal_paper1_june_q2.6.2"],
     "confidence": "high"},

    # --- PHY-008 qualitative change ---
    {"breakdown_id": "BREAKDOWN-PHY-008-A", "stage": "reasoning",
     "description": "The prediction is made from an intuition about the surface feature of the change rather than from the governing relationship (e.g. 'one bulb is gone so the others get dimmer').",
     "parent_understanding_model": "UNDERSTANDING-PHY-008",
     "observable_signals": ["prediction with no equation quoted", "prediction contradicts the relationship the student themselves states"],
     "possible_confusions": ["everyday reasoning substituted for proportional reasoning"],
     "distinguishing_questions": ["Ask which equation links the quantity that changed to the quantity being asked about"],
     "source_basis": ["physics_2025_internal_paper1_nov_q8.3", "physics_2019_internal_paper1_june_q7.7.2"],
     "confidence": "high"},
    {"breakdown_id": "BREAKDOWN-PHY-008-B", "stage": "concept",
     "description": "The wrong quantity is held constant: the student applies the constant-voltage reasoning to a series circuit, or ignores internal resistance where the memo requires it.",
     "parent_understanding_model": "UNDERSTANDING-PHY-008",
     "observable_signals": ["gives the same answer for the series and the parallel case", "treats the battery's terminal voltage as fixed"],
     "possible_confusions": ["series and parallel behaviour conflated", "ideal battery assumed"],
     "distinguishing_questions": ["Ask which quantity stays the same in this arrangement and why"],
     "source_basis": ["physics_2021_internal_paper1_nov_q7.2.2", "physics_2025_internal_paper1_nov_q8.3",
                      "physics_2025_internal_paper1_nov_q9.5"],
     "confidence": "high"},
    {"breakdown_id": "BREAKDOWN-PHY-008-C", "stage": "explanation",
     "description": "The prediction is correct but the chain is incomplete: an intermediate quantity (total current, normal force) is skipped, so the justification earns part marks only.",
     "parent_understanding_model": "UNDERSTANDING-PHY-008",
     "observable_signals": ["jumps from the change to the conclusion in one step", "names the formula but does not apply it"],
     "possible_confusions": ["believing the correct prediction carries the marks"],
     "distinguishing_questions": ["Ask what happens to the quantity between the one that changed and the one asked about"],
     "source_basis": ["physics_2021_internal_paper1_nov_q7.1.7", "physics_2025_internal_paper1_nov_q8.3",
                      "physics_2019_internal_paper1_june_q7.7.2"],
     "confidence": "high"},

    # --- PHY-009 circuits ---
    {"breakdown_id": "BREAKDOWN-PHY-009-A", "stage": "interpretation",
     "description": "The circuit diagram is misread: components that share a node pair are not recognised as parallel, or the meters are treated as resistors.",
     "parent_understanding_model": "UNDERSTANDING-PHY-009",
     "observable_signals": ["adds resistances that are in parallel", "includes the voltmeter in the resistance"],
     "possible_confusions": ["diagram layout mistaken for the electrical connections"],
     "distinguishing_questions": ["Ask which components have both ends connected to the same two points"],
     "source_basis": ["physics_2021_internal_paper1_nov_q7.1.2", "physics_2023_internal_paper1_june_q8.2"],
     "confidence": "high"},
    {"breakdown_id": "BREAKDOWN-PHY-009-B", "stage": "strategy",
     "description": "The network is not reduced before Ohm's law is applied, or the total resistance is used where the question asks about one component.",
     "parent_understanding_model": "UNDERSTANDING-PHY-009",
     "observable_signals": ["V = IR applied with the total R to find a branch current", "no equivalent-resistance step"],
     "possible_confusions": ["total and component quantities interchanged"],
     "distinguishing_questions": ["Ask which resistance the given voltage is across"],
     "source_basis": ["physics_2023_internal_paper1_june_q8.4", "physics_2025_internal_paper1_nov_q9.4"],
     "confidence": "high"},
    {"breakdown_id": "BREAKDOWN-PHY-009-C", "stage": "concept",
     "description": "Internal resistance is ignored, so emf is treated as the terminal voltage and the lost-voltage step is missing.",
     "parent_understanding_model": "UNDERSTANDING-PHY-009",
     "observable_signals": ["emf set equal to the voltmeter reading", "r omitted from emf = I(Rext + r)"],
     "possible_confusions": ["ideal battery assumed"],
     "distinguishing_questions": ["Ask where the missing voltage goes when current flows"],
     "source_basis": ["physics_2025_internal_paper1_nov_q9.3", "physics_2025_internal_paper1_nov_q9.4"],
     "confidence": "high"},
    {"breakdown_id": "BREAKDOWN-PHY-009-D", "stage": "execution",
     "description": "The wrong power or energy form is used for what is held constant, or time is not converted for W = VIt.",
     "parent_understanding_model": "UNDERSTANDING-PHY-009",
     "observable_signals": ["uses P = I2R where the voltage is the fixed quantity", "substitutes minutes into W = VIt"],
     "possible_confusions": ["the three power forms treated as unrelated"],
     "distinguishing_questions": ["Ask which of V, I or R is fixed for this component"],
     "source_basis": ["physics_2023_internal_paper1_june_q8.6", "physics_2021_internal_paper1_nov_q7.2.2"],
     "confidence": "medium"},

    # --- PHY-010 investigations ---
    {"breakdown_id": "BREAKDOWN-PHY-010-A", "stage": "interpretation",
     "description": "The hypothesis states an outcome rather than a relationship between the named variables, or states the variables in the wrong order.",
     "parent_understanding_model": "UNDERSTANDING-PHY-010",
     "observable_signals": ["hypothesis has no second variable", "dependent and independent variables reversed"],
     "possible_confusions": ["hypothesis confused with a prediction of the result"],
     "distinguishing_questions": ["Ask which variable is being changed and which is being measured"],
     "source_basis": ["physics_2019_internal_paper1_june_q6.1"],
     "confidence": "medium"},
    {"breakdown_id": "BREAKDOWN-PHY-010-B", "stage": "execution",
     "description": "Graph construction loses marks systematically: no heading, axis labels without units, a scale that does not use the grid, or points joined dot-to-dot.",
     "parent_understanding_model": "UNDERSTANDING-PHY-010",
     "observable_signals": ["missing units on an axis", "plotted points connected instead of a line of best fit", "scale using only part of the grid"],
     "possible_confusions": ["graph conventions treated as cosmetic"],
     "distinguishing_questions": ["Ask what a marker looks for on each axis before looking at the points"],
     "source_basis": ["physics_2019_internal_paper1_june_q6.4", "physics_2021_internal_paper1_nov_q8.2",
                      "physics_2025_internal_paper1_nov_q6.1.2"],
     "confidence": "high"},
    {"breakdown_id": "BREAKDOWN-PHY-010-C", "stage": "execution",
     "description": "The gradient is calculated from plotted data points instead of from a triangle on the line of best fit, or is reported without a unit.",
     "parent_understanding_model": "UNDERSTANDING-PHY-010",
     "observable_signals": ["gradient equals y/x of one point", "no unit attached to the gradient"],
     "possible_confusions": ["line of best fit treated as decoration"],
     "distinguishing_questions": ["Ask how a gradient is taken from a straight-line graph and what units the rise and run have"],
     "source_basis": ["physics_2021_internal_paper1_nov_q8.5", "physics_2025_internal_paper1_nov_q6.1.3"],
     "confidence": "high"},
    {"breakdown_id": "BREAKDOWN-PHY-010-D", "stage": "reasoning",
     "description": "The gradient is obtained but not connected to a physical quantity, so the unknown cannot be found.",
     "parent_understanding_model": "UNDERSTANDING-PHY-010",
     "observable_signals": ["stops after the gradient", "cannot say what the axes' ratio represents"],
     "possible_confusions": ["gradient treated as a purely mathematical property"],
     "distinguishing_questions": ["Ask what physical relationship the two plotted quantities obey and what the constant in it is"],
     "source_basis": ["physics_2021_internal_paper1_nov_q8.6", "physics_2021_internal_paper1_nov_q8.7",
                      "physics_2025_internal_paper1_nov_q6.1.3"],
     "confidence": "high"},

    # --- PHY-011 photons ---
    {"breakdown_id": "BREAKDOWN-PHY-011-A", "stage": "concept",
     "description": "A single level energy is used instead of the difference between two levels, or the number of possible transitions is taken as the number of levels.",
     "parent_understanding_model": "UNDERSTANDING-PHY-011",
     "observable_signals": ["substitutes 13,6 eV alone", "answers 3 levels = 3 photons for the wrong reason"],
     "possible_confusions": ["photon energy identified with a level energy"],
     "distinguishing_questions": ["Ask which two levels the transition is between and what is released"],
     "source_basis": ["physics_2023_internal_paper1_june_q10.2", "physics_2021_internal_paper1_nov_q9.1"],
     "confidence": "medium"},
    {"breakdown_id": "BREAKDOWN-PHY-011-B", "stage": "execution",
     "description": "The eV<->J conversion is omitted or applied twice, or wavelength is not converted from nm to m.",
     "parent_understanding_model": "UNDERSTANDING-PHY-011",
     "observable_signals": ["answer in J when eV was requested", "655 substituted for 655 x 10^-9"],
     "possible_confusions": ["eV treated as an SI unit"],
     "distinguishing_questions": ["Ask what unit the answer must be in and what the given wavelength is in metres"],
     "source_basis": ["physics_2023_internal_paper1_june_q10.3", "physics_2025_internal_paper1_nov_q7.2"],
     "confidence": "high"},
    {"breakdown_id": "BREAKDOWN-PHY-011-C", "stage": "explanation",
     "description": "Beam power is confused with photon energy when explaining why one laser is more hazardous.",
     "parent_understanding_model": "UNDERSTANDING-PHY-011",
     "observable_signals": ["argues from the equal 5 mW rating", "no mention of frequency or wavelength"],
     "possible_confusions": ["intensity and photon energy conflated"],
     "distinguishing_questions": ["Ask what differs between the two beams if their total power output is the same"],
     "source_basis": ["physics_2025_internal_paper1_nov_q7.1"],
     "confidence": "medium"},

    # --- PHY-012 MCQ ---
    {"breakdown_id": "BREAKDOWN-PHY-012-A", "stage": "interpretation",
     "description": "The item is answered before the question is parsed, so a familiar phrase in an option is selected without testing it against the situation.",
     "parent_understanding_model": "UNDERSTANDING-PHY-012",
     "observable_signals": ["cannot restate what the item is asking", "selects an option contradicting their own written work elsewhere"],
     "possible_confusions": ["recognition of wording mistaken for recognition of the physics"],
     "distinguishing_questions": ["Ask the student to restate the question in their own words before choosing"],
     "source_basis": ["physics_2019_internal_paper1_june_q1.1", "physics_2023_internal_paper1_june_q1.6"],
     "confidence": "medium"},
    {"breakdown_id": "BREAKDOWN-PHY-012-B", "stage": "concept",
     "description": "The underlying concept is genuinely missing, and the same error appears in the written questions on that topic.",
     "parent_understanding_model": "UNDERSTANDING-PHY-012",
     "observable_signals": ["the same misconception appears in a written item on the same topic", "cannot eliminate any distractor on reasoning"],
     "possible_confusions": ["topic-specific misconceptions listed under the corresponding written-topic model"],
     "distinguishing_questions": ["Ask the student to solve the same situation as a written calculation"],
     "source_basis": ["physics_2021_internal_paper1_nov_q1.6", "physics_2023_internal_paper1_june_q1.7"],
     "confidence": "medium"},

    # --- PHY-013 Newton III ---
    {"breakdown_id": "BREAKDOWN-PHY-013-A", "stage": "concept",
     "description": "The normal force is given as the reaction to the weight, because the two forces are equal and opposite on the same body.",
     "parent_understanding_model": "UNDERSTANDING-PHY-013",
     "observable_signals": ["answers 'the upward force of the table on the object'", "cannot name the two interacting bodies"],
     "possible_confusions": ["equilibrium pair mistaken for a third-law pair"],
     "distinguishing_questions": ["Ask which two objects each of the two forces acts between"],
     "source_basis": ["physics_2019_internal_paper1_june_q5.5", "physics_2023_internal_paper1_june_q7.1.3"],
     "confidence": "high"},
    {"breakdown_id": "BREAKDOWN-PHY-013-B", "stage": "reasoning",
     "description": "In a collision between unequal masses the student gives the larger body the larger force, contrary to Newton's third law.",
     "parent_understanding_model": "UNDERSTANDING-PHY-013",
     "observable_signals": ["force scaled by mass", "different accelerations taken to imply different forces"],
     "possible_confusions": ["F = ma applied to the pair instead of the third law"],
     "distinguishing_questions": ["Ask which law relates the two forces the bodies exert on each other"],
     "source_basis": ["physics_2025_internal_paper1_nov_q5.3"],
     "confidence": "medium"},

    # --- PHY-014 momentum ---
    {"breakdown_id": "BREAKDOWN-PHY-014-A", "stage": "strategy",
     "description": "Only the momentum equation is written, so a two-unknown elastic collision cannot be solved, or kinetic energy is conserved but momentum is not.",
     "parent_understanding_model": "UNDERSTANDING-PHY-014",
     "observable_signals": ["one equation for two unknowns", "guesses a final velocity"],
     "possible_confusions": ["'elastic' taken to mean only energy is conserved"],
     "distinguishing_questions": ["Ask how many unknowns there are and what second condition the word 'elastic' supplies"],
     "source_basis": ["physics_2025_internal_paper1_nov_q5.2"],
     "confidence": "medium"},
    {"breakdown_id": "BREAKDOWN-PHY-014-B", "stage": "execution",
     "description": "Directions are not encoded as signs, so the momentum sum is formed from magnitudes only.",
     "parent_understanding_model": "UNDERSTANDING-PHY-014",
     "observable_signals": ["both initial velocities added as positives", "final answer without a direction"],
     "possible_confusions": ["momentum treated as a scalar"],
     "distinguishing_questions": ["Ask which direction was chosen positive and what sign each velocity then carries"],
     "source_basis": ["physics_2025_internal_paper1_nov_q5.2"],
     "confidence": "medium"},
    {"breakdown_id": "BREAKDOWN-PHY-014-C", "stage": "execution",
     "description": "In the impulse calculation the contact time is left in milliseconds or the change in momentum is taken without the sign change.",
     "parent_understanding_model": "UNDERSTANDING-PHY-014",
     "observable_signals": ["uses 20 instead of 0,02 s", "computes m(vf) only"],
     "possible_confusions": ["impulse taken as the final momentum"],
     "distinguishing_questions": ["Ask what change in velocity the contact produces and in what unit the time must be"],
     "source_basis": ["physics_2025_internal_paper1_nov_q5.5"],
     "confidence": "medium"},
]

DIAGNOSTICS = [
    # PHY-001
    {"diagnostic_id": "DIAG-PHY-001-A", "understanding_model_id": "UNDERSTANDING-PHY-001",
     "target_breakdown": "BREAKDOWN-PHY-001-B",
     "question": "In your own words, what would have to be true for a force to count as friction?",
     "purpose": "Determine whether the student holds both elements of the definition the memo ticks (opposes motion, parallel to the contact surface) without being given the wording.",
     "distinguishes": ["BREAKDOWN-PHY-001-B", "BREAKDOWN-PHY-001-C"],
     "expected_evidence": ["names the opposing role AND the direction relative to the surface", "mentions that it acts between surfaces in contact"],
     "follow_up_conditions": [
         {"condition": "only the opposing role is given", "follow_up": "If the same two surfaces are pressed together but the pull is sideways, does the friction change? Why?"},
         {"condition": "both elements given", "follow_up": "Why does the memo insist on 'parallel to the surface' rather than just 'opposing motion'?"}],
     "source_or_rationale": "Memos for 2019 Q5.2, 2021 Q5.2 and 2023 Q6.1 all split the friction definition into exactly these two ticked elements.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-001-B", "understanding_model_id": "UNDERSTANDING-PHY-001",
     "target_breakdown": "BREAKDOWN-PHY-001-A",
     "question": "A car's speedometer reads a steady 60 km/h while it goes around a roundabout. Is its velocity constant? What is the difference you are using?",
     "purpose": "Probe whether the scalar/vector boundary that separates speed from velocity and distance from displacement is actually held.",
     "distinguishes": ["BREAKDOWN-PHY-001-A"],
     "expected_evidence": ["says velocity is not constant because direction changes", "attributes constancy of speed to magnitude only"],
     "follow_up_conditions": [
         {"condition": "says velocity is constant", "follow_up": "What two things would both have to stay the same for velocity to be constant?"}],
     "source_or_rationale": "2019 Q3.2.2/3.2.3 and 2023 Q2.5 both turn on direction change with constant speed; 2021 Q1.3 tests the same idea in MCQ form.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-001-C", "understanding_model_id": "UNDERSTANDING-PHY-001",
     "target_breakdown": None,
     "question": "Two students state Ohm's law. One says 'current is proportional to voltage'. What is the other student likely to add, and why does it matter?",
     "purpose": "Test whether the student knows that the qualifying condition is part of the marked definition, not decoration.",
     "distinguishes": ["BREAKDOWN-PHY-001-B"],
     "expected_evidence": ["supplies 'at constant temperature'", "explains that resistance changes with temperature"],
     "follow_up_conditions": [
         {"condition": "cannot supply the condition", "follow_up": "What happens to a filament bulb's resistance as it gets hotter, and what does that do to the law?"}],
     "source_or_rationale": "2023 memo Q8.1 ticks 'directly proportional to the potential difference' and 'at constant temperature' separately.",
     "confidence": "high"},

    # PHY-002
    {"diagnostic_id": "DIAG-PHY-002-A", "understanding_model_id": "UNDERSTANDING-PHY-002",
     "target_breakdown": "BREAKDOWN-PHY-002-A",
     "question": "Before you calculate anything: what quantities does this question actually give you, and which one is missing?",
     "purpose": "Determine whether equation selection is driven by the known quantities or by familiarity with a formula.",
     "distinguishes": ["BREAKDOWN-PHY-002-A"],
     "expected_evidence": ["lists the givens including which are absent (often time)", "names the equation that contains exactly those plus the unknown"],
     "follow_up_conditions": [
         {"condition": "names an equation containing a quantity not given", "follow_up": "Where would that quantity come from?"}],
     "source_or_rationale": "Memo method steps for 2021 Q4.3.2 and 2023 Q2.2 begin with the specific equation containing the given quantities.",
     "confidence": "medium"},
    {"diagnostic_id": "DIAG-PHY-002-B", "understanding_model_id": "UNDERSTANDING-PHY-002",
     "target_breakdown": "BREAKDOWN-PHY-002-B",
     "question": "Which direction have you decided is positive, and what sign does each term in your equation get as a result?",
     "purpose": "Expose sign-convention failures that the memos mark separately from the final answer.",
     "distinguishes": ["BREAKDOWN-PHY-002-B"],
     "expected_evidence": ["declares a positive direction before substituting", "assigns a negative sign to g or a in the appropriate cases"],
     "follow_up_conditions": [
         {"condition": "all terms positive in a braking or upward problem", "follow_up": "The truck is slowing down while moving forward - what does that say about the sign of a relative to v?"}],
     "source_or_rationale": "2019 memo Q2.2.3 'Must show that the acceleration is negative'; 2021 memo Q4.3.2 marks the negative sign as a separate mark.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-002-C", "understanding_model_id": "UNDERSTANDING-PHY-002",
     "target_breakdown": "BREAKDOWN-PHY-002-D",
     "question": "Walk me through what happens between the start and the moment the question asks about - is it all one kind of motion?",
     "purpose": "Determine whether the student recognises a multi-stage problem before choosing a method.",
     "distinguishes": ["BREAKDOWN-PHY-002-D"],
     "expected_evidence": ["identifies the distinct stages (reaction time then braking; up then down)", "says which quantity must be found first"],
     "follow_up_conditions": [
         {"condition": "treats it as one stage", "follow_up": "Does the same equation describe the whole trip? What changes part-way through?"}],
     "source_or_rationale": "2019 memo Q2.2.4 sums three separate distances; 2023 memo Q3.3 requires the cliff height before the height above the cliff.",
     "confidence": "high"},

    # PHY-003
    {"diagnostic_id": "DIAG-PHY-003-A", "understanding_model_id": "UNDERSTANDING-PHY-003",
     "target_breakdown": "BREAKDOWN-PHY-003-A",
     "question": "On this velocity-time graph the line goes below the axis. What is the object doing while the line is negative?",
     "purpose": "Distinguish 'graph as a picture of the path' from 'graph of a signed quantity'.",
     "distinguishes": ["BREAKDOWN-PHY-003-A"],
     "expected_evidence": ["says the object moves in the negative direction", "does not claim the object is below the ground"],
     "follow_up_conditions": [
         {"condition": "reads it as position below the start", "follow_up": "What does the vertical axis measure here, and can that quantity be negative?"}],
     "source_or_rationale": "2025 Q1.1.2 asks for the greatest westward velocity, i.e. the most negative v; 2021 Q1.3 tests direction on a track diagram.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-003-B", "understanding_model_id": "UNDERSTANDING-PHY-003",
     "target_breakdown": "BREAKDOWN-PHY-003-B",
     "question": "Two sections of this graph have the same height but different steepness. Which has the greater acceleration, and what are you comparing?",
     "purpose": "Separate reading a value from reading a gradient.",
     "distinguishes": ["BREAKDOWN-PHY-003-B"],
     "expected_evidence": ["chooses the steeper section", "states that gradient represents acceleration"],
     "follow_up_conditions": [
         {"condition": "chooses by height", "follow_up": "What does the height of the line tell you, and what does the slope tell you?"}],
     "source_or_rationale": "2025 memo Q1.1.4 requires 'steepest gradient' as the separate reason mark.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-003-C", "understanding_model_id": "UNDERSTANDING-PHY-003",
     "target_breakdown": "BREAKDOWN-PHY-003-C",
     "question": "Describe the motion in this interval so that someone who cannot see the graph would know exactly what the object is doing.",
     "purpose": "Test whether the student supplies both required elements (what the velocity does, and the direction) that the memos tick separately.",
     "distinguishes": ["BREAKDOWN-PHY-003-C"],
     "expected_evidence": ["states the velocity behaviour AND the direction", "avoids ambiguous phrasing such as 'slowing down' alone"],
     "follow_up_conditions": [
         {"condition": "gives only the velocity behaviour", "follow_up": "Which way is it moving while that happens?"}],
     "source_or_rationale": "2019 memo Q3.1.2 and 2021 memo Q3.3 each allocate two marks: one for the velocity statement, one for the direction.",
     "confidence": "high"},

    # PHY-004
    {"diagnostic_id": "DIAG-PHY-004-A", "understanding_model_id": "UNDERSTANDING-PHY-004",
     "target_breakdown": "BREAKDOWN-PHY-004-A",
     "question": "Before you draw anything: how many distinct phases does this motion have, and where does each one start and stop?",
     "purpose": "Establish whether the student plans section by section, which is how these items are marked.",
     "distinguishes": ["BREAKDOWN-PHY-004-A"],
     "expected_evidence": ["identifies each phase and its boundary times", "says what the graph does in each"],
     "follow_up_conditions": [
         {"condition": "describes one overall motion", "follow_up": "Is the acceleration the same throughout? What happens at the bounce?"}],
     "source_or_rationale": "2021 memo Q3.8 and 2025 memo Q2.7 allocate marks per section of the graph.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-004-B", "understanding_model_id": "UNDERSTANDING-PHY-004",
     "target_breakdown": "BREAKDOWN-PHY-004-B",
     "question": "The cart goes up the slope and comes back down. Which part has the steeper line on your graph, and why?",
     "purpose": "Test whether relative steepness is derived from the forces rather than drawn symmetrically.",
     "distinguishes": ["BREAKDOWN-PHY-004-B"],
     "expected_evidence": ["says the upward section is steeper", "explains that friction and the weight component act in the same direction going up"],
     "follow_up_conditions": [
         {"condition": "draws them equal", "follow_up": "What forces act along the slope on the way up, and on the way down?"}],
     "source_or_rationale": "2021 memo Q6.1.5 marks 'gradient steeper on the way up than on the way down'; Q6.1.4 requires the force reasoning.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-004-C", "understanding_model_id": "UNDERSTANDING-PHY-004",
     "target_breakdown": "BREAKDOWN-PHY-004-C",
     "question": "If I only saw your graph and not the question, what values would I need labelled to know you had answered it?",
     "purpose": "Make the student treat labels and the stated direction convention as part of the answer.",
     "distinguishes": ["BREAKDOWN-PHY-004-C"],
     "expected_evidence": ["names the specific times or heights the question asks for", "confirms the direction convention matches the given graph"],
     "follow_up_conditions": [
         {"condition": "says no labels are needed", "follow_up": "The memo for this item awards a mark for labelled values - which ones would it be looking for?"}],
     "source_or_rationale": "2023 memo Q4.7 marks shapes and times separately; 2019 memo Q3.1.8 says '3/4 if on the negative side'.",
     "confidence": "high"},

    # PHY-005
    {"diagnostic_id": "DIAG-PHY-005-A", "understanding_model_id": "UNDERSTANDING-PHY-005",
     "target_breakdown": "BREAKDOWN-PHY-005-A",
     "question": "For each arrow on your diagram, which other object is doing the pushing or pulling?",
     "purpose": "Expose invented forces and third-law partners drawn on the wrong body.",
     "distinguishes": ["BREAKDOWN-PHY-005-A"],
     "expected_evidence": ["names a real interacting object for every arrow", "removes any 'force of motion' arrow"],
     "follow_up_conditions": [
         {"condition": "cannot name an agent for an arrow", "follow_up": "If no object causes that force, should it be on the diagram?"}],
     "source_or_rationale": "2025 memo Q3.1 lists the four forces with their directions; 2023 Q1.4 offers 'the ma force exerted by the crate' as a rejected distractor.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-005-B", "understanding_model_id": "UNDERSTANDING-PHY-005",
     "target_breakdown": "BREAKDOWN-PHY-005-B",
     "question": "Is the normal force here the same size as the weight? What decides that?",
     "purpose": "Test whether the normal force is treated as a fixed reaction to weight or as whatever the perpendicular equilibrium requires.",
     "distinguishes": ["BREAKDOWN-PHY-005-B"],
     "expected_evidence": ["says they differ on an incline or when a vertical component exists", "refers to the perpendicular direction having no acceleration"],
     "follow_up_conditions": [
         {"condition": "says they are always equal", "follow_up": "The rope pulls upward at 30 degrees - what does that do to how hard the ground pushes up?"}],
     "source_or_rationale": "2025 memo Q3.3 requires FN = Fg - F sin30; 2023 Q7.2.2 requires FN = mg cos theta.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-005-C", "understanding_model_id": "UNDERSTANDING-PHY-005",
     "target_breakdown": "BREAKDOWN-PHY-005-C",
     "question": "The person is slowing down as the trampoline stops them. Should the two arrows on your diagram be the same length?",
     "purpose": "Check that relative arrow length follows from the acceleration rather than being drawn equal by default.",
     "distinguishes": ["BREAKDOWN-PHY-005-C"],
     "expected_evidence": ["draws the upward force longer", "links the length difference to the upward net force"],
     "follow_up_conditions": [
         {"condition": "draws them equal", "follow_up": "If the forces were equal, what would the acceleration be?"}],
     "source_or_rationale": "2025 memo Q2.5 states 'FN must be longer than Fg'; 2021 memo Q5.1 requires 'Tension force > Friction force'.",
     "confidence": "high"},

    # PHY-006
    {"diagnostic_id": "DIAG-PHY-006-A", "understanding_model_id": "UNDERSTANDING-PHY-006",
     "target_breakdown": "BREAKDOWN-PHY-006-A",
     "question": "How many objects are accelerating here, and what is the acceleration of each?",
     "purpose": "Establish whether the string constraint is recognised before any equation is written.",
     "distinguishes": ["BREAKDOWN-PHY-006-A"],
     "expected_evidence": ["states both bodies share the same magnitude of acceleration", "explains that the inextensible string enforces this"],
     "follow_up_conditions": [
         {"condition": "gives different accelerations", "follow_up": "What would happen to the string if one body accelerated more than the other?"}],
     "source_or_rationale": "2025 memo Q4.3 and 2023 memo Q7.1.1 both solve two equations sharing one a and one T.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-006-B", "understanding_model_id": "UNDERSTANDING-PHY-006",
     "target_breakdown": "BREAKDOWN-PHY-006-A",
     "question": "Is the tension in the string equal to the weight of the hanging mass? Why or why not?",
     "purpose": "Target the most common assumption in this family, which the 2025 paper asks about before any calculation.",
     "distinguishes": ["BREAKDOWN-PHY-006-A"],
     "expected_evidence": ["says no, because the hanging mass accelerates", "uses Fnet = ma on the hanging mass to compare T and mg"],
     "follow_up_conditions": [
         {"condition": "says they are equal", "follow_up": "If T equalled the weight, what would the net force on the hanging mass be?"}],
     "source_or_rationale": "2025 Q4.1/4.2 ask for the comparison and its justification; memo answer: tension greater than weight.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-006-C", "understanding_model_id": "UNDERSTANDING-PHY-006",
     "target_breakdown": "BREAKDOWN-PHY-006-B",
     "question": "You have two equations. Which direction did you choose as positive, and is it the same in both?",
     "purpose": "Check consistency of the sign convention across the two body equations.",
     "distinguishes": ["BREAKDOWN-PHY-006-B"],
     "expected_evidence": ["one declared positive direction used in both equations", "consistent signs for a and T"],
     "follow_up_conditions": [
         {"condition": "conventions differ", "follow_up": "If both bodies accelerate 'positively' in your equations, which way is each actually moving?"}],
     "source_or_rationale": "2025 memo Q4.3 marks the equality TA on B = -TB on A explicitly, showing the convention is part of the marking.",
     "confidence": "medium"},

    # PHY-007
    {"diagnostic_id": "DIAG-PHY-007-A", "understanding_model_id": "UNDERSTANDING-PHY-007",
     "target_breakdown": "BREAKDOWN-PHY-007-A",
     "question": "Which component did you use - the one next to the 30 degree angle or the one opposite it? How did you decide?",
     "purpose": "Make the choice of trigonometric ratio explicit rather than habitual.",
     "distinguishes": ["BREAKDOWN-PHY-007-A"],
     "expected_evidence": ["identifies the adjacent side for cos", "refers to the triangle rather than to a rule of thumb"],
     "follow_up_conditions": [
         {"condition": "cannot justify the ratio", "follow_up": "Draw the triangle and mark which side is the horizontal component."}],
     "source_or_rationale": "2025 memo Q3.3 marks the substitution (300)sin30 for the vertical component, showing the ratio choice is assessed.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-007-B", "understanding_model_id": "UNDERSTANDING-PHY-007",
     "target_breakdown": "BREAKDOWN-PHY-007-B",
     "question": "The rope pulls up at an angle while the canoe is pulled along the ground. Does the ground push up as hard as it would if the rope were horizontal?",
     "purpose": "Test whether the vertical component is recognised as changing the normal force, and with it the friction.",
     "distinguishes": ["BREAKDOWN-PHY-007-B"],
     "expected_evidence": ["says the normal force is reduced", "connects the reduced normal force to reduced maximum friction"],
     "follow_up_conditions": [
         {"condition": "says the normal force is unchanged", "follow_up": "What does the upward part of the pull do to how hard the canoe presses on the mud?"}],
     "source_or_rationale": "2025 memo Q3.3 (FN = Fg - F sin30) and Q3.5 (removing load reduces FN and therefore friction).",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-007-C", "understanding_model_id": "UNDERSTANDING-PHY-007",
     "target_breakdown": "BREAKDOWN-PHY-007-C",
     "question": "You have an angle of 79,5 degrees. Measured from what, and turning which way?",
     "purpose": "Check that the mathematical angle is converted into the direction format the question asks for.",
     "distinguishes": ["BREAKDOWN-PHY-007-C"],
     "expected_evidence": ["states the reference direction", "converts correctly to a bearing"],
     "follow_up_conditions": [
         {"condition": "cannot say", "follow_up": "A bearing is measured from north clockwise - where does your angle start?"}],
     "source_or_rationale": "2019 memo Q4.1.2 awards a separate mark for the final bearing (190,5 degrees).",
     "confidence": "high"},

    # PHY-008
    {"diagnostic_id": "DIAG-PHY-008-A", "understanding_model_id": "UNDERSTANDING-PHY-008",
     "target_breakdown": "BREAKDOWN-PHY-008-A",
     "question": "Before you tell me increase or decrease: which equation links the thing that changed to the thing being asked about?",
     "purpose": "Force the governing relationship to be named before the prediction, which is how the marks are allocated.",
     "distinguishes": ["BREAKDOWN-PHY-008-A"],
     "expected_evidence": ["names a specific equation", "identifies which symbols in it are affected"],
     "follow_up_conditions": [
         {"condition": "gives the prediction with no equation", "follow_up": "What would you write down if you had to show your reasoning to a marker?"}],
     "source_or_rationale": "2019 memo Q7.7.2 requires two named formulae for 4 marks; 2025 memo Q8.3 requires emf = Vint + Vext.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-008-B", "understanding_model_id": "UNDERSTANDING-PHY-008",
     "target_breakdown": "BREAKDOWN-PHY-008-B",
     "question": "In this arrangement, which quantity stays the same for both bulbs - the current through them or the voltage across them?",
     "purpose": "Expose the series/parallel constant mix-up that makes the same relationship give opposite answers.",
     "distinguishes": ["BREAKDOWN-PHY-008-B"],
     "expected_evidence": ["identifies the constant correctly for the arrangement", "chooses the matching power form"],
     "follow_up_conditions": [
         {"condition": "gets the constant wrong", "follow_up": "In a series circuit, does the current have anywhere else to go?"}],
     "source_or_rationale": "2021 memo Q7.2.2 requires 'P inversely proportional to R at constant V' for one circuit and 'directly proportional at constant I' for the other.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-008-C", "understanding_model_id": "UNDERSTANDING-PHY-008",
     "target_breakdown": "BREAKDOWN-PHY-008-C",
     "question": "You said the power increases. What happens to the total current first, and what does that do to the voltage lost inside the battery?",
     "purpose": "Elicit the intermediate steps the memo marks, rather than a one-step jump to the conclusion.",
     "distinguishes": ["BREAKDOWN-PHY-008-C"],
     "expected_evidence": ["states that total resistance and current change", "says less voltage is lost internally so the external voltage rises"],
     "follow_up_conditions": [
         {"condition": "skips to the conclusion", "follow_up": "Where does the emf of the battery get shared out?"}],
     "source_or_rationale": "2025 memo Q8.3 awards one mark per link: increase, current decreases, less internal loss (Vint = Ir), external voltage increases.",
     "confidence": "high"},

    # PHY-009
    {"diagnostic_id": "DIAG-PHY-009-A", "understanding_model_id": "UNDERSTANDING-PHY-009",
     "target_breakdown": "BREAKDOWN-PHY-009-A",
     "question": "Which resistors in this circuit have both of their ends joined to the same two points?",
     "purpose": "Test whether parallel groupings are recognised from the connections rather than from the drawing's layout.",
     "distinguishes": ["BREAKDOWN-PHY-009-A"],
     "expected_evidence": ["identifies the parallel pair correctly", "explains the shared-node criterion"],
     "follow_up_conditions": [
         {"condition": "misidentifies the grouping", "follow_up": "Trace the wire from each end of that resistor - where does it lead?"}],
     "source_or_rationale": "2021 memo Q7.1.2 and 2023 memo Q8.2 both require the parallel combination before any current is found.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-009-B", "understanding_model_id": "UNDERSTANDING-PHY-009",
     "target_breakdown": "BREAKDOWN-PHY-009-C",
     "question": "The voltmeter across the battery reads less than the emf. Where has the rest of the emf gone?",
     "purpose": "Determine whether internal resistance and lost voltage are part of the student's circuit model.",
     "distinguishes": ["BREAKDOWN-PHY-009-C"],
     "expected_evidence": ["attributes the difference to the internal resistance", "uses emf = I(Rext + r) or Vterm = emf - Ir"],
     "follow_up_conditions": [
         {"condition": "says the reading is the emf", "follow_up": "The battery is stated to have 0,5 ohm internal resistance - what happens when current flows through it?"}],
     "source_or_rationale": "2025 memo Q9.3/Q9.4 require emf = I(Rext + r) and emf = Vext + Vint.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-009-C", "understanding_model_id": "UNDERSTANDING-PHY-009",
     "target_breakdown": "BREAKDOWN-PHY-009-B",
     "question": "The question asks for the reading on voltmeter V1. Which resistance is that voltage across - the total or one component?",
     "purpose": "Check that component-level and circuit-level quantities are not interchanged.",
     "distinguishes": ["BREAKDOWN-PHY-009-B"],
     "expected_evidence": ["identifies the component the meter is across", "uses that component's resistance in V = IR"],
     "follow_up_conditions": [
         {"condition": "uses the total resistance", "follow_up": "What is V1 physically connected to?"}],
     "source_or_rationale": "2023 memo Q8.4 requires the total current first and then V = IR for the specific resistor; 2025 memo Q9.2 does the reverse.",
     "confidence": "high"},

    # PHY-010
    {"diagnostic_id": "DIAG-PHY-010-A", "understanding_model_id": "UNDERSTANDING-PHY-010",
     "target_breakdown": "BREAKDOWN-PHY-010-A",
     "question": "In this investigation, which variable is being changed on purpose and which is being measured?",
     "purpose": "Establish whether the student can identify the variables that a hypothesis must relate in order.",
     "distinguishes": ["BREAKDOWN-PHY-010-A"],
     "expected_evidence": ["names the independent and dependent variables", "states the relationship between them, not an outcome"],
     "follow_up_conditions": [
         {"condition": "cannot separate them", "follow_up": "If you changed nothing, what would still happen?"}],
     "source_or_rationale": "2019 memo Q6.1 marks the hypothesis in three parts and notes 'order matters'.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-010-B", "understanding_model_id": "UNDERSTANDING-PHY-010",
     "target_breakdown": "BREAKDOWN-PHY-010-C",
     "question": "How would you take the gradient of this graph, and what units would it have?",
     "purpose": "Distinguish taking a gradient from the line of best fit (with units) from dividing one point's coordinates.",
     "distinguishes": ["BREAKDOWN-PHY-010-C", "BREAKDOWN-PHY-010-D"],
     "expected_evidence": ["chooses two points on the line of best fit", "gives the unit as y-unit over x-unit"],
     "follow_up_conditions": [
         {"condition": "uses a plotted point", "follow_up": "Why is the line of best fit used instead of the individual points?"}],
     "source_or_rationale": "2021 memo Q8.5 requires the gradient and its unit; 2025 memo Q6.1.3 allows a 10% tolerance, implying a read-off gradient.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-010-C", "understanding_model_id": "UNDERSTANDING-PHY-010",
     "target_breakdown": "BREAKDOWN-PHY-010-D",
     "question": "Your gradient has a value and a unit. What physical quantity in this experiment does that number represent?",
     "purpose": "Test the step that carries the most marks: equating the measured gradient to the theoretical constant.",
     "distinguishes": ["BREAKDOWN-PHY-010-D"],
     "expected_evidence": ["identifies the constant (g, or 1/(G m1 m2))", "sets up the equation to find the unknown"],
     "follow_up_conditions": [
         {"condition": "cannot say", "follow_up": "Write the theoretical equation relating the two quantities you plotted and see what the coefficient is."}],
     "source_or_rationale": "2021 memo Q8.6/Q8.7 require the gradient to be identified as 1/(G m1 m2) and then used to find the mass.",
     "confidence": "high"},

    # PHY-011
    {"diagnostic_id": "DIAG-PHY-011-A", "understanding_model_id": "UNDERSTANDING-PHY-011",
     "target_breakdown": "BREAKDOWN-PHY-011-A",
     "question": "An electron drops from the third level to the ground state. How many different photons could be emitted, and how did you count them?",
     "purpose": "Determine whether transitions are counted by pairing levels rather than by counting levels.",
     "distinguishes": ["BREAKDOWN-PHY-011-A"],
     "expected_evidence": ["gives 3", "explains the count as the possible pairs of levels involved"],
     "follow_up_conditions": [
         {"condition": "gives the wrong count", "follow_up": "List every possible downward jump between the levels."}],
     "source_or_rationale": "2021 Q9.1 and 2023 Q10.1 are the same item; both memo answers are 3.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-011-B", "understanding_model_id": "UNDERSTANDING-PHY-011",
     "target_breakdown": "BREAKDOWN-PHY-011-A",
     "question": "To find the photon's energy, which number from the diagram do you use?",
     "purpose": "Expose the use of a single level energy instead of the difference between two levels.",
     "distinguishes": ["BREAKDOWN-PHY-011-A"],
     "expected_evidence": ["takes the difference between the two levels", "handles the negative signs correctly"],
     "follow_up_conditions": [
         {"condition": "uses one level value", "follow_up": "The electron ends lower than it started - what happened to the energy in between?"}],
     "source_or_rationale": "2023 memo Q10.2 substitutes (13,6 - 3,4) x 1,6 x 10^-19, i.e. a level difference converted to joules.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-011-C", "understanding_model_id": "UNDERSTANDING-PHY-011",
     "target_breakdown": "BREAKDOWN-PHY-011-C",
     "question": "Two lasers put out the same total power, but one is green and one is red. What is different about the light itself?",
     "purpose": "Separate beam power from photon energy, the distinction the 2025 item is built on.",
     "distinguishes": ["BREAKDOWN-PHY-011-C"],
     "expected_evidence": ["says the green photons each carry more energy", "links this to shorter wavelength / higher frequency"],
     "follow_up_conditions": [
         {"condition": "argues from the power rating", "follow_up": "If the total power is the same, what must be different about the individual photons?"}],
     "source_or_rationale": "2025 memo Q7.1 requires 'higher frequency, more energy' plus 'wavelength inversely proportional to frequency'.",
     "confidence": "high"},

    # PHY-012
    {"diagnostic_id": "DIAG-PHY-012-A", "understanding_model_id": "UNDERSTANDING-PHY-012",
     "target_breakdown": "BREAKDOWN-PHY-012-A",
     "question": "Before you look at the options - what physics idea does this question turn on?",
     "purpose": "Determine whether the item is parsed before the options are considered.",
     "distinguishes": ["BREAKDOWN-PHY-012-A"],
     "expected_evidence": ["names the relevant concept without seeing the options", "then eliminates options on that basis"],
     "follow_up_conditions": [
         {"condition": "cannot name the concept", "follow_up": "Which topic in this paper does this question belong to?"}],
     "source_or_rationale": "The MCQ memos give only letters, so no distractor evidence exists; this diagnostic is Tier 3 inference designed to expose option-matching.",
     "confidence": "medium"},
    {"diagnostic_id": "DIAG-PHY-012-B", "understanding_model_id": "UNDERSTANDING-PHY-012",
     "target_breakdown": "BREAKDOWN-PHY-012-B",
     "question": "Why is each of the other three options wrong?",
     "purpose": "Distinguish lucky selection from understanding, and locate which specific concept is missing.",
     "distinguishes": ["BREAKDOWN-PHY-012-B"],
     "expected_evidence": ["gives a physics reason for rejecting each distractor", "is consistent with their written answers on the same topic"],
     "follow_up_conditions": [
         {"condition": "cannot reject the distractors", "follow_up": "Which one looks most plausible to you, and what makes it tempting?"}],
     "source_or_rationale": "No memo in this batch analyses MCQ distractors; the diagnostic is Tier 3 inference justified by the absence of that evidence.",
     "confidence": "medium"},

    # PHY-013
    {"diagnostic_id": "DIAG-PHY-013-A", "understanding_model_id": "UNDERSTANDING-PHY-013",
     "target_breakdown": "BREAKDOWN-PHY-013-A",
     "question": "The Earth pulls down on the book. What is the partner force in that interaction - which object exerts it, on what, and which way?",
     "purpose": "Test the third-law pairing directly, targeting the normal-force substitution the memos reject.",
     "distinguishes": ["BREAKDOWN-PHY-013-A"],
     "expected_evidence": ["names the book pulling up on the Earth", "keeps the force type gravitational"],
     "follow_up_conditions": [
         {"condition": "answers 'the table pushes up on the book'", "follow_up": "Which two objects does that force act between, and is it the same interaction as the weight?"}],
     "source_or_rationale": "2019 memo Q5.5 and 2023 memo Q7.1.3 both require the object's gravitational pull on the Earth, upward; 2021 Q1.7 offers the normal force as a rejected option.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-013-B", "understanding_model_id": "UNDERSTANDING-PHY-013",
     "target_breakdown": "BREAKDOWN-PHY-013-B",
     "question": "A heavy truck collides with a small car. Which one experiences the larger force during the collision, and which law tells you?",
     "purpose": "Test equal-magnitude reasoning independently of the masses.",
     "distinguishes": ["BREAKDOWN-PHY-013-B"],
     "expected_evidence": ["says the forces are equal in magnitude", "cites Newton's third law rather than F = ma"],
     "follow_up_conditions": [
         {"condition": "gives the truck the larger force", "follow_up": "If the forces are equal, why do the two vehicles respond so differently?"}],
     "source_or_rationale": "2025 memo Q5.3: 'They will experience an equal magnitude of force (NIII)'.",
     "confidence": "high"},

    # PHY-014
    {"diagnostic_id": "DIAG-PHY-014-A", "understanding_model_id": "UNDERSTANDING-PHY-014",
     "target_breakdown": "BREAKDOWN-PHY-014-A",
     "question": "You have two unknown velocities after the collision. What two facts about this collision can you turn into equations?",
     "purpose": "Determine whether the student recognises that 'perfectly elastic' supplies a second equation.",
     "distinguishes": ["BREAKDOWN-PHY-014-A"],
     "expected_evidence": ["names conservation of momentum and conservation of kinetic energy (or the relative-velocity relation)", "explains why two equations are needed"],
     "follow_up_conditions": [
         {"condition": "gives only momentum", "follow_up": "What extra information does the word 'elastic' give you?"}],
     "source_or_rationale": "2025 memo Q5.2 shows both the energy equation and the relative-velocity shortcut as accepted routes.",
     "confidence": "medium"},
    {"diagnostic_id": "DIAG-PHY-014-B", "understanding_model_id": "UNDERSTANDING-PHY-014",
     "target_breakdown": "BREAKDOWN-PHY-014-B",
     "question": "The two carts are moving towards each other. What signs will their velocities have in your equation, and which direction did you choose as positive?",
     "purpose": "Establish the sign convention before any substitution, since momentum is a vector quantity.",
     "distinguishes": ["BREAKDOWN-PHY-014-B"],
     "expected_evidence": ["declares a positive direction", "assigns opposite signs to the two initial velocities"],
     "follow_up_conditions": [
         {"condition": "adds both as positive", "follow_up": "If both velocities are positive, which way are both carts moving?"}],
     "source_or_rationale": "2025 memo Q5.2 substitutes (0,25)(+2) + (0,5)(-5), i.e. an explicit sign convention.",
     "confidence": "medium"},
]

# Families whose evidence is real but too thin for a model in this run. They are
# reported in unresolved_items with their member evidence so the next Pass 2 run
# can pick them up without re-deriving them.
DEFERRED_FAMILIES = [
    {
        "candidate_id": "CANDIDATE-FAMILY-PHY-A",
        "proposed_name": "Static-friction threshold on an inclined plane (mu = tan theta)",
        "evidence": [
            ("PHY-2019-MY", "5.6"), ("PHY-2019-MY", "5.7"),
            ("PHY-2023-MY", "7.2.2"), ("PHY-2023-MY", "7.2.3"), ("PHY-2023-MY", "7.2.4"),
        ],
        "reason_deferred": "5 members but only 2 papers; needs a third paper before a model is written",
    },
    {
        "candidate_id": "CANDIDATE-FAMILY-PHY-B",
        "proposed_name": "Work-energy theorem used instead of kinematics",
        "evidence": [
            ("PHY-2021-NOV", "6.2.1"), ("PHY-2021-NOV", "6.2.2"), ("PHY-2021-NOV", "6.2.4"),
            ("PHY-2025-NOV", "2.6"), ("PHY-2025-NOV", "4.6"),
        ],
        "reason_deferred": "5 members but only 2 papers, and 2025 Q4.6 explicitly instructs 'use ENERGY PRINCIPLES' so the two papers may not be testing the same choice",
    },
    {
        "candidate_id": "CANDIDATE-FAMILY-PHY-C",
        "proposed_name": "Symbolic 'in terms of' reasoning with no numerical data",
        "evidence": [("PHY-2019-MY", "2.3"), ("PHY-2023-MY", "2.7")],
        "reason_deferred": "2 members, 2 papers - meets the minimum for a family but is too thin for marking_requirements to be generalised",
    },
    # CANDIDATE-FAMILY-PHY-D (Newton's first law used to explain a load in an accelerating
    # vehicle) was absorbed into QUESTION-FAMILY-PHY-015 during this run: 2019 Q5.3.1 and
    # 2021 Q4.2 are members of that family, which has nine members across three papers.
    {
        "candidate_id": "CANDIDATE-FAMILY-PHY-E",
        "proposed_name": "'Prove / show that' items where the target value is printed",
        "evidence": [("PHY-2023-MY", "6.3"), ("PHY-2025-NOV", "2.4"), ("PHY-2025-NOV", "3.4")],
        "reason_deferred": "3 members but 2 papers; also overlaps QUESTION-FAMILY-PHY-002, so the boundary must be settled with more exemplars",
    },
]

MODELS += [
    {
        "identity": "UNDERSTANDING-PHY-015",
        "definition": (
            "Understanding a principle well enough to use it as the reason for a specific "
            "observation - stating the principle, applying it to the objects in the situation, and "
            "completing the causal chain the memo ticks."
        ),
        "topic": "Cross-topic: written physical explanation",
        "question_family": "QUESTION-FAMILY-PHY-015",
        "assessment_operations": ["explain a phenomenon", "justify a proposal", "link a principle to a situation"],
        "required_knowledge": [
            "Newton's first law and inertia as the explanation for a load moving relative to an "
            "accelerating vehicle",
            "friction depends on mu and the normal force, so changing either changes the maximum "
            "static friction",
            "a force at an angle has a component that pulls off the line of motion",
            "positive work means the object gains energy, negative work means it loses energy; a "
            "force perpendicular to the displacement does no work",
            "energy is lost in a bounce when the rebound speed or height is smaller",
        ],
        "prerequisites": [
            "UNDERSTANDING-PHY-001 (the principle must be statable before it can be applied)",
            "UNDERSTANDING-PHY-005 (which forces act, and in which direction)",
        ],
        "required_reasoning": [
            "identify the principle that governs the situation rather than describing what happens",
            "apply it to the specific objects named in the question",
            "complete the chain to the outcome the question asks about, in the order the memo marks",
        ],
        "required_procedure": (
            "name the principle -> apply it to the stated objects -> state the consequence -> "
            "answer the question actually asked"
        ),
        "evidence_of_understanding": [
            "names a principle rather than restating the observation",
            "completes every link the memo ticks, including the final consequence",
            "can explain the same situation in a different context (e.g. a box on a truck and a "
            "granite block on a trailer)",
        ],
        "marking_requirements": [
            "one mark per reasoning link: 2019 memo 5.3.1 ticks 'external force applied to the "
            "truck', 'inertia of the box resists the change', 'friction not great enough', 'hence "
            "it slides off'; 2021 memo 4.2 ticks the same four links",
            "2021 memo 4.3.4 requires a named equation (Ff proportional to mu for the same FN) for "
            "the third mark - a purely verbal answer cannot score full marks",
            "2025 memo 3.5 ticks 'normal force decreases' and 'Ff = mu FN so static friction "
            "decreases' - the relationship must be quoted",
            "2021 memo 6.1.2 and 6.1.3 allocate one mark per element (positive vs negative work; "
            "naming the frictional force)",
            "2019 memo 3.1.5 requires the reason from the graph, not just 'yes'",
        ],
        "common_breakdowns": ["BREAKDOWN-PHY-015-A", "BREAKDOWN-PHY-015-B", "BREAKDOWN-PHY-015-C"],
        "misconceptions": [
            "[Tier 3 inference] 'a moving object needs a force to keep moving' - the direct "
            "obstacle to the inertia explanations in 2019 Q5.3.1 and 2021 Q4.2",
            "[Tier 3 inference] 'heavier means more friction because of the weight, not because of "
            "the normal force' - the relationship the 2025 Q3.5 memo requires",
            "[Tier 3 inference] 'if nothing moves, no forces act' - blocks the equilibrium reasoning",
        ],
        "diagnostic_dimensions": ["concept", "reasoning", "explanation"],
        "diagnostic_questions": ["DIAG-PHY-015-A", "DIAG-PHY-015-B", "DIAG-PHY-015-C"],
    },
    {
        "identity": "UNDERSTANDING-PHY-016",
        "definition": (
            "Understanding that distance and speed describe the path taken while displacement and "
            "velocity describe the change in position, and being able to give both accounts of the "
            "same motion with a direction attached to the vector one."
        ),
        "topic": "Mechanics: motion",
        "question_family": "QUESTION-FAMILY-PHY-016",
        "assessment_operations": ["distinguish scalar and vector quantities", "apply both to one motion", "state a direction"],
        "required_knowledge": [
            "distance = length of the path travelled; displacement = change in position (straight "
            "line from start to finish)",
            "speed = distance/time; velocity = displacement/time and carries a direction",
            "instantaneous velocity at a point on a curved path is along the tangent there",
        ],
        "prerequisites": ["UNDERSTANDING-PHY-001", "Pythagoras and bearings for the resultant displacement"],
        "required_reasoning": [
            "add the legs for distance but take the straight line for displacement",
            "recognise that a direction must accompany any velocity",
            "keep the two accounts separate when both are asked for in one item",
        ],
        "required_procedure": None,
        "evidence_of_understanding": [
            "gives different values for distance and displacement on the same route and explains why",
            "attaches a direction to every velocity",
            "illustrates both with the positions named in the question, as the memo requires",
        ],
        "marking_requirements": [
            "2021 memo 2.1.1 awards one mark for each definition and one for each worked "
            "illustration (20 + 36 = 56 m for the path; straight line A to C for the displacement)",
            "2019 memo 3.2.3 awards four marks: distance definition, reference to the A-B-C route, "
            "displacement definition, straight line A to C with direction",
            "2019 memo 3.2.2 awards one mark for the magnitude (marked 'c.o.e.') and one for the "
            "direction 'west'",
        ],
        "common_breakdowns": ["BREAKDOWN-PHY-016-A", "BREAKDOWN-PHY-016-B"],
        "misconceptions": [
            "[Tier 3 inference] 'displacement is just the total distance in a straight line'",
            "[Tier 3 inference] 'velocity and speed have the same value in every problem'",
        ],
        "diagnostic_dimensions": ["concept", "representation"],
        "diagnostic_questions": ["DIAG-PHY-016-A", "DIAG-PHY-016-B"],
    },
]

BREAKDOWNS += [
    {"breakdown_id": "BREAKDOWN-PHY-015-A", "stage": "reasoning",
     "description": "The student describes what happens instead of naming the principle that makes it happen, so the answer restates the question.",
     "parent_understanding_model": "UNDERSTANDING-PHY-015",
     "observable_signals": ["no principle named", "answer repeats the wording of the question", "no causal connective such as 'because' or 'so'"],
     "possible_confusions": ["description mistaken for explanation"],
     "distinguishing_questions": ["Ask which physics law or relationship accounts for that, and to write it down"],
     "source_basis": ["physics_2019_internal_paper1_june_q5.3.1", "physics_2021_internal_paper1_nov_q4.2"],
     "confidence": "high"},
    {"breakdown_id": "BREAKDOWN-PHY-015-B", "stage": "explanation",
     "description": "The principle is named but the chain stops short of the consequence the question asks for, losing the final memo tick.",
     "parent_understanding_model": "UNDERSTANDING-PHY-015",
     "observable_signals": ["names inertia but does not say the box slides", "quotes a relationship but does not apply it to the numbers or objects given"],
     "possible_confusions": ["assuming naming the law completes the answer"],
     "distinguishing_questions": ["Ask what follows from that principle for this particular object"],
     "source_basis": ["physics_2025_internal_paper1_nov_q3.5", "physics_2021_internal_paper1_nov_q4.3.4"],
     "confidence": "high"},
    {"breakdown_id": "BREAKDOWN-PHY-015-C", "stage": "concept",
     "description": "The wrong principle is selected - for example friction is invoked where the memo requires inertia, or weight where the normal force governs.",
     "parent_understanding_model": "UNDERSTANDING-PHY-015",
     "observable_signals": ["invokes a principle that does not involve the quantities in the situation", "confuses weight with normal force in a friction argument"],
     "possible_confusions": ["friction attributed to weight rather than to the normal force", "inertia treated as a force"],
     "distinguishing_questions": ["Ask which two quantities the frictional force actually depends on in this situation"],
     "source_basis": ["physics_2025_internal_paper1_nov_q3.5", "physics_2021_internal_paper1_nov_q6.1.3"],
     "confidence": "medium"},
    {"breakdown_id": "BREAKDOWN-PHY-016-A", "stage": "concept",
     "description": "Distance and displacement are treated as the same quantity, so the path length is reported for both.",
     "parent_understanding_model": "UNDERSTANDING-PHY-016",
     "observable_signals": ["identical values given for distance and displacement", "no reference to the straight-line change in position"],
     "possible_confusions": ["path length and change in position conflated"],
     "distinguishing_questions": ["Ask what would change if the runner took a different route between the same two points"],
     "source_basis": ["physics_2019_internal_paper1_june_q3.2.3", "physics_2021_internal_paper1_nov_q2.1.1"],
     "confidence": "high"},
    {"breakdown_id": "BREAKDOWN-PHY-016-B", "stage": "explanation",
     "description": "A velocity is reported without a direction, losing the direction mark the memos allocate separately.",
     "parent_understanding_model": "UNDERSTANDING-PHY-016",
     "observable_signals": ["magnitude only", "no compass direction or bearing"],
     "possible_confusions": ["velocity treated as a scalar"],
     "distinguishing_questions": ["Ask what else must be stated for a velocity to be complete"],
     "source_basis": ["physics_2019_internal_paper1_june_q3.2.2"],
     "confidence": "high"},
]

DIAGNOSTICS += [
    {"diagnostic_id": "DIAG-PHY-015-A", "understanding_model_id": "UNDERSTANDING-PHY-015",
     "target_breakdown": "BREAKDOWN-PHY-015-A",
     "question": "The truck accelerates and the box slides backwards off it. Which physics idea explains that - not what happens, but why it has to happen?",
     "purpose": "Determine whether the student reaches for a governing principle rather than narrating the event.",
     "distinguishes": ["BREAKDOWN-PHY-015-A"],
     "expected_evidence": ["names inertia or Newton's first law", "says the box tends to keep its state of motion"],
     "follow_up_conditions": [
         {"condition": "only describes the sliding", "follow_up": "What would the box do if there were no friction at all between it and the truck?"}],
     "source_or_rationale": "2019 memo 5.3.1 and 2021 memo 4.2 both tick 'inertia' as a separate mark within a four-link chain.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-015-B", "understanding_model_id": "UNDERSTANDING-PHY-015",
     "target_breakdown": "BREAKDOWN-PHY-015-C",
     "question": "You said the friction gets smaller when the cooler box is taken out. What exactly does friction depend on, and which of those changed?",
     "purpose": "Test whether the friction relationship (mu and normal force) is what the student is reasoning from.",
     "distinguishes": ["BREAKDOWN-PHY-015-C", "BREAKDOWN-PHY-015-B"],
     "expected_evidence": ["names Ff = mu FN", "identifies the normal force as the quantity that changed"],
     "follow_up_conditions": [
         {"condition": "says friction depends on the weight", "follow_up": "On a slope, is the normal force equal to the weight? What does that do to your reasoning?"}],
     "source_or_rationale": "2025 memo 3.5 ticks 'normal force decreases' and 'Ff = mu FN so static friction decreases'.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-015-C", "understanding_model_id": "UNDERSTANDING-PHY-015",
     "target_breakdown": "BREAKDOWN-PHY-015-B",
     "question": "Take your explanation one step further: so what happens to the box, and why does that follow?",
     "purpose": "Check that the causal chain is carried through to the consequence the question asks about.",
     "distinguishes": ["BREAKDOWN-PHY-015-B"],
     "expected_evidence": ["states the outcome", "connects it to the previous step rather than asserting it"],
     "follow_up_conditions": [
         {"condition": "stops at the principle", "follow_up": "What would a marker still be waiting for after that sentence?"}],
     "source_or_rationale": "The final tick in 2019 memo 5.3.1 is 'hence it will slide off' - the consequence is separately marked.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-016-A", "understanding_model_id": "UNDERSTANDING-PHY-016",
     "target_breakdown": "BREAKDOWN-PHY-016-A",
     "question": "A runner goes from A to B to C. Are the distance and the displacement the same number? Which one changes if the route changes but A and C stay fixed?",
     "purpose": "Separate path length from change in position using the same setup the memos use.",
     "distinguishes": ["BREAKDOWN-PHY-016-A"],
     "expected_evidence": ["says they differ", "identifies distance as the quantity that changes with the route"],
     "follow_up_conditions": [
         {"condition": "says they are the same", "follow_up": "What is the shortest possible path from A to C, and does the runner take it?"}],
     "source_or_rationale": "2021 memo 2.1.1 and 2019 memo 3.2.3 each award separate marks for the two definitions and their application.",
     "confidence": "high"},
    {"diagnostic_id": "DIAG-PHY-016-B", "understanding_model_id": "UNDERSTANDING-PHY-016",
     "target_breakdown": "BREAKDOWN-PHY-016-B",
     "question": "You gave the athlete's velocity as 3,81 m/s. Is that a complete answer for a velocity?",
     "purpose": "Test whether the direction requirement of a vector quantity is part of the student's habit.",
     "distinguishes": ["BREAKDOWN-PHY-016-B"],
     "expected_evidence": ["says a direction is required", "supplies the correct direction for the position asked about"],
     "follow_up_conditions": [
         {"condition": "says it is complete", "follow_up": "What is the difference between that answer and a speed?"}],
     "source_or_rationale": "2019 memo 3.2.2 awards one mark for the magnitude and one for 'west'.",
     "confidence": "high"},
]
