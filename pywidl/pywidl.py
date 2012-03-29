#!/usr/bin/python
# -*- coding: UTF-8 -*-

from grammar import parse

from mako.template import Template

import sys

name = "pywidl"
version = "0.0"


def printUsage():
  print """USAGE: pywidl <options> source

  Options:
    -v, --version
    -n, --native
    -m, --mako
    -o, --output FILE
    -t, --template FILE
"""



def printVersion():
  print "%s %s" % (name, version)



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



def appArgs():
  args = {}
  for i in range(1, len(sys.argv)):
    arg = sys.argv[i]
    if arg == "-v" or arg == "--version":
      key = "version"
      value = None
    elif arg == "-m" or arg == "--mako":
      key = "template_type"
      value = App.MAKO_TEMPLATE
    elif arg == "-n" or arg == "--native":
      key = "template_type"
      value = App.NATIVE_TEMPLATE
    elif arg == "-o" or arg == "--output" and i < len(sys.argv) - 1:
      i += 1
      key = "output"
      value = sys.argv[i]
    elif arg == "-t" or arg == "--template" and i < len(sys.argv) - 1:
      i += 1
      key = "template"
      value = sys.argv[i]
    else:
      key = "source"
      value = arg
    args[key] = value
  return args



def main():
  app_args = appArgs()

  if "version" in app_args:
    printVersion()
    return

  source = app_args.get("source", None)
  output = app_args.get("output", None)
  template = app_args.get("template", None)
  template_type = app_args.get("template_type", App.NATIVE_TEMPLATE)

  if source is None or output is None \
  or template is None or template_type is None:
    printUsage()
    return

  app = App(source, output, template, template_type)
  return app.run()



if __name__ == "__main__":
  main()
