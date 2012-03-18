# -*- coding: UTF-8 -*-

import ply.lex as lex

import os



tokens = (
  "integer",
  "float",
  "identifier",
  "string",
  "whitespace",
  "other",
)

t_integer = r"-?(0([0-7]*|[Xx][0-9A-Fa-f]+)|[1-9][0-9]*)"
t_identifier = r"[A-Z_a-z][0-9A-Z_a-z]*"
t_string = r"\"[^\"]*\""
t_whitespace = r"[\t\n\r ]+|[\t\n\r ]*((//.*|/\*.*?\*/)[\t\n\r ]*)+"



def t_error(t):
  print "Illegal character '%s'" % t.value[0]
  t.lexer.skip(1)



lexdir = os.path.dirname(__file__)
lex.lex(lextab="pywidl.lextab", outputdir=lexdir, optimize=1)
