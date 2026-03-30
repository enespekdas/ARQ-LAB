# API and execution notes for ARQ Lab

Bu not, prompt'larda kullanılan automation beklentilerini özetler.

## ARQ API workflow

### 1) Login
`POST /api/v2/auth/login`

Suggested payload:
```json
{
  "workspaceKey": "default",
  "email": "<ARQ_EMAIL>",
  "password": "<ARQ_PASSWORD>"
}
```

### 2) Project create or reuse
`POST /api/v2/projects`

### 3) Application create
`POST /api/v2/applications`

Suggested repository source:
```json
{
  "providerType": "GENERIC_GIT",
  "repositoryLocator": "http://localhost:3000/arq/repo-name.git",
  "defaultBranch": "main"
}
```

### 4) Application scan
`POST /api/v2/scans/application`

Example head snapshot:
```json
{
  "applicationId": "<uuid>",
  "modules": ["guardian"],
  "refName": "main",
  "scanMode": "HEAD_SNAPSHOT",
  "branchScope": "SINGLE_BRANCH"
}
```

Example Guardian history:
```json
{
  "applicationId": "<uuid>",
  "modules": ["guardian"],
  "refName": "main",
  "scanMode": "REF_HISTORY"
}
```

Example all branches:
```json
{
  "applicationId": "<uuid>",
  "modules": ["guardian"],
  "scanMode": "HEAD_SNAPSHOT",
  "branchScope": "ALL_BRANCHES"
}
```

## Important behavior assumptions

- `REF_HISTORY` should be used only for Guardian scenarios.
- Quantum scenarios should use `HEAD_SNAPSHOT`.
- `ALL_BRANCHES` should omit or ignore `refName`.
- Findings list is intentionally lean.
- Explainability assertions should use finding detail and occurrences endpoints.

## Findings export

`GET /api/v2/reports/findings`

Typical filters to use:
- `applicationId`
- `module`
- `branchName`
- `ruleKey`
- `limit`
- `format=json`

## Finding detail

- `GET /api/v2/findings/{id}`
- `GET /api/v2/findings/{id}/occurrences`

Quantum explainability assertions should check:
- `detectionSource`
- `semanticKey`
- `explainability.resolvedValue`
- `explainability.resolutionScope`
- `explainability.queryFamily`
- `explainability.rawEvidenceJson`

Guardian-specific exported fields should check:
- `presentOnHead`
- `presentInHistory`
- `exposureScope`
- `scanMode`

## Gitea notes

Use Gitea API and git CLI together:
- Gitea API: create repo, check repo exists
- git CLI: push main and branches, tags if needed

Public repo recommendation:
- create repos as public to keep ARQ clone step simple under `GENERIC_GIT`
