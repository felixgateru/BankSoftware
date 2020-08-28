from data.mongo_setup import mongo_setup
from colorama import Fore
from services import create_account

def start_page():
    print(Fore.GREEN + "*" * 30 + "Welcome to G-Bank Management System" + '*' * 30)
    print(Fore.BLUE + "Today is a good day")
    print('\n', '\n', '\n')
    print(Fore.YELLOW + "Please login or create an account:")


def get_input():
    message = "Do you want to:\n1.Log in\n2.Create account\n3.Exit\n"
    count = 0
    value_str = input(message)
    while count < 2 and not value_str.isnumeric():
        print("Value must be an integer number between 1 and 3!")
        value_str = input(message)
        count = count + 1

    if value_str.isnumeric():
        return int(value_str)


def login():
    print("logged in")



def main():
    mongo_setup()
    start_page()
    choice = get_input()
    if choice is None:
        print("You have exceeded login trials")
    elif choice == 1:
        login()
    elif choice == 2:
        create_account.main()
    elif choice > 2 :
        print("Invalid Entry")


        


if __name__ == '__main__':
    main()

#TODO check how to get input thrice