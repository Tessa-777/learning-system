"""Pass 1 evidence table — Grade 11 English Paper 1, 14 November 2016.

Authored by reading the extracted text of the paper (.docx) and its memorandum,
then transcribing each numbered question item and the memorandum's own answer.

Paper: data/organized/english/Grade 11 English P1 Nov 2016.docx   (90 marks)
Memo:  data/organized/english/Grade 11 English P1 Nov Memo 2016.docx (90 marks)

Pairing evidence (printed, not inherited):
  * both documents print the same header block — SUBJECT English, DATE
    14 November, 2016, GRADE 11, MARKS 90, EXAMINER Mrs Nichas, Mr de Reuck,
    Mrs Oosthuysen, Mrs Leeburn, MODERATOR Mrs Nichas;
  * the memo restates the paper's own numbered items 1.1-1.9, 3.1-3.4, 4.1-4.6
    and 6.1-6.7 word-for-word;
  * every attempted pairing must survive that check: the inherited
    document-level stub batch paired this paper with a memorandum from a
    different sitting, and sample_manifest.json was not consulted.

Record tuple layout (see SCHEMA below):
(qn, marks, section, qformat, text, set_text, has_visual, memo_evidence,
 memo_answer, memo_steps, memo_notes, rubric_ref, allocation, needs_visual,
 ocr_uncertain)

MEMO SCOPE (read from the memorandum itself): it answers Question 1, Question 3,
Question 4 and Question 6. Question 2 (summary) is restated with no model answer
and no rubric. Question 5 (visual literacy, 15 marks) has NO marking section at
all — this is recorded, not invented.
"""

PAPER = {
    "paper_key": "ENG-2016-NOV-P1",
    "paper_path": "data/organized/english/Grade 11 English P1 Nov 2016.docx",
    "memo_path": "data/organized/english/Grade 11 English P1 Nov Memo 2016.docx",
    "year": 2016,
    "exam_date": "14 November, 2016",
    "exam_period": "nov",
    "paper_number": "P1",
    "paper_type": "paper1",
    "exam_board": "internal",
    "paper_focus": "Language — reading and viewing (comprehension, summary, poetry, visual literacy, textual editing)",
    "total_marks": 90,
    "examiner": "Mrs Nichas, Mr de Reuck, Mrs Oosthuysen, Mrs Leeburn",
    "moderator": "Mrs Nichas",
    "duration_stated": {"paper": "2 1/2 hours", "memo": "2 1/2 hours"},
    "fidelity_rung": "A",
    "section_totals": {"1": 26, "2": 10, "3/4": 26, "5": 15, "6": 13},
    "section_key_map": {"1": "1", "2": "2", "3": "3/4", "4": "3/4", "5": "5", "6": "6"},
    "section_totals_basis": "printed 'Possible Marks' row of the paper's cover table, which the memo's cover repeats (26/10/26/15/13 = 90)",
    "item_anchor_overrides": {
        "2.1": {"paper": "question 2 – summary10 marks",
                "note": "the summary is a section-level task; its 10 marks are printed in the section heading"},
    },
    "mark_discrepancies": [
        {
            "section": "1",
            "printed_section_total": 26,
            "sum_of_printed_item_marks": 25,
            "detail": (
                "Question 1 is headed 'comprehension 26 marks' but its printed items "
                "1.1-1.9 allocate 3+1+2+2+2+3+3+2+3+4 = 25 marks. The memorandum "
                "restates the same items with the same bracketed marks, so the "
                "shortfall is in the source, not in this transcription. The missing "
                "mark is left unallocated rather than padded onto an item."
            ),
        }
    ],
    "source_hashes": {
        "paper_path": "dc4ca8cbac163a716e9e24eba5a8e83061c6544da874330135478d906fe9afde",
        "memo_path": "a02e13b683dfae947d9ed0d8b505845426df4cb2530194e8400593b1efc4defb",
    },
    "notes": (
        "Paper 1 is a language/reading-and-viewing paper: comprehension, summary, "
        "seen and unseen poetry, visual literacy and textual editing. It contains no "
        "set-work literature section and must not be merged with a Paper 2 family. "
        "TEXT 1 is a David Brooks New York Times column ('Modern toughness', "
        "30 August 2016); TEXT 2 is 'Humans have in-built time limit'; the poems are "
        "'Release, February 1990' (Lynne Bryer) and 'Blessing' (Imtiaz Dharker). "
        "Visual literacy refers to TEXTS 3-6, which are images."
    ),
}

SCHEMA = (
    "qn", "marks", "section", "qformat", "text", "set_text", "has_visual",
    "memo_evidence", "memo_answer", "memo_steps", "memo_notes", "rubric_ref",
    "allocation", "needs_visual", "ocr_uncertain",
)

RECORDS = [
    # ---------------- QUESTION 1: COMPREHENSION (header 26; items total 25) ----------------
    ("1.1", 3, "Comprehension", "Extended/Paragraph Response",
     "David Brooks writes a weekly newspaper column for the New York Times. Judge whether "
     "the opening sentence of TEXT 1 is appropriate by considering the content and purpose "
     "of the column.", None, False,
     "model_answer",
     "The opening sentence is appropriate as it is written in a conversational style which "
     "fits with the style of a newspaper column. He includes a quote to introduce his topic "
     "on the fragility of today's youth. His purpose is to inform and raise awareness for "
     "this issue. He seeks to air his views and encourages the reader to follow the journey "
     "with him.",
     ["Style judgment: conversational style suits a newspaper column",
      "Content: quote introduces the topic of youth fragility",
      "Purpose: to inform and raise awareness",
      "Effect on reader: invites the reader to follow the argument"],
     "Three marks cover style, content and purpose; a bare 'yes it is appropriate' earns nothing.",
     False, "allocated", False, False),

    ("1.2", 1, "Comprehension", "Short Answer",
     "Explain the meaning of the idiom, 'that rings true to me' in paragraph 2.", None, False,
     "model_answer",
     "The writer agrees with the idiom, it is true for him.",
     ["writer agrees / it is true for him"],
     "One mark only; the idiom must be explained, not merely identified.",
     False, "allocated", False, False),

    ("1.3", 2, "Comprehension", "Extended/Paragraph Response",
     "Quote an example of informal language used in paragraph 3 and explain its effectiveness.",
     None, False, "model_answer",
     "'If you hang around', 'once upon a time', 'kids were raised' — the writer seeks to draw "
     "the reader into the text, making the reader feel part of the conversation.",
     ["Quotation of an informal expression from paragraph 3",
      "Effect: draws the reader in / makes the reader part of the conversation"],
     "The mark pair splits quotation from explanation; a quotation alone is not enough.",
     False, "allocated", False, False),

    ("1.4", 2, "Comprehension", "Extended/Paragraph Response",
     "What is the writer implying about young people when he refers to the 'orchid generation'?",
     None, False, "model_answer",
     "Like orchids, young people are fragile, gentle, beautiful but difficult to grow and maintain.",
     ["fragile / over-protected",
      "comparison carried through: beautiful but hard to maintain"],
     "Requires the implication of the metaphor, not a restatement of the phrase.",
     False, "allocated", False, False),

    ("1.5.1", 2, "Comprehension", "Extended/Paragraph Response",
     "Examine the use of diction in paragraph 8. Explain the difference in the connotations of "
     "the words 'hard' and 'ardent' in the context of the paragraph.", None, False, "model_answer",
     "'hard' — tough, unbending, immovable. 'ardent' — strong, enthusiastic, intense. Therefore "
     "the people we admire are not immovable and inflexible; rather they are strong and intensely "
     "enthusiastic about what they believe and are completely committed to their ideals.",
     ["connotations of 'hard' (tough, unbending, immovable)",
      "connotations of 'ardent' (strong, enthusiastic, intense)",
      "the contrast applied to the people the writer admires"],
     "Diction question: both words must be unpacked and contrasted; one word alone caps the mark.",
     False, "allocated", False, False),

    ("1.5.2", 3, "Comprehension", "Extended/Paragraph Response",
     "Identify the idiomatic expression used in paragraph 9 that would support your answer to "
     "1.5.1 and explain how this contradicts the writer's earlier assertions about young people.",
     None, False, "model_answer",
     "'strong like water' — young people are strong rather than fragile like orchids; they are "
     "more resilient than we give them credit for. Earlier the writer alluded to young people "
     "being weak and the victims of helicopter parenting, over-protected and unable to deal with "
     "setbacks. This idiom contradicts that.",
     ["identification of the idiom 'strong like water'",
      "explanation that it asserts resilience rather than fragility",
      "explicit contradiction of the earlier helicopter-parenting claim"],
     "Three marks require identification plus the contradiction; a cross-reference back to 1.5.1 "
     "is demanded by the wording.",
     False, "allocated", False, False),

    ("1.6", 3, "Comprehension", "Extended/Paragraph Response",
     "The writer uses the expression, 'means inspired by an end' in paragraph 11. How does this "
     "meaning differ from the original expression, 'means to an end' and why does the writer "
     "choose the first expression?", None, False, "model_answer",
     "'means inspired by an end' — positive connotations of being inspired by a lofty goal; you "
     "are focused and driven to achieve that goal. 'means to an end' — a person who will do "
     "whatever it takes to reach the desired result; this may not be good as any avenue could be "
     "pursued regardless of ethics. The writer would seek to inspire his readers rather than "
     "present them as arrogant, overly ambitious individuals who merely seek their own gain, "
     "therefore he uses the first expression.",
     ["meaning of the altered expression (inspired by a lofty goal)",
      "meaning of the original idiom (whatever it takes, regardless of ethics)",
      "reason for the writer's choice (to inspire, not to imply arrogance)"],
     "Three marks: both meanings plus the persuasive motive for the substitution.",
     False, "allocated", False, False),

    ("1.7", 2, "Comprehension", "Extended/Paragraph Response",
     "What is the effect of the use of repetition and commas in paragraph 12?", None, False,
     "model_answer",
     "The repeated phrases 'may have not been intrinsically tough/steadfast/gritty, but was "
     "tough/steadfast' emphasise the contrast in the lines and lead to a climax in the paragraph. "
     "The commas list related ideas or separate main from subordinate clauses.",
     ["repetition emphasises the contrast and builds to a climax",
      "commas list related ideas / separate clause elements"],
     "Two devices, two marks; both must be addressed.",
     False, "allocated", False, False),

    ("1.8", 3, "Comprehension", "Extended/Paragraph Response",
     "Do you agree with the writer's view in paragraphs 16-18 regarding mental toughness in "
     "people today? Explain your answer with close reference to these paragraphs.", None, False,
     "rubric_reference",
     "Must refer to the paragraphs by quoting. Use IEB rubric for this answer.",
     ["memo gives a rubric instruction rather than a model answer",
      "IEB rubric (not printed in this memorandum) governs the mark"],
     "The memo instructs markers to use the IEB rubric and to require quotation from paragraphs "
     "16-18. No rubric descriptors are printed in the memorandum, so the criteria cannot be "
     "transcribed here.",
     True, "allocated", False, False),

    ("1.9", 4, "Comprehension", "Extended/Paragraph Response",
     "Considering the extract above and the information from TEXT 1, how would Joel Stein answer "
     "David Brooks if the following question was asked of him, 'Do young people (millennials) "
     "today have the strength of character to succeed?' Your answer needs to make reference to "
     "both texts.", None, False, "model_answer",
     "Joel Stein would probably say that although millennials have the potential to succeed, they "
     "are narcissistic and carry an air of entitlement. He would say that they are focused on "
     "themselves and on climbing the mountain in order to achieve fame and glory and attribute "
     "success to that ideal. He would say that young people are bored easily and he would agree "
     "with Brooks in saying that young people are unable to face difficulties, e.g. with their "
     "bosses or what they perceive to be boring work. Brooks ultimately believes that young people "
     "are strong and have the potential to succeed, which Stein is sceptical about.",
     ["adopt Stein's position (narcissism, entitlement)",
      "support it from the Stein extract",
      "contrast it with Brooks' position in TEXT 1",
      "synthesise the two texts into an answer to the question posed"],
     "Memo ends with 'Use IEB rubric.' — the four marks are rubric-marked as well as modelled.",
     True, "allocated", False, False),

    # ---------------- QUESTION 2: SUMMARY (10 marks) ----------------
    ("2.1", 10, "Summary", "Extended/Paragraph Response",
     "Refer to TEXT 2, \"Humans have in-built time limit\" and answer the following question. Text 2 "
     "asks some interesting ethical questions regarding the new research claiming we may soon hit a "
     "natural lifespan limit of 115 years. The questions are: 'Can we change that?' and 'Should we?' "
     "By summarising TEXT 2 in not more than 90 words, write an overview of the research in this "
     "area for a class report. Your summary should focus on the aspects of the text that support your "
     "stance to the questions above. Your response must be in the form of one coherent paragraph. "
     "You must use full sentences. Your language use must be accurate and in an appropriate register. "
     "Provide an appropriate title which is included in your word count. Provide an accurate word "
     "count at the end of the summary. Use your own words. 'Cutting and pasting' of information is "
     "not acceptable.", None, False, "restated_only",
     "NOT ANSWERED IN THE MEMORANDUM — the memorandum restates the task and its instructions "
     "but prints no model summary, no mark breakdown and no rubric.",
     ["no marking evidence printed"],
     "Marking requirements for the summary cannot be derived from this memorandum. Recorded as a "
     "marking-evidence gap; the 10 marks are allocated by the paper.",
     False, "allocated", False, False),

    # ---------------- QUESTION 3: SEEN POETRY (10 of the 26 combined poetry marks) ----------------
    ("3.1", 2, "Poetry (Seen)", "Extended/Paragraph Response",
     "Read the poem 'Release, February 1990' by Lynne Bryer. Contrast the perceptions of Mandela "
     "in stanzas one and two. Quote to support your answer.", "Release, February 1990", False,
     "model_answer",
     "Stanza 1 — Mandela is a grandfather, kind, wise. Stanza 2 — he is perceived to be a bogeyman "
     "or a warrior. Plus quotes.",
     ["contrast of stanza 1 perception (grandfather, kind, wise)",
      "contrast of stanza 2 perception (bogeyman / warrior)",
      "supporting quotation"],
     "The memo's '+quotes' makes the quotation compulsory alongside the contrast.",
     False, "allocated", False, False),

    ("3.2", 3, "Poetry (Seen)", "Extended/Paragraph Response",
     "Explain the reference to fate in the poem and its link to Mandela as a messiah.",
     "Release, February 1990", False, "model_answer",
     "It was time that Mandela was released from prison; SA could stand no more delay. It was part "
     "of destiny for SA to end apartheid. Mandela is therefore perceived to be a messiah who is "
     "capable of 'saving' the country from danger, fear, bitterness and civil war.",
     ["fate/destiny: the time had come",
      "the country could stand no more delay",
      "Mandela as messiah who saves the country"],
     "Three linked steps; the messiah link must be argued from the poem's own language.",
     False, "allocated", False, False),

    ("3.3", 3, "Poetry (Seen)", "Extended/Paragraph Response",
     "Examine the diction in stanzas 3 and 4. How does the diction show a shift in tone in these "
     "stanzas?", "Release, February 1990", False, "model_answer",
     "Stanza 3 — tone is somewhat harsh, using dark imagery: 'burned, dark, snakes, writhing, "
     "night' to describe the fear of some in the country. Stanza 4 — tone becomes more gentle, "
     "excited, accepting that it was time for Mandela to be released and for SA to start a new "
     "era: 'elated, cool, not doubting, destined'.",
     ["stanza 3 diction and the harsh/dark tone it creates",
      "stanza 4 diction and the gentler, accepting tone",
      "the shift explicitly named"],
     "Requires quotation from both stanzas plus a statement of the shift.",
     False, "allocated", False, False),

    ("3.4", 2, "Poetry (Seen)", "Extended/Paragraph Response",
     "Explain the meaning of the paradox in line 32 and how it affects the message of the poem "
     "as a whole.", "Release, February 1990", False, "model_answer",
     "South Africans were dislocated; apartheid ensured separation and discrimination. Yet the "
     "line draws together dislocation with a calmness of knowing — South Africans knew their "
     "destiny was about to change and this brought a feeling of peace.",
     ["explanation of the paradox (dislocated yet calm)",
      "effect on the poem's message as a whole (peaceful certainty of change)"],
     "Both the local paradox and its effect on the whole poem are marked.",
     False, "allocated", False, False),

    # ---------------- QUESTION 4: UNSEEN POETRY (16 of the 26 combined poetry marks) ----------------
    ("4.1", 2, "Poetry (Unseen)", "Extended/Paragraph Response",
     "In light of the content presented in the poem, why is the title effective? Quote from the poem "
     "to support your answer.", "Blessing", False,
     "model_answer",
     "The title refers to the 'blessing' of water, the life that it provides: 'Sometimes a sudden "
     "rush of fortune, silver crashes to the ground, blessing sings over their small bones.'",
     ["the title's meaning: water as a blessing, the life it provides",
      "quotation supporting it"],
     "Judgement of the title plus a quotation; the quotation carries part of the mark.",
     False, "allocated", False, False),

    ("4.2", 2, "Poetry (Unseen)", "Extended/Paragraph Response",
     "Provide an example of religious imagery from the poem. Discuss the connotations of the image "
     "you have chosen.", "Blessing", False, "model_answer",
     "'voice of a kindly god' — water is so precious that even one drop of it is like a god in a "
     "cup. 'a congregation' — the people who rush from their huts when there is water are like a "
     "congregation in a church who listen to the word of God. 'the blessing sings' — water likened "
     "to a blessing singing a hymn of praise over the people.",
     ["identification of religious imagery",
      "connotations of the chosen image spelled out"],
     "The memo gives three acceptable images; any one, correctly connotated, earns the marks.",
     False, "allocated", False, False),

    ("4.3", 2, "Poetry (Unseen)", "Extended/Paragraph Response",
     "Examine the figurative language in stanza 1. How do the use of personification and the "
     "simile emphasise the lack of water in the region?", "Blessing", False, "model_answer",
     "The earth is likened to skin that is so dry it cracks like a pod of a pea or a flower. The "
     "earth is thirsty and dry.",
     ["simile: skin cracking like a pod",
      "personification of the earth as thirsty/dry",
      "both tied to the lack of water"],
     "Two named devices (personification and simile) must both be dealt with; the memo's answer "
     "rewards the effect, i.e. drought.",
     False, "allocated", False, False),

    ("4.4", 3, "Poetry (Unseen)", "Extended/Paragraph Response",
     "How does the structure of stanza 3 reflect the action described in the poem?", "Blessing",
     False, "model_answer",
     "Structure — short lines, listing of images, items of value are used as containers, people "
     "rush to get water. The pace of the poem is quickened with the shortened lines; people are "
     "frantically trying to collect water.",
     ["short lines / listing identified as the structural feature",
      "effect: quickened pace",
      "link to the frantic action of collecting water"],
     "Requires the form-to-meaning link, not just describing the stanza.",
     False, "allocated", False, False),

    ("4.5", 3, "Poetry (Unseen)", "Short Answer",
     "Which of the following visuals best capture the mood of stanza 4? Quote from stanza 4 to "
     "support your answer. (Visual A and Visual B are printed as images in the paper.)",
     "Blessing", True, "model_answer",
     "Boys will probably choose Visual A as the stanza speaks of naked children screaming with "
     "delight at the water that gushes over their thin bodies; the water glistens as it covers "
     "them. If they refer to Visual B, it would be to enhance the effect of the drought/dryness "
     "mentioned in the poem, the feeling created just before the water pipe bursts.",
     ["choice of visual",
      "quotation from stanza 4",
      "justification linking chosen visual to the stanza's mood"],
     "The memo itself hedges ('boys will probably choose...'), so the justification matters more "
     "than the choice. The two visuals are images and cannot be verified from the text layer.",
     False, "allocated", True, False),

    ("4.6", 4, "Poetry (Unseen)", "Extended/Paragraph Response",
     "Considering Release and Blessing, discuss the nature of hope as it is presented in both the "
     "poems. Your answer needs to include a reference to who is seen to be hopeful and for what "
     "reasons. You also need to substantiate your reasoning with careful reference to both poems.",
     "Release, February 1990; Blessing", False, "model_answer",
     "In 'Release', the poet suggests that the release of Mandela from prison has given the "
     "country hope much like a messiah brings hope. Mandela was seen to be the person who would "
     "unite the country and his emerging from prison was a sign of the peace that would follow. "
     "Even though some feared a civil war, there was a calm sense of knowing that hope would "
     "inspire change. In 'Blessing', hope is inspired by water, which in turn gives life to the "
     "community around it. Water is a symbol of hope which could be linked to the hope of "
     "releasing an icon in Mandela; he is like water cleansing the country of its past.",
     ["hope in 'Release': who is hopeful (the country) and why (Mandela's release as messianic)",
      "hope in 'Blessing': who is hopeful (the community) and why (water as life)",
      "comparison / link between the two presentations of hope",
      "textual substantiation from both poems"],
     "Cross-poem comparison question; both poems must be quoted and the 'who and why' requirement "
     "answered explicitly.",
     False, "allocated", False, False),

    # ---------------- QUESTION 5: VISUAL LITERACY (15 marks — NO MEMO SECTION) ----------------
    ("5.1", 3, "Visual Literacy", "Extended/Paragraph Response",
     "Refer to TEXT 3, a world map of child labour. Provide a justified reason for the areas which "
     "make the most use of child labour. In your answer also identify whose interests are being "
     "served in the creation of this map.", None, True, "none",
     "NOT ANSWERED IN THE MEMORANDUM — the supplied memorandum contains no Question 5 / visual "
     "literacy marking section at all.",
     ["no marking evidence printed"],
     "Marking evidence is absent; the question and its 3 marks are recorded from the paper only.",
     False, "allocated", True, False),

    ("5.2", 4, "Visual Literacy", "Extended/Paragraph Response",
     "Refer to TEXT 4. Identify 2 possible long-term consequences of child labour on the emotional, "
     "social and economic development of children affected by these circumstances. Substantiate "
     "your answer.", None, True, "none",
     "NOT ANSWERED IN THE MEMORANDUM — no Question 5 marking section is present.",
     ["no marking evidence printed"],
     "Two consequences across three domains are demanded by the wording; impossible to verify "
     "marking without the memo.",
     False, "allocated", True, False),

    ("5.3", 5, "Visual Literacy", "Extended/Paragraph Response",
     "Refer to TEXTS 5 and 6. How is the reader positioned to view the targeted company in these "
     "texts? Provide visual and verbal clues from each of the texts to justify your answer.",
     None, True, "none",
     "NOT ANSWERED IN THE MEMORANDUM — no Question 5 marking section is present.",
     ["no marking evidence printed"],
     "Bias/positioning question over two images; no memo evidence available.",
     False, "allocated", True, False),

    ("5.4", 3, "Visual Literacy", "Extended/Paragraph Response",
     "Discuss which text (TEXT 5 or TEXT 6) you believe would have the most impact in wealthy "
     "societies. Justify your answer.", None, True, "none",
     "NOT ANSWERED IN THE MEMORANDUM — no Question 5 marking section is present.",
     ["no marking evidence printed"],
     "Evaluation-style question; no memo evidence available.",
     False, "allocated", True, False),

    # ---------------- QUESTION 6: TEXTUAL EDITING (13 marks) ----------------
    ("6.1", 2, "Language Structures & Conventions", "Extended/Paragraph Response",
     "Read TEXT 7, 'Watch Less Television!'. How does the writer's use of pronouns in paragraph 1 "
     "position the reader?", None, False, "model_answer",
     "The writer addresses the reader directly by writing in the second person. The reader is "
     "positioned as the person who watches too much TV and, therefore, is not living their life.",
     ["identification of second-person address",
      "effect: the reader is positioned as the over-watcher"],
     "Requires the grammatical observation plus its effect on the reader.",
     False, "allocated", False, False),

    ("6.2", 2, "Language Structures & Conventions", "Short Answer",
     "Identify and correct the grammatical error that occurs in the last sentence of paragraph 2.",
     None, False, "model_answer",
     "Split infinitive 'to truly expect' — what truly to expect.",
     ["identification of the error (split infinitive)",
      "correction supplied"],
     "Both identification and correction are required for the two marks.",
     False, "allocated", False, False),

    ("6.3", 2, "Language Structures & Conventions", "Short Answer",
     "Correct the TWO spelling mistakes in paragraphs 3 and 5.", None, False, "model_answer",
     "Advertisment — advertisement; You're — your.",
     ["advertisment — advertisement",
      "you're — your"],
     "One mark per word; the memo supplies both exactly.",
     False, "allocated", False, False),

    ("6.4", 1, "Language Structures & Conventions", "Short Answer",
     "Provide a synonym for the word 'immune' (paragraph 3).", None, False, "model_answer",
     "Resistant, safe, protected.",
     ["any acceptable synonym"],
     "One mark; the memo accepts three alternatives.",
     False, "allocated", False, False),

    ("6.5.1", 1, "Language Structures & Conventions", "Short Answer",
     "Rewrite the following sentence in the passive voice: 'These real people are facing real "
     "problems.'", None, False, "model_answer",
     "Real problems are being faced by real people.",
     ["accurate passive transformation"],
     "One mark for the transformation.",
     False, "allocated", False, False),

    ("6.5.2", 2, "Language Structures & Conventions", "Extended/Paragraph Response",
     "Why is this particular sentence more effective when written in the active voice?", None, False,
     "model_answer",
     "The paragraph from which this sentence comes is about these 'real people'. The problems they "
     "face are secondary to the people, therefore these 'real people' should be the focus of the "
     "sentence, the subject of the sentence.",
     ["the paragraph's focus is the people, not the problems",
      "the active voice keeps 'real people' as subject / focus"],
     "Requires a reasoned answer about emphasis and sentence focus.",
     False, "allocated", False, False),

    ("6.6", 1, "Language Structures & Conventions", "Short Answer",
     "Identify the syntax (sentence construction) error in sentence 1 of paragraph 6.", None, False,
     "model_answer",
     "Tautology, 'less satisfaction and fulfilment'.",
     ["tautology identified"],
     "One mark; the memo names the error type and the phrase.",
     False, "allocated", False, False),

    ("6.7", 2, "Language Structures & Conventions", "Short Answer",
     "Identify and correct the grammatical error in sentence 2 of paragraph 6.", None, False,
     "model_answer",
     "Concord error ('TV viewers reports') should be 'TV viewers report'.",
     ["identification of the concord error",
      "correction supplied"],
     "Sentence 2 of paragraph 6 is 'According to the Journal of Economic Psychology, TV viewers "
     "reports lower life satisfaction...' — the concord error is in the subject-verb agreement of "
     "'viewers reports'.",
     False, "allocated", False, False),
]
