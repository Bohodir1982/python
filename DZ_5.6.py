subj = {}
with open('file_6.txt', mode='r', encoding='utf-8') as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')

# не могу разобраться с ошибкой
# C:\Python39\python.exe C:/PROJECT/lesson_5/DZ_5.6.py
# Traceback (most recent call last):
#   File "C:\PROJECT\lesson_5\DZ_5.6.py", line 3, in <module>
#     for line in init_f:
#   File "C:\Python39\lib\encodings\cp1251.py", line 23, in decode
#     return codecs.charmap_decode(input,self.errors,decoding_table)[0]
# UnicodeDecodeError: 'charmap' codec can't decode byte 0x98 in position 1: character maps to <undefined>
#
# Process finished with exit code 1