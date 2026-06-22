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
            raise ValueError("Некоректні аргументи")

    def _init_from_ints(self, n, d):
        if d == 0:
            raise ZeroDivisionError("Знаменник нуль")
        gcd = math.gcd(n, d)
        self._n = n // gcd
        self._d = d // gcd
        if self._d < 0:
            self._n = -self._n
            self._d = -self._d

    def _init_from_string(self, s):
        if '/' in s:
            parts = s.split('/')
            self._init_from_ints(int(parts[0].strip()), int(parts[1].strip()))
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

    def _to_rational(self, other):
        if isinstance(other, Rational):
            return other
        elif isinstance(other, int):
            return Rational(other, 1)
        raise TypeError("Некоректний тип")

    def __add__(self, other):
        other = self._to_rational(other)
        return Rational(self._n * other._d + other._n * self._d, self._d * other._d)

    def __radd__(self, other):
        return self.__add__(other)


class RationalList:
    def __init__(self, initial_elements=None):
        self._elements = []
        if initial_elements:
            for item in initial_elements:
                self.append(item)

    def append(self, item):
        if isinstance(item, Rational):
            self._elements.append(item)
        elif isinstance(item, int):
            self._elements.append(Rational(item, 1))
        else:
            raise TypeError("Елементом списку може бути лише Rational або int")

    def __len__(self):
        return len(self._elements)

    def __getitem__(self, index):
        return self._elements[index]

    def __setitem__(self, index, value):
        if isinstance(value, Rational):
            self._elements[index] = value
        elif isinstance(value, int):
            self._elements[index] = Rational(value, 1)
        else:
            raise TypeError("Значення має бути Rational або int")

    def __add__(self, other):
        new_list = RationalList(self._elements)
        if isinstance(other, RationalList):
            for item in other._elements:
                new_list.append(item)
        elif isinstance(other, (Rational, int)):
            new_list.append(other)
        else:
            raise TypeError("Некоректний тип для конкатенації")
        return new_list

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            for item in other._elements:
                self.append(item)
        elif isinstance(other, (Rational, int)):
            self.append(other)
        else:
            raise TypeError("Некоректний тип для додавання")
        return self

    def __str__(self):
        return str(self._elements)

    def sum_all(self):
        total = Rational(0, 1)
        for item in self._elements:
            total = total + item
        return total


def process_file(filename):
    r_list = RationalList()
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                tokens = line.strip().split()
                for token in tokens:
                    if token:
                        r_list.append(Rational(token))

        if len(r_list) == 0:
            print(f"Файл {filename} порожній.")
            return

        total_sum = r_list.sum_all()
        print(f"=== {filename} ===")
        print(f"Елементи списку: {r_list}")
        print(f"Кількість елементів: {len(r_list)}")
        print(f"Сума послідовності (дріб): {total_sum}")
        print(f"Сума послідовності (десятковий): {float(total_sum):.4f}")
        print("-" * 40)

    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")


if __name__ == "__main__":
    files = ["input01.txt", "input02.txt", "input03.txt"]
    for f in files:
        process_file(f)