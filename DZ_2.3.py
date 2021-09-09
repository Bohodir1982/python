seasons_list = [['Зима', ['12', '1', '2']], ['Весна', ['3', '4', '5']], ['Лето', ['6', '7', '8']], ['Осень', ['9', '10', '11']]]

seasons_dict = {'Зима': ['12', '1', '2'], 'Весна': ['3', '4', '5'], 'Лето': ['6', '7', '8'], 'Осень': ['9', '10', '11']}

while True:
    month_number = input('Введите номер месяца: ')
    if month_number not in sum(seasons_dict.values(), []):
        print('Неправильно введенный номер месяца. Попробуйте еще раз')

    break
for season, months in seasons_list:
    if month_number in months:
        print(f'Определено, что месяц за номером по списку {month_number} это {season}')

for season, months in seasons_dict.items():
    if month_number in months:
        print(f'Определено, что месяц за номером по словарю {month_number} это {season}')
