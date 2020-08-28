from dateutil import parser
from services import data_services as svc
from random import randint
from data.employees import Employee


def get_pfno():
    case = True
    i = '0001'
    while case:
        pfs = list(str(Employee.objects().filter().only('PF_No')))
        if i in pfs:
            a = str(randint(0, 9))
            b = str(randint(0, 9))
            c = str(randint(0, 9))
            d = str(randint(0, 9))
            i = a + b + c + d
        else:
            case = False
            return i


def set_password():
    case = True
    while case:
        value1 = input("Please set up a password.")
        value2 = input("Please re-enter the password")
        if value1 != value2:
            case = True
            print("passwords do not match")
        else:
            return value1


def main():
    print("Welcome.Please enter your details to create your account:")
    first_name = input("Please enter your first name:")
    sur_name = input("Please enter your middle name:")
    middle_name = input("Please enter your sur name:")
    age = int(input("Please provide your age:"))
    Nat_Id_No = input("Please enter your National Id No:")
    gender = input("Please enter your gender [m/f]").lower()
    DOB = parser.parse(
        input("Please enter your date of birth: [yyyy-mm-dd]")
    )
    employee_level = input('Please enter your employee level:')
    PF_No = get_pfno()
    password = set_password()

    new_account = svc.createaccount(first_name, middle_name, sur_name, age, Nat_Id_No, gender, DOB,
                                    employee_level, PF_No, password)

    print(f'Account successfully created with PF No.{new_account.PF_No} and password:{new_account.password}')
    print("Please remember these credentials as you will need them to log in!")
