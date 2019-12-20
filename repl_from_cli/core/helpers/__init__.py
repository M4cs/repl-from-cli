def ask_yes_no(prompt):
    while True:
        answer = input(str(prompt + ' [Y\\N]: '))
        if answer.lower() == 'y':
            return True
        elif answer.lower() == 'n':
            return False
        else:
            print('Please Choose Y or N')