"""Pass 1 evidence table — Grade 11 English Paper 1, November 2017.

Authored by reading the extracted text of the paper (.docx) and its memorandum.

Paper: data/organized/english/Grade 11 Paper 1 Nov 2017.docx       (90 marks)
Memo:  data/organized/english/Grade 11 Paper 1 Nov 2017.memo.docx  (90 marks)

Pairing evidence (printed, not inherited): identical header block in both
documents — SUBJECT English Paper 1, DATE November, 2017, GRADE 11, MARKS 90,
EXAMINER Mrs Nichas, Mr Brouard, MODERATOR Mrs Oosthuysen, Mrs Leeburn,
Mrs Nichas, DURATION 2 1/2 hours — identical printed section headings, and the
memo restates every numbered item with the same bracketed marks. The memorandum
ends with its own mark grid (1.1 2, 1.2 3, ... 5.3 2) which agrees with the
bracketed marks of every transcribed item.

This paper prints no 'Possible Marks' cover row; the section totals are printed
in the section headings (25 + 10 + 30 + 20 + 5 = 90) and are verified against
the header MARKS. The transcribed items sum to the same 90 marks exactly.
"""

PAPER = {
    "paper_key": "ENG-2017-NOV-P1",
    "paper_path": "data/organized/english/Grade 11 Paper 1 Nov 2017.docx",
    "memo_path": "data/organized/english/Grade 11 Paper 1 Nov 2017.memo.docx",
    "year": 2017,
    "exam_date": "November, 2017",
    "exam_period": "nov",
    "paper_number": "P1",
    "paper_type": "paper1",
    "exam_board": "internal",
    "paper_focus": "Language — reading and viewing (comprehension, summary, poetry, visual literacy, textual editing)",
    "total_marks": 90,
    "examiner": "Mrs Nichas, Mr Brouard",
    "moderator": "Mrs Oosthuysen, Mrs Leeburn, Mrs Nichas",
    "duration_stated": {"paper": "2 1/2 hours", "memo": "2 1/2 hours"},
    "fidelity_rung": "A",
    "section_totals": {"1": 25, "2": 10, "3": 30, "4": 20, "5": 5},
    "section_totals_basis": "printed section headings (question 1: cOMPREHENSION25 marks, QUESTION 2: SUMMARY10 MARKS, question 3: poetry30 marks, question 4 – visual literacy20 marks, question 5 – textual editing5 marks), which sum to the header MARKS 90",
    "cover_table_absent_reason": "the paper prints no 'Possible Marks' cover row; its cover carries only STUDENT'S RESULT / COMMENT / signature lines, so section totals are verified from the printed section headings",
    "section_anchors": [
        "question 1: cOMPREHENSION25 marks", "QUESTION 2: SUMMARY10 MARKS",
        "question 3: poetry30 marks", "question 4 – visual literacy20 marks",
        "question 5 – textual editing5 marks",
    ],
    "memo_section_anchors": [
        "question 1: cOMPREHENSION25 marks", "QUESTION 2: SUMMARY10 MARKS",
        "question 3: poetry30 marks", "question 4 – visual literacy20 marks",
        "question 5 – textual editing5 marks",
    ],
    "item_anchor_overrides": {
        "2.1": {"paper": "QUESTION 2: SUMMARY10 MARKS",
                "note": "the summary is a section-level task; its 10 marks are printed in the section heading"},
        "1.11": {
            "paper": "1.11 Considering the message of the cartoon above and Text 1",
            "memo": "1.11 Considering the message of the cartoon above and Text 1",
            "note": "both documents prefix the item number with a stray text-box figure ('116459021590001.11'), so the anchor text is used instead of a bare number search",
        }
    },
    "source_hashes": {
        "paper_path": "ddacac818a6b9d6c4271a50a300790c6497e47e3ca7184816f833098ab5c0ec2",
        "memo_path": "09edeff3f51bbf9e1d2a732dd39329fd9e70f1d22ecdcea6855ce298b9d50beb",
    },
    "notes": (
        "Paper 1 language paper. TEXT 1 is 'Life is an Eroding Beach' (a column on the 'ostrich "
        "effect'); TEXT 2 is 'Rise of the Drones'; the seen poem is 'The Pauper' (Richard Ntiru) "
        "and the unseen poem is 'Decomposition' (Zulfikar Ghose); TEXTS 3-5 are Amnesty "
        "International visual texts, TEXT 5 being the cover of a book about President Zuma; TEXT 6 "
        "is the textual-editing passage on Tavi Gevinson. Comprehension, summary, poetry and "
        "textual editing are language skills and must not be merged with Paper 2 set-work literature."
    ),
}

SCHEMA = (
    "qn", "marks", "section", "qformat", "text", "set_text", "has_visual",
    "memo_evidence", "memo_answer", "memo_steps", "memo_notes", "rubric_ref",
    "allocation", "needs_visual", "ocr_uncertain",
)

STEMS = {}

RECORDS = [
    # ---------------- QUESTION 1: COMPREHENSION (25) ----------------
    ("1.1", 2, "Comprehension", "Extended/Paragraph Response",
     "Read TEXT 1, 'Life is an Eroding Beach'. Explain the effectiveness of starting the text with "
     "a rhetorical question.", None, False, "model_answer",
     "The question points to the ridiculousness of such a question. Not many people would have "
     "thought of this. It involves the reader in the conversation.",
     ["effect: points to the ridiculousness of the question",
      "effect: involves the reader / draws the reader into the conversation"],
     "Two marks for two distinct effects on the reader.",
     False, "allocated", False, False),

    ("1.2", 3, "Comprehension", "Extended/Paragraph Response",
     "Explain how the diction and the tone of the column contribute to the writer's intention.",
     None, False, "model_answer",
     "Informal language used, 'not so, friends'; cliché phrases, 'like sands in the hour glass' "
     "inform the tone — tongue-in-cheek, philosophical, pensive. His intention is to raise awareness.",
     ["diction named and illustrated",
      "tone named from that diction (tongue-in-cheek, philosophical, pensive)",
      "link to the writer's intention (to raise awareness)"],
     "Three marks; both diction and tone must be tied to the intention.",
     False, "allocated", False, False),

    ("1.3", 3, "Comprehension", "Extended/Paragraph Response",
     "Why does the writer mention that she doubts whether 'Knowledge is power' (paragraph 3)?",
     None, False, "model_answer",
     "Too much knowledge leads to confusion, therefore it is disempowering and causes anxiety. She "
     "feels anxious about the sand problem in the world and the Wikileaks saga.",
     ["knowledge leading to confusion is disempowering",
      "it causes anxiety",
      "illustration from the text (sand problem / Wikileaks)"],
     "Three marks: claim, reason and textual illustration.",
     False, "allocated", False, False),

    ("1.4", 2, "Comprehension", "Extended/Paragraph Response",
     "Explain the metaphorical reference to Popeye in paragraph 4.", None, False, "model_answer",
     "Popeye — a cartoon character of a sailor who becomes strong when he eats spinach. In this "
     "context, she is using it to refer to a person having so much information that their brain "
     "swells like Popeye.",
     ["identification of Popeye (sailor who grows strong on spinach)",
      "application: knowledge so abundant it swells the brain"],
     "The metaphor must be unpacked, not merely labelled.",
     False, "allocated", False, False),

    ("1.5", 1, "Language Structures & Conventions", "Short Answer",
     "'Almost everything related to food manufacture and preparation.' (paragraph 6) Identify the "
     "grammatical error in this sentence.", None, False, "model_answer",
     "No finite verb, no subject. 'I wish I didn't know about problems/errors related to food "
     "manufacture and preparation.' (Anything suitable.)",
     ["identification: the fragment has no finite verb / no subject", "correction supplied"],
     "One mark; the memo accepts any suitable correction.",
     False, "allocated", False, False),

    ("1.6", 1, "Language Structures & Conventions", "Short Answer",
     "What is the function of the hyphen in 'better-off-not-knowing category' (paragraph 7)?",
     None, False, "model_answer",
     "Joining words to form a compound adjective.",
     ["compounding words into a single adjective"],
     "One mark; the grammatical term itself is the answer.",
     False, "allocated", False, False),

    ("1.7", 2, "Comprehension", "Extended/Paragraph Response",
     "Explain the shift in meaning in the idiomatic expression 'Real kick in the teeth/face' as it "
     "has been used in paragraphs 8 and 11.", None, False, "model_answer",
     "In paragraph 8, the idiom refers to something that you didn't expect or that upsets you. In "
     "paragraph 11, it refers to the literal meaning of being kicked in the face.",
     ["figurative meaning (paragraph 8)",
      "literal meaning (paragraph 11)",
      "the shift itself named"],
     "Two marks: the two meanings and the shift between them.",
     False, "allocated", False, False),

    ("1.8", 2, "Comprehension", "Extended/Paragraph Response",
     "Explain the humour expressed by the writer in relation to her teacher's aphorism (a concise "
     "statement that contains a general truth) in paragraph 9.", None, False, "model_answer",
     "Rhyming has nothing to do with wisdom. The writer is mocking the saying or pointing to a "
     "childlike belief that pithy statements have to be true.",
     ["the humour identified (she mocks the aphorism)",
      "reason: rhyme is not the same as truth/wisdom"],
     "Two marks; the joke's logic must be explained.",
     False, "allocated", False, False),

    ("1.9", 1, "Comprehension", "Short Answer",
     "What is suggested about how the writer views herself when she says that '16 year later, I "
     "think of it almost daily' in paragraph 9?", None, False, "model_answer",
     "She is still affected by the insult she received. Her self-esteem is still affected.",
     ["the remark still affects her / her self-esteem"],
     "One mark.",
     False, "allocated", False, False),

    ("1.10", 3, "Comprehension", "Extended/Paragraph Response",
     "To what extent is Shankar Vedantam's (the host of the 'Hidden Brain' podcast) opinion "
     "surrounding knowledge reliable? Explain your answer.", None, False, "model_answer",
     "It is purely his opinion and therefore cannot be considered to be reliable. An opinion cannot "
     "be trusted as absolute truth. (Memo's alternative: boys can also argue that his opinion might "
     "be reliable as he quotes economists and learned people and therefore supports his views with "
     "those of knowledgeable people who have researched this topic.)",
     ["position taken on reliability",
      "reason: it is opinion, not verified fact",
      "the memo's accepted alternative: reliance on cited economists and researchers"],
     "The memo explicitly allows either position provided the reasoning is sound.",
     False, "allocated", False, False),

    ("1.11", 5, "Comprehension", "Extended/Paragraph Response",
     "Considering the message of the cartoon above and Text 1, evaluate, by using examples from your "
     "own experience, whether you agree with Rebecca Davis' interpretation regarding the 'Ostrich "
     "effect'. (A cartoon is printed with the question.)", None, True, "model_answer",
     "Text 1 refers to not wanting to know everything. 'Ignorance is bliss' is the preferred state "
     "of being. The message of the cartoon becomes harsher saying that it is not about ignoring "
     "information or not wanting to know about it, but actually harming others who have information "
     "in order to perpetuate the 'ignorance is bliss' idea. Boys could also argue that some people "
     "are so insistent that they remain ignorant that they will prevent others from informing them "
     "and therefore could be considered guilty.",
     ["explanation of the 'ostrich effect' from Text 1",
      "reading of the cartoon's harsher message (harming those who hold information)",
      "evaluation: agreement or disagreement argued",
      "supporting example from the candidate's own experience"],
     "Five marks; the cartoon is an image, so the visual cannot be verified from the text layer, "
     "though the memo supplies its reading. The wording requires an own-experience example.",
     False, "allocated", True, False),

    # ---------------- QUESTION 2: SUMMARY (10) ----------------
    ("2.1", 10, "Summary", "Extended/Paragraph Response",
     "Read TEXT 2, 'Rise of the Drones' and answer the following question. As a technological "
     "enthusiast, you have been asked to address a group of scientists at a conference for Drone "
     "development. By summarising TEXT 2, present your views on the positive and negative effects "
     "of drone technology in the world. Take note of the following: Your summary must be in the "
     "form of ONE paragraph, using no more than 90 words. Your language use must be accurate and "
     "in an appropriate register. Do not include the title provided in your word count. Provide an "
     "accurate word count at the end of the summary. Use your own words. 'Cutting and pasting' of "
     "information is not acceptable.", None, False, "restated_only",
     "NOT ANSWERED IN THE MEMORANDUM — the memorandum restates the task and its requirements but "
     "prints no model summary, no point list and no rubric.",
     ["no marking evidence printed"],
     "Note the contrast with the 2016 and 2018 papers, whose summaries DO include the title in the "
     "word count: this paper instructs the opposite. Recorded as printed; no marking requirements "
     "can be derived without marking evidence.",
     False, "allocated", False, False),

    # ---------------- QUESTION 3: POETRY (30) ----------------
    ("3.1", 2, "Poetry (Seen)", "Extended/Paragraph Response",
     "Using your knowledge of the connotation of the word 'malignant'; what does Ntiru imply "
     "about the presence of the pauper in lines 3-4?",
     "The Pauper", False, "model_answer",
     "The poet is asking what cancerous (malignant) force created the Pauper. Poverty has not been "
     "created by the poor but by forces beyond their control and by greedy governments.",
     ["connotation of 'malignant' (cancerous)",
      "implication: poverty is created by forces beyond the pauper's control / by greedy governments"],
     "The word's connotation must be used, not just defined.",
     False, "allocated", False, False),

    ("3.2", 2, "Poetry (Seen)", "Extended/Paragraph Response",
     "What commentary is the poet making in lines 16-18 regarding the issue of charity and the "
     "inequality found within Ugandan society?", "The Pauper", False, "model_answer",
     "The rich do not regard the pauper, they merely drive by in their beautiful cars. It's ironic "
     "that there is such wealth in such poverty in Ugandan society. Clearly the society does not "
     "give the poor anything and they are forced onto the streets and live on 'hairless goatskins'.",
     ["the rich ignore the pauper (drive past in beautiful cars)",
      "irony of wealth beside extreme poverty / society gives nothing"],
     "Two marks: the observation and the commentary on inequality/charity.",
     False, "allocated", False, False),

    ("3.3", 2, "Poetry (Seen)", "Extended/Paragraph Response",
     "Describe the tone of the lines mentioned in 3.2? Justify your answer by quoting from the poem.",
     "The Pauper", False, "model_answer",
     "Ironic, scathing. 'Your ribs and bones reflecting the light that beautiful cars reflect on you.'",
     ["tone named (ironic / scathing)", "justifying quotation"],
     "The quotation is compulsory; a tone label alone does not earn the second mark.",
     False, "allocated", False, False),

    ("3.4", 2, "Poetry (Seen)", "Extended/Paragraph Response",
     "Explain how the enjambment in lines 17/18 and again in lines 19/20 helps to create meaning.",
     "The Pauper", False, "model_answer",
     "The enjambment makes the movement of the pauper fluid and slow. There is a contrast between "
     "the slow and graphic actions of the pauper squashing lice in his nails and the movement of "
     "the expensive cars going past him.",
     ["effect of enjambment: fluid, slow movement",
      "contrast created with the cars / the graphic actions"],
     "Two marks; the device must be tied to the contrast it creates.",
     False, "allocated", False, False),

    ("3.5", 3, "Poetry (Seen)", "Extended/Paragraph Response",
     "Explain how the use of repetition and sentence structure affects the meaning of the final stanza.",
     "The Pauper", False, "model_answer",
     "The repetition of 'pauper, pauper' and 'beautiful' emphasises the plight of the pauper and how "
     "grotesque his situation is. 'Beautiful' highlights the disparity between the rich and the poor. "
     "The final stanza speaks of the selfishness of the government officials who do not care about "
     "the poor and their issues become only part of a 'supplementary' question — of secondary "
     "importance in their agendas. They are all overweight and overindulged. The mood is gloomy, cynical.",
     ["repetition analysed ('pauper, pauper' / 'beautiful')",
      "effect: plight and disparity emphasised",
      "sentence structure / the 'supplementary question' as secondary importance",
      "mood named (gloomy, cynical)"],
     "Note the paper asks for the mood while the memorandum's grid labels 3.5 as 3 marks; the memo "
     "answer covers repetition, structure and mood.",
     False, "allocated", False, False),

    ("3.6", 3, "Poetry (Unseen)", "Extended/Paragraph Response",
     "Read the unseen poem 'Decomposition' by Zulfikar Ghose. The word composition means 'the nature "
     "of something' or 'a creative work especially a poem or piece of music'. The poem's title, "
     "however, is Decomposition. By referring to the words Composition and Decomposition, explain "
     "the central message of the poem.", "Decomposition", False, "model_answer",
     "The poet attempts to take a photo/make a picture (composition) out of someone's suffering and "
     "feels guilty for it. He acknowledges a beggar's 'decomposed' state, being 'broken down' — "
     "'hunger and solitude' — and his attempt to 'compose art' out of it.",
     ["'composition' as the poet's framing/art-making",
      "the beggar's decomposed/broken-down state",
      "central message: guilt at making art out of suffering"],
     "Three marks; the wordplay must be resolved into the poem's message.",
     False, "allocated", False, False),

    ("3.7.1", 1, "Poetry (Unseen)", "Short Answer",
     "Identify the figure of speech in line 8.", "Decomposition", False, "model_answer",
     "Metaphor.",
     ["metaphor identified"],
     "One mark for the label only.",
     False, "allocated", False, False),

    ("3.7.2", 2, "Poetry (Unseen)", "Extended/Paragraph Response",
     "Why is this comparison (line 8) so powerful in describing the situation of the sleeping beggar?",
     "Decomposition", False, "model_answer",
     "The beggar is so thin that he has become part of the stone pavement, carved into it like a fossil.",
     ["explanation: the beggar merges with the stone / is carved into it",
      "effect: he is thin, worn, fossilised"],
     "Requires the effect of the comparison, not its repetition.",
     False, "allocated", False, False),

    ("3.8", 1, "Poetry (Unseen)", "Short Answer",
     "The poet states that the people are 'indifferent' to the sight of the beggar. Quote another "
     "word from the poem that highlights the indifference of people?", "Decomposition", False,
     "model_answer",
     "glibly",
     ["glibly (the single printed answer)"],
     "One mark; the memo gives exactly one word.",
     False, "allocated", False, False),

    ("3.9", 3, "Poetry (Unseen)", "Extended/Paragraph Response",
     "To whom does the idiomatic expression, the man on the street refer? Why is it ironic that the "
     "poet would give his photograph that title?", "Decomposition", False, "model_answer",
     "The average, common man. The beggar is not an average man, he is below average, one who "
     "suffers and represents the lowest in our society.",
     ["referrent: the average, common man",
      "irony: the beggar is below average / the lowest in society"],
     "Three marks; both the reference and the irony must be explained.",
     False, "allocated", False, False),

    ("3.10", 4, "Poetry (Unseen)", "Extended/Paragraph Response",
     "In both 'The Pauper' and 'Decomposition', similar images are used to show the physical state "
     "of the beggar/pauper. Compare two images (other than the image referred to in 3.7) from each "
     "poem used to draw the reader into the plight of the beggar.",
     "The Pauper; Decomposition", False, "model_answer",
     "Pauper imagery — 'trudging on horny pads', 'grimy emaciated skin', 'craning to see' — these "
     "images portray the horrific state of the beggar; he has been on the street for a long time and "
     "the elements have aged him. Decomposition imagery — 'grey-haired, wearing shorts and a dirty "
     "shirt', 'his arms and legs could be cracks in the stone', 'his head in the posture of one "
     "weeping' — also indicate the pitiful state of the beggar, how thin he is, how old and how "
     "hopeless his situation is.",
     ["two images from The Pauper",
      "two images from Decomposition",
      "each image tied to the plight of the beggar",
      "comparison drawn across the poems"],
     "Cross-poem comparison; four marks over the two poems and the comparison.",
     False, "allocated", False, False),

    ("3.11", 5, "Poetry (Unseen)", "Extended/Paragraph Response",
     "Examine the following quote and accompanying picture and then answer the question that "
     "follows. To what extent do you agree that poverty is created and human suffering is often "
     "seen as inspiration for an art form rather that inspiration to help and eradicate poverty? "
     "Quote from the VISUAL, the SEEN and UNSEEN poem to support your argument. (A picture is "
     "printed with the question.)", "The Pauper; Decomposition", True, "model_answer",
     "Poverty is created by systems, governments, people and their greed. We take pictures and feel "
     "sorry for those in this situation but don't do much to prevent it. Social media makes us aware "
     "of pictures like the one above that raise awareness for the condition of the poor but little "
     "is done to combat it. These pictures become an art form and are displayed across various forms "
     "of media. 'Tourists and I will take your snapshots' from The Pauper and 'attempting to compose "
     "art out of his hunger and his solitude' from Decomposition highlight this fact. Boys however "
     "also need to argue that there are people who do much to help alleviate poverty, who donate "
     "thousands to those in need.",
     ["argument on whether poverty is created",
      "argument on suffering as artistic inspiration vs inspiration to help",
      "quotation from the visual",
      "quotation from the seen poem",
      "quotation from the unseen poem",
      "the memo's required counter-argument (those who do help)"],
     "Five marks across the argument and the three required sources; the visual is an image and "
     "cannot be verified from the text layer.",
     False, "allocated", True, False),

    # ---------------- QUESTION 4: VISUAL LITERACY (20 — every item depends on an image) ----------------
    ("4.1", 4, "Visual Literacy", "Extended/Paragraph Response",
     "Study TEXTS 3, 4 and 5 (produced by Amnesty International). By referring to visual and verbal "
     "details, explain the satirical message of TEXT 3.", None, True, "model_answer",
     "A person is attempting a smile but his/her teeth are covered in barbed wire to look like "
     "braces. The advertiser uses words such as 'freely' and 'freedom' to indicate that in many "
     "countries the opposite is happening. Many people do not have the luxury of 'freedom of speech' "
     "and are constrained, even jailed for speaking out against the prevailing order.",
     ["visual detail read (barbed-wire braces)",
      "verbal detail read ('freely' / 'freedom')",
      "satirical message: the opposite of freedom of speech",
      "link to constraint/punishment for speaking out"],
     "Four marks across both clue types and the satire's message; the text is an image.",
     False, "allocated", True, False),

    ("4.2", 2, "Visual Literacy", "Extended/Paragraph Response",
     "Considering what Amnesty International does, assess the relevance of their logo.", None, True,
     "model_answer",
     "The logo is a candle that is lit to symbolise their company being a light perhaps for those "
     "whose rights have been abused. They offer hope to the oppressed. It is therefore appropriate.",
     ["identification of the logo element (lit candle)",
      "assessment: light/hope for the oppressed, therefore appropriate to Amnesty's purpose"],
     "Requires an assessment, not a description.",
     False, "allocated", True, False),

    ("4.3", 3, "Visual Literacy", "Extended/Paragraph Response",
     "Explain the irony inherent in TEXT 4. Refer to visual details to support your answer.", None,
     True, "model_answer",
     "Books are supposed to educate you, open your mind and teach you something different and "
     "interesting. They are not supposed to lead to your death or harm you. The open book would "
     "indicate new knowledge being gained; the red bookmark in the shape of a hangman's noose "
     "suggests that many authors risk their lives to have their work published.",
     ["the expectation established (books educate)",
      "the visual detail (noose-shaped bookmark)",
      "the irony resolved: authors risk their lives to publish"],
     "Three marks; the visual detail must be cited.",
     False, "allocated", True, False),

    ("4.4", 2, "Visual Literacy", "Extended/Paragraph Response",
     "Explain why censorship would be detrimental in a democratic society.", None, True,
     "model_answer",
     "Censorship prevents freedom of speech and therefore goes against a democratic society which "
     "seeks to encourage the voice of the people.",
     ["censorship prevents freedom of speech",
      "democracy requires the voice of the people, so censorship is detrimental"],
     "Two marks; the argument must connect the two clauses.",
     False, "allocated", True, False),

    ("4.5", 2, "Visual Literacy", "Extended/Paragraph Response",
     "Refer to TEXT 5. This book has just been published in South Africa and stock is limited. From "
     "the verbal details, what do you believe the book's content will reveal?", None, True,
     "model_answer",
     "The book will reveal who the people are who have kept our president in power. It suggests that "
     "they are criminals who have been covering up crimes for Zuma and therefore have kept him out "
     "of prison. It suggests that Zuma is a criminal too and this book will expose him. 'keeping "
     "Zuma in power and out of prison'.",
     ["prediction from the verbal details: names of those keeping the president in power",
      "inference: criminal cover-up, exposure"],
     "Requires inference from the book-cover wording, which is an image.",
     False, "allocated", True, False),

    ("4.6", 2, "Visual Literacy", "Extended/Paragraph Response",
     "How would the visual of TEXT 5 add to the tone of the title of the book?", None, True,
     "model_answer",
     "The laughing face of Zuma adds to the satirical/critical tone of the title.",
     ["visual detail (the laughing face)",
      "tone: satirical/critical"],
     "Two marks; the visual element must be named.",
     False, "allocated", True, False),

    ("4.7", 3, "Visual Literacy", "Extended/Paragraph Response",
     "Do you believe that Jacques Paux will need help from Amnesty International in the next few "
     "months following the release of this book? Explain your answer with reference to TEXTS 3 and "
     "4 and your own knowledge.", None, True, "model_answer",
     "Text 4 suggests that authors will be hanged for speaking out against an order. Text 3 suggests "
     "that those who speak out will be jailed or prevented from doing so. Considering that Paux is "
     "already facing charges of treason and revealing sensitive information, he will need the help "
     "of Amnesty International.",
     ["prediction stated",
      "reference to TEXT 4 (authors harmed for speaking out)",
      "reference to TEXT 3 (speakers jailed/constrained)",
      "own knowledge of Paux's treason charges"],
     "Three marks requiring both texts plus the candidate's own knowledge.",
     False, "allocated", True, False),

    ("4.8", 2, "Visual Literacy", "Extended/Paragraph Response",
     "Explain the pun on the word 'dynamite' in TEXT 5.", None, True, "model_answer",
     "Dynamite — an explosive and dynamite — someone being very powerful and dynamic.",
     ["the two meanings (explosive; powerful/dynamic)"],
     "Two marks for the pun's double meaning.",
     False, "allocated", True, False),

    # ---------------- QUESTION 5: TEXTUAL EDITING (5) ----------------
    ("5.1", 2, "Language Structures & Conventions", "Extended/Paragraph Response",
     "Read TEXT 6 and answer the questions that follow. Identify the register of this text. Quote to "
     "support your answer.", None, False, "model_answer",
     "The register is informal — 'like a seasoned pro', 'received goodies'.",
     ["register named (informal)", "supporting quotation"],
     "Both the register and its quotation are required.",
     False, "allocated", False, False),

    ("5.2", 1, "Language Structures & Conventions", "Short Answer",
     "Identify the error of concord in sentence 3.", None, False, "model_answer",
     "The fashion industry 'wasn't' not 'weren't'.",
     ["the concord error identified and corrected"],
     "One mark; note the paper's own sentence 3 reads 'The fashion industry probably weren't "
     "prepared for the influence Gevinson...'.",
     False, "allocated", False, False),

    ("5.3", 2, "Language Structures & Conventions", "Extended/Paragraph Response",
     "Write a dictionary entry for the neologism, 'tastemaker' as it is used in this text. Include a "
     "part of speech and a definition of the word.", None, False, "model_answer",
     "Tastemaker (n): a person who makes new trends in fashion, one who is tasteful in their "
     "fashion choices.",
     ["part of speech (noun)", "definition in context"],
     "Two marks: part of speech and definition.",
     False, "allocated", False, False),
]
