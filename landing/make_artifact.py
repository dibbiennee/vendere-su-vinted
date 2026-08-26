#!/usr/bin/env python3
"""Deriva artifact.html da index.html: stessa pagina, senza lo scaffolding
del documento, che l'ambiente Artifact aggiunge per conto suo."""
import re, pathlib
src = pathlib.Path(__file__).parent / "index.html"
out = pathlib.Path(__file__).parent / "artifact.html"
s = src.read_text(encoding="utf-8")
s = s.replace("<!DOCTYPE html>\n", "").replace('<html lang="it">\n', "")
s = s.replace("<head>\n", "").replace('<meta charset="utf-8">\n', "")
s = s.replace("</head>\n", "").replace("<body>\n", "")
s = s.replace("</body>\n", "").replace("</html>\n", "")
out.write_text(s, encoding="utf-8")
print("scritto", out.name, len(s)//1024, "KB")
