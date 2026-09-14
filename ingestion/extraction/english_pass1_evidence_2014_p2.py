"""Pass 1 evidence table — Grade 11 English Paper 2, July 2014 (set work + writing).

Authored by reading the extracted text of the paper (.docx) and its memorandum.

Paper: data/organized/english/Grade 11 Paper 2 July 2014.docx      (80 marks)
Memo:  data/organized/english/Grade 11 Paper 2 July Memo.docx      (no header printed)

PAIRING EVIDENCE (printed content, not the inherited manifest): the memorandum
prints no header block, so it cannot be paired on DATE/MARKS/EXAMINER. It is
paired instead on numbered content that matches this paper item-for-item — the
same two extracts from The God of Small Things, the same 1.1-1.10 numbering and
the same bracketed marks, verified one by one — together with the Phase-2
inventory record for this file (SOURCE-ORC-ENG-2014-007: year 2014, term 2,
paper 2, document_type memorandum), which the paper's own header corroborates
(DATE 25 July 2014). No other sitting in the batch uses this set text, and
neither the essay nor the blog of any other year is answered by this memo. This
is precisely the pairing the document-level stub batch got wrong: it attached
the July 2013 paper to the 2025/26 memorandum.

SCOPE OF THE MEMORANDUM: it marks Question 1 only (The God of Small Things
contextual, 1.1-1.10, 30 marks). Question 2 (essay) and Question 3 (blog) are
restated by the paper but receive no marking evidence.
"""

PAPER = {
    "paper_key": "ENG-2014-JUL-P2",
    "paper_path": "data/organized/english/Grade 11 Paper 2 July 2014.docx",
    "memo_path": "data/organized/english/Grade 11 Paper 2 July Memo.docx",
    "year": 2014,
    "exam_date": "25 July 2014",
    "exam_period": "july",
    "paper_number": "P2",
    "paper_type": "paper2",
    "exam_board": "internal",
    "paper_focus": "Literature and Writing — set-work contextual questions, literature essay, transactional writing",
    "total_marks": 80,
    "examiner": "Mr De Reuck, Mrs De Reuck, Mrs Oosthuysen",
    "moderator": "Mrs Nichas",
    "duration_stated": {"paper": "2 1/2 hours", "memo": None},
    "fidelity_rung": "A",
    "marks_style": "trailing",
    "section_totals": {"1": 30, "2": 30, "3": 20},
    "section_totals_basis": "printed section headings (question 1 – The God of Small Things30 Marks CONTEXTUAL, Question 2 – THE GOD OF SMALL THINGS 30 marks ESSAY, question 3 – transactional writing20 marks), which sum to the header MARKS 80",
    "cover_table_absent_reason": (
        "the paper prints no 'Possible Marks' cover row — its cover carries only the report block "
        "(STUDENT'S RESULT / COMMENT / signatures) — so the three section totals are read from the "
        "printed section headings and checked against the header MARKS 80"
    ),
    "pairing_basis": "content_and_printed_totals",
    "pairing_anchors": [
        "question 1 – The God of Small Things30 Marks",
        "1.1Explain what is meant by the comment: Estha had been re-Returned.3",
        "1.10",
    ],
    "pairing_note": (
        "The memorandum carries no header, so pairing is verified by identical numbered contextual "
        "items and marks (1.1-1.10 on The God of Small Things, 30 marks) plus the Phase-2 inventory "
        "record SOURCE-ORC-ENG-2014-007 (year 2014, P2, memorandum). No other sitting in the batch "
        "uses this set text and no other memorandum answers these items."
    ),
    "section_anchors": [
        "question 1 – The God of Small Things30 Marks CONTEXTUAL",
        "Question 2 – THE GOD OF SMALL THINGS 30 marks ESSAY",
        "question 3 – transactional writing20 marks",
    ],
    "memo_section_anchors": ["question 1 – The God of Small Things30 Marks CONTEXTUAL"],
    "item_anchor_overrides": {
        "2.1": {"paper": "Question 2 – THE GOD OF SMALL THINGS 30 marks ESSAY",
                "note": "the essay's marks are printed in its section heading, not after the item"},
        "3.1": {"paper": "question 3 – transactional writing20 marks",
                "note": "the blog's marks are printed in its section heading, not after the item"},
    },
    "memo_section_anchors_absent": [
        "Question 2 – THE GOD OF SMALL THINGS 30 marks ESSAY",
        "question 3 – transactional writing20 marks",
    ],
    "source_hashes": {
        "paper_path": "d3cf1f0fd1b8d68390b7b57c80622154be093743343d5a059edba99bbafdbae0",
        "memo_path": "6c842badb38c25b0909594410d0092a737c74c2a3ee6a010d07e3ed15502dfe0",
    },
    "notes": (
        "Paper 2 set-work / writing paper on The God of Small Things (Arundhati Roy). Question 1 "
        "prints two extracts — 'Paradise Pickles & Preserves' (Chapter 1, pp. 20-23) and 'The "
        "Pessimist and the Optimist' (Chapter 13, pp. 254-257). The memorandum answers Question 1 in "
        "full with rubric-style marking notes ('Mark for relevance and quoting from the extracts "
        "provided'); Question 2 (essay on the twins' destroyed innocence, 450-500 words with a plan) "
        "and Question 3 (blog on 'burning bling' / Izikhothane) have no marking evidence. This set "
        "text appears in no other sitting in the batch, which constrains family merging in Pass 2."
    ),
}

SCHEMA = (
    "qn", "marks", "section", "qformat", "text", "set_text", "has_visual",
    "memo_evidence", "memo_answer", "memo_steps", "memo_notes", "rubric_ref",
    "allocation", "needs_visual", "ocr_uncertain",
)

STEMS = {}

RECORDS = [
    # ---------------- QUESTION 1: THE GOD OF SMALL THINGS — CONTEXTUAL (30) ----------------
    ("1.1", 3, "Novel", "Extended/Paragraph Response",
     "Refer to Extract 1, 'Paradise Pickles & Preserves' (Chapter 1, pp. 20-23). Explain what is "
     "meant by the comment: Estha had been re-Returned.", "The God of Small Things", False,
     "model_answer",
     "Estha, when he was seven, was sent away from the family at Ayemenem. He was sent to stay with "
     "his father and was not seen again for 23 years. This became known as when Estha was 'Returned'. "
     "Now that he is back, he has been re-Returned, sent home.",
     ["the first 'Returning' explained (sent to his father at seven, gone 23 years)",
      "the term's origin in the family's language",
      "the present re-Return (sent home again)"],
     "Three marks across the two events and the coinage itself.",
     False, "allocated", False, False),

    ("1.2", 1, "Novel", "Short Answer",
     "Refer to Extract 1. What is the biological relationship between Estha and Rahel?",
     "The God of Small Things", False, "model_answer",
     "They are twins/siblings.",
     ["twins"],
     "One mark only; the memo accepts 'twins' or 'siblings'.",
     False, "allocated", False, False),

    ("1.3", 2, "Novel", "Extended/Paragraph Response",
     "Refer to Extract 1. How do you know from the extract that Estha and Rahel are connected on a "
     "spiritual and mental level?", "The God of Small Things", False, "model_answer",
     "Rahel was able to sense Estha and what he was feeling, doing and thinking. He was 'rocking', "
     "and Rahel could feel 'the wetness of rain on his (Estha's) skin'. Rahel is also able to hear "
     "Estha's thoughts in a way, hear 'the raucous, scrambled world inside his head'. This implies "
     "some psychic or spiritual connection.",
     ["sensory connection: she feels the rain on his skin / his rocking",
      "mental connection: she hears the world inside his head",
      "conclusion: a psychic/spiritual connection"],
     "Two marks requiring textual quotation from Extract 1 plus the inference.",
     False, "allocated", False, False),

    ("1.4", 3, "Novel", "Extended/Paragraph Response",
     "Refer to Extract 1. Account for the fact that Baby Kochamma is of the opinion that Estha has "
     "lost his mind.", "The God of Small Things", False, "model_answer",
     "Estha does not speak at all. He is a quiet man who goes on endless walks. He does not even "
     "greet his sister when he sees her again, for the first time in a very long time. Baby Kochamma "
     "views this very odd behaviour as a sign that Estha has gone mad, or has 'lost his mind'.",
     ["Estha's silence and endless walking",
      "he does not greet Rahel after years apart",
      "Baby Kochamma reads this behaviour as madness"],
     "Three marks; the behaviours and Baby Kochamma's interpretation of them.",
     False, "allocated", False, False),

    ("1.5", 2, "Novel", "Short Answer",
     "Refer to Extract 2, 'The Pessimist and the Optimist' (Chapter 13, pp. 254-257). What "
     "information is Vellya Paapen compelled to share with Mammachi?", "The God of Small Things",
     False, "model_answer",
     "The affair between Ammu and Velutha.",
     ["the affair between Ammu and Velutha"],
     "Two marks; the memo's answer is a single proposition.",
     False, "allocated", False, False),

    ("1.6", 3, "Novel", "Extended/Paragraph Response",
     "Refer to Extract 2. Why does he feel that he is torn between Loyalty and Love?",
     "The God of Small Things", False, "model_answer",
     "He feels an immense loyalty for the Ipe Family and all they have given him. He is also a victim "
     "of the discrimination in India and the caste system is entrenched within him. The loyalty he "
     "feels for the Ipe family is conflicting with the love he has for his son. If he is to be loyal "
     "he must destroy his son; if his love for his son stopped him, he would consider himself disloyal.",
     ["loyalty to the Ipe family (what they have given him)",
      "the caste system entrenched in him",
      "love for his son Velutha, whom loyalty requires him to destroy"],
     "Three marks; the memo spells out the double bind explicitly.",
     False, "allocated", False, False),

    ("1.7", 3, "Novel", "Extended/Paragraph Response",
     "Refer to Extract 2. How does Mammachi's response to touching Vellya Paapen's glass eye "
     "undermine her claim that she wasn't averse to listening to bardic stories about herself and "
     "her family's Christian munificence?", "The God of Small Things", False, "model_answer",
     "She has time to listen to how wonderful and Christian, how charitable, her family is. She "
     "wants to hear these stories but is so repulsed by the eye of Vellya Paapen because the eye is "
     "slimy with eye fluid from this 'untouchable', which means he is literally not meant to be "
     "touched. The caste distinction, at this time abolished by law, is very unchristian. So the "
     "irony of her enjoying hearing of her and her family's 'Christian munificence' contradicts her "
     "disgust at being exposed to a few eye juices.",
     ["her enjoyment of the family's munificence stories",
      "her physical repulsion at the untouchable's eye fluid",
      "the contradiction: respect for untouchability versus claimed Christian munificence"],
     "Three marks; the answer is an irony argument and the memo marks the contradiction.",
     False, "allocated", False, False),

    ("1.8", 3, "Novel", "Short Answer",
     "Refer to Extract 2. Baby Kochamma sees the situation as God's Way of punishing Ammu for her "
     "sins. According to Baby Kochamma, what are these sins?", "The God of Small Things", False,
     "model_answer",
     "Getting married without permission; leaving her husband / getting a divorce; Ammu dared to "
     "still have something exciting in her life rather than spend it repenting.",
     ["marrying without permission",
      "leaving her husband / divorcing",
      "having an exciting life instead of repenting"],
     "Three marks; the memo lists three sins.",
     False, "allocated", False, False),

    ("1.9", 4, "Novel", "Extended/Paragraph Response",
     "Refer to Extract 2. Discuss how the statement 'How could she stand the smell? Haven't you "
     "noticed? They have a particular smell, these Paravans' highlights the caste system which "
     "exists in India. Quote from the extract to support your answer.", "The God of Small Things",
     False, "model_answer",
     "The quote presents the reader with the irrational, generalised stereotyping that is typically "
     "associated with a system such as the caste system in India. The caste system places people in "
     "groups (which determine their pecking order within the society) from birth. These people are "
     "confined to these groups and labelled, stereotyped, and treated as such. Any suitable quote(s). "
     "Possible quote: 'She smelled her hands when she'd finished.'",
     ["the statement identified as irrational generalised stereotyping",
      "caste explained as a birth-assigned grouping with a pecking order",
      "quotation from the extract supporting the reading"],
     "Four marks; the memo accepts any suitable supporting quotation and marks both the reading of "
     "the statement and the description of caste.",
     False, "allocated", False, False),

    ("1.10", 6, "Novel", "Extended/Paragraph Response",
     "Refer to both extracts. Baby Kochamma is the character who the reader grows to dislike the "
     "most in the novel. Write a well-constructed paragraph in which you discuss her perception of "
     "the world and her attitude towards Estha and Rahel. Make close reference to the extracts "
     "provided.", "The God of Small Things", False, "rubric_reference",
     "Mark for relevance and quoting from the extracts provided.",
     ["memo gives a marking instruction rather than model content",
      "relevance to the question",
      "quotation from the extracts"],
     "The memorandum supplies a rubric instruction instead of a model paragraph: markers are told to "
     "mark for relevance and for quoting from the extracts. It describes a paragraph's construction "
     "only at that level, so no mark-by-mark breakdown can be transcribed.",
     True, "allocated", False, False),

    # ---------------- QUESTION 2: LITERATURE ESSAY (30) ----------------
    ("2.1", 30, "Essay Writing", "Essay",
     "The God of Small Things: 'The novel is the story of Rahel and Estha, twins growing up among "
     "the banana vats and peppercorns of their blind grandmother's factory, and amid scenes of "
     "political turbulence in Kerala. Armed only with the innocence of youth, they fashion a "
     "childhood in the shade of the wreck that is their family: their lonely, lovely mother, their "
     "beloved Uncle Chacko (pickle baron, radical Marxist) and their sworn enemy, Baby Kochamma "
     "(ex-nun, incumbent grand-aunt).' In an essay of 450-500 words discuss how Rahel and Estha's "
     "shared experiences, as well as the complex relationships within their dysfunctional family, "
     "destroy the innocence of their youth. Include a plan of your essay and ensure that you make "
     "close reference to the novel.", "The God of Small Things", False, "restated_only",
     "NOT ANSWERED IN THE MEMORANDUM — this paper's memorandum marks Question 1 only; the essay "
     "prompt is printed in the paper without any model essay, plan, rubric or level descriptors.",
     ["no marking evidence printed"],
     "30 marks allocated by the paper. Without marking evidence the essay cannot ground a Pass 2 "
     "breakdown; a plan is demanded by the wording, which is a notable form requirement.",
     False, "allocated", False, False),

    # ---------------- QUESTION 3: TRANSACTIONAL WRITING (20) ----------------
    ("3.1", 20, "Transactional Writing", "Extended/Paragraph Response",
     "Read the passage 'BURNING BLING' (printed in the paper) about Izikhothane youths in SA "
     "townships for whom 'fame comes at a staggering price' — they tear up or burn wads of cash, "
     "designer clothes and shoes and recklessly slosh expensive alcohol on the ground. Write a blog "
     "of 200-250 words in which you discuss your reaction to the idea of 'burning bling'.",
     None, False, "restated_only",
     "NOT ANSWERED IN THE MEMORANDUM — the blog instruction is printed in the paper; the "
     "memorandum supplies no model answer, checklist or rubric for it.",
     ["no marking evidence printed"],
     "20 marks allocated by the paper; no marking evidence, so no marking requirements can be derived.",
     False, "allocated", False, False),
]
