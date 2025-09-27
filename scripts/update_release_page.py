from collections import defaultdict
from os import environ
from pathlib import Path

root = Path(__file__).parent.parent
masses = sorted(set(x.parent.name for x in root.glob("**/*.copier-answers.yml")))
repo = environ["GITHUB_REPOSITORY"]
assert repo
printout_types = {"missalette": "Missalette", "missalette-booklet": "Missalette [Booklet]", "pew-sheet": "Pew Sheet", "pew-sheet-booklet": "Pew Sheet [Booklet]"}
download_links = defaultdict(dict)
        
if __name__ == "__main__":
    assert Path(root, "releases.md").exists()
    releases = ["# Latest Releases", "| | | | | |", "| --- | --- | --- | --- | --- |"]
    for mass in masses:
        links = [' '.join(mass.split('-'))]
        for p_type, p_typeF in printout_types.items():
            if Path(root, "pdfs", f"{mass}_{p_type}.pdf").exists():
                links.append(f"[{p_typeF}](https://github.com/{repo}/releases/download/latest/{mass}_{p_type}.pdf)")
            else:
                links.append("_not available_")
        releases.append(f"| {'|'.join(links)} |")
        
    with open(Path(root, "releases.md"), "w") as f:
        f.write("\n".join(releases))