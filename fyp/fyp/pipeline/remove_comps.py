#!/usr/bin/env python3

import argparse
import logging

from ultralytics import YOLO
from ultralytics.yolo.engine.results import Results
from cv2 import VideoCapture, imshow, waitKey

def remove_comps(args):
  model = YOLO(args.weights)
  stream = VideoCapture(0)

  if not stream.isOpened():
    logging.error("Could not open video stream")
    exit(1)

  while True:
    ret, frame = stream.read()
    if not ret:
      logging.error("Could not read frame")
      break

    results: "list[Results]" = model.predict(frame)
    
    if len(results) == 0:
      continue

    result = results[0]

    if result.boxes is None:
      continue
    
    for box in result.boxes:
      x1, y1, x2, y2 = box.xyxy
      x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
      frame[y1:y2, x1:x2] = 255

    imshow("frame", frame)
    if waitKey(1) & 0xFF == ord("q"):
      break
  




def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--weights", type=str, help="initial weights path")
  
  args = parser.parse_args()
  remove_comps(args)


if __name__ == "__main__":
  main()
