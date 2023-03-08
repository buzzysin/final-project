# Turn Pascal VOC annotations into YOLO format

import os
import argparse
import xml.etree.ElementTree as ET
from pathlib import Path


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--input", type=str,
                      required=True, help="Input directory")
  parser.add_argument("-o", "--output", type=str,
                      required=True, help="Output directory")
  parser.add_argument("-c", "--classes", type=str,
                      required=True, help="Classes file")

  args = parser.parse_args()

  input = Path(args.input)
  output = Path(args.output)
  classes = Path(args.classes)

  # Read the classes
  class_names = []
  with open(classes, "r") as f:
    for line in f:
      class_names.append(line.strip())

  # Create the output directory
  output.mkdir(parents=True, exist_ok=True)

  # Process the annotations
  for annotation in input.glob("*.xml"):
    # Read the annotation
    tree = ET.parse(annotation)
    root = tree.getroot()

    # Get the image name
    image_root = root.find("filename")

    if image_root is None:
      return

    image_name = image_root.text.split(".")[0] # type: ignore

    # Get the image size
    size = root.find("size")

    if size is None:
      return

    image_width = int(size.find("width").text)  # type: ignore
    image_height = int(size.find("height").text)  # type: ignore

    # Get the objects
    objects = root.findall("object")

    # Create the output file
    output_file = output / f"{image_name}.txt"
    with open(output_file, mode="w") as f:
      for obj in objects:
        # Get the class name
        class_name = obj.find("name").text  # type: ignore

        class_index = class_names.index(class_name)

        # Get the bounding box
        bndbox = obj.find("bndbox")
        xmin = int(bndbox.find("xmin").text)  # type: ignore
        ymin = int(bndbox.find("ymin").text)  # type: ignore
        xmax = int(bndbox.find("xmax").text)  # type: ignore
        ymax = int(bndbox.find("ymax").text)  # type: ignore

        # Calculate the center and width
        x = (xmin + xmax) / 2 / image_width
        y = (ymin + ymax) / 2 / image_height
        w = (xmax - xmin) / image_width
        h = (ymax - ymin) / image_height

        # Write the line
        f.write(f"{class_index} {x} {y} {w} {h} {os.linesep}")


if __name__ == "__main__":
  main()
