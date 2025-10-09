#!/usr/bin/python3
import traceback
from collections import defaultdict, namedtuple
from contextlib import suppress
from datetime import datetime
from io import BytesIO
from os import environ
from pathlib import Path
from re import search
from sys import path
from time import sleep
from typing import Any, Iterable
from zipfile import ZipFile

import httpx

path.insert(0, str(Path("__file__").parent))

from package import oldname

root = Path(__file__).parent.parent

EXPECTED_NO_PDFS = 4 # (misallette + pew sheet) * (normal, booklet)


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


def get_pdf_links(assets: list[dict[str, Any]]) -> dict[str, dict[str, str]]:
    links = defaultdict(dict)
    for asset in assets:
        name = asset["name"]
        if not name.endswith(".pdf") or "_" not in name:
            print("skipping", name)
            continue
        else:
            parent, name = name.split("_", 1)
            links[parent][name] = asset["browser_download_url"]
    return links


def generate_makefile(dirs: Iterable[Path]):
    print("generating makefile for", dirs)
    makefile = root / "makefile"
    if not dirs:
        makefile.write_text(".PHONY: all\n\n all:\n\techo 'nothing to do...'\n\n")
        return

    dirs = [x.relative_to(root) for x in dirs]
    with makefile.open("w") as f:
        f.write(f".PHONY: all {' '.join(str(x) for x in dirs)}\n\n")
        f.write(f"all: {' '.join(str(x) for x in dirs)}\n\n")
        for dir in dirs:
            f.write(f"{dir}:\n")
            f.write(f"\tmake -C {dir} || true\n\n")


def download_pdfs(outdir: Path) -> int:
    for name, link in asset_links[outdir.name].items():
        print(f"downloading {outdir.name}/{name}")
        r = get(link)
        with (outdir / name).open("wb") as f:
            f.write(r.content)

    return len(asset_links[outdir.name])


Version = namedtuple("Version", "template_version,document_version")


def version(texf: Path) -> Version | None:
    assert texf.suffix == ".yml"
    match = []
    for v in ["_commit", "version"]:
        try:
            line = next(l for l in texf.read_text().splitlines() if v in l)
        except StopIteration:
            return None

        found = search(r"((0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$)", line)
        if found:
            match.append(found.group(0))

    if len(match) == 2:
        return Version(match[0], match[1])
    else:
        return None


if __name__ == "__main__":
    repo = environ["GITHUB_REPOSITORY"]
    assert repo

    all_dirs = set(x.parent for x in root.glob("**/[Mm]akefile"))
    url = f"https://api.github.com/repos/{repo}/releases/latest"
    try:
        data = get(url).json()
        asset_links = get_pdf_links(data["assets"])
        zipf = get(data["zipball_url"]).content
        zipf = ZipFile(BytesIO(zipf))
        outer = Path(zipf.namelist()[0])
        zipf.extractall()
        release = Path("latest-release")
        outer.rename(release)
        assert release.exists()

        changed_dirs = set()
        fs = list(release.glob("**/.copier-answers.yml"))
        print("fs", fs)
        for origf in fs:
            currentf = root / origf.relative_to(release)
            if not currentf.exists():
                continue
            if v_original := version(origf):
                if v_original != (v_current:=version(currentf)):
                    print(f"{origf} [{v_original}] differs from {currentf} [{v_current}]")
                else:
                    print(origf, "is identical to", currentf)
                    count = download_pdfs(currentf.parent)
                    if count == EXPECTED_NO_PDFS:
                        with suppress(KeyError):
                            all_dirs.remove(currentf.parent)
                    else:
                        print("incorrect number of pdfs found, will rebuild", currentf)
            else:
                print(origf, "has no version, skipping...")
    except Exception as e:
        print("Unable to get previous release, assuming none")
        traceback.print_exc()

    generate_makefile(all_dirs)
