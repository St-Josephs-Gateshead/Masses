#!/usr/bin/python3
from pathlib import Path
from shutil import copyfile


def newname(p: Path):
    return Path(f"{p.parent.name}_{p.name}")


def oldname(p: Path):
    assert "_" in p.name
    parent, name = p.name.split("_", 1)
    return Path(parent, name)


if __name__ == "__main__":
    root = Path(__file__).parent.parent
    outdir = root / "pdfs"
    outdir.mkdir(exist_ok=True)

    for pdf in root.glob("**/*.pdf"):
        if pdf.parent.name == "pdfs":
            continue
        target = outdir / newname(pdf)
        copyfile(pdf, target)
        print("Copied", pdf, "to", target)
