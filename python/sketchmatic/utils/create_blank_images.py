import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("width", type=int)
  parser.add_argument("height", type=int)
  parser.add_argument("count", type=int)
  parser.add_argument("start", type=int)
  parser.add_argument("stop", type=int)
  parser.add_argument("output", type=str)
  args = parser.parse_args()

  from PIL import Image
  from pathlib import Path
  import numpy as np

  output_dir = Path(args.output)
  output_dir.mkdir(parents=True, exist_ok=True)

  for i in range(args.count):
    image = Image.fromarray(np.zeros((args.height, args.width, 3), dtype=np.uint8))
    image.save(output_dir / f"{i}.png")

if __name__ == "__main__":
  main()