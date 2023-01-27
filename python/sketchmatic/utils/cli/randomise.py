import argparse
from pathlib import Path
import random


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--input", type=str,
                      required=True, help="Input directory")
  parser.add_argument("-p", "--prefix", type=str, default="image",
                      help="Prefix for the image name, default: %(default)s")

  group = parser.add_mutually_exclusive_group()
  group.add_argument("-o", "--output", type=str, help="Output directory")
  group.add_argument("-I", "--in-place", action="store_true",
                     default=False, help="Rename images in place")

  args = parser.parse_args()

  input = Path(args.input)
  output: Path | None = Path(args.output) if args.output is not None else Path(
      args.input + "_randomised")
  prefix: str = args.prefix
  in_place: bool = args.in_place

  input.mkdir(parents=True, exist_ok=True)
  output.mkdir(parents=True, exist_ok=True)

  images = list(input.glob("*.png"))
  renamed = images[:]
  random.shuffle(renamed)

  for i, image in enumerate(renamed):
    image.rename(output / f"{prefix}_{i:03}.png")
    renamed[i] = output / f"{prefix}_{i:03}.png"

  if in_place:
    for i, image in enumerate(renamed):
      image.rename(input / f"{prefix}_{i:03}.png")

    # Empty the output directory
    for image in output.glob(f"{prefix}_*.png"):
      image.unlink()

    # Delete the output directory if it is empty
    if not list(output.glob("*")):
      output.rmdir()
    


if __name__ == "__main__":
  main()
