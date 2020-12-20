from rply import ParserGenerator, LexerGenerator  # rply parser/lexer module to define new operator precedence
from rply.token import BaseBox

day18_file = open("C:/Users/zstavrakas/Desktop/Advent of Code 2020/Input Files/18.1.txt", 'r')
expressions = day18_file.read().split('\n')

# Generate the lexer/tokeniser to take in inputs and ignore whitespace in the expressions
# add takes a rule name, and a regular expression that defines the rule
lg = LexerGenerator()
lg.add("PLUS", r"\+")
lg.add("MUL", r"\*")
lg.add("NUMBER", r"\d+")
lg.add("OPEN_PARENS", r"\(")
lg.add("CLOSE_PARENS", r"\)")
lg.ignore("\s+") # ignore whitespace

lexer = lg.build() # build the lexer 


# Define the abstract syntax tree (AST) to outline how tokenised expressions will be evaluated
# the BaseBox allows the variables to still have a type to ensure the everything is statically typed 
class Number(BaseBox):
    def __init__(self, value):
        self.value = value
    
    def eval(self):
        return self.value

class BinaryOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Mul(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()


# Generate the parser for part 1 - multiplication and addition have equal precedence
# get the token names and assign precedence to the different tokens in their evaluation
pg = ParserGenerator(
    # list of accepted token names
    ['NUMBER', 'OPEN_PARENS', 'CLOSE_PARENS', 'PLUS', 'MUL'],  
    # operator precedence is listed in ascending order - can be left, right, or nonassoc - written as a list of tuples
    precedence = [
        ('left', ['PLUS', 'MUL'])
    ]
) # NOTE: the parser is redefined in part 2 in order to allow for addition to have higher precedence - the above applies EQUAL precedence

@pg.production('expression : NUMBER')
def expression_number(p):
    # p is a list of pieces matched by the right hand side of the rule
    return Number(int(p[0].getstr()))

@pg.production('expression : OPEN_PARENS expression CLOSE_PARENS')
def expression_parens(p):
    return p[1]

@pg.production('expression : expression PLUS expression')
@pg.production('expression : expression MUL expression')
def expression_binop(p):
    left, right = p[0], p[2]
    if p[1].gettokentype() == 'PLUS':
        return Add(left, right)
    elif p[1].gettokentype() == "MUL":
        return Mul(left, right)
    else:
        raise AssertionError("Sorry, this operation is not available/possible!")

parser = pg.build()  # bulid the parser


# Define the NEW parser for part 2 - addition has precedence over multiplication
# Re-construct the parser using the updated rule set
pg = ParserGenerator(
    # list of accepted token names
    ['NUMBER', 'OPEN_PARENS', 'CLOSE_PARENS', 'MUL', 'PLUS'],  
    # operator precedence is listed in ascending order - can be left, right, or nonassoc - written as a list of tuples
    precedence = [
        ('left', ['MUL']), 
        ('left', ['PLUS'])
    ]
)

# define the various parser operations that will need to be performed at runtime during expression evaluation
@pg.production('expression : NUMBER')
def expression_number(p):
    # p is a list of pieces matched by the right hand side of the rule
    return Number(int(p[0].getstr()))

@pg.production('expression : OPEN_PARENS expression CLOSE_PARENS')
def expression_parens(p):
    return p[1]

@pg.production('expression : expression PLUS expression')
@pg.production('expression : expression MUL expression')
def expression_binop(p):
    left, right = p[0], p[2]
    if p[1].gettokentype() == 'PLUS':
        return Add(left, right)
    elif p[1].gettokentype() == "MUL":
        return Mul(left, right)
    else:
        raise AssertionError("Sorry, this operation is not available/possible!")

parser2 = pg.build()  # re-build the parser using the updated rule set


# ---------------------------------------------------------------------
# PART 1
# You have been given a list of unusual math expressions where operator precedence does not exist (although brackets still matter)
# Find the sum of all the expressions (e.g. 2 + 3 * (4 + 3 * 2) would become 2 + 3 * 14 = 70) - only + and * are required

def first_solution(expressions):
    return sum([parser.parse(lexer.lex(line)).eval() for line in expressions])

# PART 2
# The same as Part 1, except now addition has higher precedence than multiplication instead of being equal

def second_solution(expressions):
    return sum([parser2.parse(lexer.lex(line)).eval() for line in expressions])

# tests
print(first_solution(expressions))
print(second_solution(expressions))
