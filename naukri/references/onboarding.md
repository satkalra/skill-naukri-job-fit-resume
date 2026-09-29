# Onboarding — building the candidate's vault

Run this once, the first time a user invokes the skill and no candidate-profile / career-vault / resume-variants can be found in the conversation, uploaded files, or connected project/workspace knowledge.

## When to run it

Check first (Step 0 of SKILL.md) whether the three vault files already exist somewhere reachable (pasted in, uploaded, or present in project/workspace files with recognizable names like `candidate-profile`, `career-vault`, `resume-variants`). If they exist, load them and skip onboarding. If the user says "just do a one-off with this resume I'm pasting," skip onboarding for that single run and don't build the vault — but mention that a vault would make future runs faster.

## What to ask for (one compact batch, not a slow interview)

Ask in a single message, so the user can answer everything at once:

1. **Master resume** — paste text or attach the file (most recent, most complete version).
2. **Hard-gate facts:**
   - Work authorization status and any sponsorship needs.
   - Current location and relocation willingness (which cities/regions, if any).
   - Security clearance, if any.
   - Required licenses/certifications actually held (with names, not just "yes").
   - Total years of relevant experience, and current level (e.g., IC3, Senior, Manager).
3. **Target roles** — 2–4 kinds of roles being pursued (e.g., "backend engineer roles," "operations manager roles," "customer-facing solutions roles"), since this drives the resume-variants routing rules.
4. **Any additional evidence** not in the master resume that should be searchable later: side projects, volunteer work, publications, talks, notable metrics the resume doesn't mention yet.

Do not ask more than this up front — anything else (individual bullet metrics, extra context) can be gathered later, per-application, when a specific requirement needs evidence the vault doesn't have.

## Building the three files

### candidate-profile.md

Fill in the `templates/candidate-profile.md` template using the hard-gate answers above. Leave anything unknown as `TBD` rather than guessing. This file is read on every run to answer hard gates and knockout questions.

### career-vault.md

Break the master resume (and any extra evidence supplied) into individual bullets/achievements. For each one, fill in the `templates/career-vault.md` row format:

- The bullet text (as strong as the source material supports — don't invent metrics not present in the source).
- Where it came from (employer/role/project — the provenance).
- Whether it has a *verified* metric (a number the user actually supplied) or not.
- Tags for skills/domains it provides evidence for, so future evidence-matrix steps can retrieve it.

This file is the single source of truth for Stage 3 (evidence retrieval) — never invent a bullet that isn't traceable to this file or to something the user confirms in-conversation.

### resume-variants.md

Ask which 2–4 "shapes" of role the user is targeting (already gathered above) and propose a base variant per shape, using `templates/resume-variants.md`. Default routing heuristic when it's unclear which variant fits a given job description:

- **Customer-facing / delivery-facing responsibilities listed first** → the variant emphasizing communication, delivery, and cross-team work.
- **System-building / platform / infrastructure responsibilities listed first** → the variant emphasizing technical depth and engineering ownership.
- **Domain-or-data-as-the-product responsibilities listed first** (the job is about producing insights, analytics, or domain-specific outputs) → the variant emphasizing domain and analytical work.

Adjust the exact variant names/count to whatever roles the user is actually targeting — 2 to 4 variants is typical; don't force a 3-way split if the user only targets one kind of role.

## Handing it back

Once all three files are drafted, output them in full (as text the user can save, or as files if the environment supports file output) and say plainly:

> Save these three files — `candidate-profile.md`, `career-vault.md`, `resume-variants.md` — to your assistant's persistent project or workspace storage (a Claude Project's project knowledge, a ChatGPT project's files, or a local folder it can re-read) so future runs of this skill can find them automatically without re-onboarding.

Then continue with the job the user originally pasted, if any, using the newly built vault.

## Updating the vault later

When a user provides a new metric, a new project, or corrects an existing entry, offer to update `career-vault.md` (or `candidate-profile.md` for gate facts) and hand back the updated file the same way — don't silently accumulate changes only in conversation memory.
