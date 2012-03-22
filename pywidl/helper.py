# -*- coding: UTF-8 -*-

import model



ARRAY = 0
NULLABLE = 1

SHORT = 0
LONG = 1
LONGLONG = 2

GETTER = 0
SETTER = 1
CREATOR = 2
DELETER = 3
LEGACYCALLER = 4
STATIC = 5



def unwrapTypeSuffix(type, suffix):
  if not suffix: return type

  specifier = suffix.pop()
  if specifier == ARRAY:
    return model.Array(t=unwrapTypeSuffix(type, suffix))

  if specifier == NULLABLE:
    unwrapped = unwrapTypeSuffix(type, suffix)
    unwrapped.nullable = True
    return unwrapped

  raise RuntimeError("unknown specifier: %s" % specifier)



def unwrapIntegerType(unsigned, type):
  if type == SHORT:
    return unsigned and model.UnsignedShort() or model.Short()
  if type == LONG:
    return unsigned and model.UnsignedLong() or model.Long()
  if type == LONGLONG:
    return unsigned and model.UnsignedLongLong() or model.LongLong()
  raise RuntimeError("unknown type: %s" % type)



def applyQualifiers(operation, qualifiers):
  for qualifier in qualifiers:
    if qualifier == GETTER:
      operation.getter = True
    elif qualifier == SETTER:
      operation.setter = True
    elif qualifier == CREATOR:
      operation.creator = True
    elif qualifier == DELETER:
      operation.deleter = True
    elif qualifier == LEGACYCALLER:
      operation.legacycaller = True
    elif qualifier == STATIC:
      operation.static = True
    else:
      raise RuntimeError("unknown qualifier: %s" % qualifier)
  return operation
