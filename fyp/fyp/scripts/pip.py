#!/usr/bin/env python3

import subprocess
import sys 

if __name__ == '__main__':
  _python = sys.executable
  args = sys.argv
  
  # Remove the first argument, which is the name of this script.
  args.pop(0)

  # Run the script.
  # print(f"Running: {_python} -m pip {' '.join(args)}")
  subprocess.run([_python, '-m', "pip", *args])
