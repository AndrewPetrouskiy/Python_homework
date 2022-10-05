#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def get_positive_int():
    while True:
        try:
            reply = int(input("Enter a number of fibanacci "))
            if reply > 0:
                return reply
            else:
                print("This number isn't positive")
        except:
            print("Not a number... Try again")


def all_fibanacci(n):
    fib1 = 0
    fib2 = 1
    n = n - 2
    temp = -1
    fib = [fib2, fib1, fib2]
    for i in range(0, n):
        fib1, fib2 = fib2, (fib1 + fib2)
        fib.append(fib2)
        fib3 = fib2 * temp
        temp *= -1
        fib.insert(0, fib3)
    return fib


number = get_positive_int()
print(all_fibanacci(number))


    
#============================== Teacher's solution==============================================

# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def neg_fib(num: int):
    a, b = 1, 1
    list_nums = [0]

    for i in range(num):
        list_nums.append(a)
        list_nums.insert(0, a * (-1) ** i)
        a, b = b, b + a

    return list_nums


print(*neg_fib(int(input())))




 
 

