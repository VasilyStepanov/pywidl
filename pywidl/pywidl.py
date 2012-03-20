#!/usr/bin/python
# -*- coding: UTF-8 -*-

from grammar import parse

from mako.template import Template

import sys


def printUsage():
  print """USAGE: pywidl <options> source

  Options:
    -m, --mako
    -n, --native
    -o, --output FILE
    -t, --template FILE
"""



class App(object):
  NATIVE_TEMPLATE = 0
  MAKO_TEMPLATE = 1


  def __init__(self, source, output, template, template_type=NATIVE_TEMPLATE):
    self._source = source
    self._output = output
    self._template = template
    self._template_type = template_type

  
  def _parse(self):
    with open(self._source, 'r') as f:
      return parse(f.read())


  def _emitNative(self, definitions):
    exec("import %s as template" % self._template)
    template.render(
      definitions=definitions,
      source=self._source,
      output=self._output,
      template=self._template,
      template_type=self._template_type)


  def _emitMako(self, definitions):
    template = Template(filename=self._template)
    with open(self._output, 'w') as f:
      f.write(template.render(
        definitions=definitions,
        source=self._source,
        output=self._output,
        template=self._template,
        template_type=self._template_type))

  
  def _emit(self, definitions):
    if self._template_type == self.NATIVE_TEMPLATE:
      self._emitNative(definitions)
    elif self._template_type == self.MAKO_TEMPLATE:
      self._emitMako(definitions)
    else:
      raise ValueError("Unknown template type: %d" % self._template_type)


  def run(self):
    definitions = self._parse()
    self._emit(definitions)



def main():
  source = None
  output = None
  template = None
  template_type = App.NATIVE_TEMPLATE

  i = 1
  while i < len(sys.argv):
    arg = sys.argv[i]
    if arg == "-m" or arg == "--mako":
      template_type = App.MAKO_TEMPLATE
    elif arg == "-n" or arg == "--mako":
      template_type = App.NATIVE_TEMPLATE
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
