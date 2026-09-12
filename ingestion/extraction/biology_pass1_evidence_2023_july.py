"""Question-level evidence transcribed from the paper and its verified marking guidelines.

Do not silently correct source errors. LOCATORS retains source pages and shared context.
"""

PAPER = {'paper_key': 'BIO-2023-JUL',
 'paper_path': 'data/organized/biology/July exam p1.pdf',
 'memo_path': 'data/organized/biology/July exam p1 MG.pdf',
 'year': 2023,
 'exam_date': '21 JULY 2023',
 'exam_period': 'july',
 'paper_type': 'paper1',
 'exam_board': 'internal',
 'total_marks': 150,
 'question_totals': [60, 30, 30, 30],
 'examiner': 'MRS S. STEGMANN',
 'moderator': 'MRS B. ZAJAC',
 'duration_stated': '2 ½ HOURS',
 'fidelity_rung': 'A',
 'notes': 'Read directly from digital PDF text. Whitespace normalized, blank answer lines and repeating headers '
          'omitted. Lettered subparts retain source letters; rowN identifies an unnumbered matching row. '
          'Image-dependent evidence is unresolved, not reconstructed.',
 'alignment_anchors': {'memo': '4.1.1. Alicin',
                       'paper': 'Which substance will be destroyed if you were to cook the garlic'}}

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
  'Microorganisms',
  'Definition/Terminology',
  'Acellular',
  False,
  [],
  'D ✓',
  ['D'],
  'D ✓',
  False,
  False),
 ('1.1.row10',
  1,
  'Microorganisms',
  'Definition/Terminology',
  'Saprotropic',
  False,
  [],
  'L ✓',
  ['L'],
  'L ✓',
  False,
  False),
 ('1.1.row2',
  1,
  'Microorganisms',
  'Definition/Terminology',
  'Spores',
  False,
  [],
  'H ✓',
  ['H'],
  'H ✓',
  False,
  False),
 ('1.1.row3',
  1,
  'Microorganisms',
  'Definition/Terminology',
  'Spherical shape',
  False,
  [],
  'F ✓',
  ['F'],
  'F ✓',
  False,
  False),
 ('1.1.row4',
  1,
  'Microorganisms',
  'Definition/Terminology',
  'Consumers',
  False,
  [],
  'K ✓',
  ['K'],
  'K ✓',
  False,
  False),
 ('1.1.row5',
  1,
  'Microorganisms',
  'Definition/Terminology',
  'Binary fission',
  False,
  [],
  'C ✓',
  ['C'],
  'C ✓',
  False,
  False),
 ('1.1.row6',
  1,
  'Microorganisms',
  'Definition/Terminology',
  'Circular ring of DNA',
  False,
  [],
  'E ✓',
  ['E'],
  'E ✓',
  False,
  False),
 ('1.1.row7',
  1,
  'Microorganisms',
  'Definition/Terminology',
  'Eukaryotic',
  False,
  [],
  'B ✓',
  ['B'],
  'B ✓',
  False,
  False),
 ('1.1.row8',
  1,
  'Microorganisms',
  'Definition/Terminology',
  'Plant-like protists',
  False,
  [],
  'I ✓',
  ['I'],
  'I ✓',
  False,
  False),
 ('1.1.row9',
  1,
  'Microorganisms',
  'Definition/Terminology',
  'Floating organisms',
  False,
  [],
  'G ✓',
  ['G'],
  'G ✓',
  False,
  False),
 ('1.2.1',
  1,
  'Microorganisms',
  'Multiple Choice',
  'Antibiotics are used to treat some diseases. Which diseases could they be effective against? Bacterial '
  'infection HIV Yeast infection A ✓ ✓ ✓ B ✓ × ✓ C ✓ × × D × ✓ × (1)',
  False,
  [],
  'C ✓ (1)',
  ['C'],
  'C ✓ (1)',
  False,
  False),
 ('1.2.2',
  1,
  'Microorganisms',
  'Multiple Choice',
  'Viruses consist of: A. RNA, DNA and a protein coat B. Proteins, cell membrane and RNA C. RNA or DNA and a cell '
  'membrane D. RNA or DNA and a protein coat (1)',
  False,
  [],
  'D ✓ (1)',
  ['D'],
  'D ✓ (1)',
  False,
  False),
 ('1.2.3',
  1,
  'Excretion',
  'Multiple Choice',
  'The diagram below shows the human excretory system and related blood vessels. What are structures X, Y and Z? '
  'X Y Z A ureter bladder urethra B ureter kidney urethra C urethra bladder ureter D urethra kidney ureter (1)',
  True,
  [],
  'A ✓ (1)',
  ['A'],
  'A ✓ (1)',
  True,
  False),
 ('1.2.4',
  1,
  'Excretion',
  'Multiple Choice',
  'Which row describes the urine produced by a person on a hot day? Concentration of urine Volume of urine A '
  'concentrated large B concentrated small C dilute large D dilute small (1)',
  False,
  [],
  'B ✓ (1)',
  ['B'],
  'B ✓ (1)',
  False,
  False),
 ('1.2.5',
  1,
  'Excretion',
  'Multiple Choice',
  'In healthy people, which substance is completely reabsorbed into the blood from the kidney tubules? A. Glucose '
  'B. Salts C. Urea D. Water (1)',
  False,
  [],
  'A ✓ (1)',
  ['A'],
  'A ✓ (1)',
  False,
  False),
 ('1.2.6',
  1,
  'Skeletal system',
  'Multiple Choice',
  'The axial skeleton is made up of the following regions: A. Skull, vertebral column and pelvis B. Skull, '
  'vertebral column, ribs and sternum C. Skull, pectoral girdle, ribs and sternum D. Skull, pelvic girdle, ribs '
  'and sternum (1)',
  False,
  [],
  'B ✓ (1)',
  ['B'],
  'B ✓ (1)',
  False,
  False),
 ('1.2.7',
  1,
  'Skeletal system',
  'Multiple Choice',
  'Which of the following statements is NOT true about tendons? A. Connects muscle to bone. B. Comprised of '
  'collagen and elastic fibres. C. Stabilizes joints. D. Bring about movement. (1)',
  False,
  [],
  'B ✓ (1)',
  ['B'],
  'B ✓ (1)',
  False,
  False),
 ('1.2.8',
  1,
  'Skeletal system',
  'Multiple Choice',
  'What type of bone would a rib be classified as? A. Long bone B. Short bone C. Flat bone D. Irregular bone (1)',
  False,
  [],
  'C ✓ (1)',
  ['C'],
  'C ✓ (1)',
  False,
  False),
 ('1.2.9',
  2,
  'Microorganisms',
  'Multiple Choice',
  'The graph shows the number of people infected with HIV, in one part of the world, from 1985 to 2010. (2) Using '
  'data from the graph, which statement is correct? A. Between 1995 and 2000 the number of people infected with '
  'HIV increased by 67%. B. Between 1995 and 2000 the number of people infected with HIV increased by 20%. C. '
  'Between 1990 and 1995 the number of people infected with HIV doubled. D. Between 1995 and 2000 the number of '
  'people infected with HIV doubled.',
  True,
  [],
  'A ✓✓ (2)',
  ['A'],
  'A ✓✓ (2)',
  True,
  False),
 ('1.3.1',
  1,
  'Microorganisms',
  'Definition/Terminology',
  'What is a pathogen? (1)',
  False,
  [],
  'Disease-causing organism/ agent ✓ (1)',
  ['Disease-causing organism/ agent'],
  'Disease-causing organism/ agent ✓ (1)',
  False,
  False),
 ('1.3.2',
  1,
  'Microorganisms',
  'Short Answer',
  'Which country had the greatest number of adults infected with HIV/AIDS? (1)',
  False,
  [],
  'A ✓ (1)',
  ['A'],
  'A ✓ (1)',
  False,
  False),
 ('1.3.3',
  3,
  'Microorganisms',
  'Short Answer',
  'Calculate the percentage of adults from Country B that were infected with HIV/AIDS. (3)',
  False,
  [],
  '8200/ 248 490 ✓ * 100 ✓ = 3,29 %✓ adults (accept if rounded down to 3) (3)',
  ['8200/ 248 490', '* 100', '= 3,29 %', 'adults (accept if rounded down to 3) (3)'],
  '8200/ 248 490 ✓ * 100 ✓ = 3,29 %✓ adults (accept if rounded down to 3) (3)',
  False,
  False),
 ('1.3.4',
  2,
  'Microorganisms',
  'Short Answer',
  'How could the government of countries greatly affected by HIV/AIDS reduce the number of people infected in the '
  'future? (2)',
  False,
  [],
  'Make people more aware about how HIV is transmitted Educate people on the STI Make condoms more readily '
  'available Any acceptable answer ✓✓ (2)',
  ['Make people more aware about how HIV is transmitted Educate people on the STI Make condoms more readily '
   'available Any acceptable answer'],
  'Make people more aware about how HIV is transmitted Educate people on the STI Make condoms more readily '
  'available Any acceptable answer ✓✓ (2)',
  False,
  False),
 ('1.3.5',
  7,
  'Microorganisms',
  'Data/Graph Interpretation',
  'In the space below draw a bar graph to show the estimated number of adults infected with HIV/AIDS. (7)',
  True,
  [],
  'Heading (H) ✓✓ X axis (title + scale)- (X) ✓ Y axis (title + scale)- (Y) ✓ Bars same width + spacing the same '
  '(B) ✓ Plotting (P)✓✓ (7)',
  ['Heading (H)',
   'X axis (title + scale)- (X)',
   'Y axis (title + scale)- (Y)',
   'Bars same width + spacing the same (B)',
   'Plotting (P)'],
  'Heading (H) ✓✓ X axis (title + scale)- (X) ✓ Y axis (title + scale)- (Y) ✓ Bars same width + spacing the same '
  '(B) ✓ Plotting (P)✓✓ (7)',
  True,
  False),
 ('1.4.1',
  2,
  'Excretion',
  'Data/Graph Interpretation',
  'The box on the left shows the beginning of a sentence. The boxes on the right show some sentence endings. Draw '
  'TWO straight lines from “Excretion” to the boxes on the right to make two correct sentences. (2)',
  True,
  [],
  'unresolved — answer connections are images, not available in the text layer.',
  [],
  'unresolved — answer connections are images, not available in the text layer.',
  True,
  False),
 ('1.4.2',
  4,
  'Excretion',
  'Short Answer',
  'Name TWO excretory organs, other than the kidneys, found in the body and what substance they excrete. (4)',
  False,
  [],
  'Lungs- CO2 Large intestine/ colon- faeces Skin- sweat ✓✓✓✓ (any 2 x 2=4)',
  ['Lungs- CO2 Large intestine/ colon- faeces Skin- sweat', '(any 2 x 2=4)'],
  'Lungs- CO2 Large intestine/ colon- faeces Skin- sweat ✓✓✓✓ (any 2 x 2=4)',
  False,
  False),
 ('1.4.3',
  3,
  'Excretion',
  'Short Answer',
  'The kidneys filter blood and produce a liquid known as urine. Name three substances found in urine. (3) 1- 2- '
  '3-',
  False,
  [],
  'Water Urea Uric acid Creatinine Salts ✓✓✓ (any 3)',
  ['Water Urea Uric acid Creatinine Salts', '(any 3)'],
  'Water Urea Uric acid Creatinine Salts ✓✓✓ (any 3)',
  False,
  False),
 ('1.4.4.A',
  3,
  'Excretion',
  'Labelling/Diagram',
  'Name structures P, Q and R. (3) P- Q- R-',
  True,
  [],
  'P- renal artery ✓ Q- Bladder ✓ R- Ureter ✓ (3)',
  ['P- renal artery', 'Q- Bladder', 'R- Ureter'],
  'P- renal artery ✓ Q- Bladder ✓ R- Ureter ✓ (3)',
  True,
  False),
 ('1.4.4.B',
  5,
  'Excretion',
  'Data/Graph Interpretation',
  'Tabulate two differences between the blood found in vessel A and vessel B. (5) A B',
  True,
  [],
  'Table showing the difference in blood between vessel A and B/ inferior vena cava and aorta ✓ Differences: - A '
  'carries blood high in CO2 and B carries blood low in CO2 - A carries blood low in O2 and B carries blood high '
  'in O2 - A carries purified blood and B carries unfiltered blood any 2 x 2 ✓✓✓✓ -1 Table incomplete (5) ✓ ✓',
  ['Table showing the difference in blood between vessel A and B/ inferior vena cava and aorta',
   'Differences: - A carries blood high in CO2 and B carries blood low in CO2 - A carries blood low in O2 and B '
   'carries blood high in O2 - A carries purified blood and B carries unfiltered blood any 2 x 2',
   '-1 Table incomplete (5)'],
  'Table showing the difference in blood between vessel A and B/ inferior vena cava and aorta ✓ Differences: - A '
  'carries blood high in CO2 and B carries blood low in CO2 - A carries blood low in O2 and B carries blood high '
  'in O2 - A carries purified blood and B carries unfiltered blood any 2 x 2 ✓✓✓✓ -1 Table incomplete (5) ✓ ✓',
  True,
  False),
 ('1.4.5',
  3,
  'Excretion',
  'Short Answer',
  'The volume and concentration of urine produced is affected by changes in water consumption, temperature and '
  'exercise levels. The table below shows three different conditions. Complete the table by writing increases or '
  'decreases in the spaces to show the effect of each condition on the volume and concentration of urine '
  'produced. (3) Condition Volume of urine Concentration of urine Increase in water consumption Increase in '
  'temperature Increase in exercise level',
  False,
  [],
  'Increase in water consumption: Increases / Decreases ✓ (both correct). Increase in temperature: Decreases / '
  'Increases ✓ (both correct). Increase in exercise level: Decreases / Increases ✓ (both correct). (3)',
  ['Increase in water consumption: Increases / Decreases',
   '(both correct). Increase in temperature: Decreases / Increases',
   '(both correct). Increase in exercise level: Decreases / Increases',
   '(both correct). (3)'],
  'Increase in water consumption: Increases / Decreases ✓ (both correct). Increase in temperature: Decreases / '
  'Increases ✓ (both correct). Increase in exercise level: Decreases / Increases ✓ (both correct). (3)',
  False,
  False),
 ('1.5',
  6,
  'Skeletal system',
  'Labelling/Diagram',
  'In the word box below are the names of six different bones. Label the bones on the diagram of skeleton. '
  'Cranium Clavicle Radius Femur Sacrum Tarsals',
  True,
  [],
  'Cranium ✓ Clavicle ✓ radius ✓ sacrum ✓ femur ✓ tarsals ✓; placements unresolved — inspect diagram.',
  ['Cranium', 'Clavicle', 'radius', 'sacrum', 'femur', 'tarsals', '; placements unresolved — inspect diagram.'],
  'Cranium ✓ Clavicle ✓ radius ✓ sacrum ✓ femur ✓ tarsals ✓; placements unresolved — inspect diagram.',
  True,
  False),
 ('2.1.1',
  2,
  'Excretion',
  'Definition/Terminology',
  'Define the term excretion. (2)',
  False,
  [],
  'The removal of harmful metabolic wastes from the body✓✓ (2)',
  ['The removal of harmful metabolic wastes from the body'],
  'The removal of harmful metabolic wastes from the body✓✓ (2)',
  False,
  False),
 ('2.1.2',
  1,
  'Excretion',
  'Data/Graph Interpretation',
  'In which part of the nephron does a similar process take place as illustrated by the kidney machine? (1)',
  True,
  [],
  'Renal corpuscle ✓ (1)',
  ['Renal corpuscle'],
  'Renal corpuscle ✓ (1)',
  True,
  False),
 ('2.1.3',
  4,
  'Excretion',
  'Short Answer',
  'Compare the composition of the dialysis fluid and the patient’s blood. (4)',
  False,
  [],
  'The dialysis fluid contains no waste substances✓/ no nitrogenous wastes/urea, uric acid, etc. whereas the '
  'patient’s blood does. ✓ The glucose, amino acids, salts and other blood constituents are in the same '
  'concentration in both the dialysis fluid and patient’s blood ✓✓ the fluid has a similar composition to plasma '
  '(4)',
  ['The dialysis fluid contains no waste substances',
   '/ no nitrogenous wastes/urea, uric acid, etc. whereas the patient’s blood does.',
   'The glucose, amino acids, salts and other blood constituents are in the same concentration in both the '
   'dialysis fluid and patient’s blood',
   'the fluid has a similar composition to plasma (4)'],
  'The dialysis fluid contains no waste substances✓/ no nitrogenous wastes/urea, uric acid, etc. whereas the '
  'patient’s blood does. ✓ The glucose, amino acids, salts and other blood constituents are in the same '
  'concentration in both the dialysis fluid and patient’s blood ✓✓ the fluid has a similar composition to plasma '
  '(4)',
  False,
  False),
 ('2.1.4',
  2,
  'Excretion',
  'Short Answer',
  'Give a reason for your answer to QUESTION 2.1.3. (2)',
  False,
  [],
  'A concentration gradient needs to be set up and maintained between the patient’s blood and dialysis fluid for '
  'waste substances✓ only so that these diffuse out of the blood into the dialysis solution. ✓ (2)',
  ['A concentration gradient needs to be set up and maintained between the patient’s blood and dialysis fluid for '
   'waste substances',
   'only so that these diffuse out of the blood into the dialysis solution.'],
  'A concentration gradient needs to be set up and maintained between the patient’s blood and dialysis fluid for '
  'waste substances✓ only so that these diffuse out of the blood into the dialysis solution. ✓ (2)',
  False,
  False),
 ('2.1.5',
  2,
  'Excretion',
  'Short Answer',
  'Explain why dialysis fluid is continually replaced. (2)',
  False,
  [],
  'As waste substances move into the fluid the concentration gradient becomes less and less. ✓ It is replaced to '
  'maintain the concentration gradient and ensure maximum diffusion of waste out of the blood. ✓ (2) 1 mark for '
  'sterilization- sterile fluid.',
  ['As waste substances move into the fluid the concentration gradient becomes less and less.',
   'It is replaced to maintain the concentration gradient and ensure maximum diffusion of waste out of the blood.',
   '(2) 1 mark for sterilization- sterile fluid.'],
  'As waste substances move into the fluid the concentration gradient becomes less and less. ✓ It is replaced to '
  'maintain the concentration gradient and ensure maximum diffusion of waste out of the blood. ✓ (2) 1 mark for '
  'sterilization- sterile fluid.',
  False,
  False),
 ('2.1.6',
  2,
  'Excretion',
  'Short Answer',
  'Explain the purpose of having so many tubes carrying blood through the dialyser. (2)',
  False,
  [],
  'Creates a large surface area✓ to ensure maximum absorption of waste✓ (2)',
  ['Creates a large surface area', 'to ensure maximum absorption of waste'],
  'Creates a large surface area✓ to ensure maximum absorption of waste✓ (2)',
  False,
  False),
 ('2.1.7',
  2,
  'Excretion',
  'Short Answer',
  'Provide two disadvantages of dialysis. (2)',
  False,
  [],
  'Time consuming Very expensive Hard to hold down a job Have to limit fluid intake Potassium and phosphates are '
  'not removed and can build up and become life-threatening May feel ill during treatment Anticoagulants are '
  'added which may lead to bleeding problems. ✓✓ (any 2)',
  ['Time consuming Very expensive Hard to hold down a job Have to limit fluid intake Potassium and phosphates are '
   'not removed and can build up and become life-threatening May feel ill during treatment Anticoagulants are '
   'added which may lead to bleeding problems.',
   '(any 2)'],
  'Time consuming Very expensive Hard to hold down a job Have to limit fluid intake Potassium and phosphates are '
  'not removed and can build up and become life-threatening May feel ill during treatment Anticoagulants are '
  'added which may lead to bleeding problems. ✓✓ (any 2)',
  False,
  False),
 ('2.1.8',
  1,
  'Excretion',
  'Definition/Terminology',
  'Dialysis is a short-term solution to kidney failure. What is the long-term solution? (1)',
  False,
  [],
  'Kidney transplant ✓ (1)',
  ['Kidney transplant'],
  'Kidney transplant ✓ (1)',
  False,
  False),
 ('2.2.1',
  1,
  'Excretion',
  'Labelling/Diagram',
  'Provide the name of the kidney unit seen in Figure A. (1)',
  True,
  [],
  'Nephron ✓ (1)',
  ['Nephron'],
  'Nephron ✓ (1)',
  True,
  False),
 ('2.2.2',
  1,
  'Excretion',
  'Data/Graph Interpretation',
  'Structure R is a branch of which main vessel? (1)',
  True,
  [],
  'Renal vein ✓ (accept inferior vena cava) (1)',
  ['Renal vein', '(accept inferior vena cava) (1)'],
  'Renal vein ✓ (accept inferior vena cava) (1)',
  True,
  False),
 ('2.2.3',
  1,
  'Excretion',
  'Labelling/Diagram',
  'Provide the name of structure P. (1)',
  True,
  [],
  'Glomerulus ✓ (1)',
  ['Glomerulus'],
  'Glomerulus ✓ (1)',
  True,
  False),
 ('2.2.4',
  2,
  'Excretion',
  'Data/Graph Interpretation',
  'In which region of the kidney would you find structure 1 and structure 3? (2) 1- 3-',
  True,
  [],
  '1- cortex ✓ 3- Medulla ✓ (2)',
  ['1- cortex', '3- Medulla'],
  '1- cortex ✓ 3- Medulla ✓ (2)',
  True,
  False),
 ('2.2.5',
  1,
  'Excretion',
  'Labelling/Diagram',
  'What is the name of region 2 where the cells in Figure B are found? (1)',
  True,
  [],
  'Proximal convoluted tubule ✓ (1)',
  ['Proximal convoluted tubule'],
  'Proximal convoluted tubule ✓ (1)',
  True,
  False),
 ('2.2.6',
  2,
  'Excretion',
  'Data/Graph Interpretation',
  'Explain why the cells in Figure B contain many mitochondria. (2)',
  True,
  [],
  'Most useful substances are reabsorbed by active transport✓ in the PCT. This requires a lot of energy ✓and '
  'therefore a lot of mitochondria (2)',
  ['Most useful substances are reabsorbed by active transport',
   'in the PCT. This requires a lot of energy',
   'and therefore a lot of mitochondria (2)'],
  'Most useful substances are reabsorbed by active transport✓ in the PCT. This requires a lot of energy ✓and '
  'therefore a lot of mitochondria (2)',
  True,
  False),
 ('2.2.7.a',
  2,
  'Excretion',
  'Data/Graph Interpretation',
  'Protein in blood plasma and region 1. (2)',
  True,
  [],
  'Protein is too big to be filtered out of the glomerulus and will therefore not be present in the filtrate '
  '(region 1) but will remain in the blood plasma ✓✓ (2)',
  ['Protein is too big to be filtered out of the glomerulus and will therefore not be present in the filtrate '
   '(region 1) but will remain in the blood plasma'],
  'Protein is too big to be filtered out of the glomerulus and will therefore not be present in the filtrate '
  '(region 1) but will remain in the blood plasma ✓✓ (2)',
  True,
  False),
 ('2.2.7.b',
  2,
  'Excretion',
  'Data/Graph Interpretation',
  'Glucose in region 1 and region 3. (2)',
  True,
  [],
  'Glucose is filtered out of the blood and is present in the filtrate (region 1) ✓ it is reabsorbed completely '
  'in the PCT ✓and will therefore not be present in the Loop of Henle (region 3) (2)',
  ['Glucose is filtered out of the blood and is present in the filtrate (region 1)',
   'it is reabsorbed completely in the PCT',
   'and will therefore not be present in the Loop of Henle (region 3) (2)'],
  'Glucose is filtered out of the blood and is present in the filtrate (region 1) ✓ it is reabsorbed completely '
  'in the PCT ✓and will therefore not be present in the Loop of Henle (region 3) (2)',
  True,
  False),
 ('2.2.7.c',
  2,
  'Excretion',
  'Data/Graph Interpretation',
  'Urea between region 1 and region 3. (2)',
  True,
  [],
  'Urea is actively secreted ✓ back into the kidney tubules from the blood ✓so region 3 will contain higher '
  'amounts (2)',
  ['Urea is actively secreted',
   'back into the kidney tubules from the blood',
   'so region 3 will contain higher amounts (2)'],
  'Urea is actively secreted ✓ back into the kidney tubules from the blood ✓so region 3 will contain higher '
  'amounts (2)',
  True,
  False),
 ('3.1.1',
  3,
  'Skeletal system',
  'Labelling/Diagram',
  'Identify bones B, C and D. (3) B- C- D-',
  True,
  [],
  'B- radium ✓ C- ulna ✓ D- humerus ✓ (3)',
  ['B- radium', 'C- ulna', 'D- humerus'],
  'B- radium ✓ C- ulna ✓ D- humerus ✓ (3)',
  True,
  False),
 ('3.1.2',
  2,
  'Skeletal system',
  'Labelling/Diagram',
  'Name structure A and provide it’s function. (2)',
  True,
  [],
  'Tendon ✓ Attaches muscle to bone to bring about movement ✓ (2)',
  ['Tendon', 'Attaches muscle to bone to bring about movement'],
  'Tendon ✓ Attaches muscle to bone to bring about movement ✓ (2)',
  True,
  False),
 ('3.1.3',
  2,
  'Skeletal system',
  'Data/Graph Interpretation',
  'Explain the treatment necessary if structure A were to rupture. (2)',
  True,
  [],
  'Surgery to repair and reattach the tendon ✓ Then a cast/sling to immobilize the joint ✓ (2)',
  ['Surgery to repair and reattach the tendon', 'Then a cast/sling to immobilize the joint'],
  'Surgery to repair and reattach the tendon ✓ Then a cast/sling to immobilize the joint ✓ (2)',
  True,
  False),
 ('3.1.4',
  7,
  'Skeletal system',
  'Labelling/Diagram',
  'Joint 1 and 2 are both types of synovial joints. In the space on the next page tabulate the difference between '
  'them by comparing the following: (7) - Name of synovial joint - Type of movement allowed - Where it is found '
  'in the body (other than in the diagram above) A Biceps B C D',
  True,
  [],
  'A table comparing various characteristics of two synovial joints ✓. 1: Ball and socket ✓; Most flexible- '
  'allows for movement in many directions ✓; Hip/ between femur and pelvis ✓. 2: Hinge ✓; Allows for movement up '
  'and down ✓ (NOT side to side); e.g. phalanges, knee, ankle ✓. (7)',
  ['A table comparing various characteristics of two synovial joints',
   '. 1: Ball and socket',
   '; Most flexible- allows for movement in many directions',
   '; Hip/ between femur and pelvis',
   '. 2: Hinge',
   '; Allows for movement up and down',
   '(NOT side to side); e.g. phalanges, knee, ankle',
   '. (7)'],
  'A table comparing various characteristics of two synovial joints ✓. 1: Ball and socket ✓; Most flexible- '
  'allows for movement in many directions ✓; Hip/ between femur and pelvis ✓. 2: Hinge ✓; Allows for movement up '
  'and down ✓ (NOT side to side); e.g. phalanges, knee, ankle ✓. (7)',
  True,
  False),
 ('3.1.5.A',
  1,
  'Skeletal system',
  'Short Answer',
  'bowing of the legs:',
  False,
  [],
  'Rickets ✓',
  ['Rickets'],
  'Rickets ✓',
  False,
  False),
 ('3.1.5.B',
  1,
  'Skeletal system',
  'Short Answer',
  'weak and brittle bones:',
  False,
  [],
  'Osteoporosis ✓',
  ['Osteoporosis'],
  'Osteoporosis ✓',
  False,
  False),
 ('3.1.5.C',
  1,
  'Skeletal system',
  'Short Answer',
  'inflammation and pain at the joints: (3)',
  False,
  [],
  'Arthritis/ rheumatoid arthritis ✓ (3)',
  ['Arthritis/ rheumatoid arthritis'],
  'Arthritis/ rheumatoid arthritis ✓ (3)',
  False,
  False),
 ('3.2.1',
  2,
  'Skeletal system',
  'Definition/Terminology',
  'What is rheumatoid arthritis? (2)',
  False,
  [],
  'a chronic, inflammatory disorder in which your immune system mistakenly attacks the lining of membrane that '
  'surrounds your joints. ✓✓ (2)',
  ['a chronic, inflammatory disorder in which your immune system mistakenly attacks the lining of membrane that '
   'surrounds your joints.'],
  'a chronic, inflammatory disorder in which your immune system mistakenly attacks the lining of membrane that '
  'surrounds your joints. ✓✓ (2)',
  False,
  False),
 ('3.2.2',
  2,
  'Skeletal system',
  'Short Answer',
  'According to Dr. Sachs, what causes the deformities in the feet of a rheumatoid arthritis sufferer? (2)',
  False,
  [],
  'The ligaments and surrounding soft tissue are affected ✓and the joints weaken. ✓ Deformities then occur. (2)',
  ['The ligaments and surrounding soft tissue are affected',
   'and the joints weaken.',
   'Deformities then occur. (2)'],
  'The ligaments and surrounding soft tissue are affected ✓and the joints weaken. ✓ Deformities then occur. (2)',
  False,
  False),
 ('3.2.3',
  1,
  'Skeletal system',
  'Definition/Terminology',
  'What is the “excess joint fluid” referred to in paragraph 2 better known as? (1)',
  False,
  [],
  'Synovial fluid ✓ (1)',
  ['Synovial fluid'],
  'Synovial fluid ✓ (1)',
  False,
  False),
 ('3.2.4',
  2,
  'Skeletal system',
  'Short Answer',
  'Explain the findings (paragraph 3) in the study that compared foot problems in RA patients and patients '
  'without arthritis. (2)',
  False,
  [],
  '98% of RA patients experienced foot pain whereas only 76% of patients without arthritis had foot pain ✓ 96% of '
  'RA patients reported difficulty in function and 66% without arthritis had function difficulties ✓ (2)',
  ['98% of RA patients experienced foot pain whereas only 76% of patients without arthritis had foot pain',
   '96% of RA patients reported difficulty in function and 66% without arthritis had function difficulties'],
  '98% of RA patients experienced foot pain whereas only 76% of patients without arthritis had foot pain ✓ 96% of '
  'RA patients reported difficulty in function and 66% without arthritis had function difficulties ✓ (2)',
  False,
  False),
 ('3.2.5',
  2,
  'Skeletal system',
  'Short Answer',
  'Name TWO fixed variables that the investigation would have had to adhere to. (2)',
  False,
  [],
  'Same gender Same age group Same length of time having RA Same kind of RA Same number of patients in each group '
  '✓✓ (any 2)',
  ['Same gender Same age group Same length of time having RA Same kind of RA Same number of patients in each '
   'group',
   '(any 2)'],
  'Same gender Same age group Same length of time having RA Same kind of RA Same number of patients in each group '
  '✓✓ (any 2)',
  False,
  False),
 ('3.2.6',
  2,
  'Skeletal system',
  'Short Answer',
  'One of the foot problems caused by RA is a bunion. Describe what a bunion is. (2)',
  False,
  [],
  'An enlarged bursa at the base of the big toe✓. The joint becomes thickened, bent and often inflamed. ✓ OR A '
  'bony bump that forms on the joint at the base of your big toe. ✓ Occurs when some of the bones in the front '
  'part of your toe move out of place✓ (2)',
  ['An enlarged bursa at the base of the big toe',
   '. The joint becomes thickened, bent and often inflamed.',
   'OR A bony bump that forms on the joint at the base of your big toe.',
   'Occurs when some of the bones in the front part of your toe move out of place'],
  'An enlarged bursa at the base of the big toe✓. The joint becomes thickened, bent and often inflamed. ✓ OR A '
  'bony bump that forms on the joint at the base of your big toe. ✓ Occurs when some of the bones in the front '
  'part of your toe move out of place✓ (2)',
  False,
  False),
 ('3.2.7',
  2,
  'Skeletal system',
  'Definition/Terminology',
  'What is osteoarthritis? (2)',
  False,
  [],
  'Cartilage that cushions the ends of bones in joints softens and wears away✓. Bones rub against one another '
  'causing pain and stiffness. ✓ (2)',
  ['Cartilage that cushions the ends of bones in joints softens and wears away',
   '. Bones rub against one another causing pain and stiffness.'],
  'Cartilage that cushions the ends of bones in joints softens and wears away✓. Bones rub against one another '
  'causing pain and stiffness. ✓ (2)',
  False,
  False),
 ('4.1.1',
  1,
  'Microorganisms',
  'Short Answer',
  'Which substance will be destroyed if you were to cook the garlic and then to consume it? (1)',
  False,
  [],
  'Alicin ✓ (1)',
  ['Alicin'],
  'Alicin ✓ (1)',
  False,
  False),
 ('4.1.2.a',
  1,
  'Microorganisms',
  'Short Answer',
  'The independent variable:',
  False,
  [],
  'Contents of the test tube ✓',
  ['Contents of the test tube'],
  'Contents of the test tube ✓',
  False,
  False),
 ('4.1.2.b',
  1,
  'Microorganisms',
  'Short Answer',
  'The dependent variable:',
  False,
  [],
  'Diameter/ growth of bacteria colony ✓',
  ['Diameter/ growth of bacteria colony'],
  'Diameter/ growth of bacteria colony ✓',
  False,
  False),
 ('4.1.2.c',
  2,
  'Microorganisms',
  'Short Answer',
  'Two fixed variables:',
  False,
  [],
  'same amount of milk; same time/period to do the investigation; same environmental conditions/temperature ✓✓ '
  '(any 2) (4)',
  ['same amount of milk; same time/period to do the investigation; same environmental conditions/temperature',
   '(any 2) (4)'],
  'same amount of milk; same time/period to do the investigation; same environmental conditions/temperature ✓✓ '
  '(any 2) (4)',
  False,
  False),
 ('4.1.3',
  2,
  'Microorganisms',
  'Short Answer',
  'Why were the petri dishes kept in the fridge before the start of the investigation? (2)',
  False,
  [],
  'To avoid the growth of bacteria✓ before the start of the experiment as most bacteria do not grow in cold '
  'conditions. ✓ (2)',
  ['To avoid the growth of bacteria',
   'before the start of the experiment as most bacteria do not grow in cold conditions.'],
  'To avoid the growth of bacteria✓ before the start of the experiment as most bacteria do not grow in cold '
  'conditions. ✓ (2)',
  False,
  False),
 ('4.1.4.A',
  2,
  'Microorganisms',
  'Short Answer',
  'Petri dish A: (2) ',
  False,
  [],
  'Petri dish A: there was very little bacterial growth✓ as no E.coli was added to the sample. The already '
  'existing bacteria on the agar is the growth that is seen. ✓ (2) ',
  ['Petri dish A: there was very little bacterial growth',
   'as no E.coli was added to the sample. The already existing bacteria on the agar is the growth that is seen.'],
  'Petri dish A: there was very little bacterial growth✓ as no E.coli was added to the sample. The already '
  'existing bacteria on the agar is the growth that is seen. ✓ (2) ',
  False,
  False),
 ('4.1.4.C',
  2,
  'Microorganisms',
  'Short Answer',
  'Petri dish C: (2)',
  False,
  [],
  'Petri dish C: The E.coli specimen and garlic extract did not show any signs of bacterial growth. ✓ The alicin/ '
  'antimicrobial substance in the garlic extract destroyed the bacteria. ✓ Hence there was no growth in C. (2)',
  ['Petri dish C: The E.coli specimen and garlic extract did not show any signs of bacterial growth.',
   'The alicin/ antimicrobial substance in the garlic extract destroyed the bacteria.',
   'Hence there was no growth in C. (2)'],
  'Petri dish C: The E.coli specimen and garlic extract did not show any signs of bacterial growth. ✓ The alicin/ '
  'antimicrobial substance in the garlic extract destroyed the bacteria. ✓ Hence there was no growth in C. (2)',
  False,
  False),
 ('4.1.5',
  1,
  'Microorganisms',
  'Definition/Terminology',
  'What is the function of the agar when culturing/growing bacteria? (1)',
  False,
  [],
  'It is a medium/ source of nutrition for microorganisms ✓ (1)',
  ['It is a medium/ source of nutrition for microorganisms'],
  'It is a medium/ source of nutrition for microorganisms ✓ (1)',
  False,
  False),
 ('4.1.6',
  2,
  'Microorganisms',
  'Short Answer',
  'Can garlic be considered an antibiotic? Give a reason for your answer. (2)',
  False,
  [],
  'No. ✓ Antibiotics are only effective against bacteria. Garlic is partially effective against bacteria and '
  'viruses. ✓ (2)',
  ['No.',
   'Antibiotics are only effective against bacteria. Garlic is partially effective against bacteria and viruses.'],
  'No. ✓ Antibiotics are only effective against bacteria. Garlic is partially effective against bacteria and '
  'viruses. ✓ (2)',
  False,
  False),
 ('4.1.7',
  5,
  'Microorganisms',
  'Labelling/Diagram',
  'In the space on the next page draw a labelled diagram of a bacterium. (5)',
  True,
  [],
  'Heading ✓ Accuracy and diagram rules ✓ Any 3 labels ✓✓✓ (5)',
  ['Heading', 'Accuracy and diagram rules', 'Any 3 labels'],
  'Heading ✓ Accuracy and diagram rules ✓ Any 3 labels ✓✓✓ (5)',
  True,
  False),
 ('4.2.1',
  1,
  'Microorganisms',
  'Definition/Terminology',
  'What is meant by a mutualistic relationship? (1)',
  False,
  [],
  'A relationship/ association between two organisms, where both benefit. ✓ (1)',
  ['A relationship/ association between two organisms, where both benefit.'],
  'A relationship/ association between two organisms, where both benefit. ✓ (1)',
  False,
  False),
 ('4.2.2',
  2,
  'Microorganisms',
  'Short Answer',
  'Describe the mutualistic relationship between the fungus and the plants. (2)',
  False,
  [],
  'The hyphae of the fungus increase the absorptive surface of the plant’s roots ✓/ allow the plant to absorb '
  'water, phosphorous and other minerals from the soil. The plant provides the fungus with carbohydrates ✓ (2)',
  ['The hyphae of the fungus increase the absorptive surface of the plant’s roots',
   '/ allow the plant to absorb water, phosphorous and other minerals from the soil. The plant provides the '
   'fungus with carbohydrates'],
  'The hyphae of the fungus increase the absorptive surface of the plant’s roots ✓/ allow the plant to absorb '
  'water, phosphorous and other minerals from the soil. The plant provides the fungus with carbohydrates ✓ (2)',
  False,
  False),
 ('4.2.3',
  1,
  'Microorganisms',
  'Short Answer',
  'Describe ONE way in which the scientists ensured that the results of this investigation are valid. (1)',
  False,
  [],
  'Same type of soil was used All other factors were kept the same ✓ (any 1)',
  ['Same type of soil was used All other factors were kept the same', '(any 1)'],
  'Same type of soil was used All other factors were kept the same ✓ (any 1)',
  False,
  False),
 ('4.2.4',
  3,
  'Microorganisms',
  'Short Answer',
  'Explain why the plants grown in sterilised soil grew much slower than plants grown in non- sterilised soil. '
  '(3)',
  False,
  [],
  'Sterilizing the soil killed the fungi ✓ meaning that there were no mycorrhizal hyphae ✓ to increase the '
  'absorptive surface of the plant’s roots. ✓ The plant could not get sufficient water, phosphorous and other '
  'mineral ions from the soil, ✓ resulting in slow growth. (any 3)',
  ['Sterilizing the soil killed the fungi',
   'meaning that there were no mycorrhizal hyphae',
   'to increase the absorptive surface of the plant’s roots.',
   'The plant could not get sufficient water, phosphorous and other mineral ions from the soil,',
   'resulting in slow growth. (any 3)'],
  'Sterilizing the soil killed the fungi ✓ meaning that there were no mycorrhizal hyphae ✓ to increase the '
  'absorptive surface of the plant’s roots. ✓ The plant could not get sufficient water, phosphorous and other '
  'mineral ions from the soil, ✓ resulting in slow growth. (any 3)',
  False,
  False),
 ('4.2.5',
  2,
  'Microorganisms',
  'Short Answer',
  'What conclusion can be drawn from the results of this experiment? (2)',
  False,
  [],
  'Mycorrhizal fungi encourage plant growth as can be seen in plants grown in non-sterilised soil. ✓✓ (2)',
  ['Mycorrhizal fungi encourage plant growth as can be seen in plants grown in non-sterilised soil.'],
  'Mycorrhizal fungi encourage plant growth as can be seen in plants grown in non-sterilised soil. ✓✓ (2)',
  False,
  False),
 ('4.2.6',
  2,
  'Microorganisms',
  'Short Answer',
  'Name AND explain one other type of symbiotic relationship. (2)',
  False,
  [],
  'Parasitism- one organism benefits and the other is harmed. ✓✓ OR Commensalism- one organism benefits and the '
  'other is unchanged/ unaffected ✓✓ (2)',
  ['Parasitism- one organism benefits and the other is harmed.',
   'OR Commensalism- one organism benefits and the other is unchanged/ unaffected'],
  'Parasitism- one organism benefits and the other is harmed. ✓✓ OR Commensalism- one organism benefits and the '
  'other is unchanged/ unaffected ✓✓ (2)',
  False,
  False)]

SOURCE_HASHES = {'paper_path': 'b6fcfaaade034a73926972f247cbbed7357a8224b1c73ce1aec05c4a38f9feff',
 'memo_path': 'd7c388d0dc2523e6a159c566bf12101ee8b02b5271f83b02e9ad29139568996f'}

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
           'question_stem_text': ' HIV is a pathogen that can cause AIDS. The table below shows the adult '
                                 'population size of a country and the estimated number of people infected with '
                                 'HIV/AIDS in that country in 2016. Data for six countries are shown. Country '
                                 'Adult population size Estimated number of adults infected with HIV/AIDS A 808 '
                                 '824 220 000 B 248 490 8 200 C 221 000 221 D 3 250 000 130 000 E 5 111 111 46 '
                                 '000 F 1 333 333 48 000',
           'parent_question_number': '1.3'},
 '1.3.2': {'page': 5,
           'memo_page': 2,
           'question_stem_text': ' HIV is a pathogen that can cause AIDS. The table below shows the adult '
                                 'population size of a country and the estimated number of people infected with '
                                 'HIV/AIDS in that country in 2016. Data for six countries are shown. Country '
                                 'Adult population size Estimated number of adults infected with HIV/AIDS A 808 '
                                 '824 220 000 B 248 490 8 200 C 221 000 221 D 3 250 000 130 000 E 5 111 111 46 '
                                 '000 F 1 333 333 48 000',
           'parent_question_number': '1.3'},
 '1.3.3': {'page': 6,
           'memo_page': 2,
           'question_stem_text': ' HIV is a pathogen that can cause AIDS. The table below shows the adult '
                                 'population size of a country and the estimated number of people infected with '
                                 'HIV/AIDS in that country in 2016. Data for six countries are shown. Country '
                                 'Adult population size Estimated number of adults infected with HIV/AIDS A 808 '
                                 '824 220 000 B 248 490 8 200 C 221 000 221 D 3 250 000 130 000 E 5 111 111 46 '
                                 '000 F 1 333 333 48 000',
           'parent_question_number': '1.3'},
 '1.3.4': {'page': 6,
           'memo_page': 2,
           'question_stem_text': ' HIV is a pathogen that can cause AIDS. The table below shows the adult '
                                 'population size of a country and the estimated number of people infected with '
                                 'HIV/AIDS in that country in 2016. Data for six countries are shown. Country '
                                 'Adult population size Estimated number of adults infected with HIV/AIDS A 808 '
                                 '824 220 000 B 248 490 8 200 C 221 000 221 D 3 250 000 130 000 E 5 111 111 46 '
                                 '000 F 1 333 333 48 000',
           'parent_question_number': '1.3'},
 '1.3.5': {'page': 6,
           'memo_page': 2,
           'question_stem_text': ' HIV is a pathogen that can cause AIDS. The table below shows the adult '
                                 'population size of a country and the estimated number of people infected with '
                                 'HIV/AIDS in that country in 2016. Data for six countries are shown. Country '
                                 'Adult population size Estimated number of adults infected with HIV/AIDS A 808 '
                                 '824 220 000 B 248 490 8 200 C 221 000 221 D 3 250 000 130 000 E 5 111 111 46 '
                                 '000 F 1 333 333 48 000',
           'parent_question_number': '1.3'},
 '1.4.1': {'page': 7, 'memo_page': 3, 'question_stem_text': ' ', 'parent_question_number': '1.4'},
 '1.4.2': {'page': 7, 'memo_page': 3, 'question_stem_text': ' ', 'parent_question_number': '1.4'},
 '1.4.3': {'page': 7, 'memo_page': 3, 'question_stem_text': ' ', 'parent_question_number': '1.4'},
 '1.4.5': {'page': 9, 'memo_page': 4, 'question_stem_text': ' ', 'parent_question_number': '1.4'},
 '1.5': {'page': 9, 'memo_page': 4, 'question_stem_text': None, 'parent_question_number': '1'},
 '2.1.1': {'page': 10,
           'memo_page': 5,
           'question_stem_text': ' If a person’s kidneys happen to get damaged or do not function correctly a '
                                 'person can be placed on a dialysis machine to help the functioning of the '
                                 'kidneys.',
           'parent_question_number': '2.1'},
 '2.1.2': {'page': 10,
           'memo_page': 5,
           'question_stem_text': ' If a person’s kidneys happen to get damaged or do not function correctly a '
                                 'person can be placed on a dialysis machine to help the functioning of the '
                                 'kidneys.',
           'parent_question_number': '2.1'},
 '2.1.3': {'page': 10,
           'memo_page': 5,
           'question_stem_text': ' If a person’s kidneys happen to get damaged or do not function correctly a '
                                 'person can be placed on a dialysis machine to help the functioning of the '
                                 'kidneys.',
           'parent_question_number': '2.1'},
 '2.1.4': {'page': 11,
           'memo_page': 5,
           'question_stem_text': ' If a person’s kidneys happen to get damaged or do not function correctly a '
                                 'person can be placed on a dialysis machine to help the functioning of the '
                                 'kidneys.',
           'parent_question_number': '2.1'},
 '2.1.5': {'page': 11,
           'memo_page': 5,
           'question_stem_text': ' If a person’s kidneys happen to get damaged or do not function correctly a '
                                 'person can be placed on a dialysis machine to help the functioning of the '
                                 'kidneys.',
           'parent_question_number': '2.1'},
 '2.1.6': {'page': 11,
           'memo_page': 5,
           'question_stem_text': ' If a person’s kidneys happen to get damaged or do not function correctly a '
                                 'person can be placed on a dialysis machine to help the functioning of the '
                                 'kidneys.',
           'parent_question_number': '2.1'},
 '2.1.7': {'page': 11,
           'memo_page': 5,
           'question_stem_text': ' If a person’s kidneys happen to get damaged or do not function correctly a '
                                 'person can be placed on a dialysis machine to help the functioning of the '
                                 'kidneys.',
           'parent_question_number': '2.1'},
 '2.1.8': {'page': 11,
           'memo_page': 5,
           'question_stem_text': ' If a person’s kidneys happen to get damaged or do not function correctly a '
                                 'person can be placed on a dialysis machine to help the functioning of the '
                                 'kidneys.',
           'parent_question_number': '2.1'},
 '2.2.1': {'page': 12,
           'memo_page': 6,
           'question_stem_text': ' Figure A is a diagram of a filtration unit of the kidney. The arrows show the '
                                 'direction of blood flow. Figure B is a drawing of a vertical section through a '
                                 'cell from the lining of region 2 of diagram A. Figure A Figure B',
           'parent_question_number': '2.2'},
 '2.2.2': {'page': 12,
           'memo_page': 6,
           'question_stem_text': ' Figure A is a diagram of a filtration unit of the kidney. The arrows show the '
                                 'direction of blood flow. Figure B is a drawing of a vertical section through a '
                                 'cell from the lining of region 2 of diagram A. Figure A Figure B',
           'parent_question_number': '2.2'},
 '2.2.3': {'page': 12,
           'memo_page': 6,
           'question_stem_text': ' Figure A is a diagram of a filtration unit of the kidney. The arrows show the '
                                 'direction of blood flow. Figure B is a drawing of a vertical section through a '
                                 'cell from the lining of region 2 of diagram A. Figure A Figure B',
           'parent_question_number': '2.2'},
 '2.2.4': {'page': 12,
           'memo_page': 6,
           'question_stem_text': ' Figure A is a diagram of a filtration unit of the kidney. The arrows show the '
                                 'direction of blood flow. Figure B is a drawing of a vertical section through a '
                                 'cell from the lining of region 2 of diagram A. Figure A Figure B',
           'parent_question_number': '2.2'},
 '2.2.5': {'page': 12,
           'memo_page': 6,
           'question_stem_text': ' Figure A is a diagram of a filtration unit of the kidney. The arrows show the '
                                 'direction of blood flow. Figure B is a drawing of a vertical section through a '
                                 'cell from the lining of region 2 of diagram A. Figure A Figure B',
           'parent_question_number': '2.2'},
 '2.2.6': {'page': 13,
           'memo_page': 6,
           'question_stem_text': ' Figure A is a diagram of a filtration unit of the kidney. The arrows show the '
                                 'direction of blood flow. Figure B is a drawing of a vertical section through a '
                                 'cell from the lining of region 2 of diagram A. Figure A Figure B',
           'parent_question_number': '2.2'},
 '3.1.1': {'page': 14,
           'memo_page': 7,
           'question_stem_text': ' The diagram below shows the bones and muscles in the human arm.',
           'parent_question_number': '3.1'},
 '3.1.2': {'page': 14,
           'memo_page': 7,
           'question_stem_text': ' The diagram below shows the bones and muscles in the human arm.',
           'parent_question_number': '3.1'},
 '3.1.3': {'page': 14,
           'memo_page': 7,
           'question_stem_text': ' The diagram below shows the bones and muscles in the human arm.',
           'parent_question_number': '3.1'},
 '3.1.4': {'page': 14,
           'memo_page': 7,
           'question_stem_text': ' The diagram below shows the bones and muscles in the human arm.',
           'parent_question_number': '3.1'},
 '3.2.1': {'page': 17,
           'memo_page': 7,
           'question_stem_text': 'Shared source/context for 3.2.1: refer to July exam p1.pdf, pages [14, 15]. '
                                 'Extended passage/table is preserved in the original PDF.',
           'parent_question_number': '3.2'},
 '3.2.2': {'page': 17,
           'memo_page': 7,
           'question_stem_text': 'Shared source/context for 3.2.2: refer to July exam p1.pdf, pages [14, 15]. '
                                 'Extended passage/table is preserved in the original PDF.',
           'parent_question_number': '3.2'},
 '3.2.3': {'page': 17,
           'memo_page': 7,
           'question_stem_text': 'Shared source/context for 3.2.3: refer to July exam p1.pdf, pages [14, 15]. '
                                 'Extended passage/table is preserved in the original PDF.',
           'parent_question_number': '3.2'},
 '3.2.4': {'page': 17,
           'memo_page': 7,
           'question_stem_text': 'Shared source/context for 3.2.4: refer to July exam p1.pdf, pages [14, 15]. '
                                 'Extended passage/table is preserved in the original PDF.',
           'parent_question_number': '3.2'},
 '3.2.5': {'page': 17,
           'memo_page': 8,
           'question_stem_text': 'Shared source/context for 3.2.5: refer to July exam p1.pdf, pages [14, 15]. '
                                 'Extended passage/table is preserved in the original PDF.',
           'parent_question_number': '3.2'},
 '3.2.6': {'page': 17,
           'memo_page': 8,
           'question_stem_text': 'Shared source/context for 3.2.6: refer to July exam p1.pdf, pages [14, 15]. '
                                 'Extended passage/table is preserved in the original PDF.',
           'parent_question_number': '3.2'},
 '3.2.7': {'page': 17,
           'memo_page': 8,
           'question_stem_text': 'Shared source/context for 3.2.7: refer to July exam p1.pdf, pages [14, 15]. '
                                 'Extended passage/table is preserved in the original PDF.',
           'parent_question_number': '3.2'},
 '4.1.1': {'page': 18,
           'memo_page': 9,
           'question_stem_text': ' Garlic is known to have the ability to fight bacteria and viruses. It is known '
                                 'to be effective against a wide range of bacteria and can combat the common '
                                 'cold. The antimicrobial substance in garlic is called alicin. To maintain the '
                                 'antibacterial properties of garlic, it must be consumed or applied as raw '
                                 'garlic. Scientists wanted to investigate the effectiveness of garlic in killing '
                                 'bacteria. They conducted the experiment as follows: • They used three petri '
                                 'dishes prepared with blood agar and stored these in a refrigerator. • Before '
                                 'the start of the experiment, they removed the petri dishes from the '
                                 'refrigerator to allow them to reach room temperature. • They prepared three '
                                 'test specimens and labelled them as described below: o The three test tubes '
                                 'were labelled A, B and C. o The contents of the test tubes were measured and '
                                 'mixed as shown in the table below: Test tube Contents of the test tubes 100 mL '
                                 'milk 5 mL E.coli bacterium Garlic extract A ✓ x x B ✓ ✓ x C ✓ ✓ ✓ • They petri '
                                 'dishes were labelled A, B and C. • They removed the lid in petri dish A and '
                                 'used the syringe to extract 10 mL of the sample from test tube A and placed it '
                                 'in the center of petri dish A. • In the same way, using a new syringe a 10 mL '
                                 'sample was extracted from test tube B and placed in petri dish B and the '
                                 'procedure was repeated for petri dish C. • The petri dish lids were replaced, '
                                 'and the petri dishes were stored in a cool and shaded place. o The diameter of '
                                 'the E.coli colony was measured every day for 5 days and recorded in the table '
                                 'below: Petri dish Diameter of bacteria colony (mm) Day 1 Day 2 Day 3 Day 4 Day '
                                 '5 A 0 1,7 3,0 4,6 7,1 B 0 4,2 8.4 15,1 36,5 C 0 0 0 0 0',
           'parent_question_number': '4.1'},
 '4.1.3': {'page': 19,
           'memo_page': 9,
           'question_stem_text': ' Garlic is known to have the ability to fight bacteria and viruses. It is known '
                                 'to be effective against a wide range of bacteria and can combat the common '
                                 'cold. The antimicrobial substance in garlic is called alicin. To maintain the '
                                 'antibacterial properties of garlic, it must be consumed or applied as raw '
                                 'garlic. Scientists wanted to investigate the effectiveness of garlic in killing '
                                 'bacteria. They conducted the experiment as follows: • They used three petri '
                                 'dishes prepared with blood agar and stored these in a refrigerator. • Before '
                                 'the start of the experiment, they removed the petri dishes from the '
                                 'refrigerator to allow them to reach room temperature. • They prepared three '
                                 'test specimens and labelled them as described below: o The three test tubes '
                                 'were labelled A, B and C. o The contents of the test tubes were measured and '
                                 'mixed as shown in the table below: Test tube Contents of the test tubes 100 mL '
                                 'milk 5 mL E.coli bacterium Garlic extract A ✓ x x B ✓ ✓ x C ✓ ✓ ✓ • They petri '
                                 'dishes were labelled A, B and C. • They removed the lid in petri dish A and '
                                 'used the syringe to extract 10 mL of the sample from test tube A and placed it '
                                 'in the center of petri dish A. • In the same way, using a new syringe a 10 mL '
                                 'sample was extracted from test tube B and placed in petri dish B and the '
                                 'procedure was repeated for petri dish C. • The petri dish lids were replaced, '
                                 'and the petri dishes were stored in a cool and shaded place. o The diameter of '
                                 'the E.coli colony was measured every day for 5 days and recorded in the table '
                                 'below: Petri dish Diameter of bacteria colony (mm) Day 1 Day 2 Day 3 Day 4 Day '
                                 '5 A 0 1,7 3,0 4,6 7,1 B 0 4,2 8.4 15,1 36,5 C 0 0 0 0 0',
           'parent_question_number': '4.1'},
 '4.1.5': {'page': 19,
           'memo_page': 9,
           'question_stem_text': ' Garlic is known to have the ability to fight bacteria and viruses. It is known '
                                 'to be effective against a wide range of bacteria and can combat the common '
                                 'cold. The antimicrobial substance in garlic is called alicin. To maintain the '
                                 'antibacterial properties of garlic, it must be consumed or applied as raw '
                                 'garlic. Scientists wanted to investigate the effectiveness of garlic in killing '
                                 'bacteria. They conducted the experiment as follows: • They used three petri '
                                 'dishes prepared with blood agar and stored these in a refrigerator. • Before '
                                 'the start of the experiment, they removed the petri dishes from the '
                                 'refrigerator to allow them to reach room temperature. • They prepared three '
                                 'test specimens and labelled them as described below: o The three test tubes '
                                 'were labelled A, B and C. o The contents of the test tubes were measured and '
                                 'mixed as shown in the table below: Test tube Contents of the test tubes 100 mL '
                                 'milk 5 mL E.coli bacterium Garlic extract A ✓ x x B ✓ ✓ x C ✓ ✓ ✓ • They petri '
                                 'dishes were labelled A, B and C. • They removed the lid in petri dish A and '
                                 'used the syringe to extract 10 mL of the sample from test tube A and placed it '
                                 'in the center of petri dish A. • In the same way, using a new syringe a 10 mL '
                                 'sample was extracted from test tube B and placed in petri dish B and the '
                                 'procedure was repeated for petri dish C. • The petri dish lids were replaced, '
                                 'and the petri dishes were stored in a cool and shaded place. o The diameter of '
                                 'the E.coli colony was measured every day for 5 days and recorded in the table '
                                 'below: Petri dish Diameter of bacteria colony (mm) Day 1 Day 2 Day 3 Day 4 Day '
                                 '5 A 0 1,7 3,0 4,6 7,1 B 0 4,2 8.4 15,1 36,5 C 0 0 0 0 0',
           'parent_question_number': '4.1'},
 '4.1.6': {'page': 19,
           'memo_page': 9,
           'question_stem_text': ' Garlic is known to have the ability to fight bacteria and viruses. It is known '
                                 'to be effective against a wide range of bacteria and can combat the common '
                                 'cold. The antimicrobial substance in garlic is called alicin. To maintain the '
                                 'antibacterial properties of garlic, it must be consumed or applied as raw '
                                 'garlic. Scientists wanted to investigate the effectiveness of garlic in killing '
                                 'bacteria. They conducted the experiment as follows: • They used three petri '
                                 'dishes prepared with blood agar and stored these in a refrigerator. • Before '
                                 'the start of the experiment, they removed the petri dishes from the '
                                 'refrigerator to allow them to reach room temperature. • They prepared three '
                                 'test specimens and labelled them as described below: o The three test tubes '
                                 'were labelled A, B and C. o The contents of the test tubes were measured and '
                                 'mixed as shown in the table below: Test tube Contents of the test tubes 100 mL '
                                 'milk 5 mL E.coli bacterium Garlic extract A ✓ x x B ✓ ✓ x C ✓ ✓ ✓ • They petri '
                                 'dishes were labelled A, B and C. • They removed the lid in petri dish A and '
                                 'used the syringe to extract 10 mL of the sample from test tube A and placed it '
                                 'in the center of petri dish A. • In the same way, using a new syringe a 10 mL '
                                 'sample was extracted from test tube B and placed in petri dish B and the '
                                 'procedure was repeated for petri dish C. • The petri dish lids were replaced, '
                                 'and the petri dishes were stored in a cool and shaded place. o The diameter of '
                                 'the E.coli colony was measured every day for 5 days and recorded in the table '
                                 'below: Petri dish Diameter of bacteria colony (mm) Day 1 Day 2 Day 3 Day 4 Day '
                                 '5 A 0 1,7 3,0 4,6 7,1 B 0 4,2 8.4 15,1 36,5 C 0 0 0 0 0',
           'parent_question_number': '4.1'},
 '4.1.7': {'page': 19,
           'memo_page': 9,
           'question_stem_text': ' Garlic is known to have the ability to fight bacteria and viruses. It is known '
                                 'to be effective against a wide range of bacteria and can combat the common '
                                 'cold. The antimicrobial substance in garlic is called alicin. To maintain the '
                                 'antibacterial properties of garlic, it must be consumed or applied as raw '
                                 'garlic. Scientists wanted to investigate the effectiveness of garlic in killing '
                                 'bacteria. They conducted the experiment as follows: • They used three petri '
                                 'dishes prepared with blood agar and stored these in a refrigerator. • Before '
                                 'the start of the experiment, they removed the petri dishes from the '
                                 'refrigerator to allow them to reach room temperature. • They prepared three '
                                 'test specimens and labelled them as described below: o The three test tubes '
                                 'were labelled A, B and C. o The contents of the test tubes were measured and '
                                 'mixed as shown in the table below: Test tube Contents of the test tubes 100 mL '
                                 'milk 5 mL E.coli bacterium Garlic extract A ✓ x x B ✓ ✓ x C ✓ ✓ ✓ • They petri '
                                 'dishes were labelled A, B and C. • They removed the lid in petri dish A and '
                                 'used the syringe to extract 10 mL of the sample from test tube A and placed it '
                                 'in the center of petri dish A. • In the same way, using a new syringe a 10 mL '
                                 'sample was extracted from test tube B and placed in petri dish B and the '
                                 'procedure was repeated for petri dish C. • The petri dish lids were replaced, '
                                 'and the petri dishes were stored in a cool and shaded place. o The diameter of '
                                 'the E.coli colony was measured every day for 5 days and recorded in the table '
                                 'below: Petri dish Diameter of bacteria colony (mm) Day 1 Day 2 Day 3 Day 4 Day '
                                 '5 A 0 1,7 3,0 4,6 7,1 B 0 4,2 8.4 15,1 36,5 C 0 0 0 0 0',
           'parent_question_number': '4.1'},
 '4.2.1': {'page': 21,
           'memo_page': 10,
           'question_stem_text': ' A mycorrhiza is a mutualistic relationship between fungal hyphae and the roots '
                                 'of true plants. The hyphae increase the absorptive surface of the plant’s roots '
                                 'by aiding in the absorption of water, phosphorus and other mineral ions from '
                                 'the soil to the roots of plants. The plant is photosynthetic and provides the '
                                 'fungus with carbohydrates. Scientists conducted an experiment to determine the '
                                 'effect of mycorrhizal associations on plant growth. The experiment was '
                                 'conducted as follow: • Two groups of plants were grown. • One group was planted '
                                 'in soil that had been sterilised (free from living microorganisms). • The other '
                                 'group was planted in the same type of soil but the soil had not been '
                                 'sterilised. • All other factors remained the same between the two groups. • The '
                                 'plants were allowed to grow for 8 week. • Each week, the height (in '
                                 'centimeters) of each plant was measured. The table below shows the growth of '
                                 'the plants over the 8-week period. Week Height of plants grown in sterilised '
                                 'soil (cm) Height of plants grown in non-sterilised soil (cm) 1 0,8 2,0 2 1,5 '
                                 '5,5 3 2,0 8,7 4 2,3 10,0 5 2,4 12,0 6 3,8 16,2 7 5,0 19,1 8 6,0 25,0',
           'parent_question_number': '4.2'},
 '4.2.2': {'page': 21,
           'memo_page': 10,
           'question_stem_text': ' A mycorrhiza is a mutualistic relationship between fungal hyphae and the roots '
                                 'of true plants. The hyphae increase the absorptive surface of the plant’s roots '
                                 'by aiding in the absorption of water, phosphorus and other mineral ions from '
                                 'the soil to the roots of plants. The plant is photosynthetic and provides the '
                                 'fungus with carbohydrates. Scientists conducted an experiment to determine the '
                                 'effect of mycorrhizal associations on plant growth. The experiment was '
                                 'conducted as follow: • Two groups of plants were grown. • One group was planted '
                                 'in soil that had been sterilised (free from living microorganisms). • The other '
                                 'group was planted in the same type of soil but the soil had not been '
                                 'sterilised. • All other factors remained the same between the two groups. • The '
                                 'plants were allowed to grow for 8 week. • Each week, the height (in '
                                 'centimeters) of each plant was measured. The table below shows the growth of '
                                 'the plants over the 8-week period. Week Height of plants grown in sterilised '
                                 'soil (cm) Height of plants grown in non-sterilised soil (cm) 1 0,8 2,0 2 1,5 '
                                 '5,5 3 2,0 8,7 4 2,3 10,0 5 2,4 12,0 6 3,8 16,2 7 5,0 19,1 8 6,0 25,0',
           'parent_question_number': '4.2'},
 '4.2.3': {'page': 21,
           'memo_page': 10,
           'question_stem_text': ' A mycorrhiza is a mutualistic relationship between fungal hyphae and the roots '
                                 'of true plants. The hyphae increase the absorptive surface of the plant’s roots '
                                 'by aiding in the absorption of water, phosphorus and other mineral ions from '
                                 'the soil to the roots of plants. The plant is photosynthetic and provides the '
                                 'fungus with carbohydrates. Scientists conducted an experiment to determine the '
                                 'effect of mycorrhizal associations on plant growth. The experiment was '
                                 'conducted as follow: • Two groups of plants were grown. • One group was planted '
                                 'in soil that had been sterilised (free from living microorganisms). • The other '
                                 'group was planted in the same type of soil but the soil had not been '
                                 'sterilised. • All other factors remained the same between the two groups. • The '
                                 'plants were allowed to grow for 8 week. • Each week, the height (in '
                                 'centimeters) of each plant was measured. The table below shows the growth of '
                                 'the plants over the 8-week period. Week Height of plants grown in sterilised '
                                 'soil (cm) Height of plants grown in non-sterilised soil (cm) 1 0,8 2,0 2 1,5 '
                                 '5,5 3 2,0 8,7 4 2,3 10,0 5 2,4 12,0 6 3,8 16,2 7 5,0 19,1 8 6,0 25,0',
           'parent_question_number': '4.2'},
 '4.2.4': {'page': 21,
           'memo_page': 10,
           'question_stem_text': ' A mycorrhiza is a mutualistic relationship between fungal hyphae and the roots '
                                 'of true plants. The hyphae increase the absorptive surface of the plant’s roots '
                                 'by aiding in the absorption of water, phosphorus and other mineral ions from '
                                 'the soil to the roots of plants. The plant is photosynthetic and provides the '
                                 'fungus with carbohydrates. Scientists conducted an experiment to determine the '
                                 'effect of mycorrhizal associations on plant growth. The experiment was '
                                 'conducted as follow: • Two groups of plants were grown. • One group was planted '
                                 'in soil that had been sterilised (free from living microorganisms). • The other '
                                 'group was planted in the same type of soil but the soil had not been '
                                 'sterilised. • All other factors remained the same between the two groups. • The '
                                 'plants were allowed to grow for 8 week. • Each week, the height (in '
                                 'centimeters) of each plant was measured. The table below shows the growth of '
                                 'the plants over the 8-week period. Week Height of plants grown in sterilised '
                                 'soil (cm) Height of plants grown in non-sterilised soil (cm) 1 0,8 2,0 2 1,5 '
                                 '5,5 3 2,0 8,7 4 2,3 10,0 5 2,4 12,0 6 3,8 16,2 7 5,0 19,1 8 6,0 25,0',
           'parent_question_number': '4.2'},
 '4.2.5': {'page': 21,
           'memo_page': 10,
           'question_stem_text': ' A mycorrhiza is a mutualistic relationship between fungal hyphae and the roots '
                                 'of true plants. The hyphae increase the absorptive surface of the plant’s roots '
                                 'by aiding in the absorption of water, phosphorus and other mineral ions from '
                                 'the soil to the roots of plants. The plant is photosynthetic and provides the '
                                 'fungus with carbohydrates. Scientists conducted an experiment to determine the '
                                 'effect of mycorrhizal associations on plant growth. The experiment was '
                                 'conducted as follow: • Two groups of plants were grown. • One group was planted '
                                 'in soil that had been sterilised (free from living microorganisms). • The other '
                                 'group was planted in the same type of soil but the soil had not been '
                                 'sterilised. • All other factors remained the same between the two groups. • The '
                                 'plants were allowed to grow for 8 week. • Each week, the height (in '
                                 'centimeters) of each plant was measured. The table below shows the growth of '
                                 'the plants over the 8-week period. Week Height of plants grown in sterilised '
                                 'soil (cm) Height of plants grown in non-sterilised soil (cm) 1 0,8 2,0 2 1,5 '
                                 '5,5 3 2,0 8,7 4 2,3 10,0 5 2,4 12,0 6 3,8 16,2 7 5,0 19,1 8 6,0 25,0',
           'parent_question_number': '4.2'},
 '4.2.6': {'page': 21,
           'memo_page': 10,
           'question_stem_text': ' A mycorrhiza is a mutualistic relationship between fungal hyphae and the roots '
                                 'of true plants. The hyphae increase the absorptive surface of the plant’s roots '
                                 'by aiding in the absorption of water, phosphorus and other mineral ions from '
                                 'the soil to the roots of plants. The plant is photosynthetic and provides the '
                                 'fungus with carbohydrates. Scientists conducted an experiment to determine the '
                                 'effect of mycorrhizal associations on plant growth. The experiment was '
                                 'conducted as follow: • Two groups of plants were grown. • One group was planted '
                                 'in soil that had been sterilised (free from living microorganisms). • The other '
                                 'group was planted in the same type of soil but the soil had not been '
                                 'sterilised. • All other factors remained the same between the two groups. • The '
                                 'plants were allowed to grow for 8 week. • Each week, the height (in '
                                 'centimeters) of each plant was measured. The table below shows the growth of '
                                 'the plants over the 8-week period. Week Height of plants grown in sterilised '
                                 'soil (cm) Height of plants grown in non-sterilised soil (cm) 1 0,8 2,0 2 1,5 '
                                 '5,5 3 2,0 8,7 4 2,3 10,0 5 2,4 12,0 6 3,8 16,2 7 5,0 19,1 8 6,0 25,0',
           'parent_question_number': '4.2'},
 '1.4.4.A': {'page': 8,
             'memo_page': 3,
             'question_stem_text': '  Below is a diagram of part of the human excretory system and associated '
                                   'blood vessels. ',
             'parent_question_number': '1.4.4'},
 '1.4.4.B': {'page': 8,
             'memo_page': 3,
             'question_stem_text': '  Below is a diagram of part of the human excretory system and associated '
                                   'blood vessels. ',
             'parent_question_number': '1.4.4'},
 '2.2.7.a': {'page': 13,
             'memo_page': 6,
             'question_stem_text': ' Figure A is a diagram of a filtration unit of the kidney. The arrows show '
                                   'the direction of blood flow. Figure B is a drawing of a vertical section '
                                   'through a cell from the lining of region 2 of diagram A. Figure A Figure B '
                                   'Below are the concentrations of some substances in blood plasma and in the '
                                   'regions labelled 1 and 3 on Figure A. Substance Concentration/ mg per cm3 '
                                   'Blood plasma Region 1 Region 3 Protein 8000 0 0 Glucose 100 100 0 Salts 320 '
                                   '320 300 Urea 30 30 2000 Explain the difference in concentration of the '
                                   'following: ',
             'parent_question_number': '2.2.7'},
 '2.2.7.b': {'page': 13,
             'memo_page': 6,
             'question_stem_text': ' Figure A is a diagram of a filtration unit of the kidney. The arrows show '
                                   'the direction of blood flow. Figure B is a drawing of a vertical section '
                                   'through a cell from the lining of region 2 of diagram A. Figure A Figure B '
                                   'Below are the concentrations of some substances in blood plasma and in the '
                                   'regions labelled 1 and 3 on Figure A. Substance Concentration/ mg per cm3 '
                                   'Blood plasma Region 1 Region 3 Protein 8000 0 0 Glucose 100 100 0 Salts 320 '
                                   '320 300 Urea 30 30 2000 Explain the difference in concentration of the '
                                   'following: ',
             'parent_question_number': '2.2.7'},
 '2.2.7.c': {'page': 13,
             'memo_page': 6,
             'question_stem_text': ' Figure A is a diagram of a filtration unit of the kidney. The arrows show '
                                   'the direction of blood flow. Figure B is a drawing of a vertical section '
                                   'through a cell from the lining of region 2 of diagram A. Figure A Figure B '
                                   'Below are the concentrations of some substances in blood plasma and in the '
                                   'regions labelled 1 and 3 on Figure A. Substance Concentration/ mg per cm3 '
                                   'Blood plasma Region 1 Region 3 Protein 8000 0 0 Glucose 100 100 0 Salts 320 '
                                   '320 300 Urea 30 30 2000 Explain the difference in concentration of the '
                                   'following: ',
             'parent_question_number': '2.2.7'},
 '3.1.5.A': {'page': 15,
             'memo_page': 7,
             'question_stem_text': ' The diagram below shows the bones and muscles in the human arm. Various type '
                                   'of diseases are associated with the skeletal system. Identify the disease '
                                   'characterized by each of the following: ',
             'parent_question_number': '3.1.5'},
 '3.1.5.B': {'page': 15,
             'memo_page': 7,
             'question_stem_text': ' The diagram below shows the bones and muscles in the human arm. Various type '
                                   'of diseases are associated with the skeletal system. Identify the disease '
                                   'characterized by each of the following: ',
             'parent_question_number': '3.1.5'},
 '3.1.5.C': {'page': 15,
             'memo_page': 7,
             'question_stem_text': ' The diagram below shows the bones and muscles in the human arm. Various type '
                                   'of diseases are associated with the skeletal system. Identify the disease '
                                   'characterized by each of the following: ',
             'parent_question_number': '3.1.5'},
 '4.1.2.a': {'page': 19,
             'memo_page': 9,
             'question_stem_text': ' Garlic is known to have the ability to fight bacteria and viruses. It is '
                                   'known to be effective against a wide range of bacteria and can combat the '
                                   'common cold. The antimicrobial substance in garlic is called alicin. To '
                                   'maintain the antibacterial properties of garlic, it must be consumed or '
                                   'applied as raw garlic. Scientists wanted to investigate the effectiveness of '
                                   'garlic in killing bacteria. They conducted the experiment as follows: • They '
                                   'used three petri dishes prepared with blood agar and stored these in a '
                                   'refrigerator. • Before the start of the experiment, they removed the petri '
                                   'dishes from the refrigerator to allow them to reach room temperature. • They '
                                   'prepared three test specimens and labelled them as described below: o The '
                                   'three test tubes were labelled A, B and C. o The contents of the test tubes '
                                   'were measured and mixed as shown in the table below: Test tube Contents of '
                                   'the test tubes 100 mL milk 5 mL E.coli bacterium Garlic extract A ✓ x x B ✓ ✓ '
                                   'x C ✓ ✓ ✓ • They petri dishes were labelled A, B and C. • They removed the '
                                   'lid in petri dish A and used the syringe to extract 10 mL of the sample from '
                                   'test tube A and placed it in the center of petri dish A. • In the same way, '
                                   'using a new syringe a 10 mL sample was extracted from test tube B and placed '
                                   'in petri dish B and the procedure was repeated for petri dish C. • The petri '
                                   'dish lids were replaced, and the petri dishes were stored in a cool and '
                                   'shaded place. o The diameter of the E.coli colony was measured every day for '
                                   '5 days and recorded in the table below: Petri dish Diameter of bacteria '
                                   'colony (mm) Day 1 Day 2 Day 3 Day 4 Day 5 A 0 1,7 3,0 4,6 7,1 B 0 4,2 8.4 '
                                   '15,1 36,5 C 0 0 0 0 0 State: (4) ',
             'parent_question_number': '4.1.2'},
 '4.1.2.b': {'page': 19,
             'memo_page': 9,
             'question_stem_text': ' Garlic is known to have the ability to fight bacteria and viruses. It is '
                                   'known to be effective against a wide range of bacteria and can combat the '
                                   'common cold. The antimicrobial substance in garlic is called alicin. To '
                                   'maintain the antibacterial properties of garlic, it must be consumed or '
                                   'applied as raw garlic. Scientists wanted to investigate the effectiveness of '
                                   'garlic in killing bacteria. They conducted the experiment as follows: • They '
                                   'used three petri dishes prepared with blood agar and stored these in a '
                                   'refrigerator. • Before the start of the experiment, they removed the petri '
                                   'dishes from the refrigerator to allow them to reach room temperature. • They '
                                   'prepared three test specimens and labelled them as described below: o The '
                                   'three test tubes were labelled A, B and C. o The contents of the test tubes '
                                   'were measured and mixed as shown in the table below: Test tube Contents of '
                                   'the test tubes 100 mL milk 5 mL E.coli bacterium Garlic extract A ✓ x x B ✓ ✓ '
                                   'x C ✓ ✓ ✓ • They petri dishes were labelled A, B and C. • They removed the '
                                   'lid in petri dish A and used the syringe to extract 10 mL of the sample from '
                                   'test tube A and placed it in the center of petri dish A. • In the same way, '
                                   'using a new syringe a 10 mL sample was extracted from test tube B and placed '
                                   'in petri dish B and the procedure was repeated for petri dish C. • The petri '
                                   'dish lids were replaced, and the petri dishes were stored in a cool and '
                                   'shaded place. o The diameter of the E.coli colony was measured every day for '
                                   '5 days and recorded in the table below: Petri dish Diameter of bacteria '
                                   'colony (mm) Day 1 Day 2 Day 3 Day 4 Day 5 A 0 1,7 3,0 4,6 7,1 B 0 4,2 8.4 '
                                   '15,1 36,5 C 0 0 0 0 0 State: (4) ',
             'parent_question_number': '4.1.2'},
 '4.1.2.c': {'page': 19,
             'memo_page': 9,
             'question_stem_text': ' Garlic is known to have the ability to fight bacteria and viruses. It is '
                                   'known to be effective against a wide range of bacteria and can combat the '
                                   'common cold. The antimicrobial substance in garlic is called alicin. To '
                                   'maintain the antibacterial properties of garlic, it must be consumed or '
                                   'applied as raw garlic. Scientists wanted to investigate the effectiveness of '
                                   'garlic in killing bacteria. They conducted the experiment as follows: • They '
                                   'used three petri dishes prepared with blood agar and stored these in a '
                                   'refrigerator. • Before the start of the experiment, they removed the petri '
                                   'dishes from the refrigerator to allow them to reach room temperature. • They '
                                   'prepared three test specimens and labelled them as described below: o The '
                                   'three test tubes were labelled A, B and C. o The contents of the test tubes '
                                   'were measured and mixed as shown in the table below: Test tube Contents of '
                                   'the test tubes 100 mL milk 5 mL E.coli bacterium Garlic extract A ✓ x x B ✓ ✓ '
                                   'x C ✓ ✓ ✓ • They petri dishes were labelled A, B and C. • They removed the '
                                   'lid in petri dish A and used the syringe to extract 10 mL of the sample from '
                                   'test tube A and placed it in the center of petri dish A. • In the same way, '
                                   'using a new syringe a 10 mL sample was extracted from test tube B and placed '
                                   'in petri dish B and the procedure was repeated for petri dish C. • The petri '
                                   'dish lids were replaced, and the petri dishes were stored in a cool and '
                                   'shaded place. o The diameter of the E.coli colony was measured every day for '
                                   '5 days and recorded in the table below: Petri dish Diameter of bacteria '
                                   'colony (mm) Day 1 Day 2 Day 3 Day 4 Day 5 A 0 1,7 3,0 4,6 7,1 B 0 4,2 8.4 '
                                   '15,1 36,5 C 0 0 0 0 0 State: (4) ',
             'parent_question_number': '4.1.2'},
 '4.1.4.A': {'page': 19,
             'memo_page': 9,
             'question_stem_text': ' Garlic is known to have the ability to fight bacteria and viruses. It is '
                                   'known to be effective against a wide range of bacteria and can combat the '
                                   'common cold. The antimicrobial substance in garlic is called alicin. To '
                                   'maintain the antibacterial properties of garlic, it must be consumed or '
                                   'applied as raw garlic. Scientists wanted to investigate the effectiveness of '
                                   'garlic in killing bacteria. They conducted the experiment as follows: • They '
                                   'used three petri dishes prepared with blood agar and stored these in a '
                                   'refrigerator. • Before the start of the experiment, they removed the petri '
                                   'dishes from the refrigerator to allow them to reach room temperature. • They '
                                   'prepared three test specimens and labelled them as described below: o The '
                                   'three test tubes were labelled A, B and C. o The contents of the test tubes '
                                   'were measured and mixed as shown in the table below: Test tube Contents of '
                                   'the test tubes 100 mL milk 5 mL E.coli bacterium Garlic extract A ✓ x x B ✓ ✓ '
                                   'x C ✓ ✓ ✓ • They petri dishes were labelled A, B and C. • They removed the '
                                   'lid in petri dish A and used the syringe to extract 10 mL of the sample from '
                                   'test tube A and placed it in the center of petri dish A. • In the same way, '
                                   'using a new syringe a 10 mL sample was extracted from test tube B and placed '
                                   'in petri dish B and the procedure was repeated for petri dish C. • The petri '
                                   'dish lids were replaced, and the petri dishes were stored in a cool and '
                                   'shaded place. o The diameter of the E.coli colony was measured every day for '
                                   '5 days and recorded in the table below: Petri dish Diameter of bacteria '
                                   'colony (mm) Day 1 Day 2 Day 3 Day 4 Day 5 A 0 1,7 3,0 4,6 7,1 B 0 4,2 8.4 '
                                   '15,1 36,5 C 0 0 0 0 0 Explain the results in the following petri dishes: ',
             'parent_question_number': '4.1.4'},
 '4.1.4.C': {'page': 19,
             'memo_page': 9,
             'question_stem_text': ' Garlic is known to have the ability to fight bacteria and viruses. It is '
                                   'known to be effective against a wide range of bacteria and can combat the '
                                   'common cold. The antimicrobial substance in garlic is called alicin. To '
                                   'maintain the antibacterial properties of garlic, it must be consumed or '
                                   'applied as raw garlic. Scientists wanted to investigate the effectiveness of '
                                   'garlic in killing bacteria. They conducted the experiment as follows: • They '
                                   'used three petri dishes prepared with blood agar and stored these in a '
                                   'refrigerator. • Before the start of the experiment, they removed the petri '
                                   'dishes from the refrigerator to allow them to reach room temperature. • They '
                                   'prepared three test specimens and labelled them as described below: o The '
                                   'three test tubes were labelled A, B and C. o The contents of the test tubes '
                                   'were measured and mixed as shown in the table below: Test tube Contents of '
                                   'the test tubes 100 mL milk 5 mL E.coli bacterium Garlic extract A ✓ x x B ✓ ✓ '
                                   'x C ✓ ✓ ✓ • They petri dishes were labelled A, B and C. • They removed the '
                                   'lid in petri dish A and used the syringe to extract 10 mL of the sample from '
                                   'test tube A and placed it in the center of petri dish A. • In the same way, '
                                   'using a new syringe a 10 mL sample was extracted from test tube B and placed '
                                   'in petri dish B and the procedure was repeated for petri dish C. • The petri '
                                   'dish lids were replaced, and the petri dishes were stored in a cool and '
                                   'shaded place. o The diameter of the E.coli colony was measured every day for '
                                   '5 days and recorded in the table below: Petri dish Diameter of bacteria '
                                   'colony (mm) Day 1 Day 2 Day 3 Day 4 Day 5 A 0 1,7 3,0 4,6 7,1 B 0 4,2 8.4 '
                                   '15,1 36,5 C 0 0 0 0 0 Explain the results in the following petri dishes: ',
             'parent_question_number': '4.1.4'},
 '1.1.row1': {'page': 2,
              'memo_page': 2,
              'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                    'Column I. Each letter may only be used once. Column II: A bacillus; B '
                                    'protists; C asexual; D virus; E plasmid; F coccus; G plankton; H fungi; I '
                                    'algae; J autotrophic; K heterotrophic; L decomposers.',
              'parent_question_number': '1.1'},
 '1.1.row2': {'page': 2,
              'memo_page': 2,
              'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                    'Column I. Each letter may only be used once. Column II: A bacillus; B '
                                    'protists; C asexual; D virus; E plasmid; F coccus; G plankton; H fungi; I '
                                    'algae; J autotrophic; K heterotrophic; L decomposers.',
              'parent_question_number': '1.1'},
 '1.1.row3': {'page': 2,
              'memo_page': 2,
              'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                    'Column I. Each letter may only be used once. Column II: A bacillus; B '
                                    'protists; C asexual; D virus; E plasmid; F coccus; G plankton; H fungi; I '
                                    'algae; J autotrophic; K heterotrophic; L decomposers.',
              'parent_question_number': '1.1'},
 '1.1.row4': {'page': 2,
              'memo_page': 2,
              'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                    'Column I. Each letter may only be used once. Column II: A bacillus; B '
                                    'protists; C asexual; D virus; E plasmid; F coccus; G plankton; H fungi; I '
                                    'algae; J autotrophic; K heterotrophic; L decomposers.',
              'parent_question_number': '1.1'},
 '1.1.row5': {'page': 2,
              'memo_page': 2,
              'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                    'Column I. Each letter may only be used once. Column II: A bacillus; B '
                                    'protists; C asexual; D virus; E plasmid; F coccus; G plankton; H fungi; I '
                                    'algae; J autotrophic; K heterotrophic; L decomposers.',
              'parent_question_number': '1.1'},
 '1.1.row6': {'page': 2,
              'memo_page': 2,
              'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                    'Column I. Each letter may only be used once. Column II: A bacillus; B '
                                    'protists; C asexual; D virus; E plasmid; F coccus; G plankton; H fungi; I '
                                    'algae; J autotrophic; K heterotrophic; L decomposers.',
              'parent_question_number': '1.1'},
 '1.1.row7': {'page': 2,
              'memo_page': 2,
              'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                    'Column I. Each letter may only be used once. Column II: A bacillus; B '
                                    'protists; C asexual; D virus; E plasmid; F coccus; G plankton; H fungi; I '
                                    'algae; J autotrophic; K heterotrophic; L decomposers.',
              'parent_question_number': '1.1'},
 '1.1.row8': {'page': 2,
              'memo_page': 2,
              'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                    'Column I. Each letter may only be used once. Column II: A bacillus; B '
                                    'protists; C asexual; D virus; E plasmid; F coccus; G plankton; H fungi; I '
                                    'algae; J autotrophic; K heterotrophic; L decomposers.',
              'parent_question_number': '1.1'},
 '1.1.row9': {'page': 2,
              'memo_page': 2,
              'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                    'Column I. Each letter may only be used once. Column II: A bacillus; B '
                                    'protists; C asexual; D virus; E plasmid; F coccus; G plankton; H fungi; I '
                                    'algae; J autotrophic; K heterotrophic; L decomposers.',
              'parent_question_number': '1.1'},
 '1.1.row10': {'page': 2,
               'memo_page': 2,
               'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                     'Column I. Each letter may only be used once. Column II: A bacillus; B '
                                     'protists; C asexual; D virus; E plasmid; F coccus; G plankton; H fungi; I '
                                     'algae; J autotrophic; K heterotrophic; L decomposers.',
               'parent_question_number': '1.1'}}
