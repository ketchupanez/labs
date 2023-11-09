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
    def process_argument(arg):
        if isinstance(arg, list):
            product = 1
            for i in range(len(arg)):
                if i % 2 != 0:
                    product *= arg[i]
            print("Произведение элементов с нечетными номерами:", product)

            max_value = max(arg)
            arg.remove(max_value)
            print("Новый список после удаления наибольшего элемента:", arg)

        elif isinstance(arg, dict):
            sorted_values = sorted(arg.values(), reverse=True)
            print("Первые три наибольших значения в словаре:", sorted_values[:3])

        elif isinstance(arg, int):
            sum_of_digits = sum([int(digit) for digit in str(arg)])
            print("Сумма цифр числа:", sum_of_digits)

        elif isinstance(arg, str):
            vowels = 0
            consonants = 0
            words = arg.split()

            for word in words:
                for char in word:
                    if char.lower() in 'aeiouаеёиоуыэюя':
                        vowels += 1
                    elif char.isalpha():
                        consonants += 1

            print("Количество гласных в строке:", vowels)
            print("Количество согласных в строке:", consonants)
            print("Количество слов в строке:", len(words))

    process_argument([1, 2, 3, 4, 5])
    process_argument({'a': 10, 'b': 20, 'c': 30, 'd': 40})
    process_argument(12345)
    process_argument("люблю маму")



    # user_input = input("Введите значение: ")
    #
    # try:
    #     user_input = eval(user_input)
    #
    #     result = process_argument(user_input)
    #     print("Результат:", result)
    #
    # except Exception as e:
    #     print("Ошибка ввода:", e)




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
                while True:
                    try:
                        element = int(input(f"Введите элемент [{i}, {j}]: "))
                        row.append(element)
                        break  # Выход из цикла while после успешного ввода
                    except ValueError:
                        print("Введите целое число для элемента матрицы.")
            matrix.append(row)

        neg_column = None
        for j in range(cols):
            is_negative_column = all(matrix[i][j] < 0 for i in range(rows))
            if is_negative_column:
                neg_column = j
                break

        if neg_column is not None:
            sum_of_elements = sum(matrix[i][neg_column] for i in range(rows))
            average = sum_of_elements / rows
            print(f"Первый отрицательный столбец: {neg_column}")
            print(f"Среднее арифметическое элементов этого столбца: {average}")
        else:
            print("В матрице нет столбца, все элементы которого отрицательны.")

        print("Матрица:")
        for i in range(rows):
            for j in range(cols):
                print(matrix[i][j], end='  ')
            print()


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

