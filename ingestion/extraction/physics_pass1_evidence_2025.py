"""Pass 1 evidence table — Grade 11 Physical Science: Physics, 03 November 2025 (final).

Paper:  data/organized/physics/G11 -  QP - Physics Final Exam - Nov - 2025.pdf (135 marks, Mr Hilder)
Memo:   data/organized/physics/G11 -  MG - Physics Final Exam - Nov - 2025.pdf

The memo's mathematical content is set in a maths font that extracts imperfectly
(italic-glyph substitutions), so numeric working is marked ocr_uncertain where the
extraction was garbled even though the answer values were legible.
"""

PAPER = {
    "paper_key": "PHY-2025-NOV",
    "paper_path": "data/organized/physics/G11 -  QP - Physics Final Exam - Nov - 2025.pdf",
    "memo_path": "data/organized/physics/G11 -  MG - Physics Final Exam - Nov - 2025.pdf",
    "year": 2025,
    "exam_date": "03 November 2025",
    "exam_period": "nov",
    "paper_type": "paper1",
    "exam_board": "internal",
    "total_marks": 135,
    "examiner": "Mr Hilder",
    "moderator": "Mr Ntombela",
    "duration_stated": {"paper": "2 hours", "memo": "2 hours"},
    "fidelity_rung": "A",
    "notes": (
        "Paper header states MARKS 135 and its Question Total row sums to 135 "
        "(18/23/15/18/16/17/5/7/16); the memo header states MARKS 125 while its own "
        "Question Total row also sums to 135 - contradiction logged. Memo also splits "
        "6.1.3 into 6.1.3/6.1.4/6.1.5 and re-allocates marks in Q8 relative to the paper."
    ),
}

SCHEMA = (
    "qn", "marks", "topic", "qtype", "text", "has_diagram", "formulae",
    "memo_answer", "memo_steps", "memo_notes", "needs_visual", "ocr_uncertain",
)

RECORDS = [
    # ---------------- QUESTION 1: VELOCITY-TIME GRAPH + TWO-BODY KINEMATICS (18) ----------------
    ("1.1.1", 2, "Mechanics-Motion", "Definition/Explain",
     "Define velocity. (Roomba vacuum cleaner moving in a straight line; velocity-time graph with points a-i)",
     True, [], "the rate of change of position (or rate of displacement / rate of change of displacement)",
     ["rate of change of position (2)"], "Memo note: 'AON' - any of three equivalent phrasings accepted.", True, False),
    ("1.1.2", 2, "Mechanics-Motion graphs", "Data/Graph Interpretation",
     "During which interval(s) was the Roomba moving with the greatest westward velocity?",
     True, [], "d-e", ["d-e (2)"], "Requires reading negative velocity as westward.", True, False),
    ("1.1.3", 2, "Mechanics-Motion graphs", "Data/Graph Interpretation",
     "At which point(s) did the Roomba change direction?",
     True, [], "c, f and i", ["c and f and i (2)"], "Direction change = sign change of velocity.", True, False),
    ("1.1.4", 3, "Mechanics-Motion graphs", "Data/Graph Interpretation",
     "During which interval(s) was the magnitude of the Roomba's acceleration greatest? Briefly explain how "
     "you got to your answer.",
     True, [], "e-g (or e-f or f-g); it has the steepest gradient",
     ["interval identified (2)", "explanation: steepest gradient (1)"],
     "Explanation mark requires linking acceleration to gradient.", True, False),
    ("1.1.5", 4, "Mechanics-Motion graphs", "Diagram-based",
     "Draw a sketch graph to show the Roomba's acceleration with time over the period shown. Label points a-i.",
     True, [], "step acceleration graph: hi < cd, eg < ab, de and gh = 0",
     ["h-i smaller than c-d (1)", "e-g smaller than a-b (1)", "d-e and g-h equal zero (1)", "labels (1)"],
     "Memo note: 'inconsistent sign convention (-1)'.", True, False),
    ("1.2", 5, "Mechanics-Motion", "Calculation",
     "A child rides a scooter at constant 1,2 m.s-1; the Roomba is at rest 2 m ahead and accelerates sideways "
     "across a 1,5 m wide hallway. Calculate the minimum acceleration the Roomba needs to just clear the "
     "hallway before the scooter reaches it.",
     True, ["v = dx/dt", "s = ut + 1/2 at2"], "1,08 m.s-2",
     ["child: 1,2 = 2/dt -> dt = 1,67 s", "Roomba: 1,5 = 0 + 1/2 a(1,67)^2", "3 = 2,776a", "a = 1,08 m.s-2"],
     "Two-body problem: the time available is set by the other object's motion.", True, False),

    # ---------------- QUESTION 2: VERTICAL MOTION / TRAMPOLINE (23) ----------------
    ("2.1", 2, "Mechanics-Motion", "Definition/Explain",
     "Define the term displacement. (70 kg person jumps upward at 4,2 m.s-1 from a platform, free-falls for "
     "1,57 s onto a trampoline)",
     True, [], "change in position", ["change in position (2)"], "Two-mark definition.", True, False),
    ("2.2", 3, "Mechanics-Motion", "Calculation",
     "Calculate the height h of the first platform above the trampoline.",
     True, ["dy = vi t + 1/2 gt2"], "5,48 m",
     ["dy = vi t + 1/2 gt2", "h = (4,2)(1,57) + 1/2(-9,8)(1,57)^2", "h = -5,48 m -> 5,48 m above the trampoline"],
     "Memo marks the sign convention explicitly ('e&s' = equation and substitution).", True, False),
    ("2.3", 4, "Mechanics-Motion", "Calculation",
     "Calculate the person's maximum displacement relative to the trampoline during their initial jump.",
     True, ["vf2 = vi2 + 2g dy"], "6,38 m",
     ["0 = 4,2^2 + 2(-9,8)(y_max - 5,48) (coe 2.2)", "-17,64 = -19,6(y_max - 5,48)",
      "0,9 = y_max - 5,48", "y_max = 6,38 m"],
     "Requires adding the rise above the platform to the platform height.", True, False),
    ("2.4", 3, "Mechanics-Motion", "Calculation",
     "Show that the magnitude of the person's velocity just before landing on the trampoline is "
     "approximately 11,19 m.s-1.",
     True, ["vf = vi + at", "vf2 = vi2 + 2g dy", "dy = ((vi+vf)/2)dt"], "11,19 m.s-1",
     ["Method A: vf = vi + at = 4,2 + (-9,8)(1,57) = -11,19 m.s-1",
      "Method B: dy = ((vi+vf)/2)dt", "Method C: vf2 = vi2 + 2g dy"],
     "'Show that' item: three alternative methods all accepted.", True, True),
    ("2.5", 2, "Mechanics-Forces", "Diagram-based",
     "Draw a labelled free-body diagram showing all forces acting on the person as the trampoline brings "
     "them to rest.",
     True, [], "normal/trampoline force upward (longer than weight) and weight downward",
     ["FN / Ftrampoline (1)", "Fg (1)"],
     "Memo note: 'FN must be longer than Fg' - relative magnitude is part of the mark.", True, False),
    ("2.6", 4, "Mechanics-Momentum", "Calculation",
     "Determine the average force exerted by the trampoline on the person as it brings him to rest over the "
     "downward stretch of 0,8 m.",
     True, ["vf2 = vi2 + 2a dy", "Fnet = ma"], "6164,2 N",
     ["vf2 = vi2 + 2a dy -> 0 = -11,2^2 + 2a(-0,8) -> a = 78,26 m.s-2",
      "Fnet = Fg + Ftrampoline -> (70)(78,4) = (70)(-9,8) + FT", "FT = 6164,2 N",
      "OR work-energy: Wnet = dEk -> -0,8F + (686)(-0,8) = -1/2(70)(11,2^2) -> F = 6164,2 N"],
     "Two independent methods (Newton II and work-energy) are both fully marked.", True, True),
    ("2.7", 5, "Mechanics-Motion graphs", "Diagram-based",
     "Sketch a vertical displacement-time graph of the motion from the jump off the first platform to landing "
     "on the second platform 3,0 m above the trampoline, using the trampoline as zero reference and labelling "
     "key points/values.",
     True, [], "displacement-time curve as shown in the memo",
     ["axis labels with units and names", "calculated values shown", "initial jump motion negative curve",
      "curve below the axis to -0,8 m", "bounce up: negative curve not reaching zero, lower than max"],
     "Five marks distributed over labelling and the shape of each phase.", True, False),

    # ---------------- QUESTION 3: STATIC FRICTION / APPLIED FORCE AT AN ANGLE (15) ----------------
    ("3.1", 4, "Mechanics-Forces", "Diagram-based",
     "A boy pulls a 50 kg canoe carrying a 20 kg cooler box with 300 N at 30 degrees to the horizontal; "
     "mu_s = 0,6. Draw a labelled free-body diagram showing all the forces acting on the canoe.",
     True, [], "weight down, normal force up, applied force at 30 degrees up-right, static friction left",
     ["Fg / weight: arrow vertically down (1)", "FN / normal force: arrow vertically up (1)",
      "FA / tension: arrow at 30 degrees up and to the right (1)", "fs / static friction: arrow horizontally left (1)"],
     "The memo states an explicit per-force marking criteria list.", True, False),
    ("3.2", 2, "Mechanics-Forces", "Definition/Explain",
     "Explain what is meant by the term maximum static frictional force.",
     False, [], "the maximum force that opposes the tendency of motion of a stationary object",
     ["maximum force opposing the tendency of motion", "of a stationary object"],
     "Two marks; the 'stationary object' qualifier is required.", False, False),
    ("3.3", 3, "Mechanics-Forces", "Calculation",
     "Calculate the normal force acting on the canoe.",
     True, ["FN = Fg - Fy"], "536 N",
     ["FN = Fg - Fy", "= (70)(9,8) - (300)sin30", "= 686 - 150 = 536 N"],
     "Requires subtracting the vertical component of the applied force.", True, False),
    ("3.4", 4, "Mechanics-Forces", "Calculation",
     "Determine, by means of a full calculation, that the boy will not be able to move the fully loaded "
     "canoe (70 kg).",
     True, ["Fs(max) = mu_s FN", "Fx = FA cos theta"], "will not move",
     ["Fs(max) = (0,6)(536) = 321,6 N", "Fx = 300 cos30 = 267,30 N",
      "the applied force is less than static friction so it will not move"],
     "'Determine by full calculation' items require both quantities AND the comparison statement.", True, False),
    ("3.5", 2, "Mechanics-Forces", "Definition/Explain",
     "The boy removes the cooler box and can now move the canoe with the same force at the same angle. "
     "Provide an explanation as to why he is able to move the canoe.",
     True, ["Ff = mu_s FN"],
     "removing the cooler box decreases the normal force; since Ff = mu_s FN the static frictional force "
     "decreases",
     ["normal force decreases (1)", "Ff = mu_s FN so static friction decreases (1)"],
     "Causal chain with a quoted relationship.", True, False),

    # ---------------- QUESTION 4: CONNECTED BODIES + WORK-ENERGY + POWER (18) ----------------
    ("4.1", 1, "Mechanics-Forces", "Short Answer",
     "Block A (5 kg) on a rough 30-degree incline is connected over a frictionless pulley to hanging block B "
     "(2 kg); 2 N of friction acts on A while accelerating. How does the tension compare to the weight of "
     "block B while the system accelerates? Circle GREATER THAN, LESS THAN or EQUAL TO.",
     True, [], "GREATER THAN", ["greater than (1)"], "Single-mark qualitative comparison.", True, False),
    ("4.2", 2, "Mechanics-Forces", "Definition/Explain",
     "Justify your answer to 4.1, referring to the forces on block B and Newton's Second Law.",
     True, ["Fnet = ma"],
     "block B accelerates upwards so there must be a net force upwards; the forces are weight down and "
     "tension up, so tension must be greater than weight",
     ["net force upwards because B accelerates up (1)", "therefore FT > Fg (1)"],
     "Explicit instruction to reference Newton's Second Law.", True, False),
    ("4.3", 4, "Mechanics-Forces", "Calculation",
     "Calculate the tension in the string to validate the answer to 4.2.",
     True, ["Fnet = ma"], "T = 20,64 N; a = -0,42 m.s-2",
     ["A: Fg(parallel) + FT + Ff = ma -> 24,5 + FT - 2 = 5a -> FT = 5a + 22,5",
      "B: FT + Fg = 2a -> -19,8 + FT = 2a -> FT = 2a + 19,8",
      "TA on B = -TB on A -> 5a + 22,5 = -2a + 19,8", "a = -0,42 m.s-2", "T = 20,64 N"],
     "Two-body simultaneous equations; sign convention drives the whole solution.", True, True),
    ("4.4", 1, "Mechanics-Forces", "Short Answer",
     "How does the magnitude of the system's acceleration compare to the acceleration due to gravity on "
     "Earth? Circle GREATER THAN, LESS THAN or EQUAL TO.",
     False, [], "LESS THAN", ["less than"],
     "Memo adds a 2-mark justification: the net force accelerates the total mass, and the opposing component "
     "of A's weight reduces the net force below Fg of B.", False, False),
    ("4.5", 2, "Work Energy Power", "Definition/Explain",
     "State the work-energy theorem.",
     False, [], "the work done on an object by a net force is equal to the object's change in kinetic energy",
     ["work done by a net force", "equals change in kinetic energy"], "Two-part statement.", False, False),
    ("4.6", 3, "Work Energy Power", "Calculation",
     "When the block reaches the end of the slope it has gained 1,59 J of kinetic energy. Use ENERGY "
     "PRINCIPLES to determine how far the block travelled along the slope after being released.",
     True, ["Wnet = dEk"], "0,77 m",
     ["W = dEk; Fnet dx = Ekf - Eki", "(Fg(parallel) + Ff + FN)dx = 1,59 - 0",
      "(24,5 + (-2) + (-20,44) coe 4.3)dx = 1,59", "2,06 dx = 1,59", "dx = 0,77 m"],
     "Question wording says 'block B travelled along the slope' although B hangs vertically and A is on the "
     "slope; the memo solves for the block on the slope - wording defect logged.", True, True),
    ("4.7", 5, "Work Energy Power", "Calculation",
     "Block B is replaced by a perfectly efficient electric motor which pulls the 5 kg block up the same "
     "slope at constant velocity 0,5 m.s-1. Determine the electrical power that must be supplied to the motor.",
     True, ["Fnet = 0", "P = Fv"], "12,12 W",
     ["constant velocity means Fnet = 0", "0 = Fg(parallel) + Ff + Fmotor",
      "-Fmotor = (5)(-9,8)sin30 + (-2)", "Fmotor = 24,245 N", "P = Fv = (24,245)(0,5) = 12,12 W"],
     "Equilibrium condition plus P = Fv; five marks.", True, True),

    # ---------------- QUESTION 5: MOMENTUM / IMPULSE (16) ----------------
    ("5.1", 2, "Mechanics-Momentum", "Definition/Explain",
     "State the principle of conservation of linear momentum in words. (cart A 0,25 kg at 2 m.s-1 right; "
     "cart B 0,5 kg at 5 m.s-1 left; perfectly elastic collision lasting 0,05 s)",
     False, [], "the total linear momentum of an isolated system remains constant (is conserved)",
     ["total linear momentum", "of an isolated system remains constant"], "Two-part statement.", False, False),
    ("5.2", 6, "Mechanics-Momentum", "Calculation",
     "By applying the principles of conservation of both momentum and kinetic energy, calculate the final "
     "velocity (magnitude and direction) of both carts immediately after the collision.",
     False, ["sum p before = sum p after", "sum Ek before = sum Ek after"],
     "Cart A: 7,33 m.s-1 to the left; Cart B: 0,33 m.s-1 to the left",
     ["momentum: (0,25)(+2) + (0,5)(-5) = 0,25 vAf + 0,5 vBf -> -2 = 0,25 vAf + 0,5 vBf",
      "kinetic energy (or relative velocity): 8,75 = 0,125 vAf^2 + 0,25 vBf^2",
      "relative-velocity shortcut: vAi - vBi = vBf - vAf -> 7 = vBf - vAf",
      "substitute and solve: vAf = -7,33 m.s-1; vBf = -0,33 m.s-1"],
     "Six marks; direction must be stated with each magnitude. Memo shows both the energy route and the "
     "relative-velocity shortcut.", False, True),
    ("5.3", 1, "Mechanics-Momentum", "Short Answer",
     "Explain which cart, if either, experiences the greater force during the collision.",
     False, [], "they experience an equal magnitude of force (Newton's third law)",
     ["equal magnitude of force", "Newton III"],
     "Paper allocates 1 mark; the memo shows 2 ticks against this answer - allocation mismatch logged.", False, False),
    ("5.4", 2, "Mechanics-Momentum", "Definition/Explain",
     "Define impulse.",
     False, [], "the product of force and contact time", ["product of force and contact time (2)"],
     "Two marks for the definition.", False, False),
    ("5.5", 3, "Mechanics-Momentum", "Calculation",
     "Consider cart A moving after the collision. Calculate the magnitude of the force that acted on it "
     "during the collision, if the collision took 20 milliseconds.",
     False, ["dp = F dt"], "116,63 N",
     ["m(vf - vi) = F dt", "0,25(-7,33 - 2) = F(0,02)", "-2,3325 = 0,02F", "F = -116,63 N"],
     "Time must be converted from milliseconds; the stem gives 0,05 s elsewhere in the question.", False, True),
    ("5.6", 2, "Mechanics-Momentum", "Experiment/Investigation",
     "The magnetic collision attachments were used to improve the results. Why would magnetic attachments be "
     "used rather than rubber bumpers or springs?",
     False, [],
     "they allow the trolleys to interact without physical contact, so there is minimal deformation, "
     "friction, sound or heat loss, making the collision closer to perfectly elastic",
     ["interact without physical contact (1)", "minimal deformation/friction/sound/heat loss (1)",
      "collision closer to perfectly elastic (1)"],
     "Paper allocates 2 marks; the memo shows 3 ticks - allocation mismatch logged.", False, False),

    # ---------------- QUESTION 6: GRAVITATION GRAPH + ELECTROSTATICS (17) ----------------
    ("6.1.1", 2, "Mechanics-Gravitation", "Definition/Explain",
     "An astronaut determines the weight of several masses. Define gravitational field.",
     False, [], "the force acting per unit mass", ["force acting per unit mass (2)"], "Two-mark definition.", False, False),
    ("6.1.2", 4, "Mechanics-Gravitation", "Data/Graph Interpretation",
     "Plot a graph of weight (y-axis) vs mass (x-axis) on the graph paper provided. No heading is necessary "
     "and the x-axis has been labelled.",
     True, [], "straight line through the origin",
     ["y-axis label and scale (1)", "5 points correctly plotted (2)", "line of best fit (1)"],
     "Memo note: 'check 0,2 & 0,6' - two specific points flagged as commonly misplotted. The paper says no "
     "heading is needed, unlike the 2021 and 2019 graph items.", True, False),
    ("6.1.3", 4, "Mechanics-Gravitation", "Calculation",
     "Determine the gradient of the graph and its unit, then refer to Table A (Venus 8,87; Mars 3,71; "
     "Jupiter 23,12; Pluto 0,58) to determine which planet the astronaut was on.",
     True, ["gradient = dy/dx"], "gradient approximately 3,7 N.kg-1; the planet is Mars",
     ["gradient = dy/dx using values read from the candidate's graph", "gradient approximately 3,7 N.kg-1 "
      "(plus or minus 10% tolerance)", "planet identified as Mars"],
     "The memo splits this into 6.1.3 (3), 6.1.4 (2: gradient equals Fg/m so it represents g) and 6.1.5 "
     "(1: Mars), i.e. 6 marks against the paper's 4 - allocation mismatch logged. Memo note: "
     "'show your calculations'.", True, True),
    ("6.2.1", 1, "Electrostatics", "Short Answer",
     "Three point charges lie on a straight line: Q1-Q2 = 1,5 m, Q2-Q3 = 1,0 m; Q1 is positive, "
     "Q3 = +2 microC and Q3 experiences a net electrostatic force of 0,3 N to the left (towards Q1). Is the "
     "sign of charge Q2 positive or negative? Circle POSITIVE or NEGATIVE.",
     True, [], "Positive",
     ["positive"],
     "Single-mark choice. NOTE: the memo's 6.2.2 reasoning concludes Q2 must be NEGATIVE, contradicting the "
     "6.2.1 answer of 'Positive' - contradiction logged.", True, False),
    ("6.2.2", 2, "Electrostatics", "Definition/Explain",
     "Explain your reasoning for Question 6.2.1.",
     True, [],
     "Q3 experiences a net force to the left; since Q1 is positive the force from Q1 on Q3 is repulsive (to "
     "the right), so Q2 must exert a stronger attractive force to the left; for Q2 to attract Q3, Q2 must be "
     "negative",
     ["force from Q1 on Q3 is repulsive/to the right (1)", "Q2 must attract Q3, therefore Q2 is negative (1)"],
     "Memo offers three alternative accepted reasonings, all concluding Q2 is negative.", True, False),
    ("6.2.3", 4, "Electrostatics", "Calculation",
     "Charge Q2 is now removed; the electrostatic force on Q3 due to Q1 is now 0,012 N. Calculate the "
     "magnitude of the unknown charge Q1.",
     True, ["F = kQ1Q2/r2"], "4,16 x 10^-6 C",
     ["F = kQ1Q2/r2", "0,012 = (9 x 10^9)(2 x 10^-6)(Q1)/(1 + 1,5)^2", "Q1 = 4,16 x 10^-6 C"],
     "Requires adding the two separations to get the Q1-Q3 distance.", True, True),

    # ---------------- QUESTION 7: PHOTONS (5) ----------------
    ("7.1", 2, "Waves Sound Light", "Definition/Explain",
     "Laser A emits red light (650 nm, 5 mW) and laser B green light (530 nm, 5 mW). Explain why, at equal "
     "power, the green laser is more dangerous to the human eye.",
     False, ["c = f lambda"],
     "the green light has a higher frequency and hence carries more energy per photon, as wavelength is "
     "inversely proportional to frequency",
     ["higher frequency so more energy (1)", "wavelength inversely proportional to frequency (1)"],
     "Two-mark qualitative reasoning item.", False, False),
    ("7.2", 3, "Waves Sound Light", "Calculation",
     "Determine the energy transferred by a single wave in the green laser beam; give the answer in "
     "electron volts.",
     False, ["E = hc/lambda"], "2,33 eV",
     ["E = hc/lambda = (6,6 x 10^-34)(3 x 10^8)/(530 x 10^-9)", "E = 3,735 x 10^-19 J",
      "E(eV) = 3,735 x 10^-19 / 1,6 x 10^-19 = 2,33 eV"],
     "Unit conversion to eV is required for the final mark. Same item type as 2023 Q10.3.", False, False),

    # ---------------- QUESTION 8: PARALLEL CIRCUIT WITH INTERNAL RESISTANCE (7) ----------------
    ("8.1", 2, "Electric Circuits", "Calculation",
     "Three bulbs A, B, C (4 W, 6 W, 10 W) are connected in parallel to a 12 V source with significant "
     "internal resistance; all are at maximum brightness and the voltmeter over the battery reads 12 V. "
     "Calculate the resistance of the 4 W bulb.",
     True, ["P = V2/R"], "36 ohm", ["P = V2/R", "4 = 12^2/R", "R = 36 ohm"],
     "Paper allocates 2 marks; the memo shows (3) - allocation mismatch logged.", True, False),
    ("8.2", 1, "Electric Circuits", "Short Answer",
     "How will the equivalent resistance of the circuit change if the 6 W bulb burns out? Circle INCREASES, "
     "DECREASES or NO CHANGE.",
     True, [], "INCREASE", ["increase (1)"], "Single-mark qualitative prediction.", True, False),
    ("8.3", 4, "Electric Circuits", "Definition/Explain",
     "How will the power dissipated by the 10 W bulb change if the 6 W bulb burns out? Give a reason.",
     True, ["Vemf = I(Rext + r)"], "INCREASE",
     ["increase (1)", "total current decreases because total resistance increases (1)",
      "less voltage lost across the internal resistor, Vinternal = Ir (1)",
      "so the external voltage over the 10 W bulb increases, Vemf = Vinternal + Vexternal (1)"],
     "Four-step causal chain including internal resistance; paper allocates 4 marks, memo shows (3) - "
     "allocation mismatch logged.", True, False),

    # ---------------- QUESTION 9: EMF AND INTERNAL RESISTANCE (16) ----------------
    ("9.1", 2, "Electric Circuits", "Definition/Explain",
     "The three external resistors are ohmic conductors. Explain the meaning of the term ohmic conductor. "
     "(battery of unknown emf with internal resistance 0,5 ohm; 4 ohm and 8 ohm resistors plus unknown R)",
     True, [],
     "a component for which the current through it is directly proportional to the potential difference "
     "across it provided the temperature remains constant; it obeys Ohm's Law and has constant resistance",
     ["current directly proportional to potential difference (1)", "provided temperature remains constant (1)"],
     "Same two required elements as the Ohm's Law definition in 2023 Q8.1.", True, False),
    ("9.2", 3, "Electric Circuits", "Calculation",
     "When switch S is OPEN, voltmeter V1 reads 3,2 V. Calculate the current through the battery.",
     True, ["V = IR"], "0,8 A", ["V = IR", "3,2 = I(4)", "I = 0,8 A"],
     "Requires identifying which resistor V1 is across from the circuit diagram.", True, False),
    ("9.3", 4, "Electric Circuits", "Calculation",
     "Calculate the emf of the battery.",
     True, ["emf = I(Rext + r)"], "10 V", ["emf = I(Rext + r)", "emf = 0,8(12 + 0,5)", "emf = 10 V"],
     "External resistance must be combined before applying the emf equation.", True, False),
    ("9.4", 5, "Electric Circuits", "Calculation",
     "When switch S is CLOSED, voltmeter V2 reads 8,8 V. Calculate the resistance of resistor R.",
     True, ["emf = Vext + Vint", "1/Rp = 1/R1 + 1/R2"], "5,28 ohm",
     ["emf = Vext + Vint -> 10 = 8,8 + I(0,5) -> I = 2,4 A",
      "Rext = V/I = 8,8/2,4 = 3,666 ohm", "1/3,666 = 1/12 + 1/R", "R = 5,28 ohm"],
     "Three-stage calculation; five marks.", True, False),
    ("9.5", 2, "Electric Circuits", "Definition/Explain",
     "The battery becomes heated when voltmeter V1 is replaced by a connecting wire. Explain this "
     "observation.",
     True, [],
     "the internal resistance consumes more power due to the greater current and so converts electrical "
     "energy into thermal energy",
     ["greater current through the internal resistance (1)", "electrical energy converted to thermal energy (1)"],
     "Short-circuit reasoning; two marks.", True, False),
]
