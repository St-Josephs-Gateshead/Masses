#!/usr/bin/python3
import traceback
from collections import namedtuple
from contextlib import suppress
from datetime import datetime
from io import BytesIO
from os import environ
from pathlib import Path
from re import findall
from sys import path
from time import sleep
from typing import Iterable
from zipfile import ZipFile

import httpx

path.insert(0, str(Path("__file__").parent))

from package import oldname

root = Path(__file__).parent.parent


def get(*args, **kwargs):
    while True:
        kwargs["follow_redirects"] = kwargs.get("follow_redirects", True)
        r = httpx.get(*args, **kwargs)
        if r.status_code == 403:
            reset = datetime.fromtimestamp(int(r.headers["X-RateLimit-Reset"]))
            diff = max((reset - datetime.now()).total_seconds(), 0)
            print("Ratelimited for", diff, "seconds")
            sleep(diff)
        else:
            r.raise_for_status()
            return r


def generate_makefile(dirs: Iterable[Path]):
    print("generating makefile for", dirs)
    makefile = root / "makefile"
    if not dirs:
        makefile.write_text(".PHONY: all\n\n all:\n\techo 'nothing to do...'\n\n")
        return

    dirs = [x.relative_to(root) for x in dirs]
    with makefile.open("w") as f:
        f.write(f".PHONY: all {' '.join(str(x) for x in dirs)}\n\n")
        for dir in dirs:
            f.write(f"{dir}:\n")
            f.write(f"\tmake -C {dir}\n\n")


def download_pdfs(outdir: Path):
    for asset in assets:
        name = asset["name"]
        if not name.endswith(".pdf") or "_" not in name:
            print("skipping", name)
            continue
        old = oldname(Path(name))
        if old.parent.name == outdir.name:
            print("downloading", old)
            r = get(asset["browser_download_url"])
            with (outdir / old.name).open("wb") as f:
                f.write(r.content)


Version = namedtuple("Version", "document_version,template_version")


def version(texf: Path) -> Version | None:
    assert texf.suffix == ".tex"
    try:
        line = next(l for l in texf.read_text().splitlines() if "\\version" in l)
    except StopIteration:
        return None

    match = findall(r"(v[0-9]+\.[0-9]+\.[0-9]+.+?)", line)
    if match:
        assert len(match) == 2
        # regex catches any trailing chars for e.g. v1.0.0rc1, but we also have a ) after it
        return Version(match[0].strip(), match[1].replace(")", "").strip())
    else:
        return None


if __name__ == "__main__":
    repo = environ["GITHUB_REPOSITORY"]
    assert repo

    all_dirs = set(x.parent for x in root.glob("**/[Mm]akefile"))
    url = f"https://api.github.com/repos/{repo}/releases/latest"
    try:
        data = get(url).json()
        assets = get(data["assets_url"]).json()
        zipf = get(data["zipball_url"]).content
        zipf = ZipFile(BytesIO(zipf))
        outer = Path(zipf.namelist()[0])
        zipf.extractall()
        release = Path("latest-release")
        outer.rename(release)
        assert release.exists()

        changed_dirs = set()
        fs = list(release.glob("**/*.tex"))
        print("fs", fs)
        for origf in fs:
            currentf = root / origf.relative_to(release)
            if v := version(origf):
                if v != version(currentf):
                    print(origf, "differs from", currentf)
                else:
                    print(origf, "is identical to", currentf)
                    download_pdfs(currentf.parent)
                    with suppress(KeyError):
                        all_dirs.remove(currentf.parent)
            else:
                print(origf, "has no version, skipping...")
    except Exception as e:
        print("Unable to get previous release, assuming none")
        traceback.print_exc()

    generate_makefile(all_dirs)
