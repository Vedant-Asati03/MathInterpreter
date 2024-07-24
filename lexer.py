from tokens import TokenType, Token


WHITESPACE = " \n\t"


class Lexer:

    def __init__(self, text):
        self.text = iter(text)
        self.advance()

        self.token_type = {
            "+": TokenType.PLUS,
            "-": TokenType.MINUS,
            # "|": TokenType.MODULUS,
            "*": TokenType.MULTIPLY,
            "/": TokenType.DIVIDE,
            "^": TokenType.EXPONENT,
            "**": TokenType.EXPONENT,
            "(": TokenType.LPAREN,
            ")": TokenType.RPAREN,
        }

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):

        while self.current_char:

            if self.current_char in WHITESPACE:
                self.advance()

            elif self.current_char == "." or self.current_char.isdigit():
                yield self.generate_number()  # type: ignore

            elif self.current_char in list(self.token_type.keys()):
                current_char = self.current_char
                self.advance()
                yield Token(self.token_type[current_char])  # type: ignore

            else:
                raise Exception(f"Illegal character '{self.current_char}'")

    def generate_number(self):
        decimal_point_count = 0
        number_str = str(self.current_char)
        self.advance()

        while self.current_char and (
            self.current_char == "." or self.current_char.isdigit()
        ):
            if self.current_char == ".":
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break

            number_str += self.current_char
            self.advance()

        if number_str.startswith("."):
            number_str = "0" + number_str
        if number_str.endswith("."):
            number_str += "0"

        return Token(TokenType.NUMBER, float(number_str))
