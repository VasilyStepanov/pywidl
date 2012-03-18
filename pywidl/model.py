# -*- coding: UTF-8 -*-

from core import Object
from interface import IDefinition
from interface import IInterface
from interface import IInterfaceMember
from interface import IAttribute



class Definition(Object):
  iface = IDefinition



class Interface(Definition):
  iface = IInterface



class InterfaceMember(Object):
  iface = IInterfaceMember



class Attribute(InterfaceMember):
  iface = IAttribute
