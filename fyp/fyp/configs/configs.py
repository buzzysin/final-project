# Runtime

class Runtime:
  def __init__(self, env):
    self.env = env

  def var(self, **kwargs):
    return kwargs[self.env] if self.env in kwargs else None


runtime = Runtime(env="dev")


config_base = {
    # The model to use
    "model": "models/custom-v8n.yaml",
}

# Run
config_train = {
    # The name of the project
    "project": "finalyearproject",
    # The name of the experiment
    "name": runtime.var(test="test", dev="dev"),
    # The path to the dataset
    "data": "datasets/circuits.yaml",
    # The number of epochs to train for
    "epochs": runtime.var(test=1, dev=10, prod=100),
    # The batch size
    # "batch": -1,  # -1 = auto
    # The image size
    "imgsz": runtime.var(test=256, dev=256, prod=512),
    # The number of GPUs to use
    "device": "0",
    # Overwrite existing results
    "exist_ok": runtime.var(dev=True, prod=False),
    # Validate the model after each epoch
    "val": runtime.var(dev=True, prod=False),
}

config_optimizer = {
    "algorithm": "bayes",
    "parameters": {
        "batch": {
            "type": "discrete",
            "values": [16, 32, 64]
        },
        "box": {
            "type": "discrete",
            "values": [0.02, 0.2]
        },
        "cls": {
            "type": "discrete",
            "values": [0.2]
        },
        "copy_paste": {
            "type": "discrete",
            "values": [1]
        },
        "degrees": {
            "type": "discrete",
            "values": [0, 45]
        },
        "epochs": {
            "type": "discrete",
            "values": [5]
        },
        "fl_gamma": {
            "type": "discrete",
            "values": [0]
        },
        "fliplr": {
            "type": "discrete",
            "values": [0]
        },
        "flipud": {
            "type": "discrete",
            "values": [0]
        },
        "hsv_h": {
            "type": "discrete",
            "values": [0]
        },
        "hsv_s": {
            "type": "discrete",
            "values": [0]
        },
        "hsv_v": {
            "type": "discrete",
            "values": [0]
        },
        "iou": {
            "type": "discrete",
            "values": [0.7]
        },
        "lr0": {
            "type": "discrete",
            "values": [0.00001, 0.1]
        },
        # "lrf": {
        #     "type": "discrete",
        #     "values": [0.01, 1]
        # },
        "mixup": {
            "type": "discrete",
            "values": [1]
        },
        "momentum": {
            "type": "discrete",
            "values": [0.6]
        },
        "mosaic": {
            "type": "discrete",
            "values": [0]
        },
        # "obj": {
        #     "type": "discrete",
        #     "values": [0.2]
        # },
        # "obj_pw": {
        #     "type": "discrete",
        #     "values": [0.5]
        # },
        "optimizer": {
            "type": "categorical",
            "values": ["SGD", "Adam", "AdamW"]
        },
        "perspective": {
            "type": "discrete",
            "values": [0]
        },
        "scale": {
            "type": "discrete",
            "values": [0]
        },
        "shear": {
            "type": "discrete",
            "values": [0]
        },
        "translate": {
            "type": "discrete",
            "values": [0]
        },
        "warmup_bias_lr": {
            "type": "discrete",
            "values": [0, 0.2]
        },
        "warmup_epochs": {
            "type": "discrete",
            "values": [5]
        },
        "warmup_momentum": {
            "type": "discrete",
            "values": [0, 0.95]
        },
        "weight_decay": {
            "type": "discrete",
            "values": [0, 0.001]
        }
    },
    "spec": {
        "maxCombo": 0,
        "metric": "metrics/mAP_0.5",
        "objective": "maximize"
    },
    "trials": 1
}
