from tokens import *

class Parser:

    def __init__(self, lexer):

        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    # Error message
    def error(self, message):

        raise Exception(f"Syntax Error: {message}")

    # Match expected token
    def eat(self, token_type):

        if self.current_token[0] == token_type:

            print("Matched:", self.current_token)

            self.current_token = self.lexer.get_next_token()

        else:

            self.error(
                f"Expected {token_type}, got {self.current_token[0]}"
            )

    # program → stmt_list
    def program(self):

        self.stmt_list()

        if self.current_token[0] != EOF:
            self.error("Expected EOF")

    # stmt_list → stmt stmt_list | ε
    def stmt_list(self):

        while self.current_token[0] in (ID, READ, WRITE):

            self.stmt()

    # stmt → id := expr
    #      | read id
    #      | write expr
    def stmt(self):

        # id := expr
        if self.current_token[0] == ID:

            self.eat(ID)
            self.eat(ASSIGN)

            self.expr()

        # read id
        elif self.current_token[0] == READ:

            self.eat(READ)
            self.eat(ID)

        # write expr
        elif self.current_token[0] == WRITE:

            self.eat(WRITE)

            self.expr()

        else:

            self.error("Invalid statement")

    # expr → term {(+|-) term}
    def expr(self):

        self.term()

        while self.current_token[0] in (PLUS, MINUS):

            if self.current_token[0] == PLUS:
                self.eat(PLUS)

            else:
                self.eat(MINUS)

            self.term()

    # term → factor {(*|/) factor}
    def term(self):

        self.factor()

        while self.current_token[0] in (TIMES, DIVIDE):

            if self.current_token[0] == TIMES:
                self.eat(TIMES)

            else:
                self.eat(DIVIDE)

            self.factor()

    # factor → (expr) | id | number
    def factor(self):

        # ( expr )
        if self.current_token[0] == LPAREN:

            self.eat(LPAREN)

            self.expr()

            self.eat(RPAREN)

        # id
        elif self.current_token[0] == ID:

            self.eat(ID)

        # number
        elif self.current_token[0] == NUMBER:

            self.eat(NUMBER)

        else:

            self.error(
                "Expected NUMBER, ID, or '('"
            )