# -*- coding: UTF-8 -*-



class IPyWIdlObject(object):
  @classmethod
  def attributes(cls):
    for attr in dir(cls):
      if not attr: continue
      if attr[0] == '_': continue
      yield (attr, getattr(cls, attr))



class PyWIdlObject(object):
  iface = None

  def __init__(self, **kwargs):
    assert self.iface, "%s.iface must be defined" % self.__class__.__name__

    for attr, default_value in self.iface.attributes():
      if hasattr(self, attr): continue
      if hasattr(self.__class__, attr): continue
      value = kwargs.get(attr, default_value)
      setattr(self, attr, value)
