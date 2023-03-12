import argparse
from pathlib import Path

import comet_ml
from comet_ml import Experiment

from ultralytics import YOLO

global exp


def train(args):
  # Stop any previous experiments

  try:
    model = YOLO(model=args.model)

    model.train(data=args.data,
                epochs=args.epochs,
                batch=args.batch,
                imgsz=args.imgsz,
                device=args.device,
                exist_ok=args.exist_ok,
                save=args.save,
                save_period=args.save_period,
                #
                project=args.project,
                name=args.name
                )

    results = model.predict()

  except Exception as e:
    raise e

  finally:
    ...
    # exp.end()


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--model", type=str, help="model path", default="yolov8n.pt")
  parser.add_argument("--data", type=str, help="data path", default="datasets/circuits.yaml")
  parser.add_argument("--epochs", type=int, help="number of epochs", default=100)
  parser.add_argument("--batch", type=int, help="batch size", default=4)
  parser.add_argument("--imgsz", type=int, help="image size", default=512)
  parser.add_argument("--save", type=bool, help="save model", default=True)
  parser.add_argument("--save-period", type=int,
                      help="save period", default=20)
  parser.add_argument("--exist-ok", help="exist ok",
                      action="store_true", default=False)
  parser.add_argument("--device", type=str, help="device", default="0")
  parser.add_argument("--project", type=str,
                      help="project name", default="finalyearproject")
  parser.add_argument("--name", type=str,
                      help="experiment name", default="default")

  args = parser.parse_args()

  train(args)


if __name__ == "__main__":
  main()
