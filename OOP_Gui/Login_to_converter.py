from tkinter import *


class Login1:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("Login to converter")

        self.lbl_login = Label("Username")
        self.lbl_login.pack()

        self.txt_login = Entry(text="Enter your username")
        self.txt_login.pack()

        self.lbl_password = Label("Password")
        self.lbl_password.pack()

        self.txt_password = Entry(text="Enter your password")
        self.txt_password.pack()

    def run(self):
        self.root.mainloop()


obj = Login1()
obj.run()
