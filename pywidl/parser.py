# -*- coding: UTF-8 -*-

from lexer import tokens

import ply.yacc as yacc

def p_Definitions(p):
  "Definitions : identifier whitespace integer whitespace"
  p[0] = [p[1]] + [p[3]]



parser = yacc.yacc()



def parse(source):
  return parser.parse(source)
