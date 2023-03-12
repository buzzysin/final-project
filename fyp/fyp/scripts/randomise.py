import argparse
from pathlib import Path
import random

EXT = "png"

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--indir", type=str,
                      required=True, help="Indir directory")
  parser.add_argument("-p", "--prefix", type=str, default="image",
                      help="Prefix for the image name, default: %(default)s")

  group = parser.add_mutually_exclusive_group()
  group.add_argument("-O", "--outdir", type=str, help="Output directory")
  group.add_argument("-I", "--in-place", action="store_true",
                     default=False, help="Rename images in place")

  args = parser.parse_args()

  indir = Path(args.indir)
  outdir: Path | None = Path(args.outdir) if args.outdir is not None else Path(
      args.indir + "_randomised")
  prefix: str = args.prefix
  in_place: bool = args.in_place

  indir.mkdir(parents=True, exist_ok=True)
  outdir.mkdir(parents=True, exist_ok=True)

  images = list(indir.glob(f"*.{EXT}"))
  renamed = images[:]
  random.shuffle(renamed)

  for i, image in enumerate(renamed):
    image.rename(outdir / f"{prefix}_{i:03}.{EXT}")
    renamed[i] = outdir / f"{prefix}_{i:03}.{EXT}"

  if in_place:
    for i, image in enumerate(renamed):
      image.rename(indir / f"{prefix}_{i:03}.{EXT}")

    # Empty the outdir directory
    for image in outdir.glob(f"{prefix}_*.{EXT}"):
      image.unlink()

    # Delete the outdir directory if it is empty
    if not list(outdir.glob("*")):
      outdir.rmdir()
    


if __name__ == "__main__":
  main()
