from random import choices , sample

# Task 1


def get_positive_int():
    while True:
        try:
            reply = int(input("Enter a positive number ... "))
            if reply > 0:
                return reply
        except:
            print("Not a positive number... Try again")


def get_int():
    while True:
        try:
            reply = int(input("Enter the number ... "))
            return reply
        except:
            print("Not a number... Try again")


def fill_array(num):
    array = random.sample(range(num*2), num)
    print(array)
    return array


def find_number_in_array(array, num):
    if num in array:
        print(f"The desired number {desired_number} has in array")
    else:
        print(f"The desired number {desired_number} haven't in array")


# number = get_positive_int()
# desired_number = get_int()
# find_number_in_array(fill_array(number), desired_number)


# Task 2

def fill_string_array(num, source):
    array = []
    for i in range(num):
        temp = choices(source, k=3)
        array.append("".join(temp))
    return array

def find_second_encounter(array, word):
    if array.count(word) > 1:
        first_encounter = array.index(word)
        print(f"The second encounter: {array.index(word, first_encounter + 1)}")
    else:
        print(-1)

number = get_positive_int()
source_word = input("Enter the source word ")
words = fill_string_array(number, source_word)
print(words)
find_second_encounter(words, input("Enter the desire word "))
