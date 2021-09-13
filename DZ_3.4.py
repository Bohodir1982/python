# пример №1
def my_func(num_1, deg_1):
    return num_1 ** deg_1
print(my_func(4, 4))

# пример №2
def my_func(num_1, deg_1):
    num_1 = int(input('Введите число - '))
    deg_1 = int(input('Введите степень - '))
    return num_1 ** deg_1
print(my_func((), ()))
#
# # пример №3
print ('pow(100, 2) : ', pow(100, 2))

# пример №4
def my_func(num_1, deg_1):
    p = num_1
    i = -1
    while i > deg_1:
        p = p * num_1
        i -= 1
    if deg_1 == 0:
        p = 1
    return 1 / p


print(my_func(18, -10))
