# Вариант 27

import ex1
import ex2.human
import ex2.house
import ex2.smallHouse
#import ex3
#import ex4

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
            hm = ex2.human.Human(40000)
            hs = ex2.house.House
            shs = ex2.smallHouse.SmallHouse


            while True:
                    znach = int(input("\tВыберите значение: \n1 - Посмотреть баланс, \n2 - Посмотреть доступные для покупки дома.\n"))

                    if znach == 1:
                        print(f"Баланс: {hm._money}$")

                    elif znach == 2:
                        home1 = ex2.house.House("Дом1",20000, 78)
                        home2 = ex2.smallHouse.SmallHouse("Дом 2",5000)
                        home3 = ex2.house.House("Дом 3",50000, 127)

                        home1.print_info()
                        home2.print_info()
                        home3.print_info()

                        z = int(input("Какой дом вы желаете приобрести? Введите № от 1 до 3\n"))
                        if z == 1:
                            if hm.buy_house(home1, 5):
                                hm.make_deal(home1, 20000)

                        elif z == 2:
                            if hm.buy_house(home2, 5):
                                hm.make_deal(home2, 5000)

                        elif z == 3:
                            if hm.buy_house(home3, 5):
                                hm.make_deal(home3, 50000)

                        else:
                            print("Вы ввели неверное значение, пожалуйста, повторите ввод.\n")




                    else:
                        print("Вы ввели неверное значение, пожалуйста, повторите ввод.\n")


        elif a == 3:
            pass
        elif a == 4:
            pass
    else:
        print("Вы ввели неверное значение, пожалуйста, повторите ввод.\n")
