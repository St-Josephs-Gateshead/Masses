#!/usr/bin/python3
from filecmp import cmp
from os import environ
from pathlib import Path
from shutil import unpack_archive
from sys import path
from typing import Iterable

import httpx

path.insert(0, str(Path("__file__").parent))

from package import oldname

root = Path(__file__).parent.parent


def generate_makefile(dirs: Iterable[Path]):
    dirs = [x.relative_to(root) for x in dirs]
    with (root / "makefile").open("w") as f:
        f.write(f".PHONY: all {' '.join(str(x) for x in dirs)}\n\n")
        for dir in dirs:
            f.write(f"{dir}:\n")
            f.write(f"\tmake -C {dir}\n\n")


repo = environ["GITHUB_REPOSITORY"]
assert repo


url = f"https://api.github.com/repos/{repo}/releases/latest"
resp = httpx.get(url, follow_redirects=True)
if resp.status_code == 404:
    print("No previous release")
    generate_makefile(set(x.parent for x in root.glob("*/[Mm]akefile")))
    exit(0)
resp.raise_for_status()
data = resp.json()

resp = httpx.get(data["assets_url"])
resp.raise_for_status()
assets = resp.json()


def download_pdfs(outdir: Path):
    old = oldname(outdir)
    for asset in assets:
        if asset["name"] == old.name:
            print("downloading", old)
            r = httpx.get(asset["browser_download_url"])
            r.raise_for_status()
            with (outdir / old.name).open("wb") as f:
                f.write(r.content)


resp = httpx.get(data["zipball_url"], follow_redirects=True)
resp.raise_for_status()
zipf = Path("latest-release.zip")
with zipf.open("wb") as f:
    f.write(resp.content)
unpack_archive(zipf)
# archive inner dir is reponame-releasename
outdir = Path(f"{repo.split('/')[1]}-{data['name'].lstrip('v')}")
outdir.rename("latest-release")

changed_dirs = set()
for origf in outdir.glob("*/*.tex"):
    parts = []
    for part in origf.parts:
        if part == outdir.name:
            break
        parts.append(part)
    currentf = Path(root, *parts)
    if not cmp(origf, currentf):
        changed_dirs.add(currentf.parent)
    else:
        download_pdfs(currentf.parent)

generate_makefile(changed_dirs)
