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
  "cleanExpectedMatches": 3,
  "mustFindMatched": 3,
  "mustFindMissing": [],
  "missingExpectedFindings": [],
  "mustNotFindViolations": [],
  "sameSurfaceExtraFindings": [],
  "sameFileDifferentSignalFindings": [],
  "unexpectedFindings": [],
  "extraFindings": [],
  "mayFindReview": [],
  "unexpectedRegexOnlyFindings": [],
  "explainabilityFailures": [],
  "refStateFailures": [],
  "noiseCount": 0,
  "noiseBreakdown": {},
  "verdict": "PASS_CLEAN",
  "verdictClass": "PASS_CLEAN",
  "finalVerdictReason": "all expected findings matched cleanly with no unexpected noise",
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

Regex-only Quantum hits must not satisfy a semantic-required expectation by themselves. When a scenario declares an explainability contract, expected positives should only be counted as clean matches if the exported finding carries real explainability signal.
