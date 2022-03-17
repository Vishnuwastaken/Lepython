from tkinter import *
from tkinter import *
import random

# class displays a window and has functions that lets them play the game
class Random_Number:
    def __init__(self, root, username):
        self.root = root
        self.root.iconify()
        self.username = username
        self.currentWindow = Toplevel()
        self.currentWindow.geometry("750x500")
        self.currentWindow.title("My random number guessing game!!")
        self.currentWindow.configure(bg="indigo")

        # gives them instructions
        self.lbl_instructions = Label(self.currentWindow, text=f"Hi {self.username.title()}, You will be given a number from 1-100 and you have to guess the number", font=("arial", 14), fg="gold", relief='raised')
        self.lbl_instructions.pack()

        # instructs them to enter a number between 1-100
        self.lbl_input = Label(self.currentWindow, text="Enter a number between 1-100", relief='raised', fg="darkorange")
        self.lbl_input.pack(pady=20)

        # here, the user enters the number
        self.txt_number = Entry(self.currentWindow)
        self.txt_number.pack(padx=50)

        # the user submits their number
        self.btn_guess = Button(self.currentWindow, text="Guess", command=self.Guess, fg="springgreen")
        self.btn_guess.pack(pady=20)

        # label is just for displaying an appropriate msg
        self.lbl_output = Label(self.currentWindow, text="", relief='raised')
        self.lbl_output.pack()

        # a button for them to restart and disabled in the start
        self.btn_restart = Button(self.currentWindow, text="Play again", command=self.Restart, state=DISABLED)
        self.btn_restart.pack(pady=20)

        # if they finished playing or give up they go back to mainmenu
        self.btn_goback = Button(self.currentWindow, text="Go back to main window", command=self.Goback, fg="crimson")
        self.btn_goback.pack(pady=20)

        # value is randomized between 1 and 100
        self.value = random.randint(1,100)

    # function that compares user's input with random value
    def Guess(self):
        # if the value inputted matches the random number/ actual value button is enabled
        if self.value == int(self.txt_number.get()):
            self.lbl_output.config(text=f'Congrats {self.username.title()}! You entered the right number of {self.value}', fg="green")
            self.btn_restart.config(state=NORMAL)
        # if the number inputted is lower than the random value
        elif int(self.txt_number.get()) < self.value:
            self.lbl_output.config(text='Your number is too low', fg="red")
        # if number inputted is greater than the actual value
        else:
            self.lbl_output.config(text='Your number is too high', fg="orange")

    # function that re-generates the number/ replay the game
    def Restart(self):
        self.value = random.randint(1,100)
        self.btn_restart.config(state=DISABLED, fg="green")
        self.txt_number.delete(0,END)
        self.lbl_output.config(text="Game restarted", fg="green")


    # they go back to mainmenu
    def Goback(self):
        from Post_Login import Mainmenu
        Mainmenu(self.root, self.username)
        self.currentWindow.withdraw()

# this code allows the file to be used as a module (importable)
# if __name__ == "__main__":
#     root = Tk()
#     start = Random_Number(root)
#     root.mainloop()