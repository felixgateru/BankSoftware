from data.employees import Employee


def createaccount(first_name, middle_name, sur_name, age, Nat_Id_No,
                  gender, DOB, employee_level, PF_No, password) -> Employee:
    x = Employee()
    x.first_name = first_name
    x.middle_name = middle_name
    x.sur_name = sur_name
    x.age = age
    x.Nat_Id_No = Nat_Id_No
    x.gender = gender
    x.DOB = DOB
    x.level = employee_level
    x.PF_No = PF_No
    x.password = password

    x.save()

    return x
