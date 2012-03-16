# -*- coding: UTF-8 -*-

import os
from setuptools import setup

def read(fname):
  return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name = "pywidl",
  version = "0.0",
  author = "Vasily Stepanov",
  author_email = "vasily.stepanov@gmail.com",
  description = "Generic code generator from WebIDL interfaces.",
  install_requires = ['ply>=3.4'],
  setup_requires = ['ply>=3.4'],
  license = "MIT",
  keywords = "webidl",
  url = "https://github.com/VasilyStepanov/pywidl",
  packages = ['pywidl', 'tests'],
  long_description = read('README'),
  classifiers = [
    "Development Status :: 1 - Planning",
    "Topic :: Software Development :: Code Generators",
    "License :: OSI Approved :: MIT License",
  ],
  entry_points = """
    [console_scripts]
      pywidl = pywidl.pywidl:main
  """
)
