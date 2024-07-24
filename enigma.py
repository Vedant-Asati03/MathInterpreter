from lexer import Lexer
from parser import Parser
from interpreter import Interpreter


while True:

    text = input(">>> ")
    lexer = Lexer(text)

    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    tree = parser.parse()
    if not tree: continue
    interpreter = Interpreter()
    value = interpreter.visit(tree)
    print(value)
