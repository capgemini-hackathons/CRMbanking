from models.user import create_user, get_users, User
from models.contact import create_contact, Gender
# from models.contract import *
# from models.lead import *
# from models.product import *


class UserAction:
    @classmethod
    def login_user(cls):
        print('Welcome to CRMBanking')
        username1 = input('Enter your name (username): ')
        password1 = input('Enter password: ')
        allusers = User.select().where(User.username == username1).limit(1)
        if len(allusers) != 1:
            print("User or password incorrect!")
        user = allusers[0]
        if user.username == username1:
            if user.password == password1:
                print('Hi, ', username1)
                print("User is logged in")  # LOG start session
                return True
            else:
                print('User or password incorrect!')
                return False
        return False

    @classmethod
    def section(cls):
        print("Choose section!")
        action = input("1 - Contacts, 2 - Contracts, 3 - Leads, 4 - Users, 5 - Products, 0 - Exit: ")
        return action

    @classmethod
    def operation(cls):
        print("Choose operation!")
        action = input(f"1 - Create, 2 - Get, 3 - Import from file, 4 - Export in file, 5 - Sign, "
                       f"9 - Go to Section, 0 - Exit: ")
        return action

    @classmethod
    def operation_create_user(cls):
        username1 = input('Enter username: ')
        password1 = input('Enter password: ')
        msg = create_user(username=username1, password=password1)
        return print(msg)

    @classmethod
    def operation_get_user(cls):
        msgs = get_users()
        print("All users (Id, Created, Username, Password):")
        for msg in msgs:
            print(msg)

    @classmethod
    def operation_create_contact(cls):
        msg = ''
        name1 = input('Enter name: ')
        email1 = input('Enter E-mail: ')
        age1 = input('Enter age: ')
        gender_answer = input('Enter gender (m - male, f - female): ')
        while True:
            if gender_answer == "f":
                msg = create_contact(name=name1, email=email1, age=age1, gender=Gender.female)
            elif gender_answer == "m":
                msg = create_contact(name=name1, email=email1, age=age1, gender=Gender.male)
            else:
                msg = f'Incorrect data. Try again!'
            return print(msg)

    #create contact
    #get contacts

    #create contract
    #get contracts

    # create lead
    # amount1 = input('Enter amount: ')
    # contact_id1 = input('Enter contact_id: ')
    # lead1 = Lead(amount=amount1,contact_id=contact_id1).save()
    # print(lead1)
