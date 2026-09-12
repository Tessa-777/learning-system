"""Question-level evidence transcribed from the paper and its verified marking guidelines.

Do not silently correct source errors. LOCATORS retains source pages and shared context.
"""

PAPER = {'paper_key': 'BIO-2023-NOV',
 'paper_path': 'data/organized/biology/November exam paper 1.pdf',
 'memo_path': 'data/organized/biology/November exam paper 1 MG.pdf',
 'year': 2023,
 'exam_date': '24 NOVEMBER 2023',
 'exam_period': 'november',
 'paper_type': 'paper1',
 'exam_board': 'internal',
 'total_marks': 200,
 'question_totals': [80, 40, 40, 40],
 'examiner': 'MRS S. STEGMANN',
 'moderator': 'MRS B. ZAJAC',
 'duration_stated': '3 HOURS',
 'fidelity_rung': 'A',
 'notes': 'Read directly from digital PDF text. Whitespace normalized, blank answer lines and repeating headers '
          'omitted. Lettered subparts retain source letters; rowN identifies an unnumbered matching row. '
          'Image-dependent evidence is unresolved, not reconstructed.',
 'alignment_anchors': {'memo': '20 snails caught in the first sample',
                       'paper': 'Ashleigh catches lady bugs at random'}}

SCHEMA = ('qn',
 'marks',
 'topic',
 'qtype',
 'text',
 'has_diagram',
 'formulae',
 'memo_answer',
 'memo_steps',
 'memo_notes',
 'needs_visual',
 'ocr_uncertain')

RECORDS = [('1.1.row1',
  1,
  'Population ecology',
  'Definition/Terminology',
  'An indication of the variety of living things found in an environment.',
  False,
  [],
  'F ✓',
  ['F'],
  'F ✓',
  False,
  False),
 ('1.1.row10',
  1,
  'Population ecology',
  'Definition/Terminology',
  'The number of individuals an area can sustain.',
  False,
  [],
  'B ✓',
  ['B'],
  'B ✓',
  False,
  False),
 ('1.1.row2',
  1,
  'Population ecology',
  'Definition/Terminology',
  'Process of gradual change of an ecological community over time.',
  False,
  [],
  'A ✓',
  ['A'],
  'A ✓',
  False,
  False),
 ('1.1.row3',
  1,
  'Population ecology',
  'Definition/Terminology',
  'Linked food chains showing the energy flow in an ecosystem',
  False,
  [],
  'C ✓',
  ['C'],
  'C ✓',
  False,
  False),
 ('1.1.row4',
  1,
  'Population ecology',
  'Definition/Terminology',
  'A group of organisms occupying the same area that can breed freely with one another.',
  False,
  [],
  'J ✓',
  ['J'],
  'J ✓',
  False,
  False),
 ('1.1.row5',
  1,
  'Population ecology',
  'Definition/Terminology',
  'Organisms that hunt and kill their food.',
  False,
  [],
  'K ✓',
  ['K'],
  'K ✓',
  False,
  False),
 ('1.1.row6',
  1,
  'Population ecology',
  'Definition/Terminology',
  'Dividing vegetation into vertical layers.',
  False,
  [],
  'H ✓',
  ['H'],
  'H ✓',
  False,
  False),
 ('1.1.row7',
  1,
  'Population ecology',
  'Definition/Terminology',
  'Non-living components in the environment.',
  False,
  [],
  'E ✓',
  ['E'],
  'E ✓',
  False,
  False),
 ('1.1.row8',
  1,
  'Population ecology',
  'Definition/Terminology',
  'Area in which living and non-living things interact with each other.',
  False,
  [],
  'I ✓',
  ['I'],
  'I ✓',
  False,
  False),
 ('1.1.row9',
  1,
  'Population ecology',
  'Definition/Terminology',
  'Living components in the environment.',
  False,
  [],
  'D ✓',
  ['D'],
  'D ✓',
  False,
  False),
 ('1.2.1',
  1,
  'Transport in animals',
  'Multiple Choice',
  'The pulmonary artery carries blood away from the (1) A. Right ventricle B. Right atrium C. Left ventricle D. '
  'Left atrium',
  False,
  [],
  'A ✓ (1)',
  ['A'],
  'A ✓ (1)',
  False,
  False),
 ('1.2.2',
  1,
  'Transport in animals',
  'Multiple Choice',
  'Blood Type A will NOT agglutinate when mixed with (1) A. Type B B. Type A C. Type O D. None of the above',
  False,
  [],
  'B ✓ (1)',
  ['B'],
  'B ✓ (1)',
  False,
  False),
 ('1.2.3',
  1,
  'Population ecology',
  'Multiple Choice',
  'The age-gender pyramid above is for a developed country since… (1) A. The number of newborns is high. B. There '
  'are more young people than old people. C. There are more females than males in each age group. D. The life '
  'expectancy of the population is high. Age-gender pyramid of a population (in millions) Female Male',
  True,
  [],
  'D ✓ (1)',
  ['D'],
  'D ✓ (1)',
  True,
  False),
 ('1.2.4',
  1,
  'Population ecology',
  'Multiple Choice',
  'Which ONE of the following can correctly be deduced from the pyramid shown above? (1) A. There are less than 2 '
  'million people between 0 and 10 years. B. There are more males than females in the age group 11 to 20 years. '
  'C. The birth and death rates are about the same. D. There are more females than males who are 50 years or '
  'older.',
  True,
  [],
  'D ✓ (1)',
  ['D'],
  'D ✓ (1)',
  True,
  False),
 ('1.2.5',
  1,
  'Population ecology',
  'Multiple Choice',
  'Living in a herd is of benefit to zebra as it: (1) A. Allows individuals to source more food. B. Reduces '
  'competition as some zebra eat grass whilst other zebra eat leaves. C. Allows the herd to avoid predators more '
  'easily. D. Reduces competition for mates.',
  False,
  [],
  'C ✓ (1)',
  ['C'],
  'C ✓ (1)',
  False,
  False),
 ('1.2.6',
  1,
  'Population ecology',
  'Multiple Choice',
  'Which of the following combinations of characteristics, (i) to (iv), are true of a social species such as '
  'termites? (1) (i) Individuals live in groups (ii) Individuals care for young that are not their own (iii) All '
  'individuals of the colony have the same body structure (iv) Not all individuals get to reproduce A. (i), (ii), '
  '(iii), (iv) B. (i), (iii) C. (i), (ii), (iv) D. (ii), (iii)',
  False,
  [],
  'C ✓ (1)',
  ['C'],
  'C ✓ (1)',
  False,
  False),
 ('1.2.7',
  1,
  'Population ecology',
  'Multiple Choice',
  'Certain plants attract pollinators by generating heat at different times of the day. Different plant species '
  'heat up at different time of the day. This concept can be best described as: (1) A. A density independent '
  'factor B. Resource partitioning C. Asexual reproduction D. Predation',
  False,
  [],
  'B ✓ (1)',
  ['B'],
  'B ✓ (1)',
  False,
  False),
 ('1.2.8',
  1,
  'Population ecology',
  'Multiple Choice',
  'Which of the following would NOT be classified as a density independent factor in decreasing population '
  'numbers? (1) A. Pollution from a surrounding factory B. Oil spill in the ocean C. Food availability D. '
  'Hurricane',
  False,
  [],
  'C ✓ (1)',
  ['C'],
  'C ✓ (1)',
  False,
  False),
 ('1.2.9',
  2,
  'Transport in animals',
  'Multiple Choice',
  'A diagram of a human red blood cell is shown. The length of line XY on the diagram is 40mm. The actual width '
  'of the cell is 0.008mm. What is the magnification of the diagram? (2) A. x500 B. x5 000 C. x50 000 D. x 500 '
  '000',
  True,
  [],
  'B ✓✓ (2)',
  ['B'],
  'B ✓✓ (2)',
  True,
  False),
 ('1.3.1',
  1,
  'Transport in animals',
  'Multiple Choice',
  'Heart muscle supplied with oxygen and nutrients A. Pulmonary artery B. Coronary artery',
  False,
  [],
  'B ONLY ✓',
  ['B ONLY'],
  'B ONLY ✓',
  False,
  False),
 ('1.3.2',
  1,
  'Transport in animals',
  'Multiple Choice',
  'Capillaries A. Microscopic B. Easy diffusion of metabolites in and out of cells',
  False,
  [],
  'BOTH ✓',
  ['BOTH'],
  'BOTH ✓',
  False,
  False),
 ('1.3.3',
  1,
  'Transport in animals',
  'Multiple Choice',
  'Oxygenated blood A. All arteries B. Venules',
  False,
  [],
  'NONE ✓',
  ['NONE'],
  'NONE ✓',
  False,
  False),
 ('1.3.4',
  1,
  'Transport in animals',
  'Multiple Choice',
  'Systolic blood pressure A. Atria are contracted B. Ventricles are relaxed',
  False,
  [],
  'NONE ✓',
  ['NONE'],
  'NONE ✓',
  False,
  False),
 ('1.3.5',
  1,
  'Transport in animals',
  'Multiple Choice',
  'Smooth muscle layer of blood vessels A. Vasoconstriction B. Vasodilation',
  False,
  [],
  'BOTH ✓',
  ['BOTH'],
  'BOTH ✓',
  False,
  False),
 ('1.4.1',
  2,
  'Transport in animals',
  'Short Answer',
  'Why do the heart rates of both learners increase after jogging on the spot for one minute? (2)',
  False,
  [],
  'More oxygen ✓ is needed to be pumped around the body for increased respiration ✓ and the increase CO2 needs to '
  'be brought to the lungs for exhalation faster. ✓ (any 2)',
  ['More oxygen',
   'is needed to be pumped around the body for increased respiration',
   'and the increase CO2 needs to be brought to the lungs for exhalation faster.',
   '(any 2)'],
  'More oxygen ✓ is needed to be pumped around the body for increased respiration ✓ and the increase CO2 needs to '
  'be brought to the lungs for exhalation faster. ✓ (any 2)',
  False,
  False),
 ('1.4.2',
  1,
  'Transport in animals',
  'Short Answer',
  'Which learner would you classify as the fittest? (1)',
  False,
  [],
  'Learner A ✓ (1)',
  ['Learner A'],
  'Learner A ✓ (1)',
  False,
  False),
 ('1.4.3',
  1,
  'Transport in animals',
  'Short Answer',
  'Give a reason for your answer to QUESTION 1.4.2. (1)',
  False,
  [],
  'Their resting heart rate is lower OR their heart rate returns to resting HR quicker than B ✓ (1)',
  ['Their resting heart rate is lower OR their heart rate returns to resting HR quicker than B'],
  'Their resting heart rate is lower OR their heart rate returns to resting HR quicker than B ✓ (1)',
  False,
  False),
 ('1.4.4',
  1,
  'Transport in animals',
  'Short Answer',
  'How long did it take for Learner A’s heart rate to return to normal after running? (1)',
  False,
  [],
  '4 minutes ✓ (1)',
  ['4 minutes'],
  '4 minutes ✓ (1)',
  False,
  False),
 ('1.4.5',
  1,
  'Transport in animals',
  'Short Answer',
  'Name the dependent variable of this investigation. (1)',
  False,
  [],
  'Heart rate (bpm) ✓ (1)',
  ['Heart rate (bpm)'],
  'Heart rate (bpm) ✓ (1)',
  False,
  False),
 ('1.4.6',
  2,
  'Transport in animals',
  'Short Answer',
  'Name TWO controlled variables in this investigation. (2)',
  False,
  [],
  'same gender (female) Same age of learners ✓ Same apparatus to measure HR ✓✓ (any 2)',
  ['same gender (female) Same age of learners', 'Same apparatus to measure HR', '(any 2)'],
  'same gender (female) Same age of learners ✓ Same apparatus to measure HR ✓✓ (any 2)',
  False,
  False),
 ('1.4.7',
  7,
  'Transport in animals',
  'Data/Graph Interpretation',
  'On the grid below draw a double line graph illustrating the results of both learners’ heart rate for the five '
  'minutes after their last activity. (7)',
  True,
  [],
  'Heading (H)- all variables ✓ X-axis (X)- title + unit ✓and scale ✓ (time) Y-axis (Y)- title + unit ✓ and scale '
  '✓ (HR) Key (K) ✓ Plotting (P) ✓ (7)',
  ['Heading (H)- all variables',
   'X-axis (X)- title + unit',
   'and scale',
   '(time) Y-axis (Y)- title + unit',
   'and scale',
   '(HR) Key (K)',
   'Plotting (P)'],
  'Heading (H)- all variables ✓ X-axis (X)- title + unit ✓and scale ✓ (time) Y-axis (Y)- title + unit ✓ and scale '
  '✓ (HR) Key (K) ✓ Plotting (P) ✓ (7)',
  True,
  False),
 ('1.5.1',
  1,
  'Transport in animals',
  'Short Answer',
  'Which person do you think suffers from coronary artery disease? (1)',
  False,
  [],
  'B ✓ (1)',
  ['B'],
  'B ✓ (1)',
  False,
  False),
 ('1.5.2',
  2,
  'Transport in animals',
  'Short Answer',
  'Give a reason for your answer to QUESTION 1.5.1. (2)',
  False,
  [],
  'Blood flow is lowered✓ due to the narrowing of the lumen ✓ (2)',
  ['Blood flow is lowered', 'due to the narrowing of the lumen'],
  'Blood flow is lowered✓ due to the narrowing of the lumen ✓ (2)',
  False,
  False),
 ('1.5.3',
  1,
  'Transport in animals',
  'Short Answer',
  'What substance causes blockages inside arteries such as coronary arteries? (1)',
  False,
  [],
  'Cholesterol ✓ (1)',
  ['Cholesterol'],
  'Cholesterol ✓ (1)',
  False,
  False),
 ('1.5.4',
  1,
  'Transport in animals',
  'Short Answer',
  'What could a person do to decrease the substance mentioned in QUESTION 1.5.3. in their diet? (1)',
  False,
  [],
  'Lowered the intake of animal fat in one’s diet Increase HDLs in one’s diet ✓ (any 1)',
  ['Lowered the intake of animal fat in one’s diet Increase HDLs in one’s diet', '(any 1)'],
  'Lowered the intake of animal fat in one’s diet Increase HDLs in one’s diet ✓ (any 1)',
  False,
  False),
 ('1.5.5',
  2,
  'Transport in animals',
  'Short Answer',
  'Calculate the difference in blood flow between person A and person B. (2)',
  False,
  [],
  '250-155 = 95✓ cm3/minute ✓ (2)',
  ['250-155 = 95', 'cm3/minute'],
  '250-155 = 95✓ cm3/minute ✓ (2)',
  False,
  False),
 ('1.5.6',
  2,
  'Transport in animals',
  'Short Answer',
  'Calculate the volume of blood flowing through the coronary arteries of person A in 1 hour. (2)',
  False,
  [],
  '250 x 60✓= 15 000 cm3/minute ✓(no unit no mark) (2)',
  ['250 x 60', '= 15 000 cm3/minute', '(no unit no mark) (2)'],
  '250 x 60✓= 15 000 cm3/minute ✓(no unit no mark) (2)',
  False,
  False),
 ('1.5.7.a',
  2,
  'Transport in animals',
  'Short Answer',
  'Give TWO advantages of using a stent instead of CABG. (2) 1- 2-',
  False,
  [],
  'Only a small cut/ incision is made in the skin No other vessels are used during this procedure Only 2-3 hours '
  'is spent in hospital after the procedure as opposed to 7 days Recovery time is 7 days as opposed to 12 weeks. '
  'The risk of a heart attack during the procedure is lower than CABG ✓✓ (any 2)',
  ['Only a small cut/ incision is made in the skin No other vessels are used during this procedure Only 2-3 hours '
   'is spent in hospital after the procedure as opposed to 7 days Recovery time is 7 days as opposed to 12 weeks. '
   'The risk of a heart attack during the procedure is lower than CABG',
   '(any 2)'],
  'Only a small cut/ incision is made in the skin No other vessels are used during this procedure Only 2-3 hours '
  'is spent in hospital after the procedure as opposed to 7 days Recovery time is 7 days as opposed to 12 weeks. '
  'The risk of a heart attack during the procedure is lower than CABG ✓✓ (any 2)',
  False,
  False),
 ('1.5.7.b',
  2,
  'Transport in animals',
  'Short Answer',
  'Give TWO advantages of using CABG instead of a stent. (2) 1- 2-',
  False,
  [],
  'The chance of failure within a year is substantially lower The patient is under general anesthetic (trauma and '
  'stress are lowered) Can be used when multiple blockages are present whereas a stent can only be used for a '
  'single blockage ✓✓ (any 2)',
  ['The chance of failure within a year is substantially lower The patient is under general anesthetic (trauma '
   'and stress are lowered) Can be used when multiple blockages are present whereas a stent can only be used for '
   'a single blockage',
   '(any 2)'],
  'The chance of failure within a year is substantially lower The patient is under general anesthetic (trauma and '
  'stress are lowered) Can be used when multiple blockages are present whereas a stent can only be used for a '
  'single blockage ✓✓ (any 2)',
  False,
  False),
 ('1.6.1',
  2,
  'Population ecology',
  'Definition/Terminology',
  'Define the term ‘population’. (2)',
  False,
  [],
  'A group of organisms of the same species ✓ that occupy the same are and can breed ✓ (2)',
  ['A group of organisms of the same species', 'that occupy the same are and can breed'],
  'A group of organisms of the same species ✓ that occupy the same are and can breed ✓ (2)',
  False,
  False),
 ('1.6.2',
  1,
  'Population ecology',
  'Labelling/Diagram',
  'Name the independent variable in the above investigation. (1)',
  True,
  [],
  'Time/weeks ✓ OR species A and B ✓ (1)',
  ['Time/weeks', 'OR species A and B'],
  'Time/weeks ✓ OR species A and B ✓ (1)',
  True,
  False),
 ('1.6.3',
  2,
  'Population ecology',
  'Data/Graph Interpretation',
  'What is the difference in population numbers of species A and B after being in the same habitat for 4 weeks? '
  '(2)',
  True,
  [],
  '100-20 ✓= 80 more of Species A ✓ (2)',
  ['100-20', '= 80 more of Species A'],
  '100-20 ✓= 80 more of Species A ✓ (2)',
  True,
  False),
 ('1.6.4',
  1,
  'Population ecology',
  'Data/Graph Interpretation',
  'What principle is shown in graph C? (1)',
  True,
  [],
  'Competitive exclusion ✓ (1)',
  ['Competitive exclusion'],
  'Competitive exclusion ✓ (1)',
  True,
  False),
 ('1.6.5',
  4,
  'Population ecology',
  'Data/Graph Interpretation',
  'Describe the growth patterns of species A and B when separated compared to when they are together in the same '
  'habitat. (4)',
  True,
  [],
  'Separated: numbers increase greatly due to their being no competiton ✓ Together: both species grow in the '
  'first week ✓ as there is sufficient food but thereafter species A increases greatly while species B '
  'drastically decreases ✓due to being outcompeted by A when food is limited ✓ (4)',
  ['Separated: numbers increase greatly due to their being no competiton',
   'Together: both species grow in the first week',
   'as there is sufficient food but thereafter species A increases greatly while species B drastically decreases',
   'due to being outcompeted by A when food is limited'],
  'Separated: numbers increase greatly due to their being no competiton ✓ Together: both species grow in the '
  'first week ✓ as there is sufficient food but thereafter species A increases greatly while species B '
  'drastically decreases ✓due to being outcompeted by A when food is limited ✓ (4)',
  True,
  False),
 ('1.6.6.a',
  2,
  'Population ecology',
  'Short Answer',
  'Differentiate between a predator and a prey. (2)',
  False,
  [],
  'Predator: organism that hunts and kills its food ✓ Prey: organism eaten by another (predator) ✓ (2)',
  ['Predator: organism that hunts and kills its food', 'Prey: organism eaten by another (predator)'],
  'Predator: organism that hunts and kills its food ✓ Prey: organism eaten by another (predator) ✓ (2)',
  False,
  False),
 ('1.6.6.b',
  5,
  'Population ecology',
  'Data/Graph Interpretation',
  'On the set of axis below sketch the relationship between species A and it’s predator over an extended period. '
  '(5)',
  True,
  [],
  'Heading (H) ✓ Axes headings (time on X-axis, species number on Y-axis) (A) ✓ Prey numbers always higher than '
  'predator (N) ✓ Cyclic change in predator always slightly after prey (C) ✓ Key (K) ✓ (5)',
  ['Heading (H)',
   'Axes headings (time on X-axis, species number on Y-axis) (A)',
   'Prey numbers always higher than predator (N)',
   'Cyclic change in predator always slightly after prey (C)',
   'Key (K)'],
  'Heading (H) ✓ Axes headings (time on X-axis, species number on Y-axis) (A) ✓ Prey numbers always higher than '
  'predator (N) ✓ Cyclic change in predator always slightly after prey (C) ✓ Key (K) ✓ (5)',
  True,
  False),
 ('1.7',
  8,
  'Skeletal system',
  'Data/Graph Interpretation',
  'Draw a line from the bones in the middle to the correct type of bone (left) and the location of it in the body '
  '(right). Type of bone Location in the body',
  True,
  [],
  'unresolved — matching connections to pictured bones are not readable in the text layer; 8 marks printed.',
  [],
  'unresolved — matching connections to pictured bones are not readable in the text layer; 8 marks printed.',
  True,
  False),
 ('1.8',
  2,
  'Skeletal system',
  'Short Answer',
  'Name TWO types of skeletons other than that of a human. 1- 2-',
  False,
  [],
  'Hydrostatic ✓ Exoskeleton ✓',
  ['Hydrostatic', 'Exoskeleton'],
  'Hydrostatic ✓ Exoskeleton ✓',
  False,
  False),
 ('2.1.1',
  2,
  'Skeletal system',
  'Short Answer',
  'List TWO functions of the skeleton. (2) 1- 2-',
  False,
  [],
  'Movement in correlation with muscles Protection of internal organs Storage of minerals Support and structure '
  'Production of blood cells ✓✓ (any 2)',
  ['Movement in correlation with muscles Protection of internal organs Storage of minerals Support and structure '
   'Production of blood cells',
   '(any 2)'],
  'Movement in correlation with muscles Protection of internal organs Storage of minerals Support and structure '
  'Production of blood cells ✓✓ (any 2)',
  False,
  False),
 ('2.1.2',
  1,
  'Skeletal system',
  'Data/Graph Interpretation',
  'What girdle is shown above? (1)',
  True,
  [],
  'Pectoral ✓ (1)',
  ['Pectoral'],
  'Pectoral ✓ (1)',
  True,
  False),
 ('2.1.3',
  2,
  'Skeletal system',
  'Data/Graph Interpretation',
  'Give the LETTERS of the bones that make up the girdle mentioned in 2.1.2. (2) H',
  True,
  [],
  'A ✓ and B ✓ (2)',
  ['A', 'and B'],
  'A ✓ and B ✓ (2)',
  True,
  False),
 ('2.1.4',
  5,
  'Skeletal system',
  'Labelling/Diagram',
  'Synovial joints are freely moveable joints that assist with movement. Draw and label a diagram of a typical '
  'synovial joint in the space below. (5)',
  True,
  [],
  'Heading ✓ Correct diagram/ accuracy ✓ Any 3 labels ✓✓✓ (5)',
  ['Heading', 'Correct diagram/ accuracy', 'Any 3 labels'],
  'Heading ✓ Correct diagram/ accuracy ✓ Any 3 labels ✓✓✓ (5)',
  True,
  False),
 ('2.1.5',
  1,
  'Skeletal system',
  'Data/Graph Interpretation',
  'Give the LETTER of a synovial joint in the diagram on the previous page. (1)',
  True,
  [],
  'H ✓ (1)',
  ['H'],
  'H ✓ (1)',
  True,
  False),
 ('2.1.6',
  2,
  'Skeletal system',
  'Labelling/Diagram',
  'Name the type of synovial joint AND the movement it allows mentioned in 2.1.5. (2)',
  True,
  [],
  'Ball and socket joint ✓- allows for rotation and movement in many directions ✓ (2)',
  ['Ball and socket joint', '- allows for rotation and movement in many directions'],
  'Ball and socket joint ✓- allows for rotation and movement in many directions ✓ (2)',
  True,
  False),
 ('2.1.7',
  4,
  'Skeletal system',
  'Labelling/Diagram',
  'Give the names of bones B, D, E and G. (4) B- D- E- G-',
  True,
  [],
  'B- scapula ✓ D- radius ✓ E- ulna ✓ G- metacarpals ✓ (4)',
  ['B- scapula', 'D- radius', 'E- ulna', 'G- metacarpals'],
  'B- scapula ✓ D- radius ✓ E- ulna ✓ G- metacarpals ✓ (4)',
  True,
  False),
 ('2.1.8',
  2,
  'Skeletal system',
  'Definition/Terminology',
  'C is an example of a long bone. It contains both red and yellow bone marrow. What is the function of red '
  'marrow? (2)',
  False,
  [],
  'Produces red blood cells ✓ and white blood cells ✓ (2)',
  ['Produces red blood cells', 'and white blood cells'],
  'Produces red blood cells ✓ and white blood cells ✓ (2)',
  False,
  False),
 ('2.2.1',
  1,
  'Skeletal system',
  'Definition/Terminology',
  'What is arthritis? (1)',
  False,
  [],
  'Inflammation of the joints ✓ (1)',
  ['Inflammation of the joints'],
  'Inflammation of the joints ✓ (1)',
  False,
  False),
 ('2.2.2',
  2,
  'Skeletal system',
  'Definition/Terminology',
  'What is a joint? (2)',
  False,
  [],
  'A region where two or more ✓ bones meet ✓ (2)',
  ['A region where two or more', 'bones meet'],
  'A region where two or more ✓ bones meet ✓ (2)',
  False,
  False),
 ('2.2.3',
  1,
  'Skeletal system',
  'Short Answer',
  'Name the connective tissue that joins the bones at a joint. (1)',
  False,
  [],
  'Ligament ✓ (1)',
  ['Ligament'],
  'Ligament ✓ (1)',
  False,
  False),
 ('2.2.4',
  2,
  'Skeletal system',
  'Short Answer',
  'Give TWO characteristics of the tissue in 2.2.3. (2) 1- 2-',
  False,
  [],
  'Contains collagen ✓ and elastic fibres ✓ Strong and resilient ✓ Flexible ✓ (any 2)',
  ['Contains collagen', 'and elastic fibres', 'Strong and resilient', 'Flexible', '(any 2)'],
  'Contains collagen ✓ and elastic fibres ✓ Strong and resilient ✓ Flexible ✓ (any 2)',
  False,
  False),
 ('2.2.5',
  3,
  'Skeletal system',
  'Short Answer',
  'Describe the condition of the joint if a person has osteoarthritis. (3)',
  False,
  [],
  'Articular cartilage ✓ of joint wears away ✓ Bones of joint grind against each other ✓ Small outgrowths of bone '
  'are produced ✓ (any 3)',
  ['Articular cartilage',
   'of joint wears away',
   'Bones of joint grind against each other',
   'Small outgrowths of bone are produced',
   '(any 3)'],
  'Articular cartilage ✓ of joint wears away ✓ Bones of joint grind against each other ✓ Small outgrowths of bone '
  'are produced ✓ (any 3)',
  False,
  False),
 ('2.2.6',
  2,
  'Skeletal system',
  'Short Answer',
  'Suggest ONE reason why osteoarthritis is more common in middle-aged people. (2)',
  False,
  [],
  'More years of wear and tear✓ on the cartilage due to physical activity or past injuries ✓ (2)',
  ['More years of wear and tear', 'on the cartilage due to physical activity or past injuries'],
  'More years of wear and tear✓ on the cartilage due to physical activity or past injuries ✓ (2)',
  False,
  False),
 ('2.3.1',
  1,
  'Skeletal system',
  'Short Answer',
  'Name the disease in which bones bend due to poor bone formation in children. (1)',
  False,
  [],
  'Rickets ✓ (1)',
  ['Rickets'],
  'Rickets ✓ (1)',
  False,
  False),
 ('2.3.2',
  1,
  'Skeletal system',
  'Short Answer',
  'What vitamin is deficient in the above disease? (1)',
  False,
  [],
  'Vitamin D ✓ (1)',
  ['Vitamin D'],
  'Vitamin D ✓ (1)',
  False,
  False),
 ('2.3.3',
  2,
  'Skeletal system',
  'Data/Graph Interpretation',
  'When is the peak bone density formed in men and women? (2)',
  True,
  [],
  'Accept between 24-27 years ✓✓ (2)',
  ['Accept between 24-27 years'],
  'Accept between 24-27 years ✓✓ (2)',
  True,
  False),
 ('2.3.4',
  2,
  'Skeletal system',
  'Data/Graph Interpretation',
  'Give a heading for the graph above. (2)',
  True,
  [],
  'A graph showing the relationship between bone mass and age✓ of both men and women✓ (2)',
  ['A graph showing the relationship between bone mass and age', 'of both men and women'],
  'A graph showing the relationship between bone mass and age✓ of both men and women✓ (2)',
  True,
  False),
 ('2.3.5',
  4,
  'Skeletal system',
  'Data/Graph Interpretation',
  'Provide TWO conclusions from the graph above. (4) 1- 2-',
  True,
  [],
  'Men have higher bone mass then women Women’s bone mass/ density decreases more than males after the age of 40. '
  'Men and women experience a peak in bone mass at the same age ✓✓✓✓ (any 2 x 2=4)',
  ['Men have higher bone mass then women Women’s bone mass/ density decreases more than males after the age of '
   '40. Men and women experience a peak in bone mass at the same age',
   '(any 2 x 2=4)'],
  'Men have higher bone mass then women Women’s bone mass/ density decreases more than males after the age of 40. '
  'Men and women experience a peak in bone mass at the same age ✓✓✓✓ (any 2 x 2=4)',
  True,
  False),
 ('3.1.1',
  2,
  'Transport in animals',
  'Labelling/Diagram',
  'Provide labels for A and C. (2) A- C-',
  True,
  [],
  'A- right atrium✓ C- Left ventricle ✓ (2)',
  ['A- right atrium', 'C- Left ventricle'],
  'A- right atrium✓ C- Left ventricle ✓ (2)',
  True,
  False),
 ('3.1.2.a',
  1,
  'Transport in animals',
  'Data/Graph Interpretation',
  'Valve between chamber C and B.',
  True,
  [],
  'Closed ✓',
  ['Closed'],
  'Closed ✓',
  True,
  False),
 ('3.1.2.b',
  1,
  'Transport in animals',
  'Data/Graph Interpretation',
  'Valve between chamber C and vessel Y.',
  True,
  [],
  'Open ✓ (2)',
  ['Open'],
  'Open ✓ (2)',
  True,
  False),
 ('3.1.3.a',
  2,
  'Transport in animals',
  'Data/Graph Interpretation',
  'A large amount of elastic tissue in blood vessel Y. (2)',
  True,
  [],
  'Blood pressure is high and elastic tissue can recoil✓ to even out the pressure ✓ (2)',
  ['Blood pressure is high and elastic tissue can recoil', 'to even out the pressure'],
  'Blood pressure is high and elastic tissue can recoil✓ to even out the pressure ✓ (2)',
  True,
  False),
 ('3.1.3.b',
  1,
  'Transport in animals',
  'Data/Graph Interpretation',
  'Valves in blood vessels such as blood vessel X. (1)',
  True,
  [],
  'Allows one way flow of blood/ prevents the backflow of blood ✓ (1)',
  ['Allows one way flow of blood/ prevents the backflow of blood'],
  'Allows one way flow of blood/ prevents the backflow of blood ✓ (1)',
  True,
  False),
 ('3.1.4',
  2,
  'Transport in animals',
  'Labelling/Diagram',
  'On the diagram on the previous page label the pulmonary artery and a pulmonary vein. (2)',
  True,
  [],
  'pulmonary artery and a pulmonary vein labelled on diagram ✓✓ (2)',
  ['pulmonary artery and a pulmonary vein labelled on diagram'],
  'pulmonary artery and a pulmonary vein labelled on diagram ✓✓ (2)',
  True,
  False),
 ('3.1.5',
  5,
  'Transport in animals',
  'Short Answer',
  'Tabulate TWO structural differences between arteries and veins. (5)',
  False,
  [],
  'Heading ✓ Any 2 differences x 2: - Arteries have a thicker muscular layer with more elastic fibres; veins have '
  'less elastic fibres and a thinner muscular layer ✓✓ - Arteries have a narrower, regular shaped lumen; veins '
  'have a large, irregular shaped lumen✓✓ - Arteries don’t contain valves; veins contain semilunar valves ✓✓ -1 '
  'Table not drawn/ drawn incorrectly (5)',
  ['Heading',
   'Any 2 differences x 2: - Arteries have a thicker muscular layer with more elastic fibres; veins have less '
   'elastic fibres and a thinner muscular layer',
   '- Arteries have a narrower, regular shaped lumen; veins have a large, irregular shaped lumen',
   '- Arteries don’t contain valves; veins contain semilunar valves',
   '-1 Table not drawn/ drawn incorrectly (5)'],
  'Heading ✓ Any 2 differences x 2: - Arteries have a thicker muscular layer with more elastic fibres; veins have '
  'less elastic fibres and a thinner muscular layer ✓✓ - Arteries have a narrower, regular shaped lumen; veins '
  'have a large, irregular shaped lumen✓✓ - Arteries don’t contain valves; veins contain semilunar valves ✓✓ -1 '
  'Table not drawn/ drawn incorrectly (5)',
  False,
  False),
 ('3.1.6',
  2,
  'Transport in animals',
  'Labelling/Diagram',
  'A pacemaker is a small, battery-powered device that prevents the heart from beating too slowly. You need '
  'surgery to get a pacemaker. The device is placed under the skin near the collarbone. On the diagram on the '
  'previous page label the heart’s natural pacemaker. (2)',
  True,
  [],
  'SA node ✓ labelled in correct place ✓ (2)',
  ['SA node', 'labelled in correct place'],
  'SA node ✓ labelled in correct place ✓ (2)',
  True,
  False),
 ('3.1.7.a',
  1,
  'Transport in animals',
  'Data/Graph Interpretation',
  'Why was vessel Y used to measure blood pressure? (1)',
  True,
  [],
  'It is the aorta✓ which is the artery in which BP is measured accurately (1)',
  ['It is the aorta', 'which is the artery in which BP is measured accurately (1)'],
  'It is the aorta✓ which is the artery in which BP is measured accurately (1)',
  True,
  False),
 ('3.1.7.b',
  2,
  'Transport in animals',
  'Data/Graph Interpretation',
  'Explain why the pressure moves up and down. (2)',
  True,
  [],
  'Pressure increase when heart is contracted (systole) ✓and decreases when its relaxed (diastole) ✓ (2)',
  ['Pressure increase when heart is contracted (systole)', 'and decreases when its relaxed (diastole)'],
  'Pressure increase when heart is contracted (systole) ✓and decreases when its relaxed (diastole) ✓ (2)',
  True,
  False),
 ('3.1.7.c',
  1,
  'Transport in animals',
  'Data/Graph Interpretation',
  'What factors might make the frequency of the heartbeat waves increase? (1)',
  True,
  [],
  'Increase activity Increased stress ✓ (any 1)',
  ['Increase activity Increased stress', '(any 1)'],
  'Increase activity Increased stress ✓ (any 1)',
  True,
  False),
 ('3.1.7.d',
  2,
  'Transport in animals',
  'Data/Graph Interpretation',
  'What is the blood pressure of the person whose heartbeat is recorded here? (2)',
  True,
  [],
  '105 (accept 103-107) ✓/ 68 (accept 66-70) ✓ (2)',
  ['105 (accept 103-107)', '/ 68 (accept 66-70)'],
  '105 (accept 103-107) ✓/ 68 (accept 66-70) ✓ (2)',
  True,
  False),
 ('3.2.1',
  2,
  'Transport in animals',
  'Short Answer',
  'Predict the values of X and Y in the table above. (2) X- Y-',
  False,
  [],
  'X- 110 or 109 ✓ Y- 144 ✓ (2)',
  ['X- 110 or 109', 'Y- 144'],
  'X- 110 or 109 ✓ Y- 144 ✓ (2)',
  False,
  False),
 ('3.2.2',
  1,
  'Transport in animals',
  'Definition/Terminology',
  'What is the independent variable in this investigation? (1)',
  False,
  [],
  'Age ✓ (1)',
  ['Age'],
  'Age ✓ (1)',
  False,
  False),
 ('3.2.3',
  2,
  'Transport in animals',
  'Short Answer',
  'Explain what ‘minimum heart rate for metabolising fat’ means. (2)',
  False,
  [],
  'The lowest one’s heart rate can be to break down fat stores OR the rate at which one’s heart should beat to '
  'burn fat ✓✓ (2)',
  ['The lowest one’s heart rate can be to break down fat stores OR the rate at which one’s heart should beat to '
   'burn fat'],
  'The lowest one’s heart rate can be to break down fat stores OR the rate at which one’s heart should beat to '
  'burn fat ✓✓ (2)',
  False,
  False),
 ('3.2.4',
  1,
  'Transport in animals',
  'Short Answer',
  'Mention one fixed variable in this investigation. (1)',
  False,
  [],
  'Same gender of cyclists Same number of cyclists in each age group ✓ (any 1)',
  ['Same gender of cyclists Same number of cyclists in each age group', '(any 1)'],
  'Same gender of cyclists Same number of cyclists in each age group ✓ (any 1)',
  False,
  False),
 ('3.2.5',
  2,
  'Transport in animals',
  'Short Answer',
  'What conclusion can be made from the results above? (2)',
  False,
  [],
  'As age increases ✓ they minimum heart rate for metabolising fat and improving fitness decreases ✓ (2)',
  ['As age increases', 'they minimum heart rate for metabolising fat and improving fitness decreases'],
  'As age increases ✓ they minimum heart rate for metabolising fat and improving fitness decreases ✓ (2)',
  False,
  False),
 ('3.3.1',
  2,
  'Transport in animals',
  'Short Answer',
  'Explain one structural adaptation of red blood cells that allows them to maximise their oxygen carrying '
  'capacity. (2)',
  False,
  [],
  'They are flexible allowing them to fit through narrow capillaries to deliver oxygen OR The biconcave shape '
  'increases surface area for oxygen transportation OR The lose their nucleus upon maturity to allow for more '
  'space to carry oxygen ✓✓ (any 1 x 2)',
  ['They are flexible allowing them to fit through narrow capillaries to deliver oxygen OR The biconcave shape '
   'increases surface area for oxygen transportation OR The lose their nucleus upon maturity to allow for more '
   'space to carry oxygen',
   '(any 1 x 2)'],
  'They are flexible allowing them to fit through narrow capillaries to deliver oxygen OR The biconcave shape '
  'increases surface area for oxygen transportation OR The lose their nucleus upon maturity to allow for more '
  'space to carry oxygen ✓✓ (any 1 x 2)',
  False,
  False),
 ('3.3.2',
  3,
  'Transport in animals',
  'Short Answer',
  'It is calculated that blood doping on average can increase performance by 12% based on a correlating number of '
  'red blood cells. If blood normally contains 250 000 000 cells, calculate how many red blood cells would be '
  'found on average in doped blood. Show all working. (3) It is well known that blood doping, by thickening the '
  'blood, leads to an increased risk of several deadly diseases such as heart disease (also known as coronary '
  'artery disease (CAD)) and stroke.',
  False,
  [],
  '250 000 000 x 12%✓ = 30 000 000 + 250 000 000 ✓= 280 000 000 cells ✓ (3)',
  ['250 000 000 x 12%', '= 30 000 000 + 250 000 000', '= 280 000 000 cells'],
  '250 000 000 x 12%✓ = 30 000 000 + 250 000 000 ✓= 280 000 000 cells ✓ (3)',
  False,
  False),
 ('3.3.3',
  1,
  'Transport in animals',
  'Data/Graph Interpretation',
  'On the diagram below mark with an X where a blockage would occur that could cause a major, and possibly fatal, '
  'heart attack. (1)',
  True,
  [],
  'X anywhere on the major vessels ✓ (1)',
  ['X anywhere on the major vessels'],
  'X anywhere on the major vessels ✓ (1)',
  True,
  False),
 ('3.3.4',
  2,
  'Transport in animals',
  'Short Answer',
  'Name TWO risk factors of CAD that can be controlled. (2)',
  False,
  [],
  'High BP/ smoking/ high blood cholesterol/ obesity/ type 2 diabetes/ environmental stress/ sedentary (inactive) '
  'lifestyle/ diet high in sugars and saturated fats/ diet low in fruit and vegetables ✓✓ (any 2)',
  ['High BP/ smoking/ high blood cholesterol/ obesity/ type 2 diabetes/ environmental stress/ sedentary '
   '(inactive) lifestyle/ diet high in sugars and saturated fats/ diet low in fruit and vegetables',
   '(any 2)'],
  'High BP/ smoking/ high blood cholesterol/ obesity/ type 2 diabetes/ environmental stress/ sedentary (inactive) '
  'lifestyle/ diet high in sugars and saturated fats/ diet low in fruit and vegetables ✓✓ (any 2)',
  False,
  False),
 ('3.3.5',
  1,
  'Transport in animals',
  'Short Answer',
  'Name ONE risk factor of CAD that cannot be controlled. (1)',
  False,
  [],
  'Age/ genetic predisposition/ being male/ having a high achieving personality ✓ (any 1)',
  ['Age/ genetic predisposition/ being male/ having a high achieving personality', '(any 1)'],
  'Age/ genetic predisposition/ being male/ having a high achieving personality ✓ (any 1)',
  False,
  False),
 ('3.3.6',
  1,
  'Transport in animals',
  'Short Answer',
  'Identify ONE symptom of a stroke. (1)',
  False,
  [],
  'Paralysis of the limbs on one side of the body/ difficulties with speech and/or swallowing/ unconsciousness/ '
  'visual field disturbances ✓ (any 1)',
  ['Paralysis of the limbs on one side of the body/ difficulties with speech and/or swallowing/ unconsciousness/ '
   'visual field disturbances',
   '(any 1)'],
  'Paralysis of the limbs on one side of the body/ difficulties with speech and/or swallowing/ unconsciousness/ '
  'visual field disturbances ✓ (any 1)',
  False,
  False),
 ('4.1.1',
  1,
  'Population ecology',
  'Labelling/Diagram',
  'Name the source of information required to plot the above graph. (1)',
  True,
  [],
  'Census ✓ (1)',
  ['Census'],
  'Census ✓ (1)',
  True,
  False),
 ('4.1.2',
  1,
  'Population ecology',
  'Data/Graph Interpretation',
  'Which population pyramid (A or B) shows an increasing population? (1)',
  True,
  [],
  'A ✓ (1)',
  ['A'],
  'A ✓ (1)',
  True,
  False),
 ('4.1.3',
  4,
  'Population ecology',
  'Data/Graph Interpretation',
  'Explain your answer to QUESTION 4.1.2. (4)',
  True,
  [],
  'The base of the age pyramid is wide but it narrows towards the top ✓ This indicates a high proportion of '
  'individuals in the younger age group. ✓ When they grow up and reproduce the population will increase in size. '
  '✓ The narrowing of the pyramid towards the top also indicates a high death rate with increasing age. ✓ (4)',
  ['The base of the age pyramid is wide but it narrows towards the top',
   'This indicates a high proportion of individuals in the younger age group.',
   'When they grow up and reproduce the population will increase in size.',
   'The narrowing of the pyramid towards the top also indicates a high death rate with increasing age.'],
  'The base of the age pyramid is wide but it narrows towards the top ✓ This indicates a high proportion of '
  'individuals in the younger age group. ✓ When they grow up and reproduce the population will increase in size. '
  '✓ The narrowing of the pyramid towards the top also indicates a high death rate with increasing age. ✓ (4)',
  True,
  False),
 ('4.1.4',
  3,
  'Population ecology',
  'Data/Graph Interpretation',
  'Describe the trend of population growth in Graph B. (3)',
  True,
  [],
  'The population size at each age group remains almost equal. ✓ This indicates that the birth and death rates '
  'are almost the same. ✓ Therefore, the population will remain more or less the same/ stable population. ✓ (3)',
  ['The population size at each age group remains almost equal.',
   'This indicates that the birth and death rates are almost the same.',
   'Therefore, the population will remain more or less the same/ stable population.'],
  'The population size at each age group remains almost equal. ✓ This indicates that the birth and death rates '
  'are almost the same. ✓ Therefore, the population will remain more or less the same/ stable population. ✓ (3)',
  True,
  False),
 ('4.1.5.a',
  1,
  'Population ecology',
  'Data/Graph Interpretation',
  'What growth form is shown by humans from 1930 to 1999? (1)',
  True,
  [],
  'Exponential / geometric / logarithmic / J-shaped ✓ (1)',
  ['Exponential / geometric / logarithmic / J-shaped'],
  'Exponential / geometric / logarithmic / J-shaped ✓ (1)',
  True,
  False),
 ('4.1.5.b',
  2,
  'Population ecology',
  'Data/Graph Interpretation',
  'Give any TWO reasons for the slow population growth from 1999 to 2015. (2) 1- 2-',
  True,
  [],
  'The human population has almost reached the carrying capacity of planet earth and therefore begin to '
  'experience environmental resistance such as: - Competition for food, water and space - This could lead to war '
  'or increased crime rate - New diseases - Greater awareness and education (2)',
  ['The human population has almost reached the carrying capacity of planet earth and therefore begin to '
   'experience environmental resistance such as: - Competition for food, water and space - This could lead to war '
   'or increased crime rate - New diseases - Greater awareness and education (2)'],
  'The human population has almost reached the carrying capacity of planet earth and therefore begin to '
  'experience environmental resistance such as: - Competition for food, water and space - This could lead to war '
  'or increased crime rate - New diseases - Greater awareness and education (2)',
  True,
  False),
 ('4.1.5.c.i',
  2,
  'Population ecology',
  'Definition/Terminology',
  'Define the term ‘carrying capacity’. (2)',
  False,
  [],
  'The maximum number✓ of individuals an area can sustain ✓ (2)',
  ['The maximum number', 'of individuals an area can sustain'],
  'The maximum number✓ of individuals an area can sustain ✓ (2)',
  False,
  False),
 ('4.1.5.c.ii',
  2,
  'Population ecology',
  'Short Answer',
  'How have humans managed to continually increase the earth’s carrying capacity? (2)',
  False,
  [],
  'Improving methods of food production (monoculture) ✓ Methods of treating diseases have greatly improved ✓ (2)',
  ['Improving methods of food production (monoculture)', 'Methods of treating diseases have greatly improved'],
  'Improving methods of food production (monoculture) ✓ Methods of treating diseases have greatly improved ✓ (2)',
  False,
  False),
 ('4.1.5.c.iii',
  1,
  'Population ecology',
  'Short Answer',
  'Predict the fate of humans if the current population growth is sustained without check. (1)',
  False,
  [],
  'Could lead to possible extinction ✓ (1)',
  ['Could lead to possible extinction'],
  'Could lead to possible extinction ✓ (1)',
  False,
  False),
 ('4.1.5.c.iv',
  1,
  'Population ecology',
  'Short Answer',
  'Suggest a practical solution to reduce the accelerated growth of the human population. (1)',
  False,
  [],
  'Educate and organize awareness programmes to highlight the consequences of unchecked population growth Tax '
  'incentives for smaller families Introduction of family planning programmes Any other logical answer ✓ (any 1)',
  ['Educate and organize awareness programmes to highlight the consequences of unchecked population growth Tax '
   'incentives for smaller families Introduction of family planning programmes Any other logical answer',
   '(any 1)'],
  'Educate and organize awareness programmes to highlight the consequences of unchecked population growth Tax '
  'incentives for smaller families Introduction of family planning programmes Any other logical answer ✓ (any 1)',
  False,
  False),
 ('4.2.1',
  1,
  'Population ecology',
  'Data/Graph Interpretation',
  'What type of relationship is shown in the graph? (1)',
  True,
  [],
  'Predator- prey ✓ (1)',
  ['Predator- prey'],
  'Predator- prey ✓ (1)',
  True,
  False),
 ('4.2.2',
  1,
  'Population ecology',
  'Labelling/Diagram',
  'Identify the prey population in the above graph. (1)',
  True,
  [],
  'Green flies ✓ (1)',
  ['Green flies'],
  'Green flies ✓ (1)',
  True,
  False),
 ('4.2.3',
  1,
  'Population ecology',
  'Data/Graph Interpretation',
  'Provide a reason for your answer to QUESTION 4.2.2. (1)',
  True,
  [],
  'The rising and falling of the green fly population occurs before that of the lady bugs ✓ OR the number of lady '
  'birds is continually lower than that of the green flies (1)',
  ['The rising and falling of the green fly population occurs before that of the lady bugs',
   'OR the number of lady birds is continually lower than that of the green flies (1)'],
  'The rising and falling of the green fly population occurs before that of the lady bugs ✓ OR the number of lady '
  'birds is continually lower than that of the green flies (1)',
  True,
  False),
 ('4.2.4',
  3,
  'Population ecology',
  'Data/Graph Interpretation',
  'Explain why the chances of lady birds and green flies reaching the carrying capacity is limited. (3)',
  True,
  [],
  'The two species control each other’s population size ✓ - When the lady bird population increased the green '
  'flies decreases ✓ - When the green flies population decreases the lady birds decreases ✓ - Therefore both '
  'populations do not exceed carrying capacity ✓ (3)',
  ['The two species control each other’s population size',
   '- When the lady bird population increased the green flies decreases',
   '- When the green flies population decreases the lady birds decreases',
   '- Therefore both populations do not exceed carrying capacity'],
  'The two species control each other’s population size ✓ - When the lady bird population increased the green '
  'flies decreases ✓ - When the green flies population decreases the lady birds decreases ✓ - Therefore both '
  'populations do not exceed carrying capacity ✓ (3)',
  True,
  False),
 ('4.2.5',
  3,
  'Population ecology',
  'Data/Graph Interpretation',
  'Explain the changes in green fly population from July 1998 to October 1998. (3) Number of lady birds Number of '
  'green flies',
  True,
  [],
  'Due to an increase in lady bug ✓ numbers there was an increase in predation, ✓ leading to a decrease in green '
  'flies✓ as they are the food source. (3)',
  ['Due to an increase in lady bug',
   'numbers there was an increase in predation,',
   'leading to a decrease in green flies',
   'as they are the food source. (3)'],
  'Due to an increase in lady bug ✓ numbers there was an increase in predation, ✓ leading to a decrease in green '
  'flies✓ as they are the food source. (3)',
  True,
  False),
 ('4.3.1',
  3,
  'Population ecology',
  'Data/Graph Interpretation',
  'Using a formula, it is determined that there are 60 lady bugs in the population. How many lady bugs were there '
  'in the first sample? (3)',
  True,
  [],
  'P= (M x C)/R 60= (M x 15)/ 5 ✓ M= (60 x 5)/15 ✓ = 20 snails caught in the first sample ✓ (3)',
  ['P= (M x C)/R 60= (M x 15)/ 5', 'M= (60 x 5)/15', '= 20 snails caught in the first sample'],
  'P= (M x C)/R 60= (M x 15)/ 5 ✓ M= (60 x 5)/15 ✓ = 20 snails caught in the first sample ✓ (3)',
  True,
  False),
 ('4.3.2',
  2,
  'Population ecology',
  'Short Answer',
  'Name TWO precautions Ashleigh needs to take when completing this investigation. (2)',
  False,
  [],
  'Only a short time should pass between the first and second sampling so no births and deaths occur. The '
  'markings must not damage the individual The markings must not affect the animals behaviour or movement. The '
  'marked animals must be given enough time to mix freely with the rest of the population before the second '
  'sample is taken. The population needs to be closed ✓✓ (any 2)',
  ['Only a short time should pass between the first and second sampling so no births and deaths occur. The '
   'markings must not damage the individual The markings must not affect the animals behaviour or movement. The '
   'marked animals must be given enough time to mix freely with the rest of the population before the second '
   'sample is taken. The population needs to be closed',
   '(any 2)'],
  'Only a short time should pass between the first and second sampling so no births and deaths occur. The '
  'markings must not damage the individual The markings must not affect the animals behaviour or movement. The '
  'marked animals must be given enough time to mix freely with the rest of the population before the second '
  'sample is taken. The population needs to be closed ✓✓ (any 2)',
  False,
  False),
 ('4.3.3',
  1,
  'Population ecology',
  'Short Answer',
  'How could Ashleigh improve the accuracy and reliability of her investigation. (1)',
  False,
  [],
  'Repeat the sampling several times and calculate an average ✓ (1)',
  ['Repeat the sampling several times and calculate an average'],
  'Repeat the sampling several times and calculate an average ✓ (1)',
  False,
  False),
 ('4.3.4',
  2,
  'Population ecology',
  'Short Answer',
  'Why is the mark-recapture method the best method to use to determine the lady bug population? (2) X X X X X',
  False,
  [],
  'Lady birds are very mobile✓ and not easily visible ✓ (2)',
  ['Lady birds are very mobile', 'and not easily visible'],
  'Lady birds are very mobile✓ and not easily visible ✓ (2)',
  False,
  False),
 ('4.4.1',
  1,
  'Population ecology',
  'Data/Graph Interpretation',
  'What structural feature determines the different species of finch? (1)',
  True,
  [],
  'Beak shape and size ✓ (1)',
  ['Beak shape and size'],
  'Beak shape and size ✓ (1)',
  True,
  False),
 ('4.4.2.a',
  1,
  'Population ecology',
  'Data/Graph Interpretation',
  'Which two finches will compete the least with each other for food: A small ground finch and large ground finch '
  'B large ground finch and sharp-billed ground finch C small tree finch and medium ground finch D vegetarian '
  'finch and small ground finch',
  True,
  [],
  'C ✓',
  ['C'],
  'C ✓',
  True,
  False),
 ('4.4.2.b',
  1,
  'Population ecology',
  'Data/Graph Interpretation',
  'The only exclusively carnivorous finch has a bill that is adapted as follows: A only probing C probing and '
  'biting tips B probing and edge crushing D biting tips and edge crushing',
  True,
  [],
  'A ✓ (2)',
  ['A'],
  'A ✓ (2)',
  True,
  False),
 ('4.4.3',
  2,
  'Population ecology',
  'Data/Graph Interpretation',
  'Would the large tree finch and large ground finch be able to co-exist on the same island? Give a reason for '
  'your answer. (2)',
  True,
  [],
  'Yes. ✓ They occupy different ecological niches The large tree finch eats mainly animal material, while the '
  'large ground finch eats mainly plant material. (any 1 ✓) (2)',
  ['Yes.',
   'They occupy different ecological niches The large tree finch eats mainly animal material, while the large '
   'ground finch eats mainly plant material. (any 1'],
  'Yes. ✓ They occupy different ecological niches The large tree finch eats mainly animal material, while the '
  'large ground finch eats mainly plant material. (any 1 ✓) (2)',
  True,
  False)]

SOURCE_HASHES = {'paper_path': '9147343dbe05a4cb9daca0f7714e0d8ad44520cf672c8abc1a9b7ebb89160067',
 'memo_path': '5fb127988337c7cdc7a88e0c1d30b4e92a1fdb3ecf441cbeb5936bd3aac1d63a'}

LOCATORS = {'1.2.1': {'page': 3,
           'memo_page': 2,
           'question_stem_text': ' Various possibilities are suggested as answers to the following questions. '
                                 'Indicate the correct answer by writing the correct letter from the '
                                 'corresponding question in the space provided in the table below:',
           'parent_question_number': '1.2'},
 '1.2.2': {'page': 3,
           'memo_page': 2,
           'question_stem_text': ' Various possibilities are suggested as answers to the following questions. '
                                 'Indicate the correct answer by writing the correct letter from the '
                                 'corresponding question in the space provided in the table below:',
           'parent_question_number': '1.2'},
 '1.2.3': {'page': 3,
           'memo_page': 2,
           'question_stem_text': ' Various possibilities are suggested as answers to the following questions. '
                                 'Indicate the correct answer by writing the correct letter from the '
                                 'corresponding question in the space provided in the table below:',
           'parent_question_number': '1.2'},
 '1.2.4': {'page': 4,
           'memo_page': 2,
           'question_stem_text': ' Various possibilities are suggested as answers to the following questions. '
                                 'Indicate the correct answer by writing the correct letter from the '
                                 'corresponding question in the space provided in the table below:',
           'parent_question_number': '1.2'},
 '1.2.5': {'page': 4,
           'memo_page': 2,
           'question_stem_text': ' Various possibilities are suggested as answers to the following questions. '
                                 'Indicate the correct answer by writing the correct letter from the '
                                 'corresponding question in the space provided in the table below:',
           'parent_question_number': '1.2'},
 '1.2.6': {'page': 4,
           'memo_page': 2,
           'question_stem_text': ' Various possibilities are suggested as answers to the following questions. '
                                 'Indicate the correct answer by writing the correct letter from the '
                                 'corresponding question in the space provided in the table below:',
           'parent_question_number': '1.2'},
 '1.2.7': {'page': 4,
           'memo_page': 2,
           'question_stem_text': ' Various possibilities are suggested as answers to the following questions. '
                                 'Indicate the correct answer by writing the correct letter from the '
                                 'corresponding question in the space provided in the table below:',
           'parent_question_number': '1.2'},
 '1.2.8': {'page': 4,
           'memo_page': 2,
           'question_stem_text': ' Various possibilities are suggested as answers to the following questions. '
                                 'Indicate the correct answer by writing the correct letter from the '
                                 'corresponding question in the space provided in the table below:',
           'parent_question_number': '1.2'},
 '1.2.9': {'page': 5,
           'memo_page': 2,
           'question_stem_text': ' Various possibilities are suggested as answers to the following questions. '
                                 'Indicate the correct answer by writing the correct letter from the '
                                 'corresponding question in the space provided in the table below:',
           'parent_question_number': '1.2'},
 '1.3.1': {'page': 5,
           'memo_page': 2,
           'question_stem_text': ' Indicate whether each of the descriptions in COLUMN I applies to A ONLY, B '
                                 'ONLY, BOTH A AND B OR NEITHER of the items in COLUMN II. Write A only, B only, '
                                 'both or neither in the answer column. COLUMN I COLUMN II ANSWER',
           'parent_question_number': '1.3'},
 '1.3.2': {'page': 5,
           'memo_page': 2,
           'question_stem_text': ' Indicate whether each of the descriptions in COLUMN I applies to A ONLY, B '
                                 'ONLY, BOTH A AND B OR NEITHER of the items in COLUMN II. Write A only, B only, '
                                 'both or neither in the answer column. COLUMN I COLUMN II ANSWER',
           'parent_question_number': '1.3'},
 '1.3.3': {'page': 5,
           'memo_page': 2,
           'question_stem_text': ' Indicate whether each of the descriptions in COLUMN I applies to A ONLY, B '
                                 'ONLY, BOTH A AND B OR NEITHER of the items in COLUMN II. Write A only, B only, '
                                 'both or neither in the answer column. COLUMN I COLUMN II ANSWER',
           'parent_question_number': '1.3'},
 '1.3.4': {'page': 5,
           'memo_page': 2,
           'question_stem_text': ' Indicate whether each of the descriptions in COLUMN I applies to A ONLY, B '
                                 'ONLY, BOTH A AND B OR NEITHER of the items in COLUMN II. Write A only, B only, '
                                 'both or neither in the answer column. COLUMN I COLUMN II ANSWER',
           'parent_question_number': '1.3'},
 '1.3.5': {'page': 5,
           'memo_page': 2,
           'question_stem_text': ' Indicate whether each of the descriptions in COLUMN I applies to A ONLY, B '
                                 'ONLY, BOTH A AND B OR NEITHER of the items in COLUMN II. Write A only, B only, '
                                 'both or neither in the answer column. COLUMN I COLUMN II ANSWER',
           'parent_question_number': '1.3'},
 '1.4.1': {'page': 6,
           'memo_page': 2,
           'question_stem_text': ' An investigation was performed to determine the effect of exercise on heart '
                                 'rate. A learner (A) recorded her resting heart rate three times and recorded '
                                 'it. She then recorded her heart rate after one minute of walking on the spot, '
                                 'one minute jogging on the spot and one minute of running as fast as possible. '
                                 'She then did the same for her friend (B). Their results are recorded below. '
                                 'Activity Heart rate (bpm) Learner A Heart rate (bpm) Learner B Rest 54 68 Rest '
                                 '52 66 Rest 52 67 Walking 72 80 Jogging 94 112 Running 132 150 Immediately after '
                                 'the last activity they measured their pulse rate every minute for 5 minutes. '
                                 'They recorded this below. Time Heart rate (bpm) Learner A Heart rate (bpm) '
                                 'Learner B 1 110 137 2 95 120 3 72 102 4 54 84 5 54 72',
           'parent_question_number': '1.4'},
 '1.4.2': {'page': 6,
           'memo_page': 2,
           'question_stem_text': ' An investigation was performed to determine the effect of exercise on heart '
                                 'rate. A learner (A) recorded her resting heart rate three times and recorded '
                                 'it. She then recorded her heart rate after one minute of walking on the spot, '
                                 'one minute jogging on the spot and one minute of running as fast as possible. '
                                 'She then did the same for her friend (B). Their results are recorded below. '
                                 'Activity Heart rate (bpm) Learner A Heart rate (bpm) Learner B Rest 54 68 Rest '
                                 '52 66 Rest 52 67 Walking 72 80 Jogging 94 112 Running 132 150 Immediately after '
                                 'the last activity they measured their pulse rate every minute for 5 minutes. '
                                 'They recorded this below. Time Heart rate (bpm) Learner A Heart rate (bpm) '
                                 'Learner B 1 110 137 2 95 120 3 72 102 4 54 84 5 54 72',
           'parent_question_number': '1.4'},
 '1.4.3': {'page': 6,
           'memo_page': 2,
           'question_stem_text': ' An investigation was performed to determine the effect of exercise on heart '
                                 'rate. A learner (A) recorded her resting heart rate three times and recorded '
                                 'it. She then recorded her heart rate after one minute of walking on the spot, '
                                 'one minute jogging on the spot and one minute of running as fast as possible. '
                                 'She then did the same for her friend (B). Their results are recorded below. '
                                 'Activity Heart rate (bpm) Learner A Heart rate (bpm) Learner B Rest 54 68 Rest '
                                 '52 66 Rest 52 67 Walking 72 80 Jogging 94 112 Running 132 150 Immediately after '
                                 'the last activity they measured their pulse rate every minute for 5 minutes. '
                                 'They recorded this below. Time Heart rate (bpm) Learner A Heart rate (bpm) '
                                 'Learner B 1 110 137 2 95 120 3 72 102 4 54 84 5 54 72',
           'parent_question_number': '1.4'},
 '1.4.4': {'page': 6,
           'memo_page': 2,
           'question_stem_text': ' An investigation was performed to determine the effect of exercise on heart '
                                 'rate. A learner (A) recorded her resting heart rate three times and recorded '
                                 'it. She then recorded her heart rate after one minute of walking on the spot, '
                                 'one minute jogging on the spot and one minute of running as fast as possible. '
                                 'She then did the same for her friend (B). Their results are recorded below. '
                                 'Activity Heart rate (bpm) Learner A Heart rate (bpm) Learner B Rest 54 68 Rest '
                                 '52 66 Rest 52 67 Walking 72 80 Jogging 94 112 Running 132 150 Immediately after '
                                 'the last activity they measured their pulse rate every minute for 5 minutes. '
                                 'They recorded this below. Time Heart rate (bpm) Learner A Heart rate (bpm) '
                                 'Learner B 1 110 137 2 95 120 3 72 102 4 54 84 5 54 72',
           'parent_question_number': '1.4'},
 '1.4.5': {'page': 7,
           'memo_page': 2,
           'question_stem_text': ' An investigation was performed to determine the effect of exercise on heart '
                                 'rate. A learner (A) recorded her resting heart rate three times and recorded '
                                 'it. She then recorded her heart rate after one minute of walking on the spot, '
                                 'one minute jogging on the spot and one minute of running as fast as possible. '
                                 'She then did the same for her friend (B). Their results are recorded below. '
                                 'Activity Heart rate (bpm) Learner A Heart rate (bpm) Learner B Rest 54 68 Rest '
                                 '52 66 Rest 52 67 Walking 72 80 Jogging 94 112 Running 132 150 Immediately after '
                                 'the last activity they measured their pulse rate every minute for 5 minutes. '
                                 'They recorded this below. Time Heart rate (bpm) Learner A Heart rate (bpm) '
                                 'Learner B 1 110 137 2 95 120 3 72 102 4 54 84 5 54 72',
           'parent_question_number': '1.4'},
 '1.4.6': {'page': 7,
           'memo_page': 2,
           'question_stem_text': ' An investigation was performed to determine the effect of exercise on heart '
                                 'rate. A learner (A) recorded her resting heart rate three times and recorded '
                                 'it. She then recorded her heart rate after one minute of walking on the spot, '
                                 'one minute jogging on the spot and one minute of running as fast as possible. '
                                 'She then did the same for her friend (B). Their results are recorded below. '
                                 'Activity Heart rate (bpm) Learner A Heart rate (bpm) Learner B Rest 54 68 Rest '
                                 '52 66 Rest 52 67 Walking 72 80 Jogging 94 112 Running 132 150 Immediately after '
                                 'the last activity they measured their pulse rate every minute for 5 minutes. '
                                 'They recorded this below. Time Heart rate (bpm) Learner A Heart rate (bpm) '
                                 'Learner B 1 110 137 2 95 120 3 72 102 4 54 84 5 54 72',
           'parent_question_number': '1.4'},
 '1.4.7': {'page': 7,
           'memo_page': 2,
           'question_stem_text': ' An investigation was performed to determine the effect of exercise on heart '
                                 'rate. A learner (A) recorded her resting heart rate three times and recorded '
                                 'it. She then recorded her heart rate after one minute of walking on the spot, '
                                 'one minute jogging on the spot and one minute of running as fast as possible. '
                                 'She then did the same for her friend (B). Their results are recorded below. '
                                 'Activity Heart rate (bpm) Learner A Heart rate (bpm) Learner B Rest 54 68 Rest '
                                 '52 66 Rest 52 67 Walking 72 80 Jogging 94 112 Running 132 150 Immediately after '
                                 'the last activity they measured their pulse rate every minute for 5 minutes. '
                                 'They recorded this below. Time Heart rate (bpm) Learner A Heart rate (bpm) '
                                 'Learner B 1 110 137 2 95 120 3 72 102 4 54 84 5 54 72',
           'parent_question_number': '1.4'},
 '1.5.1': {'page': 8,
           'memo_page': 3,
           'question_stem_text': ' The table below gives information about the blood flow in two people. Person '
                                 'Blood flow through the coronary arteries in cm3/ minute A 250 B 155',
           'parent_question_number': '1.5'},
 '1.5.2': {'page': 8,
           'memo_page': 3,
           'question_stem_text': ' The table below gives information about the blood flow in two people. Person '
                                 'Blood flow through the coronary arteries in cm3/ minute A 250 B 155',
           'parent_question_number': '1.5'},
 '1.5.3': {'page': 8,
           'memo_page': 3,
           'question_stem_text': ' The table below gives information about the blood flow in two people. Person '
                                 'Blood flow through the coronary arteries in cm3/ minute A 250 B 155',
           'parent_question_number': '1.5'},
 '1.5.4': {'page': 8,
           'memo_page': 3,
           'question_stem_text': ' The table below gives information about the blood flow in two people. Person '
                                 'Blood flow through the coronary arteries in cm3/ minute A 250 B 155',
           'parent_question_number': '1.5'},
 '1.5.5': {'page': 8,
           'memo_page': 3,
           'question_stem_text': ' The table below gives information about the blood flow in two people. Person '
                                 'Blood flow through the coronary arteries in cm3/ minute A 250 B 155',
           'parent_question_number': '1.5'},
 '1.5.6': {'page': 8,
           'memo_page': 3,
           'question_stem_text': ' The table below gives information about the blood flow in two people. Person '
                                 'Blood flow through the coronary arteries in cm3/ minute A 250 B 155',
           'parent_question_number': '1.5'},
 '1.6.1': {'page': 10,
           'memo_page': 3,
           'question_stem_text': ' The growth patterns of two closely related species (A and B) that rely on the '
                                 'same food source were investigated. At first the two species were separated and '
                                 'then the two species were kept in the same habitat for the same period of time. '
                                 'In all cases the organisms were provided with a limited food supply. The '
                                 'results were shown in three graphs (A, B and C) below.',
           'parent_question_number': '1.6'},
 '1.6.2': {'page': 10,
           'memo_page': 3,
           'question_stem_text': ' The growth patterns of two closely related species (A and B) that rely on the '
                                 'same food source were investigated. At first the two species were separated and '
                                 'then the two species were kept in the same habitat for the same period of time. '
                                 'In all cases the organisms were provided with a limited food supply. The '
                                 'results were shown in three graphs (A, B and C) below.',
           'parent_question_number': '1.6'},
 '1.6.3': {'page': 10,
           'memo_page': 3,
           'question_stem_text': ' The growth patterns of two closely related species (A and B) that rely on the '
                                 'same food source were investigated. At first the two species were separated and '
                                 'then the two species were kept in the same habitat for the same period of time. '
                                 'In all cases the organisms were provided with a limited food supply. The '
                                 'results were shown in three graphs (A, B and C) below.',
           'parent_question_number': '1.6'},
 '1.6.4': {'page': 10,
           'memo_page': 3,
           'question_stem_text': ' The growth patterns of two closely related species (A and B) that rely on the '
                                 'same food source were investigated. At first the two species were separated and '
                                 'then the two species were kept in the same habitat for the same period of time. '
                                 'In all cases the organisms were provided with a limited food supply. The '
                                 'results were shown in three graphs (A, B and C) below.',
           'parent_question_number': '1.6'},
 '1.6.5': {'page': 11,
           'memo_page': 3,
           'question_stem_text': ' The growth patterns of two closely related species (A and B) that rely on the '
                                 'same food source were investigated. At first the two species were separated and '
                                 'then the two species were kept in the same habitat for the same period of time. '
                                 'In all cases the organisms were provided with a limited food supply. The '
                                 'results were shown in three graphs (A, B and C) below.',
           'parent_question_number': '1.6'},
 '1.7': {'page': 12, 'memo_page': 4, 'question_stem_text': None, 'parent_question_number': '1'},
 '1.8': {'page': 12, 'memo_page': 4, 'question_stem_text': None, 'parent_question_number': '1'},
 '2.1.1': {'page': 13,
           'memo_page': 5,
           'question_stem_text': ' Study the diagram of a region of the human skeleton. Answer the questions that '
                                 'follow.',
           'parent_question_number': '2.1'},
 '2.1.2': {'page': 13,
           'memo_page': 5,
           'question_stem_text': ' Study the diagram of a region of the human skeleton. Answer the questions that '
                                 'follow.',
           'parent_question_number': '2.1'},
 '2.1.3': {'page': 13,
           'memo_page': 5,
           'question_stem_text': ' Study the diagram of a region of the human skeleton. Answer the questions that '
                                 'follow.',
           'parent_question_number': '2.1'},
 '2.1.4': {'page': 14,
           'memo_page': 5,
           'question_stem_text': ' Study the diagram of a region of the human skeleton. Answer the questions that '
                                 'follow.',
           'parent_question_number': '2.1'},
 '2.1.5': {'page': 14,
           'memo_page': 5,
           'question_stem_text': ' Study the diagram of a region of the human skeleton. Answer the questions that '
                                 'follow.',
           'parent_question_number': '2.1'},
 '2.1.6': {'page': 14,
           'memo_page': 5,
           'question_stem_text': ' Study the diagram of a region of the human skeleton. Answer the questions that '
                                 'follow.',
           'parent_question_number': '2.1'},
 '2.1.7': {'page': 14,
           'memo_page': 5,
           'question_stem_text': ' Study the diagram of a region of the human skeleton. Answer the questions that '
                                 'follow.',
           'parent_question_number': '2.1'},
 '2.1.8': {'page': 14,
           'memo_page': 5,
           'question_stem_text': ' Study the diagram of a region of the human skeleton. Answer the questions that '
                                 'follow.',
           'parent_question_number': '2.1'},
 '2.2.1': {'page': 15,
           'memo_page': 6,
           'question_stem_text': ' Read the information below and answer the questions that follow. The word '
                                 'arthritis means inflammation of the joints, and there are more than 100 forms '
                                 'of arthritis. One of the more common types is osteoarthritis. Osteoarthritis '
                                 'occurs throughout the world and affects people differently, with joint damage '
                                 'developing over years or in same cases more quickly. Osteoarthritis is a '
                                 'degenerative form of arthritis that often affects middle aged people, but can '
                                 'occur in young people who suffer from joint injuries. Rheumatologists are '
                                 'doctors who are experts in diagnosing arthritis and other diseases of the '
                                 'joints, muscles and bones. Warning signs of this disease are typically pain '
                                 'after an activity, limited range of motion and stiffness, and swelling and '
                                 'tenderness of one or more joints.',
           'parent_question_number': '2.2'},
 '2.2.2': {'page': 15,
           'memo_page': 6,
           'question_stem_text': ' Read the information below and answer the questions that follow. The word '
                                 'arthritis means inflammation of the joints, and there are more than 100 forms '
                                 'of arthritis. One of the more common types is osteoarthritis. Osteoarthritis '
                                 'occurs throughout the world and affects people differently, with joint damage '
                                 'developing over years or in same cases more quickly. Osteoarthritis is a '
                                 'degenerative form of arthritis that often affects middle aged people, but can '
                                 'occur in young people who suffer from joint injuries. Rheumatologists are '
                                 'doctors who are experts in diagnosing arthritis and other diseases of the '
                                 'joints, muscles and bones. Warning signs of this disease are typically pain '
                                 'after an activity, limited range of motion and stiffness, and swelling and '
                                 'tenderness of one or more joints.',
           'parent_question_number': '2.2'},
 '2.2.3': {'page': 15,
           'memo_page': 6,
           'question_stem_text': ' Read the information below and answer the questions that follow. The word '
                                 'arthritis means inflammation of the joints, and there are more than 100 forms '
                                 'of arthritis. One of the more common types is osteoarthritis. Osteoarthritis '
                                 'occurs throughout the world and affects people differently, with joint damage '
                                 'developing over years or in same cases more quickly. Osteoarthritis is a '
                                 'degenerative form of arthritis that often affects middle aged people, but can '
                                 'occur in young people who suffer from joint injuries. Rheumatologists are '
                                 'doctors who are experts in diagnosing arthritis and other diseases of the '
                                 'joints, muscles and bones. Warning signs of this disease are typically pain '
                                 'after an activity, limited range of motion and stiffness, and swelling and '
                                 'tenderness of one or more joints.',
           'parent_question_number': '2.2'},
 '2.2.4': {'page': 15,
           'memo_page': 6,
           'question_stem_text': ' Read the information below and answer the questions that follow. The word '
                                 'arthritis means inflammation of the joints, and there are more than 100 forms '
                                 'of arthritis. One of the more common types is osteoarthritis. Osteoarthritis '
                                 'occurs throughout the world and affects people differently, with joint damage '
                                 'developing over years or in same cases more quickly. Osteoarthritis is a '
                                 'degenerative form of arthritis that often affects middle aged people, but can '
                                 'occur in young people who suffer from joint injuries. Rheumatologists are '
                                 'doctors who are experts in diagnosing arthritis and other diseases of the '
                                 'joints, muscles and bones. Warning signs of this disease are typically pain '
                                 'after an activity, limited range of motion and stiffness, and swelling and '
                                 'tenderness of one or more joints.',
           'parent_question_number': '2.2'},
 '2.2.5': {'page': 15,
           'memo_page': 6,
           'question_stem_text': ' Read the information below and answer the questions that follow. The word '
                                 'arthritis means inflammation of the joints, and there are more than 100 forms '
                                 'of arthritis. One of the more common types is osteoarthritis. Osteoarthritis '
                                 'occurs throughout the world and affects people differently, with joint damage '
                                 'developing over years or in same cases more quickly. Osteoarthritis is a '
                                 'degenerative form of arthritis that often affects middle aged people, but can '
                                 'occur in young people who suffer from joint injuries. Rheumatologists are '
                                 'doctors who are experts in diagnosing arthritis and other diseases of the '
                                 'joints, muscles and bones. Warning signs of this disease are typically pain '
                                 'after an activity, limited range of motion and stiffness, and swelling and '
                                 'tenderness of one or more joints.',
           'parent_question_number': '2.2'},
 '2.2.6': {'page': 15,
           'memo_page': 6,
           'question_stem_text': ' Read the information below and answer the questions that follow. The word '
                                 'arthritis means inflammation of the joints, and there are more than 100 forms '
                                 'of arthritis. One of the more common types is osteoarthritis. Osteoarthritis '
                                 'occurs throughout the world and affects people differently, with joint damage '
                                 'developing over years or in same cases more quickly. Osteoarthritis is a '
                                 'degenerative form of arthritis that often affects middle aged people, but can '
                                 'occur in young people who suffer from joint injuries. Rheumatologists are '
                                 'doctors who are experts in diagnosing arthritis and other diseases of the '
                                 'joints, muscles and bones. Warning signs of this disease are typically pain '
                                 'after an activity, limited range of motion and stiffness, and swelling and '
                                 'tenderness of one or more joints.',
           'parent_question_number': '2.2'},
 '2.3.1': {'page': 16,
           'memo_page': 6,
           'question_stem_text': ' Study the graph below and answer the questions that follow.',
           'parent_question_number': '2.3'},
 '2.3.2': {'page': 16,
           'memo_page': 6,
           'question_stem_text': ' Study the graph below and answer the questions that follow.',
           'parent_question_number': '2.3'},
 '2.3.3': {'page': 16,
           'memo_page': 6,
           'question_stem_text': ' Study the graph below and answer the questions that follow.',
           'parent_question_number': '2.3'},
 '2.3.4': {'page': 16,
           'memo_page': 6,
           'question_stem_text': ' Study the graph below and answer the questions that follow.',
           'parent_question_number': '2.3'},
 '2.3.5': {'page': 16,
           'memo_page': 6,
           'question_stem_text': ' Study the graph below and answer the questions that follow.',
           'parent_question_number': '2.3'},
 '3.1.1': {'page': 17,
           'memo_page': 7,
           'question_stem_text': ' The diagram below shows a section through the human heart.',
           'parent_question_number': '3.1'},
 '3.1.4': {'page': 18,
           'memo_page': 7,
           'question_stem_text': ' The diagram below shows a section through the human heart.',
           'parent_question_number': '3.1'},
 '3.1.5': {'page': 18,
           'memo_page': 7,
           'question_stem_text': ' The diagram below shows a section through the human heart.',
           'parent_question_number': '3.1'},
 '3.1.6': {'page': 18,
           'memo_page': 7,
           'question_stem_text': ' The diagram below shows a section through the human heart.',
           'parent_question_number': '3.1'},
 '3.2.1': {'page': 19,
           'memo_page': 8,
           'question_stem_text': ' The table below shows the recommended minimum heart rates that cyclists of '
                                 'different ages should maintain in order to either metabolise fat or improve '
                                 'their fitness. Age Minimum heart rate for metabolising fat (beats/min) Minimum '
                                 'heart rate for improving fitness (beats/min) 10 136 168 20 130 160 30 123 152 '
                                 '40 116 Y 50 X 136 60 104 128',
           'parent_question_number': '3.2'},
 '3.2.2': {'page': 19,
           'memo_page': 8,
           'question_stem_text': ' The table below shows the recommended minimum heart rates that cyclists of '
                                 'different ages should maintain in order to either metabolise fat or improve '
                                 'their fitness. Age Minimum heart rate for metabolising fat (beats/min) Minimum '
                                 'heart rate for improving fitness (beats/min) 10 136 168 20 130 160 30 123 152 '
                                 '40 116 Y 50 X 136 60 104 128',
           'parent_question_number': '3.2'},
 '3.2.3': {'page': 20,
           'memo_page': 8,
           'question_stem_text': ' The table below shows the recommended minimum heart rates that cyclists of '
                                 'different ages should maintain in order to either metabolise fat or improve '
                                 'their fitness. Age Minimum heart rate for metabolising fat (beats/min) Minimum '
                                 'heart rate for improving fitness (beats/min) 10 136 168 20 130 160 30 123 152 '
                                 '40 116 Y 50 X 136 60 104 128',
           'parent_question_number': '3.2'},
 '3.2.4': {'page': 20,
           'memo_page': 8,
           'question_stem_text': ' The table below shows the recommended minimum heart rates that cyclists of '
                                 'different ages should maintain in order to either metabolise fat or improve '
                                 'their fitness. Age Minimum heart rate for metabolising fat (beats/min) Minimum '
                                 'heart rate for improving fitness (beats/min) 10 136 168 20 130 160 30 123 152 '
                                 '40 116 Y 50 X 136 60 104 128',
           'parent_question_number': '3.2'},
 '3.2.5': {'page': 20,
           'memo_page': 8,
           'question_stem_text': ' The table below shows the recommended minimum heart rates that cyclists of '
                                 'different ages should maintain in order to either metabolise fat or improve '
                                 'their fitness. Age Minimum heart rate for metabolising fat (beats/min) Minimum '
                                 'heart rate for improving fitness (beats/min) 10 136 168 20 130 160 30 123 152 '
                                 '40 116 Y 50 X 136 60 104 128',
           'parent_question_number': '3.2'},
 '3.3.1': {'page': 20,
           'memo_page': 8,
           'question_stem_text': ' Blood doping is the practice of boosting the number of red blood cells in the '
                                 'bloodstream in order to enhance athletic performance. Because such blood cells '
                                 'carry from the lungs to the muscles, a higher concentration in the blood can '
                                 'improve an athlete’s aerobic capacity (VO2 max) and endurance.',
           'parent_question_number': '3.3'},
 '3.3.2': {'page': 20,
           'memo_page': 8,
           'question_stem_text': ' Blood doping is the practice of boosting the number of red blood cells in the '
                                 'bloodstream in order to enhance athletic performance. Because such blood cells '
                                 'carry from the lungs to the muscles, a higher concentration in the blood can '
                                 'improve an athlete’s aerobic capacity (VO2 max) and endurance.',
           'parent_question_number': '3.3'},
 '3.3.3': {'page': 21,
           'memo_page': 8,
           'question_stem_text': ' Blood doping is the practice of boosting the number of red blood cells in the '
                                 'bloodstream in order to enhance athletic performance. Because such blood cells '
                                 'carry from the lungs to the muscles, a higher concentration in the blood can '
                                 'improve an athlete’s aerobic capacity (VO2 max) and endurance.',
           'parent_question_number': '3.3'},
 '3.3.4': {'page': 21,
           'memo_page': 8,
           'question_stem_text': ' Blood doping is the practice of boosting the number of red blood cells in the '
                                 'bloodstream in order to enhance athletic performance. Because such blood cells '
                                 'carry from the lungs to the muscles, a higher concentration in the blood can '
                                 'improve an athlete’s aerobic capacity (VO2 max) and endurance.',
           'parent_question_number': '3.3'},
 '3.3.5': {'page': 21,
           'memo_page': 8,
           'question_stem_text': ' Blood doping is the practice of boosting the number of red blood cells in the '
                                 'bloodstream in order to enhance athletic performance. Because such blood cells '
                                 'carry from the lungs to the muscles, a higher concentration in the blood can '
                                 'improve an athlete’s aerobic capacity (VO2 max) and endurance.',
           'parent_question_number': '3.3'},
 '3.3.6': {'page': 21,
           'memo_page': 8,
           'question_stem_text': ' Blood doping is the practice of boosting the number of red blood cells in the '
                                 'bloodstream in order to enhance athletic performance. Because such blood cells '
                                 'carry from the lungs to the muscles, a higher concentration in the blood can '
                                 'improve an athlete’s aerobic capacity (VO2 max) and endurance.',
           'parent_question_number': '3.3'},
 '4.1.1': {'page': 23,
           'memo_page': 9,
           'question_stem_text': ' Study the Age-gender pyramids representing two different countries and answer '
                                 'the questions that follow. A B',
           'parent_question_number': '4.1'},
 '4.1.2': {'page': 23,
           'memo_page': 9,
           'question_stem_text': ' Study the Age-gender pyramids representing two different countries and answer '
                                 'the questions that follow. A B',
           'parent_question_number': '4.1'},
 '4.1.3': {'page': 23,
           'memo_page': 9,
           'question_stem_text': ' Study the Age-gender pyramids representing two different countries and answer '
                                 'the questions that follow. A B',
           'parent_question_number': '4.1'},
 '4.1.4': {'page': 23,
           'memo_page': 9,
           'question_stem_text': ' Study the Age-gender pyramids representing two different countries and answer '
                                 'the questions that follow. A B',
           'parent_question_number': '4.1'},
 '4.2.1': {'page': 25,
           'memo_page': 10,
           'question_stem_text': ' The graph below represents an interaction between two organisms in an '
                                 'ecosystem.',
           'parent_question_number': '4.2'},
 '4.2.2': {'page': 25,
           'memo_page': 10,
           'question_stem_text': ' The graph below represents an interaction between two organisms in an '
                                 'ecosystem.',
           'parent_question_number': '4.2'},
 '4.2.3': {'page': 25,
           'memo_page': 10,
           'question_stem_text': ' The graph below represents an interaction between two organisms in an '
                                 'ecosystem.',
           'parent_question_number': '4.2'},
 '4.2.4': {'page': 25,
           'memo_page': 10,
           'question_stem_text': ' The graph below represents an interaction between two organisms in an '
                                 'ecosystem.',
           'parent_question_number': '4.2'},
 '4.2.5': {'page': 25,
           'memo_page': 10,
           'question_stem_text': ' The graph below represents an interaction between two organisms in an '
                                 'ecosystem.',
           'parent_question_number': '4.2'},
 '4.3.1': {'page': 26,
           'memo_page': 10,
           'question_stem_text': ' Ashleigh catches lady bugs at random and marked each one with an X and '
                                 'returned them to her garden. After one week, a second sample was collected. The '
                                 'diagram below shows the lady bugs that were caught during the second selection.',
           'parent_question_number': '4.3'},
 '4.3.2': {'page': 26,
           'memo_page': 10,
           'question_stem_text': ' Ashleigh catches lady bugs at random and marked each one with an X and '
                                 'returned them to her garden. After one week, a second sample was collected. The '
                                 'diagram below shows the lady bugs that were caught during the second selection.',
           'parent_question_number': '4.3'},
 '4.3.3': {'page': 26,
           'memo_page': 10,
           'question_stem_text': ' Ashleigh catches lady bugs at random and marked each one with an X and '
                                 'returned them to her garden. After one week, a second sample was collected. The '
                                 'diagram below shows the lady bugs that were caught during the second selection.',
           'parent_question_number': '4.3'},
 '4.3.4': {'page': 26,
           'memo_page': 10,
           'question_stem_text': ' Ashleigh catches lady bugs at random and marked each one with an X and '
                                 'returned them to her garden. After one week, a second sample was collected. The '
                                 'diagram below shows the lady bugs that were caught during the second selection.',
           'parent_question_number': '4.3'},
 '4.4.1': {'page': 27,
           'memo_page': 10,
           'question_stem_text': ' Fourteen finch species, with beaks of different shapes and sizes, originated '
                                 'from one common ancestor by means of evolution. The different shapes and sizes '
                                 'of their beaks determine the type of food they eat. Study the diagram below and '
                                 'answer the questions that follow.',
           'parent_question_number': '4.4'},
 '4.4.3': {'page': 27,
           'memo_page': 10,
           'question_stem_text': ' Fourteen finch species, with beaks of different shapes and sizes, originated '
                                 'from one common ancestor by means of evolution. The different shapes and sizes '
                                 'of their beaks determine the type of food they eat. Study the diagram below and '
                                 'answer the questions that follow.',
           'parent_question_number': '4.4'},
 '1.5.7.a': {'page': 9,
             'memo_page': 3,
             'question_stem_text': ' The table below gives information about the blood flow in two people. Person '
                                   'Blood flow through the coronary arteries in cm3/ minute A 250 B 155 Coronary '
                                   'artery disease can be treated by: • Inserting a stent • Using a Coronary '
                                   'Artery Bypass Graft (CABG) The table on the next page gives information about '
                                   'each method: Stent CABG Procedure The patient is awake during the procedure. '
                                   'A small cut is made in the skin. A wire mesh is inserted into the coronary '
                                   'artery via a blood vessel in the arm or leg. The patient is not awake during '
                                   'the procedure. The chest is cut open. A section of blood vessel from the arm '
                                   'or leg is removed. It is used to create a new channel for blood to bypass the '
                                   'blockage in the coronary artery. When procedure is recommended When only one '
                                   'blockage is present When multiple blockages are present Time spent in '
                                   'hospital after procedure 2-3 hours At least 7 days Recovery time after '
                                   'procedure 7 days 12 weeks Risk of heart attack during procedure 1% 2% Chance '
                                   'of failure within one year 40% 5% ',
             'parent_question_number': '1.5.7'},
 '1.5.7.b': {'page': 9,
             'memo_page': 3,
             'question_stem_text': ' The table below gives information about the blood flow in two people. Person '
                                   'Blood flow through the coronary arteries in cm3/ minute A 250 B 155 Coronary '
                                   'artery disease can be treated by: • Inserting a stent • Using a Coronary '
                                   'Artery Bypass Graft (CABG) The table on the next page gives information about '
                                   'each method: Stent CABG Procedure The patient is awake during the procedure. '
                                   'A small cut is made in the skin. A wire mesh is inserted into the coronary '
                                   'artery via a blood vessel in the arm or leg. The patient is not awake during '
                                   'the procedure. The chest is cut open. A section of blood vessel from the arm '
                                   'or leg is removed. It is used to create a new channel for blood to bypass the '
                                   'blockage in the coronary artery. When procedure is recommended When only one '
                                   'blockage is present When multiple blockages are present Time spent in '
                                   'hospital after procedure 2-3 hours At least 7 days Recovery time after '
                                   'procedure 7 days 12 weeks Risk of heart attack during procedure 1% 2% Chance '
                                   'of failure within one year 40% 5% ',
             'parent_question_number': '1.5.7'},
 '1.6.6.a': {'page': 11,
             'memo_page': 3,
             'question_stem_text': ' The growth patterns of two closely related species (A and B) that rely on '
                                   'the same food source were investigated. At first the two species were '
                                   'separated and then the two species were kept in the same habitat for the same '
                                   'period of time. In all cases the organisms were provided with a limited food '
                                   'supply. The results were shown in three graphs (A, B and C) below. After some '
                                   'time, a natural predator of species A was introduced into the habitat. ',
             'parent_question_number': '1.6.6'},
 '1.6.6.b': {'page': 11,
             'memo_page': 4,
             'question_stem_text': ' The growth patterns of two closely related species (A and B) that rely on '
                                   'the same food source were investigated. At first the two species were '
                                   'separated and then the two species were kept in the same habitat for the same '
                                   'period of time. In all cases the organisms were provided with a limited food '
                                   'supply. The results were shown in three graphs (A, B and C) below. After some '
                                   'time, a natural predator of species A was introduced into the habitat. ',
             'parent_question_number': '1.6.6'},
 '3.1.2.a': {'page': 17,
             'memo_page': 7,
             'question_stem_text': ' The diagram below shows a section through the human heart. Write down '
                                   'whether the following valves are open or closed when the pressure in chamber '
                                   'C is at its highest: (2) ',
             'parent_question_number': '3.1.2'},
 '3.1.2.b': {'page': 17,
             'memo_page': 7,
             'question_stem_text': ' The diagram below shows a section through the human heart. Write down '
                                   'whether the following valves are open or closed when the pressure in chamber '
                                   'C is at its highest: (2) ',
             'parent_question_number': '3.1.2'},
 '3.1.3.a': {'page': 17,
             'memo_page': 7,
             'question_stem_text': ' The diagram below shows a section through the human heart. Explain the '
                                   'advantage of having: ',
             'parent_question_number': '3.1.3'},
 '3.1.3.b': {'page': 18,
             'memo_page': 7,
             'question_stem_text': ' The diagram below shows a section through the human heart. Explain the '
                                   'advantage of having: ',
             'parent_question_number': '3.1.3'},
 '3.1.7.a': {'page': 19,
             'memo_page': 7,
             'question_stem_text': ' The diagram below shows a section through the human heart. The blood '
                                   'pressure in vessel Y was recorded using an electronic pressure gauge. Here is '
                                   'the recording: Time in seconds Blood pressure graph mmHg ',
             'parent_question_number': '3.1.7'},
 '3.1.7.b': {'page': 19,
             'memo_page': 7,
             'question_stem_text': ' The diagram below shows a section through the human heart. The blood '
                                   'pressure in vessel Y was recorded using an electronic pressure gauge. Here is '
                                   'the recording: Time in seconds Blood pressure graph mmHg ',
             'parent_question_number': '3.1.7'},
 '3.1.7.c': {'page': 19,
             'memo_page': 7,
             'question_stem_text': ' The diagram below shows a section through the human heart. The blood '
                                   'pressure in vessel Y was recorded using an electronic pressure gauge. Here is '
                                   'the recording: Time in seconds Blood pressure graph mmHg ',
             'parent_question_number': '3.1.7'},
 '3.1.7.d': {'page': 19,
             'memo_page': 7,
             'question_stem_text': ' The diagram below shows a section through the human heart. The blood '
                                   'pressure in vessel Y was recorded using an electronic pressure gauge. Here is '
                                   'the recording: Time in seconds Blood pressure graph mmHg ',
             'parent_question_number': '3.1.7'},
 '4.1.5.a': {'page': 24,
             'memo_page': 9,
             'question_stem_text': ' Study the Age-gender pyramids representing two different countries and '
                                   'answer the questions that follow. A B The graph below shows the growth of the '
                                   'human population from 1650 to 2015. ',
             'parent_question_number': '4.1.5'},
 '4.1.5.b': {'page': 24,
             'memo_page': 9,
             'question_stem_text': ' Study the Age-gender pyramids representing two different countries and '
                                   'answer the questions that follow. A B The graph below shows the growth of the '
                                   'human population from 1650 to 2015. ',
             'parent_question_number': '4.1.5'},
 '4.1.5.c.i': {'page': 24,
               'memo_page': 9,
               'question_stem_text': ' Study the Age-gender pyramids representing two different countries and '
                                     'answer the questions that follow. A B The graph below shows the growth of '
                                     'the human population from 1650 to 2015.  Current global population of over '
                                     '7 billion is already two to three times higher than the sustainable level. '
                                     'Several recent studies show that Earth’s resources are enough to sustain '
                                     'only about 2 billion people at a European standard of living. ',
               'parent_question_number': '4.1.5.c'},
 '4.1.5.c.ii': {'page': 24,
                'memo_page': 9,
                'question_stem_text': ' Study the Age-gender pyramids representing two different countries and '
                                      'answer the questions that follow. A B The graph below shows the growth of '
                                      'the human population from 1650 to 2015.  Current global population of over '
                                      '7 billion is already two to three times higher than the sustainable level. '
                                      'Several recent studies show that Earth’s resources are enough to sustain '
                                      'only about 2 billion people at a European standard of living. ',
                'parent_question_number': '4.1.5.c'},
 '4.1.5.c.iii': {'page': 24,
                 'memo_page': 9,
                 'question_stem_text': ' Study the Age-gender pyramids representing two different countries and '
                                       'answer the questions that follow. A B The graph below shows the growth of '
                                       'the human population from 1650 to 2015.  Current global population of '
                                       'over 7 billion is already two to three times higher than the sustainable '
                                       'level. Several recent studies show that Earth’s resources are enough to '
                                       'sustain only about 2 billion people at a European standard of living. ',
                 'parent_question_number': '4.1.5.c'},
 '4.1.5.c.iv': {'page': 24,
                'memo_page': 9,
                'question_stem_text': ' Study the Age-gender pyramids representing two different countries and '
                                      'answer the questions that follow. A B The graph below shows the growth of '
                                      'the human population from 1650 to 2015.  Current global population of over '
                                      '7 billion is already two to three times higher than the sustainable level. '
                                      'Several recent studies show that Earth’s resources are enough to sustain '
                                      'only about 2 billion people at a European standard of living. ',
                'parent_question_number': '4.1.5.c'},
 '4.4.2.a': {'page': 27,
             'memo_page': 10,
             'question_stem_text': ' Fourteen finch species, with beaks of different shapes and sizes, originated '
                                   'from one common ancestor by means of evolution. The different shapes and '
                                   'sizes of their beaks determine the type of food they eat. Study the diagram '
                                   'below and answer the questions that follow. In each of the following, CIRCLE '
                                   'only the letter that corresponds: (2) ',
             'parent_question_number': '4.4.2'},
 '4.4.2.b': {'page': 27,
             'memo_page': 10,
             'question_stem_text': ' Fourteen finch species, with beaks of different shapes and sizes, originated '
                                   'from one common ancestor by means of evolution. The different shapes and '
                                   'sizes of their beaks determine the type of food they eat. Study the diagram '
                                   'below and answer the questions that follow. In each of the following, CIRCLE '
                                   'only the letter that corresponds: (2) ',
             'parent_question_number': '4.4.2'},
 '1.1.row1': {'page': 2,
              'memo_page': 2,
              'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                    'Column I. Each letter may only be used once. Column II: A succession; B '
                                    'carrying capacity; C food web; D biotic factors; E abiotic factors; F '
                                    'biodiversity; G community; H stratification; I ecosystem; J population; K '
                                    'predator.',
              'parent_question_number': '1.1'},
 '1.1.row2': {'page': 2,
              'memo_page': 2,
              'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                    'Column I. Each letter may only be used once. Column II: A succession; B '
                                    'carrying capacity; C food web; D biotic factors; E abiotic factors; F '
                                    'biodiversity; G community; H stratification; I ecosystem; J population; K '
                                    'predator.',
              'parent_question_number': '1.1'},
 '1.1.row3': {'page': 2,
              'memo_page': 2,
              'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                    'Column I. Each letter may only be used once. Column II: A succession; B '
                                    'carrying capacity; C food web; D biotic factors; E abiotic factors; F '
                                    'biodiversity; G community; H stratification; I ecosystem; J population; K '
                                    'predator.',
              'parent_question_number': '1.1'},
 '1.1.row4': {'page': 2,
              'memo_page': 2,
              'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                    'Column I. Each letter may only be used once. Column II: A succession; B '
                                    'carrying capacity; C food web; D biotic factors; E abiotic factors; F '
                                    'biodiversity; G community; H stratification; I ecosystem; J population; K '
                                    'predator.',
              'parent_question_number': '1.1'},
 '1.1.row5': {'page': 2,
              'memo_page': 2,
              'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                    'Column I. Each letter may only be used once. Column II: A succession; B '
                                    'carrying capacity; C food web; D biotic factors; E abiotic factors; F '
                                    'biodiversity; G community; H stratification; I ecosystem; J population; K '
                                    'predator.',
              'parent_question_number': '1.1'},
 '1.1.row6': {'page': 2,
              'memo_page': 2,
              'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                    'Column I. Each letter may only be used once. Column II: A succession; B '
                                    'carrying capacity; C food web; D biotic factors; E abiotic factors; F '
                                    'biodiversity; G community; H stratification; I ecosystem; J population; K '
                                    'predator.',
              'parent_question_number': '1.1'},
 '1.1.row7': {'page': 2,
              'memo_page': 2,
              'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                    'Column I. Each letter may only be used once. Column II: A succession; B '
                                    'carrying capacity; C food web; D biotic factors; E abiotic factors; F '
                                    'biodiversity; G community; H stratification; I ecosystem; J population; K '
                                    'predator.',
              'parent_question_number': '1.1'},
 '1.1.row8': {'page': 2,
              'memo_page': 2,
              'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                    'Column I. Each letter may only be used once. Column II: A succession; B '
                                    'carrying capacity; C food web; D biotic factors; E abiotic factors; F '
                                    'biodiversity; G community; H stratification; I ecosystem; J population; K '
                                    'predator.',
              'parent_question_number': '1.1'},
 '1.1.row9': {'page': 2,
              'memo_page': 2,
              'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                    'Column I. Each letter may only be used once. Column II: A succession; B '
                                    'carrying capacity; C food web; D biotic factors; E abiotic factors; F '
                                    'biodiversity; G community; H stratification; I ecosystem; J population; K '
                                    'predator.',
              'parent_question_number': '1.1'},
 '1.1.row10': {'page': 2,
               'memo_page': 2,
               'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                     'Column I. Each letter may only be used once. Column II: A succession; B '
                                     'carrying capacity; C food web; D biotic factors; E abiotic factors; F '
                                     'biodiversity; G community; H stratification; I ecosystem; J population; K '
                                     'predator.',
               'parent_question_number': '1.1'}}
