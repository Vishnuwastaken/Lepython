import json
import ast

spacer = "--**-- --**-- --**-- --**-- --**-- "

print(spacer)
print("Functions Assessment !\n")
print("Welcome to Vishnu's code!\n")
print("This is my modified login system!")
print(spacer)

current_users = []
login_id = ''
admin = {'username': 'admin', 'password': 'guess_me'}
current_users.append(admin)

# current_users = [admin]


def write_to_file(file_name):
    with open(file_name, 'w') as file_out:
        json.dump(current_users, file_out)


def read_file(file_name):
    with open(file_name, 'r') as file_in:
        new_list = ast.literal_eval(file_in.read())
        global current_users
        current_users = new_list


def registration():
    username_verification = False
    while not username_verification:
        username = input("Enter a new username: ").lower().strip()
        u_index = search_user(username)

        if u_index == -1:
            username_verification = True
        else:
            print("Username taken. Please choose a different username.")

    pass_verification = False
    while not pass_verification:
        password = input("Enter a password: ")
        count = 0
        for _ in password:
            count = count + 1

        if count >= 3:
            confirm_password = input("Reenter the password: ")
            if password == confirm_password:
                create_user(username, password)
                pass_verification = True
            else:
                print("Verification Failed. Please enter the same password twice")
        else:
            print("Please enter a password with at least 10 characters.")


def authentication(user_index):
    correct_pass = False
    count = 0
    while not correct_pass and count < 3:
        user_password = input("Enter your password: ")
        user = current_users[user_index]
        if user['password'] == user_password:
            print(f"Welcome, {user['username'].title()}")
            correct_pass = True
        else:
            count = count + 1
            if count == 3:
                print("Authentication failed. Please try again.")
            else:
                print("Incorrect password. Please try gain.")
                print(f"You have {3 - count} attempt(s) left.")

    return correct_pass


def search_user(username):
    index = -1
    i = 0
    for user in current_users:
        if user['username'].lower() == username.lower():
            index = i
            break

        i = i + 1
    return index


def update_password():
    u_id = input('Enter your username: ')
    index = search_user(u_id)
    if index == -1:
        print('Username not found')
    else:
        valid = authentication(index)
        if valid:
            pwd = input('Enter your new password: ')
            user = {'username': u_id, 'password': pwd}
            current_users[index] = user
            print('Your password has been successfully changed!!')
            write_to_file('accounts.txt')
        else:
            print('Incorrect password so access denied. ')


def update_username():
    u_id = input('Enter your username: ')
    index = search_user(u_id)
    if index == -1:
        print('Username not found')
    else:
        valid = authentication(index)
        if valid:
            username_verification = False
            while not username_verification:
                username = input("Enter a new username: ").lower().strip()
                u_index = search_user(username)

                if u_index == -1:
                    username_verification = True
                else:
                    print("Username taken. Please choose a different username.")

            pwd = current_users[index]['password']
            user = {'username': username, 'password': pwd}
            current_users[index] = user
            print('Your username has been successfully changed!!')
            write_to_file('accounts.txt')
        else:
            print('Wrong password!! Access denied!!')


def print_users():
    for i in range(len(current_users)):
        print('USER:', current_users[i]['username'], ', and PASSWORD:', current_users[i]['password'])


def delete_user(user_index):
    u_name = current_users[user_index]['username']
    del current_users[user_index]
    print(u_name, 'has been deleted!!')
    write_to_file('accounts.txt')


def add_user():
    username_verification = False
    while not username_verification:
        username = input("Enter a new username: ").lower().strip()
        u_index = search_user(username)

        if u_index == -1:
            username_verification = True
        else:
            print("Username taken. Please choose a different username.")

    pass_verification = False
    while not pass_verification:
        password = input("Enter a password: ")
        count = 0
        for _ in password:
            count = count + 1

        if count >= 3:
            confirm_password = input("Reenter the password: ")
            if password == confirm_password:
                create_user(username, password)
                pass_verification = True
            else:
                print("Verification Failed. Please enter the same password twice")
        else:
            print("Please enter a password with at least 10 characters.")


def create_user(username, password):
    new_user = {'username': username, 'password': password}
    current_users.append(new_user)
    write_to_file('accounts.txt')
    print(f"{username.title()} has been added.")
    print('Your username is: ', new_user['username'])
    print('Your password is: ', new_user['password'])


def show_users():
    for i in range(len(current_users)):
        print(current_users[i]['username'])


def launch_app():
    print('Launching the application...')
    exit()


def display_menu():
    print('Enter one the followings:')
    print('"1" for Login.')
    print('"2" for Registration.')
    print('"3" to Search a User.')
    print('"4" to update Password.')
    print('"5" to update username.')
    print('"6" to print all Users.')
    print('"7" to Delete a User.')
    print('"8" to Add a new User.')
    print('"9 to save all users')
    print('"0 to read all users')
    print('"91" to exit.')
    choice = input('What would you like to do? : ')
    return choice


# main program
separator = '--------------------------'
exit_program = False
print('~*~  Welcome to my program ~*~')
read_file('accounts.txt')
while not exit_program:
    print(separator)
    u_choice = display_menu()
    if u_choice == '1':
        account_name = input("Enter your username: ")
        u_index = search_user(account_name)
        if u_index == -1:
            print("User doesn't exist. Please try again.")
        else:
            auth_pass = authentication(u_index)
            if auth_pass:
                login_id = account_name
                # launch_app()
    elif u_choice == '2':
        registration()
    elif u_choice == '3':
        name = input('Enter a username to search:  ')
        ans = search_user(name)
        if ans == -1:
            print('User not found.')
        else:
            print('User already exists.')
    elif u_choice == '4':
        update_password()
    elif u_choice == '5':
        update_username()
    elif u_choice == '6':
        if login_id == 'admin':
            print_users()
        else:
            print('Only admins can access this')
    elif u_choice == '7':
        if login_id == 'admin':
            name = input('Enter a name to delete: ')
            if name.lower() == 'admin':
                print("Admin can't be deleted")
            else:
                index = search_user(name)
                if index == -1:
                    print('User not found')
                else:
                    delete_user(index)
        else:
            print('Only admin can access this feature!')
    elif u_choice == '8':
        if login_id == 'admin':
            add_user()
        else:
            print('Please login as admin to add user')
    elif u_choice == '9':
        write_to_file('accounts.txt')
        print('Your file has been updated!')
    elif u_choice == '0':
        read_file('accounts.txt')
        print('The information has been inputted')
    elif u_choice == '91':
        print('Okay. Goodbye. See you next time.')
        exit_program = True
    else:
        print("Invalid option. Please try again.")
