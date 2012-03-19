# -*- coding: UTF-8 -*-

from core import Object
from interface import *



class Definition(Object):
  iface = IDefinition



class Interface(Definition):
  iface = IInterface



class InterfaceMember(Object):
  iface = IInterfaceMember



class Attribute(InterfaceMember):
  iface = IAttribute



class Type(Object):
  iface = IType



class SingleType(Type):
  iface = ISingleType



class Any(Type):
  iface = IAny



class Array(Type):
  iface = IArray
