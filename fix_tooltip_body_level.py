#!/usr/bin/env python3
"""
Fix term-popup: move from CSS absolute-positioned tooltip to JS body-level tooltip.
The CSS approach fails because parent overflow:hidden and z-index stacking contexts
hide the popup. This creates a single <div> at <body> level, positioned via
getBoundingClientRect(), completely escaping all containment.
"""

import re
from pathlib import Path

BASE = Path("/home/yn4416/projects/python-reading-guide")
DIRS = [
    BASE / "01_basics" / "interactive",
    BASE / "02_python_syntax" / "interactive",
]

# === CSS: replace the old term-popup rules with body-level tooltip styles ===

OLD_TERM_CSS = re.compile(
    r'\.term \{[^}]*\}'
    r'\s*\.term:hover \{[^}]*\}'
    r'\s*\.term-popup \{[^}]*\}'
    r'(?:\s*\.term-popup::after \{[^}]*\})?'
    r'\s*\.term:hover \.term-popup,\s*\.term:focus \.term-popup,\s*\.term\.show-popup \.term-popup \{[^}]*\}',
    re.DOTALL
)

NEW_TERM_CSS = """.term {
  border-bottom: 1px dashed var(--accent);
  cursor: help;
  color: #c4b5fd;
  transition: color 0.2s;
}
.term:hover, .term:focus { color: var(--fg-bright); }
.term-popup { display: none; }

/* body-level tooltip — positioned by JS, escapes all overflow/z-index */
#term-tooltip {
  display: none;
  position: fixed;
  background: var(--bg-raised);
  border: 1px solid var(--accent);
  border-radius: 8px;
  padding: 8px 14px;
  font-size: 13px;
  color: var(--fg);
  line-height: 1.6;
  white-space: nowrap;
  z-index: 99999;
  box-shadow: 0 8px 24px rgba(0,0,0,0.4), 0 0 0 1px rgba(124,58,237,0.3);
  pointer-events: none;
  max-width: 320px;
}
#term-tooltip::after {
  content: '';
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  border: 6px solid transparent;
  border-top-color: var(--accent);
}
#term-tooltip.below::after {
  top: auto;
  bottom: 100%;
  border-top-color: transparent;
  border-bottom-color: var(--accent);
}"""

# === Mobile override: replace old term-popup mobile rule ===
OLD_MOBILE_TERM = re.compile(
    r'\.term-popup \{ white-space: normal; min-width: 200px; max-width: 280px; font-size: 12px; \}'
)
NEW_MOBILE_TERM = "  #term-tooltip { white-space: normal; min-width: 200px; max-width: 280px; font-size: 12px; }"

# === JS: replace old term JS with body-level tooltip logic ===
OLD_TERM_JS = re.compile(
    r'// term popup click toggle \(mobile support\).*?'
    r'document\.addEventListener\(\'click\', function\(\)\{ document\.querySelectorAll\(\'\.term\.show-popup\'\)\.forEach\(function\(t\)\{ t\.classList\.remove\(\'show-popup\'\); \}\); \}\);',
    re.DOTALL
)

TERM_JS = """<script>
// term popup — body-level tooltip (escapes overflow/z-index)
(function(){
  var tip = document.createElement('div');
  tip.id = 'term-tooltip';
  document.body.appendChild(tip);
  var currentTerm = null;

  function showTip(term) {
    var popup = term.querySelector('.term-popup');
    if (!popup) return;
    tip.textContent = popup.textContent;
    tip.style.display = 'block';
    tip.classList.remove('below');

    // position: prefer above, fallback below
    var r = term.getBoundingClientRect();
    var tw = tip.offsetWidth;
    var th = tip.offsetHeight;
    var left = r.left + r.width / 2 - tw / 2;
    left = Math.max(8, Math.min(left, window.innerWidth - tw - 8));
    var top = r.top - th - 10;
    if (top < 8) {
      top = r.bottom + 10;
      tip.classList.add('below');
    }
    tip.style.left = left + 'px';
    tip.style.top = top + 'px';
    currentTerm = term;
  }

  function hideTip() {
    tip.style.display = 'none';
    currentTerm = null;
  }

  document.querySelectorAll('.term').forEach(function(t){
    t.setAttribute('tabindex', '0');
    t.addEventListener('mouseenter', function(){ showTip(t); });
    t.addEventListener('mouseleave', function(){ hideTip(); });
    t.addEventListener('focus', function(){ showTip(t); });
    t.addEventListener('blur', function(){ hideTip(); });
    // mobile: click toggle
    t.addEventListener('click', function(e){
      e.stopPropagation();
      if (currentTerm === t) { hideTip(); }
      else { showTip(t); }
    });
  });
  document.addEventListener('click', function(){ hideTip(); });
  window.addEventListener('scroll', function(){ if (currentTerm) showTip(currentTerm); }, {passive:true});
})();
</script>"""

count = 0
for d in DIRS:
    for f in sorted(d.glob("*.html")):
        src = f.read_text(encoding="utf-8")

        # 1) Replace term CSS block
        src = OLD_TERM_CSS.sub(NEW_TERM_CSS, src)

        # 2) Fix mobile override
        src = OLD_MOBILE_TERM.sub(NEW_MOBILE_TERM, src)

        # 3) Replace old term JS (or inject new if old not found)
        if OLD_TERM_JS.search(src):
            src = OLD_TERM_JS.sub(TERM_JS, src)
        elif "term popup — body-level" not in src:
            # Inject before </body> but after existing scripts
            src = src.replace("</body>", "\n" + TERM_JS + "\n</body>")
        else:
            print(f"  - {f.name} (already fixed)")
            continue

        f.write_text(src, encoding="utf-8")
        count += 1
        print(f"  ✓ {f.name}")

print(f"\nDone: {count} files updated")
