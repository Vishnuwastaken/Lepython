from tkinter import *


class MyLogin:
    def __init__(self):
        self.users = {'admin': '1234567890', 'bob': 'password'}
        self.frame = Tk()
        self.frame.title("My own login")
        self.frame.geometry("500x300")

        self.lbl_username = Label(text="Enter your username: ")
        self.lbl_username.grid(row=0, column=0)

        self.txt_username = Entry()
        self.txt_username.grid(row=0, column=1)

        self.lbl_password = Label(text="Enter your password: ")
        self.lbl_password.grid(row=1, column=0)

        self.txt_password = Entry()
        self.txt_password.grid(row=1, column=1)

        self.btn = Button(text="GO", command=self.click_go)
        self.btn.grid(row=2, column=1)

    def click_go(self):
        username = self.txt_username.get()
        password = self.txt_password.get()
        self.lbl_welcome = Label(text=f"Welcome {username.title()}")
        self.lbl_wrongpass = Label(text="WRONG PASSWORD")
        self.lbl_wrongname = Label(text="Name does not exist")

        if username in self.users:
            if self.users[username] == password:
                self.lbl_welcome.config(text=f"Welcome {username.title()}")
                self.lbl_wrongpass.config(text="")
                self.lbl_wrongname.config(text="")

                self.lbl_welcome.grid(row=3, column=1, sticky='w')
            else:
                self.lbl_welcome.config(text="")
                self.lbl_wrongname.config(text="")
                self.lbl_wrongpass = Label(text="WRONG PASSWORD")
                self.lbl_wrongpass.grid(row=3, column=1, sticky='w')
        else:
            self.lbl_welcome.config(text="")
            self.lbl_wrongpass.config(text="")
            self.lbl_wrongname.config(text="Name does not exist")
            self.lbl_wrongname.grid(row=3, column=1, sticky='w')



    def run(self):
        self.frame.mainloop()

Window1 = MyLogin()
Window1.run()
