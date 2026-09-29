# ATS Resume Guidelines (V2.1)

Status: Baseline specification for resume generation, job filtering, and evaluation used by this skill. Supersedes V1 and V2 drafts.

---

## The central finding

There is no universal "ATS test" or standardized ATS score.

Different systems behave differently:

* Greenhouse can perform exact-match searches across job titles, skills, locations, resume text, and recruiter notes.
* Workday describes extracting and normalizing skills using parsing and natural-language processing (semantic matching).
* Employers can configure knockout questions that automatically reject applicants based on work authorization, location, licensing, or other requirements.
* Some ATS products rank candidates; others primarily parse, store, search, and filter applications for recruiters.
* ATS platforms rarely auto-reject on resume content. The real failure modes are (a) mis-parsing, (b) being ranked/buried under volume, and (c) knockout-question failures. Recruiters typically search parsed fields and review only the top-ranked slice of applicants.

Therefore, this skill does not attempt to "beat the ATS." It produces resumes that:

1. Parse correctly.
2. Pass eligibility filters.
3. Contain the terminology recruiters may search for.
4. Demonstrate evidence for the job's requirements.
5. Persuade the recruiter in the first 6–10 seconds after the resume is opened.

---

# 1. Filter jobs before tailoring the resume

Resume optimization cannot compensate for failing a genuine hard requirement.

Before generating a resume, identify:

| Requirement type     | Examples                                                     | Treatment                               |
| --------------------- | ------------------------------------------------------------ | --------------------------------------- |
| Legal and logistical  | Work authorization, sponsorship, clearance, location, travel | Hard gate                               |
| Credential            | Degree, license, certification                               | Hard gate when explicitly mandatory     |
| Experience            | "5+ years," management experience, production experience     | Determine whether strict or approximate |
| Technical             | Excel, SQL, welding certification, CAD, salesforce           | Evidence-match requirement              |
| Domain                | Fintech, healthcare, hospitality, logistics, education        | Evaluate depth and transferability      |
| Responsibility        | Manage a P&L, lead a clinical team, run a production line     | Match against achievements              |
| Preferred             | Nice-to-have tools or industry exposure                      | Ranking signal, not automatic rejection |

### Rule

An application must be blocked when:

* A legal or logistical hard gate fails.
* A mandatory license or clearance is absent.
* The applicant would need to answer an application question dishonestly.
* The role is materially above the applicant's demonstrated level.
* The job's central function is absent from the applicant's background.

Never tailor a resume by inventing missing qualifications.

### Timing rule (new in V2.1)

Application timing materially affects outcomes at high volume. Prioritize postings less than 48–72 hours old; apply the same day where possible. For older postings, only apply when fit is Tier-A or a referral exists, and make the headline/summary ultra-relevant.

---

# 2. Use an ATS-safe document structure

Greenhouse specifically identifies graphics, photos, WordArt, scanned documents, tables, headers, footers, text boxes, columns, unclear sections, and incomplete job titles as possible causes of failed or partial parsing. Multi-column layouts are the single most damaging formatting error: parsers read across columns and interleave unrelated text, corrupting titles and bullets downstream.

## Required layout

Use:

* One column.
* Left-aligned text.
* Normal bullet points (standard round bullets from the word processor's list tool).
* Standard section headings.
* Consistent date formatting: "Month YYYY" (e.g., January 2024 – Present), identical on every entry. Mixed date formats within one resume break parsing worst of all. Every job entry must be dated.
* Reverse-chronological experience. Functional (undated) formats are penalized or misparsed; career changers use a hybrid (Skills section above reverse-chronological experience).
* Text-based documents rather than scanned images.
* Standard fonts: Arial, Calibri, Garamond, Georgia, Helvetica, Tahoma, Verdana, Times New Roman. Body 10–12 pt (never below 10 pt — some parsers skip tiny text as decorative), headings 14–16 pt.

Do not use:

* Tables, including invisible layout tables.
* Sidebars or two-column templates.
* Icons in place of words.
* Skill progress bars or star ratings.
* Charts, photos, logos, or decorative graphics.
* Text boxes.
* Contact information inside headers or footers (stored in a separate XML node many parsers never read).
* Unicode symbols as bullets (→, ✓, emoji) — these tokenize as garbage characters and can fragment or drop entire bullets.
* Important information represented only through hyperlinks.
* Manually spaced letters such as `J O R D A N`.
* White text, tiny text, or hidden keywords (see §13 — now actively detected as fraud).

## Standard section names

Preferred headings:

* Professional Summary
* Technical Skills or Skills
* Professional Experience
* Projects
* Education
* Certifications

Avoid creative headings such as "My Journey," "Where I've Made an Impact," or "My Toolbox." Standard headings make extraction and human scanning more reliable.

## Contact section

Place contact information directly in the document body:

`Name | City, State | Phone | Email | LinkedIn | Portfolio`

For US applications, a full street address is unnecessary. Use visible labels or recognizable URLs rather than icons alone.

---

# 3. File-format rules

Major ATS platforms accept both Word and text-based PDF, but extraction reliability differs. DOCX parses more consistently because the file format is XML with guaranteed text ordering; PDF extraction depends on the internal text-drawing order of the producing application.

### Policy

Generate both:

1. `First_Last_TargetRole_Resume.docx`
2. `First_Last_TargetRole_Resume.pdf`

Submission logic:

* Follow the employer's explicit instructions first.
* Use DOCX when no format is specified (safest across Taleo, Workday, iCIMS).
* Use PDF when requested, or on modern platforms (Greenhouse, Lever) when the application preview confirms correct extraction.
* Never submit a scanned PDF.
* Keep the file below 1 MB where practical.
* Never use filenames such as `resume_final_v7_revised.pdf`.

### Parseability test

Before release:

1. Extract all text from the generated file.
2. Verify text appears in the intended reading order.
3. Confirm that name, contact information, employers, titles, dates, skills, and education were extracted.
4. Check that no characters were corrupted.
5. Compare extracted text against the source resume.

A visually attractive resume that parses incorrectly must fail quality control. Note: this is parse *verification*, not a third-party "ATS score" (see doctrine §9).

### Platform-specific notes (new in V2.1)

When the platform is identifiable (careers-page URL usually reveals it):

* **Workday:** exact keyword/title matches weighted heavily; DOCX preferred; strict on date formats; has an AI screening layer.
* **Greenhouse:** friendliest parser; recruiters primarily view the rendered PDF, so visual clarity matters more here; semantic matching helps, exact phrasing still scores higher.
* **Lever:** full-text search driven; handles PDF well; human review happens earlier; dense, searchable skills lines help.
* **Taleo:** strictest literal keyword matching and weakest parser; DOCX strongly preferred; ASCII-safe formatting only.
* **iCIMS:** keyword-heavy; parsing varies by tier; DOCX safer; tables frequently break; ensure critical skills appear multiple times in context.

When the platform is unknown (default), follow the strictest common denominator: the rules in §2.

---

# 4. Build for both exact matching and semantic matching

Greenhouse's talent filtering requires exact keyword matches; Workday's skill extraction recognizes related concepts. The resume therefore needs three forms of alignment.

## Exact terminology

Where truthful, use the wording from the job description:

* `Customer relationship management`, not only `client tools`.
* `Search engine optimization`, not only `marketing`.
* `Amazon Web Services`, not only `cloud`.
* `Financial forecasting`, not only `analytics`.

Title alignment is one of the highest-leverage moves: align the headline with the posted job title's phrasing when honestly applicable (large-scale application analyses associate title matching with multi-fold higher interview rates). Never fabricate a title (see §9).

## Acronym expansion

Use the full term and acronym once each:

* Customer Relationship Management (CRM)
* Search Engine Optimization (SEO)
* Extract, Transform, Load (ETL)
* Continuous Integration and Continuous Delivery (CI/CD)
* Amazon Web Services (AWS)

## Semantic evidence

Keywords should appear in meaningful evidence, not merely in a skills list. Keywords in the context of a quantified achievement carry more scoring weight than the same keyword in a bare list.

Weak:

> Skills: Excel, SQL, Salesforce, Forecasting, Reporting

Stronger:

> Built a quarterly demand-forecasting model in SQL and Excel, feeding a Salesforce-integrated reporting dashboard used by the regional sales team.

## Skills-based screening (new in V2.1)

The dominant 2026 shift is skills-first filtering: a majority of enterprise hiring teams filter by specific required skills before reviewing job history, and skills declared in a dedicated Skills section typically carry more scoring weight than the same skill mentioned once in a bullet. The Skills section is mandatory, placed high (after the summary), and written in the posting's terminology — every genuinely-held required skill must appear there AND in evidence.

---

# 5. Extract keywords by importance, not raw frequency

Classify job-description language into five groups.

### A. Mandatory qualifications

Signal words: Required · Must have · Minimum · At least · Demonstrated · Proven experience · Essential

### B. Core responsibilities

Usually the first responsibilities listed or the duties repeated throughout the posting. Requirements listed first or repeated carry the most weight.

### C. Tools and technical skills

Languages, platforms, methodologies, frameworks, certifications, systems.

### D. Domain concepts

Examples: Payments · Risk · Fraud · Healthcare claims · Supply-chain forecasting · Advertising measurement · Patient intake · Retail merchandising

### E. Behavioral signals

Examples: Cross-functional · Ownership · Ambiguity · Stakeholder management · Mentoring · Executive communication

Soft skills are demonstrated through experience, not listed.

Weak:

> Leadership, communication, ownership, teamwork

Stronger:

> Led a five-person cross-departmental rollout of a new scheduling system, resolving conflicting stakeholder requirements and delivering on schedule.

---

# 6. Every important keyword needs evidence

Create an internal evidence matrix before rewriting.

| Job requirement                     | Candidate evidence                        | Strength | Resume location            |
| ------------------------------------ | ------------------------------------------ | -------: | --------------------------- |
| Own a regional sales pipeline        | Managed a multi-state territory quota      |   Strong | Current experience          |
| SQL                                  | Multiple production reporting queries      |   Strong | Skills and bullets          |
| AWS                                  | EC2, S3, RDS experience                    | Moderate | Skills and relevant bullet  |
| Kubernetes                           | No verified evidence                       |     None | Exclude                     |
| Healthcare compliance                | Compliance-adjacent project                | Moderate | Projects                    |
| Team leadership                      | Led a cross-functional launch team         |   Strong | Current experience          |

A skill may be inserted only when supported by: work history, a verified project, education or research, a certification, or a user-confirmed experience record.

No requirement is upgraded from "exposure" to "expertise."

---

# 7. Optimize the top third for the recruiter

ATS compatibility gets the resume retrieved. The opening section determines whether the recruiter continues past the 6–10 second first scan.

The top third answers:

1. What role is this person?
2. At what level?
3. What are their strongest relevant capabilities?
4. What evidence makes them credible?

## Recommended order for experienced candidates

1. Name and contact information.
2. Targeted professional headline or summary.
3. Skills (technical or functional, as relevant to the field).
4. Professional experience.
5. Projects (when relevant).
6. Education.

## Professional headline

Role-aligned but truthful:

> Operations Manager | Supply Chain, Vendor Management and Process Improvement

Do not falsely replace the applicant's current title with the advertised title.

## Professional summary

Optional. Include when it explains specialization, seniority, a career transition, or unusually broad experience. 2–4 lines: role, years, domains, 1–2 proof points. Must contain at least one keyword or achievement from the target posting, or remove it.

Recommended structure:

> Operations professional with 6+ years of experience managing multi-site logistics and vendor relationships. Delivered process improvements and reporting systems using SQL, Excel and Salesforce. Experienced in taking initiatives from pilot through company-wide rollout.

Avoid: "Results-driven professional," "Passionate problem solver," "Hard-working team player," objectives about what the applicant wants, or a summary that duplicates the skills section.

---

# 8. Experience bullets must demonstrate outcomes

## Bullet formula

**Action + object + method/context + scale + result**

Example:

> Redesigned the vendor onboarding process across three regional warehouses, cutting new-vendor setup time and standardizing compliance documentation.

Where verified metrics exist:

> Rebuilt the weekly reporting pipeline in SQL and Excel, reducing manual reconciliation work by approximately 20%.

## Quantification target (new in V2.1)

Target: at least ~70% of experience bullets contain a measurable element (%, $, time, scale, count). Modern ATS scoring and human reviewers both distinguish achievement-oriented from duty-listing resumes. This is a target, not a license to invent numbers — see below.

## Acceptable forms of measurement

Accuracy · Latency · Throughput · Cost · Reliability · Users, teams, services, clients, documents, or accounts · Time saved · Error reduction · Release or launch frequency · Adoption · Project scope · Team size · System or program scale

When no outcome metric exists, state the business or operational consequence without fabricating a number.

Good:

> Introduced a standardized intake checklist for new clients, reducing missing-document follow-ups and simplifying onboarding.

Not acceptable:

> Improved efficiency by 40%.

unless the candidate has evidence for the 40%.

## Bullet allocation

* Current role: 4–6 bullets.
* Previous relevant role: 3–5 bullets.
* Older or less relevant role: 1–3 bullets.
* Each bullet: preferably one line, maximum two.
* Most relevant accomplishment first.
* Remove bullets that merely restate generic job duties.

---

# 9. Preserve official titles while improving discoverability

Use the official title, with an honest clarifier where useful:

> Operations Manager
> Marketing Coordinator
> Software Engineer — Platform Team

Do not change `Data Analyst` into `Senior Machine Learning Engineer`.

A clarifier may be added only when it describes the actual work:

> Operations Manager (Supply Chain and Vendor Relations)

Standardize abbreviations where space permits: Senior not Sr. · Vice President not VP · Software Engineer not SWE in the title field · Machine Learning not only ML. Keep title formatting consistent across all entries — AI-era parsers penalize inconsistency.

---

# 10. Skills-section rules

The skills section improves retrieval; it is not a keyword warehouse.

Recommended format (adapt categories to the candidate's field):

> **Core Tools:** Excel, SQL, Salesforce, Tableau
> **Operations:** Vendor management, inventory planning, process improvement
> **Systems and Platforms:** SAP, NetSuite, Workday
> **Languages/Technical (if applicable):** Python, SQL, TypeScript

Rules:

* Order categories by job importance; order skills within category by relevance.
* Use only verified skills; do not list every tool ever encountered.
* Remove obsolete or irrelevant tools when space is limited.
* No proficiency bars, no soft skills.
* Every central skill listed here must also appear in experience or projects (a recruiter should be able to find the skill, then find evidence of its use).

---

# 11. Projects should close evidence gaps

Projects are valuable when they demonstrate a requirement not sufficiently visible in employment. This applies beyond software (e.g., a volunteer-led fundraising campaign, a community program redesign, a personal portfolio piece).

Each selected project contains: problem or objective · approach · relevant tools · scale, evaluation, adoption, or result · link only when the linked work is presentable and accessible.

Exclude projects that: duplicate stronger professional experience · use irrelevant tools · were simple tutorials or coursework · cannot be explained in an interview · make unsupported outcome claims.

For experienced applicants, projects should not consume more space than professional experience unless unusually relevant.

---

# 12. Resume length is contextual

* Under ~3 years of relevant experience: prefer one page.
* 3–8 years with substantial relevant work: one or two pages.
* Use two pages only when page two contains strong, job-relevant evidence. ATS platforms do not penalize length; cramming does more harm than a clean second page.
* Never shrink text excessively to force one page; never pad to reach two.

Formatting targets: 10–12 pt readable font · at least 0.5-inch margins · consistent spacing and typography · moderate bold · no walls of text.

---

# 13. Keyword-stuffing and ATS hacks are prohibited

Reject:

* Copying the complete job description into the resume.
* Repeating the same skill unnaturally.
* White text, tiny invisible text, keywords in document metadata. (Not merely ineffective — Workday, Greenhouse, and Lever now detect zero-opacity/white-on-white text; flagged applications can be auto-rejected with a fraud indicator attached to the candidate record, and the parser renders hidden text visibly to recruiters anyway.)
* Listing tools or technologies the candidate has not used.
* Artificially changing dates or seniority.
* Inflated metrics.
* Fabricated clients, employers, projects, or certifications.

Every generated statement must pass this test:

> Could the applicant explain and defend this statement during an interview?

---

# 14. Application-form consistency matters

The ATS profile is created from both the resume and manually entered fields. Verify consistency across: resume · application form · LinkedIn · portfolio · work-authorization answer · employment dates · degree names · job titles · location · years of experience.

A well-tailored resume can still fail if the application form contains conflicting or disqualifying answers. Never advise answering "No sponsorship required" when sponsorship will be required. Knockout questions are the one part of the pipeline with a real delete button — answer them accurately and deliberately.

---

# 15. Tailoring pipeline

## Stage 1 — Job normalization

Extract: job title · level · function · location · work arrangement · compensation when available · sponsorship language · required qualifications · preferred qualifications · responsibilities · technical skills · domain language · date posted · ATS platform (from careers-page URL, if identifiable).

## Stage 2 — Hard-gate evaluation

Return one of: Eligible · Eligible with uncertainty · Ineligible · Needs user confirmation. Ineligible jobs are filtered out before resume generation.

## Stage 3 — Evidence retrieval

Retrieve from the candidate's career vault: master resume · previous resumes · project records · achievement inventory · user-confirmed metrics · skills and certifications. Every proposed bullet carries provenance.

## Stage 4 — Requirement-to-evidence mapping

Label evidence for every major requirement: Direct · Adjacent · Weak · Missing.

## Stage 5 — Content selection

Select experiences that best prove: core role fit · required technical skills · required level · domain relevance · demonstrated impact.

## Stage 6 — Controlled rewriting

May: reorder bullets · shorten bullets · replace vague language with precise language · use the employer's terminology where equivalent · surface previously omitted verified experience · emphasize relevant outcomes.

May not: invent experience · change facts · create unsupported numbers · upgrade proficiency · hide major eligibility problems.

## Stage 7 — ATS linting

Check: single-column structure · standard headings · no tables or text boxes · correct extraction order · required terms present where supported · acronyms expanded · contact information in body · consistent "Month YYYY" dates · standard bullets only · headline/summary contains target-role keywords · both DOCX and PDF generated · ≥70% quantified bullets (or documented reason).

## Stage 8 — Human-review simulation

A simulated recruiter answers: Is the target role obvious? Are must-have qualifications visible in the top third? Does recent experience support the requested level? Are achievements more prominent than duties? Is anything confusing, generic, or implausible? Would the recruiter know why this applicant fits this specific job?

## Stage 9 — Factuality audit

Compare every generated claim against its source evidence. Unsupported claims are removed or sent for user confirmation.

## Stage 10 — Submission logistics (new in V2.1)

Confirm knockout-question answers · confirm file format per §3 · apply within the timing window per §1 · log the application per §19.

---

# 16. Internal scoring model

This is a **Job–Resume Evidence Score**, not an "ATS score."

| Component                     |  Weight |
| ------------------------------ | ------: |
| Required-skill evidence        |      25 |
| Core-responsibility evidence   |      25 |
| Seniority and scope alignment  |      15 |
| Domain relevance               |      10 |
| Demonstrated outcomes          |      10 |
| ATS parseability               |      10 |
| Human readability and clarity  |       5 |
| **Total**                      | **100** |

Hard gates remain outside the numeric score.

### Decision thresholds (heuristics, not industry standards)

* **85–100:** Strong application; apply.
* **78–84:** Reasonable application; apply when strategically valuable.
* **68–77:** Apply mainly with a referral, strong adjacent experience, or compelling reason.
* **Below 68:** Usually skip.
* **Any hard-gate failure:** Block.

A resume does not receive points merely because a keyword appears. Points require supporting evidence.

---

# 17. Why a 90% callback target is not realistic

A 90% callback rate cannot be achieved through resume tailoring.

Market baseline (as reported in industry hiring-platform analyses, e.g. Ashby's aggregate applicant data, circa 2026 — treat as directional, not a verified statistic): interview rates appear to have fallen from roughly 7–8% in 2021 to somewhere around 3.6–4.7% depending on role type, plausibly driven by rising application volume (reportedly 290+ applications per hire in some analyses) and more AI-generated applications. Referred and internal candidates progress at substantially higher rates than inbound applicants, which is why channel matters more than any resume edit. Referred and internal candidates progress at substantially higher rates than inbound applicants, which is why channel matters more than any resume edit.

Even a perfect resume cannot control: internal candidates · previously sourced candidates · referrals · hiring freezes · position cancellations · late applications · recruiter workload · compensation mismatch · immigration constraints · hiring-manager preferences · candidates with more direct domain experience.

A 90% callback rate would only be plausible in a highly artificial pool consisting mostly of recruiter-invited applications or roles created for the candidate.

---

# 18. Objectives

Controllable quality goals:

| Metric                                     | Initial target |
| -------------------------------------------- | -------------: |
| Successful text extraction                   |           100% |
| Applications passing all hard gates          |           100% |
| Factual claims with provenance               |           100% |
| Top job requirements supported by evidence   |         85–90% |
| Applications scoring at least 78             |           90%+ |
| Applications submitted within 72h of post    |           70%+ |
| Tier-A cold-application callback rate        |         20–30% |
| Same-function referral callback rate         |         35–45% |
| Unsupported or fabricated claims             |             0% |

Calibration note: the market-wide application-to-interview rate is currently 3.6–4.7%. The Tier-A cold target of 20–30% therefore represents roughly 5x market average and is achievable only through strict fit filtering (§1, §16), tailoring (§15), and timing — it is a stretch operating goal, not a benchmark. Recalibrate after the first 30 comparable applications.

Top-level objective:

> **Maximize verified interview probability per application while minimizing low-fit applications and factual distortion.**

---

# 19. Measurement and learning loop

Track every submitted application with: company · job title · job URL or requisition ID · date posted · date applied · application channel · referral status · eligibility status · evidence score · resume version · ATS platform (if known) · major requirements covered · missing requirements · response · recruiter screen · interview · rejection stage · rejection reason when known.

Calculate callback rates separately for: cold inbound · referrals · recruiter outreach · job families · fit tiers · recently posted vs. older jobs · one-page vs. two-page resumes · headline/summary strategies.

Never combine channels into one callback number; referrals and cold applications have materially different expected outcomes.

Review rules:

* Use a rolling sample of at least 30 comparable applications before major conclusions.
* Change one important strategy at a time.
* If Tier-A cold callback rate is under ~10% after 30 applications, the likely problem is role-fit or seniority mismatch, not formatting — tighten §16 thresholds before changing resume style.

---

## Final doctrine

1. **Filter before tailoring.**
2. **Eligibility beats keyword optimization.**
3. **Evidence beats keyword frequency.**
4. **Exact terminology and semantic context both matter.**
5. **Every claim must be traceable to verified experience.**
6. **ATS parseability is mandatory but not sufficient.**
7. **The resume must be optimized for a human after retrieval.**
8. **Referrals and timing are part of the application strategy.**
9. **Never optimize for a fake universal ATS score — verify parsing, ignore vendor scores.**
10. **Measure actual callbacks and interviews by fit tier and application source.**

This is the baseline specification for resume generation and evaluation used by this skill.
