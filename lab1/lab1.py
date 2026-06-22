import math
class Shape:
    def get_perimeter(self):
        raise NotImplementedError
    def get_area(self):
        raise NotImplementedError
    def get_name(self):
        return self.__class__.__name__
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def get_perimeter(self):
        return self.a + self.b + self.c
    def get_area(self):
        p = self.get_perimeter() / 2
        # Захист від від'ємного виразу під коренем (якщо фігура некоректна)
        val = p * (p - self.a) * (p - self.b) * (p - self.c)
        return math.sqrt(val) if val > 0 else 0
class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_perimeter(self):
        return 2 * (self.a + self.b)

    def get_area(self):
        return self.a * self.b
class Trapeze(Shape):
    def __init__(self, a, b, c, d):
        self.a = a  # Основа 1
        self.b = b  # Основа 2
        self.c = c  # Бічна сторона 1
        self.d = d  # Бічна сторона 2

    def get_perimeter(self):
        return self.a + self.b + self.c + self.d

    def get_area(self):
        if abs(self.a - self.b) < 1e-9:
            return 0
        diff = self.a - self.b
        numerator = (self.c + self.d + diff) * (self.c + self.d - diff) * (self.c - self.d + diff) * (
                    -self.c + self.d + diff)
        if numerator < 0:
            return 0
        return ((self.a + self.b) / (4 * abs(diff))) * math.sqrt(numerator)

class Parallelogram(Shape):
    def __init__(self, a, b, h):
        self.a = a  # Сторона, до якої проведено висоту
        self.b = b  # Інша сторона
        self.h = h  # Висота

    def get_perimeter(self):
        return 2 * (self.a + self.b)

    def get_area(self):
        return self.a * self.h
class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def get_perimeter(self):
        return 2 * math.pi * self.r

    def get_area(self):
        return math.pi * self.r ** 2

def main():

    files = files = ["input01.txt", "input02.txt", "input03.txt"]

    for filename in files:
        print(f"\n=== {filename} ")
        shapes = []

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    parts = line.strip().split()
                    if not parts:
                        continue

                    shape_type = parts[0]

                    params = [float(x) for x in parts[1:]]

                    if shape_type == "Triangle" and len(params) == 3:
                        shapes.append(Triangle(*params))
                    elif shape_type == "Rectangle" and len(params) == 2:
                        shapes.append(Rectangle(*params))
                    elif shape_type == "Trapeze" and len(params) == 4:
                        shapes.append(Trapeze(*params))
                    elif shape_type == "Parallelogram" and len(params) == 3:
                        shapes.append(Parallelogram(*params))
                    elif shape_type == "Circle" and len(params) == 1:
                        shapes.append(Circle(*params))

        except FileNotFoundError:
            print(f"Помилка: Файл {filename} не знайдено в папці lab. Пропускаємо його.")
            continue

        if not shapes:
            print("Файл порожній або не містить коректних даних про фігури.")
            continue
        max_area_shape = max(shapes, key=lambda s: s.get_area())
        max_perimeter_shape = max(shapes, key=lambda s: s.get_perimeter())
        print(f"  -> Фігура з найбільшою площею: {max_area_shape.get_name()} (Площа = {max_area_shape.get_area():.2f})")
        print(
            f"  -> Фігура з найбільшим периметром: {max_perimeter_shape.get_name()} (Периметр = {max_perimeter_shape.get_perimeter():.2f})")
if __name__ == "__main__":
    main()