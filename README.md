# Naukri — job evaluation and resume tailoring skill

Paste a job description or job posting link and get: a hard-gate eligibility check, a requirement-to-evidence matrix, a 100-point Job–Resume Evidence Score, a clear **APPLY / APPLY WITH REFERRAL ONLY / SKIP** verdict, and — when the verdict is APPLY — a tailored, ATS-safe resume (DOCX + PDF) with a parseability check, a factuality audit, knockout-question reminders, and a one-line tracker record.

It never fabricates skills, titles, dates, employers, or metrics — every claim on a generated resume must trace back to your own material.

## What's inside

```
naukri/                       ← the skill folder — zip this to install
├── SKILL.md                  entry point: the workflow and when to use each reference
├── references/
│   ├── ats-guidelines.md     the full ATS/resume methodology (V2.1), numbered §1-19
│   ├── scoring-rubric.md     how to award points for each scoring component
│   ├── onboarding.md         first-run interview + how to build your vault
│   └── output-templates.md   exact report/table layouts
├── templates/
│   ├── candidate-profile.md  your hard-gate facts (work auth, location, level, ...)
│   ├── career-vault.md       your master evidence bank, one row per achievement
│   └── resume-variants.md    your 2-4 base resumes + routing rules
├── scripts/
│   ├── build_resume.py       JSON → ATS-safe DOCX (+ PDF)
│   ├── parse_check.py        verifies a generated resume parses correctly
│   └── resume_schema.json    input schema for build_resume.py
└── examples/
    └── jordan_lee.json       a fictional worked example
```

## Install

### Claude.ai (Settings → Capabilities/Skills)

1. Zip the `naukri/` folder (not the repo root — just the inner folder).
2. In Claude.ai, go to **Settings → Capabilities** (or **Skills**, depending on your plan) and upload the zip.
3. Start a chat and paste a job description or link.

### Cowork

Same as Claude.ai — upload the zipped `naukri/` folder wherever Cowork lists installable skills.

### ChatGPT (Skills)

1. Zip the same `naukri/` folder.
2. In ChatGPT, open **Skills** and upload the zip. OpenAI's upload flow and file-size limits change periodically — check the current "Skills in ChatGPT" help article on OpenAI's site if the upload doesn't behave as expected.
3. Start a chat and paste a job description or link.

### Claude Code

Copy the `naukri/` folder into `~/.claude/skills/`:

```
cp -r naukri ~/.claude/skills/naukri
```

## First run: onboarding

The first time you use the skill, it has no resume or evidence bank to work from. It will ask you, in one batch, for your master resume, your hard-gate facts (work authorization, location, clearance, required credentials, years of experience), and your target roles. From that it builds three files:

- `candidate-profile.md`
- `career-vault.md`
- `resume-variants.md`

Save these into your **Claude Project's project knowledge** (or your **ChatGPT project's files**) so future runs find them automatically without repeating onboarding. If you just want a one-off evaluation, tell the skill "one-off, use this resume" and it will skip building a vault.

## Example prompts

- *"Should I apply to this job? [paste description]"*
- *"[paste a job posting link] — evaluate this role"*
- *"Score this job against my resume"*
- *"Tailor my resume for this posting"*

## Privacy note

Your candidate profile, career vault, and resume variants are personal data. They live in **your own** Claude Project or ChatGPT project, not in this repository. If you fork or customize this skill, do not commit your own `candidate-profile.md`, `career-vault.md`, or `resume-variants.md` — the included `.gitignore` already excludes common local-data filenames, but double-check before pushing.

## Maintainer

Maintainer: [@satkalra](https://github.com/satkalra)
