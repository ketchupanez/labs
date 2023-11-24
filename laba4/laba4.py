# Вариант 27

import ex1
import ex2.human
import ex2.house
import ex2.smallHouse
import ex3.Car
import ex3.SportCar
import ex3.PoliceCar
import ex3.WorkCar
import ex3.TownCar
from ex4 import  BouquetShop

print("\t\t -Меню-")

print(" 1. Класс Triangle. В нем 3 метода:\n     1) проверка на существование треугольника по данным сторонам\n     2)Нахождение S треугольника.\n     3)Нахождение P треугольника.")
print(" 2. Класс House.")
print(" 3. Базовый класс Car.")
print(" 4. Свой класс")


while True:
    a = int(input("Выберите значение: "))

    if a.isdigit():
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
                        if tr.is_triangle():
                            tr.square()

                        else:
                            print("Треугольника с такими сторонвми не существует - найти площадь невозможно")

                    elif znach == 3:
                        if tr.is_triangle():
                            tr.perimeter()
                        else:
                            print("Треугольника с такими сторонвми не существует - найти периметр невозможно")

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
                        home1 = ex2.house.House("Дом1", 20000, 78)
                        home2 = ex2.smallHouse.SmallHouse("Дом 2", 5000)
                        home3 = ex2.house.House("Дом 3", 50000, 127)

                        home1.print_info()
                        home2.print_info()
                        home3.print_info()

                        z = int(input("Какой дом вы желаете приобрести? Введите № от 1 до 3\n"))
                        if z == 1:
                                hm.make_deal(home1)

                        elif z == 2:
                                hm.make_deal(home2)

                        elif z == 3:
                                hm.make_deal(home3)

                        else:
                            print("Вы ввели неверное значение, пожалуйста, повторите ввод.\n")

                    else:
                        print("Вы ввели неверное значение, пожалуйста, повторите ввод.\n")

        elif a == 3:
            c = ex3.Car.Car
            tc = ex3.TownCar.TownCar
            sc = ex3.SportCar.SportCar
            wc = ex3.WorkCar.WorkCar
            pc = ex3.PoliceCar.PoliceCar

            while True:
                car1 = ex3.Car.Car("bmw", "black", 79, None)
                car2 = ex3.Car.Car("porsche", "red", 125, None)
                car3 = ex3.Car.Car("audi", "black", 79, True)
                car4 = ex3.Car.Car("MAZ", "blue", 45, None)

                z = int(input("Какой машиной вы хотите управлять?\n 1- городской\n 2- гоночной\n 3- грузовой\n"))

                if z == 1:
                    print(f"Вы выбрали {car1.color} {car1.name}")

                    while True:
                        a = int(input("Выбирите действие:\n 1- поехать\n 2- остановиться\n 3- повернуть\n 4- посмотреть скорость\n 5- выход\n"))

                        if a == 1:
                            c.go(car1)
                        elif a == 2:
                            c.stop(car1)
                        elif a == 3:
                            c.turn(car1)
                        elif a == 4:
                            tc.show_speed(car1)
                            if car1.speed > 60:
                                print(" ")
                                print("*Приближается полицейская машина*")
                                pc.viu(car3)
                                pc.stop_request(car1)
                                print(" ")
                        elif a == 5:
                            print("Программа завершена")
                            break
                        else:
                            print("Вы ввели неверное значение!")

                elif z == 2:
                    print(f"Вы выбрали {car2.color} {car2.name}")

                    while True:
                        a = int(input("Выбирите действие:\n 1- поехать\n 2- остановиться\n 3- повернуть\n 4- посмотреть скорость\n 5- погазовать\n"))

                        if a == 1:
                            c.go(car2)
                        elif a == 2:
                            c.stop(car2)
                        elif a == 3:
                            c.turn(car2)
                        elif a == 4:
                            c.show_speed(car2)
                        elif a == 5:
                            sc.vrum(car2)
                        else:
                            print("Вы ввели неверное значение!")

                elif z == 3:
                    print(f"Вы выбрали {car4.color} {car4.name}")

                    while True:
                        a = int(input("Выбирите действие:\n 1- поехать\n 2- остановиться\n 3- повернуть\n 4- посмотреть скорость\n"))

                        if a == 1:
                            c.go(car4)
                        elif a == 2:
                            c.stop(car4)
                        elif a == 3:
                            c.turn(car4)
                        elif a == 4:
                            wc.show_speed(car4)
                            if car3.speed > 40:
                                print(" ")
                                print("*Приближается полицейская машина*")
                                pc.viu(car3)
                                pc.stop_request(car4)
                                print(" ")
                        else:
                            print("Вы ввели неверное значение!")

                else:
                    print("Вы ввели неверное значение, пожалуйста, повторите ввод.\n")

        elif a == 4:
            bs = BouquetShop

            while True:
                a = int(input("Выберите дейтствие:\n 1 - Войти в цветочный\n 2 - Уйти\n"))
                if a == 1:
                    bs.output()
                    bs.catalog()
                    z = int(input("Выберите какой-нибудь из букетов (1-4)\n"))
                    if 1 <= z <= 4:
                       print(f"*Вы выбрали {z} букет (здесь и далее нажимайте Enter)*")
                       input()
                       print("*Сотрудница начала составлять букет*")
                       input()
                       print("*Спустя 15 минут томительного ожидания, композиция была завершена*")
                       input()
                       print("- Вот Ваш букет")
                       input()
                       print("*Вы уже начали тянуть руки навстречу букету, он же в ответ\n тянулся к Вам навстречу лепестками свежих, привезенных этим утром, цветов, как вдруг, услышали голос флориста*")
                       print("- Прошу прощения, Вы не оплатили заказ")
                       input()
                       print("*Вы сунули руку в карман за кошельком и, к своему стыду, поняли, что оставили его дома*")
                       input()
                       print("*Цветы до вас так и не дотянулись, а букет так и не увидел лучей заходящего солнца,\nоставшись в четырех стенах цветочного магазина*")
                       input()
                       print("**Конец**")
                    else:
                        print("Неверный ввод")

                elif a == 2:
                    print("*Вы решили не заходить в магазин* (здесь и далее нажимайте Enter)")
                    input()
                    print("*Вернувшись с прогулки вы хотели вкусно поужинать*")
                    input()
                    print("*Подходя к двери квартиры Вы увидели чемодан, предположительно, набитый Вашими вещами*")
                    input()
                    print("*Позже Вы узнали, что подруга Вашей девушки видела, как вы долго и мучительно смотрели на цветочный магазин, \nно, к вашему сожалению, сделали неверный выбор, решив уйти и не купив букет свежих цветов*")
                    input()
                    print("*Вы облажались\n")
                else:
                    print("Неверный выбор значения!")
    else:
        print("Вы ввели неверное значение, пожалуйста, повторите ввод.\n")






