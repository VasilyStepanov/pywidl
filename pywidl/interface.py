# -*- coding: UTF-8 -*-



class IObject(object):
  @classmethod
  def attributes(cls):
    for attr in dir(cls):
      if not attr: continue
      if attr[0] == '_': continue
      yield (attr, getattr(cls, attr))



class IDefinition(IObject):
  name = None
  extended_attributes = []



class IInterface(IDefinition):
  parent = None
