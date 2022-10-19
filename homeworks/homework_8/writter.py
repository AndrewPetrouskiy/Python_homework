import pandas as pd


def fill_teachers(num=0):
    ls2 = []
    features = {'teacher"s id': '', 'name': '', 'surname': '', 'subject': '', 'classroom': '', 'age': ''}
    num += 1
    while True:
        if input('To exit the program, press "Q", to continue "Enter": ').upper() == 'Q':
            break
        f_copy = features.copy()
        for f in features:
            if f == 'teacher"s id':
                f_copy[f] = num
                num += 1
            else:
                answer = input(f'Enter property value "{f}": ')  # Enter value
                f_copy[f] = answer
        ls2.append(f_copy)
    return ls2



for_example = [
    {'teacher"s id': '1', 'name': 'Aurora', 'surname': 'Sinistra', 'subject': ' астрономия',
     'classroom': 'Астрономическая башня',
     'age': '48'},
    {'teacher"s id': '2', 'name': 'Quirinus', 'surname': 'Quirrell', 'subject': 'Защита от Тёмных искусств',
     'classroom': '3 башня',
     'age': '38'},
    {'teacher"s id': '3', 'name': 'Gilderoy', 'surname': 'Lockhart', 'subject': 'Защита от Тёмных искусств',
     'classroom': '3 башня',
     'age': '53'},
    {'teacher"s id': '4', 'name': 'Remus', 'surname': 'Lupin', 'subject': 'Защита от Тёмных искусств',
     'classroom': '3 башня', 'age': '42'},
    {'teacher"s id': '5', 'name': 'Alastor', 'surname': 'Moody', 'subject': 'Защита от Тёмных искусств',
     'classroom': '3 башня',
     'age': '64'},
    {'teacher"s id': '6', 'name': 'Dolores', 'surname': 'Umbridge', 'subject': 'Защита от Тёмных искусств',
     'classroom': '3 башня',
     'age': '52'},
    {'teacher"s id': '7', 'name': 'Severus', 'surname': 'Snape', 'subject': 'Защита от Тёмных искусств',
     'classroom': '3 башня',
     'age': '42'},
    {'teacher"s id': '8', 'name': 'Horace', 'surname': 'Slughorn', 'subject': 'Зельеваренье', 'classroom': 'cover',
     'age': '66'},
    {'teacher"s id': '9', 'name': 'Minerva', 'surname': 'McGonagall', 'subject': 'Трансфигурация',
     'classroom': 'башня Грифиндор',
     'age': '72'},
    {'teacher"s id': '10', 'name': 'Rolanda', 'surname': 'Hooch', 'subject': 'полет на метле', 'classroom': 'стадион',
     'age': '45'},
    {'teacher"s id': '11', 'name': 'Sybill', 'surname': 'Trelawney', 'subject': 'прорицание',
     'classroom': 'башня магии',
     'age': '72'},
    {'teacher"s id': '12', 'name': 'Albus', 'surname': 'Dambldor', 'subject': 'director', 'classroom': 'главная башня',
     'age': '115'}
]
my_df = pd.DataFrame(for_example)
my_df.to_csv('demo.csv', index=False)