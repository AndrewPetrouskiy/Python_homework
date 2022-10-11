# Task 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import os
from itertools import groupby



def rle_coding(data1):
    groups = []
    for key, grp in groupby(data1):
        count = 0
        for i in grp:
            count += 1
        groups.append(count)
        groups.append(key)
    return "".join(map(str, groups))


def rle_decode(data1):
    decode = ''
    count2 = ''
    for el in data1:
        if el.isdigit():
            count2 += el
        else:
            decode += el * int(count2)
            count2 = ''
    return decode


if os.path.exists('text_words.txt'):
    with open('text_words.txt', "r", encoding="utf-8") as text:
        data = text.read()
else:
    print("file with name 'text_words.txt' doesn't exist")


result = rle_coding(data)
result2 = rle_decode(result)
print(result2)

if os.path.exists('text_code_words.txt'):
    with open('text_code_words.txt', "r", encoding="utf-8") as text2:
        result2 = text2.read()
else:
    with open('text_code_words.txt', "a", encoding="utf-8") as text2:
        text2.write(result)
