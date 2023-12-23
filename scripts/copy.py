from pathlib import Path

Stem = str

files: dict[Path, Stem] = {
    Path("introit.gabc"): Stem("in--"),
    Path("gradual.gabc"): Stem("gr--"),
    Path("alleluia.gabc"): Stem("al--"),
    Path("offertory.gabc"): Stem("of--"),
    Path("communion.gabc"): Stem("co--"),
}


def populate(src_dir: Path, dest_dir: Path):
    for target, stem in files.items():
        candidates = list(src_dir.glob(f"{stem}*.gabc"))
        assert len(candidates) == 1
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
