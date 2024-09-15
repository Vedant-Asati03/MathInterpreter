from enum import Enum
from dataclasses import dataclass


class TokenType(Enum):
    NUMBER = 0
    VARIABLE = 0
    PLUS = 1
    MINUS = 2
    MODULUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    EXPONENT = 5
    LPAREN = 6
    RPAREN = 7


@dataclass
class Token:
    type: TokenType
    value: any = None  # type: ignore

    def __repr__(self) -> str:
        return self.type.name + (f":{self.value}" if self.value else "")
