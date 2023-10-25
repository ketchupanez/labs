# #Вариант 27

print("\t Меню")

print(" 1. Напишите функцию для вывода всех простых чисел в заданном диапазоне.")
print(" 2. Напишите функцию, которая будет принимать один аргумент.\n Если в функцию передаётся список, Найдите произведение элементов с нечетными номерами.\n Найдите наибольший элемент списка, затем удалите его и выведите новый список.")
print(" Если словарь, вывести на экран первые три наибольших значения.\n Число – определить сумму его цифр. Строка – определить сколько в ней гласных, а сколько согласных.\n Посчитать количество слов.")
print(" 3. Найти в матрице первый столбец, все элементы которого отрицательны, и среднее арифметическое этих элементов.")
print(" 4. Напишите программу, демонстрирующую работу try \ except \ finally\n")

#place for functions
def task_1():
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def find_prime_num_in_range(start, end):
        prime_list = []
        for num in range(max(2, start), end + 1):
            if is_prime(num):
                prime_list.append(num)
        return prime_list

    try:
        a = int(input("Введите нижнюю границу диапазона: "))
        b = int(input("Введите верхнюю границу диапазона: "))
        print("Диапазон: [", a, ";", b, "]")
    except ValueError:
        print("Неверное значение")

    while True:
        nums = input("Введите числа в пределах диапазона: ")

        if nums == '0':
            break

        nums_list = nums.split()
        for num in nums_list:
            num = int(num)
            if a <= num <= b:
                if is_prime(num):
                    print( num)

            else:
                print(num, 'не находится в указанном диапазоне')


def task_2():
    final_cost = 0

    with open("prices.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line.rstrip())
            parts_finder = line.split()

            if len(parts_finder) == 3:
                item_name, quantity, price_per_unit = parts_finder
                try:
                    quantity = int(quantity)
                    price_per_unit = float(price_per_unit.replace(",", "."))

                    line_cost = quantity * price_per_unit
                    final_cost += line_cost  # подсчитываем общую стоимость товаров
                except ValueError:
                    print(f"Ошибка в строке {line}")
                    continue

            else:
                print(f"Ошибка в  строке {line} и она не будет подсчитана")

    print(f"Общая стоимость всех товаров в корзине : {final_cost:2f}")

def task_3():
 while True:
    try:
     rows = int(input("Введите количество строк: "))
     cols = int(input("Введите количество столбцов: "))

     if rows > 0 and cols > 0:
         print("Размерность матрицы: ", rows, "x", cols)
     else:
         print("Данные значения не могут быть отрицательными или равными 0, пожалуйста, повторите ввод")
    except ValueError:
        print("Введите целые числа для размерности матрицы")

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        matrix.append(row)

    for i in range(rows):
        for j in range(cols):
            while True:
                matrix[i][j] = int(input(f"Введите элемент [{i}, {j}]: "))
                if matrix[i][j] > 0:
                    break

        print(matrix[i])

    print("Матрица:")
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end='  ')
        print()

    #for j in range(cols):
     #   for i in range(rows):









def task_4():
    print("a = 2/0")
    try:
        a = 2/0
        print(a)
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
    finally:
        print("Конец программы\n")



while True:
    a = (input("Выберите значение: "))

    if a.isdigit():
        a = int(a)
        if a == 1:
            task_1()
        elif a == 2:
            task_2()
        elif a == 3:
            task_3()
        elif a == 4:
            task_4()
    else:
        print("Вы ввели неверное значение, пожалуйста, повторите ввод.\n")

