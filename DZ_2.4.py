while True:
    var_str = ('АКБ Капиталбанк Филиал Апельсин банк')
    if len(var_str) < 3 or var_str.count(' ') < 1:
        print(var_str)
    break

for idx, word in enumerate(var_str.split()):
    print(idx + 1, (word, word[:10])[len(word) > 9])
