# Changelog

## 1.0.0 — 2026-09-29

Initial release.

- Job ingestion, hard-gate check, evidence matrix, 100-point Job–Resume Evidence Score, and APPLY/APPLY WITH REFERRAL ONLY/SKIP verdict.
- Resume tailoring pipeline (`scripts/build_resume.py`) producing ATS-safe DOCX + PDF, and a parseability checker (`scripts/parse_check.py`).
- First-run onboarding flow that builds a candidate profile, career vault, and resume-variant routing from the user's own material.
- Packaged as both a standalone Agent Skill (`naukri/`, for Claude.ai / Cowork / ChatGPT / manual Claude Code install) and a Claude Code plugin + marketplace (`.claude-plugin/`).
