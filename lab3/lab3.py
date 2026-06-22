import math


class Figure:
    def dimension(self):
        pass

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        pass


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def dimension(self):
        return 2

    def perimetr(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimetr() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def volume(self):
        return self.square()


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dimension(self):
        return 2

    def perimetr(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b

    def volume(self):
        return self.square()


class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def dimension(self):
        return 2

    def perimetr(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        if self.a == self.b:
            return 0.0
        s = self.perimetr() / 2
        part = (self.b + self.a) / (self.b - self.a)
        root = (s - self.a) * (s - self.b) * (s - self.a - self.c) * (s - self.a - self.d)
        if root < 0:
            return 0.0
        return part * math.sqrt(root)

    def volume(self):
        return self.square()


class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def dimension(self):
        return 2

    def perimetr(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.h

    def volume(self):
        return self.square()


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def dimension(self):
        return 2

    def perimetr(self):
        return 2 * math.pi * self.r

    def square(self):
        return math.pi * (self.r ** 2)

    def volume(self):
        return self.square()


class Ball(Figure):
    def __init__(self, r):
        self.r = r

    def dimension(self):
        return 3

    def volume(self):
        return (4 / 3) * math.pi * (self.r ** 3)


class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self._h = h

    def dimension(self):
        return 3

    def height(self):
        return self._h

    def squareBase(self):
        return super().square()

    def volume(self):
        return (1 / 3) * self.squareBase() * self._h


class QuadrangularPyramid(Rectangle):
    def __init__(self, a, h):
        super().__init__(a, a)
        self._h = h

    def dimension(self):
        return 3

    def height(self):
        return self._h

    def squareBase(self):
        return super().square()

    def volume(self):
        return (1 / 3) * self.squareBase() * self._h


class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def dimension(self):
        return 3

    def height(self):
        return self.c

    def squareBase(self):
        return super().square()

    def volume(self):
        return self.squareBase() * self.c


class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self._h = h

    def dimension(self):
        return 3

    def height(self):
        return self._h

    def squareBase(self):
        return super().square()

    def volume(self):
        return (1 / 3) * self.squareBase() * self._h


class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self._h = h

    def dimension(self):
        return 3

    def height(self):
        return self._h

    def squareBase(self):
        return super().square()

    def volume(self):
        return self.squareBase() * self._h


def process_file(filename):
    shapes = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
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
                elif shape_type == "Ball" and len(params) == 1:
                    shapes.append(Ball(*params))
                elif shape_type == "TriangularPyramid" and len(params) == 2:
                    shapes.append(TriangularPyramid(*params))
                elif shape_type == "QuadrangularPyramid" and len(params) == 2:
                    shapes.append(QuadrangularPyramid(*params))
                elif shape_type == "RectangularParallelepiped" and len(params) == 3:
                    shapes.append(RectangularParallelepiped(*params))
                elif shape_type == "Cone" and len(params) == 2:
                    shapes.append(Cone(*params))
                elif shape_type == "TriangularPrism" and len(params) == 4:
                    shapes.append(TriangularPrism(*params))
    except FileNotFoundError:
        print(f"Помилка: Файл {filename} не знайдено.")
        return

    if not shapes:
        print(f"Файл {filename} порожній або не містить коректних даних.")
        return

    max_shape = max(shapes, key=lambda s: s.volume())

    print(f"=== Результати для файлу: {filename} ===")
    print(f"Найбільша фігура за мірою: {max_shape.__class__.__name__}")
    print(f"Вимірність: {max_shape.dimension()}-вимірна")
    print(f"Значення міри (площа або об'єм): {max_shape.volume():.2f}")
    print("-" * 40)


if __name__ == "__main__":
    files = ["input01.txt", "input02.txt", "input03.txt"]
    for f in files:
        process_file(f)