"""Pass 1 evidence table — Grade 11 English Paper 2, July 2015 (set work + writing).

Authored by reading the extracted text of the paper (.docx) and its memorandum.

Paper: data/organized/english/Grade 11 Paper 2 July 2015.docx       (90 marks)
Memo:  data/organized/english/Grade 11 Paper 2 July 2015 Memo.docx  (90 marks)

Pairing evidence (printed, not inherited): identical header block in both
documents — SUBJECT English Paper 2, DATE July 2015, GRADE 11, MARKS 90,
EXAMINER Mrs Nichas/ Mrs Oosthuysen, MODERATOR Mr De Reuck, Mrs Leeburn,
DURATION 2 hours — identical printed cover table 'Possible Marks 20 30 20 20 90',
identical section headings, and the memo restates each numbered item.

SOURCE ABNORMALITIES PRESERVED (not silently corrected):
  * Question 3 instructs candidates to answer TWO of the three 20-mark options
    (blog, dialogue, formal letter). The cover table prints four numbers for
    three columns because both answers to Question 3 are counted separately.
    The option records are marked allocation='alternative'; the section total
    counts two of them.
  * In the memorandum the second transactional option is numbered '2' instead of
    '3.2', and the last Question 1 item (the prayer question) is numbered '1.7'
    again instead of '1.8'. Records keep the logical numbering and carry the
    printed wording so the mismatch stays visible.
"""

PAPER = {
    "paper_key": "ENG-2015-JUL-P2",
    "paper_path": "data/organized/english/Grade 11 Paper 2 July 2015.docx",
    "memo_path": "data/organized/english/Grade 11 Paper 2 July 2015 Memo.docx",
    "year": 2015,
    "exam_date": "July 2015",
    "exam_period": "july",
    "paper_number": "P2",
    "paper_type": "paper2",
    "exam_board": "internal",
    "paper_focus": "Literature and Writing — set-work drama extract, literature essay, transactional writing",
    "total_marks": 90,
    "examiner": "Mrs Nichas/ Mrs Oosthuysen",
    "moderator": "Mr De Reuck, Mrs Leeburn",
    "duration_stated": {"paper": "2 hours", "memo": "2 hours"},
    "fidelity_rung": "A",
    "section_totals": {"1": 20, "2": 30, "3": 40},
    "section_totals_basis": "printed cover row 'Possible Marks 20 30 20 20 90' read with the instruction 'Answer TWO of the following THREE QUESTIONS' for Question 3, so the printed 20+20 belongs to one section",
    "cover_table_groups": {"1": [20], "2": [30], "3": [20, 20]},
    "alternative_sections": {"3": {"options": 3, "counted": 2, "marks_each": 20}},
    "section_anchors": [
        "QUESTION 1 – OTHELLO 20 MARKS", "question 2 – GATSBY 30 marks",
        "question 3 – TRANSACTIONAL WRITING",
    ],
    "memo_section_anchors": [
        "QUESTION 1 – OTHELLO 20 MARKS", "question 2 – GATSBY 30 marks",
        "question 3 – TRANSACTIONAL WRITING",
    ],
    "memo_numbering_overrides": {
        "1.8": "1.7",
    },
    "item_anchor_overrides": {
        "2.1": {"paper": "question 2 – GATSBY 30 marks",
                "note": "the essay's marks are printed in its section heading, not after the item"},
        "3.1": {"paper": "question 3 – TRANSACTIONAL WRITING",
                "note": "each transactional option's 20 marks are printed in the shared instruction to answer TWO of the THREE questions"},
        "3.2": {"paper": "question 3 – TRANSACTIONAL WRITING"},
        "3.3": {"paper": "question 3 – TRANSACTIONAL WRITING"},
    },
    "source_hashes": {
        "paper_path": "24a4923db37033fc2aad9066b22f16f4b70158e0334daf56206459afbf42a78c",
        "memo_path": "84f0bfd7bc58069b2a570d71c3ac4d2e1a96389d0ea98e84fc75c4fbe4dd5c4a",
    },
    "notes": (
        "Paper 2 is the set-work / writing paper: Question 1 is a seen drama extract with contextual "
        "questions (Othello, Act 5 Scene 2), Question 2 is a literature essay on The Great Gatsby, "
        "Question 3 is transactional writing (blog, dialogue, formal letter). These competences are "
        "distinct from Paper 1 language skills and must not be merged into one family. The memorandum "
        "answers Question 1 in full but only restates Questions 2 and 3 with no model answer and no "
        "rubric, so the essay and transactional records carry no marking evidence."
    ),
}

SCHEMA = (
    "qn", "marks", "section", "qformat", "text", "set_text", "has_visual",
    "memo_evidence", "memo_answer", "memo_steps", "memo_notes", "rubric_ref",
    "allocation", "needs_visual", "ocr_uncertain",
)

STEMS = {}

RECORDS = [
    # ---------------- QUESTION 1: OTHELLO, Act 5 Scene 2 (20) ----------------
    ("1.1", 1, "Drama", "Short Answer",
     "Read the extract from Othello, Act 5 Scene 2, printed in the paper. To what 'cause' is "
     "Othello referring in line 1?", "Othello", False, "model_answer",
     "The cause relating to killing his wife. Desdemona must die for the greater good.",
     ["the cause is the killing of Desdemona for the greater good"],
     "One mark; the memo's answer joins the act to its justification.",
     False, "allocated", False, False),

    ("1.2", 2, "Drama", "Extended/Paragraph Response",
     "Explain the effectiveness of his repeating the word 'cause' in the first 3 lines.",
     "Othello", False, "model_answer",
     "Othello is unsure, he needs to convince himself that he is doing the right thing, that he is "
     "killing her because of a 'cause'.",
     ["insecurity / self-persuasion", "he needs to convince himself the killing is justified"],
     "Two marks for the psychological effect the repetition reveals.",
     False, "allocated", False, False),

    ("1.3", 1, "Drama", "Short Answer",
     "Mention a reason that Othello gives for needing to perform such a deed?", "Othello", False,
     "model_answer",
     "To save Desdemona from betraying other men in the way he thinks she has betrayed him.",
     ["so that she cannot betray more men"],
     "One mark; the reason is printed in the extract ('else she'll betray more men').",
     False, "allocated", False, False),

    ("1.4", 3, "Drama", "Extended/Paragraph Response",
     "Refer to lines 13, 14 and 15. Explain how Othello's use of imagery to describe Desdemona is "
     "appropriate to her character.", "Othello", False, "model_answer",
     "Othello compares her to a rose. He must pluck the rose, destroy it so that it cannot grow any "
     "more. Desdemona is as beautiful as a rose, as delicate and as sweet.",
     ["the rose image identified",
      "the act of plucking/destroying the rose explained",
      "the appropriateness to Desdemona (beautiful, delicate, sweet)"],
     "Three marks; the image, its action and its aptness for her character.",
     False, "allocated", False, False),

    ("1.5", 2, "Drama", "Extended/Paragraph Response",
     "What do you understand by the paradox in lines 18 and 19, '...when thou art dead, and I will "
     "kill thee and love thee after.'", "Othello", False, "model_answer",
     "This statement sounds like a contradiction. When Desdemona is dead at his hand, he will love "
     "her in eternity where she will be his alone and he won't have to share her with Cassio, or "
     "anyone else.",
     ["the contradiction named",
      "resolution: in death she is his alone, no longer shared"],
     "Two marks: the paradox and its resolution.",
     False, "allocated", False, False),

    ("1.6", 5, "Drama", "Extended/Paragraph Response",
     "What do Othello's lines (1-22) reveal about his change in character in the play? Provide an "
     "example from earlier in the play to support your answer.", "Othello", False, "model_answer",
     "Othello was a confident general in the beginning of the play. He loved his wife and was "
     "confident that she loved him back. They were married in secret against her father's wishes — "
     "how much more proof of love could there be. He referred to her as 'kind and gentle Desdemona' "
     "in earlier lines. As the play progresses, Othello changes and becomes cruel, suspicious and "
     "won't even talk to Desdemona. He tells her that he won't consider her request to re-instate "
     "Cassio and commands her to go to bed. He screams at her and calls her a strumpet. (Answer must "
     "focus on Othello's change in character, not on Iago's manipulation of him.)",
     ["the earlier Othello characterised (confident, loving)",
      "supporting example from earlier in the play",
      "the changed Othello characterised (cruel, suspicious, violent)",
      "supporting example from the extract",
      "focus must be on the change in Othello, not on Iago"],
     "Five marks; the memo's bracketed instruction explicitly warns that an answer about Iago's "
     "manipulation does not answer this question.",
     False, "allocated", False, False),

    ("1.7", 4, "Drama", "Extended/Paragraph Response",
     "To what extent is Iago responsible for Othello's change in character? Provide an example from "
     "the play to support your answer.", "Othello", False, "model_answer",
     "Iago is largely responsible for Othello's change in character. He manipulates Othello by "
     "planting seeds in his mind that Desdemona and Cassio are in a relationship. He places Othello "
     "in a trance to control him. He invents stories of Desdemona and Cassio lying together and "
     "whispering to each other. He steals her handkerchief and plants it in Cassio's room to "
     "implicate him.",
     ["a position on the extent of Iago's responsibility",
      "manipulation: planting suspicion",
      "specific plot evidence (trance, invented stories, handkerchief)"],
     "Four marks; 'to what extent' requires a judged position plus evidence, not a summary of Iago.",
     False, "allocated", False, False),

    ("1.8", 2, "Drama", "Extended/Paragraph Response",
     "Why does Othello ask his wife if she has prayed?", "Othello", False, "model_answer",
     "He does not want her soul to go to hell if she has not been absolved of her sins / if she has "
     "not asked for forgiveness for the day's sins — a common superstition.",
     ["concern for her soul",
      "the belief that an unprepared death damns the soul"],
     "Two marks; note the memorandum prints this item again as '1.7' (numbering error), so it is "
     "paired here by content and mark.",
     False, "allocated", False, False),

    # ---------------- QUESTION 2: LITERATURE ESSAY (30) ----------------
    ("2.1", 30, "Essay Writing", "Essay",
     "Write a literary essay on The Great Gatsby: 'For such a short title, The Great Gatsby raises a "
     "lot of questions. Is Gatsby great? Or is Fitzgerald being ironic? And why is he \"the\" great "
     "Gatsby? Discuss to what extent Gatsby deserves the title GREAT.' Length: approximately 450-500 "
     "words. Close and relevant reference to the novel is essential.", "The Great Gatsby", False,
     "restated_only",
     "NOT ANSWERED IN THE MEMORANDUM — the memorandum restates the essay topic and its conditions "
     "but prints no model essay, no rubric and no level descriptors.",
     ["no marking evidence printed"],
     "The 30 marks are allocated by the paper and the cover table. No marking requirements can be "
     "derived for this record from the supplied memorandum, so the essay is not used as family "
     "evidence in Pass 2.",
     False, "allocated", False, False),

    # ---------------- QUESTION 3: TRANSACTIONAL WRITING (answer TWO of three) ----------------
    ("3.1", 20, "Transactional Writing", "Extended/Paragraph Response",
     "Write a blog of 200-250 words in which you discuss your opinion on graffiti as an art form "
     "which is met with mixed emotions. Remember to personalise your response and to avoid "
     "generalisations.", None, False, "restated_only",
     "NOT ANSWERED IN THE MEMORANDUM — the option is restated with the paper's instruction only.",
     ["no marking evidence printed"],
     "Transactional-writing option; no model response or rubric in the supplied memorandum.",
     False, "alternative", False, False),

    ("3.2", 20, "Transactional Writing", "Extended/Paragraph Response",
     "Write a dialogue of 200-250 words in which you, as the grade representative, convince your "
     "Headmaster that the Matric Dance should not be cancelled after negative Facebook posts about "
     "its cost. Begin your dialogue with the printed Headmaster's line: 'I believe you are here to "
     "convince me that I should not do away with the Matric Dance. I hope you have a most convincing "
     "argument.' (Facebook posts are printed as source material in the paper.)", None, False,
     "restated_only",
     "NOT ANSWERED IN THE MEMORANDUM — the option is restated with the paper's instruction only. "
     "The memorandum mis-numbers this item '2' instead of '3.2'.",
     ["no marking evidence printed"],
     "Transactional-writing option; no model response or rubric in the supplied memorandum.",
     False, "alternative", False, False),

    ("3.3", 20, "Transactional Writing", "Extended/Paragraph Response",
     "Write a formal letter of complaint of 200-250 words to the Dean of a university of your choice "
     "arguing that the new admission requirement — a D symbol or higher for Afrikaans Additional "
     "Language for entry to any faculty — is most unfair. Use the correct format.", None, False,
     "restated_only",
     "NOT ANSWERED IN THE MEMORANDUM — the option is restated with the paper's instruction only.",
     ["no marking evidence printed"],
     "Transactional-writing option; no model response or rubric in the supplied memorandum.",
     False, "alternative", False, False),
]
