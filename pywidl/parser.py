# -*- coding: UTF-8 -*-

from lexer import tokens

import ply.yacc as yacc

import os

def p_Definitions(p):
  "Definitions : identifier whitespace integer whitespace"
  p[0] = [p[1]] + [p[3]]



parsedir = os.path.dirname(__file__)
parser = yacc.yacc(outputdir=parsedir, debug=0)



def parse(source):
  return parser.parse(source)
