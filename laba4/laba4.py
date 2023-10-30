# Вариант 27

import ex1

print("\t\t -Меню-")

print(" 1. Класс Triangle. В нем 3 метода:\n     1) проверка на существование треугольника по данным сторонам\n     2)Нахождение S треугольника.\n     3)Нахождение P треугольника.")
print(" 2. Класс House.")
print(" 3. Базовый класс Car.")
print(" 4. Свой класс")

while True:
    a = (input("Выберите значение: "))

    if a.isdigit():
        a = int(a)
        if a == 1:
            while True:
                znach = (input("Выберите значение (1 - Проверка, 2 - S треугольника, 3 - P треугольника): "))

                if znach.isdigit():
                    znach = int(znach)
                    a = int(input("Первая сторона треугольника: "))
                    b = int(input("Вторая сторона треугольника: "))
                    c = int(input("Третья сторона треугольника: "))

                    tr = ex1.Triangle(a, b, c)
                    if znach == 1:
                        tr.is_triangle()
                    elif znach == 2:
                        tr.square()
                    elif znach == 3:
                        tr.perimeter()
                else:
                    print("Вы ввели неверное значение, пожалуйста, повторите ввод.\n")
        elif a == 2:
            pass
        elif a == 3:
            pass
        elif a == 4:
            pass
    else:
        print("Вы ввели неверное значение, пожалуйста, повторите ввод.\n")
