from tkinter import *
from User_Model import User
# from WINDOW import MainWindow
from Post_Login import *

# this has functions used throughout login and signup
class Authentication:
    def __init__(self, root):
        self.root = root
        # users is initialized from accounts.txt
        self.users = []
        self.read_file("/Users/vish/Desktop/Computer Sicence IB/CS_Projects/OOP/accounts.txt")

    # if the user wants to quit the app
    def exit_handle(self):
        quit()

    # new user info is added to accounts.txt
    def write_to_file(self, file_name):
        with open(file_name, 'w') as file_out:
            for user in self.users:
                user_account = user.get_username() + ',' + \
                               user.get_password() + ',' + \
                               user.get_email() + ',' + \
                               str(user.is_admin()) + ',' + '\n'
                file_out.write(user_account)

    # exisiting user are uploaded to list "users"
    def read_file(self, file_name):
        with open(file_name, 'r') as file_in:
            lines = file_in.readlines()
            for line in lines:
                if line != '\n':
                    new_list = line.split(',')
                    new_user = User(new_list[0], new_list[1], new_list[2], new_list[3])
                    self.users.append(new_user)

    # searches whether the username is available or not
    def search_user(self, username):
        index = -1
        i = 0
        for user in self.users:
            if str(user.get_username()).lower() == username.lower():
                index = i
                break

            i = i + 1
        return index

    # it checks if the password of user matches
    def authentication(self, user_index, user_password):
        correct_pass = False
        user = self.users[user_index]
        if user.get_password() == user_password:
            correct_pass = True
        return correct_pass

    # it returns the status 1 (user doesnt exist), 2(wrong password), and 3(succesful login)
    def login_handle(self, account_name, account_pwd):
        u_index = self.search_user(account_name)
        if u_index == -1:
            return 1
        else:
            auth_pass = self.authentication(u_index, account_pwd)
            if auth_pass:
                return 2
            else:
                return 3

    # adds a new item to the list "users"
    def add_newuser(self, username, password):
        new_list = [username, password, "", ""]
        new_user = User(new_list[0], new_list[1], new_list[2], new_list[3])
        self.users.append(new_user)

# displays the "Login" window
class Login:
    def __init__(self, root):
        # self.frame = Tk()
        self.root = root
        self.root.withdraw()
        self.frame = Toplevel()
        self.frame.title("Welcome! Please Login.")
        self.frame.geometry("500x500")
        self.users = []
        self.frame.configure(bg="teal")

        # gives welcome msg
        self.lbl_welcome = Label(self.frame, text="~*~  Welcome to Vishnu's app ~*~", bg="green", fg="black", font=("arial","20"), relief='raised')
        self.lbl_welcome.pack()

        # gives instructions
        self.lbl_info = Label(self.frame, text="If you have an account, Login, else go to sign up and then login", font=("arial",14))
        self.lbl_info.pack(pady=20)

        # displays label and tells them to enter username
        self.lbl_username = Label(self.frame, text="Enter your username: ", bg="orange", fg="black", relief='raised')
        self.lbl_username.pack(pady=5)

        # textbox where the user enters their username
        self.txt_username = Entry(self.frame)
        self.txt_username.pack()

        # displays label and tells them to enter password
        self.lbl_password = Label(self.frame, text="Enter your password: ", bg="orange", fg="black", relief='raised')
        self.lbl_password.pack(pady=5)

        # textbox where the user enters their username
        self.txt_password = Entry(self.frame)
        self.txt_password.pack()

        # after they enter all details, they press login
        self.btn_login = Button(self.frame, text="Login", command=self.login_wrapper, fg="green")
        self.btn_login.pack(pady=20)

        # There is a signup button if they dont have an account.
        self.btn_signup = Button(self.frame, text="Sign up", command=self.signup, fg="purple")
        self.btn_signup.pack(pady=20)

        # just tells them to input their details above
        self.lbl_status = Label(self.frame, text="Login above.", fg="magenta")
        self.lbl_status.pack(pady=10)

        # if they want to exit, they press this button
        self.btn_exit = Button(self.frame, text="Exit", command=self.exit_handle, fg="crimson")
        self.btn_exit.pack(pady=20)

    # this function calls the method login_handle from "Authentication"
    def login_wrapper(self):
        auth = Authentication(self.root)
        status = auth.login_handle(self.txt_username.get(), self.txt_password.get())
        if status == 1:
            self.lbl_status.config(text="Username does not exist", fg="red")
        elif status == 2:
            self.lbl_status.config(text=f"Welcome, {self.txt_username.get().title()}", fg="green")
            from OOP_Projects.Post_Login import Mainmenu
            Mainmenu(self.root, self.txt_username.get())
            self.frame.destroy()
        else:
            self.lbl_status.config(text="Incorrect password!!", fg="red")

    # goes to the signup window
    def signup(self):
        Signup(self.root)
        self.frame.destroy()

    # they can quit the app
    def exit_handle(self):
        quit()


# Displays a new window, and has functions that makes them sign up
class Signup:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()
        self.currentWindow = Toplevel()
        self.currentWindow.title("Sign up Window")
        self.currentWindow.geometry("700x500")
        self.currentWindow.configure(bg="lightseagreen")

        # gives them instructions
        self.lbl_instruct = Label(self.currentWindow, text="Please enter a username, password, and repeat the password again", font=("arial", 20), fg="gold", relief='raised')
        self.lbl_instruct.pack()

        # label that tells them to enter a username
        self.lbl_username1 = Label(self.currentWindow, text="Enter a username", fg="black", bg="orange", relief='raised')
        self.lbl_username1.pack(pady=5)

        # textbox where they enter username
        self.txt_username1 = Entry(self.currentWindow)
        self.txt_username1.pack()

        # label that tells them to enter password
        self.lbl_password1 = Label(self.currentWindow, text="Enter a password", fg="black", bg="orange", relief='raised')
        self.lbl_password1.pack(pady=5)

        # textbox where they enter password
        self.txt_password1 = Entry(self.currentWindow)
        self.txt_password1.pack()

        # label that tells them to re-enter password
        self.lbl_confirmpass = Label(self.currentWindow, text="Retype the password", fg="black", bg="orange", relief='raised')
        self.lbl_confirmpass.pack(pady=5)

        # textbox where they re-enter password
        self.txt_confirmpass = Entry(self.currentWindow)
        self.txt_confirmpass.pack()

        # Submits their details
        self.btn_submit = Button(self.currentWindow, text="Sign Up", command=self.signup_wrapper, fg="darkgreen")
        self.btn_submit.pack(pady=20)

        # gives them an instruction on where to sign up
        self.lbl_status = Label(self.currentWindow, text="Sign Up above.", fg="lime")
        self.lbl_status.pack(pady=10)

        # if they want to exit, they press this button
        self.btn_exit = Button(self.currentWindow, text="Exit", command=self.exit_handle, fg="crimson")
        self.btn_exit.pack(pady=20)

    # they can quit the app
    def exit_handle(self):
        quit()

    def signup_wrapper(self):
        # checks if the username exists
        self.auth = Authentication(self.root)
        index = self.auth.search_user(self.txt_username1.get())
        # displays error msg if the username exists
        if index != -1:
            self.lbl_status.config(text="Username already exists, Retry", fg="red")
        # if they leave username/ password blank, it shows error msg
        elif len(self.txt_username1.get()) != 0 and len(self.txt_password1.get()) != 0:
            # if re-entered password matches it prompts them back to Login and updates accounts.txt
            if self.txt_confirmpass.get() == self.txt_password1.get():
                self.auth.add_newuser(self.txt_username1.get(), self.txt_password1.get())
                self.auth.write_to_file("/Users/vish/Desktop/Computer Sicence IB/CS_Projects/OOP/accounts.txt")
                Login(self.root)
                self.currentWindow.destroy()
            # if password doesnt match, they have to re-enter password again
            else:
                self.lbl_status.config(text="ERROR, Re-enter both passwords", fg="red")
        # the error msg is displayed here if username/password is left empty
        else:
            self.lbl_status.config(text="Can't leave username and password blank!", fg="red")

# this code allows the file to be used as a module (importable)
if __name__ == "__main__":
    root = Tk()
    root.title("Begin the app!")
    root.geometry("500x300")
    root.configure(bg="saddlebrown")
    def go():
        Login(root)
    def close():
        root.destroy()

    photo = PhotoImage(file="Press button.png")
    img_lbl = Label(root, image=photo)
    img_lbl.pack()

    btn_start = Button(root, text="COMMENCE THE APP", command=go, fg="lawngreen")
    btn_start.pack(pady=10)

    btn_leave = Button(root, text="EXIT", command=close, fg="orangered")
    btn_leave.pack(pady=10)

    root.mainloop()
