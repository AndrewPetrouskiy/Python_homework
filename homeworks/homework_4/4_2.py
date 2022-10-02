# Task 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N


def get_positive_int():
    while True:
        try:
            reply = int(input("Enter a positive number ... "))
            if reply >= 0:
                return reply
            else:
                print("This number isn't positive")
        except:
            print("Not a number... Try again")


def find_all_prime_factors_of_number(n):
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            n //= d
        else:
            d += 1
    factors.append(n)
    return factors


number = get_positive_int()
factors = find_all_prime_factors_of_number(number)
# Выводим исходное число и все простые множители.
print(f'{number} = {factors}')
