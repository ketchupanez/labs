# #Вариант 27
#
print("\t Меню")

print(" 1. Посчитать кол-во четных/нечетных цифр \n 2. Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в веденном с клавиатуры слове. ")
print(" 3. Найти произведение элементов списка с нечетными номерами. \n 4. Отсортировать словарь по ключу в порядке возрастания")
print(" 5. Магазин игрушек \n 6. Кортеж")

a = int(input("\nВыберите значение: "))
if a == 1:

        num = int(input("Введите число: "))
        even = 0  # четные
        odd = 0  # нечетные

        num_str = str(num)

        for i in num_str:
            if int(i) % 2 == 0:
                even += 1
            else:
                odd += 1

        print("Четных:", even, "а Нечетных:", odd)

elif a == 2:
    word = input("Введите слово: ")

elif a == 3:

    elements = input("Введите элементы списка через пробел: ").split()
    print(elements)
    # Преобразуем элементы в числа
    elements = [int(x) for x in elements]

    product_odd = 1
    for i in range(0, len(elements), 2):
        product_odd *= elements[i]

    print("Произведение элементов с нечетными номерами:", product_odd)

    max_element = max(elements)
    while max_element in elements:
        elements.remove(max_element)

    print("Список без наибольшего элемента:", elements)


elif a == 4:
     my_dict = {'a': 50, 'c': 5, 'd': 56, 'e': 4, 'f': 58, 'z': 20}
     print(my_dict)

     sorted_dict = dict(sorted(my_dict.items(), key=lambda items: items[1]))
     print("\nОтсортированный по возрастанию значений список: ", sorted_dict)

     print("Первые три элемента нового списка: ", list(sorted_dict.values())[0:3])


elif a == 5:
     toy_shop = {
         "Акула": ["акула", 68, 4],
         "Попит": ["попит", 7, 9],
         "Капибара": ["капибара", 19, 3],
         "Скибиди Туалет": ["скибиди туалет", 103, 5],
     }

     def display_description():
         print("\nОписание товара: ")
         for item, info in toy_shop.items():
             print(f"{item} - {info[0]}")


     def display_price():
         print("\nСтоимость игрушек: ")
         for item, info in toy_shop.items():
             print(f"{item} - {info[1]} руб.")


     def display_quantity():
         print("\nКоличество товаров в наличии:")
         for item, info in toy_shop.items():
             print(f"{item} - {info[2]} шт.")


     def display_all_info():
         print("\nИнформация о товарах:")
         for item, info in toy_shop.items():
             print(f"{item}:")
             print(f"  Описание: {info[0]}")
             print(f"  Цена: {info[1]} руб.")
             print(f"  Количество: {info[2]} шт.")


     def purchase():
         total_cost = 0
         while True:
             item_name = input("Введите название изделия (или 'z' для выхода): ")
             if item_name == 'z':
                 break
             if item_name in toy_shop:
                 quantity_to_buy = int(input(f"Введите количество {item_name}, которое хотите купить: "))
                 if quantity_to_buy > toy_shop[item_name][2]:
                     print(f"Данное кол-во товара отсутствует на складе {item_name}")
                 else:
                     cost = quantity_to_buy * toy_shop[item_name][1]
                     total_cost += cost
                     toy_shop[item_name][2] -= quantity_to_buy
                     print(f"Вы купили {quantity_to_buy} штук {item_name} за {cost} руб.")
             else:
                 print(f"Товар {item_name} отсутствует в продаже.")

         print(f"Итого к оплате: {total_cost} руб.")
         display_quantity()


     while True:
         print("\nМеню:")
         print("1. Просмотр описания")
         print("2. Просмотр цены")
         print("3. Просмотр количества")
         print("4. Вся информация")
         print("5. Покупка")
         choice = input("Выберите пункт меню (или 'z' для выхода): ")

         if choice == '1':
             display_description()
         elif choice == '2':
             display_price()
         elif choice == '3':
             display_quantity()
         elif choice == '4':
             display_all_info()
         elif choice == '5':
             display_all_info()
             purchase()
         elif choice == 'n':
             break
         else:
             print("Введите корректное число!")

else :
     print("Дан кортеж:")
     tuple = (-1, 0, -44, -3, -79, -51, -22, -58)
     print(tuple)

     positive = False
     sum = 0

     for i in tuple:
             if positive:
                 sum += i
                 print("Сумма элементов после первого положительного числа:", sum)
             elif i > 0:
                 print("Первое положительное: ", i)
                 positive = True
             else:
                 print("Положительных чисел нет")
             break




