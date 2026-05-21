from tokens import *

class Lexer:

    def __init__(self, text):

        self.text = text
        self.pos = 0

        if len(text) > 0:
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    # Move to next character
    def advance(self):

        self.pos += 1

        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    # Skip spaces and new lines
    def skip_whitespace(self):

        while (
            self.current_char is not None
            and
            self.current_char.isspace()
        ):
            self.advance()

    # Read identifiers and reserved words
    def identifier(self):

        result = ""

        while (
            self.current_char is not None
            and
            (
                self.current_char.isalnum()
                or self.current_char == '_'
            )
        ):

            result += self.current_char
            self.advance()

        # Reserved words
        if result.lower() == "read":
            return (READ, result)

        elif result.lower() == "write":
            return (WRITE, result)

        else:
            return (ID, result)

    # Read numbers
    def number(self):

        result = ""

        while (
            self.current_char is not None
            and
            (
                self.current_char.isdigit()
                or self.current_char == '.'
            )
        ):

            result += self.current_char
            self.advance()

        return (NUMBER, result)

    # Main scanner
    def get_next_token(self):

        while self.current_char is not None:

            # Ignore spaces/newlines
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            # Identifier
            if (
                self.current_char.isalpha()
                or self.current_char == '_'
            ):
                return self.identifier()

            # Number
            if self.current_char.isdigit():
                return self.number()

            # :=
            if self.current_char == ':':

                self.advance()

                if self.current_char == '=':
                    self.advance()
                    return (ASSIGN, ':=')

                else:
                    raise Exception(
                        "Syntax Error: expected '=' after ':'"
                    )

            # +
            if self.current_char == '+':
                self.advance()
                return (PLUS, '+')

            # -
            if self.current_char == '-':
                self.advance()
                return (MINUS, '-')

            # *
            if self.current_char == '*':
                self.advance()
                return (TIMES, '*')

            # /
            if self.current_char == '/':
                self.advance()
                return (DIVIDE, '/')

            # (
            if self.current_char == '(':
                self.advance()
                return (LPAREN, '(')

            # )
            if self.current_char == ')':
                self.advance()
                return (RPAREN, ')')

            # Unknown character
            raise Exception(
                f"Unknown character: {self.current_char}"
            )

        return (EOF, None)