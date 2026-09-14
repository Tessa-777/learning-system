"""Pass 1 evidence table — Grade 11 English Paper 1, July 2018.

Authored by reading the extracted text of the paper (PDF) and its memorandum.

Paper: data/organized/english/Grade 11 Paper 1 July 2018.pdf       (90 marks)
Memo:  data/organized/english/Grade 11 Paper 1 July 2018 Memo.pdf  (90 marks)

Pairing evidence (printed, not inherited): both documents carry the identical
header block — SUBJECT ENGLISH PAPER 1, DATE July 2018, GRADE 11, MARKS 90,
EXAMINERS Mrs Oosthuysen, Mrs Nichas, MODERATOR Mrs Nichas, DURATION 2 1/2 hours
— and the identical cover row 'Possible Marks 25 10 20 25 10 90'; the memo
restates every numbered item with the same bracketed marks.

SOURCE ABNORMALITIES PRESERVED (not silently corrected):
  * Question 6 (textual editing) is headed 'QUESTION 6 10 MARKS' but its items
    are mis-numbered 5.1-5.5 in both the paper and the memo. Records here use
    the logical numbers 6.1-6.5 and carry printed_question_number = 5.x.
  * Question 5's printed section total is 25 marks while its own items allocate
    2+3+2+2+2+3+2+5+3 = 24. The shortfall is declared, not padded.
"""

PAPER = {
    "paper_key": "ENG-2018-JUL-P1",
    "paper_path": "data/organized/english/Grade 11 Paper 1 July 2018.pdf",
    "memo_path": "data/organized/english/Grade 11 Paper 1 July 2018 Memo.pdf",
    "year": 2018,
    "exam_date": "July 2018",
    "exam_period": "july",
    "paper_number": "P1",
    "paper_type": "paper1",
    "exam_board": "internal",
    "paper_focus": "Language — reading and viewing (comprehension, summary, poetry, visual literacy, textual editing)",
    "total_marks": 90,
    "examiner": "Mrs Oosthuysen, Mrs Nichas",
    "moderator": "Mrs Nichas",
    "duration_stated": {"paper": "2 1/2 hours", "memo": "2 1/2 hours"},
    "fidelity_rung": "A",
    "section_totals": {"1": 25, "2": 10, "3/4": 20, "5": 25, "6": 10},
    "section_key_map": {"1": "1", "2": "2", "3": "3/4", "4": "3/4", "5": "5", "6": "6"},
    "section_totals_basis": "printed 'Possible Marks' row (25 10 20 25 10 90) with printed section headers QUESTION 3 10 MARKS and QUESTION 4 10 MARKS combining to the table's 3/4 column",
    "section_anchors": [
        "QUESTION 1 25 MARKS", "QUESTION 2 10 MARKS", "QUESTION 3 10 MARKS",
        "QUESTION 4 10 MARKS", "QUESTION 5 25 MARKS", "QUESTION 6 10 MARKS",
    ],
    "memo_section_anchors": [
        "QUESTION 1 25 MARKS", "QUESTION 2 10 MARKS", "QUESTION 3 10 MARKS",
        "QUESTION 4 10 MARKS", "QUESTION 5 25 MARKS", "QUESTION 6 10 MARKS",
    ],
    "printed_numbering": {
        "6": {
            "printed_prefix": "5",
            "note": "The paper heads the textual-editing section 'QUESTION 6 10 MARKS' but numbers its items 5.1-5.5; the memo repeats the same mis-numbering.",
        }
    },
    "item_anchor_overrides": {
        "2.1": {"paper": "QUESTION 2 10 MARKS",
                "note": "the summary is a section-level task; its 10 marks are printed in the section heading"},
    },
    "mark_discrepancies": [
        {
            "section": "5",
            "printed_section_total": 25,
            "sum_of_printed_item_marks": 24,
            "detail": (
                "Question 5 is headed 'QUESTION 5 25 MARKS' but its printed items allocate "
                "5.1(2) + 5.2(3) + 5.3.1(2) + 5.3.2(2) + 5.4(2) + 5.5(3) + 5.6(2) + 5.7(5) + 5.8(3) = 24. "
                "The memorandum restates the same items with the same brackets, so the missing mark "
                "belongs to the source; it is declared rather than added to an item."
            ),
        }
    ],
    "source_hashes": {
        "paper_path": "9edc4f2cf8ee98d695ed262175407b3f7bb24a93e116b98b95fc2502d3091b88",
        "memo_path": "9937237e0658ac60c61b99e836429f101052c37954051de48658e69cdef871d6",
    },
    "notes": (
        "Paper 1 language paper. TEXT 1 is 'South Africa's #MeToo gap: No accountability for "
        "high-profile men' (Shaazia Ebrahim, 05 Dec 2017); TEXT 2 is 'Global Migration'; the seen "
        "poem is e.e. cummings' 'i thank You God for most this amazing'; the unseen poems are "
        "Dennis Brutus' 'Nightsong: City' and W.B. Yeats' 'The Second Coming'; TEXTS 3-4 are AIDS "
        "advertisements (images); TEXT 5 is 'The Greatest Soccer players of all time' (Jon O'Brien, 2017). "
        "The comprehension, summary and textual-editing items are language skill items and must not "
        "be merged with the Paper 2 set-work literature families."
    ),
}

SCHEMA = (
    "qn", "marks", "section", "qformat", "text", "set_text", "has_visual",
    "memo_evidence", "memo_answer", "memo_steps", "memo_notes", "rubric_ref",
    "allocation", "needs_visual", "ocr_uncertain",
)

STEMS = {
    "1.7.1": "Refer to paragraph 7: 'We can bang on about #16DaysofActivism all we like but if we can't address the trashy behaviour of our leaders then these campaigns are just window dressing.'",
    "1.7.2": "Refer to paragraph 7: 'We can bang on about #16DaysofActivism all we like but if we can't address the trashy behaviour of our leaders then these campaigns are just window dressing.'",
}

RECORDS = [
    # ---------------- QUESTION 1: COMPREHENSION (25) ----------------
    ("1.1", 1, "Comprehension", "Short Answer",
     "In your own words, define what the #MeToo movement entails.", None, False, "model_answer",
     "A movement that seeks to campaign against violence against women and children, sexual misconduct.",
     ["movement against violence/sexual misconduct"],
     "One mark; 'in your own words' forbids lifting the text's phrasing.",
     False, "allocated", False, False),

    ("1.2", 2, "Comprehension", "Extended/Paragraph Response",
     "Explain why it would be appropriate for the writer to refer to the movement as sending "
     "'shockwaves' across the US. In your answer, consider the connotations of the word 'shockwaves'.",
     None, False, "model_answer",
     "Earthquake metaphor — to explain the impact of the abuse, the number of people involved, the "
     "status of the people involved (high profile) and how far-reaching it is. Shocked reaction to "
     "the events. The repercussions of the movement are felt across the country.",
     ["earthquake metaphor / connotation of shockwaves",
      "impact: scale, high-profile accused, far-reaching repercussions"],
     "The memo's own note adds that depth and layering of ideas are essential.",
     False, "allocated", False, False),

    ("1.3", 2, "Comprehension", "Extended/Paragraph Response",
     "Explain the meaning of the idiomatic expression, 'call men in power out' as it has been used "
     "in paragraph 3.", None, False, "model_answer",
     "To name and shame men of status in society, to make them accountable for their actions.",
     ["name and shame / hold accountable", "men of status or power"],
     "Idiom must be glossed in context.",
     False, "allocated", False, False),

    ("1.4", 2, "Comprehension", "Short Answer",
     "Identify and correct the grammar error in the sentence, 'South Africa, however, does not seem "
     "to know how to call men in power out.'", None, False, "model_answer",
     "Dangling/misplaced preposition — to know how to call out men in power.",
     ["identification of the misplaced/dangling preposition", "corrected sentence"],
     "Both identification and correction carry the two marks.",
     False, "allocated", False, False),

    ("1.5", 3, "Comprehension", "Extended/Paragraph Response",
     "How reliable is the writer's argument in paragraph 4? Your answer should consider diction and tone.",
     None, False, "model_answer",
     "His argument is reliable as he quotes stats provided by SA Medical Research Council to support "
     "his answer: '21% over the age of 18 reported that they'd experienced violence at the hands of a "
     "partner.' Tone is formal, accusatory, harsh — 'unreported', 'femicide rate', '5 times higher', "
     "'poorest households'. So emotive language might lead to an opinionated argument which may lower "
     "the reliability as the writer wishes to persuade the reader of his point of view.",
     ["evidence of reliability: cited statistics / source",
      "diction and tone named and illustrated",
      "judgement: emotive language can reduce reliability"],
     "The memo's note: 'Depth and complexity of answer is essential here. Layering of ideas and proof.'",
     False, "allocated", False, False),

    ("1.6", 2, "Comprehension", "Extended/Paragraph Response",
     "Explain the effectiveness of the rhetorical question in paragraph 6?", None, False,
     "model_answer",
     "Raise awareness for violence and take action against abuse. Do something about the violence.",
     ["effect: compels awareness / action in the reader"],
     "Two marks for the effect on the reader.",
     False, "allocated", False, False),

    ("1.7.1", 3, "Comprehension", "Extended/Paragraph Response",
     "Identify the register used in the sentence above. How does the use of register affect the "
     "message of the text?", None, False, "model_answer",
     "Informal, colloquial register. Draws the reader into the text, makes them feel part of the "
     "discussion. It highlights the dirty, repulsive nature of the sexual acts. Writer is being harsh "
     "and blunt.",
     ["register identified (informal/colloquial)",
      "effect on the reader (draws them in / makes them part of the discussion)",
      "effect on the message (blunt, harsh, highlights the repulsive nature)"],
     "For 'call men in power out' the memo expects a colloquial register label plus effect.",
     False, "allocated", False, False),

    ("1.7.2", 3, "Comprehension", "Extended/Paragraph Response",
     "Provide a dictionary definition for #16DaysofActivism. Your entry needs to include a part of "
     "speech, definition and etymology (word origin).", None, False, "model_answer",
     "#16DaysofActivism n. 16 days, or a period of time in which people speak out against abuse and "
     "actively try to combat it. From social campaigns / social media handle. Joining of words to "
     "create a handle or name of campaign.",
     ["part of speech",
      "definition",
      "etymology / word origin (coined as a social-media handle)"],
     "Three marks: part of speech, definition, etymology — missing any one loses its mark.",
     False, "allocated", False, False),

    ("1.8", 3, "Comprehension", "Extended/Paragraph Response",
     "Evaluate how successful the hashtags and awareness campaigns could be in addressing "
     "discrimination in South Africa.", None, False, "model_answer",
     "Hashtags are generally not successful / have limited success as they raise awareness but "
     "don't inspire action. 'Window-dressing' — they present ideas and dress it up but don't offer "
     "opportunities to make a difference. Hashtags trend but are forgotten often. (Some who seek "
     "revenge against an alleged attack, could attach their names to the campaign to validate their "
     "experiences.)",
     ["evaluation: limited success — awareness without action",
      "the 'window-dressing' judgement",
      "counter-consideration: campaigns trend then are forgotten / may be misused"],
     "Requires an evaluative stance; a description of what the campaigns do would not earn these "
     "marks. Three marks over the judgement, the reason and the counter-consideration.",
     False, "allocated", False, False),

    ("1.9", 4, "Comprehension", "Extended/Paragraph Response",
     "Considering the title of the article and the cartoon below, how does the writer position "
     "herself in relation to her subject matter? Refer to visual and verbal details in your answer. "
     "(A cartoon showing faceless women labelled 'me too' is printed with the question.)", None, True,
     "model_answer",
     "The cartoon reveals a number of women who have been abused, 'me too'. They are faceless, have "
     "no facial features and are therefore not considered to be important. They don't want to be "
     "identified as victims. The writer raises awareness for the shocking nature of SA abuse and that "
     "this campaign needs to be broadened as this campaign has not gone far enough. Even at the "
     "highest levels of government, abuse is not being adequately addressed and insufficient "
     "convictions have been made. 'No accountability', 'me too gap', 'high-profile men' — emotive "
     "words in the title accuse SA of not dealing adequately with this issue.",
     ["reading of the cartoon (faceless women, anonymity, importance)",
      "reading of verbal details (title's emotive diction)",
      "positioning of the writer (raising awareness, accusing, arguing the campaign has not gone far enough)"],
     "The cartoon is an image; the memo's answer supplies the reading, but the visual itself cannot be "
     "verified from the text layer.",
     False, "allocated", True, False),

    # ---------------- QUESTION 2: SUMMARY (10) ----------------
    ("2.1", 10, "Summary", "Extended/Paragraph Response",
     "Refer to TEXT 2, Global Migration. Summarise, in not more than 90 words, how the international "
     "community could address the challenges related to global migration. Requirements: one coherent "
     "paragraph; full sentences; accurate language use in an appropriate register; an appropriate "
     "title included in the word count; an accurate word count at the end; own words (no cutting and "
     "pasting).", None, False, "restated_only",
     "NOT ANSWERED IN THE MEMORANDUM — the memorandum restates the task and its instructions but "
     "prints no model summary, no point list and no rubric.",
     ["no marking evidence printed"],
     "The 10 marks are allocated by the paper; no marking evidence exists in the supplied memorandum, "
     "so no marking requirements can be derived for this record.",
     False, "allocated", False, False),

    # ---------------- QUESTION 3: SEEN POETRY (10 of the 20 combined poetry marks) ----------------
    ("3.1", 2, "Poetry (Seen)", "Extended/Paragraph Response",
     "Read the poem 'i thank You God for most this amazing' by e.e. cummings. How does the use of "
     "punctuation in line 1 enhance the poet's purpose in this poem?", "i thank You God for most this amazing",
     False, "model_answer",
     "The small letter use of i and capital letters for You and God indicate the poet wants to praise "
     "God and indicate the insignificance of humanity.",
     ["identification of the lower-case 'i' and capitalised 'You'/'God'",
      "effect: praise of God / insignificance of humanity"],
     "Requires the punctuation/capitalisation detail plus its purpose.",
     False, "allocated", False, False),

    ("3.2", 2, "Poetry (Seen)", "Extended/Paragraph Response",
     "Comment on the purpose of the parenthesis in stanzas 2 and 4.",
     "i thank You God for most this amazing", False, "model_answer",
     "The poet's personal experience and his own thoughts. He feels alive and aware of the abundance "
     "of God's beauty.",
     ["purpose of the parenthesis (personal aside / inner thought)",
      "content: feeling alive, awareness of God's beauty"],
     "Two marks for purpose plus content of the parenthetical lines.",
     False, "allocated", False, False),

    ("3.3", 2, "Poetry (Seen)", "Extended/Paragraph Response",
     "Discuss the effectiveness of cummings' use of inverted word order in the poem.",
     "i thank You God for most this amazing", False, "model_answer",
     "To stress a particular word in the sentence 'I thank you for most this amazing', to stress the "
     "'most'. It forces the reader to pause and contemplate the lines more carefully. Accept other "
     "examples. One example with effect.",
     ["an example of inverted word order",
      "effect: emphasis / forces the reader to pause and contemplate"],
     "The memo explicitly accepts any one example provided its effect is given.",
     False, "allocated", False, False),

    ("3.4", 1, "Poetry (Seen)", "Short Answer",
     "What do you think the poet means by the expression lifted from the no / of all nothing (lines "
     "10 and 11)?", "i thank You God for most this amazing", False, "model_answer",
     "To be lifted from ignorance into a state of awareness of creation.",
     ["explanation of the expression: ignorance to awareness of creation"],
     "One mark; the memo's answer is short and conceptual.",
     False, "allocated", False, False),

    ("3.5", 3, "Poetry (Seen)", "Extended/Paragraph Response",
     "Select the image which best describes the overall tone of the poem. Justify your choice by "
     "making close reference to the poem and the image. (IMAGES A, B and C are printed with the "
     "question.)", "i thank You God for most this amazing", True, "model_answer",
     "Choose one image and connect to a tone of awe, inspiring, amazement, reverence. Must refer to "
     "poem and visual details in image.",
     ["choice of image",
      "a tone named (awe/inspiring/amazement/reverence)",
      "reference to both poem and visual details"],
     "The memo demands reference to both the poem and the chosen image's visual details.",
     False, "allocated", True, False),

    # ---------------- QUESTION 4: UNSEEN POETRY (10 of the 20 combined poetry marks) ----------------
    ("4.1", 2, "Poetry (Unseen)", "Extended/Paragraph Response",
     "Read 'Nightsong: City' by Dennis Brutus. Who is the speaker addressing in the poem? "
     "Substantiate your answer.", "Nightsong: City", False, "model_answer",
     "Speaking to the city/land/country. Wanting his city/country to sleep in peace.",
     ["addressee identified (the city/land/love)",
      "substantiation from the poem (wanting the city to sleep in peace)"],
     "Substantiation is required, not the identification alone.",
     False, "allocated", False, False),

    ("4.2", 2, "Poetry (Unseen)", "Extended/Paragraph Response",
     "Account for the speaker's use of the word, cockroach (line 3), to describe the police cars.",
     "Nightsong: City", False, "model_answer",
     "They are scurrying, pests, creeping out of hiding places, ominous, dirty feeling about them, invasive.",
     ["connotations of 'cockroach' (scurrying, pests, hidden, invasive)",
      "effect: ominous, dirty, threatening presence"],
     "Two marks for the connotation and the effect.",
     False, "allocated", False, False),

    ("4.3", 2, "Poetry (Unseen)", "Extended/Paragraph Response",
     "Identify and discuss the effectiveness of the figure of speech in line 5.",
     "Nightsong: City", False, "model_answer",
     "Simile — violence compared to a rag that is infested with bugs and tossed aside. Violence is "
     "pervasive and you toss it aside so as not to be affected by it.",
     ["identification of the simile",
      "effectiveness: pervasiveness of violence / being tossed aside"],
     "Both identification and discussion are marked.",
     False, "allocated", False, False),

    ("4.4", 4, "Poetry (Unseen)", "Extended/Paragraph Response",
     "Consider 'The Second Coming' by Yeats and 'Nightsong: City' by Brutus and discuss how the "
     "structure of both poems enhances the mood. Justify your response with reference to both poems.",
     "Nightsong: City; The Second Coming", False, "model_answer",
     "Structure of Second Coming: no rhyming, free verse reflects the restlessness of society, "
     "anarchy. Enjambment creates fluidity or argument in lines 6,7 and 8,9. Structure of Nightsong: "
     "3 stanzas of equal length, no rhyming to indicate the lack of structure in society emphasising "
     "the violence of society. Mood: sombre, restless (Nightsong); hopeless, faithless and desperate "
     "(Second Coming). Quotes required.",
     ["structure of poem 1 named and linked to mood",
      "structure of poem 2 named and linked to mood",
      "mood stated for both",
      "quotation from both poems"],
     "Cross-poem comparison; four marks distributed across both structures, the two moods and the "
     "required quotation.",
     False, "allocated", False, False),

    # ---------------- QUESTION 5: VISUAL LITERACY (25; items total 24) ----------------
    ("5.1", 2, "Visual Literacy", "Extended/Paragraph Response",
     "Refer to TEXT 3, the advertisement for the TOPSY FOUNDATION. What is the advertiser's "
     "intention in stating that 'AIDS is creating child parents at an alarming rate'?", None, True,
     "model_answer",
     "Shocks the reader; realisation of the horror of the AIDS epidemic. Awareness of the destruction "
     "of the traditional family unit. Shocking understanding of young children becoming adults too "
     "soon and needing to parent.",
     ["intention: to shock / raise awareness",
      "realisation: children becoming parents too soon"],
     "The advertisement itself is an image; the memo's answer is text but the visual cannot be verified.",
     False, "allocated", True, False),

    ("5.2", 3, "Visual Literacy", "Extended/Paragraph Response",
     "Discuss the effectiveness of the image used to support the message of the advertiser.", None,
     True, "model_answer",
     "Childish handwriting, the crayon, the toy car, spelling mistakes to indicate that a child has "
     "written the note. The note supports the fact that so many children are acting as parents.",
     ["visual details named (handwriting, crayon, toy car, spelling)",
      "effect: the note reads as written by a child",
      "link to the message that children are acting as parents"],
     "Three marks across visual detail, effect and link to message.",
     False, "allocated", True, False),

    ("5.3.1", 2, "Visual Literacy", "Short Answer",
     "Study the logo at the bottom of the advertisement. Provide a definition for the word stigma as "
     "used in the logo.", None, True, "model_answer",
     "A negative generalisation/idea/perception/reputation about an issue or a person.",
     ["definition of stigma: negative generalisation about a person or issue"],
     "Two marks for the definition as used in the logo.",
     False, "allocated", True, False),

    ("5.3.2", 2, "Visual Literacy", "Extended/Paragraph Response",
     "How does the design of the logo enhance the advertiser's message?", None, True, "model_answer",
     "The plus/minus on the T to suggest the extent to which people are judged because of being HIV "
     "positive. Cross could symbolise death, mark on a grave.",
     ["description of the logo's design elements",
      "effect: judgement, HIV positive, cross/death symbolism"],
     "Requires a reading of the logo's visual design.",
     False, "allocated", True, False),

    ("5.4", 2, "Visual Literacy", "Extended/Paragraph Response",
     "What does it mean to be HIV NEUTRAL?", None, True, "model_answer",
     "Not to make a judgement of people who are HIV positive or who suffer from AIDS.",
     ["definition: not judging people who are HIV positive"],
     "Two marks; the term is defined by the advertisement's logo text (image).",
     False, "allocated", True, False),

    ("5.5", 3, "Visual Literacy", "Extended/Paragraph Response",
     "How does the use of the diction succeed in calling the reader to take action?", None, True,
     "model_answer",
     "Emotive words 'passionate', 'smart', 'honest', 'kind', 'cautious' — these words make people "
     "feel good about making a difference. These words inspire people not to be judgemental and to "
     "befriend people with AIDS and be more empathetic to their plight.",
     ["emotive words listed",
      "effect on the reader: feel good about making a difference",
      "intended action: be less judgemental, befriend and empathise"],
     "Three marks across diction, effect and action.",
     False, "allocated", True, False),

    ("5.6", 2, "Visual Literacy", "Extended/Paragraph Response",
     "Discuss how the font and font size play an integral part in the effectiveness of the advertisement.",
     None, True, "model_answer",
     "Larger font and bolder to emphasize the essence of the message — to be caring and compassionate. "
     "The font looks like a command; the reader feels that he/she is compelled to be more compassionate.",
     ["font/size described (large, bold)",
      "effect: emphasis and compulsion / the font reads as a command"],
     "Typography question; depends on the advertisement image.",
     False, "allocated", True, False),

    ("5.7", 5, "Visual Literacy", "Extended/Paragraph Response",
     "Refer to both TEXTS 3 and 4. Identify and discuss the bias evident in both TEXT 3 and TEXT 4. "
     "Focus on verbal and visual clues.", None, True, "model_answer",
     "Text 3 assumes that the child-parent is a black child which suggests that mostly black people "
     "are affected by AIDS in SA. The child lacks education which is also associated with AIDS. The "
     "letter is written by 'Nomsa' to 'Principal Dhlamini' enforcing the black stereotype that many "
     "black children cannot attend school any longer as they are obliged to stay home and look after "
     "smaller siblings. Text 4 — white hands reach out to help those in need. This suggests that all "
     "generosity and assistance is metered out by white benevolent, educated, elite people. The "
     "language used is grammatically correct and sophisticated, 'stigma free'.",
     ["bias in TEXT 3 identified (race, education, names)",
      "bias in TEXT 4 identified (white hands as benefactors)",
      "verbal clues cited",
      "visual clues cited"],
     "Five marks across both texts and both clue types; the memo is explicit about the stereotype it "
     "wants named.",
     False, "allocated", True, False),

    ("5.8", 3, "Visual Literacy", "Extended/Paragraph Response",
     "Suggest two ways in which an advertiser could overcome bias in an advertisement which focuses "
     "on social issues.", None, True, "model_answer",
     "Reflect all race groups, not make judgements based on level of education, use of language that "
     "is inclusive and not biased e.g. 'HIV affects us all'. The use of inclusive pronouns would "
     "overcome bias and unite all. Circle of hands, not just 2 hands. Names should be more generic.",
     ["two suggestions offered",
      "each suggestion tied to the bias it removes",
      "inclusive alternatives (pronouns, circle of hands, generic names)"],
     "Three marks requiring two suggestions with justification.",
     False, "allocated", True, False),

    # ---------------- QUESTION 6: TEXTUAL EDITING (10; source prints items as 5.1-5.5) ----------------
    ("6.1", 2, "Language Structures & Conventions", "Short Answer",
     "Read TEXT 5, 'The Greatest Soccer players of all time' (Jon O'Brien, 2017). Identify and "
     "correct the grammar error in line 1.", None, False, "model_answer",
     "Split infinitive — 'to always spark' should be corrected as 'to spark always'.",
     ["identification of the split infinitive", "correction supplied"],
     "Two marks: identification and correction.",
     False, "allocated", False, False),

    ("6.2", 2, "Language Structures & Conventions", "Extended/Paragraph Response",
     "Why would the writer choose to place 'Golden Boot' (paragraph 2) in capital letters?", None,
     False, "model_answer",
     "The status he has achieved has earned him the respect of being known as having a Golden Boot.",
     ["effect of capitalisation: status, respect, an earned title"],
     "Two marks; the memo ties capitals to status/respect rather than a grammar label.",
     False, "allocated", False, False),

    ("6.3", 2, "Language Structures & Conventions", "Extended/Paragraph Response",
     "Explain the connotations of the title 'Black Panther' being given to Eusebio.", None, False,
     "model_answer",
     "He is a hero, a king, someone who is fit and strong and stealthy like a panther.",
     ["connotations: hero, king, strong, stealthy"],
     "Two marks for the connotations of the nickname.",
     False, "allocated", False, False),

    ("6.4", 2, "Language Structures & Conventions", "Extended/Paragraph Response",
     "Explain the effectiveness of the use of informal language to describe George Best in paragraph 3.",
     None, False, "model_answer",
     "The informal language is used to criticize him for being fast and loose. It makes him sound like "
     "a person who lacks moral values.",
     ["informal language identified as criticism", "effect: lacking moral values"],
     "Two marks; register is judged by its effect on the subject's portrayal.",
     False, "allocated", False, False),

    ("6.5", 2, "Language Structures & Conventions", "Extended/Paragraph Response",
     "By analysing the sentence structure of the last sentence, assess the effectiveness of the "
     "writer's choice to convey his message.", None, False, "model_answer",
     "Compound sentence starting with a misrelated participle. Although this player didn't showcase "
     "his talents globally, the titles he has won are listed, therefore encouraging the reader to "
     "admire him.",
     ["sentence structure identified (compound sentence / misrelated participle)",
      "effect on the message: the reader is encouraged to admire the player"],
     "Two marks across structure analysis and effect.",
     False, "allocated", False, False),
]
