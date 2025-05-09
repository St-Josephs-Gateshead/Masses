from pathlib import Path

Stem = str

files: dict[Path, Stem] = {
    Path("introit.gabc"): Stem("in--"),
    Path("gradual.gabc"): Stem("gr--"),
    Path("alleluia.gabc"): Stem("al--"),
    Path("offertory.gabc"): Stem("of--"),
    Path("communion.gabc"): Stem("co--"),
    Path("tract.gabc"): Stem("tr--"),
}


def populate(src_dir: Path, dest_dir: Path):
    for target, stem in files.items():
        candidates = list(src_dir.glob(f"{stem}*.gabc"))
        if not candidates:
            continue
        assert (
            len(candidates) == 1
        ), f"Multiple candidates found for {src_dir}/{stem}*.gabc"
        candidates[0].rename(dest_dir / target)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "--src-dir", type=Path, default=Path("~/Downloads").expanduser()
    )
    parser.add_argument("DEST_DIR", type=Path)
    args = parser.parse_args()

    populate(args.src_dir, args.DEST_DIR)
