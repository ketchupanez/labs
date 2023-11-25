#Вариант 7

import numpy as np

print("\t~Меню~")
print("1. Вычислить с помощью NumPy")
print("2. Работа с Pandas и визуализация данных в Matplotlib")
print("3. Визуализация данных в Matplotlib")

def task_1():

    zn = int(input("Выбирите значение:\n 1- Вычислить значение выражения \n 2- Матрицы\n"))
    if zn == 1:

        x = 0.75
        a = np.sin(np.pi/8 - 1)**2 + (3 + x**2)**(1/4)
        b = np.arcsin(x/2) - 5.236 * 10**(-2)
        c = np.log(abs(3.12-x))
        y = a / b + c

        print("При x = 0.75, значение выражения =", y)
    elif zn == 2:

        N = 42

        # матрица X
        X = np.ones((12, 3))
        X[:, 1] = np.arange(N, N + 12)
        X[:, 2] = np.random.randint(60, 83, size=12)

        # вектор Y
        Y = np.random.uniform(13.5, 18.6, size=12).reshape(-1, 1)

        # A=(X^T⋅X)^(-1)⋅(X^T⋅Y)
        A = np.linalg.inv(X.T @ X) @ (X.T @ Y)

        print("Вектор оценок A:" + A)

        Y_2 = X @ A

        print("\nИсходные значения Y:" + Y)
        print("\nПолученные значения Y:" + Y_2)

def task_2():

    zn = int(input("Выберите значение:\n 1- Работа с графиками и обработка массивов \n 2- Построить графики функций"))
    if zn == 1:
        pass
    elif zn == 2:
        pass
    else:
        print("Вы ввели неверное значение!")

while True:
    z = int(input("Выберите значение: "))
    if z == 1:
        task_1()
    elif z == 2:
        #task_2()
        pass
    elif z == 3:
        #task_3()
        pass
    else:
        print("Вы ввели неверное значение! Повторите ввод!")


