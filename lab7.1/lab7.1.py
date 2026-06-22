import math


class RationalError(ZeroDivisionError):
    def __init__(self, message="Помилка: знаменник не може дорівнювати нулю"):
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
            raise ValueError("Некоректні аргументи")

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

    def get_n(self):
        return self._n

    def get_d(self):
        return self._d


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
            raise TypeError("Некоректний тип")

    def __len__(self):
        return len(self._elements)

    def __getitem__(self, index):
        return self._elements[index]

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
                            print(f"Попередження у файлі {filename}: пропущено некоректний дріб '{token}' ({e})")
                        except ValueError:
                            print(f"Попередження у файлі {filename}: не вдалося розпізнати токен '{token}'")

        if len(r_list) == 0:
            print(f"Файл {filename} порожній або не містить коректних дробів.")
            return

        print(f"=== Результати для файлу: {filename} ===")
        print(f"Успішно завантажені елементи: {r_list}")
        print("-" * 50)

    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")


if __name__ == "__main__":
    files = ["input01.txt", "input02.txt", "input03.txt"]
    for f in files:
        process_file(f)