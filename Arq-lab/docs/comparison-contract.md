# Comparison Contract

`comparison.json` should contain at least:

```json
{
  "scenarioId": "G-V1-JAVA-001",
  "milestone": "M1",
  "module": "guardian",
  "applicationKey": "arq-lab-g-v1-java-001",
  "scanRunId": "uuid",
  "runnability": {
    "build": "passed",
    "test": "passed",
    "smoke": "passed"
  },
  "mustFindExpected": 3,
  "mustFindMatched": 3,
  "mustFindMissing": [],
  "mustNotFindViolations": [],
  "extraFindings": [],
  "mayFindReview": [],
  "explainabilityFailures": [],
  "refStateFailures": [],
  "verdict": "PASS",
  "followUpAction": "none"
}
```

## Special notes

### Guardian
Prefer comparison against:
- rule family / rule key
- normalized path
- branch name
- exposure fields

### Quantum
Prefer comparison against:
- rule family / rule key
- normalized path
- query family
- resolved value (where stable enough)
- explainability field presence
