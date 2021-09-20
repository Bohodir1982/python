def emp_sal():
    try:
        time = float(input('Выработка в часах - '))
        salary = int(input('Ставка в часах - '))
        bonus = int(input('Премия - '))
        res = (time * salary) + bonus
        print(f'заработная плата сотрудника  {res}')
    except ValueError:
        return print('Not a number')

emp_sal()

# пример 2
#использования скрипта
from lesson_4.me_math1 import my_math_eq
print(my_math_eq(10, 10, 5))


# пример 3
import модуль
модуль.head()
print(модуль.calc())