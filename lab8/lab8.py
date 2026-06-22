import math


def task_a():
    print("\n--- Задача a) Обчислення x_k = (x^k) / k ---")
    try:
        x = float(input("Введіть дійсне число x: "))
        k = int(input("Введіть ціле число k (k >= 1): "))
        if k < 1:
            print("Помилка: k повинно бути більшим або дорівнювати 1.")
            return

        result = (x ** k) / k
        print(f"Результат x_{k} = {result:.6f}")
    except ValueError:
        print("Некоректне введення числових даних.")


def task_b():
    print("\n--- Задача b) Обчислення добутку P_n ---")
    try:
        n = int(input("Введіть параметр n (n >= 1): "))
        if n < 1:
            print("Помилка: n повинно бути >= 1.")
            return

        p = 1.0
        for i in range(1, n + 1):
            p *= 1.0 / (i + math.factorial(1))  # 1! = 1, тобто 1 / (i + 1)

        print(f"Результат добутку P_{n} = {p:.8f}")
    except ValueError:
        print("Некоректне введення числових даних.")

def task_c():
    print("\n--- Задача c) Визначник тридіагональної матриці порядку n ---")
    try:
        n = int(input("Введіть порядок матриці n (n >= 1): "))
        if n < 1:
            print("Помилка: n повинно бути >= 1.")
            return
        # D_1 = 2
        # D_2 = 2*2 - 3*1 = 1
        # D_i = 2 * D_{i-1} - 3 * D_{i-2}
        if n == 1:
            print("Визначник матриці = 2")
            return
        elif n == 2:
            print("Визначник матриці = 1")
            return

        d_prev2 = 2  # D_1
        d_prev1 = 1  # D_2
        current_d = 0

        for i in range(3, n + 1):
            current_d = 2 * d_prev1 - 3 * d_prev2
            d_prev2 = d_prev1
            d_prev1 = current_d

        print(f"Визначник матриці порядку {n} = {d_prev1}")
    except ValueError:
        print("Некоректне введення числових даних.")

def task_d():
    print("\n--- Задача d) Обчислення суми S_n з рекурентними a_k ---")
    try:
        n = int(input("Введіть параметр n (n >= 1): "))
        if n < 1:
            print("Помилка: n повинно бути >= 1.")
            return
        a = [0] * (max(3, n) + 1)
        a[1] = 0
        a[2] = 1

        for k in range(3, n + 1):
            a[k] = a[k - 1] + k * a[k - 2]

        total_sum = 0
        for k in range(1, n + 1):
            total_sum += (2 ** k) * a[k]

        print(f"Сума S_{n} = {total_sum}")
    except ValueError:
        print("Некоректне введення числових даних.")
def task_e():
    print("\n--- Задача e) Розклад sin(x) у ряд Тейлора ---")
    try:
        x = float(input("Введіть значення x (в радіанах): "))
        eps = float(input("Введіть точність епсилон (наприклад, 0.00001): "))
        if eps <= 0:
            print("Помилка: точність повинна бути більшою за 0.")
            return
        x_mod = math.fmod(x, 2 * math.pi)

        term = x_mod
        taylor_sin = term
        n = 1

        while abs(term) > eps:
            term = term * (-x_mod ** 2) / ((2 * n) * (2 * n + 1))
            taylor_sin += term
            n += 1

        math_sin = math.sin(x)
        print(f"\nОбчислено через ряд Тейлора: {taylor_sin:.6f}")
        print(f"Значення з бібліотеки math:  {math_sin:.6f}")
        print(f"Абсолютна похибка:           {abs(taylor_sin - math_sin):.6e}")
        print(f"Кількість врахованих членів: {n}")
    except ValueError:
        print("Некоректне введення числових даних.")

if __name__ == "__main__":
    while True:
        print("\n================ Головне меню ================")
        print("a) Обчислення x_k = (x^k) / k")
        print("b) Обчислення добутку P_n")
        print("c) Обчислення визначника тридіагональної матриці")
        print("d) Обчислення суми S_n")
        print("e) Розклад sin(x) у ряд Тейлора")
        print("0) Вихід з програми")
        print("==============================================")

        choice = input("Оберіть пункт меню (a, b, c, d, e або 0): ").strip().lower()

        if choice == 'a':
            task_a()
        elif choice == 'b':
            task_b()
        elif choice == 'c':
            task_c()
        elif choice == 'd':
            task_d()
        elif choice == 'e':
            task_e()
        elif choice == '0':
            print("Програму завершено. Успішної здачі!")
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")