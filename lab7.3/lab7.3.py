import math


class RationalError(ZeroDivisionError):
    def __init__(self, message="Помилка: знаменник не може дорівнювати нулю"):
        self.message = message
        super().__init__(self.message)


class RationalValueError(TypeError):
    def __init__(self, message="Помилка: тип даних не підтримується для операцій з раціональними числами"):
        self.message = message
        super().__init__(self.message)


class Rational:
    def __init__(self, *args):
        if len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int):
            self._init_from_ints(args[0], args[1])
        elif len(args) == 1 and isinstance(args[0], str):
            self._init_from_string(args[0])
        elif len(args) == 1 and isinstance(args[0], Rational):
            self._init_from_ints(args[0]._n, args[0]._d)
        else:
            raise RationalValueError("Некоректні аргументи для конструктора")

    def _init_from_ints(self, n, d):
        if d == 0:
            raise RationalError()
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
                try:
                    self._init_from_ints(int(parts[0].strip()), int(parts[1].strip()))
                except ValueError:
                    raise RationalValueError("Рядок містить нецілі значення у дробі")
            else:
                raise RationalValueError("Некоректний формат рядка для дробу")
        else:
            try:
                self._init_from_ints(int(s.strip()), 1)
            except ValueError:
                raise RationalValueError("Рядок не є коректним цілим числом")

    def __str__(self):
        if self._d == 1:
            return str(self._n)
        return f"{self._n}/{self._d}"

    def __repr__(self):
        return self.__str__()


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
            raise RationalValueError(
                f"Неможливо додати тип '{type(item).__name__}' до RationalList. Дозволено лише Rational або int.")

    def __len__(self):
        return len(self._elements)

    def __getitem__(self, index):
        return self._elements[index]

    def __setitem__(self, index, value):
        if isinstance(value, (Rational, int)):
            self._elements[index] = value if isinstance(value, Rational) else Rational(value, 1)
        else:
            raise RationalValueError(
                f"Неможливо встановити тип '{type(value).__name__}' за індексом. Дозволено лише Rational або int.")

    def __add__(self, other):
        new_list = RationalList(self._elements)
        if isinstance(other, RationalList):
            for item in other._elements:
                new_list.append(item)
        elif isinstance(other, (Rational, int)):
            new_list.append(other)
        else:
            raise RationalValueError(f"Операція '+' не підтримується для RationalList та '{type(other).__name__}'")
        return new_list

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            for item in other._elements:
                self.append(item)
        elif isinstance(other, (Rational, int)):
            self.append(other)
        else:
            raise RationalValueError(f"Операція '+=' не підтримується для RationalList та '{type(other).__name__}'")
        return self

    def __str__(self):
        return str(self._elements)


def process_file(filename):
    r_list = RationalList()
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                tokens = line.strip().split()
                for token in tokens:
                    if token:
                        try:
                            r_list.append(Rational(token))
                        except RationalError as e:
                            print(f"[{filename}] Пропущено дріб: {token} ({e})")
                        except RationalValueError as e:
                            print(f"[{filename}] Пропущено токен: {token} ({e.message})")

        if len(r_list) == 0:
            print(f"Файл {filename} не містить коректних даних.")
            return

        print(f"=== Завантажено з файлу: {filename} ===")
        print(f"Елементи списку: {r_list}")

        # Демонстрація перевірки виключення RationalValueError для методів списку
        print("\n--- Тестування захисту RationalList ---")
        try:
            print("Спроба використати оператор '+' з некоректним типом (float)...")
            test_add = r_list + 3.14
        except RationalValueError as e:
            print(f"Успішно перехоплено помилку оператора '+': {e.message}")

        try:
            print("Спроба використати оператор '+=' з некоректним типом (str)...")
            r_list += "некоректні_дані"
        except RationalValueError as e:
            print(f"Успішно перехоплено помилку оператора '+=': {e.message}")

        print("-" * 60)

    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")


if __name__ == "__main__":
    files = ["input01.txt", "input02.txt", "input03.txt"]
    for f in files:
        process_file(f)