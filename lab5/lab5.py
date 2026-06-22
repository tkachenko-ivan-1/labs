import math


class Rational:
    def __init__(self, *args):
        if len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int):
            self._init_from_ints(args[0], args[1])
        elif len(args) == 1 and isinstance(args[0], str):
            self._init_from_string(args[0])
        elif len(args) == 1 and isinstance(args[0], Rational):
            self._init_from_ints(args[0]._n, args[0]._d)
        else:
            raise ValueError("Некоректні аргументи для конструктора")

    def _init_from_ints(self, n, d):
        if d == 0:
            raise ZeroDivisionError("Знаменник не може дорівнювати нулю")
        gcd = math.gcd(n, d)
        self._n = n // gcd
        self._d = d // gcd
        if self._d < 0:
            self._n = -self._n
            self._d = -self._d

    def _init_from_string(self, s):
        if '/' in s:
            parts = s.split('/')
            if len(parts) == 2:
                self._init_from_ints(int(parts[0].strip()), int(parts[1].strip()))
            else:
                raise ValueError("Некоректний формат дробу")
        else:
            self._init_from_ints(int(s.strip()), 1)

    def __str__(self):
        if self._d == 1:
            return str(self._n)
        return f"{self._n}/{self._d}"

    def __repr__(self):
        return self.__str__()

    def __float__(self):
        return self._n / self._d

    def __getitem__(self, key):
        if key == "n":
            return self._n
        elif key == "d":
            return self._d
        raise KeyError("Ключ повинен бути 'n' або 'd'")

    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise TypeError("Значення має бути цілим числом")
        if key == "n":
            self._init_from_ints(value, self._d)
        elif key == "d":
            self._init_from_ints(self._n, value)
        else:
            raise KeyError("Ключ повинен бути 'n' або 'd'")

    def _to_rational(self, other):
        if isinstance(other, Rational):
            return other
        elif isinstance(other, int):
            return Rational(other, 1)
        raise TypeError("Операція підтримується лише для типів Rational або int")

    def __add__(self, other):
        other = self._to_rational(other)
        return Rational(self._n * other._d + other._n * self._d, self._d * other._d)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        other = self._to_rational(other)
        return Rational(self._n * other._d - other._n * self._d, self._d * other._d)

    def __rsub__(self, other):
        other = self._to_rational(other)
        return Rational(other._n * self._d - self._n * other._d, other._d * self._d)

    def __mul__(self, other):
        other = self._to_rational(other)
        return Rational(self._n * other._n, self._d * other._d)

    def __rmul__(self, other):
        return self.__mul__(other)


def parse_expression_to_tokens(expr_str):
    raw_tokens = expr_str.strip().split()
    tokens = []
    for token in raw_tokens:
        if token in ['+', '-', '*']:
            tokens.append(token)
        else:
            tokens.append(Rational(token))
    return tokens


def evaluate_tokens(tokens):
    i = 0
    while i < len(tokens):
        if tokens[i] == '*':
            left = tokens[i - 1]
            right = tokens[i + 1]
            result = left * right
            tokens[i - 1: i + 2] = [result]
            i -= 1
        else:
            i += 1

    total = tokens[0]
    i = 1
    while i < len(tokens):
        op = tokens[i]
        right = tokens[i + 1]
        if op == '+':
            total = total + right
        elif op == '-':
            total = total - right
        i += 2

    return total


if __name__ == "__main__":
    try:
        with open("input01.txt", "r", encoding="utf-8") as file:
            expression_str = file.read().strip()

        print(f"Вхідний вираз: {expression_str}")

        tokens = parse_expression_to_tokens(expression_str)
        result_rational = evaluate_tokens(tokens)

        print(f"Результат у вигляді звичайного дробу: {result_rational}")
        print(f"Результат у вигляді десяткового дробу: {float(result_rational):.4f}")

    except FileNotFoundError:
        print("Помилка: Файл input01.txt не знайдено.")