# Task 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.


def get_positive_int() -> int:
    while True:
        try:
            reply = int(input("Enter how many elements must be in the list ... "))
            if reply > 0:
                return reply
            else:
                print("This number isn't positive")
        except:
            print("Not a number... Try again")

def fill_list(num: int) -> list:
    return [i for i in range(20, num + 1) if i %20 == 0 or i % 21 == 0]


print(fill_list(get_positive_int()))