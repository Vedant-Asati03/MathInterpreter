from lexer import Lexer
from parser import Parser
from interpreter import Interpreter


while True:

    expression = input(">>> ")

    if expression == "exit":
        break

    lexer = Lexer(expression)

    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    tree = parser.parse()

    if not tree:
        continue

    interpreter = Interpreter()
    value = interpreter.visit(tree)

    print(value)
