from tkinter import *
from OOP_Projects.User_Model import User


class Login:
    def __init__(self, root):
        self.root = root
        self.root.iconify()
        self.curWindow = Toplevel()
        self.curWindow.title("Welcome! Pls login.")
        self.curWindow.geometry("500x500")

        # self.frame = Toplevel()
        # self.frame.title("Welcome! Please Login.")
        # self.frame.geometry("300x200")
        # self.curWindow = Toplevel()

        self.users = []

        self.lbl_welcome = Label(self.curWindow, text="~*~  Welcome to my program ~*~")
        self.lbl_welcome.pack()

        self.lbl_username = Label(self.curWindow, text="Enter your username: ")
        self.lbl_username.pack()

        self.txt_username = Entry(self.curWindow)
        self.txt_username.pack()

        self.lbl_password = Label(self.curWindow, text="Enter your password: ")
        self.lbl_password.pack()

        self.txt_password = Entry(self.curWindow)
        self.txt_password.pack()

        self.btn_login = Button(self.curWindow, text="Login", command=self.login_handle)
        self.btn_login.pack()

        self.lbl_status = Label(self.curWindow, text="Login above.")
        self.lbl_status.pack()

        self.read_file("/Users/vish/Desktop/Computer Sicence IB/CS_Projects/OOP/accounts.txt")

    # def run(self):
    #     self.frame.mainloop()

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


#made it further action
    def login_handle(self):
        account_name = self.txt_username.get()
        u_index = self.search_user(account_name)
        if u_index == -1:
            self.lbl_status.config(text="User doesn't exit. Please try again.", fg="red")
        else:
            auth_pass = self.authentication(u_index)
            if auth_pass:
                self.further_action()

                # Convertor(self.root)
                # self.curWindow.destroy()
            # launch_app()

# added option to convert or exit
    def further_action(self):
        self.btn_convert = Button(self.curWindow, text="Go to Convertor", command=self.convert)
        self.btn_convert.pack()

        self.btn_close = Button(self.curWindow, text="Exit", command=self.close)
        self.btn_close.pack()

    def convert(self):
        Convertor(self.root)
        self.curWindow.destroy()

    def close(self):
        self.curWindow.destroy()
        self.root.destroy()

#made a new convertor to do celc to farenheit or farenheit to celc
class Convertor:
    def __init__(self, root):
        self.root = root
        self.frame = Toplevel()
        self.frame.geometry("500x500")
        self.frame.title("Celsius to Fahrenheit or Fahrenheit to Celsius Convertor")

        self.lbl_temp = Label(self.frame, text="Enter a temperature in Celsius or Fahrenheit")
        self.lbl_temp.pack()

        self.txt_temp = Entry(self.frame, text="Enter a temperature")
        self.txt_temp.pack()

        self.btn_celc = Button(self.frame, text="Celsius", command=self.to_celc)
        self.btn_celc.pack()

        self.lbl_celc = Label(self.frame, text="")
        self.lbl_celc.pack()

        self.btn_fare = Button(self.frame, text="Fahrenheit", command=self.to_fare)
        self.btn_fare.pack()

        self.lbl_fare = Label(self.frame, text="")
        self.lbl_fare.pack()

        self.btn_close = Button(self.frame, text="Exit", command=self.close)
        self.btn_close.pack(pady=40)

    def to_celc(self):
        answer = int(self.txt_temp.get())
        answer = (answer-32)*(5/9)
        self.lbl_celc.config(text=answer)

    def to_fare(self):
        answer1 = int(self.txt_temp.get())
        answer1 = (answer1*9/5)+32
        self.lbl_fare.config(text=answer1)

    def close(self):
        self.frame.destroy()
        self.root.destroy()

root = Tk()


app = Login(root)
root.mainloop()
# app.run()
