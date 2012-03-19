# -*- coding: UTF-8 -*-

from core import Object
from interface import *



class Definition(Object):
  iface = IDefinition



class Interface(Definition):
  iface = IInterface



class InterfaceMember(Object):
  iface = IInterfaceMember



class Attribute(InterfaceMember):
  iface = IAttribute



class Type(Object):
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



class Any(Type):
  iface = IAny



class Array(Type):
  iface = IArray
