"""Question-level evidence transcribed from the paper and its verified marking guidelines.

Do not silently correct source errors. LOCATORS retains source pages and shared context.
"""

PAPER = {'paper_key': 'BIO-2023-MICRO',
 'paper_path': 'data/organized/biology/Class test- microorganisms.pdf',
 'memo_path': 'data/organized/biology/Class test- microorganisms MG.pdf',
 'year': 2023,
 'exam_date': '2 OCTOBER 2023',
 'exam_period': 'october',
 'paper_type': 'class_test',
 'exam_board': 'internal',
 'total_marks': 40,
 'question_totals': [10, 13, 17],
 'examiner': 'MRS S. STEGMANN',
 'moderator': 'MRS B. ZAJAC',
 'duration_stated': '40 MINUTES',
 'fidelity_rung': 'A',
 'notes': 'Read directly from digital PDF text. Whitespace normalized, blank answer lines and repeating headers '
          'omitted. Lettered subparts retain source letters; rowN identifies an unnumbered matching row. '
          'Image-dependent evidence is unresolved, not reconstructed.',
 'alignment_anchors': {'memo': '2.1. Type of bacteria',
                       'paper': 'Valentina and Ishika are microbiology students investigating penicillin '
                                'resistance'}}

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

RECORDS = [('1.row1',
  1,
  'Microorganisms',
  'Definition/Terminology',
  'Antibodies',
  False,
  [],
  'E ✓',
  ['E'],
  'E ✓',
  False,
  False),
 ('1.row10',
  1,
  'Microorganisms',
  'Definition/Terminology',
  'Thrush',
  False,
  [],
  'D ✓',
  ['D'],
  'D ✓',
  False,
  False),
 ('1.row2',
  1,
  'Microorganisms',
  'Definition/Terminology',
  'Viruses that infect bacteria',
  False,
  [],
  'H ✓',
  ['H'],
  'H ✓',
  False,
  False),
 ('1.row3',
  1,
  'Microorganisms',
  'Definition/Terminology',
  'Weakened immune system',
  False,
  [],
  'B ✓',
  ['B'],
  'B ✓',
  False,
  False),
 ('1.row4', 1, 'Microorganisms', 'Definition/Terminology', 'Algae', False, [], 'G ✓', ['G'], 'G ✓', False, False),
 ('1.row5', 1, 'Microorganisms', 'Definition/Terminology', 'Germs', False, [], 'C ✓', ['C'], 'C ✓', False, False),
 ('1.row6', 1, 'Microorganisms', 'Definition/Terminology', 'Agar', False, [], 'A ✓', ['A'], 'A ✓', False, False),
 ('1.row7',
  1,
  'Microorganisms',
  'Definition/Terminology',
  'Acellular',
  False,
  [],
  'J ✓',
  ['J'],
  'J ✓',
  False,
  False),
 ('1.row8',
  1,
  'Microorganisms',
  'Definition/Terminology',
  'Mosquito',
  False,
  [],
  'F ✓',
  ['F'],
  'F ✓',
  False,
  False),
 ('1.row9',
  1,
  'Microorganisms',
  'Definition/Terminology',
  'Antibiotics',
  False,
  [],
  'I ✓',
  ['I'],
  'I ✓',
  False,
  False),
 ('2.1',
  1,
  'Microorganisms',
  'Short Answer',
  'State the independent variable in this experiment. (1)',
  False,
  [],
  'Type of bacteria ✓ (1)',
  ['Type of bacteria'],
  'Type of bacteria ✓ (1)',
  False,
  False),
 ('2.2',
  2,
  'Microorganisms',
  'Short Answer',
  'Write a suitable hypothesis for the experiment. (2)',
  False,
  [],
  'All bacteria ✓ will be killed by penicillin. ✓ (any statement regarding the independent and dependent '
  'variable) (2)',
  ['All bacteria',
   'will be killed by penicillin.',
   '(any statement regarding the independent and dependent variable) (2)'],
  'All bacteria ✓ will be killed by penicillin. ✓ (any statement regarding the independent and dependent '
  'variable) (2)',
  False,
  False),
 ('2.3',
  1,
  'Microorganisms',
  'Data/Graph Interpretation',
  'Which bacteria showed the most antibiotic resistance? (1)',
  True,
  [],
  'Bacteria C ✓ (1)',
  ['Bacteria C'],
  'Bacteria C ✓ (1)',
  True,
  False),
 ('2.4',
  2,
  'Microorganisms',
  'Data/Graph Interpretation',
  'Explain your answer to QUESTION 2.3. (2)',
  True,
  [],
  'There was no change in the number of bacteria✓ after the penicillin was added and no clear zone formed✓. (2)',
  ['There was no change in the number of bacteria',
   'after the penicillin was added and no clear zone formed',
   '. (2)'],
  'There was no change in the number of bacteria✓ after the penicillin was added and no clear zone formed✓. (2)',
  True,
  False),
 ('2.5',
  3,
  'Microorganisms',
  'Short Answer',
  'Explain how resistance to antibiotics develops in a population of bacteria. (3)',
  False,
  [],
  'A few bacteria develop random mutations✓ which cause them to be resistant to an antibiotic. These resistant '
  'bacteria will survive and multiply✓ producing a fully antibiotic resistant population. ✓ (3)',
  ['A few bacteria develop random mutations',
   'which cause them to be resistant to an antibiotic. These resistant bacteria will survive and multiply',
   'producing a fully antibiotic resistant population.'],
  'A few bacteria develop random mutations✓ which cause them to be resistant to an antibiotic. These resistant '
  'bacteria will survive and multiply✓ producing a fully antibiotic resistant population. ✓ (3)',
  False,
  False),
 ('2.6',
  1,
  'Microorganisms',
  'Short Answer',
  'State ONE way in which the development of resistant bacteria can be minimized. (1)',
  False,
  [],
  'The full course of antibiotics needs to be taken/ completed Numerous courses/ ongoing antibiotics should be '
  'avoided ✓ (any 1)',
  ['The full course of antibiotics needs to be taken/ completed Numerous courses/ ongoing antibiotics should be '
   'avoided',
   '(any 1)'],
  'The full course of antibiotics needs to be taken/ completed Numerous courses/ ongoing antibiotics should be '
  'avoided ✓ (any 1)',
  False,
  False),
 ('2.7.A',
  2,
  'Microorganisms',
  'Short Answer',
  'Explain why controls are necessary in this experiment. (2)',
  False,
  [],
  'To compare results ✓ and see what the natural result would look like ✓ (2)',
  ['To compare results', 'and see what the natural result would look like'],
  'To compare results ✓ and see what the natural result would look like ✓ (2)',
  False,
  False),
 ('2.7.B',
  1,
  'Microorganisms',
  'Short Answer',
  'Which ‘ingredient’ would be missing from the controls? (1)',
  False,
  [],
  'Penicillin ✓ (1)',
  ['Penicillin'],
  'Penicillin ✓ (1)',
  False,
  False),
 ('3.1.1',
  1,
  'Microorganisms',
  'Short Answer',
  'What group of microorganisms does Plasmodium belong to? (1)',
  False,
  [],
  'Protists/ protista ✓ (1)',
  ['Protists/ protista'],
  'Protists/ protista ✓ (1)',
  False,
  False),
 ('3.1.2.a',
  1,
  'Microorganisms',
  'Data/Graph Interpretation',
  'The highest temperature this patient experienced during the time period. (1)',
  True,
  [],
  '40,2 °C ✓ (accept 40-40,5) (1)',
  ['40,2 °C', '(accept 40-40,5) (1)'],
  '40,2 °C ✓ (accept 40-40,5) (1)',
  True,
  False),
 ('3.1.2.b',
  1,
  'Microorganisms',
  'Data/Graph Interpretation',
  'The number of fever attacks the patient experienced during the five days. (1)',
  True,
  [],
  '3 ✓ (1)',
  [],
  '3 ✓ (1)',
  True,
  False),
 ('3.1.3',
  1,
  'Microorganisms',
  'Short Answer',
  'Why does the graph above begin on Day 11? (1)',
  False,
  [],
  'Malaria symptoms only appear after 10 days ✓ (1)',
  ['Malaria symptoms only appear after 10 days'],
  'Malaria symptoms only appear after 10 days ✓ (1)',
  False,
  False),
 ('3.1.4',
  1,
  'Microorganisms',
  'Data/Graph Interpretation',
  'Predict on which day the patient could expect the start of the next fever attack. (1)',
  True,
  [],
  'Day 17 ✓ (1)',
  ['Day 17'],
  'Day 17 ✓ (1)',
  True,
  False),
 ('3.1.5',
  2,
  'Microorganisms',
  'Short Answer',
  'Plasmodium destroys the red blood cells. What effect could this have on the body? (2)',
  False,
  [],
  'Less oxygen will be delivered to the cells✓ and therefore a person will have less energy✓ / lowered '
  'respiration due to less oxygen (1 mark if they just say “fatigue”) (2)',
  ['Less oxygen will be delivered to the cells',
   'and therefore a person will have less energy',
   '/ lowered respiration due to less oxygen (1 mark if they just say “fatigue”) (2)'],
  'Less oxygen will be delivered to the cells✓ and therefore a person will have less energy✓ / lowered '
  'respiration due to less oxygen (1 mark if they just say “fatigue”) (2)',
  False,
  False),
 ('3.1.6',
  2,
  'Microorganisms',
  'Short Answer',
  'Suggest TWO ways of preventing malaria. (2)',
  False,
  [],
  'Take preventative medication before entering a malaria area (prescribed malaria medication) Wear long clothing '
  'in malaria areas Use repellent sprays and lotions Sleep under a mosquito net Spray mosquito nets with '
  'repellent sprays Close all windows and doors from dusk Stay indoors from dusk until dawn Any reasonable, '
  'logical answer ✓✓ (any 2)',
  ['Take preventative medication before entering a malaria area (prescribed malaria medication) Wear long '
   'clothing in malaria areas Use repellent sprays and lotions Sleep under a mosquito net Spray mosquito nets '
   'with repellent sprays Close all windows and doors from dusk Stay indoors from dusk until dawn Any reasonable, '
   'logical answer',
   '(any 2)'],
  'Take preventative medication before entering a malaria area (prescribed malaria medication) Wear long clothing '
  'in malaria areas Use repellent sprays and lotions Sleep under a mosquito net Spray mosquito nets with '
  'repellent sprays Close all windows and doors from dusk Stay indoors from dusk until dawn Any reasonable, '
  'logical answer ✓✓ (any 2)',
  False,
  False),
 ('3.2.1',
  1,
  'Microorganisms',
  'Short Answer',
  'Explain the function of CD4 cells. (1)',
  False,
  [],
  'They start their immune response. (1)',
  ['They start their immune response. (1)'],
  'They start their immune response. (1)',
  False,
  False),
 ('3.2.2',
  2,
  'Microorganisms',
  'Short Answer',
  'When will a person be classified with AIDS? (2)',
  False,
  [],
  'A person will be classified as having AIDs when the CD4 cells have been reduced ✓ and can no longer fight the '
  'HIV virus and the virus keeps multiplying ✓ When the CD4 count is lower than 200 cells/ mL of blood '
  'Opportunistic diseases have taken a toll on the body (any 2)',
  ['A person will be classified as having AIDs when the CD4 cells have been reduced',
   'and can no longer fight the HIV virus and the virus keeps multiplying',
   'When the CD4 count is lower than 200 cells/ mL of blood Opportunistic diseases have taken a toll on the body '
   '(any 2)'],
  'A person will be classified as having AIDs when the CD4 cells have been reduced ✓ and can no longer fight the '
  'HIV virus and the virus keeps multiplying ✓ When the CD4 count is lower than 200 cells/ mL of blood '
  'Opportunistic diseases have taken a toll on the body (any 2)',
  False,
  False),
 ('3.2.3',
  3,
  'Microorganisms',
  'Short Answer',
  'Explain why the HIV virus is so dangerous and causes so many deaths. (3)',
  False,
  [],
  'Because the HI virus attacks CD4 cells it stops the body from being able to start an immune response. ✓ Not '
  'being able to start an immune response the body becomes susceptible to any other type of infection ✓ and thus '
  'it won’t be able to fight of the infection and thus the person will die. ✓ (3)',
  ['Because the HI virus attacks CD4 cells it stops the body from being able to start an immune response.',
   'Not being able to start an immune response the body becomes susceptible to any other type of infection',
   'and thus it won’t be able to fight of the infection and thus the person will die.'],
  'Because the HI virus attacks CD4 cells it stops the body from being able to start an immune response. ✓ Not '
  'being able to start an immune response the body becomes susceptible to any other type of infection ✓ and thus '
  'it won’t be able to fight of the infection and thus the person will die. ✓ (3)',
  False,
  False),
 ('3.2.4',
  2,
  'Microorganisms',
  'Short Answer',
  'Why is it possible to easily cultivate and grow bacteria, but it is very difficult to cultivate a virus? (2)',
  False,
  [],
  'Bacteria can grow easily in favourable conditions ✓ whereas a virus needs a living host to grow in ✓ and they '
  'destroy the host so thus the virus will not reproduce more if there isn’t more host tissue ✓ (any 2)',
  ['Bacteria can grow easily in favourable conditions',
   'whereas a virus needs a living host to grow in',
   'and they destroy the host so thus the virus will not reproduce more if there isn’t more host tissue',
   '(any 2)'],
  'Bacteria can grow easily in favourable conditions ✓ whereas a virus needs a living host to grow in ✓ and they '
  'destroy the host so thus the virus will not reproduce more if there isn’t more host tissue ✓ (any 2)',
  False,
  False)]

SOURCE_HASHES = {'paper_path': 'f97d3ee8b236620b022817e80050ae1bdc0d80c741e991f74c7d19b2f885f918',
 'memo_path': 'eeb9f50732ae63b7cbdb3a97a48a03a4e8c3693371db6eadc70fb66b4cc49517'}

LOCATORS = {'2.1': {'page': 3,
         'memo_page': 2,
         'question_stem_text': 'Valentina and Ishika are microbiology students investigating penicillin '
                               'resistance in modern day bacterial cultures. Penicillin had, in the past, been an '
                               'effective antibiotic and so they decided to set up an experiment to determine '
                               'which type of bacterium has developed the greatest resistance to penicillin. They '
                               'obtained pure cultures of five different types of bacteria (A-E) and placed each '
                               'type of bacteria into a separate petri dish with nutrient agar. Once the agar was '
                               'set, a hollow was cut in the agar in the center of each petri dish, using a cork '
                               'borer. Penicillin was then added to the hollows. After incubation at 25°C for 24 '
                               'hours, the petri dishes were examined.',
         'parent_question_number': '2'},
 '2.2': {'page': 3,
         'memo_page': 2,
         'question_stem_text': 'Valentina and Ishika are microbiology students investigating penicillin '
                               'resistance in modern day bacterial cultures. Penicillin had, in the past, been an '
                               'effective antibiotic and so they decided to set up an experiment to determine '
                               'which type of bacterium has developed the greatest resistance to penicillin. They '
                               'obtained pure cultures of five different types of bacteria (A-E) and placed each '
                               'type of bacteria into a separate petri dish with nutrient agar. Once the agar was '
                               'set, a hollow was cut in the agar in the center of each petri dish, using a cork '
                               'borer. Penicillin was then added to the hollows. After incubation at 25°C for 24 '
                               'hours, the petri dishes were examined.',
         'parent_question_number': '2'},
 '2.3': {'page': 3,
         'memo_page': 2,
         'question_stem_text': 'Valentina and Ishika are microbiology students investigating penicillin '
                               'resistance in modern day bacterial cultures. Penicillin had, in the past, been an '
                               'effective antibiotic and so they decided to set up an experiment to determine '
                               'which type of bacterium has developed the greatest resistance to penicillin. They '
                               'obtained pure cultures of five different types of bacteria (A-E) and placed each '
                               'type of bacteria into a separate petri dish with nutrient agar. Once the agar was '
                               'set, a hollow was cut in the agar in the center of each petri dish, using a cork '
                               'borer. Penicillin was then added to the hollows. After incubation at 25°C for 24 '
                               'hours, the petri dishes were examined.',
         'parent_question_number': '2'},
 '2.4': {'page': 4,
         'memo_page': 2,
         'question_stem_text': 'Valentina and Ishika are microbiology students investigating penicillin '
                               'resistance in modern day bacterial cultures. Penicillin had, in the past, been an '
                               'effective antibiotic and so they decided to set up an experiment to determine '
                               'which type of bacterium has developed the greatest resistance to penicillin. They '
                               'obtained pure cultures of five different types of bacteria (A-E) and placed each '
                               'type of bacteria into a separate petri dish with nutrient agar. Once the agar was '
                               'set, a hollow was cut in the agar in the center of each petri dish, using a cork '
                               'borer. Penicillin was then added to the hollows. After incubation at 25°C for 24 '
                               'hours, the petri dishes were examined.',
         'parent_question_number': '2'},
 '2.5': {'page': 4,
         'memo_page': 2,
         'question_stem_text': 'Valentina and Ishika are microbiology students investigating penicillin '
                               'resistance in modern day bacterial cultures. Penicillin had, in the past, been an '
                               'effective antibiotic and so they decided to set up an experiment to determine '
                               'which type of bacterium has developed the greatest resistance to penicillin. They '
                               'obtained pure cultures of five different types of bacteria (A-E) and placed each '
                               'type of bacteria into a separate petri dish with nutrient agar. Once the agar was '
                               'set, a hollow was cut in the agar in the center of each petri dish, using a cork '
                               'borer. Penicillin was then added to the hollows. After incubation at 25°C for 24 '
                               'hours, the petri dishes were examined.',
         'parent_question_number': '2'},
 '2.6': {'page': 4,
         'memo_page': 2,
         'question_stem_text': 'Valentina and Ishika are microbiology students investigating penicillin '
                               'resistance in modern day bacterial cultures. Penicillin had, in the past, been an '
                               'effective antibiotic and so they decided to set up an experiment to determine '
                               'which type of bacterium has developed the greatest resistance to penicillin. They '
                               'obtained pure cultures of five different types of bacteria (A-E) and placed each '
                               'type of bacteria into a separate petri dish with nutrient agar. Once the agar was '
                               'set, a hollow was cut in the agar in the center of each petri dish, using a cork '
                               'borer. Penicillin was then added to the hollows. After incubation at 25°C for 24 '
                               'hours, the petri dishes were examined.',
         'parent_question_number': '2'},
 '3.1.1': {'page': 5,
           'memo_page': 3,
           'question_stem_text': ' Read the extract below and study the graph showing the temperature of a '
                                 'patient suffering with malaria. The malaria parasite is caused by a unicellular '
                                 'organism called Plasmodium. The parasite is transferred to humans by the '
                                 'Anopheles mosquito. Malaria symptoms only appear after 10 days when the first '
                                 'fever attack occurs. The graph below shows the body temperature of a malaria '
                                 'patient over five days.',
           'parent_question_number': '3.1'},
 '3.1.3': {'page': 5,
           'memo_page': 3,
           'question_stem_text': ' Read the extract below and study the graph showing the temperature of a '
                                 'patient suffering with malaria. The malaria parasite is caused by a unicellular '
                                 'organism called Plasmodium. The parasite is transferred to humans by the '
                                 'Anopheles mosquito. Malaria symptoms only appear after 10 days when the first '
                                 'fever attack occurs. The graph below shows the body temperature of a malaria '
                                 'patient over five days.',
           'parent_question_number': '3.1'},
 '3.1.4': {'page': 6,
           'memo_page': 3,
           'question_stem_text': ' Read the extract below and study the graph showing the temperature of a '
                                 'patient suffering with malaria. The malaria parasite is caused by a unicellular '
                                 'organism called Plasmodium. The parasite is transferred to humans by the '
                                 'Anopheles mosquito. Malaria symptoms only appear after 10 days when the first '
                                 'fever attack occurs. The graph below shows the body temperature of a malaria '
                                 'patient over five days.',
           'parent_question_number': '3.1'},
 '3.1.5': {'page': 6,
           'memo_page': 3,
           'question_stem_text': ' Read the extract below and study the graph showing the temperature of a '
                                 'patient suffering with malaria. The malaria parasite is caused by a unicellular '
                                 'organism called Plasmodium. The parasite is transferred to humans by the '
                                 'Anopheles mosquito. Malaria symptoms only appear after 10 days when the first '
                                 'fever attack occurs. The graph below shows the body temperature of a malaria '
                                 'patient over five days.',
           'parent_question_number': '3.1'},
 '3.1.6': {'page': 6,
           'memo_page': 3,
           'question_stem_text': ' Read the extract below and study the graph showing the temperature of a '
                                 'patient suffering with malaria. The malaria parasite is caused by a unicellular '
                                 'organism called Plasmodium. The parasite is transferred to humans by the '
                                 'Anopheles mosquito. Malaria symptoms only appear after 10 days when the first '
                                 'fever attack occurs. The graph below shows the body temperature of a malaria '
                                 'patient over five days.',
           'parent_question_number': '3.1'},
 '3.2.1': {'page': 7,
           'memo_page': 3,
           'question_stem_text': ' Acute HIV infection is the earliest stage of HIV infection, and it generally '
                                 'develops withing 2 to 4 weeks after infection with HIV. During this time, some '
                                 'people have flu-like symptoms, such as fever, headache, and rash. In the acute '
                                 'stage of infection, HIV multiplies rapidly and spreads throughout the body.',
           'parent_question_number': '3.2'},
 '3.2.2': {'page': 7,
           'memo_page': 3,
           'question_stem_text': ' Acute HIV infection is the earliest stage of HIV infection, and it generally '
                                 'develops withing 2 to 4 weeks after infection with HIV. During this time, some '
                                 'people have flu-like symptoms, such as fever, headache, and rash. In the acute '
                                 'stage of infection, HIV multiplies rapidly and spreads throughout the body.',
           'parent_question_number': '3.2'},
 '3.2.3': {'page': 7,
           'memo_page': 4,
           'question_stem_text': ' Acute HIV infection is the earliest stage of HIV infection, and it generally '
                                 'develops withing 2 to 4 weeks after infection with HIV. During this time, some '
                                 'people have flu-like symptoms, such as fever, headache, and rash. In the acute '
                                 'stage of infection, HIV multiplies rapidly and spreads throughout the body.',
           'parent_question_number': '3.2'},
 '3.2.4': {'page': 7,
           'memo_page': 4,
           'question_stem_text': ' Acute HIV infection is the earliest stage of HIV infection, and it generally '
                                 'develops withing 2 to 4 weeks after infection with HIV. During this time, some '
                                 'people have flu-like symptoms, such as fever, headache, and rash. In the acute '
                                 'stage of infection, HIV multiplies rapidly and spreads throughout the body.',
           'parent_question_number': '3.2'},
 '2.7.A': {'page': 4,
           'memo_page': 2,
           'question_stem_text': 'Valentina and Ishika are microbiology students investigating penicillin '
                                 'resistance in modern day bacterial cultures. Penicillin had, in the past, been '
                                 'an effective antibiotic and so they decided to set up an experiment to '
                                 'determine which type of bacterium has developed the greatest resistance to '
                                 'penicillin. They obtained pure cultures of five different types of bacteria '
                                 '(A-E) and placed each type of bacteria into a separate petri dish with nutrient '
                                 'agar. Once the agar was set, a hollow was cut in the agar in the center of each '
                                 'petri dish, using a cork borer. Penicillin was then added to the hollows. After '
                                 'incubation at 25°C for 24 hours, the petri dishes were examined. Valentina and '
                                 'Ishika forgot to set up controls for this experiment. ',
           'parent_question_number': '2.7'},
 '2.7.B': {'page': 4,
           'memo_page': 2,
           'question_stem_text': 'Valentina and Ishika are microbiology students investigating penicillin '
                                 'resistance in modern day bacterial cultures. Penicillin had, in the past, been '
                                 'an effective antibiotic and so they decided to set up an experiment to '
                                 'determine which type of bacterium has developed the greatest resistance to '
                                 'penicillin. They obtained pure cultures of five different types of bacteria '
                                 '(A-E) and placed each type of bacteria into a separate petri dish with nutrient '
                                 'agar. Once the agar was set, a hollow was cut in the agar in the center of each '
                                 'petri dish, using a cork borer. Penicillin was then added to the hollows. After '
                                 'incubation at 25°C for 24 hours, the petri dishes were examined. Valentina and '
                                 'Ishika forgot to set up controls for this experiment. ',
           'parent_question_number': '2.7'},
 '3.1.2.a': {'page': 5,
             'memo_page': 3,
             'question_stem_text': ' Read the extract below and study the graph showing the temperature of a '
                                   'patient suffering with malaria. The malaria parasite is caused by a '
                                   'unicellular organism called Plasmodium. The parasite is transferred to humans '
                                   'by the Anopheles mosquito. Malaria symptoms only appear after 10 days when '
                                   'the first fever attack occurs. The graph below shows the body temperature of '
                                   'a malaria patient over five days. From the chart determine: ',
             'parent_question_number': '3.1.2'},
 '3.1.2.b': {'page': 5,
             'memo_page': 3,
             'question_stem_text': ' Read the extract below and study the graph showing the temperature of a '
                                   'patient suffering with malaria. The malaria parasite is caused by a '
                                   'unicellular organism called Plasmodium. The parasite is transferred to humans '
                                   'by the Anopheles mosquito. Malaria symptoms only appear after 10 days when '
                                   'the first fever attack occurs. The graph below shows the body temperature of '
                                   'a malaria patient over five days. From the chart determine: ',
             'parent_question_number': '3.1.2'},
 '1.row1': {'page': 2,
            'memo_page': 2,
            'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                  'Column I. Each letter may only be used once. Column II: A Gel extract; B HIV; '
                                  'C Pathogens; D Fungus; E B lymphocytes; F Vector; G Protist; H Bacteriophage; '
                                  'I Bacteria; J Virus; K T lymphocytes; L decomposers.',
            'parent_question_number': '1'},
 '1.row2': {'page': 2,
            'memo_page': 2,
            'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                  'Column I. Each letter may only be used once. Column II: A Gel extract; B HIV; '
                                  'C Pathogens; D Fungus; E B lymphocytes; F Vector; G Protist; H Bacteriophage; '
                                  'I Bacteria; J Virus; K T lymphocytes; L decomposers.',
            'parent_question_number': '1'},
 '1.row3': {'page': 2,
            'memo_page': 2,
            'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                  'Column I. Each letter may only be used once. Column II: A Gel extract; B HIV; '
                                  'C Pathogens; D Fungus; E B lymphocytes; F Vector; G Protist; H Bacteriophage; '
                                  'I Bacteria; J Virus; K T lymphocytes; L decomposers.',
            'parent_question_number': '1'},
 '1.row4': {'page': 2,
            'memo_page': 2,
            'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                  'Column I. Each letter may only be used once. Column II: A Gel extract; B HIV; '
                                  'C Pathogens; D Fungus; E B lymphocytes; F Vector; G Protist; H Bacteriophage; '
                                  'I Bacteria; J Virus; K T lymphocytes; L decomposers.',
            'parent_question_number': '1'},
 '1.row5': {'page': 2,
            'memo_page': 2,
            'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                  'Column I. Each letter may only be used once. Column II: A Gel extract; B HIV; '
                                  'C Pathogens; D Fungus; E B lymphocytes; F Vector; G Protist; H Bacteriophage; '
                                  'I Bacteria; J Virus; K T lymphocytes; L decomposers.',
            'parent_question_number': '1'},
 '1.row6': {'page': 2,
            'memo_page': 2,
            'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                  'Column I. Each letter may only be used once. Column II: A Gel extract; B HIV; '
                                  'C Pathogens; D Fungus; E B lymphocytes; F Vector; G Protist; H Bacteriophage; '
                                  'I Bacteria; J Virus; K T lymphocytes; L decomposers.',
            'parent_question_number': '1'},
 '1.row7': {'page': 2,
            'memo_page': 2,
            'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                  'Column I. Each letter may only be used once. Column II: A Gel extract; B HIV; '
                                  'C Pathogens; D Fungus; E B lymphocytes; F Vector; G Protist; H Bacteriophage; '
                                  'I Bacteria; J Virus; K T lymphocytes; L decomposers.',
            'parent_question_number': '1'},
 '1.row8': {'page': 2,
            'memo_page': 2,
            'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                  'Column I. Each letter may only be used once. Column II: A Gel extract; B HIV; '
                                  'C Pathogens; D Fungus; E B lymphocytes; F Vector; G Protist; H Bacteriophage; '
                                  'I Bacteria; J Virus; K T lymphocytes; L decomposers.',
            'parent_question_number': '1'},
 '1.row9': {'page': 2,
            'memo_page': 2,
            'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                  'Column I. Each letter may only be used once. Column II: A Gel extract; B HIV; '
                                  'C Pathogens; D Fungus; E B lymphocytes; F Vector; G Protist; H Bacteriophage; '
                                  'I Bacteria; J Virus; K T lymphocytes; L decomposers.',
            'parent_question_number': '1'},
 '1.row10': {'page': 2,
             'memo_page': 2,
             'question_stem_text': 'Select the name/ or term in Column II which best matches the description in '
                                   'Column I. Each letter may only be used once. Column II: A Gel extract; B HIV; '
                                   'C Pathogens; D Fungus; E B lymphocytes; F Vector; G Protist; H Bacteriophage; '
                                   'I Bacteria; J Virus; K T lymphocytes; L decomposers.',
             'parent_question_number': '1'}}
