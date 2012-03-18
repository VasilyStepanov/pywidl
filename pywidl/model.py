# -*- coding: UTF-8 -*-



class Definition(object):
  def __init__(self, name):
    self.name = name
    self.extended_attributes = []



class Interface(Definition):
  def __init__(self, name, parent):
    super(Interface, self).__init__(name)
    self.parent = parent
