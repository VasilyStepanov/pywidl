# -*- coding: UTF-8 -*-

import ply.lex as lex

import os
import sys



literals = "{};:,=()[].<>?"



tokens = [
  "INTEGER",
  "FLOAT",
  "IDENTIFIER",
  "STRING",
  "ELLIPSIS",
]



keywords = (
  "Date",
  "DOMString",
  "any",
  "attribute",
  "boolean",
  "byte",
  "callback",
  "const",
  "creator",
  "deleter",
  "dictionary",
  "double",
  "enum",
  "exception",
  "false",
  "float",
  "getter",
  "implements",
  "inherit",
  "interface",
  "legacycaller",
  "long",
  "null",
  "object",
  "octet",
  "optional",
  "or",
  "partial",
  "readonly",
  "sequence",
  "setter",
  "short",
  "static",
  "stringifier",
  "true",
  "typedef",
  "unsigned",
  "void",
)



tokens.extend(keywords)



t_ignore = ' \t'
t_ignore_line_comment = r'//.*'


t_INTEGER = r"-?(0([0-7]*|[Xx][0-9A-Fa-f]+)|[1-9][0-9]*)"
t_FLOAT = r"-?(([0-9]+\.[0-9]*|[0-9]*\.[0-9]+)([Ee][+-]?[0-9]+)?|[0-9]+[Ee][+-]?[0-9]+)"
t_ELLIPSIS = r"\.\.\."



def t_IDENTIFIER(t):
  r"[A-Z_a-z][0-9A-Z_a-z]*"
  if t.value in keywords:
    t.type = t.value
  return t



def t_STRING(t):
  r"\"[^\"]*\""
  t.value = t.value[1:-1]
  return t



def t_ignore_block_comment(t):
  r"\/\*[^*]*\*+([^/*][^*]*\*+)*\/"
  t.lexer.lineno += t.value.count('\n')



def t_newline(t):
  r"\n+"
  t.lexer.lineno += len(t.value)



def t_error(t):
  print >>sys.stderr, "Illegal character '%s'" % t.value[0]
  t.lexer.skip(1)



lexdir = os.path.dirname(__file__)
lex.lex(lextab="pywidl.lextab", outputdir=lexdir, optimize=0)
