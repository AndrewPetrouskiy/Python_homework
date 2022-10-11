# 1. Создайте список из N натуральных чисел(0 до N),
#    упорядоченных по возрастанию. Среди чисел не хватает
#    одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
#    Найдите это число.


# from secrets import choice


# def fill_list(num):
#     array = [i for i in range(num + 1)]
#     array.remove(choice(array))
#     return array



# def check_number(array):

#     for i in range(1, len(array)):
#         if array[i] - 1 != array[i-1]:
#             return array[i] - 1
#     return -1


# array = fill_list(int(input("Enter the positive number")))
# print(array)

# print(check_number(array))


# 2. Создайте список, в который попадают числа,
#    описывающие возрастающую последовательность.
#    Порядок элементов менять нельзя.


from random import choices


def fill_list(num):
    return choices(range(num*2) , k = num)



def find_sublist(ls):
    res = []
    for i in range(len(ls)):
        cur = ls[i]
        cur_ls = [cur]
        for k in range(i, len(ls)):
            if ls[k] > cur:
                cur_ls.append(ls[k])
                cur = ls[k]
        if len(cur_ls) > 1:
            res.append(cur_ls)
    return res  



array = fill_list(int(input("Enter the number")))
print(array)
print(find_sublist(array))


# from os import path
# exists
# from itertools import groupby, starmap

# Эмодзи
# https://unicode-table.com/ru/emoji/




