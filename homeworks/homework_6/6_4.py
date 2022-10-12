# Task 4  Функция принимает в качестве аргументов строки в формате «Имя Фамилия», возвращает словарь, 
# ключи — первые буквы фамилий, значения — словари, реализованные по схеме предыдущего задания.


source_list = ["Иван Сергеев", "Инна Серова", "Петр Алексеев",
"Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
"Борис Аркадьев", "Антон Серов", "Павел Анисимов"]

def sorted_dict(ls: list) -> dict:
    my_dict = dict()
    for i in ls:
        name, surname = str(i).split()
        if surname[0] in my_dict:
            if name[0] in my_dict[surname[0]]:
                my_dict[surname[0]][name[0]].append(str(i))
            else: my_dict[surname[0]][name[0]] = [i]
        else:
            my_dict[surname[0]] = {name[0] : [i]}
    sorted_dict = sorted(my_dict.items())
    print(sorted_dict)

sorted_dict(source_list)


