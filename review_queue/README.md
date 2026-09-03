# Human Review Queue

Per `RUN_LOG_SPEC` §10, use this directory whenever the system encounters an
item that requires human review. Each item is recorded as a separate file (in
`*.yaml` form) and must state:

```yaml
issue:            # what needs review
affected_entity:  # the entity ID / artifact involved
evidence:         # IDs backing the concern
possible_resolutions: # options
recommended_review:   # who / what kind of review
```

Use the queue for:

* inaccessible source
* ambiguous extraction
* uncertain question segmentation
* uncertain memo alignment
* disputed question classification
* uncertain curriculum mapping
* low-confidence Understanding Model
* conflicting source evidence

At Phase 1 (repository bootstrap) no curriculum material has been processed, so
this queue is empty by design. Items will be added from Phase 2 onwards.
