"""Question-level evidence transcribed from the paper and its verified marking guidelines.

Do not silently correct source errors. LOCATORS retains source pages and shared context.
"""

PAPER = {'paper_key': 'BIO-2022-CYCLE1',
 'paper_path': 'data/organized/biology/Grade 11 cycle test 1.pdf',
 'memo_path': 'data/organized/biology/Grade 11 cycle test 1 MG.pdf',
 'year': 2022,
 'exam_date': '9 FEBRUARY 2022',
 'exam_period': 'february',
 'paper_type': 'cycle_test',
 'exam_board': 'internal',
 'total_marks': 50,
 'question_totals': [22, 28],
 'examiner': 'MRS S. STEGMANN',
 'moderator': 'MRS B. ZAJAC',
 'duration_stated': '1 HOUR',
 'fidelity_rung': 'A',
 'notes': 'Read directly from digital PDF text. Whitespace normalized, blank answer lines and repeating headers '
          'omitted. Lettered subparts retain source letters; rowN identifies an unnumbered matching row. '
          'Image-dependent evidence is unresolved, not reconstructed.',
 'alignment_anchors': {'memo': 'Untreated infections can spread',
                       'paper': 'Which of the following receives blood from the efferent arteriole?'}}

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

RECORDS = [('1.1.1',
  1,
  'Excretion',
  'Multiple Choice',
  'Which of the following receives blood from the efferent arteriole? A. The renal vein B. The glomerulus C. The '
  'afferent arteriole D. The peritubular capillaries',
  False,
  [],
  'D ✓',
  ['D'],
  'D ✓',
  False,
  False),
 ('1.1.2',
  1,
  'Excretion',
  'Multiple Choice',
  'Which of the following factors could possibly result in a person excreting more urine than normal? A. A high '
  'reabsorption of water in the proximal tubules B. A low concentration of ADH in the blood C. Low blood pressure '
  'because of too little tissue fluid. D. Excessive intake of salty foods.',
  False,
  [],
  'B ✓',
  ['B'],
  'B ✓',
  False,
  False),
 ('1.1.3',
  1,
  'Excretion',
  'Multiple Choice',
  'Which of the following is least likely to be present in the glomerular filtrate (the filtrate produced by the '
  'nephron before it enters the loop of Henle) of a healthy adult nephron? A. Amino acids B. Glucose C. '
  'Electrolytes D. Proteins',
  False,
  [],
  'D ✓',
  ['D'],
  'D ✓',
  False,
  False),
 ('1.1.4',
  1,
  'Excretion',
  'Multiple Choice',
  'The renal artery is a division of which main blood vessel? A. The pulmonary artery B. Inferior vena cava C. '
  'Aorta D. Superior vena cava',
  False,
  [],
  'C ✓',
  ['C'],
  'C ✓',
  False,
  False),
 ('1.1.5',
  1,
  'Excretion',
  'Multiple Choice',
  'Which of the following does the renal system NOT play a direct role in? A. Regulation of blood solute '
  'concentrations B. Blood temperature regulation C. Blood pressure regulation D. Blood pH regulation',
  False,
  [],
  'B ✓ (5)',
  ['B'],
  'B ✓ (5)',
  False,
  False),
 ('1.2.1',
  1,
  'Excretion',
  'Multiple Choice',
  'Nitrogenous waste product A: Uric acid B: Urea',
  False,
  [],
  'Both A and B ✓',
  ['Both A and B'],
  'Both A and B ✓',
  False,
  False),
 ('1.2.2',
  1,
  'Excretion',
  'Multiple Choice',
  'Removal of urine from the bladder A: Secretion B: Excretion',
  False,
  [],
  'B only ✓',
  ['B only'],
  'B only ✓',
  False,
  False),
 ('1.2.3',
  1,
  'Excretion',
  'Multiple Choice',
  'Secreted by the adrenal gland A: Adrenalin B: ADH',
  False,
  [],
  'A only ✓',
  ['A only'],
  'A only ✓',
  False,
  False),
 ('1.2.4',
  1,
  'Excretion',
  'Multiple Choice',
  'Urine composition A: Glucose B: Amino acids',
  False,
  [],
  'None ✓ (4)',
  ['None'],
  'None ✓ (4)',
  False,
  False),
 ('1.3.1',
  4,
  'Excretion',
  'Labelling/Diagram',
  'Provide labels for structures 1, 4, 6 and 7. (4)',
  True,
  [],
  '1- aorta ✓ 4- Renal vein ✓ 6- Ureter ✓ 7- Urethra ✓ (4)',
  ['1- aorta', '4- Renal vein', '6- Ureter', '7- Urethra'],
  '1- aorta ✓ 4- Renal vein ✓ 6- Ureter ✓ 7- Urethra ✓ (4)',
  True,
  False),
 ('1.3.2',
  2,
  'Excretion',
  'Definition/Terminology',
  'What is the value of the kidneys being surrounded by a thick layer of adipose tissue? (2)',
  False,
  [],
  'It provides protection ✓ from mechanical injury✓ (2)',
  ['It provides protection', 'from mechanical injury'],
  'It provides protection ✓ from mechanical injury✓ (2)',
  False,
  False),
 ('1.3.3',
  4,
  'Excretion',
  'Data/Graph Interpretation',
  'Tabulate two differences in the blood found in structures 2 and 4. (4)',
  True,
  [],
  'Heading ✓ 2 differences: ✓✓ - 2 contains oxygenated blood; 4 contains deoxygenated blood - 2 has unfiltered '
  'blood; 4 contains purified blood (can extend on this) Complete table ✓ (4)',
  ['Heading',
   '2 differences:',
   '- 2 contains oxygenated blood; 4 contains deoxygenated blood - 2 has unfiltered blood; 4 contains purified '
   'blood (can extend on this) Complete table'],
  'Heading ✓ 2 differences: ✓✓ - 2 contains oxygenated blood; 4 contains deoxygenated blood - 2 has unfiltered '
  'blood; 4 contains purified blood (can extend on this) Complete table ✓ (4)',
  True,
  False),
 ('1.3.4.A',
  2,
  'Excretion',
  'Short Answer',
  'Urine is slightly thicker in summer than in winter. (2)',
  False,
  [],
  'More water is reabsorbed ✓ as individuals sweat more, therefore lose more water from the body. The urine is '
  'therefore more concentrated/ thicker ✓ (2)',
  ['More water is reabsorbed',
   'as individuals sweat more, therefore lose more water from the body. The urine is therefore more concentrated/ '
   'thicker'],
  'More water is reabsorbed ✓ as individuals sweat more, therefore lose more water from the body. The urine is '
  'therefore more concentrated/ thicker ✓ (2)',
  False,
  False),
 ('1.3.4.B',
  1,
  'Excretion',
  'Short Answer',
  'The renal cortex has a dotted appearance. (1) (13)',
  False,
  [],
  'The dots represent the renal corpuscles✓ in the cortex. (1) (13)',
  ['The dots represent the renal corpuscles', 'in the cortex. (1) (13)'],
  'The dots represent the renal corpuscles✓ in the cortex. (1) (13)',
  False,
  False),
 ('2.1.1.a',
  2,
  'Excretion',
  'Short Answer',
  'Afferent arteriole (2)',
  False,
  [],
  'D✓- has the highest flow rate; contains proteins (any 1 ✓) (2)',
  ['D', '- has the highest flow rate; contains proteins (any 1'],
  'D✓- has the highest flow rate; contains proteins (any 1 ✓) (2)',
  False,
  False),
 ('2.1.1.b',
  2,
  'Excretion',
  'Short Answer',
  'Bowman’s capsule (2)',
  False,
  [],
  'B✓- contains glucose, but no proteins ✓ (2)',
  ['B', '- contains glucose, but no proteins'],
  'B✓- contains glucose, but no proteins ✓ (2)',
  False,
  False),
 ('2.1.1.c',
  2,
  'Excretion',
  'Short Answer',
  'Loop of Henle (2)',
  False,
  [],
  'C✓- lowest concentration of sodium ions ✓ (2)',
  ['C', '- lowest concentration of sodium ions'],
  'C✓- lowest concentration of sodium ions ✓ (2)',
  False,
  False),
 ('2.1.1.d',
  2,
  'Excretion',
  'Short Answer',
  'Collecting duct (2)',
  False,
  [],
  'A✓- lowest flow rate; highest urea concentration; contains ammonium ions (any 1 ✓) (2)',
  ['A', '- lowest flow rate; highest urea concentration; contains ammonium ions (any 1'],
  'A✓- lowest flow rate; highest urea concentration; contains ammonium ions (any 1 ✓) (2)',
  False,
  False),
 ('2.1.2',
  2,
  'Excretion',
  'Short Answer',
  'State two functions of the kidney that can be supported by the data given in the table. (2)',
  False,
  [],
  'Removal of nitrogenous wastes; regulation of sodium ions/ salt concentration (any 2 ✓✓) (2)',
  ['Removal of nitrogenous wastes; regulation of sodium ions/ salt concentration (any 2'],
  'Removal of nitrogenous wastes; regulation of sodium ions/ salt concentration (any 2 ✓✓) (2)',
  False,
  False),
 ('2.1.3',
  5,
  'Excretion',
  'Labelling/Diagram',
  'Provide a labeled diagram of the renal corpuscle. (5) (15)',
  True,
  [],
  'Heading✓ Accuracy and drawing rules ✓ 3 x correct labels ✓✓✓ (5) (15)',
  ['Heading', 'Accuracy and drawing rules', '3 x correct labels'],
  'Heading✓ Accuracy and drawing rules ✓ 3 x correct labels ✓✓✓ (5) (15)',
  True,
  False),
 ('2.2.1',
  1,
  'Excretion',
  'Short Answer',
  'A urinary tract infection (UTI) is caused by bacteria entering the urinary system. Which part of the urinary '
  'system does the bacteria most likely enter? (1)',
  False,
  [],
  'Urethra ✓ (1)',
  ['Urethra'],
  'Urethra ✓ (1)',
  False,
  False),
 ('2.2.2',
  3,
  'Excretion',
  'Short Answer',
  'Why is early detection, provided by a test kit like Combur-10 Test Strip, so vital? (3)',
  False,
  [],
  'Untreated infections can spread ✓ and could cause irreversible/severe damage✓ to the tissue throughout the '
  'urinary system. This could result in kidney failure. ✓ Therefore early detection reduces the risk of '
  'developing kidney failure. ✓ (any 3)',
  ['Untreated infections can spread',
   'and could cause irreversible/severe damage',
   'to the tissue throughout the urinary system. This could result in kidney failure.',
   'Therefore early detection reduces the risk of developing kidney failure.',
   '(any 3)'],
  'Untreated infections can spread ✓ and could cause irreversible/severe damage✓ to the tissue throughout the '
  'urinary system. This could result in kidney failure. ✓ Therefore early detection reduces the risk of '
  'developing kidney failure. ✓ (any 3)',
  False,
  False),
 ('2.2.3',
  1,
  'Excretion',
  'Short Answer',
  'Name the UTI for which Combur-10 Test Strip is very commonly used to test for. (1)',
  False,
  [],
  'Cystitis ✓ (1)',
  ['Cystitis'],
  'Cystitis ✓ (1)',
  False,
  False),
 ('2.2.4.A',
  2,
  'Excretion',
  'Short Answer',
  'Provide TWO variables that needed to be controlled in the above investigation. (2)',
  False,
  [],
  'The same number of females and males needed to participate in the study. Each age group needed to contain the '
  'same number of males and females The patients could not be suffering with any other illnesses that could alter '
  'the results of the study (any 2✓✓) (2)',
  ['The same number of females and males needed to participate in the study. Each age group needed to contain the '
   'same number of males and females The patients could not be suffering with any other illnesses that could '
   'alter the results of the study (any 2'],
  'The same number of females and males needed to participate in the study. Each age group needed to contain the '
  'same number of males and females The patients could not be suffering with any other illnesses that could alter '
  'the results of the study (any 2✓✓) (2)',
  False,
  False),
 ('2.2.4.B',
  1,
  'Excretion',
  'Short Answer',
  'Provide a conclusion for the above study. (1)',
  False,
  [],
  'UTIs are more common amongst young females ✓ (1)',
  ['UTIs are more common amongst young females'],
  'UTIs are more common amongst young females ✓ (1)',
  False,
  False),
 ('2.2.4.C',
  5,
  'Excretion',
  'Data/Graph Interpretation',
  'Display the percentage of males affected in the different age groups in an appropriate graph. (5) (13)',
  True,
  [],
  'Heading✓ Histogram✓ X-axis✓ Y-axis✓ Plotting✓ (5) (13)',
  ['Heading', 'Histogram', 'X-axis', 'Y-axis', 'Plotting'],
  'Heading✓ Histogram✓ X-axis✓ Y-axis✓ Plotting✓ (5) (13)',
  True,
  False)]

SOURCE_HASHES = {'paper_path': 'f9e28847ed0fc155ac4a25a4a2cc1243e3c71878c9f5db169bedcfcca9f927a2',
 'memo_path': 'ff3fd14af8165448fab3ba98e9fdd321ba25949b017308e18ad98f7bfa95b81e'}

LOCATORS = {'1.1.1': {'page': 2,
           'memo_page': 2,
           'question_stem_text': ' Various possibilities are suggested as answers to the following questions. '
                                 'Indicate the correct answer by writing the correct letter from the '
                                 'corresponding question on the folio paper provided. (5)',
           'parent_question_number': '1.1'},
 '1.1.2': {'page': 2,
           'memo_page': 2,
           'question_stem_text': ' Various possibilities are suggested as answers to the following questions. '
                                 'Indicate the correct answer by writing the correct letter from the '
                                 'corresponding question on the folio paper provided. (5)',
           'parent_question_number': '1.1'},
 '1.1.3': {'page': 2,
           'memo_page': 2,
           'question_stem_text': ' Various possibilities are suggested as answers to the following questions. '
                                 'Indicate the correct answer by writing the correct letter from the '
                                 'corresponding question on the folio paper provided. (5)',
           'parent_question_number': '1.1'},
 '1.1.4': {'page': 2,
           'memo_page': 2,
           'question_stem_text': ' Various possibilities are suggested as answers to the following questions. '
                                 'Indicate the correct answer by writing the correct letter from the '
                                 'corresponding question on the folio paper provided. (5)',
           'parent_question_number': '1.1'},
 '1.1.5': {'page': 2,
           'memo_page': 2,
           'question_stem_text': ' Various possibilities are suggested as answers to the following questions. '
                                 'Indicate the correct answer by writing the correct letter from the '
                                 'corresponding question on the folio paper provided. (5)',
           'parent_question_number': '1.1'},
 '1.2.1': {'page': 3,
           'memo_page': 2,
           'question_stem_text': ' Indicate whether each of the statements in COLUMN I applies to A only, B only, '
                                 'both A and B or none of the items in COLUMN II. Write A only, B only, both A '
                                 'and B or none next to the question number on your answer sheet. (4) COLUMN I '
                                 'COLUMN II',
           'parent_question_number': '1.2'},
 '1.2.2': {'page': 3,
           'memo_page': 2,
           'question_stem_text': ' Indicate whether each of the statements in COLUMN I applies to A only, B only, '
                                 'both A and B or none of the items in COLUMN II. Write A only, B only, both A '
                                 'and B or none next to the question number on your answer sheet. (4) COLUMN I '
                                 'COLUMN II',
           'parent_question_number': '1.2'},
 '1.2.3': {'page': 3,
           'memo_page': 2,
           'question_stem_text': ' Indicate whether each of the statements in COLUMN I applies to A only, B only, '
                                 'both A and B or none of the items in COLUMN II. Write A only, B only, both A '
                                 'and B or none next to the question number on your answer sheet. (4) COLUMN I '
                                 'COLUMN II',
           'parent_question_number': '1.2'},
 '1.2.4': {'page': 3,
           'memo_page': 2,
           'question_stem_text': ' Indicate whether each of the statements in COLUMN I applies to A only, B only, '
                                 'both A and B or none of the items in COLUMN II. Write A only, B only, both A '
                                 'and B or none next to the question number on your answer sheet. (4) COLUMN I '
                                 'COLUMN II',
           'parent_question_number': '1.2'},
 '1.3.1': {'page': 3,
           'memo_page': 2,
           'question_stem_text': ' The diagram below shows the excretory system of a human being. Study the '
                                 'diagram and answer the questions that follow.',
           'parent_question_number': '1.3'},
 '1.3.2': {'page': 3,
           'memo_page': 2,
           'question_stem_text': ' The diagram below shows the excretory system of a human being. Study the '
                                 'diagram and answer the questions that follow.',
           'parent_question_number': '1.3'},
 '1.3.3': {'page': 4,
           'memo_page': 2,
           'question_stem_text': ' The diagram below shows the excretory system of a human being. Study the '
                                 'diagram and answer the questions that follow.',
           'parent_question_number': '1.3'},
 '2.1.2': {'page': 4,
           'memo_page': 3,
           'question_stem_text': ' Study the following table that shows the flow rate and concentration of '
                                 'certain substances taken at regions A, B, C and D of the nephron in the human '
                                 'kidney. Part of nephron Flow rate (cm³/ min) Solute concentrations (g/100 cm³) '
                                 'Proteins Glucose Sodium ions Ammonium ions Urea A 4 0 0 0,6 0,04 1,80 B 200 0 '
                                 '0,10 0,72 0 0,05 C 40 0 0 0,3 0 0,15 D 2000 7 0,10 0,72 0 0,05',
           'parent_question_number': '2.1'},
 '2.1.3': {'page': 4,
           'memo_page': 3,
           'question_stem_text': ' Study the following table that shows the flow rate and concentration of '
                                 'certain substances taken at regions A, B, C and D of the nephron in the human '
                                 'kidney. Part of nephron Flow rate (cm³/ min) Solute concentrations (g/100 cm³) '
                                 'Proteins Glucose Sodium ions Ammonium ions Urea A 4 0 0 0,6 0,04 1,80 B 200 0 '
                                 '0,10 0,72 0 0,05 C 40 0 0 0,3 0 0,15 D 2000 7 0,10 0,72 0 0,05',
           'parent_question_number': '2.1'},
 '2.2.1': {'page': 5,
           'memo_page': 3,
           'question_stem_text': ' Study the information below and answer the questions that follow. Combur-10 '
                                 'Test Strip Streptococcus bacteria can cause serious infection of different '
                                 'parts of the urinary system. The Combur-10 Test Strip is a dry chemistry test '
                                 'for the early and reliable detection of kidney diseases, diabetes, and urinary '
                                 'tract infection, like cystitis.',
           'parent_question_number': '2.2'},
 '2.2.2': {'page': 5,
           'memo_page': 3,
           'question_stem_text': ' Study the information below and answer the questions that follow. Combur-10 '
                                 'Test Strip Streptococcus bacteria can cause serious infection of different '
                                 'parts of the urinary system. The Combur-10 Test Strip is a dry chemistry test '
                                 'for the early and reliable detection of kidney diseases, diabetes, and urinary '
                                 'tract infection, like cystitis.',
           'parent_question_number': '2.2'},
 '2.2.3': {'page': 5,
           'memo_page': 3,
           'question_stem_text': ' Study the information below and answer the questions that follow. Combur-10 '
                                 'Test Strip Streptococcus bacteria can cause serious infection of different '
                                 'parts of the urinary system. The Combur-10 Test Strip is a dry chemistry test '
                                 'for the early and reliable detection of kidney diseases, diabetes, and urinary '
                                 'tract infection, like cystitis.',
           'parent_question_number': '2.2'},
 '1.3.4.A': {'page': 4,
             'memo_page': 2,
             'question_stem_text': ' The diagram below shows the excretory system of a human being. Study the '
                                   'diagram and answer the questions that follow. Explain why: ',
             'parent_question_number': '1.3.4'},
 '1.3.4.B': {'page': 4,
             'memo_page': 2,
             'question_stem_text': ' The diagram below shows the excretory system of a human being. Study the '
                                   'diagram and answer the questions that follow. Explain why: ',
             'parent_question_number': '1.3.4'},
 '2.1.1.a': {'page': 4,
             'memo_page': 2,
             'question_stem_text': ' Study the following table that shows the flow rate and concentration of '
                                   'certain substances taken at regions A, B, C and D of the nephron in the human '
                                   'kidney. Part of nephron Flow rate (cm³/ min) Solute concentrations (g/100 '
                                   'cm³) Proteins Glucose Sodium ions Ammonium ions Urea A 4 0 0 0,6 0,04 1,80 B '
                                   '200 0 0,10 0,72 0 0,05 C 40 0 0 0,3 0 0,15 D 2000 7 0,10 0,72 0 0,05 State '
                                   'and provide a reason which of the parts (A, B, C or D) of the nephron '
                                   'represent the following: ',
             'parent_question_number': '2.1.1'},
 '2.1.1.b': {'page': 4,
             'memo_page': 2,
             'question_stem_text': ' Study the following table that shows the flow rate and concentration of '
                                   'certain substances taken at regions A, B, C and D of the nephron in the human '
                                   'kidney. Part of nephron Flow rate (cm³/ min) Solute concentrations (g/100 '
                                   'cm³) Proteins Glucose Sodium ions Ammonium ions Urea A 4 0 0 0,6 0,04 1,80 B '
                                   '200 0 0,10 0,72 0 0,05 C 40 0 0 0,3 0 0,15 D 2000 7 0,10 0,72 0 0,05 State '
                                   'and provide a reason which of the parts (A, B, C or D) of the nephron '
                                   'represent the following: ',
             'parent_question_number': '2.1.1'},
 '2.1.1.c': {'page': 4,
             'memo_page': 2,
             'question_stem_text': ' Study the following table that shows the flow rate and concentration of '
                                   'certain substances taken at regions A, B, C and D of the nephron in the human '
                                   'kidney. Part of nephron Flow rate (cm³/ min) Solute concentrations (g/100 '
                                   'cm³) Proteins Glucose Sodium ions Ammonium ions Urea A 4 0 0 0,6 0,04 1,80 B '
                                   '200 0 0,10 0,72 0 0,05 C 40 0 0 0,3 0 0,15 D 2000 7 0,10 0,72 0 0,05 State '
                                   'and provide a reason which of the parts (A, B, C or D) of the nephron '
                                   'represent the following: ',
             'parent_question_number': '2.1.1'},
 '2.1.1.d': {'page': 4,
             'memo_page': 2,
             'question_stem_text': ' Study the following table that shows the flow rate and concentration of '
                                   'certain substances taken at regions A, B, C and D of the nephron in the human '
                                   'kidney. Part of nephron Flow rate (cm³/ min) Solute concentrations (g/100 '
                                   'cm³) Proteins Glucose Sodium ions Ammonium ions Urea A 4 0 0 0,6 0,04 1,80 B '
                                   '200 0 0,10 0,72 0 0,05 C 40 0 0 0,3 0 0,15 D 2000 7 0,10 0,72 0 0,05 State '
                                   'and provide a reason which of the parts (A, B, C or D) of the nephron '
                                   'represent the following: ',
             'parent_question_number': '2.1.1'},
 '2.2.4.A': {'page': 6,
             'memo_page': 3,
             'question_stem_text': ' Study the information below and answer the questions that follow. Combur-10 '
                                   'Test Strip Streptococcus bacteria can cause serious infection of different '
                                   'parts of the urinary system. The Combur-10 Test Strip is a dry chemistry test '
                                   'for the early and reliable detection of kidney diseases, diabetes, and '
                                   'urinary tract infection, like cystitis. A study was done to determine if UTIs '
                                   'were more common amongst young males or females. The results of a test group '
                                   'of individuals suffering with UTIs at any given time is tabulated below. Age '
                                   'group (years) Female percentage affected (%) Male percentage affected (%) <1 '
                                   '39.1 60.9 1-5 73.2 26.8 6-10 82.4 17.6 11-15 66.7 33.3 Total 70.0 30.0 ',
             'parent_question_number': '2.2.4'},
 '2.2.4.B': {'page': 6,
             'memo_page': 3,
             'question_stem_text': ' Study the information below and answer the questions that follow. Combur-10 '
                                   'Test Strip Streptococcus bacteria can cause serious infection of different '
                                   'parts of the urinary system. The Combur-10 Test Strip is a dry chemistry test '
                                   'for the early and reliable detection of kidney diseases, diabetes, and '
                                   'urinary tract infection, like cystitis. A study was done to determine if UTIs '
                                   'were more common amongst young males or females. The results of a test group '
                                   'of individuals suffering with UTIs at any given time is tabulated below. Age '
                                   'group (years) Female percentage affected (%) Male percentage affected (%) <1 '
                                   '39.1 60.9 1-5 73.2 26.8 6-10 82.4 17.6 11-15 66.7 33.3 Total 70.0 30.0 ',
             'parent_question_number': '2.2.4'},
 '2.2.4.C': {'page': 6,
             'memo_page': 3,
             'question_stem_text': ' Study the information below and answer the questions that follow. Combur-10 '
                                   'Test Strip Streptococcus bacteria can cause serious infection of different '
                                   'parts of the urinary system. The Combur-10 Test Strip is a dry chemistry test '
                                   'for the early and reliable detection of kidney diseases, diabetes, and '
                                   'urinary tract infection, like cystitis. A study was done to determine if UTIs '
                                   'were more common amongst young males or females. The results of a test group '
                                   'of individuals suffering with UTIs at any given time is tabulated below. Age '
                                   'group (years) Female percentage affected (%) Male percentage affected (%) <1 '
                                   '39.1 60.9 1-5 73.2 26.8 6-10 82.4 17.6 11-15 66.7 33.3 Total 70.0 30.0 ',
             'parent_question_number': '2.2.4'}}
