#!/usr/bin/python3
from pathlib import Path

Path("./pdfs").mkdir(exist_ok=True)

for pdf in Path(".").glob("**/*.pdf"):
    if pdf.parent.name == "pdfs":
        continue
    if pdf.stem.endswith("booklet"):
        target = Path(f"./pdfs/{pdf.parent.name}-booklet.pdf")
    else:
        target = Path(f"./pdfs/{pdf.parent.name}.pdf")

    # yeah, we could use copy...
    with target.open("wb") as f:
        with pdf.open("rb") as g:
            f.write(g.read())
