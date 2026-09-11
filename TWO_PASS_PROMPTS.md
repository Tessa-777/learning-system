# Two-Pass Knowledge Bank Construction — Grade 11 Adaptive Socratic Tutor

Aligned to System Specification v1.1.0. Pass 1 produces Tier 1 evidence (§5) with
provenance (§14) and fidelity-ladder tagging (§17.2). Pass 2 consumes a batch of
Pass 1 output and produces Tier 2/3 objects — question families, Understanding
Models (§9), breakdown models (§10), diagnostics (§11) — never touching the raw
PDFs directly.

**Do not skip straight to Pass 2.** Pass 2's entire value is that it can point
back at specific Pass 1 question IDs as evidence (§14). If you paraphrase or
summarize papers into Pass 2 by hand, you lose that chain and everything Pass 2
produces becomes an unprovenanced Tier 3 claim.

---

## How the two passes fit together

```text
one paper + its memo  →  PASS 1  →  question_records[] (JSON, small)
                                            |
   (repeat per paper, same subject)        |
                                            v
        batch of question_records[]  →  PASS 2  →  question_families[]
                                                     understanding_models[]
                                                     breakdown_models[]
                                                     diagnostic_questions[]
                                                     unresolved_items[]
```

Run Pass 1 once per paper (small upload, cheap, mechanical — an AI is good at
this). Accumulate the JSON outputs. Only when you have a batch (start with your
first stratified sample, e.g. 8-15 papers for a subject) do you run Pass 2. Pass
2's job is comparison across many records at once, which is why it needs to see
a batch, not a single paper.

After each new paper is added and re-run through Pass 2, check the saturation
test (§17.3) before deciding whether to acquire more.

---

# PASS 1 — Per-paper extraction (Tier 1 evidence)

Run this once per paper+memo pair. Output stays small and mechanical on
purpose — Pass 1 should not attempt to identify families or write Understanding
Models. That temptation should be resisted explicitly in the prompt, because
without a comparison set, any "this is part of a family" claim it makes is
unfounded (§5 Tier 3 leaking into Tier 1).

## Shared Pass 1 instructions (prepend to every subject below)

```
You are performing PASS 1 of a two-pass knowledge extraction pipeline for a
Grade 11 tutoring system. Your job in this pass is EVIDENCE EXTRACTION ONLY.

Do NOT attempt to:
- identify question families
- write Understanding Models
- generalize across questions
- state what a topic "always" requires

You are looking at ONE paper and its memorandum. Extract each question as a
discrete, provenanced record. Any pattern-spotting happens in a later pass that
can see many papers at once — you cannot see that here, so do not claim it.

For every question record, generate:
- source_id: a stable ID you construct as {subject}_{year}_{exam_board}_{paper_type}_{exam_period}_{question_number}
  e.g. "history_2022_NSC_paper1_nov_q3.1"
- source_document: the filename/title of the paper as given
- source_document_sha256: if you are given a hash, include it; otherwise write "NOT_PROVIDED — caller must supply"
- memo_document: the filename/title of the matching memo
- fidelity_rung: "A" if you were given the original file bytes/a clean digital PDF,
  "B" if you're working from an OCR'd or converted transcription, "C" if you
  only have metadata and no real content (in which case do not fill in
  question_text or memo fields — just record that the source exists)
- requires_visual_verification: true if this question's meaning depends on a
  diagram, graph, circuit, image, map, or source-booklet visual that you cannot
  fully verify from what you were given; false otherwise
- ocr_uncertain: true if any part of your transcription is a low-confidence guess

Then the subject-specific fields listed below.

Output a JSON array, one object per question/sub-question. Treat each
mark-bearing sub-part (e.g. 3.1, 3.2.1) as its own record with
"parent_question_id" pointing to the stem it belongs to, plus a
"question_stem_text" field on the child giving the shared stem/context if the
sub-parts depend on shared context (e.g. a shared source, diagram, or passage).

Do not skip short questions, multiple-choice questions, or questions you find
trivial. Do not reproduce full extended source passages/extracts verbatim —
describe them (e.g. "Source 2B: photograph of Berlin Wall construction, 1961")
and cite what the question asks about them.

If you cannot determine a field confidently, write "unresolved" rather than
guessing. Do not silently invent a topic, mark allocation, or memo answer that
isn't actually shown in the material you were given.
```

## Subject-specific fields — Pass 1

Append the relevant block to the shared instructions above, per subject.

### Mathematics
```
Add these fields to each question record:
- marks
- topic_guess: your best guess at CAPS topic (Algebra & Equations, Number
  Patterns, Functions & Graphs, Trigonometry, Euclidean Geometry, Analytical
  Geometry, Finance & Growth, Statistics, Probability, Measurement) — label as
  "guess" because topic confirmation happens in Pass 2 against the full sample
- question_text (preserve mathematical notation)
- has_diagram
- memo_answer
- memo_method_steps: array of each discrete marked step shown in the memo, not
  just the final answer
- memo_marking_notes: any special instruction (ecf, alternative acceptable forms, etc.)
- calculator_allowed (if stated on the paper)
```

### AP Mathematics
```
Add these fields to each question record:
- marks
- module_guess: your best guess (Calculus, Statistics, Matrices, Algebra,
  Calculus of Motion, Other) — label as "guess"
- question_text (preserve mathematical notation)
- has_diagram
- memo_answer
- memo_method_steps
- memo_marking_notes
- apparent_prerequisite_core_topics: Core Maths topics this question seems to
  assume, if obviously identifiable from the question itself (do not infer
  beyond what's visible in this single paper)
```

### Physical Science (Physics and Chemistry)
```
Add these fields to each question record:
- marks
- discipline: "Physics" or "Chemistry" (from paper label + content — flag
  mismatch if the paper says one but content suggests the other)
- topic_guess (Physics: Mechanics-Forces, Mechanics-Momentum, Waves Sound
  Light, Electrostatics, Electric Circuits, Electromagnetism / Chemistry:
  Matter & Materials, Atomic Structure, Bonding, Intermolecular Forces,
  Chemical Change, Reaction Rates, Energy & Chemical Change, Acids & Bases)
- question_type: Multiple Choice, Calculation, Definition/Explain,
  Diagram-based, Data/Graph Interpretation, Experiment/Investigation
- question_text (include full MCQ options; describe circuit/apparatus diagrams)
- has_diagram
- required_formulae_visible: formulae explicitly needed, as shown
- memo_answer (include units exactly as given)
- memo_method_steps
- memo_marking_notes
```

### English
```
First state which paper type this is: Language (comprehension/summary/
structures), Literature (novel/drama/poetry), or Writing (essay/transactional).

Add these fields to each question record:
- marks
- section_guess: Comprehension, Summary, Language Structures & Conventions,
  Visual Literacy, Poetry (Seen), Poetry (Unseen), Novel, Drama, Short Stories,
  Essay Writing, Transactional Writing
- set_text_title (name the specific novel/drama if applicable; null if unseen/generic)
- question_text (reference paragraph/stanza/act-scene-line; do NOT reproduce
  the full source extract — note "refer to source paper" instead)
- question_format: Multiple Choice, Short Answer, Extended/Paragraph Response,
  Essay, Table/Matching
- memo_answer (or memo's model answer)
- memo_marking_notes
- rubric_reference: true if memo says "mark per rubric/annexure" rather than
  giving a direct answer — if true, summarize the rubric's stated criteria
  rather than reproducing a full sample essay verbatim
```

### History
```
Add these fields to each question record:
- marks
- topic_guess: the CAPS topic this seems to belong to (e.g. Russian Revolution,
  Scramble for Africa, Ideas of Race, Industrialisation, Origins of WWI) —
  label as "guess"
- question_format: Source-based Question, Essay, Structured/Short Answer
- skill_focus_guess: Extract Evidence, Compare Sources, Evaluate Reliability/
  Usefulness/Bias, Contextualise, Explain Causation, Explain Significance/
  Consequence, Construct Argument
- source_reference: describe what the source is (type, date, what it shows) —
  do not reproduce lengthy extracts in full
- question_text
- memo_answer (the memo's expected points, as given)
- memo_marking_notes
- essay_rubric_levels_if_present: if this is a level-marked essay, summarize
  the level descriptors shown in the memo (don't reproduce the full official
  rubric verbatim if lengthy — summarize the distinguishing criteria per level)
```

### Biology (Life Sciences)
```
Add these fields to each question record:
- marks
- topic_guess: Plant Nutrition & Transport, Animal Nutrition, Gas Exchange,
  Excretion, Human Reproduction, Population Ecology, Human Impact on Environment
- question_type: Multiple Choice, Definition/Terminology, Labelling/Diagram,
  Short Answer, Data/Graph Interpretation, Extended Response/Essay
- question_text (describe diagrams, e.g. "nephron diagram, labels A-E")
- has_diagram
- memo_answer
- memo_marking_notes
- key_terminology_tested: array of biological terms this question specifically tests
```

---

# PASS 2 — Cross-paper synthesis (Tier 2/3: families, models, breakdowns, diagnostics)

Run this against a **batch** of Pass 1 JSON output for one subject — not the
original PDFs. Re-run as the batch grows, and check the saturation test each
time.

## Shared Pass 2 instructions (prepend to every subject below)

```
You are performing PASS 2 of a two-pass knowledge extraction pipeline for a
Grade 11 tutoring system. You are given a batch of PASS 1 question records
(JSON) for one subject — not raw papers. Your job is to find what repeats
across this batch and compress it into the objects below. Every claim you make
must cite the specific source_id values from the batch that support it. If you
cannot point to at least two independent source_ids supporting a claim, do not
assert it as a validated pattern — put it in unresolved_items instead, tagged
"single_exemplar."

Do not import general knowledge about what "History source questions usually
want" or "how Physics calculations are usually marked" from outside this batch.
Every pattern must be grounded in the actual records provided (Tier 1 evidence,
per the spec's source-of-truth hierarchy). If the batch is too small or too
uniform to support a claim, say so explicitly rather than filling the gap with
plausible-sounding general knowledge — that would be an unprovenanced Tier 3
claim wearing a Tier 2 label.

Produce four kinds of output:

1. QUESTION FAMILIES
A question family is a recurring pattern of question — same underlying
competence being assessed, even if surface wording/numbers differ. For each
family:
- family_id
- family_name (short, descriptive — this is what the student should learn to
  recognise, e.g. "Evaluate source reliability using content + origin")
- member_source_ids: array of Pass 1 source_ids that belong to this family
  (minimum 2 — a family with only 1 member is not yet a family, log it in
  unresolved_items as "single_exemplar" instead)
- distinguishing_features: what makes a question recognisably belong to this
  family (wording patterns, command verbs, structural cues)
- typical_marks_range

2. UNDERSTANDING MODELS (per §9 of the spec)
One per question family, containing exactly these fields:
- identity, definition
- subject, grade (11)
- topic
- question_family (the family_id from above)
- assessment_operations: what the student is actually asked to DO (not just
  the topic — e.g. "identify", "evaluate", "compare", "calculate and justify")
- required_knowledge
- prerequisites
- required_reasoning
- required_procedure
- evidence_of_understanding: what a response has to contain/demonstrate to
  show real understanding, distinct from just reaching the correct final answer
- marking_requirements: derived from the memo_method_steps/memo_marking_notes
  across the family's member questions — what actually earns marks
- common_breakdowns: see breakdown model below, referenced by ID
- misconceptions: plausible incorrect beliefs that would produce a wrong answer
  here (mark clearly as Tier 3 inference if not directly evidenced in a memo's
  "common error" notes)
- diagnostic_dimensions
- diagnostic_questions: referenced by ID, see diagnostic model below
- source_references: array of member_source_ids this model is built from
- confidence: "high" if supported by 4+ member questions across different
  papers, "medium" if 2-3, and this field must not be "high" if all supporting
  questions come from the same single paper
- validation_state: "unvalidated" (Pass 2 output is not yet human-reviewed —
  do not mark it "validated" yourself)
- version: "0.1.0-draft"

3. BREAKDOWN MODELS (per §10)
For each Understanding Model, identify which of these stages plausibly apply
(not all questions need all stages — say which ones are relevant here and why):
question interpretation → prerequisite knowledge → conceptual understanding →
strategy/method selection → execution → reasoning → explanation →
verification/evaluation

For each applicable stage, describe what a breakdown at that stage would look
like — specific enough that a tutor could tell it apart from a breakdown at a
different stage. Ground this in memo_marking_notes where you can (e.g. if the
memo separately allocates marks for "correct method" vs "correct final answer,"
that's direct evidence of a strategy-selection/execution split).

4. DIAGNOSTIC QUESTIONS (per §11)
For each Understanding Model, propose 2-4 diagnostic questions the tutor could
ask to determine whether the student has this understanding, WITHOUT giving
away the answer. For each:
- what it's trying to determine
- which understanding_model it belongs to
- which breakdowns it helps distinguish between
- what kind of student response would count as evidence, and of what

Also produce:

5. UNRESOLVED_ITEMS
Anything you noticed but couldn't validate: single-exemplar patterns,
source_ids with fidelity_rung "C" that couldn't contribute evidence,
source_ids flagged requires_visual_verification that you couldn't confirm,
contradictions between memos, or topics that appear in the CAPS curriculum but
have zero source_ids in this batch (curriculum gaps — these matter for §17.4:
the tutor must never answer as if these are grounded in the knowledge bank).

Output as JSON with five top-level arrays: question_families, understanding_models,
breakdown_models, diagnostic_questions, unresolved_items.

Finally, output a SATURATION REPORT object per §17.3 with these exact fields:
papers_in_sample, question_families_identified, families_first_observed_in_final_third,
strata_left_unsampled, families_supported_by_single_exemplar.
To compute families_first_observed_in_final_third: order the source papers in
this batch by the sequence they were acquired/added (ask the user for this
order if not given), split into thirds, and check whether any family's
member_source_ids are ALL drawn from only the final third — if so, that family
counts here. This number must be reported honestly; a subject cannot be
declared saturated while this is greater than 0.
```

## Subject-specific notes — Pass 2

These are short because Pass 2's structure (families → models → breakdowns →
diagnostics) is identical across subjects; only emphasis differs.

### Mathematics / AP Mathematics
```
Pay particular attention to marking_requirements: Math/AP Math memos almost
always separate "method marks" from "accuracy marks" — make sure
understanding_models distinguish "knows the right method" from "can execute it
correctly," since these are genuinely different breakdown stages here and
conflating them will make the tutor's diagnosis useless.

For AP Mathematics specifically: if a family's questions consistently assume
fluency in a Core Maths topic not itself covered in this batch, log that as a
prerequisite gap in unresolved_items, not as an assumed-known field.
```

### Physical Science
```
Cross-check discipline tagging (Physics vs Chemistry) for consistency within a
family — a family should not silently mix disciplines. Pay attention to
requires_visual_verification flags from Pass 1: a family built primarily from
circuit-diagram or graph-interpretation questions where several members are
Rung B and visually unverified should have confidence capped at "medium" and
should note this explicitly, per §17.2 ("Rung B is not acceptable, on its own,
for any question whose meaning depends on a diagram...").
```

### English
```
Keep Literature families separate per set text where the skill is genuinely
text-specific (e.g. a "theme in [novel]" family) vs genuinely general-purpose
skill families that would recur regardless of the specific text (e.g.
"identify use of figurative language and its effect" applies across poetry,
novel, and unseen extracts — treat this as one family with multi-text evidence,
not three separate ones).
```

### History
```
Source-based question families are usually the highest-value output here — this
is explicitly what the user described their brother having already internalised
(e.g. "when I see this kind of source question, they always want 4 things, in
this order"). Make sure assessment_operations and marking_requirements capture
not just WHAT is wanted but the ORDER/structure the memo rewards, if the memo's
point allocation implies one. Essay-question families should have their
essay_rubric_levels_if_present data (from Pass 1) synthesized into a single
clear level-descriptor summary in evidence_of_understanding.
```

### Biology
```
Distinguish "recall terminology" families from "apply/explain mechanism"
families even within the same topic — these are different competences with
different breakdown profiles (a student can define "osmosis" correctly and
still fail to apply it to an exam data-interpretation question). Don't merge
them into one family just because they share a topic_guess.
```

---

## Practical run order (ties back to the upload-size question)

1. Unzip each subject's archive locally. You now have individual PDFs.
2. Group what you have by form (paper number × exam board × sitting), per §17.1.
3. Pick a first stratified sample — roughly 8-15 papers per subject is a
   reasonable starting batch, not the full archive.
4. Run Pass 1 once per paper+memo (small individual uploads — this is what
   avoids the 400MB problem entirely; you're never uploading more than one
   paper at a time).
5. Collect the Pass 1 JSON outputs into one file per subject.
6. Run Pass 2 on that batch.
7. Check the saturation report. If `families_first_observed_in_final_third > 0`,
   acquire a few more papers targeted at whichever stratum produced the new
   family (not a blanket re-acquisition), then re-run Pass 1 on just those new
   papers and re-run Pass 2 on the updated batch.
8. Repeat until saturation holds, then this subject's knowledge bank moves to
   human validation before being versioned (§13) as e.g. `history@1.0.0`.