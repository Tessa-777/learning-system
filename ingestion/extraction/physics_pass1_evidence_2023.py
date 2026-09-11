"""Pass 1 evidence table — Grade 11 Physical Science: Physics, 18 July 2023 (mid-year).

Paper:  data/organized/physics/G11- Mid-Year Examination - QP - 2023.pdf (165 marks, Mr Ntombela)
Memo:   data/organized/physics/G11- Mid-Year Examination - MG FINAL - 2023.pdf (165 marks)

Extraction caveat: several sub-question numbers are auto-numbered list items in the source
document and did not survive text extraction (Questions 4, 6.2-6.7 and 7.1/7.2 sub-parts).
Numbers used here follow the paper's visual order and are flagged with ocr_uncertain=True.
"""

PAPER = {
    "paper_key": "PHY-2023-MY",
    "paper_path": "data/organized/physics/G11- Mid-Year Examination - QP - 2023.pdf",
    "memo_path": "data/organized/physics/G11- Mid-Year Examination - MG FINAL - 2023.pdf",
    "year": 2023,
    "exam_date": "18 July 2023",
    "exam_period": "june",
    "paper_type": "paper1",
    "exam_board": "internal",
    "total_marks": 165,
    "examiner": "Mr Ntombela",
    "moderator": "Mrs Govender",
    "duration_stated": {"paper": "2,5 hours", "memo": "2,5 hours"},
    "fidelity_rung": "A",
    "notes": (
        "Paper prints topic labels on each question (e.g. 'KINEMATICS - HORIZONTAL MOTION'). "
        "Paper marks table has 10 questions (14/24/10/23/9/24/19/20/12/10); the memo's marks "
        "table has only 9 columns (14/24/11/19/33/23/15/11/10) and does not match the paper - "
        "see unresolved items."
    ),
}

SCHEMA = (
    "qn", "marks", "topic", "qtype", "text", "has_diagram", "formulae",
    "memo_answer", "memo_steps", "memo_notes", "needs_visual", "ocr_uncertain",
)

RECORDS = [
    # ---------------- QUESTION 1: MULTIPLE CHOICE (14 marks) ----------------
    ("1.1", 2, "Mechanics-Vectors", "Multiple Choice",
     "The resultant of vectors A and B is C. C will have its greatest magnitude when: A A and B act at 180 "
     "degrees / B at 90 degrees / C at 45 degrees / D at 0 degrees",
     False, [], "D", [], "Memo gives option only.", False, False),
    ("1.2", 2, "Mechanics-Motion", "Multiple Choice",
     "A ball is projected vertically upwards from the ground at speed u. Taking air resistance into account, "
     "the speed at which the ball hits the ground will be: A equal to 0 / B equal to u / C smaller than u / "
     "D bigger than u",
     False, [], "C", [], "Memo gives option only.", False, False),
    ("1.3", 2, "Mechanics-Motion graphs", "Multiple Choice",
     "A ball is dropped from rest above a hard horizontal surface; the bouncing motion is shown on a v-t "
     "graph (air resistance negligible). At which labelled point does the ball reach its maximum height after "
     "the first bounce?",
     True, [], "C", [], "Memo gives option only; graph is an image.", True, False),
    ("1.4", 2, "Mechanics-Forces", "Multiple Choice",
     "A large crate of mass m is on the flatbed of a truck but not tied down. As the truck accelerates "
     "forward with acceleration a the crate remains at rest relative to the truck. What force relative to the "
     "ground causes the crate to accelerate? A normal force / B friction force / C the ma force exerted by "
     "the crate / D no force is required",
     True, [], "B", [], "Memo gives option only; diagram is an image.", True, False),
    ("1.5", 2, "Electric Circuits", "Multiple Choice",
     "Four identical lamps P, Q, R, S connected as in diagram 1 have equal brightness. When connected as in "
     "diagram 2, which statement is correct? A lamps do not light / B dimmer than diagram 1 / C same "
     "brightness / D brighter than diagram 1",
     True, [], "C", [], "Memo gives option only; both circuit diagrams are images.", True, False),
    ("1.6", 2, "Mechanics-Forces", "Multiple Choice",
     "Newton's third law concerns forces of interaction between two bodies. Which statement is NOT correct? "
     "A the two forces act on different bodies / B always opposite in direction / C at all times equal in "
     "magnitude / D the two forces are equal and opposite so the bodies are stationary",
     False, [], "D", [], "Memo gives option only.", False, False),
    ("1.7", 2, "Mechanics-Forces", "Multiple Choice",
     "A student weighing 500 N stands on a scale in an elevator moving down. When the scale reads 520 N the "
     "elevator must be: A accelerating up / B increasing in speed / C moving at constant speed / "
     "D accelerating down",
     False, [], "A", [], "Memo gives option only.", False, False),

    # ---------------- QUESTION 2: KINEMATICS - HORIZONTAL MOTION (24 marks) ----------------
    ("2.1", 1, "Mechanics-Motion", "Definition/Explain",
     "Define the term displacement. (automated guided vehicle moving from A to B (5 m north) then B to C "
     "(4 m west))",
     True, [], "the change in position", ["change in position (1)"], "Single-mark definition.", True, False),
    ("2.2", 3, "Mechanics-Motion", "Calculation",
     "Calculate the magnitude of the acceleration of the vehicle as it moves from A to B (uniform "
     "acceleration from rest to 0,5 m.s-1 over 5 m).",
     True, ["v2 = u2 + 2as"], "0,025 m.s-2",
     ["v2 = u2 + 2as", "0,5^2 = 0^2 + 2a(5)", "a = 0,025 m.s-2"], "Formula, substitution, answer.", True, False),
    ("2.3", 4, "Mechanics-Motion", "Calculation",
     "Calculate the total time it takes for the vehicle to travel from A to C.",
     True, ["v = u + at", "v = s/t"], "28 s",
     ["A-B: 0,5 = 0 + (0,025)(COE 2.2)t -> t = 20 s", "B-C: 0,5 = 4/t -> t = 8 s", "total = 20 + 8 = 28 s"],
     "Two legs solved separately then summed; the acceleration leg is marked 'COE 2.2'.", True, False),
    ("2.4", 2, "Mechanics-Motion", "Calculation",
     "Calculate the average speed of the vehicle during the trip from A to C.",
     True, ["speed = distance/time"], "0,32 m.s-1", ["s = D/t = 9/28", "= 0,32 m.s-1"],
     "Total path length (9 m) over total time.", True, False),
    ("2.5", 2, "Mechanics-Motion", "Short Answer",
     "The vehicle travels at constant speed throughout its motion at junction B. Did the vehicle accelerate "
     "as it turned left at junction B? Explain your answer.",
     True, [], "Yes; the direction of the vehicle changed even though the speed remained constant",
     ["yes (1)", "direction changed although speed constant (1)"],
     "Tests velocity as a vector: change of direction is acceleration.", True, False),
    ("2.6.1", 3, "Mechanics-Motion", "Calculation",
     "A vehicle moves from A to F along path ABCDEF (B due north of A; section lengths shown; total time "
     "10 minutes). Calculate the total distance travelled from A to F.",
     True, [], "20 m", ["D = 6 + 8 + 2(3)", "= 20 m"],
     "Sub-number not printed in the extractable text; numbered by position.", True, True),
    ("2.6.2", 3, "Mechanics-Motion", "Calculation",
     "Determine the resultant displacement of the vehicle from A to F. Give the direction as a bearing.",
     True, ["r2 = x2 + y2"], "10 m on a bearing of 53,13 degrees",
     ["r2 = 8^2 + 6^2 -> r = 10 m", "direction = 90 - 36,87", "= 53,13 degrees"],
     "Magnitude and bearing both required.", True, True),
    ("2.6.3", 2, "Mechanics-Motion", "Calculation",
     "Calculate the magnitude of the average velocity of the vehicle during the trip from A to F.",
     True, ["v = s/t"], "0,03 m.s-1", ["v = s/t = 20/600 (COE 2.5.1)", "= 0,03 m.s-1"],
     "Time must be converted to seconds (600 s); marked COE on the displacement.", True, True),
    ("2.7", 4, "Mechanics-Motion", "Calculation",
     "A golf ball travelling rectilinearly at velocity Y slows uniformly to rest after a distance S. At what "
     "initial velocity, in terms of Y, must it be struck to come to rest in double the distance, assuming the "
     "same acceleration a?",
     False, ["v2 = u2 + 2as"], "u = sqrt(2) Y",
     ["0 = Y^2 + 2as_y -> Y^2 = -2as_y", "0 = u^2 + 2a(2s_y) -> u^2 = -2a(2s_y)",
      "OR equate the accelerations", "u = sqrt(2) Y"],
     "Same symbolic 'in terms of' item type as 2019 Q2.3.", False, False),

    # ---------------- QUESTION 3: KINEMATICS - VERTICAL MOTION (10 marks) ----------------
    ("3.1", 2, "Mechanics-Motion", "Definition/Explain",
     "Define the term velocity. (boy on a cliff projects a ball vertically upwards at 20 m.s-1; it reaches "
     "the ground 6 s after projection; upward taken as positive)",
     True, [], "the rate of change of position", ["rate of change of position (2)"], "Two-mark definition.", True, False),
    ("3.2", 3, "Mechanics-Motion", "Calculation",
     "Calculate the time taken for the ball to pass the boy on its way downwards.",
     True, ["v = u + at"], "4,08 s", ["-20 = 20 + (-9,8)t", "t = 4,08 s"],
     "Symmetry argument expressed as a sign-convention calculation; both signs marked.", True, False),
    ("3.3", 5, "Mechanics-Motion", "Calculation",
     "Calculate the height of the ball above the ground 2,8 s after it is released.",
     True, ["s = ut + 1/2 at2"], "73,98 m",
     ["height of cliff: s = 20(6) + 1/2(-9,8)6^2 = -56,4 -> 56,4 m",
      "height above cliff at 2,8 s: s = 20(2,8) + 1/2(-9,8)(2,8)^2 = 17,58 m",
      "height above ground = 56,4 + 17,58 = 73,98 m"],
     "Two-stage calculation: cliff height must be found first and then added.", True, False),

    # ---------------- QUESTION 4: KINEMATICS - BOUNCING BALL GRAPH (23 marks) ----------------
    ("4.1", 2, "Mechanics-Motion", "Definition/Explain",
     "Explain what is meant by the term free fall. (golf ball dropped from 2 m, bounces on cement; "
     "position-time graph given, not to scale)",
     True, [], "motion in which the only force acting on the object is gravity (weight)",
     ["the only force acting is gravity/weight"],
     "Memo also lists 'increasing velocity down' against the same 2-mark allocation - the following "
     "sub-question ('describe the motion between 0 s and 0,64 s') has no separate answer block.", True, True),
    ("4.2", 2, "Mechanics-Motion graphs", "Data/Graph Interpretation",
     "Describe the motion of the ball between 0 s and 0,64 s.",
     True, [], "increasing velocity down", ["increasing velocity (1)", "down (1)"],
     "Answer appears merged with 4.1 in the memo.", True, True),
    ("4.3", 1, "Mechanics-Motion graphs", "Data/Graph Interpretation",
     "Calculate the time that the golf ball is in contact with the floor before the first bounce.",
     True, [], "0,03 s", ["dt = 0,67 - 0,64 = 0,03 s"], "Single mark read off the graph.", True, True),
    ("4.4", 2, "Mechanics-Motion graphs", "Data/Graph Interpretation",
     "Calculate the time it takes the golf ball to reach its maximum height after the first bounce.",
     True, [], "0,62 s", ["dt = (1,90 - 0,67)/2 = 0,62 s"],
     "Requires halving the flight interval - symmetry of vertical motion.", True, True),
    ("4.5", 3, "Mechanics-Motion", "Calculation",
     "Calculate the speed at which the golf ball leaves the floor at the first bounce.",
     True, ["v = u + at"], "6,08 m.s-1",
     ["v = u + at", "0 = u + (-9,8)(0,62) (COE 4.1.4)", "u = 6,08 m.s-1"],
     "Memo note: 'Up+ (accept any relevant equation and direction)'; the time used is COE from 4.4.", True, True),
    ("4.6", 5, "Mechanics-Motion", "Calculation",
     "Calculate time t indicated on the graph.",
     True, ["v2 = u2 + 2as", "s = ut + 1/2 at2"], "2,96 s",
     ["v2 = u2 + 2as -> 0 = u2 + 2(-9,8)(1,2) -> u = -4 m.s-1",
      "OR 1,2 = 4,85t + 1/2(-9,8)t2 -> t = 2,95 or 2,96",
      "OR drop leg: 1,2 = 4,9t2 -> t = 0,49; Tt = 1,97 + 2(0,49) = 2,96"],
     "Three alternative routes accepted.", True, True),
    ("4.7", 5, "Mechanics-Motion graphs", "Diagram-based",
     "Sketch a velocity-time graph for the motion of the golf ball from 0 s to 1,97 s, clearly indicating the "
     "times on the graph (no other values required).",
     True, [], "v-t graph with marked times 0,64 / 0,67 / 1,90 / 1,97",
     ["shapes (marks)", "times 0,64; 0,67; 1,90; 1,97 (marks)"],
     "Memo note: 'Accept the reflection of this graph'.", True, True),
    ("4.8", 3, "Work Energy Power", "Short Answer",
     "Is energy lost during the bounce? Circle YES or NO. Give a reason using information in the graph.",
     True, [], "Yes; the maximum height reached by the ball decreases",
     ["yes (1)", "maximum height reached decreases (1)"],
     "Reason must be taken from the graph. Same item type as 2019 Q3.1.5.", True, True),

    # ---------------- QUESTION 5: NEWTON'S LAWS AND VECTORS (9 marks) ----------------
    ("5.1", 2, "Mechanics-Forces", "Definition/Explain",
     "State Newton's first law of motion. (doll suspended by two strings; string A at 40 degrees to the "
     "ceiling, string B at 90 degrees to the wall; tension in A is 12,2 N)",
     True, [],
     "an object continues in a state of rest or uniform (constant) velocity unless acted upon by a net or "
     "resultant force",
     ["state of rest or uniform velocity", "unless acted on by a net/resultant force"],
     "Verbatim the same wording as the 2019 memo for 5.1.", True, False),
    ("5.2", 3, "Mechanics-Vectors", "Diagram-based",
     "Draw a triangle of forces (vector addition diagram) for the forces acting on the doll.",
     True, [], "closed triangle of the two tensions and the weight",
     ["one mark for each correct force"],
     "Memo note: 'minus 1 for angle not shown'.", True, False),
    ("5.3", 4, "Mechanics-Vectors", "Calculation",
     "Hence, determine the mass of the doll.",
     True, ["cos50 = Fg/12,2", "Fg = mg"], "0,8 kg",
     ["cos50 = Fg/12,2", "mg = 12,2 cos50", "m = 12,2 cos50 / 9,8", "m = 0,8 kg"],
     "Chained from the candidate's own diagram ('Hence').", True, False),

    # ---------------- QUESTION 6: NEWTON'S LAWS (24 marks) ----------------
    ("6.1", 2, "Mechanics-Forces", "Definition/Explain",
     "Define the term frictional force due to surface. (cartoon character on a crate dragging a toy box by "
     "a rope over a frictionless pulley; mu_k = 0,15 for both surfaces)",
     True, [], "the force that opposes the motion of an object and acts parallel to the surface in contact",
     ["opposes motion", "parallel to the contact surface"],
     "Third recurrence of the same two-part friction definition (2019 Q5.2, 2021 Q5.2).", True, False),
    ("6.2", 5, "Mechanics-Forces", "Diagram-based",
     "Draw a fully-labelled free body diagram of all the forces acting on the crate.",
     True, [], "weight, normal force, applied force F = 120 N, friction, tension",
     ["weight", "normal force", "F = 120 N", "Ff", "tension"], "One mark per correctly labelled force.", True, False),
    ("6.3", 2, "Mechanics-Forces", "Calculation",
     "Prove that the kinetic friction on the toy box is 2,76 N.",
     True, ["Ff = mu_k FN"], "2,76 N", ["Ffk = uk FN = 0,15 x 167,87", "= 2,76 N"],
     "'Prove' items give the target value and require the working to reach it.", True, False),
    ("6.4", 3, "Mechanics-Forces", "Calculation",
     "Calculate the normal force experienced by the cartoon and the crate if they have a combined mass of "
     "25 kg.",
     True, ["FN = Fg - FA sin theta"], "167,87 N",
     ["FN = Fg - FA", "= (25 x 9,8) - (120 sin40)", "= 167,87 N"],
     "Requires resolving the applied force vertically.", True, False),
    ("6.5", 3, "Mechanics-Forces", "Calculation",
     "Calculate the magnitude of the kinetic frictional force that the cartoon and the crate experience.",
     True, ["Ff = mu_k FN"], "25,18 N", ["Ffk = uk FN", "= 0,15 x 167,87 (COE 6.4)", "= 25,18 N"],
     "Marked COE 6.4.", True, False),
    ("6.6", 6, "Mechanics-Forces", "Calculation",
     "Prove by calculation that the force exerted by Mr Ntombela's son is sufficient to accelerate the "
     "system towards the cricket centre at a rate greater than 2 m.s-2.",
     True, ["Fnet = ma"], "a = 2,12 m.s-2",
     ["crate: FA - Ff - T = ma -> 120cos40 - 28,18 - T = 25a -> T = 66,74 - 25a",
      "toy box: T - Ff - Fg(parallel) = 2a with (0,15)(2)(9,8)cos20 and (2)(9,8)sin20",
      "T - 2,76 - 6,7 = 2a", "66,74 - 25a = 2a + 9,46", "a = 2,12 m.s-2"],
     "Two-body system; six marks across the two equations and the final comparison with 2 m.s-2.", True, False),
    ("6.7", 3, "Mechanics-Forces", "Definition/Explain",
     "Luke claims that exerting the same force at an angle of 0 degrees would make the applied force on the "
     "crate greater, the frictional force less, and therefore the acceleration greater. Critically analyse "
     "his reasoning.",
     True, [],
     "the net force would increase from 66,7 to 120; the friction would increase from 25 to 36,75; yes, the "
     "net force would be greater",
     ["net force increases from 66,7 to 120 (1)", "friction increases from 25 to 36,75 (1)",
      "conclusion: net force would be greater (1)"],
     "Requires evaluating a student's claim - two of the three marks are quantitative corrections to the claim.", True, False),

    # ---------------- QUESTION 7: NEWTON'S LAWS / PULLEY / INCLINE (19 marks) ----------------
    ("7.1.1", 5, "Mechanics-Forces", "Calculation",
     "Two masses (10 kg and 5 kg) are attached to a light inextensible cable over a smooth pulley and "
     "released from rest. Calculate the magnitude of the acceleration of the system and the tension in the "
     "cable.",
     True, ["Fnet = ma"], "a = 3,27 m.s-2; T = 65,33 N",
     ["10 kg: (10)(9,8) - T = 10a -> 98 - 10a = T ...(1)",
      "5 kg: T - Fg = 5a -> T = 5a + 49 ...(2)",
      "98 - 10a = 5a + 49 -> a = 3,27 m.s-2", "T = 65,33 N"],
     "Both quantities required for full marks; simultaneous equations.", True, False),
    ("7.1.2", 2, "Mechanics-Forces", "Definition/Explain",
     "State Newton's third law of motion.",
     False, [],
     "when object A exerts a force on object B, object B simultaneously exerts an oppositely directed force "
     "of equal magnitude on object A",
     ["oppositely directed force", "equal magnitude / simultaneous"], "Two-part statement.", False, False),
    ("7.1.3", 2, "Mechanics-Forces", "Short Answer",
     "Give the name and direction of the reaction force to the weight of the 5 kg mass piece.",
     False, [], "the pulling gravitational force of the 5 kg mass piece on the Earth, upwards",
     ["gravitational force of the mass on the Earth (1)", "upwards (1)"],
     "Same item type as 2019 Q5.5 and 2021 Q1.7.", False, False),
    ("7.2.1", 2, "Mechanics-Forces", "Definition/Explain",
     "Define the term normal force. (brick on an inclined plane; theta increased until the brick slides)",
     True, [], "the perpendicular force exerted by a surface on an object in contact with it",
     ["perpendicular force", "exerted by a surface on an object in contact"], "Two-part definition.", True, False),
    ("7.2.2", 2, "Mechanics-Forces", "Calculation",
     "Write an expression in terms of theta for the normal force acting on the brick.",
     True, ["FN = mg cos theta"], "FN = mg cos theta", ["mg cos theta (2)"],
     "Symbolic expression only.", True, False),
    ("7.2.3", 2, "Mechanics-Forces", "Calculation",
     "Write an expression in terms of theta for the maximum static friction force acting on the brick before "
     "it begins to slide.",
     True, ["Ff = mg sin theta"], "Ffs(max) = mg sin theta", ["mg sin theta (2)"],
     "Requires the equilibrium condition at the point of sliding.", True, False),
    ("7.2.4", 4, "Mechanics-Forces", "Calculation",
     "A 1,3 kg block is placed on a different rough surface with mu_s = 0,48 inclined at theta. Theta is "
     "increased until the block starts to slide. Calculate the angle theta when the block is just about to "
     "slide down the slope. Show all your working out.",
     True, ["Ffs(max) = mu_s FN", "tan theta = mu_s"], "25,64 degrees",
     ["Fg(parallel) = mu_s Fg(perpendicular)", "mg sin theta = mu_s mg cos theta",
      "tan theta = 0,48", "theta = 25,64 degrees"],
     "Same mu = tan theta derivation as 2019 Q5.7; 'show all your working out' is stated on the paper.", True, False),

    # ---------------- QUESTION 8: ELECTRIC CIRCUITS (20 marks) ----------------
    ("8.1", 2, "Electric Circuits", "Definition/Explain",
     "State Ohm's Law. (circuit with 4R and 6R resistors; internal resistance and wire resistance ignored)",
     True, [],
     "the current through a conductor is directly proportional to the potential difference across the "
     "conductor at constant temperature",
     ["directly proportional to potential difference", "at constant temperature"],
     "The 'constant temperature' condition is separately marked.", True, False),
    ("8.2", 3, "Electric Circuits", "Calculation",
     "Calculate the value of resistor R if the total resistance of the circuit is 4,8 ohm.",
     True, ["1/Rp = 1/R1 + 1/R2"], "R = 2 ohm",
     ["1/4,8 = 1/4R + 1/6R", "Rs = 2 ohm"], "Algebraic solution of the parallel formula.", True, False),
    ("8.3", 2, "Electric Circuits", "Definition/Explain",
     "Define the term potential difference.",
     False, [], "the work done per unit positive charge", ["work done per unit charge (2)"],
     "Two marks for the definition.", False, False),
    ("8.4", 5, "Electric Circuits", "Calculation",
     "Calculate the reading on the voltmeter if the current through the 4R resistor is 1,8 A.",
     True, ["I = V/R", "V = IR"], "4,8 V",
     ["I = V/R", "I = 14,4/12", "I = 1,2 A", "V = IR = 1,2 x 4", "= 4,8 V"],
     "Two-stage: total current first, then the voltmeter reading.", True, False),
    ("8.5", 2, "Electric Circuits", "Definition/Explain",
     "Define the term electrical work.",
     False, [], "the work done on a charged particle by an electric field",
     ["work done on a charged particle", "by an electric field"], "Two-part definition.", False, False),
    ("8.6", 3, "Electric Circuits", "Calculation",
     "Calculate the amount of energy dissipated by the 4R resistor in 2 minutes.",
     True, ["W = VIt"], "3110,4 J", ["W = VIt = 14,4 x 1,8 x 120", "= 3110,4 J"],
     "Time must be converted to seconds (120 s).", True, False),
    ("8.7", 1, "Electric Circuits", "Short Answer",
     "The 4R resistor is replaced with an ammeter. How will the reading on the voltmeter be influenced? "
     "Circle only INCREASE, DECREASE or STAY THE SAME.",
     True, [], "DECREASE", ["decrease (1)"], "Single-mark qualitative prediction.", True, False),
    ("8.8", 2, "Electric Circuits", "Definition/Explain",
     "Explain the answer to Question 8.7.",
     True, [], "the ammeter short circuits the resistors; no current flows through the resistor",
     ["ammeter short circuits the resistors (1)", "no current flows through the resistor (1)"],
     "Memo cross-reference is mis-numbered ('QUESTION 7.7' in the memo text).", True, True),

    # ---------------- QUESTION 9: ELECTRIC CIRCUITS - LEDs (12 marks) ----------------
    ("9.1", 2, "Electric Circuits", "Definition/Explain",
     "Define diode. (circuit with three LEDs A, B, C, switches S1 and S2; R1 = R2 = R3)",
     True, [], "a component that will only allow current to flow in one direction",
     ["allows current in one direction only (2)"], "Two marks for the definition.", True, False),
    ("9.2", 2, "Electric Circuits", "Definition/Explain",
     "The LED A has a knee voltage of 2,5 V. Briefly explain what a knee voltage is.",
     True, [], "the forward voltage required to allow an LED to work",
     ["forward voltage required for the LED to work (2)"], "Applied definition question.", True, False),
    ("9.3", 1, "Electric Circuits", "Short Answer",
     "Which switch should be closed to produce the brightest possible light? Circle S1 or S2.",
     True, [], "S1", ["S1 (1)"], "Single-mark choice.", True, False),
    ("9.4", 2, "Electric Circuits", "Definition/Explain",
     "Explain your answer to Question 9.3.",
     True, ["P = I2R", "P = V2/R"],
     "R is equal so double the current flows through R1 compared to R3 and R2; voltage is divided over B and "
     "C so A receives double their voltage; power is proportional to brightness and A receives four times "
     "the power",
     ["double the current through R1 (1)", "voltage divided over B and C / power-brightness link (1)"],
     "Paper allocates 2 marks; the memo shows '(3)' against this answer - contradiction logged.", True, False),
    ("9.5", 5, "Electric Circuits", "Calculation",
     "If the emf of both cells is 9 V, what must the resistances of R3 and R2 be so that the potential "
     "difference over LEDs B and C equals the knee voltage while allowing 10 mA through each LED?",
     True, ["V = IR"], "200 ohm",
     ["voltage remaining = 9 - 2,5 - 2,5 = 4 V", "2R = V/I = 4/0,01 = 400", "R = 200 ohm"],
     "Requires combining two LEDs' knee voltages and the series current.", True, False),

    # ---------------- QUESTION 10: ELECTROMAGNETIC SPECTRUM (10 marks) ----------------
    ("10.1", 2, "Waves Sound Light", "Short Answer",
     "The energy levels for a hydrogen atom are shown; an excited electron is in the 3rd level. How many "
     "unique frequencies will be in the emission spectrum as the electron returns to the ground state?",
     True, [], "3", ["3 (2)"],
     "Identical item to 2021 Q9.1 (worth 1 mark there, 2 marks here).", True, False),
    ("10.2", 4, "Waves Sound Light", "Calculation",
     "Calculate the frequency of the photon emitted when the electron transition is from the n = 2 level to "
     "the ground state.",
     True, ["E = hf"], "2,47 x 10^15 Hz",
     ["E = hf", "(13,6 - 3,4) x 1,6 x 10-19 = 6,6 x 10-34 f", "f = 2,47 x 10^15 Hz"],
     "Requires the eV-to-joule conversion; same item as 2021 Q9.2 whose memo answer was an image.", True, False),
    ("10.3", 4, "Waves Sound Light", "Calculation",
     "Hydrogen gas in a discharge tube emits light of wavelength 655 nm. Calculate the energy (in eV) that "
     "corresponds to this wavelength.",
     True, ["E = hc/lambda"], "1,89 eV",
     ["E = hc/lambda = (6,6 x 10-34)(3 x 10^8)/(655 x 10-9)", "E = 3,02 x 10-19 J", "E = 1,89 eV"],
     "Final answer must be converted to eV as instructed.", True, False),
]
