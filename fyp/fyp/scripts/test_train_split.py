# Split a folder of images into train and test folders

import argparse
from pathlib import Path
import cv2 as cv
import numpy as np
import random


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-d", "--dir", type=str,
                      required=True, help="Directory with images to split")

  parser.add_argument("-t", "--train", type=str,
                      required=True, help="Train directory")

  parser.add_argument("-V", "--validate", type=str,
                      required=True, help="Validation directory")

  parser.add_argument("-T", "--test", type=str,
                      required=False, help="Test directory")

  parser.add_argument("--test_ratio", type=float, default=0.2,
                      help="Ratio of test images, default is %(default)s")

  parser.add_argument("--validate_ratio", type=float, default=0.2,
                      help="Ratio of validate images, default is %(default)s")

  args = parser.parse_args()

  dir = Path(args.dir)
  train = Path(args.train)
  test = Path(args.test)
  validate = Path(args.validate)
  test_ratio = args.test_ratio if test else 0
  validate_ratio = args.validate_ratio
  train_ratio = 1 - validate_ratio - test_ratio

  train.mkdir(parents=True, exist_ok=True)
  validate.mkdir(parents=True, exist_ok=True)
  if test:
    test.mkdir(parents=True, exist_ok=True)

  images = []
  for image in dir.glob("*.png"):
    images.append(image)

  random.shuffle(images)

  train_split = int(len(images) * train_ratio)
  val_split = int(len(images) * validate_ratio)
  test_split = int(len(images) * test_ratio)

  for image in images[:train_split]:
    cv.imwrite(str(train / image.name), cv.imread(str(image)))

    # Find the label file (either *.txt or *.xml) and copy it to the train directory
    label = image.with_suffix(".txt")
    if not label.exists():
      label = image.with_suffix(".xml")

    with open(str(train / label.name), "w") as f:
      f.write(label.read_text())

  for image in images[train_split: train_split + val_split]:
    cv.imwrite(str(validate / image.name), cv.imread(str(image)))

    # Find the label file (either *.txt or *.xml) and copy it to the validate directory
    label = image.with_suffix(".txt")
    if not label.exists():
      label = image.with_suffix(".xml")

    with open(str(validate / label.name), "w") as f:
      f.write(label.read_text())

  for image in images[train_split + val_split:]:
    cv.imwrite(str(test / image.name), cv.imread(str(image)))

    # Find the label file (either *.txt or *.xml) and copy it to the test directory
    label = image.with_suffix(".txt")
    if not label.exists():
      label = image.with_suffix(".xml")

    with open(str(test / label.name), "w") as f:
      f.write(label.read_text())


if __name__ == "__main__":
  main()
