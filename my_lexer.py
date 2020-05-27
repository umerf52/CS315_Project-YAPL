import ply.lex as lex

tokens = (
    'AND',
    'CARET',
    'CHAR',
    'COMMA',
    'CUSTOM',
    'DATATYPE',
    'DISPLAY',
    'DIVIDE',
    'DO',
    'DOT',
    'DOUBLE',
    'EQUALEQUAL',
    'EQUALS',
    'FALSE',
    'GE',
    'GR',
    'ID',
    'INT',
    'LBRACE',
    'LE',
    'LPAREN',
    'LR',
    'MINUS',
    'MINUSMINUS',
    'MOD',
    'MULTIPLY',
    'NEW',
    'NOT',
    'NOTEQUAL',
    'OR',
    'PLUS',
    'PLUSPLUS',
    'RBRACE',
    'RPAREN',
    'STRING',
    'TRUE',
    'WHILE'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_DIVIDE = r'/'
t_MULTIPLY = r'\*'
t_EQUALS = r'='
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_RBRACE = r'\}'
t_LBRACE = r'\{'
t_EQUALEQUAL = r'=='
t_CARET = r'\^'
t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'--'
t_NOTEQUAL = r'!='
t_MOD = r'%'
t_GR = r'>'
t_LR = r'<'
t_GE = r'>='
t_LE = r'<='
t_DOT = r'\.'

t_ignore = ' \t\v\r'  # Whitespace


# Keyword for print
def t_DISPLAY(t):
    r'display'
    return t


def t_error(t):
    print('Lexer syntax error {} at position {} on line no {}'.format(
        t.value[0], t.lexpos, t.lineno))
    t.lexer.skip(1)


def t_DATATYPE(t):
    r'int|double|bool|char|string'
    return t


def t_DOUBLE(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_TRUE(t):
    r'True'
    t.value = True
    return t


def t_FALSE(t):
    r'False'
    t.value = False
    return t


def t_AND(t):
    r'AND'
    t.value = 'AND'
    return t


def t_OR(t):
    r'OR'
    t.value = 'OR'
    return t


def t_NOT(t):
    r'NOT'
    t.value = 'NOT'
    return t


def t_STRING(t):
    r'"(.*?)"'
    t.value = t.value[1:-1]
    return t


def t_DO(t):
    r'do'
    t.value = 'do'
    return t


def t_WHILE(t):
    r'while'
    t.value = 'while'
    return t


# Keyword for struct
def t_CUSTOM(t):
    r'custom'
    t.value = 'custom'
    return t


def t_NEW(t):
    r'new'
    t.value = 'new'
    return t


def t_ID(t):
    r'[_a-zA-Z][_a-zA-Z0-9]*'
    return t


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    pass


def t_CHAR(t):
    r'\'.\''
    t.value = t.value[1:-1]
    return t
