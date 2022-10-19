import pandas as pd
from writter import fill_teachers


def read_file():
    my_read = pd.read_csv('demo.csv', index_col=False)
    return my_read


def add_new_person(my_read):
    my_read2 = pd.DataFrame(fill_teachers(len(my_read)))
    my_read3 = pd.concat([my_read, my_read2])
    my_read3.to_csv("demo.csv", index=False)


def len_file():
    my_read = read_file()
    return len(my_read)


def read_column(num2):
    my_read = read_file()
    print(my_read.iloc[:, num2 - 1])


def read_row(num2):
    my_read = read_file()
    print((my_read.iloc[num2 - 1]))
