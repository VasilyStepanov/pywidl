# -*- coding: UTF-8 -*-

from lexis import *
import model
import helper

import ply.yacc as yacc

import os



# 1 TODO
def p_Definitions(p):
  """Definitions : Definitions ExtendedAttributeList Definition"""
  p[0] = p[1] + [p[3]]



# 1
def p_Definitions_empty(p):
  """Definitions :"""
  p[0] = []



# 2
def p_Definition(p):
  """Definition : CallbackOrInterface
                | PartialInterface
                | Dictionary
                | Exception
                | Enum
                | Typedef
                | ImplementsStatement
  """
  p[0] = p[1]



# 3 TODO
def p_CallbackOrInterface_callback(p):
  """CallbackOrInterface : callback CallbackRestOrInterface"""



# 3
def p_CallbackOrInterface_interface(p):
  """CallbackOrInterface : Interface"""
  p[0] = p[1]



# 4 TODO
def p_CallbackRestOrInterface(p):
  """CallbackRestOrInterface : CallbackRest
                             | Interface
  """



# 5
def p_Interface(p):
  """Interface : interface IDENTIFIER Inheritance "{" InterfaceMembers "}" ";"
  """
  p[0] = model.Interface(name=p[2], parent=p[3], members=p[5])



# 6 TODO
def p_PartialInterface(p):
  """PartialInterface : partial interface IDENTIFIER "{" InterfaceMembers "}" ";"
  """



# 7 TODO
def p_InterfaceMembers(p):
  """InterfaceMembers : InterfaceMembers ExtendedAttributeList InterfaceMember
  """
  p[0] = p[1] + [p[3]]



# 7
def p_InterfaceMembers_empty(p):
  """InterfaceMembers :"""
  p[0] = []



# 8
def p_InterfaceMember(p):
  """InterfaceMember : Const
                     | AttributeOrOperation
  """
  p[0] = p[1]



# 9 TODO
def p_Dictionary(p):
  """Dictionary : dictionary IDENTIFIER Inheritance "{" DictionaryMembers "}" ";"
  """



# 10 TODO
def p_DictionaryMembers(p):
  """DictionaryMembers : ExtendedAttributeList DictionaryMember DictionaryMembers"""



# 10 TODO
def p_DictionaryMembers_empty(p):
  """DictionaryMembers :"""



# 11 TODO
def p_DictionaryMember(p):
  """DictionaryMember : Type IDENTIFIER Default ";"
  """



# 12 TODO
def p_Default(p):
  """Default : "=" DefaultValue"""



# 12 TODO
def p_Default_empty(p):
  """Default :"""



# 13 TODO
def p_DefaultValue(p):
  """DefaultValue : ConstValue
                  | STRING
                  |
  """



# 14 TODO
def p_Exception(p):
  """Exception : exception IDENTIFIER Inheritance "{" ExceptionMembers "}" ";"
  """



# 15 TODO
def p_ExceptionMembers(p):
  """ExceptionMembers : ExtendedAttributeList ExceptionMember ExceptionMembers
                      |
  """



# 16
def p_Inheritance(p):
  """Inheritance : ":" IDENTIFIER"""
  p[0] = p[2]



# 16
def p_Inheritance_empty(p):
  """Inheritance :"""
  p[0] = None



# 17 TODO
def p_Enum(p):
  """Enum : enum IDENTIFIER "{" EnumValueList "}" ";"
  """



# 18 TODO
def p_EnumValueList(p):
  """EnumValueList : STRING EnumValues"""



# 19 TODO
def p_EnumValues(p):
  """EnumValues : "," STRING EnumValues
                |
  """



# 20 TODO
def p_CallbackRest(p):
  """CallbackRest : IDENTIFIER "=" ReturnType "(" ArgumentList ")" ";"
  """



# 21 TODO
def p_Typedef(p):
  """Typedef : typedef ExtendedAttributeList Type IDENTIFIER ";"
  """



# 22 TODO
def p_ImplementsStatement(p):
  """ImplementsStatement : IDENTIFIER implements IDENTIFIER ";"
  """



# 23 TODO
def p_Const(p):
  """Const : const ConstType IDENTIFIER "=" ConstValue ";"
  """



# 24 TODO
def p_ConstValue(p):
  """ConstValue : BooleanLiteral
                | INTEGER
                | FLOAT
                | null
  """



# 25
def p_BooleanLiteral_true(p):
  """BooleanLiteral : true"""
  p[0] = True



# 25
def p_BooleanLiteral_false(p):
  """BooleanLiteral : false"""
  p[0] = False



# 26
def p_AttributeOrOperation(p):
  """AttributeOrOperation : Attribute
                          | Operation
  """
  p[0] = p[1]



# 26 TODO
def p_AttributeOrOperation_stringifier(p):
  """AttributeOrOperation : stringifier StringifierAttributeOrOperation
  """
  p[0] = p[2]



# 27 TODO
def p_StringifierAttributeOrOperation(p):
  """StringifierAttributeOrOperation : Attribute
                                     | OperationRest
                                     | ";"
  """



# 28
def p_Attribute(p):
  """Attribute : Inherit ReadOnly attribute Type IDENTIFIER ";"
  """
  p[0] = model.Attribute(inherit=p[1], readonly=p[2], type=p[4], name=p[5])



# 29
def p_Inherit_true(p):
  """Inherit : inherit"""
  p[0] = True



# 29
def p_Inherit_false(p):
  """Inherit :"""
  p[0] = False



# 30
def p_ReadOnly_true(p):
  """ReadOnly : readonly"""
  p[0] = True



# 30
def p_ReadOnly_false(p):
  """ReadOnly :"""
  p[0] = False



# 31 TODO
def p_Operation(p):
  """Operation : Qualifiers OperationRest"""



# 32 TODO
def p_Qualifiers(p):
  """Qualifiers : static
                | Specials
  """



# 33 TODO
def p_Specials(p):
  """Specials : Special Specials
              |
  """



# 34 TODO
def p_Special(p):
  """Special : getter
             | setter
             | creator
             | deleter
             | legacycaller
  """



# 35 TODO
def p_OperationRest(p):
  """OperationRest : ReturnType OptionalIdentifier "(" ArgumentList ")" ";"
  """



# 36 TODO
def p_OptionalIdentifier(p):
  """OptionalIdentifier : IDENTIFIER
                        |
  """



# 37 TODO
def p_ArgumentList(p):
  """ArgumentList : Argument Arguments
                  |
  """



# 38 TODO
def p_Arguments(p):
  """Arguments : "," Argument Arguments
               |
  """



# 39 TODO
def p_Argument(p):
  """Argument : ExtendedAttributeList OptionalOrRequiredArgument"""



# 40 TODO
def p_OptionalOrRequiredArgument(p):
  """OptionalOrRequiredArgument : optional Type IDENTIFIER Default
                                | Type Ellipsis IDENTIFIER
  """



# # 41
# def p_Optional(p):
#   """Optional : optional
#               |
#   """



# 42 TODO
def p_Ellipsis(p):
  """Ellipsis : ELLIPSIS
              |
  """



# 43 TODO
def p_ExceptionMember(p):
  """ExceptionMember : Const
                     | ExceptionField
  """



# 44 TODO
def p_ExceptionField(p):
  """ExceptionField : Type IDENTIFIER ";"
  """



# 45 TODO
def p_ExtendedAttributeList(p):
    """ExtendedAttributeList : "[" ExtendedAttribute ExtendedAttributes "]"
    """



# 45 TODO
def p_ExtendedAttributeList_empty(p):
    """ExtendedAttributeList :"""



# 46 TODO
def p_ExtendedAttributes(p):
    """ExtendedAttributes : "," ExtendedAttribute ExtendedAttributes"""



# 46 TODO
def p_ExtendedAttributes_empty(p):
    """ExtendedAttributes :"""



# 47 TODO
def p_ExtendedAttribute(p):
  """ExtendedAttribute : "(" ExtendedAttributeInner ")" ExtendedAttributeRest
                       | "[" ExtendedAttributeInner "]" ExtendedAttributeRest
                       | "{" ExtendedAttributeInner "}" ExtendedAttributeRest
                       | Other ExtendedAttributeRest
  """



# 48 TODO
def p_ExtendedAttributeRest(p):
  """ExtendedAttributeRest : ExtendedAttribute
                           |
  """



# 49 TODO
def p_ExtendedAttributeInner(p):
  """ExtendedAttributeInner : "(" ExtendedAttributeInner ")" ExtendedAttributeInner
                            | "[" ExtendedAttributeInner "]" ExtendedAttributeInner
                            | "{" ExtendedAttributeInner "}" ExtendedAttributeInner
                            | OtherOrComma ExtendedAttributeInner
                            |
  """



# 50 TODO
def p_Other(p):
  """Other : INTEGER
           | FLOAT
           | IDENTIFIER
           | STRING
           | OTHER
           | "."
           | ELLIPSIS
           | ":"
           | ";"
           | "<"
           | "="
           | ">"
           | "?"
           | Date
           | DOMString
           | any
           | attribute
           | boolean
           | byte
           | legacycaller
           | const
           | creator
           | deleter
           | double
           | exception
           | false
           | float
           | getter
           | implements
           | inherit
           | interface
           | long
           | null
           | object
           | octet
           | optional
           | or
           | sequence
           | setter
           | short
           | static
           | stringifier
           | true
           | typedef
           | unsigned
           | void
  """



# 51 TODO
def p_OtherOrComma(p):
  """OtherOrComma : Other
                  | ","
  """



# 52 TODO
def p_Type(p):
  """Type : SingleType
          | UnionType TypeSuffix
  """
  p[0] = p[1]



# 53
def p_SingleType(p):
  """SingleType : NonAnyType"""
  p[0] = p[1]



# 53
def p_SingleType_any(p):
  """SingleType : any TypeSuffixStartingWithArray"""
  p[0] = helper.unwrapTypeSuffix(model.Any(), p[2])



# 54 TODO
def p_UnionType(p):
  """UnionType : "(" UnionMemberType or UnionMemberType UnionMemberTypes ")"
  """



# 55 TODO
def p_UnionMemberType(p):
  """UnionMemberType : NonAnyType
                     | UnionType TypeSuffix
                     | any "[" "]" TypeSuffix
  """



# 56 TODO
def p_UnionMemberTypes(p):
  """UnionMemberTypes : or UnionMemberType UnionMemberTypes
                      |
  """



# 57
def p_NonAnyType_primitiveType(p):
  """NonAnyType : PrimitiveType TypeSuffix"""
  p[0] = helper.unwrapTypeSuffix(p[1], p[2])



# 57
def p_NonAnyType_domString(p):
  """NonAnyType : DOMString TypeSuffix"""
  p[0] = helper.unwrapTypeSuffix(model.DOMString(), p[2])



# 57
def p_NonAnyType_interface(p):
  """NonAnyType : IDENTIFIER TypeSuffix"""
  p[0] = helper.unwrapTypeSuffix(model.InterfaceType(name=p[1]), p[2])



# 57
def p_NonAnyType_sequence(p):
  """NonAnyType : sequence "<" Type ">" Null"""
  p[0] = model.Sequence(t=p[3], nullable=p[5])



# 57
def p_NonAnyType_object(p):
  """NonAnyType : object TypeSuffix"""
  p[0] = helper.unwrapTypeSuffix(model.Object(), p[2])



# 57
def p_NonAnyType(p):
  """NonAnyType : Date TypeSuffix"""
  p[0] = helper.unwrapTypeSuffix(model.Date(), p[2])



# 58 TODO
def p_ConstType(p):
  """ConstType : PrimitiveType Null"""



# 59
def p_PrimitiveType_integer(p):
  """PrimitiveType : UnsignedIntegerType"""
  p[0] = p[1]



# 59
def p_PrimitiveType_boolean(p):
  """PrimitiveType : boolean"""
  p[0] = model.Boolean()



# 59
def p_PrimitiveType_byte(p):
  """PrimitiveType : byte"""
  p[0] = model.Byte()



# 59
def p_PrimitiveType_octet(p):
  """PrimitiveType : octet"""
  p[0] = model.Octet()



# 59
def p_PrimitiveType_float(p):
  """PrimitiveType : float"""
  p[0] = model.Float()



# 59
def p_PrimitiveType_double(p):
  """PrimitiveType : double"""
  p[0] = model.Double()



# 60
def p_UnsignedIntegerType_unsigned(p):
  """UnsignedIntegerType : unsigned IntegerType"""
  p[0] = helper.unwrapIntegerType(True, p[2])



# 60
def p_UnsignedIntegerType(p):
  """UnsignedIntegerType : IntegerType"""
  p[0] = helper.unwrapIntegerType(False, p[1])



# 61
def p_IntegerType_short(p):
  """IntegerType : short"""
  p[0] = helper.SHORT



# 61
def p_IntegerType_long(p):
  """IntegerType : long OptionalLong"""
  if not p[2]:
    p[0] = helper.LONG
  else:
    p[0] = helper.LONGLONG



# 62
def p_OptionalLong_true(p):
  """OptionalLong : long"""
  p[0] = True



# 62
def p_OptionalLong_false(p):
  """OptionalLong :"""
  p[0] = False



# 63
def p_TypeSuffix(p):
  """TypeSuffix : "[" "]" TypeSuffix"""
  p[0] = [helper.ARRAY] + p[3]



# 63
def p_TypeSuffix_null(p):
  """TypeSuffix : "?" TypeSuffixStartingWithArray"""
  p[0] = [helper.NULLABLE] + p[2]



# 63
def p_TypeSuffix_empty(p):
  """TypeSuffix :"""
  p[0] = []



# 64
def p_TypeSuffixStartingWithArray(p):
  """TypeSuffixStartingWithArray : "[" "]" TypeSuffix"""
  p[0] = [helper.ARRAY] + p[3]



# 64
def p_TypeSuffixStartingWithArray_empty(p):
  """TypeSuffixStartingWithArray :"""
  p[0] = []



# 65
def p_Null_true(p):
  """Null : "?"
  """
  p[0] = True



# 65
def p_Null_false(p):
  """Null :"""
  p[0] = False



# 66 TODO
def p_ReturnType(p):
  """ReturnType : Type
                | void
  """



# # 67
# def p_ExtendedAttributeNoArgs(p):
#   """ExtendedAttributeNoArgs : IDENTIFIER"""



# # 68
# def p_ExtendedAttributeArgList(p):
#   """ExtendedAttributeArgList : IDENTIFIER "(" ArgumentList ")"
#   """



# # 69
# def p_ExtendedAttributeIdent(p):
#   """ExtendedAttributeIdent : IDENTIFIER "=" IDENTIFIER
#   """



# # 70
# def p_ExtendedAttributeNamedArgList(p):
#   """ExtendedAttributeNamedArgList : IDENTIFIER "=" IDENTIFIER "(" ArgumentList ")"
#   """



def p_error(p):
  raise RuntimeError("Syntax error at '%s'" % repr(p))



parsedir = os.path.dirname(__file__)
parser = yacc.yacc(tabmodule="pywidl.parsetab", outputdir=parsedir, debug=1)



def parse(source):
  return parser.parse(source)
