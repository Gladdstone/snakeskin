import os

from setuptools import setup, find_packages

def read_from_file(file_path, split=False):
  file_contents = []
  if os.path.isfile(version_path):
    with(version_path) as file:
      if split:
        file_contents = file.read().splitlines()
      else:
        file_contents = file.read()
  return file_contents

version_path = os.path.dirname(os.path.realpath(__file__)) + "/version.txt"
VERSION = read_from_file(version_path)

requirements_path = os.path.dirname(os.path.realpath(__file__)) + "/requirements.txt"
DEPENDENCIES = read_from_file(requirements_path, split=True)

description_path = os.path.dirname(os.path.realpath(__file__)) + "/README.md"
LONG_DESCRIPTION = read_from_file(description_path)

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