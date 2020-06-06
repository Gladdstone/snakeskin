import os

from setuptools import setup, find_packages

VERSION = "0.0"

requirements_path = os.path.dirname(os.path.realpath(__file__)) + "/requirements.txt"
DEPENDENCIES = []
if os.path.isfile(requirements_path):
  with open(requirements_path) as file:
    DEPENDENCIES = file.read().splitlines()

with open("README.md", "r") as f:
  LONG_DESCRIPTION = f.read()

setup(
  name="snakeskin_cli",
  version=VERSION,
  description="A Python command-line tool for quickly creating Packer images",
  license="MIT",
  long_description=LONG_DESCRIPTION,
  author="Joseph Farrell",
  author_email="joe@joefarrell.dev",
  url="https://github.com/Gladdstone/snakeskin",
  packages=find_packages(exclude=["*.tests.*", "tests_*", "tests"]),
  install_requires=DEPENDENCIES
)