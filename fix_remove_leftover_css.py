#!/usr/bin/env python3
"""
Remove leftover CSS rules that show .term-popup on hover/focus,
causing double tooltip display (CSS + JS body-level).
Also fix body.light theme for #term-tooltip.
"""

import re
from pathlib import Path

BASE = Path("/home/yn4416/projects/python-reading-guide")
DIRS = [
    BASE / "01_basics" / "interactive",
    BASE / "02_python_syntax" / "interactive",
]

# Pattern 1: body.light .term-popup { ... } block (old tooltip CSS in light theme)
OLD_LIGHT_TERMPOPUP = re.compile(
    r'\s*body\.light \.term-popup \{[^}]*\}',
    re.DOTALL
)

# Pattern 2: .term-popup::after { ... } (standalone, not inside #term-tooltip)
OLD_TERMPOPUP_AFTER = re.compile(
    r'\s*\.term-popup::after \{[^}]*\}'
)

# Pattern 3: .term:hover .term-popup, .term:focus .term-popup, .term.show-popup .term-popup { display: block; }
OLD_HOVER_SHOW = re.compile(
    r'\s*\.term:hover \.term-popup,\s*\.term:focus \.term-popup,\s*\.term\.show-popup \.term-popup \{[^}]*\}'
)

# Add light theme support for #term-tooltip (after the body.light block)
LIGHT_TOOLTIP_ADDITION = """
body.light #term-tooltip {
  background: #fff;
  border-color: var(--accent);
  box-shadow: 0 8px 24px rgba(0,0,0,0.15), 0 0 0 1px rgba(124,58,237,0.2);
}
"""

count = 0
for d in DIRS:
    for f in sorted(d.glob("*.html")):
        src = f.read_text(encoding="utf-8")
        original = src

        # Remove old body.light .term-popup block
        src = OLD_LIGHT_TERMPOPUP.sub('', src)

        # Remove standalone .term-popup::after
        src = OLD_TERMPOPUP_AFTER.sub('', src)

        # Remove old hover/show rule
        src = OLD_HOVER_SHOW.sub('', src)

        # Add light theme for #term-tooltip (if not already present)
        if "body.light #term-tooltip" not in src and "body.light {" in src:
            src = src.replace(
                "body.light {",
                LIGHT_TOOLTIP_ADDITION + "\nbody.light {",
                1
            )

        # Clean up multiple blank lines
        src = re.sub(r'\n{3,}', '\n\n', src)

        if src != original:
            f.write_text(src, encoding="utf-8")
            count += 1
            print(f"  ✓ {f.name}")
        else:
            print(f"  - {f.name} (no change)")

print(f"\nDone: {count} files cleaned")
