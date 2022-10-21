from logg import saverecordtologfile as sr


def fill_teachers(num=0):
    data = []
    features = {'person\'s id': '', 'name': '', 'surname': '', 'phone number': '', 'description': ''}
    num += 1
    while True:
        if input('To exit the program, press "Q", to continue "Enter": ').upper() == 'Q':
            break
        f_copy = features.copy()
        for f in features:
            if f == 'person\'s id':
                f_copy[f] = num
                num += 1
            else:
                answer = input(f'Enter property value "{f}": ')  # Enter value
                f_copy[f] = answer
        data.append(f_copy)
        sr(["add new person", "full contact", f"{data}"])
    return data
