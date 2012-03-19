# -*- coding: UTF-8 -*-

import model



ARRAY = 0
NULLABLE = 1



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
