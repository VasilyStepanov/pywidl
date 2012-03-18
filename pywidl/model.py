# -*- coding: UTF-8 -*-

from interface import IDefinition
from interface import IInterface



class Object(object):
  iface = None

  def __init__(self, **kwargs):
    assert self.iface, "%s.iface must be defined" % self.__class__.__name__
    for attr, default_value in self.iface.attributes():
      value = kwargs.get(attr, default_value)
      setattr(self, attr, value)



class Definition(Object):
  iface = IDefinition



class Interface(Definition):
  iface = IInterface
