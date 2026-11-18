#!/usr/bin/env python3
"""Docs checks for this repo. Run: python3 scripts/check_docs.py

1. Every relative link in a Markdown file points to a file that exists,
   and every #anchor points to a real heading.
2. Privacy guard: no personal email addresses, bitcoin addresses or
   Lightning invoices. Applications, contact details and payouts are
   private and must never be committed to this public repo.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLACEHOLDERS = {"link", "url", "#", ""}
ALLOWED_EMAILS = {"hello@codeorange.dev", "fellowship@codeorange.dev"}

LINK = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)|<a\s+href=\"([^\"]+)\"|<img\s+src=\"([^\"]+)\"|!\[[^\]]*\]\(([^)\s]+)\)")
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
BTC_ADDR = re.compile(r"\b(bc1[ac-hj-np-z02-9]{25,87}|tb1[ac-hj-np-z02-9]{25,87}|[13][a-km-zA-HJ-NP-Z1-9]{25,34})\b")
LN_INVOICE = re.compile(r"\bln(bc|tb|bcrt)[0-9]*[a-z0-9]{50,}\b", re.I)


def slugify(heading: str) -> str:
    h = re.sub(r"<[^>]+>", "", heading).strip().lower()
    h = re.sub(r"[`*_~\[\]()]", "", h)
    h = re.sub(r"[^\w\- ]", "", h)
    return h.replace(" ", "-")


def anchors(path: Path) -> set:
    seen, out = {}, set()
    in_code = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
        if in_code:
            continue
        m = re.match(r"^#{1,6}\s+(.*?)\s*#*\s*$", line)
        if m:
            s = slugify(m.group(1))
            n = seen.get(s, 0)
            out.add(s if n == 0 else f"{s}-{n}")
            seen[s] = n + 1
    return out


def main() -> int:
    errors = []
    md_files = sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)
    for f in md_files:
        rel = f.relative_to(ROOT)
        text = f.read_text(encoding="utf-8")
        for m in LINK.finditer(text):
            target = next(g for g in m.groups() if g is not None)
            if target in PLACEHOLDERS or target.startswith(("http://", "https://", "mailto:")):
                continue
            path_part, _, frag = target.partition("#")
            dest = f if not path_part else (f.parent / path_part).resolve()
            if not dest.exists():
                errors.append(f"{rel}: broken link -> {target}")
                continue
            if frag and dest.is_file() and dest.suffix == ".md" and frag not in anchors(dest):
                errors.append(f"{rel}: missing anchor -> {target}")
        for n, line in enumerate(text.splitlines(), 1):
            for e in EMAIL.findall(line):
                if e.lower() not in ALLOWED_EMAILS and not e.lower().endswith("@example.com"):
                    errors.append(f"{rel}:{n}: email address not allowed in public repo -> {e}")
            if BTC_ADDR.search(line) and "github.com" not in line:
                errors.append(f"{rel}:{n}: looks like a bitcoin address (payouts are private)")
            if LN_INVOICE.search(line):
                errors.append(f"{rel}:{n}: looks like a Lightning invoice (payouts are private)")
    for e in errors:
        print("ERROR", e)
    print(f"Checked {len(md_files)} Markdown files: {len(errors)} problem(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
