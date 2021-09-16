from itertools import count

for el in count(int(input('Введите стартовое число '))):
    if el > 10:
        break
    print(el)

from itertools import cycle

my_list = 0
for el in cycle('asd'):
    if my_list > 10:
        break
    print(el)
    my_list += 1


from itertools import cycle
progr_lang = ['asd', '123', 'bank', 'hello']
iter = cycle(progr_lang)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))