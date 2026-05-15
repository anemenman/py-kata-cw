"""
Simple Interactive Interpreter

Task
You will create an interpreter which takes inputs described below and produces outputs, storing state in between each
input.

If you're not sure where to start with this kata, check out my Simpler Interactive Interpreter kata, which greatly
simplifies the interpreter by removing functions.

Note that the eval command has been disabled.

Concepts
The interpreter will take inputs in the language described under the language header below. This section will give an
overview of the language constructs.

Variables
Any identifier which is not a keyword or a function name will be treated as a variable. If the identifier is on the
left hand side of an assignment operator, the result of the right hand side will be stored in the variable. If a
variable occurs as part of an expression, the value held in the variable will be substituted when the expression is
evaluated.

Variables are implicitly declared the first time they are assigned to.

Example: Initializing a variable to a constant value and using the variable in another expression (Each line starting
with a '>' indicates a separate call to the input method of the interpreter, other lines represent output)

>x = 7
    7
>x + 6
    13
Referencing a non-existent variable will cause the interpreter to throw an error. The interpreter should be able to
continue accepting input even after throwing.

Example: Referencing a non-existent variable

>y + 7
    ERROR: Invalid identifier. No variable with name 'y' was found."
Assignments
An assignment is an expression that has an identifier on left side of an = operator, and any expression on the right.
Such expressions should store the value of the right hand side in the specified variable and return the result.

Example: Assigning a constant to a variable

x = 7
    7
You should also be able to chain and nest assignments. Note that the assignment operator is one of the few that is
right associative.

Example: Chained assignments. The statement below should set both x and y to 7.

x = y = 7
    7
Example: Nested assignments. The statement below should set y to 3, but it only outputs the final result.

x = 13 + (y = 3)
    16
Operator Precedence
Operator precedence will follow the common order. There is a table in the Language section below that explicitly states
the operators and their relative precedence.

Functions
Functions are declared by the fn keyword followed by a name, an optional arguments list, the => operator, and finally
an expression. All function variables are local to the function. That is, the only variable names allowed in the
function body are those declared by the arguments list. If a function has an argument called 'x', and there is also
a global variable called 'x', the function should use the value of the supplied argument, not the value of the global
variable, when evaluating the expression. References to variables not found in the argument list should result in an
error when the function is defined.

Example: declare a function to calculate the average of two variables and call it. (Each line starting with a '>'
indicates a separate call to the input method of the interpreter, other lines represent output)

>fn avg => (x + y) / 2
    ERROR: Unknown identifier 'x'
>fn avg x y => (x + y) / 2
>a = 2
    2
>b = 4
    4
>avg a b
    3
Example: declare a function with an invalid variable name in the function body

>fn add x y => x + z
    ERROR: Invalid identifier 'z' in function body.
Example: chain method calls (hint: function calls are right associative!)

>fn echo x => x
>fn add x y => x + y
>add echo 4 echo 3
    7
Name conflicts
Because variable and function names share the same grammar, conflicts are possible. Precedence will be given to the
first object declared. That is, if a variable is declared, then subsequent declaration of a function with the same name
should result in an error. Likewise, declaration of a function followed by the initialization of a variable with the
same name should result in an error.

Declaration of function with the same name as an existing function should overwrite the old function with the new one.

Example: Overwriting a function

>fn inc x => x + 1
>a = 0
    0
>a = inc a
    1
>fn inc x => x + 2
>a = inc a
    3
Input
Input will conform to either the function production or the expression production in the grammar below.

Output
Output for a valid function declaration will be an empty string (null in Java).
Output for a valid expression will be the result of the expression.
Output for input consisting entirely of whitespace will be an empty string (null in Java).
All other cases will throw an error.
-- In Haskell that is:
Right (Nothing, Interpreter)
Right (Just Double, Interpreter)
Right (Nothing, Interpreter)
Left String
Language
Grammar
This section specifies the grammar for the interpreter language in EBNF syntax Whitespace (one or more) is required:

between the fn keyword and the function name in function definitions
to separate the function name from the parameter list in function definitions
to separate the parameters in function definitions
to separate the arguments in function calls
Whitespace (zero or more) is allowed:

at the start and end of the input
between operators (including =) and their operands
before and after => (start of the function body) in function definitions
whitespace      ::= ' ' { whitespace }

function        ::= 'fn'  whitespace  fn-name { whitespace identifier } '=>' expression
fn-name         ::= identifier

expression      ::= factor | expression operator expression
factor          ::= number | identifier | assignment | '(' expression ')' | function-call
assignment      ::= identifier '=' expression
function-call   ::= fn-name { whitespace expression }

operator        ::= '+' | '-' | '*' | '/' | '%'

identifier      ::= (letter | '_') { identifier-char }
identifier-char ::= '_' | letter | digit

number          ::= { digit } '.' digit { digit } | digit { digit } ['.']

letter          ::= 'a' | 'b' | ... | 'y' | 'z' | 'A' | 'B' | ... | 'Y' | 'Z'
digit           ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
Operator Precedence
The following table lists the language's operators grouped in order of precedence. Operators within each group have
equal precedence.

Category	Operators
Multiplicative	*, /, %
Additive	+, -
Assignment	=
Function	=>
Division
You should use float division instead of integer division.
"""
import pytest
import re


class Interpreter:
    def __init__(self):
        self.vars = {}  # Глобальные переменные
        self.funcs = {}  # Глобальные функции

    def input(self, line: str):
        line = line.strip()
        if not line:
            return None

        # Инициализируем состояние парсера заново для каждого вызова
        self.tokens = self._tokenize(line)
        self.pos = 0

        # Если начинается с 'fn' -> объявление функции
        if self.tokens[0][1] == 'fn':
            self._parse_fn_def()
            return None

        # Иначе -> вычисление выражения
        return self._format_result(self._parse_expr(self.vars))

    # ==================== TOKENIZER ====================
    def _tokenize(self, text):
        # Пропускает пробелы, вытаскивает числа, операторы, идентификаторы, скобки
        pattern = r'(?P<ARROW>=>)|(?P<OP>[+\-*/%=])|(?P<LPAREN>\()|(?P<RPAREN>\))|(?P<NUMBER>\d+\.\d*|\d*\.\d+|\d+)|(?P<IDENT>[a-zA-Z_]\w*)'
        tokens = []
        for m in re.finditer(pattern, text):
            kind = m.lastgroup
            val = m.group()
            tokens.append((kind, float(val) if kind == 'NUMBER' else val))
        return tokens

    # ==================== PARSER ====================
    def _peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def _consume(self):
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok

    def _parse_expr(self, scope):
        return self._parse_assign(scope)

    def _parse_assign(self, scope):
        left = self._parse_add(scope)
        if self._peek() and self._peek()[1] == '=':
            self._consume()
            if not isinstance(left, str):
                raise ValueError("Left side of assignment must be an identifier")
            if left in self.funcs:
                raise ValueError(f"Name conflict: '{left}' is already a function.")
            # Правоассоциативность =
            right = self._parse_assign(scope)
            scope[left] = right
            return right
        return left

    def _parse_add(self, scope):
        left = self._parse_mul(scope)
        while self._peek() and self._peek()[1] in ('+', '-'):
            op = self._consume()[1]
            left = self._apply_op(op, left, self._parse_mul(scope))
        return left

    def _parse_mul(self, scope):
        left = self._parse_call(scope)
        while self._peek() and self._peek()[1] in ('*', '/', '%'):
            op = self._consume()[1]
            left = self._apply_op(op, left, self._parse_call(scope))
        return left

    def _parse_call(self, scope):
        left = self._parse_primary(scope)
        # Если распознана функция, собираем аргументы
        if isinstance(left, str) and left in self.funcs:
            args = []
            while self._peek() and self._peek()[0] in ('NUMBER', 'IDENT', 'LPAREN'):
                args.append(self._parse_add(scope))
            if args:
                return self._call_func(left, args, scope)
        return left

    def _parse_primary(self, scope):
        tok = self._peek()
        if not tok:
            raise ValueError("Unexpected end of expression")

        if tok[0] == 'NUMBER':
            self._consume()
            return tok[1]

        elif tok[0] == 'IDENT':
            name = self._consume()[1]
            if name in scope: return scope[name]
            if name in self.vars: return self.vars[name]
            if name in self.funcs: return name
            raise ValueError(f"Invalid identifier. No variable with name '{name}' was found.")

        elif tok[0] == 'LPAREN':
            self._consume()
            val = self._parse_expr(scope)
            self._consume()  # ')'
            return val

        raise ValueError(f"Unexpected token {tok}")

    # ==================== EVAL HELPERS ====================
    def _apply_op(self, op, a, b):
        if isinstance(a, str) or isinstance(b, str):
            raise ValueError("Invalid identifier in expression")
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/':
            if b == 0: raise ZeroDivisionError("Division by zero")
            return a / b
        if op == '%':
            if b == 0: raise ZeroDivisionError("Division by zero")
            return a % b
        raise ValueError(f"Unknown operator '{op}'")

    def _call_func(self, name, args, caller_scope):
        func = self.funcs[name]
        if len(args) != len(func['args']):
            raise ValueError(f"Function '{name}' expects {len(func['args'])} arguments.")

        # Локальная область: только параметры функции
        local_scope = {arg: val for arg, val in zip(func['args'], args)}
        saved_tokens, saved_pos = self.tokens, self.pos
        self.tokens, self.pos = func['body'], 0

        try:
            return self._parse_expr(local_scope)
        finally:
            self.tokens, self.pos = saved_tokens, saved_pos

    def _parse_fn_def(self):
        self._consume()  # 'fn'
        name = self._consume()[1]
        if name in self.vars:
            raise ValueError(f"Name conflict: '{name}' is already a variable.")

        args = []
        while self._peek() and self._peek()[1] != '=>':
            args.append(self._consume()[1])
        self._consume()  # '=>'

        body_tokens = self.tokens[self.pos:]
        for tok in body_tokens:
            if tok[0] == 'IDENT' and tok[1] not in args and tok[1] not in self.funcs:
                raise ValueError(f"Invalid identifier '{tok[1]}' in function body.")

        self.funcs[name] = {'args': args, 'body': body_tokens}

    def _format_result(self, val):
        # Возвращаем int, если число целое, иначе float
        if isinstance(val, float) and val.is_integer():
            return int(val)
        return val


interpreter = Interpreter()

# Basic arithmetic
assert interpreter.input("1 + 1") == 2
assert interpreter.input("2 - 1") == 1
assert interpreter.input("2 * 3") == 6
assert interpreter.input("8 / 4") == 2
assert interpreter.input("7 % 4") == 3

# Variables
assert interpreter.input("x = 1") == 1
assert interpreter.input("x") == 1
assert interpreter.input("x + 3") == 4
assert interpreter.input("x + 3") == 4

pytest.raises(Exception, lambda: interpreter.input("y"))

# Functions
interpreter.input("fn avg x y => (x + y) / 2")
assert interpreter.input("avg 4 2") == 3
pytest.raises(Exception, lambda: interpreter.input("avg 7"))
pytest.raises(Exception, lambda: interpreter.input("avg 7 2 4"))

# Conflicts
pytest.raises(Exception, lambda: interpreter.input("fn x => 0"))
pytest.raises(Exception, lambda: interpreter.input("avg = 5"))

# Attempt
assert interpreter.input('') == ''
# print(interpreter.input('one'))

result = 5.1
if isinstance(result, float) and result.is_integer():
    print(int(result))
