"""
Calculator

Create a simple calculator that given a string of operators (), +, -, *, / and numbers separated by spaces returns the
value of that expression

Example:

Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7
Remember about the order of operations! Multiplications and divisions have a higher priority and should be performed
left-to-right. Additions and subtractions have a lower priority and should also be performed left-to-right.
"""


class Calculator:
    def evaluate(self, string: str):
        self.tokens = string.split()
        self.pos = 0

        result = self._parse_expression()

        if isinstance(result, float) and result.is_integer():
            return int(result)
        return result

    def _parse_expression(self):
        result = self._parse_term()
        while self.pos < len(self.tokens) and self.tokens[self.pos] in ('+', '-'):
            op = self.tokens[self.pos]
            self.pos += 1
            right = self._parse_term()
            if op == '+':
                result += right
            else:
                result -= right
        return result

    def _parse_term(self):
        result = self._parse_factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos] in ('*', '/'):
            op = self.tokens[self.pos]
            self.pos += 1
            right = self._parse_factor()
            if op == '*':
                result *= right
            else:
                result /= right
        return result

    def _parse_factor(self):
        if self.pos < len(self.tokens) and self.tokens[self.pos] in ('+', '-'):
            op = self.tokens[self.pos]
            self.pos += 1
            val = self._parse_factor()
            return -val if op == '-' else val

        token = self.tokens[self.pos]
        self.pos += 1

        if token == '(':
            result = self._parse_expression()
            self.pos += 1
            return result

        return float(token)
