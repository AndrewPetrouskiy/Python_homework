# Task 5. ** Даны два файла, в каждом из которых находится запись многочленов.
# Задача - сформировать файл, содержащий сумму многочленов.

with open("polynomial.txt", "r", encoding="utf-8") as text, \
        open("polynomial2.txt", "r", encoding="utf-8") as text2:
    lines = text.readlines()
    lines2 = text2.readlines()
    if len(lines) == len(lines2):
        lines = [x.replace('= 0\n', '+ ') for x in lines]
        lines3 = []
        for i in range(3):
            if i == i:
                lines3.append(lines[i]+lines2[i])

        with open("polynomial3.txt", "a", encoding="utf-8") as text3:
            for i in lines3:
                text3.write(i)
