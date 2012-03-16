#!/usr/bin/python

from pywidl.pywidl import App

import unittest

from difflib import context_diff
import os.path
import sys



class TestPyWIdl(unittest.TestCase):
  def _match(self, fromfile, tofile):
    diff = context_diff(open(fromfile).readlines(), open(tofile).readlines(),
      fromfile=fromfile, tofile=tofile)

    diff_clean = True
    for line in diff:
      if diff_clean: print
      diff_clean = False
      sys.stdout.write(line)

    return diff_clean


  def _buildDom(self, source):
    src = os.path.join("tests", "data", source)
    eta = os.path.join("tests", "data", "%s.dom" % source.rsplit('.', 1)[0])
    rcv = os.path.join("tests", "received.dom")

    app = App(src, rcv,
      os.path.join("tests", "templates", "dom.mako"))
    app.run()

    self.assertTrue(self._match(eta, rcv))


  def test_basics(self):
    self._buildDom("sample.idl")



if __name__ == "__main__":
  unittest.main()
