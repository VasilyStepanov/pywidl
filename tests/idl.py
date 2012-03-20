# -*- coding: UTF-8 -*-

import pywidl



def emitType(typedef):
  ret = None

  if isinstance(typedef, pywidl.Any):
    ret = "any"
  elif isinstance(typedef, pywidl.Array):
    ret = "%s[]" % emitType(typedef.t)
  else:
    return "/* unknown type %s */" % type(typedef)

  if typedef.nullable:
    ret = "%s?" % ret

  return ret



def renderAttribute(out, attribute):
  specifier = "attribute"
  if attribute.readonly: specifier = "readonly %s" % specifier
  if attribute.inherit: specifier = "inherit %s" % specifier


  print >>out, "  %(specifier)s %(type)s %(name)s;" % {
      "specifier" : specifier,
      "type" : emitType(attribute.type),
      "name" : attribute.name,
    }


def renderInterfaceMember(out, member):
  if isinstance(member, pywidl.Attribute):
    renderAttribute(out, member)
  else:
    print >>out, "/* unknown interface member %s */" % type(member)



def renderInterface(out, interface):
  if interface.parent:
    declaration = "%s : %s" % (interface.name, interface.parent)
  else:
    declaration = "%s" % interface.name


  print >>out, "interface %s {" % declaration

  for member in interface.members:
    renderInterfaceMember(out, member)

  print >>out, "};"


  
def renderDefinition(out, definition):
  print >>out
  print >>out
  print >>out

  if isinstance(definition, pywidl.Interface):
    renderInterface(out, definition)
  else:
    print >>out, "/* unknown definition type %s */" % type(definition)



def render(definitions=[], source=None, output=None,
  template=None, template_type=None, **kwargs):
  with open(output, 'w') as out:
    print >>out, "// source: %s" % source
    print >>out, "// output: %s" % output
    print >>out, "// template: %s" % template
    print >>out, "// template_type: %d" % template_type

    for definition in definitions:
      renderDefinition(out, definition)
