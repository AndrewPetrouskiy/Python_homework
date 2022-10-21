import os.path
import pandas as pd
import exception as ex
import user_interface as ui
import reading
from writter import fill_teachers
from logg import saverecordtologfile as sr


def main():
    ui.greeting()
    ui.first_menu()

    while True:
        num = ex.enter_first_menu()
        if num == 1:
            my_read = reading.read_file()
            reading.add_new_person(my_read)
        elif num == 2:
            my_read = reading.read_file()
            print(my_read)
            sr(["You entered the readinf of file", f"in main menu you entered {num}", "completed successfully"])
        elif num == 3:
            ui.choose_column()
            my_read = reading.read_file()
            num2 = ex.enter_column()
            sr(["You choose to look at the column", f"in main menu you entered {num}", f"you entered the column {num2}"])
            if num2 == 0:
                num = ex.enter_first_menu()
            else:
                reading.read_column(num2)
        elif num == 4:
            ui.choose_row()
            my_read = reading.read_file()
            num2 = ex.enter_row(my_read)
            sr(["You choose to look at the row", f"in main menu you entered {num}", f"you entered the row {num2}"])
            if num2 == 0:
                num = ex.enter_first_menu()
            else:
                reading.read_row(num2)
        elif num == 5:
            ui.exit_list()
            sr(["press exit", f"in main menu you entered {num}", "The program ended"])
            break




if os.path.exists('phone.csv'):
    main()
else:
    print("We don't have any teachers. let's add them")
    my_df = pd.DataFrame(fill_teachers())
    my_df.to_csv('phone.csv', index=False)
    main()
