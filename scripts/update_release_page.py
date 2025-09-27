from collections import defaultdict
from os import environ
from pathlib import Path

import httpx

root = Path(__file__).parent.parent
masses = sorted(set(x.parent.name for x in root.glob("**/*.copier-answers.yml")))
repo = environ["GITHUB_REPOSITORY"]
assert repo
url = f"https://api.github.com/repos/{repo}/releases/latest"
printout_types = ["missalette", "missalette-booklet", "pew-sheet", "pew-sheet-booklet"]
download_links = defaultdict(dict)

def get(*args, **kwargs):
    while True:
        kwargs["follow_redirects"] = kwargs.get("follow_redirects", True)
        r = httpx.get(*args, **kwargs)
        r.raise_for_status()
        return r
    
def get_formatted_link(link, file_type):
    if link:
        return f"[{' '.join(file_type.split('-')).title()}]({link})"
    return "_not available_"
        
if __name__ == "__main__":
    releases = ["# Latest Releases", "| | | | | |", "| --- | --- | --- | --- | --- |"]
    assets = get(url).json()["assets"]
    for asset in assets:
        if asset["content_type"] != "application/pdf":
            continue
        asset_category = asset["name"].strip(".pdf").split("_")
        if asset_category[1] not in printout_types:
            print("A strange one found: ", asset_category[1])
        else:
            download_links[asset_category[0]][asset_category[1]] = asset["browser_download_url"]
    for mass in masses:
        releases.append(f'| {" | ".join([' '.join(mass.split('-'))] + [get_formatted_link(download_links[mass].get(t, ""), t) for t in printout_types])} |')
    with open(Path(root, "releases.md"), "w") as f:
        f.write("\n".join(releases))