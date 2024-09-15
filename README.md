# Math_Interpreter

## Overview

Math_Interpreter is a Python-based project designed to interpret and evaluate mathematical expressions. It supports
various operations such as addition, subtraction, multiplication, division, modulus, and exponentiation.

## Features

- **Tokenization**: Converts input strings into tokens.
- **Parsing**: Parses tokens into an abstract syntax tree (AST).
- **Evaluation**: Evaluates the AST to produce a result.
- **Error Handling**: Provides meaningful error messages for common issues like division by zero and unclosed
  parentheses.

## Usage

To use the Math_Interpreter, you can run the main script with a mathematical expression as input:
```githubexpressionlanguage
>>> "2 + 3 * 4"
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request. For major changes, please open an issue
first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Detailed Description

Tokenization
The tokens.py file defines the TokenType enum and the Token dataclass. The TokenType enum includes types such as NUMBER,
VARIABLE, PLUS, MINUS, MODULUS, MULTIPLY, DIVIDE, EXPONENT, LPAREN, and RPAREN.  
Values
The values.py file defines the Number and Variable dataclasses. These classes are used to represent numerical values and
variables within expressions.  
Error Handling
The error_handling.py file contains the RaiseError class, which provides methods for raising exceptions related to
common errors like division by zero and unclosed parentheses.  
Parsing
The parser.py file (not shown in the excerpts) would contain the logic for converting a sequence of tokens into an
abstract syntax tree (AST).  
Evaluation
The interpreter.py file (not shown in the excerpts) would contain the logic for evaluating the AST to produce a result.