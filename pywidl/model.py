# -*- coding: UTF-8 -*-



class PyWIdlObject(object):
  pass



class Definition(PyWIdlObject):

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



class InterfaceMember(PyWIdlObject):

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



class Type(PyWIdlObject):

  def __init__(self, name=None, nullable=False, **kwargs):

    super(Type, self).__init__(**kwargs)
    self.name = name
    self.nullable = nullable



class SingleType(Type):

  def __init__(self, **kwargs):

    super(SingleType, self).__init__(**kwargs)



class PrimitiveType(SingleType):

  def __init__(self, **kwargs):

    super(PrimitiveType, self).__init__(**kwargs)



class IntegerType(PrimitiveType):

  def __init__(self, **kwargs):

    super(IntegerType, self).__init__(**kwargs)



class Short(IntegerType):

  def __init__(self, **kwargs):

    super(Short, self).__init__(**kwargs)
    self.name = "Short"



class UnsignedShort(IntegerType):

  def __init__(self, **kwargs):

    super(UnsignedShort, self).__init__(**kwargs)
    self.name = "UnsignedShort"



class Long(IntegerType):

  def __init__(self, **kwargs):

    super(Long, self).__init__(**kwargs)
    self.name = "Long"



class UnsignedLong(IntegerType):

  def __init__(self, **kwargs):

    super(UnsignedLong, self).__init__(**kwargs)
    self.name = "UnsignedLong"



class LongLong(IntegerType):

  def __init__(self, **kwargs):

    super(LongLong, self).__init__(**kwargs)
    self.name = "LongLong"



class UnsignedLongLong(IntegerType):

  def __init__(self, **kwargs):

    super(UnsignedLongLong, self).__init__(**kwargs)
    self.name = "UnsignedLongLong"



class Boolean(PrimitiveType):

  def __init__(self, **kwargs):

    super(Boolean, self).__init__(**kwargs)
    self.name = "Boolean"



class Byte(PrimitiveType):

  def __init__(self, **kwargs):

    super(Byte, self).__init__(**kwargs)
    self.name = "Byte"



class Octet(PrimitiveType):

  def __init__(self, **kwargs):

    super(Octet, self).__init__(**kwargs)
    self.name = "Octet"



class Float(PrimitiveType):

  def __init__(self, **kwargs):

    super(Float, self).__init__(**kwargs)
    self.name = "Float"



class Double(PrimitiveType):

  def __init__(self, **kwargs):

    super(Double, self).__init__(**kwargs)
    self.name = "Double"



class DOMString(SingleType):

  def __init__(self, **kwargs):

    super(DOMString, self).__init__(**kwargs)
    self.name = "DOMString"



class InterfaceType(SingleType):

  def __init__(self, **kwargs):

    super(InterfaceType, self).__init__(**kwargs)



class Sequence(SingleType):

  def __init__(self, t=None, **kwargs):

    super(Sequence, self).__init__(**kwargs)
    self.name = "Sequence"
    self.t = t



class Object(SingleType):

  def __init__(self, **kwargs):

    super(Object, self).__init__(**kwargs)
    self.name = "Object"



class Date(SingleType):

  def __init__(self, **kwargs):

    super(Date, self).__init__(**kwargs)
    self.name = "Date"



class Any(Type):

  def __init__(self, **kwargs):

    super(Any, self).__init__(**kwargs)
    self.name = "Any"



class Array(Type):

  def __init__(self, t=None, **kwargs):

    super(Array, self).__init__(**kwargs)
    self.name = "Array"
    self.t = t



class Void(Type):
  pass



class UnionType(Type):

  def __init__(self, t=[], **kwargs):

    super(UnionType, self).__init__(**kwargs)
    self.name = property(self._getName)
    self.t = t


  def _getName(self):
    return " Or ".join([t.name for t in self.t])



class ExtendedAttribute(PyWIdlObject):

  def __init__(self, name=None, value=None, **kwargs):

    super(ExtendedAttribute, self).__init__(**kwargs)
    self.name = name
    self.value = value



class ExtendedAttributeValue(PyWIdlObject):

  def __init__(self, name=None, arguments=[], **kwargs):

    super(ExtendedAttributeValue, self).__init__(**kwargs)
    self.name = name
    self.arguments = arguments




class Argument(PyWIdlObject):

  def __init__(self, type=None, name=None, optional=False, default=None,
    ellipsis=False, extended_attributes=[], **kwargs):

    super(Argument, self).__init__(**kwargs)
    self.type = type
    self.name = name
    self.optional = optional
    self.default = default
    self.ellipsis = ellipsis
    self.extended_attributes = extended_attributes



class Operation(PyWIdlObject):

  def __init__(self, stringifier=None, name=None, return_type=None,
    arguments=[], extended_attributes=[], static=False, getter=False,
    setter=False, creator=False, deleter=False, legacycaller=False,
    **kwargs):

    super(Operation, self).__init__(**kwargs)
    self.stringifier = stringifier
    self.name = name
    self.return_type = return_type
    self.arguments = arguments
    self.extended_attributes = extended_attributes
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



class Value(PyWIdlObject):

  def __init__(self, value=None, **kwargs):

    super(Value, self).__init__(**kwargs)
    self.value = value



class BooleanValue(Value):
  pass



class IntegerValue(Value):
  pass



class FloatValue(Value):
  pass



class NullValue(Value):
  pass



class StringValue(Value):
  pass



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



class DictionaryMember(PyWIdlObject):

  def __init__(self, type=None, name=None, default=None,
    extended_attributes=[], **kwargs):

    super(DictionaryMember, self).__init__(**kwargs)
    self.type = type
    self.name = name
    self.default = default
    self.extended_attributes = extended_attributes



class Callback(Definition):
  
  def __init__(self, return_type=None, arguments=[], **kwargs):

    super(Callback, self).__init__(**kwargs)
    self.return_type = return_type
    self.arguments = arguments
