# math_parser.py

class MathParser:
    def __init__(self, expression):
        self.tokens = expression.split()
        self.current_token_index = 0

    def parse(self):
        return self.expression()

    def get_next_token(self):
        if self.current_token_index < len(self.tokens):
            self.current_token_index += 1
            return self.tokens[self.current_token_index - 1]
        return None

    def expression(self):
        result = self.term()
        while self.current_token_index < len(self.tokens) and self.tokens[self.current_token_index] in ('+', '-'):
            token = self.get_next_token()
            if token == '+':
                result += self.term()
            elif token == '-':
                result -= self.term()
        return result

    def term(self):
        result = self.factor()
        while self.current_token_index < len(self.tokens) and self.tokens[self.current_token_index] in ('*', '/'):
            token = self.get_next_token()
            if token == '*':
                result *= self.factor()
            elif token == '/':
                divisor = self.factor()
                if divisor == 0:
                    raise ValueError("Division by zero is a no-no.")
                result /= divisor
        return result

    def factor(self):
        token = self.get_next_token()
        if token.isdigit():
            return int(token)
        elif token == '(':
            result = self.expression()
            if self.get_next_token() != ')':
                raise ValueError("Mismatched parentheses, they're like socks, need a pair.")
            return result
        else:
            raise ValueError("Unexpected token: {}".format(token))

def evaluate_expression(expression):
    try:
        parser = MathParser(expression)
        return parser.parse()
    except Exception as e:
        return str(e)
