# Создание файла, с автоматический закрытием в конце.
# with open('file.txt', 'w') as data:
#  data.write('line 1\n')
#  data.write('line 2\n')


# дабавление файлов в файл. с ручным закрытием в конце.
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.close()

# считывание файла.
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#  print(line)
# data.close()



# count = 3 - это значение по умолчанию.
# def new_string(symbol, count = 3):
#  return symbol * count

# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!!
# print(new_string(4)) # 12


# рекурсия. 
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1, 40):
#     list.append(fib(e))
# print(list)

# for e in range(1,40):
#     print(fib(e))



#картеж
t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue))

