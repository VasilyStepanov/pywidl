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
# DictionaryMember
# ExtendedAttribute
# ExtendedAttributeValue
# Argument
# Type
#   DOMString
#   InterfaceType
#   Sequence
#   Object
#   Date
#   Boolean
#   Byte
#   Octet
#   Float
#   Double
#   Array
#   Void
#   Any
#   Short
#   UnsignedShort
#   Long
#   UnsignedLong
#   LongLong
#   UnsignedLongLong
#   UnionType
# Value



class Definition(object):

  def __init__(self, name=None, extended_attributes=[], **kwargs):

    super(Definition, self).__init__(**kwargs)
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

  def __init__(self, name=None, extended_attributes=[], **kwargs):

    super(InterfaceMember, self).__init__(**kwargs)
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



class DictionaryMember(object):

  def __init__(self, type=None, name=None, default=None,
    extended_attributes=[], **kwargs):

    super(DictionaryMember, self).__init__(**kwargs)
    self.type = type
    self.name = name
    self.default = default
    self.extended_attributes = extended_attributes



class ExtendedAttribute(object):

  def __init__(self, name=None, value=None, **kwargs):

    super(ExtendedAttribute, self).__init__(**kwargs)
    self.name = name
    self.value = value



class ExtendedAttributeValue(object):

  def __init__(self, name=None, arguments=[], **kwargs):

    super(ExtendedAttributeValue, self).__init__(**kwargs)
    self.name = name
    self.arguments = arguments



class Argument(object):

  def __init__(self, type=None, name=None, optional=False, default=None,
    ellipsis=False, extended_attributes=[], **kwargs):

    super(Argument, self).__init__(**kwargs)
    self.type = type
    self.name = name
    self.optional = optional
    self.default = default
    self.ellipsis = ellipsis
    self.extended_attributes = extended_attributes



class Type(object):

  def __init__(self, name=None, nullable=False, **kwargs):

    super(Type, self).__init__(**kwargs)
    self.name = name
    self.nullable = nullable



class DOMString(Type):

  def __init__(self, **kwargs):

    super(DOMString, self).__init__(**kwargs)
    self.name = "DOMString"



class InterfaceType(Type):

  def __init__(self, **kwargs):

    super(InterfaceType, self).__init__(**kwargs)



class Sequence(Type):

  def __init__(self, t=None, **kwargs):

    super(Sequence, self).__init__(**kwargs)
    self.name = "Sequence"
    self.t = t



class Object(Type):

  def __init__(self, **kwargs):

    super(Object, self).__init__(**kwargs)
    self.name = "Object"



class Date(Type):

  def __init__(self, **kwargs):

    super(Date, self).__init__(**kwargs)
    self.name = "Date"



class Boolean(Type):

  def __init__(self, **kwargs):

    super(Boolean, self).__init__(**kwargs)
    self.name = "Boolean"



class Byte(Type):

  def __init__(self, **kwargs):

    super(Byte, self).__init__(**kwargs)
    self.name = "Byte"



class Octet(Type):

  def __init__(self, **kwargs):

    super(Octet, self).__init__(**kwargs)
    self.name = "Octet"



class Float(Type):

  def __init__(self, **kwargs):

    super(Float, self).__init__(**kwargs)
    self.name = "Float"



class Double(Type):

  def __init__(self, **kwargs):

    super(Double, self).__init__(**kwargs)
    self.name = "Double"



class Array(Type):

  def __init__(self, t=None, **kwargs):

    super(Array, self).__init__(**kwargs)
    self.name = "Array"
    self.t = t



class Void(Type):
  pass



class Any(Type):

  def __init__(self, **kwargs):

    super(Any, self).__init__(**kwargs)
    self.name = "Any"



class Short(Type):

  def __init__(self, **kwargs):

    super(Short, self).__init__(**kwargs)
    self.name = "Short"



class UnsignedShort(Type):

  def __init__(self, **kwargs):

    super(UnsignedShort, self).__init__(**kwargs)
    self.name = "UnsignedShort"



class Long(Type):

  def __init__(self, **kwargs):

    super(Long, self).__init__(**kwargs)
    self.name = "Long"



class UnsignedLong(Type):

  def __init__(self, **kwargs):

    super(UnsignedLong, self).__init__(**kwargs)
    self.name = "UnsignedLong"



class LongLong(Type):

  def __init__(self, **kwargs):

    super(LongLong, self).__init__(**kwargs)
    self.name = "LongLong"



class UnsignedLongLong(Type):

  def __init__(self, **kwargs):

    super(UnsignedLongLong, self).__init__(**kwargs)
    self.name = "UnsignedLongLong"



class UnionType(Type):

  def __init__(self, t=[], **kwargs):

    super(UnionType, self).__init__(**kwargs)
    self.name = property(self._getName)
    self.t = t


  def _getName(self):
    return " Or ".join([t.name for t in self.t])



class Value(object):
  BOOLEAN = 0
  INTEGER = 1
  FLOAT = 2
  NULL = 3
  STRING = 4

  def __init__(self, type=None, value=None, **kwargs):

    super(Value, self).__init__(**kwargs)
    self.type = type
    self.value = value
