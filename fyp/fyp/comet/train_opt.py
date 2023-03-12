from typing import Any, Dict

from comet_ml import Optimizer

from ..configs.configs import config_optimizer, config_train, config_base

from ultralytics import YOLO


def main():
  # Create an optimizer object
  optimizer = Optimizer(config=config_optimizer)

  model = YOLO(**config_base)

  for experiment in optimizer.get_experiments():
    # Get hyperparameters
    parameters = experiment.params.copy()
    config = config_train.copy()

    for key, value in parameters.items():
      if key.endswith("_train"):
        parameters[key.replace("_train", "")] = value
        del parameters[key]

    config.update(parameters)
    parameters = config

    with experiment.train():
      # Start experiment
      experiment.log_parameters(parameters)

    # Train model
    model.train(**parameters)

    with experiment.test():
      results = model.val()

      experiment.log_parameter("metrics/mAP_0.5", results.box.map50)


if __name__ == "__main__":
  main()
