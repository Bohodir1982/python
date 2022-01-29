def head():
    print('Расчет Зарплаты!')
def calc():
    time = int(input('Выработка в часах - '))
    salary = int(input('Ставка в часах - '))
    bonus = int(input('Премия - '))
    return time * salary + bonus