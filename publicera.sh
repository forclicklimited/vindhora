#!/usr/bin/env bash
# Publicerar Vindhora till https://forclicklimited.github.io/vindhora/
set -euo pipefail
cd "$(dirname "$0")"
cp vindhora.html index.html
git add -A
if git diff --cached --quiet; then echo "Inget nytt att publicera."; exit 0; fi
git commit -qm "${1:-Vindhora: uppdaterad katalog}"
git push -q origin main
echo "Publicerat. Live om ~1 min: https://forclicklimited.github.io/vindhora/"
