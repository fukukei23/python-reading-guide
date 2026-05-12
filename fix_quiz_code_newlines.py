#!/usr/bin/env python3
"""
Fix quiz-code sections: convert \\n to <br> and add white-space CSS.
"""
import re, glob

files = sorted(glob.glob("01_basics/interactive/*.html") + glob.glob("02_python_syntax/interactive/*.html"))
print(f"Processing {len(files)} files...")

quiz_code_css_added = 0
newline_fixed = 0

for fp in files:
    with open(fp, "r", encoding="utf-8") as f:
        html = f.read()
    
    original = html
    
    # 1. Add white-space to .quiz-code CSS if not already present
    if ".quiz-code" in html and "white-space" not in html.split(".quiz-code")[1].split("}")[0]:
        html = html.replace(
            ".quiz-code { margin:",
            ".quiz-code { white-space: pre-wrap; margin:",
            1
        )
        quiz_code_css_added += 1
    
    # 2. Convert literal \n inside quiz-code divs to actual newlines
    # Pattern: <div class="quiz-code">...\n...</div>
    def replace_newlines(m):
        content = m.group(1)
        # Replace literal \n with actual newline
        fixed = content.replace('\\n', '\n')
        return f'<div class="quiz-code">{fixed}</div>'
    
    html = re.sub(
        r'<div class="quiz-code">(.*?)</div>',
        replace_newlines,
        html,
        flags=re.DOTALL
    )
    
    if html != original:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  FIXED: {fp}")
        newline_fixed += 1
    else:
        print(f"  OK: {fp}")

print(f"\nDone! CSS updated: {quiz_code_css_added}, Newlines fixed: {newline_fixed}")
