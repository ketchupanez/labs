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
            # Если аргумент - список
            product = 1
            max_value = max(arg)
            new_list = arg[:]
            new_list.remove(max_value)
            return product, new_list

        elif isinstance(arg, dict):
            # Если аргумент - словарь
            sorted_values = sorted(arg.values(), reverse=True)
            top_values = sorted_values[:3]
            return top_values

        elif isinstance(arg, int):
            # Если аргумент - число
            digits = [int(digit) for digit in str(arg)]
            sum_of_digits = sum(digits)
            return sum_of_digits

        elif isinstance(arg, str):
            # Если аргумент - строка
            vowels = "AEIOUaeiou"
            consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
            vowel_count = sum(1 for char in arg if char in vowels)
            consonant_count = sum(1 for char in arg if char in consonants)
            words = len(arg.split())
            return vowel_count, consonant_count, words

        else:
            return "Тип аргумента не поддерживается"




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

