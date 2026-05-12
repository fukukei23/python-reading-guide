#!/usr/bin/env python3
"""
Fix term-popup: revert from always-visible inline to hover/click tooltip.
- Changes .term-popup from display:inline to display:none + position:absolute
- Adds hover and click (mobile) show behavior via CSS
- Adds JS click handler for mobile toggle
- Keeps quiz-answer-inner enhanced styling
"""

import re
from pathlib import Path

BASE = Path("/home/yn4416/projects/python-reading-guide")
DIRS = [
    BASE / "01_basics" / "interactive",
    BASE / "02_python_syntax" / "interactive",
]

# === CSS replacement ===
OLD_TERM_POPUP_BLOCK = re.compile(
    r'\.term-popup \{[^}]*\}'
    r'(?:\s*/\* popup arrow removed[^\n]*\*/)?'
    r'(?:\s*/\* term-popup is now always visible[^\n]*\*/)?',
    re.DOTALL
)

NEW_TERM_POPUP_CSS = """.term-popup {
  display: none;
  position: absolute;
  bottom: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%);
  background: var(--bg-raised);
  border: 1px solid var(--accent);
  border-radius: 8px;
  padding: 8px 14px;
  font-size: 13px;
  color: var(--fg);
  line-height: 1.6;
  white-space: nowrap;
  z-index: 100;
  box-shadow: 0 8px 24px rgba(0,0,0,0.4), 0 0 0 1px rgba(124,58,237,0.3);
  pointer-events: none;
}
.term-popup::after {
  content: '';
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  border: 6px solid transparent;
  border-top-color: var(--accent);
}
.term:hover .term-popup,
.term:focus .term-popup,
.term.show-popup .term-popup {
  display: block;
}"""

# Mobile override — force wider tooltip on small screens
OLD_MOBILE_COMMENT = re.compile(r'\s*/\* mobile term-popup override removed \*/')
NEW_MOBILE_OVERRIDE = """
  .term-popup { white-space: normal; min-width: 200px; max-width: 280px; font-size: 12px; }"""

# === JS injection ===
TERM_JS = """
// term popup click toggle (mobile support)
document.querySelectorAll('.term').forEach(function(t){
  t.setAttribute('tabindex','0');
  t.setAttribute('role','button');
  t.addEventListener('click', function(e){
    e.stopPropagation();
    document.querySelectorAll('.term.show-popup').forEach(function(o){ if(o!==t) o.classList.remove('show-popup'); });
    t.classList.toggle('show-popup');
  });
});
document.addEventListener('click', function(){ document.querySelectorAll('.term.show-popup').forEach(function(t){ t.classList.remove('show-popup'); }); });
"""

count = 0
for d in DIRS:
    for f in sorted(d.glob("*.html")):
        src = f.read_text(encoding="utf-8")

        # 1) Replace .term-popup CSS block
        src = OLD_TERM_POPUP_BLOCK.sub(NEW_TERM_POPUP_CSS, src)

        # 2) Fix mobile override
        src = OLD_MOBILE_COMMENT.sub(NEW_MOBILE_OVERRIDE, src)

        # 3) Inject JS (before </body> if not already present)
        if "term popup click toggle" not in src:
            src = src.replace("</body>", TERM_JS + "\n</body>")

        f.write_text(src, encoding="utf-8")
        count += 1
        print(f"  ✓ {f.name}")

print(f"\nDone: {count} files updated")
