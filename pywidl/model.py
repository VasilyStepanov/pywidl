# -*- coding: UTF-8 -*-

# Definition
#   Inteface
#   PartialInterface
#   ImplementsStatement
#   Typedef
#   Dictionary
#   Callback
#   Enum
#   Exception
# InterfaceMember
#   Attribute
#   Operation
#   Const
#   ExceptionField
# OperationArgument
# DictionaryMember
# ExtendedAttribute
# ExtendedAttributeValue
# Type
#   SimpleType
#   InterfaceType
#   Sequence
#   Array
#   UnionType
# Value



class Definition(object):

  def __init__(self, name=None, extended_attributes=[]):

    super(Definition, self).__init__()
    self.name = name
    self.extended_attributes = extended_attributes



class Interface(Definition):

  def __init__(self, callback=False, parent=None, members=[], **kwargs):

    super(Interface, self).__init__(**kwargs)
    self.callback = callback
    self.parent = parent
    self.members = members



class PartialInterface(Definition):

  def __init__(self, members=[], **kwargs):

    super(PartialInterface, self).__init__(**kwargs)
    self.members = members



class ImplementsStatement(Definition):

  def __init__(self, interface=None, functionality=None, **kwargs):

    super(ImplementsStatement, self).__init__(**kwargs)
    self.interface = interface
    self.functionality = functionality



class Typedef(Definition):

  def __init__(self, type_extended_attributes=[], type=None, **kwargs):

    super(Typedef, self).__init__(**kwargs)
    self.type = type
    self.type_extended_attributes= type_extended_attributes



class Dictionary(Definition):

  def __init__(self, parent=None, members=[], **kwargs):

    super(Dictionary, self).__init__(**kwargs)
    self.parent = parent
    self.members = members



class Callback(Definition):
  
  def __init__(self, return_type=None, arguments=[], **kwargs):

    super(Callback, self).__init__(**kwargs)
    self.return_type = return_type
    self.arguments = arguments



class Enum(Definition):

  def __init__(self, values=[], **kwargs):

    super(Enum, self).__init__(**kwargs)
    self.values = values



class Exception(Definition):

  def __init__(self, parent=None, members=[], **kwargs):

    super(Exception, self).__init__(**kwargs)
    self.parent = parent
    self.members = members



class InterfaceMember(object):

  def __init__(self, name=None, extended_attributes=[]):

    super(InterfaceMember, self).__init__()
    self.name = name
    self.extended_attributes = extended_attributes



class Attribute(InterfaceMember):

  def __init__(self, stringifier=False, inherit=False, readonly=False,
    type=None, **kwargs):

    super(Attribute, self).__init__(**kwargs)
    self.stringifier = stringifier
    self.inherit = inherit
    self.readonly = readonly
    self.type = type



class Operation(InterfaceMember):

  def __init__(self, stringifier=None, return_type=None, arguments=[],
    static=False, getter=False, setter=False, creator=False, deleter=False,
    legacycaller=False, **kwargs):

    super(Operation, self).__init__(**kwargs)
    self.stringifier = stringifier
    self.return_type = return_type
    self.arguments = arguments
    self.static = static
    self.getter = getter
    self.setter = setter
    self.creator = creator
    self.deleter = deleter
    self.legacycaller = legacycaller



class Const(InterfaceMember):

  def __init__(self, type=None, value=None, **kwargs):

    super(Const, self).__init__(**kwargs)
    self.type = type
    self.value = value



class ExceptionField(InterfaceMember):

  def __init__(self, type=None, **kwargs):

    super(ExceptionField, self).__init__(**kwargs)
    self.type = type



class OperationArgument(object):

  def __init__(self, type=None, name=None, optional=False, default=None,
    ellipsis=False, extended_attributes=[]):

    super(OperationArgument, self).__init__()
    self.type = type
    self.name = name
    self.optional = optional
    self.default = default
    self.ellipsis = ellipsis
    self.extended_attributes = extended_attributes



class DictionaryMember(object):

  def __init__(self, type=None, name=None, default=None,
    extended_attributes=[]):

    super(DictionaryMember, self).__init__()
    self.type = type
    self.name = name
    self.default = default
    self.extended_attributes = extended_attributes



class ExtendedAttribute(object):

  def __init__(self, name=None, value=None):

    super(ExtendedAttribute, self).__init__()
    self.name = name
    self.value = value



class ExtendedAttributeValue(object):

  def __init__(self, name=None, arguments=[]):

    super(ExtendedAttributeValue, self).__init__()
    self.name = name
    self.arguments = arguments



class Type(object):

  def __init__(self, nullable=False):

    super(Type, self).__init__()
    self.nullable = nullable



class SimpleType(Type):
  DOMSTRING = 0
  OBJECT = 1
  DATE = 2
  BOOLEAN = 3
  BYTE = 4
  OCTET = 5
  FLOAT = 6
  DOUBLE = 7
  VOID = 8
  ANY = 9
  SHORT = 10
  UNSIGNED_SHORT = 11
  LONG = 12
  UNSIGNED_LONG = 13
  LONG_LONG = 14
  UNSIGNED_LONG_LONG = 15

  def __init__(self, type=None, **kwargs):

    super(SimpleType, self).__init__(**kwargs)
    self.type = type



class InterfaceType(Type):

  def __init__(self, name=None, **kwargs):

    super(InterfaceType, self).__init__(**kwargs)
    self.name = name



class Sequence(Type):

  def __init__(self, t=None, **kwargs):

    super(Sequence, self).__init__(**kwargs)
    self.t = t



class Array(Type):

  def __init__(self, t=None, **kwargs):

    super(Array, self).__init__(**kwargs)
    self.t = t



class UnionType(Type):

  def __init__(self, t=[], **kwargs):

    super(UnionType, self).__init__(**kwargs)
    self.t = t



class Value(object):
  BOOLEAN = 0
  INTEGER = 1
  FLOAT = 2
  NULL = 3
  STRING = 4

  def __init__(self, type=None, value=None):

    super(Value, self).__init__()
    self.type = type
    self.value = value
