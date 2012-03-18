# -*- coding: UTF-8 -*-

from core import Object
from interface import IDefinition
from interface import IInterface



class Definition(Object):
  iface = IDefinition



class Interface(Definition):
  iface = IInterface
