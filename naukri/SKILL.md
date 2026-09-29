---
name: naukri
description: Evaluate a job posting against the user's resume and decide whether to apply, then tailor an ATS-safe resume if so. Trigger on a pasted job description or job posting link, or requests like "should I apply to this job", "evaluate this role", "score this job against my resume", or "tailor my resume for this posting". Produces a hard-gate check, an evidence-to-requirement matrix, a 100-point Job-Resume Evidence Score, an APPLY / APPLY WITH REFERRAL ONLY / SKIP verdict, and — if APPLY — a tailored DOCX and PDF resume plus a one-line tracker record.
---

# Naukri: job evaluation and resume tailoring

This skill turns a job posting into a clear apply/skip decision, and — when the decision is to apply — a tailored, ATS-safe resume. The full methodology lives in `references/ats-guidelines.md` (read it once per session, or whenever a step below points at a specific section). Read `references/scoring-rubric.md` before computing a score, `references/output-templates.md` before writing up results, and `references/onboarding.md` the first time a user has no vault yet.

**The one rule that overrides everything else: never fabricate.** Never invent skills, titles, dates, employers, metrics, or projects. Every claim on a generated resume must be traceable to the user's own material or something they explicitly confirmed in conversation. If evidence for a requirement doesn't exist, say so — don't paper over it.

## Step 0 — Load the candidate's vault

Look for `candidate-profile.md`, `career-vault.md`, and `resume-variants.md` — in the conversation, in uploaded files, or in connected project/workspace files. If found, load them.

If not found: this is a first run. Load `references/onboarding.md` and follow it — ask for the master resume and hard-gate facts in one compact batch, build the three files from `templates/`, hand them back to the user, and tell them to save the files into whatever persistent project/workspace storage this environment offers (e.g. a Claude Project's project knowledge, a ChatGPT project's files, or a local folder) so future runs find them automatically.

Exception: if the user says this is a one-off and pastes a resume to use just for this job, skip onboarding and proceed with that resume for this run only — but mention that building a vault would make future runs faster and skip fewer steps.

## Step 1 — Ingest the job posting

If the user gave a link, fetch it if you're able to (via a web-fetch/browsing tool available in this environment); if you can't fetch it, ask the user to paste the full posting text instead. Never guess at a posting's content.

Extract (per Stage 1, §15): job title, level, function, location, work arrangement, compensation if listed, sponsorship language, required qualifications, preferred qualifications, responsibilities, technical skills, domain language, date posted, and the ATS platform if identifiable from the URL (careers pages often reveal Greenhouse/Workday/Lever/Taleo/iCIMS in the domain or path — see §3 platform notes).

Report this using the "Job normalization summary" template in `references/output-templates.md`.

## Step 2 — Hard gates

Per §1, check every hard gate (work authorization, sponsorship, location/relocation, clearance, required license/degree, minimum experience, whether the job's central function exists in the candidate's background) against `candidate-profile.md` and the career vault.

- Any gate **fails** → stop. Report **DO NOT APPLY**, name the failed gate, and do not proceed to scoring or tailoring.
- Any gate is **uncertain** (e.g., ambiguous sponsorship language) → ask the user that specific question before continuing. Don't guess.
- All gates **pass** → continue to Step 3.

Use the "Hard-gate check" template.

## Step 3 — Evidence mapping

Per §6 and Stage 4, build the requirement-to-evidence matrix from the career vault. For every major requirement, label the evidence Direct / Adjacent / Weak / Missing, and note where it would live on the resume. Never invent evidence — a requirement with nothing in the vault is Missing, even if it seems like something the candidate probably knows.

Use the "Evidence matrix" template.

## Step 4 — Score

Per §16 and `references/scoring-rubric.md`, compute the Job–Resume Evidence Score across the 7 weighted components (required-skill evidence 25, core-responsibility evidence 25, seniority/scope 15, domain relevance 10, demonstrated outcomes 10, ATS parseability 10, readability 5). Show the full breakdown, not just the total — it tells the user what to fix.

Also flag timing per §1: how old is the posting, and is it inside or outside the 72-hour window?

Use the "Score breakdown" template.

## Step 5 — Verdict

Apply the §16 thresholds:

- **85–100** → APPLY
- **78–84** → APPLY if strategically valuable
- **68–77** → APPLY WITH REFERRAL ONLY (or other compelling reason)
- **<68** → SKIP
- **Any hard-gate failure** → already stopped in Step 2, regardless of score

State the verdict, the top 3 reasons, and the biggest evidence gaps. Use the "Verdict" template.

## Step 6 — If APPLY: tailor the resume

1. **Pick the base variant.** Use the routing rule in `resume-variants.md`: match the job's first-listed responsibilities against the user's own variant descriptions (typically customer-facing/delivery vs. system-building/platform vs. domain-or-data-as-product — but use whatever variants the user's own file defines). Say which variant was picked and why.
2. **Tailor per Stages 5–9 (§15):** select the experiences that best prove fit; reorder/shorten/sharpen bullets using the posting's terminology where truthfully equivalent; never invent experience, numbers, or upgraded proficiency.
3. **Follow formatting rules (§2–§3):** single column, standard section headings, Month YYYY dates throughout, contact info in the document body (not header/footer), standard round bullets, standard fonts, no tables/text boxes/graphics.
4. **Headline/summary:** align to the posted title honestly (§7, §9) — never fabricate a title the candidate doesn't hold.
5. **Skills section:** posting's terminology, verified skills only, every listed skill must also appear in evidence elsewhere (§10).
6. **Quantification:** target ≥70% of bullets with a verified metric (§8). Flag any bullet where a metric would help so the user can confirm or supply one — never invent the number.
7. **Factuality audit (Stage 9):** list every claim that needs the user's confirmation before finalizing, using the "Factuality audit" template.
8. **Generate the files.** Use `scripts/build_resume.py` to produce `First_Last_TargetRole_Resume.docx` and, with `--pdf`, the matching PDF (see Scripts below). If the scripts can't run in this environment, fall back to outputting the resume as ATS-safe plain text (§2 structure) plus a formatting checklist the user can apply in their own word processor.
9. **Run the parseability test.** Use `scripts/parse_check.py` on the generated file(s) and report PASS/FAIL per §3. A FAIL must be fixed before handing the resume back.
10. **Knockout-question reminder (§14).** Remind the user to double-check application-form answers against the resume, using the "Knockout-question reminder" template.

## Step 7 — Log the application

Output the one-line tracker record (§19) using the "Tracker line" template: company, title, job URL/req ID, date posted, date applied, channel, referral Y/N, evidence score, resume version, ATS platform. The user pastes this into their own tracker.

## Callback expectations (§17–18)

If the user asks about callback rates or wants to "optimize more," remind them: market baseline is ~3.6–4.7% interview rate; a realistic Tier-A cold-outreach target is 20–30%, referral 35–45%. Never suggest tactics aimed at a 90%+ callback rate — that isn't achievable through resume tailoring and chasing it degrades application quality (§17).

## Scripts

- `scripts/build_resume.py input.json --out-dir DIR [--pdf]` — turns a resume JSON (schema: `scripts/resume_schema.json`) into an ATS-safe DOCX, and optionally a PDF (via LibreOffice if available, otherwise a reportlab fallback with the same structure).
- `scripts/parse_check.py FILE [--source input.json]` — extracts text from the generated DOCX/PDF and verifies reading order, required fields, date-format consistency, absence of corrupted characters, and the percentage of quantified bullets. Prints a PASS/FAIL table and exits non-zero on FAIL.

If a script errors because a dependency is missing, report the missing dependency plainly and fall back to the plain-text ATS-safe output described in Step 6.9.

## No-code fallback

If code execution isn't available at all in this environment, skip straight to producing the tailored resume as structured plain text following §2's layout rules, plus a checklist the user can use to format it manually in Word/Google Docs.
