from argparse import ArgumentParser
import cv2 as cv
from pathlib import Path
import numpy as np


def get_bounding_box(img: np.ndarray):
  height, width = img.shape
  xt, yt, xb, yb = 0, 0, width, height
  
  for x in range(width):
    if np.any(img[:, x] < 255):
      xt = x
      break

  for x in range(width - 1, 0, -1):
    if np.any(img[:, x] < 255):
      xb = x
      break

  for y in range(height):
    if np.any(img[y, :] < 255):
      yt = y
      break

  for y in range(height - 1, 0, -1):
    if np.any(img[y, :] < 255):
      yb = y
      break

  return xt, yt, xb, yb


def main():
  parser = ArgumentParser()

  parser.add_argument("-d", "--dir", type=str, required=True,
                      help="Directory with images to center")
  parser.add_argument("-O", "--outdir", type=str,
                      required=True, help="Outdir directory")

  args = parser.parse_args()

  dir = Path(args.dir)
  outdir = Path(args.outdir)

  outdir.mkdir(parents=True, exist_ok=True)

  for image in dir.glob("*.png"):
    source = cv.imread(str(image))
    filtered = cv.cvtColor(source, cv.COLOR_BGR2GRAY)

    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    filtered = clahe.apply(filtered)
    
    filtered = cv.adaptiveThreshold(
        filtered, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    height, width = filtered.shape

    # Find the bounding box of the image
    xt, yt, xb, yb = get_bounding_box(filtered)

    print(xt, yt, xb, yb)

    # Crop the image
    filtered = filtered[yt:yb, xt:xb]

    # Create a blank image
    canvas = np.ones((height, width), np.uint8) * 255

    # Center the image
    x = (width - filtered.shape[1]) // 2
    y = (height - filtered.shape[0]) // 2
    canvas[y:y + filtered.shape[0], x:x + filtered.shape[1]] = filtered

    # Save the image
    cv.imwrite(str(outdir / f"{image.stem}.png"), canvas)

if __name__ == "__main__":
  main()
