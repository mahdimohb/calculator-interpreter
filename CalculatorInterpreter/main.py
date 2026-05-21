from lexer import Lexer
from parser import Parser

# Input program
text = """
read x
y := 5 + 3 * 2
write y
"""

# Create lexer
lexer = Lexer(text)

# Create parser
parser = Parser(lexer)

# Start parsing
parser.program()

print("\nParsing Successful!")