#!/usr/bin/python3
from pathlib import Path
from shutil import copyfile


def newname(p: Path):
    return Path(f"{p.parent.name}_{p.name}.{p.stem}")


def oldname(p: Path):
    assert "_" in p.name
    parent, name = p.name.split("_", 1)
    return Path(parent, name)


if __name__ == "__main__":
    Path("./pdfs").mkdir(exist_ok=True)

    for pdf in Path(".").glob("**/*.pdf"):
        if pdf.parent.name == "pdfs":
            continue
        target = Path("./pdfs", newname(pdf))
        copyfile(pdf, target)
