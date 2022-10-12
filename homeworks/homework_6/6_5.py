# Task 5. ** Реализовать функцию, возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)

from random import randint, choice

nouns = ["автомобиль", "лес", "огонь", "город",
         "дом", "мороженное", "вода", "еда"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера",
           "ночью", "когда-то", "где-то", "чем-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный",
              "мягкий", "черный", "красный", "прикольный"]


def get_positive_int():
    while True:
        try:
            reply = int(input("Enter how many jokes do you want to get ... "))
            if reply > 0:
                return reply
        except:
            print("Not a positive number... Try again")


def create_jokes(noun: list, adverb: list, adjective: list, count: int, unique=False) -> list:
    result = []
    if unique:

        if count > len(noun) or count > len(adverb) or count > len(adjective):
            print("We can't create so much jokes")

        else:
            for i in range(count):
                result.append(f"{noun.pop(randint(0, len(noun) - 1))} " 
                              f"{adverb.pop(randint(0, len(adverb) - 1))} " 
                              f"{adjective.pop(randint(0, len(adjective) - 1))}")

    else:

        for i in range(count):
            result.append(
                f"{choice(noun)} {choice(adverb)} {choice(adjective)}")
    return result


print(create_jokes(nouns, adverbs, adjectives, get_positive_int(), unique=True))
print("")
print(create_jokes(nouns, adverbs, adjectives, get_positive_int()))
