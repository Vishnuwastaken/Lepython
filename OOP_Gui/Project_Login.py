from tkinter import *
from OOP_Projects.User_Model import User
# from WINDOW import MainWindow
from Guessing_Game import *

class Login:
    def __init__(self, root):
        # self.frame = Tk()
        self.root = root
        self.root.withdraw()
        self.frame = Toplevel()
        self.frame.title("Welcome! Please Login.")
        self.frame.geometry("300x200")
        self.users = []

        self.lbl_welcome = Label(self.frame, text="~*~  Welcome to my program ~*~")
        self.lbl_welcome.pack()

        self.lbl_username = Label(self.frame, text="Enter your username: ")
        self.lbl_username.pack()

        self.txt_username = Entry(self.frame)
        self.txt_username.pack()

        self.lbl_password = Label(self.frame, text="Enter your password: ")
        self.lbl_password.pack()

        self.txt_password = Entry(self.frame)
        self.txt_password.pack()

        self.btn_login = Button(self.frame, text="Login", command= self.login_handle)
        self.btn_login.pack()

        # added sign up button
        # self.btn_signup = Button(self.frame, text="Sign up", command=self.signup)
        # self.btn_signup.pack()


        self.lbl_status = Label(self.frame, text="Login above.")
        self.lbl_status.pack()

        self.btn_exit = Button(self.frame, text="Exit", command=self.exit_handle)
        self.btn_exit.pack()

        self.read_file("/Users/vish/Desktop/Computer Sicence IB/CS_Projects/OOP/accounts.txt")


    def exit_handle(self):
        quit()


    def write_to_file(self, file_name):
        with open(file_name, 'w') as file_out:
            for user in self.users:
                user_account = user.get_username() + ',' + \
                               user.get_password() + ',' + \
                               user.get_email() + ',' + \
                               str(user.is_admin()) + ',' + '\n'
                file_out.write(user_account)
            self.lbl_status.config(text="File output done.", fg="orange")


    def read_file(self, file_name):
        with open(file_name, 'r') as file_in:
            lines = file_in.readlines()
            for line in lines:
                if line != '\n':
                    new_list = line.split(',')
                    new_user = User(new_list[0], new_list[1], new_list[2], new_list[3])
                    self.users.append(new_user)
            self.lbl_status.config(text="File input done.", fg="orange")

    def search_user(self, username):
        index = -1
        i = 0
        for user in self.users:
            if str(user.get_username()).lower() == username.lower():
                index = i
                break

            i = i + 1
        return index


    def authentication(self, user_index):
        correct_pass = False
        count = 0
        while not correct_pass and count < 3:
            user_password = self.txt_password.get()
            user = self.users[user_index]
            if user.get_password() == user_password:
                self.lbl_status.config(text=f"Welcome, {user.get_username().title()}", fg="green")
                correct_pass = True
            else:
                count = count + 1
                if count == 3:
                    self.lbl_status.config(text="Authentication failed. Please try again.", fg="red")
                else:
                    self.lbl_status.config(text=f"Incorrect password. You have {3 - count} attempt(s) left.", fg="red")

        return correct_pass

    def login_handle(self):
        account_name = self.txt_username.get()
        u_index = self.search_user(account_name)
        if u_index == -1:
            self.lbl_status.config(text="User doesn't exit. Please try again.", fg="red")
        else:
            auth_pass = self.authentication(u_index)
            if auth_pass:
                self.frame.destroy()
                Random_Number(root)






# makes them sign up
# class Signup:
#     def __init__(self, root):
#         self.root = root
#         self.root.withdraw()
#         self.currentWindow = Toplevel()
#         self.currentWindow.title("Sign up Window")
#         self.currentWindow.geometry("500x500")
#
#         self.lbl_username1 = Label(self.currentWindow, text="Enter a username")
#         self.lbl_username1.pack()
#
#         self.txt_username1 = Entry(self.currentWindow)
#         self.txt_username1.pack()
#
#         self.lbl_password1 = Label(self.currentWindow, text="Enter a password")
#         self.lbl_password1.pack()
#
#         self.txt_password1 = Entry(self.currentWindow)
#         self.txt_password1.pack()
#
#         self.lbl_confirmpass = Label(self.currentWindow, text="Retype the password")
#         self.lbl_confirmpass.pack()
#
#         self.txt_confirmpass = Entry(self.currentWindow)
#         self.txt_confirmpass.pack()
#
#         self.btn_submit = Button(self.currentWindow, text="Sign Up", command=self.signup1)
#         self.btn_submit.pack()
#
#     def signup1(self):
#         self.auth = Authentication(self.root)
#         self.auth.login_handle(self.txt_username1.get())
#
#
root = Tk()
app = Login(root)
# app.run()
root.mainloop()