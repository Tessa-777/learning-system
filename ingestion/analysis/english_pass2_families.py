"""Authored, disjoint competence families from the real English Pass 1 batch.

Membership rules applied here (enforced again by the builder):
  * every member has a memorandum model answer and no unresolved marking gap;
  * every member is Rung A with no visual dependency and no OCR uncertainty;
  * no family mixes Paper 1 (Language) and Paper 2 (Literature/Writing) records —
    those are different competences and the corpus prompt forbids merging them;
  * family membership is a partition: a record belongs to at most one family;
  * a family needs at least two members in at least two different papers.

Set texts deliberately constrain the literature families: The God of Small
Things appears in the 2014 P2 pair only and Othello in the 2015 P2 pair only, so
the two set-work families that depend on text-specific content carry members
from both papers only where the operation is genuinely generic (character
motive and change, recall of a stated event, interpretation of an image). A
text-specific "theme in [novel]" family is NOT admitted on this batch: each text
occurs in one sitting only, which is a single exemplar, not a repeated pattern.
"""

P1_2016 = 'ENG-2016-NOV-P1'
P1_2017 = 'ENG-2017-NOV-P1'
P1_2018 = 'ENG-2018-JUL-P1'
P2_2014 = 'ENG-2014-JUL-P2'
P2_2015 = 'ENG-2015-JUL-P2'

FAMILIES = [
    {'family_id': 'QUESTION-FAMILY-ENG-001', 'name': 'Explain how diction, register or tone creates a stated effect',
     'topic': 'Language — authorial style', 'operations': ['identify', 'explain effect'],
     'definition': 'Name the register, tone or word-level choice the question asks about and explain the effect it creates on the reader or the message, instead of only labelling it.',
     'members': [(P1_2016, '1.3'), (P1_2016, '1.5.1'), (P1_2016, '6.1'), (P1_2016, '6.4'),
                 (P1_2017, '1.2'), (P1_2017, '1.8'), (P1_2017, '5.1'),
                 (P1_2018, '1.7.1'), (P1_2018, '6.4')]},

    {'family_id': 'QUESTION-FAMILY-ENG-002', 'name': 'Identify and correct an error of grammar, concord or spelling in context',
     'topic': 'Language Structures & Conventions', 'operations': ['identify', 'correct'],
     'definition': 'Locate the specific error in the supplied sentence and supply its corrected form; the task is error repair, not general rewriting.',
     'members': [(P1_2016, '6.2'), (P1_2016, '6.3'), (P1_2016, '6.6'), (P1_2016, '6.7'),
                 (P1_2017, '1.5'), (P1_2017, '5.2'),
                 (P1_2018, '1.4'), (P1_2018, '6.1')]},

    {'family_id': 'QUESTION-FAMILY-ENG-003', 'name': 'Explain how sentence construction or punctuation shapes meaning',
     'topic': 'Language Structures & Conventions', 'operations': ['identify', 'explain effect'],
     'definition': 'Name the syntactic or punctuation feature (repetition and commas, voice, hyphen, capitals, sentence type) and explain what it does to the meaning, emphasis or reader of the sentence.',
     'members': [(P1_2016, '1.7'), (P1_2016, '6.5.1'), (P1_2016, '6.5.2'),
                 (P1_2017, '1.6'),
                 (P1_2018, '6.2'), (P1_2018, '6.5')]},

    {'family_id': 'QUESTION-FAMILY-ENG-004', 'name': 'Interpret a poem\'s imagery, connotation or tone and its effect',
     'topic': 'Poetry — language', 'operations': ['identify', 'explain effect'],
     'definition': 'Identify the figure, image or connotative word the question targets and explain the effect it creates in the poem; naming the device without its work does not answer the question.',
     'members': [(P1_2016, '4.2'), (P1_2016, '4.3'),
                 (P1_2017, '3.1'), (P1_2017, '3.3'), (P1_2017, '3.7.2'),
                 (P1_2018, '4.2'), (P1_2018, '4.3')]},

    {'family_id': 'QUESTION-FAMILY-ENG-005', 'name': 'Explain how a poem\'s structure, form or punctuation shapes its meaning',
     'topic': 'Poetry — form', 'operations': ['identify', 'explain effect'],
     'definition': 'Explain what line arrangement, enjambment, repetition or punctuation does to the pace, emphasis or meaning of the poem, rather than describing the stanza.',
     'members': [(P1_2016, '4.4'),
                 (P1_2017, '3.4'), (P1_2017, '3.5'),
                 (P1_2018, '3.1'), (P1_2018, '3.2'), (P1_2018, '3.3')]},

    {'family_id': 'QUESTION-FAMILY-ENG-006', 'name': 'Compare the treatment of an idea across two poems',
     'topic': 'Poetry — comparative', 'operations': ['compare', 'substantiate'],
     'definition': 'Draw a comparison between two named poems, citing each poem, instead of answering on one poem and mentioning the other.',
     'members': [(P1_2016, '4.6'), (P1_2017, '3.10'), (P1_2018, '4.4')]},

    {'family_id': 'QUESTION-FAMILY-ENG-007', 'name': 'Explain a character\'s motive, change or responsibility using the whole set work',
     'topic': 'Set work — characterisation', 'operations': ['explain', 'substantiate'],
     'definition': 'Account for what a named character does, feels or becomes, and support it with evidence from outside the printed extract; describing the plot does not answer the question.',
     'members': [(P2_2014, '1.4'), (P2_2014, '1.6'), (P2_2014, '1.7'),
                 (P2_2015, '1.2'), (P2_2015, '1.6'), (P2_2015, '1.7'), (P2_2015, '1.8')]},

    {'family_id': 'QUESTION-FAMILY-ENG-008', 'name': 'Recall and relate a specific event, relationship or reference from the set work',
     'topic': 'Set work — content recall', 'operations': ['state', 'relate'],
     'definition': 'State the particular event, relationship or term the question asks about, in the terms the text itself uses; it is a recall task, not a judgment task.',
     'members': [(P2_2014, '1.1'), (P2_2014, '1.2'), (P2_2014, '1.5'), (P2_2014, '1.8'),
                 (P2_2015, '1.1'), (P2_2015, '1.3')]},

    {'family_id': 'QUESTION-FAMILY-ENG-009', 'name': 'Interpret an image, statement or relationship in a set-work extract',
     'topic': 'Set work — close reading', 'operations': ['interpret', 'substantiate'],
     'definition': 'Turn a quoted image, statement or relationship in the printed extract into its meaning in the text, quoting the extract as the memo requires.',
     'members': [(P2_2014, '1.3'), (P2_2014, '1.9'),
                 (P2_2015, '1.4'), (P2_2015, '1.5')]},

    {'family_id': 'QUESTION-FAMILY-ENG-010', 'name': 'Construct a dictionary entry for a word or neologism in context',
     'topic': 'Language — lexical knowledge', 'operations': ['define', 'classify'],
     'definition': 'Give the requested components of a dictionary entry (part of speech, definition, and where asked etymology) for the coinage or word as it is used in the supplied text.',
     'members': [(P1_2017, '5.3'), (P1_2018, '1.7.2')]},

    {'family_id': 'QUESTION-FAMILY-ENG-011', 'name': 'Evaluate the reliability, positioning or success of an argument',
     'topic': 'Language — critical evaluation', 'operations': ['evaluate', 'substantiate'],
     'definition': 'Take a position on how reliable, successfully positioned or effective the writer\'s argument is and substantiate it with the text\'s own evidence, rather than summarising the argument.',
     'members': [(P1_2016, '1.9'), (P1_2017, '1.10'), (P1_2018, '1.5'), (P1_2018, '1.8')]},

    {'family_id': 'QUESTION-FAMILY-ENG-012', 'name': 'Explain the meaning and effect of an idiom or fixed expression',
     'topic': 'Language — figurative usage', 'operations': ['explain', 'explain effect'],
     'definition': 'Unpack what the idiom or altered expression means in its paragraph and, where asked, the effect of its use or the difference from the standard form.',
     'members': [(P1_2016, '1.2'), (P1_2016, '1.6'), (P1_2017, '1.7'), (P1_2018, '1.3')]},

    {'family_id': 'QUESTION-FAMILY-ENG-013', 'name': 'Draw out the implication of a metaphor or extended comparison',
     'topic': 'Language — figurative usage', 'operations': ['interpret', 'explain'],
     'definition': 'Interpret the comparison the writer reaches for (a metaphor, a cartoon figure, a metaphor built from a natural object) and what it implies about the subject.',
     'members': [(P1_2016, '1.4'), (P1_2017, '1.4'), (P1_2018, '1.2')]},

    {'family_id': 'QUESTION-FAMILY-ENG-014', 'name': 'Explain the stated idea, message or title of a poem with quotation',
     'topic': 'Poetry — meaning', 'operations': ['interpret', 'substantiate'],
     'definition': 'Explain the poem\'s central message, title or a stated idea and support the reading with quotation from the poem, as the memo demands.',
     'members': [(P1_2016, '3.1'), (P1_2016, '3.2'), (P1_2016, '3.4'), (P1_2016, '4.1'),
                 (P1_2017, '3.2'), (P1_2017, '3.6'), (P1_2017, '3.9'),
                 (P1_2018, '3.4'), (P1_2018, '4.1')]},

    {'family_id': 'QUESTION-FAMILY-ENG-015', 'name': 'Explain the effect of a rhetorical or opening device',
     'topic': 'Language — authorial purpose', 'operations': ['identify', 'explain effect'],
     'definition': 'Judge or explain what the opening move or rhetorical question does for the reader and the writer\'s purpose, tying it to the text\'s intention.',
     'members': [(P1_2016, '1.1'), (P1_2017, '1.1'), (P1_2018, '1.6')]},
]
