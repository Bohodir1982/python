var_list = []

while True:
    item = input('Пожалуйста введите значение - ')
    var_list.append(item)

    q = input('Значние сформировано? (y/N)) ')
    if q.lower() == 'y':
        break

last_idx = len(var_list) - 2

for idx, _ in enumerate(var_list):
    if idx % 2 == 0 and idx < last_idx:
        var_list[idx + 1], var_list[idx] = var_list[idx:idx + 2]

print(var_list)