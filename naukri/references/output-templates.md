# Output Templates

Exact layouts to reuse when reporting results. Keep tables plain Markdown so they render correctly in any chat interface.

## 1. Job normalization summary (end of Stage 1)

```
**Job:** <Title> — <Company>
**Level:** <level>  **Location:** <location>  **Arrangement:** <onsite/hybrid/remote>
**Posted:** <date, or "unknown">  **Age:** <N days> (<inside/outside> 72h window)
**ATS platform:** <Greenhouse/Workday/Lever/Taleo/iCIMS/unknown>
**Sponsorship language:** <quote or "none found">
**Compensation:** <range or "not listed">
```

## 2. Hard-gate check

```
| Gate | Requirement | Candidate status | Result |
|---|---|---|---|
| Work authorization | ... | ... | Pass/Fail/Uncertain |
| Location/relocation | ... | ... | Pass/Fail/Uncertain |
| Clearance | ... | ... | Pass/Fail/N-A |
| Required degree/license | ... | ... | Pass/Fail/N-A |
| Minimum experience | ... | ... | Pass/Fail |
| Central function present | ... | ... | Pass/Fail |
```

If any row is Fail → stop and report: **DO NOT APPLY — failed: <gate name>**.
If any row is Uncertain → ask the user that specific question before continuing.

## 3. Evidence matrix (Stage 4)

```
| Requirement | Evidence | Strength | Resume location |
|---|---|---|---|
| <requirement 1> | <what the vault shows> | Direct/Adjacent/Weak/Missing | <section> |
```

## 4. Score breakdown (§16, scoring-rubric.md)

```
| Component | Weight | Score | Notes |
|---|---:|---:|---|
| Required-skill evidence | 25 | | |
| Core-responsibility evidence | 25 | | |
| Seniority and scope alignment | 15 | | |
| Domain relevance | 10 | | |
| Demonstrated outcomes | 10 | | |
| ATS parseability | 10 | | |
| Human readability and clarity | 5 | | |
| **Total** | **100** | **<sum>** | |

**Timing:** posted <N> days ago — <inside/outside> the 72h window.
```

## 5. Verdict

```
**Verdict: APPLY / APPLY WITH REFERRAL ONLY / SKIP**

Top 3 reasons:
1. ...
2. ...
3. ...

Biggest evidence gaps:
- ...
```

## 6. Factuality audit (Stage 9, if APPLY)

```
| Claim in draft resume | Source evidence | Status |
|---|---|---|
| <bullet text> | <vault entry / "needs your confirmation"> | Confirmed/Needs confirmation |
```

## 7. Tracker line (§19)

Single pipe-delimited line the user can paste into a spreadsheet:

```
<company> | <title> | <job URL or req ID> | <date posted> | <date applied> | <channel> | <referral Y/N> | <evidence score> | <resume version> | <ATS platform>
```

## 8. Knockout-question reminder (§14, if APPLY)

```
Before submitting, double-check these application-form answers match the resume:
- Work authorization / sponsorship: ...
- Willing to relocate / travel: ...
- Years of experience in <X>: ...
- Highest degree: ...
```
