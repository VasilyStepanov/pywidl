# -*- coding: UTF-8 -*-

from core import PyWIdlObject
from interface import *



class Definition(PyWIdlObject):
  iface = IDefinition



class Interface(Definition):
  iface = IInterface



class InterfaceMember(PyWIdlObject):
  iface = IInterfaceMember



class Attribute(InterfaceMember):
  iface = IAttribute



class Type(PyWIdlObject):
  iface = IType



class SingleType(Type):
  iface = ISingleType



class PrimitiveType(SingleType):
  iface = IPrimitiveType



class IntegerType(PrimitiveType):
  iface = IIntegerType
  unsigned = False



class Short(IntegerType):
  iface = IShort



class UnsignedShort(IntegerType):
  iface = IUnsignedShort



class Long(IntegerType):
  iface = ILong



class UnsignedLong(IntegerType):
  iface = IUnsignedLong



class LongLong(IntegerType):
  iface = ILongLong



class UnsignedLongLong(IntegerType):
  iface = IUnsignedLongLong



class Boolean(PrimitiveType):
  iface = IBoolean



class Byte(PrimitiveType):
  iface = IByte



class Octet(PrimitiveType):
  iface = IOctet



class Float(PrimitiveType):
  iface = IFloat



class Double(PrimitiveType):
  iface = IDouble



class DOMString(SingleType):
  iface = IDOMString



class InterfaceType(SingleType):
  iface = IInterfaceType



class Sequence(SingleType):
  iface = ISequence



class Object(SingleType):
  iface = IObject



class Date(SingleType):
  iface = IDate



class Any(Type):
  iface = IAny



class Array(Type):
  iface = IArray



class UnionType(Type):
  iface = IUnionType

  def _getName(self):
    return " Or ".join([t.name for t in self.t])

  name = property(_getName)



class ExtendedAttribute(PyWIdlObject):
  iface = IExtendedAttribute



class ExtendedAttributeValue(PyWIdlObject):
  iface = IExtendedAttributeValue
