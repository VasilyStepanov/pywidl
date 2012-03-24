#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from setuptools import setup
from distutils.command.build_py import build_py
from pywidl.pywidl import name
from pywidl.pywidl import version



class build_py_with_ply(build_py):
  def run(self, *args, **kwargs):
    import pywidl.lexis
    import pywidl.grammar
    build_py.run(self, *args, **kwargs)



def read(fname):
  return open(os.path.join(os.path.dirname(__file__), fname)).read()



setup(
  cmdclass = { 'build_py' : build_py_with_ply },

  name = name,
  version = version,
  author = "Vasily Stepanov",
  author_email = "vasily.stepanov@gmail.com",
  description = "Generic code generator from WebIDL interfaces.",
  install_requires = ["ply>=3.4", "mako>=0.5"],
  setup_requires = ["ply>=3.4"],
  license = "MIT",
  keywords = "webidl",
  url = "https://github.com/VasilyStepanov/pywidl",
  packages = ["pywidl", "tests"],
  long_description = read("README.md"),
  classifiers = [
    "Development Status :: 3 - Alpha",
    "Topic :: Software Development :: Code Generators",
    "License :: OSI Approved :: MIT License",
  ],
  test_suite = "tests.test_suite",
  entry_points = {
    "console_scripts" : [
      "pywidl = pywidl.pywidl:main"
    ],
  },
)
