import subprocess
import os

import yaml

def get_dataset():
    cmd = 'curl -sSL "https://app.roboflow.com/ds/WJ2NHgkqKC?key=es7KnLYPIv" > circuits.zip'
    result = subprocess.call(cmd, shell=True)

    if result != 0:
        print("Error downloading dataset")
        return
    
    os.makedirs("data/circuits", exist_ok=True)

    cmd = 'unzip -o circuits.zip -d data/circuits'
    result = subprocess.call(cmd, shell=True)

    if result != 0:
        print("Error unzipping dataset")
        return

    os.unlink("circuits.zip")

    os.makedirs("datasets", exist_ok=True)

    if os.path.exists("datasets/circuits.yaml"):
        os.unlink("datasets/circuits.yaml")

    os.rename("data/circuits/data.yaml", "datasets/circuits.yaml")

    with open("datasets/circuits.yaml", "r") as f:
        circuits = yaml.load(f, Loader=yaml.FullLoader)
        circuits["path"] = "../data/circuits"
        circuits["train"] = "./train"
        circuits["val"] = "./val"

        if circuits["test"]:
          circuits["test"] = "./test"

    with open("datasets/circuits.yaml", "w") as f:
        yaml.dump(circuits, f)




if __name__ == "__main__":
    get_dataset()