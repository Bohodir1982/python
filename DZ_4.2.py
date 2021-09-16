my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_new_list = [el+10 for el in my_list]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')

# пример 2
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(my_list)
my_new_list = [el for el in my_list if el % 2 == 0]
print(my_new_list)

# пример 3
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')

# привел несколько примеров но не могу найти способ как с ответа убрать число 300.