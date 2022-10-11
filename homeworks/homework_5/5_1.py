# Task 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.

from random import choices


def get_positive_int():
    while True:
        try:
            reply = int(input("Enter a positive number ... "))
            if reply > 0:
                return reply
        except:
            print("Not a positive number... Try again")


def fill_string_array(num, source):
    array = []
    for i in range(num):
        temp = choices(source, k=3)
        array.append("".join(temp))
    my_str = " ".join(array)
    return my_str

def enter_ABC():
    while True:
        try:
            word = input("Enter 'ABC' 'BAC' 'CBA' 'BCA' 'ACB' 'CAB' ")
            if word in 'ABC' 'BAC' 'CBA' 'BCA' 'ACB' 'CAB':
                return word
        except:
            print("You don't enter 'ABC' 'BAC' 'CBA' 'BCA' 'ACB' 'CAB'")
 

words = fill_string_array(get_positive_int(), enter_ABC())
print(words)
return_words = words.replace("ABC ", '')
print(return_words)
