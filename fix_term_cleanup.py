#!/usr/bin/env python3
"""
Clean up duplicated CSS from previous term-popup fixes.
Remove old quiz-answer-inner .term-popup blocks and duplicate ::after/hover rules.
"""

import re
from pathlib import Path

BASE = Path("/home/yn4416/projects/python-reading-guide")
DIRS = [
    BASE / "01_basics" / "interactive",
    BASE / "02_python_syntax" / "interactive",
]

# Pattern: /* quiz answer term-popup — enhanced visibility */ ... up to next blank line or @media
# This block contains duplicated .quiz-answer-inner .term-popup, ::after, .term:hover rules
QUIZ_BLOCK = re.compile(
    r'\n\s*/\* quiz answer term-popup — enhanced visibility \*/'
    r'.*?'
    r'(?=\n\s*(@media|/\* ===))',
    re.DOTALL
)

count = 0
for d in DIRS:
    for f in sorted(d.glob("*.html")):
        src = f.read_text(encoding="utf-8")

        # Remove the old quiz-answer-inner block with all its duplicates
        new_src = QUIZ_BLOCK.sub('\n', src)

        if new_src != src:
            f.write_text(new_src, encoding="utf-8")
            count += 1
            print(f"  ✓ {f.name}")
        else:
            print(f"  - {f.name} (no change)")

print(f"\nDone: {count} files cleaned")
