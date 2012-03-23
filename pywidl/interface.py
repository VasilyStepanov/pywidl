# -*- coding: UTF-8 -*-

from core import IPyWIdlObject



class IDefinition(IPyWIdlObject):
  name = None
  extended_attributes = []



class IInterface(IDefinition):
  parent = None
  members = []



class IInterfaceMember(IPyWIdlObject):
  name = None
  extended_attributes = []



class IAttribute(IInterfaceMember):
  stringifier = False
  inherit = False
  readonly = False
  type = None



class IType(IPyWIdlObject):
  name = None
  nullable = None



class ISingleType(IType):
  pass



class IPrimitiveType(ISingleType):
  pass



class IIntegerType(IPrimitiveType):
  pass



class IShort(IIntegerType):
  name = "Short"



class IUnsignedShort(IIntegerType):
  name = "UnsignedShort"



class ILong(IIntegerType):
  name = "Long"



class IUnsignedLong(IIntegerType):
  name = "UnsignedLong"



class ILongLong(IIntegerType):
  name = "LongLong"



class IUnsignedLongLong(IIntegerType):
  name = "UnsignedLongLong"



class IBoolean(IPrimitiveType):
  name = "Boolean"



class IByte(IPrimitiveType):
  name = "Byte"



class IOctet(IPrimitiveType):
  name = "Octet"



class IFloat(IPrimitiveType):
  name = "Float"



class IDouble(IPrimitiveType):
  name = "Double"



class IDOMString(ISingleType):
  name = "String"



class IInterfaceType(ISingleType):
  pass



class ISequence(ISingleType):
  name = "Sequence"
  t = None



class IObject(ISingleType):
  name = "Object"



class IDate(ISingleType):
  name = "Date"



class IAny(ISingleType):
  name = "Any"



class IArray(IType):
  name = "Array"
  t = None



class IVoid(IType):
  name = "void"



class IUnionType(IType):
  t = []



class IExtendedAttribute(IPyWIdlObject):
  name = None
  value = None



class IExtendedAttributeValue(IPyWIdlObject):
  name = None
  arguments = []



class IArgument(IPyWIdlObject):
  type = None
  name = None
  optional = False
  default = None
  ellipsis = False
  extended_attributes = []



class IOperation(IPyWIdlObject):
  stringifier = False
  name = None
  return_type = None
  arguments = []
  extended_attributes = []
  static = False
  getter = False
  setter = False
  creator = False
  deleter = False
  legacycaller = False



class IConst(IInterfaceMember):
  name = None
  type = None
  value = None
  extended_attributes = []



class IValue(IPyWIdlObject):
  value = None



class IBooleanValue(IValue):
  pass



class IIntegerValue(IValue):
  pass



class IFloatValue(IValue):
  pass



class INullValue(IValue):
  pass



class IStringValue(IValue):
  pass
