# -*- coding: UTF-8 -*-



class IObject(object):
  @classmethod
  def attributes(cls):
    for attr in dir(cls):
      if not attr: continue
      if attr[0] == '_': continue
      yield (attr, getattr(cls, attr))



class Object(object):
  iface = None

  def __init__(self, **kwargs):
    assert self.iface, "%s.iface must be defined" % self.__class__.__name__
    for attr, default_value in self.iface.attributes():
      value = kwargs.get(attr, default_value)
      setattr(self, attr, value)
