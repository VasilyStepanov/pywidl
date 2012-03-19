# -*- coding: UTF-8 -*-

from core import IObject



class IDefinition(IObject):
  name = None
  extended_attributes = []



class IInterface(IDefinition):
  parent = None
  members = []



class IInterfaceMember(IObject):
  name = None



class IAttribute(IInterfaceMember):
  inherit = False
  readonly = False
  type = None



class IType(IObject):
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



class IAny(ISingleType):
  name = "Any"


class IArray(IType):
  name = "Array"
  t = None
