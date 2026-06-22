import turtle
import time
class Stem:
    def __init__(self, length=150, color="green"):
        self.length = length
        self.color = color

    def draw(self, t):
        t.color(self.color)
        t.pensize(4)
        t.setheading(270)  # Напрямок вниз
        t.forward(self.length)
class Leaf:
    def __init__(self, color="green"):
        self.color = color

    def draw(self, t, side="left"):
        t.color(self.color)
        t.pensize(2)
        t.begin_fill()
        if side == "left":
            t.setheading(135)
        else:
            t.setheading(45)
        t.circle(30, 90)
        t.left(90)
        t.circle(30, 90)
        t.end_fill()
class Petal:
    def __init__(self, radius=25, color="red"):
        self.radius = radius
        self.color = color

    def draw(self, t):
        t.color(self.color)
        t.begin_fill()
        t.circle(self.radius)
        t.end_fill()
class Flower:
    def __init__(self, x, y, petal_color="purple", num_petals=6):
        self.x = x
        self.y = y
        self.num_petals = num_petals
        self.stem = Stem(length=120, color="forest green")
        self.leaf = Leaf(color="forest green")
        self.petal = Petal(radius=20, color=petal_color)

    def draw(self, t):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        self.stem.draw(t)
        t.penup()
        t.goto(self.x, self.y - 50)
        t.pendown()
        self.leaf.draw(t, side="left")

        t.penup()
        t.goto(self.x, self.y - 80)
        t.pendown()
        self.leaf.draw(t, side="right")
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()

        angle = 360 / self.num_petals
        for _ in range(self.num_petals):
            self.petal.draw(t)
            t.left(angle)
        t.color("yellow")
        t.begin_fill()
        t.circle(10)
        t.end_fill()
if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.bgcolor("light blue")
    screen.title("Лабораторна 2: Букет квітів (ООП)")
    t = turtle.Turtle()
    t.speed(0)
    bouquet = [
        Flower(x=-150, y=0, petal_color="crimson", num_petals=6),
        Flower(x=0, y=50, petal_color="orange", num_petals=8),
        Flower(x=150, y=-20, petal_color="hot pink", num_petals=5)
    ]
    for flower in bouquet:
        flower.draw(t)
    t.hideturtle()
    print("Малювання завершено!")
    turtle.done()