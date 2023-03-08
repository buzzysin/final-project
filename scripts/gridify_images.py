# Description: Gridify images in a directory into a single image
import cv2 as cv
from pathlib import Path
import numpy as np
from argparse import ArgumentParser


def main():
  # Take a subset of images from a directory and grid them into a single image

  parser = ArgumentParser()

  parser.add_argument("-d", "--dir", type=str, required=True,
                      help="Directory with images to gridify")
  parser.add_argument("-f", "--file", type=str,
                      required=True, help="File to save the gridified image")
  parser.add_argument("-r", "--rows", type=int, default=10,
                      help="Number of rows in the grid, default: %(default)s")
  parser.add_argument("-c", "--cols", type=int, default=10,
                      help="Number of columns in the grid, default: %(default)s")
  parser.add_argument("-s", "--size", type=int, default=500,
                      help="Size of the image, default: %(default)s")

  args = parser.parse_args()

  dir = Path(args.dir)
  file = Path(args.file)
  rows = args.rows
  cols = args.cols
  size = args.size

  images = []
  for image in dir.glob("*.png"):
    images.append(cv.imread(str(image)))

  # Create a blank image
  image = np.ones((rows * size, cols * size, 3), np.uint8) * 255

  # Copy the images into the blank image
  for i in range(rows):
    for j in range(cols):
      image[i * size:(i + 1) * size, j * size:(j + 1)
            * size] = images[i * cols + j]

  cv.imwrite(str(file), image)


if __name__ == "__main__":
  main()
