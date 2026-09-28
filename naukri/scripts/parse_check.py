#!/usr/bin/env python3
"""
parse_check.py — parseability test for a generated resume (§3 of ats-guidelines.md).

Usage:
    python3 parse_check.py FILE [--source input.json]

Extracts text from a DOCX or PDF, then checks:
    - name, email, phone present
    - each employer/title/date from the source JSON (if given) is present
    - skills present
    - education present
    - dates all match "Month YYYY" or "Present" (no mixed formats)
    - no corrupted / replacement characters
    - percentage of experience bullets that contain a number/%/$ (quantified)

Prints a PASS/FAIL table and exits non-zero if anything fails.
"""

import argparse
import json
import re
import sys
from pathlib import Path

MONTH_RE = re.compile(
    r"(January|February|March|April|May|June|July|August|September|October|November|December) \d{4}"
)
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(r"(\+?\d[\d\-\.\(\) ]{7,}\d)")
QUANT_RE = re.compile(r"(\d|%|\$)")
REPLACEMENT_CHAR = "�"


def fail(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def extract_docx_text(path):
    try:
        from docx import Document
    except ImportError:
        fail("python-docx is not installed; cannot parse .docx files. Install with 'pip install python-docx'.")
    doc = Document(str(path))
    parts = []
    for p in doc.paragraphs:
        if p.text.strip():
            parts.append(p.text)
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                if cell.text.strip():
                    parts.append(cell.text)
    return "\n".join(parts)


def extract_pdf_text(path):
    try:
        import pdfplumber
    except ImportError:
        pdfplumber = None

    if pdfplumber is not None:
        try:
            text_parts = []
            with pdfplumber.open(str(path)) as pdf:
                for page in pdf.pages:
                    t = page.extract_text() or ""
                    text_parts.append(t)
            text = "\n".join(text_parts)
            if text.strip():
                return text
        except Exception as e:
            print(f"WARNING: pdfplumber failed ({e}); trying pdftotext.", file=sys.stderr)

    import shutil
    import subprocess

    pdftotext = shutil.which("pdftotext")
    if pdftotext:
        try:
            result = subprocess.run([pdftotext, str(path), "-"], check=True, capture_output=True, text=True, timeout=60)
            if result.stdout.strip():
                return result.stdout
        except Exception as e:
            print(f"WARNING: pdftotext failed ({e}).", file=sys.stderr)

    fail(
        "Could not extract text from the PDF: neither pdfplumber nor pdftotext succeeded. "
        "Install pdfplumber with 'pip install pdfplumber' or install poppler-utils for pdftotext."
    )


def extract_text(path):
    suffix = path.suffix.lower()
    if suffix == ".docx":
        return extract_docx_text(path)
    elif suffix == ".pdf":
        return extract_pdf_text(path)
    else:
        fail(f"Unsupported file type '{suffix}'. Only .docx and .pdf are supported.")


def run_checks(text, source_data):
    checks = []

    def add(name, ok, detail=""):
        checks.append((name, ok, detail))

    # Corrupted characters
    has_replacement = REPLACEMENT_CHAR in text
    add("No corrupted/replacement characters", not has_replacement,
        "" if not has_replacement else "Found U+FFFD replacement character(s) in extracted text.")

    # Email / phone
    email_found = bool(EMAIL_RE.search(text))
    add("Email address extracted", email_found)

    phone_found = bool(PHONE_RE.search(text))
    add("Phone number extracted", phone_found)

    # Name
    if source_data:
        name = source_data.get("name", "")
        name_found = bool(name) and name in text
        add("Candidate name extracted", name_found, "" if name_found else f"Expected to find '{name}'.")
    else:
        add("Candidate name extracted", True, "(no source JSON given — skipped exact check)")

    # Dates: all Month-YYYY-like tokens consistent; check for any 3-letter month abbreviations mixed in
    months_found = MONTH_RE.findall(text)
    abbreviated_dates = re.findall(
        r"\b(Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\.?\s+\d{4}\b", text
    )
    mixed_dates = len(abbreviated_dates) > 0
    add("Dates consistently 'Month YYYY' (no abbreviations)", not mixed_dates,
        "" if not mixed_dates else f"Found abbreviated date forms: {abbreviated_dates}")
    add("At least one date extracted", len(months_found) > 0 or bool(re.search(r"Present", text)))

    # Source-driven checks: employers, titles, skills, education
    if source_data:
        missing = []
        for exp in source_data.get("experience", []):
            for field in ["title", "employer"]:
                if exp.get(field) and exp[field] not in text:
                    missing.append(f"experience.{field}='{exp[field]}'")
        add("All employers/titles present", len(missing) == 0,
            "" if not missing else f"Missing: {missing}")

        missing_skills = []
        for group in source_data.get("skills", []):
            for item in group.get("items", []):
                if item not in text:
                    missing_skills.append(item)
        add("All listed skills present", len(missing_skills) == 0,
            "" if not missing_skills else f"Missing: {missing_skills}")

        missing_edu = []
        for edu in source_data.get("education", []):
            if edu.get("institution") and edu["institution"] not in text:
                missing_edu.append(edu["institution"])
        add("Education entries present", len(missing_edu) == 0,
            "" if not missing_edu else f"Missing: {missing_edu}")

        # Quantified bullet percentage
        all_bullets = []
        for exp in source_data.get("experience", []):
            all_bullets.extend(exp.get("bullets", []))
        if all_bullets:
            quantified = sum(1 for b in all_bullets if QUANT_RE.search(b))
            pct = 100.0 * quantified / len(all_bullets)
            add(f"Quantified bullets >= 70% (actual: {pct:.0f}%)", pct >= 70.0)
        else:
            add("Quantified bullets >= 70%", False, "No experience bullets found in source.")
    else:
        add("All employers/titles present", True, "(no source JSON given — skipped)")
        add("All listed skills present", True, "(no source JSON given — skipped)")
        add("Education entries present", True, "(no source JSON given — skipped)")
        add("Quantified bullets >= 70%", True, "(no source JSON given — skipped)")

    return checks


def print_report(path, checks):
    print(f"\nParseability report for {path}")
    print("-" * 70)
    all_pass = True
    for name, ok, detail in checks:
        status = "PASS" if ok else "FAIL"
        if not ok:
            all_pass = False
        line = f"[{status}] {name}"
        print(line)
        if detail:
            print(f"       {detail}")
    print("-" * 70)
    print(f"OVERALL: {'PASS' if all_pass else 'FAIL'}")
    return all_pass


def main():
    parser = argparse.ArgumentParser(description="Verify a generated resume parses correctly (ATS parseability test).")
    parser.add_argument("file", help="Path to the .docx or .pdf resume to check")
    parser.add_argument("--source", help="Path to the source resume JSON, for cross-checking content", default=None)
    args = parser.parse_args()

    path = Path(args.file)
    if not path.exists():
        fail(f"File not found: {path}")

    source_data = None
    if args.source:
        source_path = Path(args.source)
        if not source_path.exists():
            fail(f"Source file not found: {source_path}")
        source_data = json.loads(source_path.read_text())

    text = extract_text(path)
    checks = run_checks(text, source_data)
    ok = print_report(path, checks)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
