#!/usr/bin/python3
from pathlib import Path
from subprocess import run

root = Path(__file__).parent.parent
if __name__ == "__main__":
    all_dirs = set(x.parent for x in root.glob("**/.copier-answers.yml"))
    failed = []
    total = len(all_dirs)
    done = 0
    for dir in all_dirs:
        try:
            done += 1
            print(f"[{done}/{total}]\t{dir}")
            run(['copier', 'update', dir.name, '-A'], check=True, text=True)        
            run(['git', 'add', '--all', '--', ':!*/propers.tex'], text=True)
            run(['git', 'commit', '-m', f"build: bump version [{dir.name}]"], text=True)
            run(['git', 'stash', 'pop'], text=True)
            run(['git', 'stash'], text=True)
        except:
            failed.append(dir)

    if failed:
        print("Some files failed to update:", failed)
    else:
        print("Update complete")