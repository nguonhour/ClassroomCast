#!/bin/sh
# Rebuilds the PDF from the Markdown source. Requires pandoc and Google Chrome.
cd "$(dirname "$0")/.."
N=ClassroomCast_Project_Scope_and_Teacher_Summary
pandoc "$N.md" -s --embed-resources --template _build/template.html -c _build/style.css -o "_build/$N.html"
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$N.pdf" "file://$PWD/_build/$N.html" 2>/dev/null
echo "Built $N.pdf"
