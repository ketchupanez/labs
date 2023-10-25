# Вариант 27

print("\t Меню")

print(" 1. Скопировать из файла F1 в файл F2 все строки, в которых есть слова, совпадающие со вторым словом.\n Определить количество цифр в последней строке файла F2")
print(" 2. Имеется текстовый файл prices.txt с информацией о заказе из магазина. Каждая строка содержит информацию : название, количество единиц, стоимость за ед.\n Определить общую стоимость заказа")

print(" 3. Найти в матрице первый столбец, все элементы которого отрицательны, и среднее арифметическое этих элементов.")
#print(" 4. Напишите программу, демонстрирующую работу try \ except \ finally\n")

def task_1():
    with open("F1.txt", "w") as f1:
        while True:
            a = input("Введите строку (чтобы завершить ввод, введите пустую строку): ")
            if not a: break
            f1.write(a + "\n")

    with open("F1.txt", "r") as f1:
        first_line = f1.readline().strip()
        print(first_line)
        second_word = first_line.split()[1]

    with open("F1.txt", "r") as f1, open("F2.txt", "w") as f2:
        for line in f1:
            if second_word in line:
                f2.write(line)

    with open("F2.txt", "r") as f2:
        lines = f2.readlines()
        last_line = lines[-1] if lines else ""
        num_count = sum(1 for char in last_line if char.isdigit())

        print(f"Количество цифр в последней строке в файле F2 = {num_count}")

def task_2():
    final_cost = 0

    with open("prices.txt", "r", encoding="utf-8") as pr:
        for line in pr:
            par = line.strip().split()

            if len(par) == 3:

                name = par[0]
                kolvo = int(par[1])
                price = int(par[2])
                print(f"Название: {par[0]}, количество единиц: {par[1]}, стоимость за единицу: {par[2]}$")
                line_cost = kolvo * price
                final_cost += line_cost
            else:
                print("Неверный формат данных")

    print(f"Общая стоимость: ${final_cost}\n")


def task_3():
    subject_dict = {}

    with open("univer.txt", "r", encoding="utf-8") as un:
        for line in un:
            par = line.strip().split(":")
            if len(par) == 1:
                subject_name = par[0].split()
                details = par[1].split()
                classes = 0
                # lect = 0
                # practice = 0
                # labs = 0

                for i in details:
                    if "(л)" in i:
                        classes += int(i.replace("(л)", ""))
                    elif "(пр)" in i:
                        classes += int(i.replace("(пр)", ""))
                    elif "(лаб)" in i:
                        classes += int(i.replace("(лаб)", ""))
                    #if i.startswith("лк"):
                     #   lect += 1
                    #elif i.startswith("пр"):
                     #   practice += 1
                    #elif i.startswith("лаб"):
                     #   labs += 1

                #classes = lect + practice + labs
                subject_dict[subject_name] = classes
            else:
                 print("Неверный формат данных")

    for subject, info in subject_dict.items():
        print(f"{subject} - {info} занятий")


def task_4():
    pass


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
