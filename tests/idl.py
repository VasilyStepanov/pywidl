# -*- coding: UTF-8 -*-

import pywidl



def emitSimpleType(typedef):
  if typedef.type == pywidl.SimpleType.DOMSTRING:
    return "DOMString"
  elif typedef.type == pywidl.SimpleType.OBJECT:
    return "object"
  elif typedef.type == pywidl.SimpleType.DATE:
    return "Date"
  elif typedef.type == pywidl.SimpleType.BOOLEAN:
    return "boolean"
  elif typedef.type == pywidl.SimpleType.BYTE:
    return "byte"
  elif typedef.type == pywidl.SimpleType.OCTET:
    return "octet"
  elif typedef.type == pywidl.SimpleType.FLOAT:
    return "float"
  elif typedef.type == pywidl.SimpleType.DOUBLE:
    return "double"
  elif typedef.type == pywidl.SimpleType.VOID:
    return "void"
  elif typedef.type == pywidl.SimpleType.ANY:
    return "any"
  elif typedef.type == pywidl.SimpleType.SHORT:
    return "short"
  elif typedef.type == pywidl.SimpleType.UNSIGNED_SHORT:
    return "unsigned short"
  elif typedef.type == pywidl.SimpleType.LONG:
    return "long"
  elif typedef.type == pywidl.SimpleType.UNSIGNED_LONG:
    return "unsigned long"
  elif typedef.type == pywidl.SimpleType.LONG_LONG:
    return "long long"
  elif typedef.type == pywidl.SimpleType.UNSIGNED_LONG_LONG:
    return "unsigned long long"

  return "/* unknown simple type %s */" % typedef.type



def emitType(typedef):
  ret = None

  if isinstance(typedef, pywidl.SimpleType):
    ret = emitSimpleType(typedef)
  elif isinstance(typedef, pywidl.InterfaceType):
    ret = typedef.name
  elif isinstance(typedef, pywidl.Sequence):
    ret = "sequence<%s>" % emitType(typedef.t)
  elif isinstance(typedef, pywidl.Array):
    ret = "%s[]" % emitType(typedef.t)
  elif isinstance(typedef, pywidl.UnionType):
    ret = "(%s)" % " or ".join([emitType(t) for t in typedef.t])
  else:
    return "/* unknown type %s */" % type(typedef)

  if typedef.nullable:
    ret = "%s?" % ret

  return ret



def emitArgument(argument):
  if argument.extended_attributes:
    extended_attributes = "%s " % emitExtendedAttributes("",
      argument.extended_attributes)
  else:
    extended_attributes = ""

  type = emitType(argument.type)
  if argument.ellipsis: type = "%s..." % type

  a = "%(extended_attributes)s%(type)s %(name)s" % {
      "extended_attributes" : extended_attributes,
      "type" : type,
      "name" : argument.name,
    }

  if argument.optional:
    a = "optional %s" % a

  if argument.default:
    a = "%s=%s" % (a, emitValue(argument.default))

  return a



def emitArguments(arguments):
  return ", ".join([emitArgument(argument) for argument in arguments])



def emitExtendedAttributeValue(value):
  if not value.arguments:
    return value.name

  return "%s(%s)" % (value.name, emitArguments(value.arguments))



def emitExtendedAttribute(attribute):
  if not attribute.value:
    return attribute.name
  if not attribute.name:
    return emitExtendedAttributeValue(attribute.value)

  return "%s=%s" % ( \
    attribute.name,
    emitExtendedAttributeValue(attribute.value))



def emitExtendedAttributes(indent, attributes):
  if not attributes: return ""

  return "%s[%s]" % (indent, (",\n%s " % indent).join(
    [emitExtendedAttribute(attribute) for attribute in attributes]))



def renderExtendedAttributes(out, indent, attributes):
  if not attributes: return

  print >>out, "%s[%s]" % (indent, (",\n%s " % indent).join(
    [emitExtendedAttribute(attribute) for attribute in attributes]))



def renderAttribute(out, attribute):
  specifier = "attribute"
  if attribute.readonly: specifier = "readonly %s" % specifier
  if attribute.inherit: specifier = "inherit %s" % specifier
  if attribute.stringifier: specifier = "stringifier %s" % specifier


  renderExtendedAttributes(out, "  ", attribute.extended_attributes)
  print >>out, "  %(specifier)s %(type)s %(name)s;" % {
      "specifier" : specifier,
      "type" : emitType(attribute.type),
      "name" : attribute.name,
    }



def renderExceptionField(out, field):
  renderExtendedAttributes(out, "  ", field.extended_attributes)
  print >>out, "  %(type)s %(name)s;" % {
      "type" : emitType(field.type),
      "name" : field.name,
    }



def renderOperation(out, operation):
  qualifiers = []
  if operation.stringifier: qualifiers.append("stringifier")
  if operation.static: qualifiers.append("static")
  if operation.getter: qualifiers.append("getter")
  if operation.setter: qualifiers.append("setter")
  if operation.creator: qualifiers.append("creator")
  if operation.deleter: qualifiers.append("deleter")
  if operation.legacycaller: qualifiers.append("legacycaller")

  specifier = emitType(operation.return_type)
  if operation.name: specifier = "%s %s" % (specifier, operation.name)

  renderExtendedAttributes(out, "  ", operation.extended_attributes)
  print >>out, "  %(qualifiers)s%(specifier)s(%(arguments)s);" % {
      "qualifiers" : "".join([qualifier + " " for qualifier in qualifiers]),
      "specifier" : specifier,
      "arguments" : emitArguments(operation.arguments),
    }



def emitValue(value):
  if value.type == pywidl.Value.BOOLEAN:
    return value.value and "true" or "false"
  if value.type == pywidl.Value.INTEGER:
    return value.value
  if value.type == pywidl.Value.FLOAT:
    return value.value
  if value.type == pywidl.Value.NULL:
    return "null"
  if value.type == pywidl.Value.STRING:
    return "\"%s\"" % value.value
  else:
    return "/* unknown value type %s */" % value



def renderConst(out, const):
  renderExtendedAttributes(out, "  ", const.extended_attributes)
  print >>out, "  const %s %s = %s;" % ( \
    emitType(const.type), const.name, emitValue(const.value))



def renderInterfaceMember(out, member):
  if isinstance(member, pywidl.Attribute):
    renderAttribute(out, member)
  elif isinstance(member, pywidl.Operation):
    renderOperation(out, member)
  elif isinstance(member, pywidl.Const):
    renderConst(out, member)
  elif isinstance(member, pywidl.ExceptionField):
    renderExceptionField(out, member)
  else:
    print >>out, "  /* unknown interface member %s */" % type(member)



def renderDictionaryMember(out, member):
  renderExtendedAttributes(out, "  ", member.extended_attributes)

  m = "%s %s" % (emitType(member.type), member.name)

  if member.default:
    m = "%s=%s" % (m, emitValue(member.default))

  print >>out, "  %s;" % m



def renderInterface(out, interface):
  if interface.parent:
    declaration = "%s : %s" % (interface.name, interface.parent)
  else:
    declaration = "%s" % interface.name

  if interface.callback:
    definition = "callback interface"
  else:
    definition = "interface"

  renderExtendedAttributes(out, "", interface.extended_attributes)
  print >>out, "%s %s {" % (definition, declaration)

  for member in interface.members:
    renderInterfaceMember(out, member)

  print >>out, "};"



def renderPartialInterface(out, interface):
  renderExtendedAttributes(out, "", interface.extended_attributes)
  print >>out, "partial interface %s {" % interface.name

  for member in interface.members:
    renderInterfaceMember(out, member)

  print >>out, "};"



def renderException(out, exception):
  if exception.parent:
    declaration = "%s : %s" % (exception.name, exception.parent)
  else:
    declaration = "%s" % exception.name

  renderExtendedAttributes(out, "", exception.extended_attributes)
  print >>out, "exception %s {" % declaration

  for member in exception.members:
    renderInterfaceMember(out, member)

  print >>out, "};"



def renderImplementsStatement(out, implements):
  print >>out, "%s implements %s;" % ( \
    implements.interface, implements.functionality)



def renderTypedef(out, typedef):
  t = "%s %s" % (emitType(typedef.type), typedef.name)

  if typedef.type_extended_attributes: t = "%s %s" % ( \
    emitExtendedAttributes("", typedef.type_extended_attributes), t)

  renderExtendedAttributes(out, "", typedef.extended_attributes)
  print >>out, "typedef %s;" % t



def renderDictionary(out, dictionary):
  if dictionary.parent:
    declaration = "%s : %s" % (dictionary.name, dictionary.parent)
  else:
    declaration = "%s" % dictionary.name

  renderExtendedAttributes(out, "", dictionary.extended_attributes)
  print >>out, "dictionary %s {" % declaration

  for member in dictionary.members:
    renderDictionaryMember(out, member)

  print >>out, "};"



def renderCallback(out, callback):
  arguments = callback.arguments;

  renderExtendedAttributes(out, "", callback.extended_attributes)
  print >>out, "callback %s = %s (%s);" % ( \
    callback.name, emitType(callback.return_type), emitArguments(arguments))



def renderEnum(out, enum):
  values = ", ".join(["\"%s\"" % value for value in enum.values])

  renderExtendedAttributes(out, "", enum.extended_attributes)
  print >>out, "enum %s { %s };" % (enum.name, values)



def renderDefinition(out, definition):
  print >>out
  print >>out
  print >>out

  if isinstance(definition, pywidl.PartialInterface):
    renderPartialInterface(out, definition)
  elif isinstance(definition, pywidl.Interface):
    renderInterface(out, definition)
  elif isinstance(definition, pywidl.ImplementsStatement):
    renderImplementsStatement(out, definition)
  elif isinstance(definition, pywidl.Typedef):
    renderTypedef(out, definition)
  elif isinstance(definition, pywidl.Dictionary):
    renderDictionary(out, definition)
  elif isinstance(definition, pywidl.Callback):
    renderCallback(out, definition)
  elif isinstance(definition, pywidl.Enum):
    renderEnum(out, definition)
  elif isinstance(definition, pywidl.Exception):
    renderException(out, definition)
  else:
    print >>out, "/* unknown definition type %s */" % type(definition)



def render(definitions=[], source=None, output=None, template=None,
  template_type=None, **kwargs):

  with open(output, 'w') as out:
    print >>out, "// source: %s" % source
    print >>out, "// output: %s" % output
    print >>out, "// template: %s" % template
    print >>out, "// template_type: %d" % template_type

    for definition in definitions:
      renderDefinition(out, definition)
