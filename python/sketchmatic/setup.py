from setuptools import setup, find_packages

REQUIRES = [
  # CLI
  # Processing
  "opencv-python",
  "numpy",
  "matplotlib",
  "seaborn",
]

PACKAGE_NAME = "sketchmatic"

setup(
  name=PACKAGE_NAME,
  version="0.0.1",
  author="Your Name",
  author_email="",
  description="Sketchmatic",
  long_description="",
  long_description_content_type="text/markdown",
  url="",
  packages=find_packages(),
  install_requires=REQUIRES,
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
)

