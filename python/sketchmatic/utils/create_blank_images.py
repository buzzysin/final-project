import argparse
from pathlib import Path
import cv2 as cv
import numpy as np

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-o", "--output", type=str, required=True, help="Output directory")
  parser.add_argument("-p", "--prefix", type=str, default="image", help="Prefix for the image name, default: %(default)s")

  parser.add_argument("-x", "--width", type=int, default=500, help="Width of the image, default: %(default)s")
  parser.add_argument("-y", "--height", type=int, default=500, help="Height of the image, default: %(default)s")


  parser.add_argument("-s", "--start", type=int, default=0, help="Number of images to create")

  groupA = parser.add_mutually_exclusive_group(required=True)
  groupA.add_argument("-c", "--count", type=int, default=100, help="Number of images to create")

  groupB = parser.add_mutually_exclusive_group(required=True)
  groupB.add_argument("-S", "--stop", type=int,  help="Last image to create")
  

  args = parser.parse_args()
  
  output = Path(args.output)
  prefix = args.prefix
  width = args.width
  height = args.height
  start = args.start
  stop = args.stop if args.stop else args.start + args.count

  output.mkdir(parents=True, exist_ok=True)

  for i in range(start, stop):
    image = np.zeros((height, width, 3), np.uint8)
    cv2.imwrite(str(output / f"{prefix}_{i:4}.png"), image)


if __name__ == "__main__":
  main()