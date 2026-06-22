import turtle
import time
import math


class Watch:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_current_time(self):
        t = time.localtime()
        return t.tm_hour, t.tm_min, t.tm_sec

    def draw(self, t):
        pass


class AnalogWatch(Watch):
    def __init__(self, x, y, radius=100):
        super().__init__(x, y)
        self.radius = radius

    def draw_face(self, t):
        t.penup()
        t.goto(self.x, self.y - self.radius)
        t.setheading(0)
        t.pendown()
        t.pensize(4)
        t.color("black")
        t.circle(self.radius)

        t.penup()
        for i in range(12):
            angle = math.radians(i * 30)
            x_start = self.x + (self.radius - 15) * math.sin(angle)
            y_start = self.y + (self.radius - 15) * math.cos(angle)
            x_end = self.x + self.radius * math.sin(angle)
            y_end = self.y + self.radius * math.cos(angle)

            t.goto(x_start, y_start)
            t.pendown()
            t.pensize(4)
            t.color("black")
            t.goto(x_end, y_end)
            t.penup()

    def draw_hand(self, t, length, angle, size, color):
        t.penup()
        t.goto(self.x, self.y)
        t.setheading(90)
        t.right(angle)
        t.pendown()
        t.pensize(size)
        t.color(color)
        t.forward(length)

    def draw(self, t):
        self.draw_face(t)
        h, m, s = self.get_current_time()

        sec_angle = s * 6
        min_angle = m * 6 + s * 0.1
        hour_angle = (h % 12) * 30 + m * 0.5

        self.draw_hand(t, self.radius * 0.5, hour_angle, 6, "black")
        self.draw_hand(t, self.radius * 0.75, min_angle, 4, "blue")
        self.draw_hand(t, self.radius * 0.85, sec_angle, 2, "red")


class DigitalWatch(Watch):
    def __init__(self, x, y, is_24h=True):
        super().__init__(x, y)
        self.is_24h = is_24h

    def toggle_format(self):
        self.is_24h = not self.is_24h

    def draw(self, t):
        h, m, s = self.get_current_time()

        if not self.is_24h:
            period = "PM" if h >= 12 else "AM"
            h = h % 12
            if h == 0:
                h = 12
            time_str = f"{h:02d}:{m:02d}:{s:02d} {period}"
        else:
            time_str = f"{h:02d}:{m:02d}:{s:02d}"

        t.penup()
        t.goto(self.x, self.y)
        t.color("darkgreen")
        t.write(time_str, align="center", font=("Courier", 24, "bold"))

        t.goto(self.x, self.y - 30)
        t.color("gray")
        t.write("Click screen to change 12H/24H", align="center", font=("Arial", 10, "italic"))


def update_clock():
    t_drawer.clear()
    analog.draw(t_drawer)
    digital.draw(t_drawer)
    screen.update()
    screen.listen()
    screen.ontimer(update_clock, 1000)


def on_screen_click(x, y):
    digital.toggle_format()
    update_clock()


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(600, 500)
    screen.bgcolor("lightgray")
    screen.title("Лабораторна 4: Годинники (ОПП)")
    screen.tracer(0)

    t_drawer = turtle.Turtle()
    t_drawer.hideturtle()
    t_drawer.speed(0)

    analog = AnalogWatch(x=0, y=60, radius=120)
    digital = DigitalWatch(x=0, y=-140, is_24h=True)

    screen.onclick(on_screen_click)

    update_clock()
    screen.mainloop()