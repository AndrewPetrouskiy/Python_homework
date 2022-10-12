# Task 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, 
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.


source_list = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]

def create_and_sorted_dict(ls: list):
    new_dict = dict()
    for i in ls:
        if i[0] not in new_dict:
            new_dict[i[0]] = [i]
        else:
            new_dict[i[0]].append(i)

    sorted_dict = sorted(new_dict.items())
    print(sorted_dict)

create_and_sorted_dict(source_list)








