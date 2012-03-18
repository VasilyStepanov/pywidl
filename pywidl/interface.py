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
