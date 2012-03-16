#!/usr/bin/python

from pywidl.pywidl import App
import unittest
import os.path



class TestPyWIdl(unittest.TestCase):
  def test_basics(self):
    app = App(
      os.path.join("tests", "data", "sample.idl"),
      os.path.join("tests", "received.dom"),
      os.path.join("tests", "templates", "dom.mako"))
    app.run()



if __name__ == "__main__":
  unittest.main()
