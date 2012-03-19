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



class IAny(ISingleType):
  name = "Any"


class IArray(IType):
  name = "Array"
  t = None
