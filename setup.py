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
    description = ("An demonstration of how to create, document, and publish "
                                   "to the cheese shop a5 pypi.org."),
    license = "MIT",
    keywords = "webidl",
    url = "https://github.com/VasilyStepanov/pywidl",
    packages=['pywidl', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Software Development :: Code Generators",
        "License :: OSI Approved :: MIT License",
    ],
)
