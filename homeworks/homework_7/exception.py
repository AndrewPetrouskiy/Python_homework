from logg import saverecordtologfile as sr


def enter_first_menu():
    while True:
        try:
            answer = int(input(
                "1 - add person \n 2 - read the whole list of teachers \n 3 - read one of columns \n"
                " 4 - read one row \n 5 - escape \n Enter please "))
            if 0 < answer < 6:
                return answer
            else:
                sr(["You entered wrong number", "in main menu", f"You entered {answer}"])
                print("You entered wrong number")
        except:
            sr(["You're wrong. Try again", "in main menu", f"You entered not a number"])
            print("You're wrong. Try again")


def enter_column():
    while True:
        try:
            answer = int(input(
                "1 - person's id' \n 2 - name \n 3 - surname \n 4 - phone number \n 5 - description \n 0 return "))
            if 0 <= answer < 6:
                return answer
            else:
                print("You entered wrong number")
                sr(["You entered wrong number", "in main menu", f"You entered {answer}"])
        except:
            print("You're wrong. Try again")
            sr(["You're wrong. Try again", "in main menu", f"You entered not a number"])


def enter_row(my_read):
    while True:
        try:
            answer = int(input(
                f"1- {len(my_read)} \n 0 - return "))
            if 0 <= answer <= len(my_read):
                return answer
            else:
                print("You entered wrong number")
                sr(["You entered wrong number", "in main menu", f"You entered {answer}"])
        except:
            print("You're wrong. Try again")
            sr(["You're wrong. Try again", "in main menu", f"You entered not a number"])
