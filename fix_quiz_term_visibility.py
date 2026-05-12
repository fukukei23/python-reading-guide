#!/usr/bin/env python3
"""
Fix term-popup visibility inside quiz-answer-inner sections.
Adds a dedicated CSS rule for better contrast.
"""
import re, glob

# CSS to inject — more visible styling for term-popups inside quiz answers
QUIZ_TERM_CSS = """
/* quiz answer term-popup — enhanced visibility */
.quiz-answer-inner .term-popup {
  background: rgba(167,139,250,0.28);
  color: #e0d4ff;
  font-weight: 600;
  font-size: 13px;
  padding: 2px 8px;
}
body.light .quiz-answer-inner .term-popup {
  background: rgba(109,40,217,0.18);
  color: #4c1d95;
}
"""

files = sorted(glob.glob("01_basics/interactive/*.html") + glob.glob("02_python_syntax/interactive/*.html"))
print(f"Processing {len(files)} files...")

for fp in files:
    with open(fp, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Skip if already fixed
    if "quiz-answer-inner .term-popup" in html:
        print(f"  SKIP (already fixed): {fp}")
        continue
    
    # Insert the quiz-term CSS right after the existing term-popup block
    # Find: "/* term-popup is now always visible */"
    marker = "/* term-popup is now always visible */"
    if marker not in html:
        print(f"  SKIP (no marker): {fp}")
        continue
    
    html = html.replace(marker, marker + QUIZ_TERM_CSS, 1)
    
    with open(fp, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"  FIXED: {fp}")

print("Done!")
