#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

def printUsage():
  print """USAGE: pywidl <options> source

  Options:
    -m, --mako
    -o, --output FILE
    -t, --template FILE
"""



class App(object):
  MAKO_TEMPLATE = 0


  def __init__(self, source, output, template, template_type):
    self._source = source
    self._output = output
    self._template = template
    self._template_type = template_type


  def run(self):
    print "hello world"



def main():
  source = None
  output = None
  template = None
  template_type = App.MAKO_TEMPLATE

  i = 1
  while i < len(sys.argv):
    arg = sys.argv[i]
    if arg == "-m" or arg == "--mako":
      template_type = App.MAKO_TEMPLATE
    elif arg == "-o" or arg == "--output":
      i += 1
      output = sys.argv[i]
    elif arg == "-t" or arg == "--template":
      i += 1
      template = sys.argv[i]
    else:
      source = arg
    i += 1

  if source is None or output is None \
  or template is None or template_type is None:
    printUsage()
    return

  app = App(source, output, template, template_type)
  return app.run()



if __name__ == "__main__":
  main()
