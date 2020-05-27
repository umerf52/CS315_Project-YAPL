import ply.yacc as yacc
import ply.lex as lex

import my_lexer

start = 'exp'  # the start symbol in our grammar

tokens = my_lexer.tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'CARET'),
    ('left', 'MULTIPLY', 'DIVIDE', 'MOD')
)


# An exp can be made of multiple stmts
def p_stmt_start(p):
    'exp : stmts'
    p[0] = p[1]


# Stmts can be broken down into a single stmt and more stmts
def p_exp_stmts(p):
    'stmts : stmt stmts'
    p[0] = [p[1]] + p[2]


# Multiple stmts can be empty
def p_exp_emptystmt(p):
    'stmts : '
    p[0] = []


# A stmt can be used to declare and assign a variable
# For example, int a = 0
def p_stmt_declaration(p):
    'stmt : DATATYPE ID EQUALS exp'
    p[0] = ('declaration', p[1], p[2], p[3], p[4])


# A stmt can also be used to update a variable
# For example, a = 1
def p_stmt_update(p):
    'stmt : ID EQUALS exp'
    p[0] = ('update', p[1], p[3])


# An exp can be enclosed in parentheses
# For example, (a+b) = a+b
def p_exp_parenthesis(p):
    'exp : LPAREN exp RPAREN'
    p[0] = p[2]


def p_value_int(p):
    'exp : INT'
    p[0] = ('int', p[1])


def p_value_double(p):
    'exp : DOUBLE'
    p[0] = ('double', p[1])


def p_value_string(p):
    'exp : STRING'
    p[0] = ('string', p[1])


def p_value_bool(p):
    '''exp : TRUE
            | FALSE'''
    p[0] = ('bool', p[1])


def p_value_char(p):
    'exp : CHAR'
    p[0] = ('char', p[1])


# An exp can be ID, for example a variable name
def p_value_id(p):
    'exp : ID'
    p[0] = ('ID', p[1])


def p_exp_binaryop(p):
    '''exp : exp PLUS exp 
            | exp MINUS exp 
            | exp MULTIPLY exp 
            | exp DIVIDE exp
            | exp CARET exp
            | exp AND exp
            | exp OR exp
            | exp EQUALEQUAL exp
            | exp NOTEQUAL exp
            | exp MOD exp
            | exp GR exp
            | exp LR exp
            | exp GE exp
            | exp LE exp'''
    p[0] = ('bop', p[1], p[2], p[3])


def p_exp_unaryop(p):
    '''stmt : ID PLUSPLUS
            | ID MINUSMINUS'''
    p[0] = ('uop', p[1], p[2])


def p_exp_not(p):
    'exp : NOT exp'
    p[0] = ('uop', p[1], p[2])


def p_stmt_display(p):
    'stmt : DISPLAY LPAREN exp RPAREN'
    p[0] = ('display', p[3])


# An exp can be separated by commas
# For example, display(a+b, c-d...)
def p_exp_comma(p):
    'exp : exp COMMA exp'
    p[0] = p[1] + p[3]


# An exp can also be a custom
# For example, object_name.attribute_name
# This is used for displaying objects of customs
def p_custom_print(p):
    'exp : ID DOT ID'
    p[0] = ('custom-display', p[1], p[3])


def p_error(p):
    print('ERROR: ', p)
    print('Parser syntax error at line: {}'.format(p.lexer.lineno))


def p_do_while(p):
    'stmt : DO LBRACE stmts RBRACE WHILE LPAREN exp RPAREN'
    p[0] = ('do-while', p[3], p[7])


# A stmt can be a custom declaration
def p_custom_declaration(p):
    'stmt : CUSTOM ID LBRACE custom_stmts RBRACE'
    p[0] = ('custom-dec', p[2], p[4])


# custom_stmts can be broken down into a single custom_stmt and more custom_stmts
def p_custom_stmts(p):
    'custom_stmts : custom_stmt custom_stmts'
    p[0] = [p[1]] + p[2]


# custom_stmts can be empty
def p_custom_empty(p):
    'custom_stmts : '
    p[0] = []


# A custom_stmt looks like the following:
# int attr_name
def p_custom_stmt(p):
    'custom_stmt : DATATYPE ID'
    p[0] = (p[1], p[2])


# This is used to make an object of custom
# For example, new CustomName object_name
def p_custom_make(p):
    'stmt : NEW ID ID'
    p[0] = ('make-custom', p[2], p[3])


# This is used to assign values to a custom object's attributes
# For example, object_name.attr_name = value
def p_custom_assign(p):
    'stmt : ID DOT ID EQUALS exp'
    p[0] = ('custom-update', p[1], p[3], p[5])
