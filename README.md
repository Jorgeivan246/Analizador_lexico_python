# Basic lexical analyzer. Formal language theory
The language used to build the parser is Python.
## Operation
The program reads the file, then regular expressions are used to find the required parts, in this case Cylon language reserved words.
Different types of expressions are used to find the required elements, some of them are:
. ^ $ * + ? { } [ ] \ | ( )

## The result is :
- The for statement is ['(name in names)', '(p in people)']
- The if statement is ['if (x > 1000)', 'if (p.age>=18)'].
- The print statement is ['print("Hello world!")', 'print("really big")'].
- The input statement is ['input("Enter your data")'].

