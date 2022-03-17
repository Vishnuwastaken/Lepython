from tkinter import *
from random import *

# this class displays a window to run the country quiz
class Quiz:
    def __init__(self, root, username):
        self.root = root
        self.root.iconify()
        self.username = username
        self.currentWindow = Toplevel()
        self.currentWindow.title("Country Quiz")
        self.currentWindow.geometry('1000x1000')
        self.currentWindow.configure(bg="indigo")

        # this is for counting the number of attempts
        self.count = 0

        # gives them instructions
        self.lbl_instructions = Label(self.currentWindow, text=f"Hi {self.username.title()}, you will be given a random country, and you have to guess its capital. There will be 3 attempts for you to guess it right. GOOD LUCK!!", font=("arial", 14), fg="gold")
        self.lbl_instructions.pack()

        # they can start quiz/ guess a capital
        self.btn_startquiz = Button(self.currentWindow, text="Guess a capital", command=self.create_question, fg="blue")
        self.btn_startquiz.pack(pady=20)

        # this will display the country
        self.lbl_country = Label(self.currentWindow, text="")
        self.lbl_country.pack()

        # they enter the capital of the given country
        self.txt_capital = Entry(self.currentWindow)
        self.txt_capital.pack()

        # they submit their guess
        self.btn_submit = Button(self.currentWindow, text="Submit your answer", command=self.answer, fg="lime")
        self.btn_submit.pack(pady=20)

        # it displays an appropriate msg depending on answer
        self.lbl_output = Label(self.currentWindow, text="")
        self.lbl_output.pack()

        # they get an button to back to mainmenu
        self.btn_goback = Button(self.currentWindow, text="Go back to main window", command=self.Goback, fg="indianred")
        self.btn_goback.pack(pady=20)

        # it is a list that stores countries and capitals from countries.txt
        self.lines = [""]
        with open("/Users/vish/Desktop/Computer Sicence IB/CS_Projects/OOP_Projects/countries.txt") as file_in:
            self.lines = file_in.readlines()

    # function that lets them go back to mainmenu
    def Goback(self):
        from Post_Login import Mainmenu
        Mainmenu(self.root, self.username)
        self.currentWindow.withdraw()

    # it makes a question and gets a random country
    def create_question(self):
        index = randint(0, len(self.lines) - 1)
        new_question = self.lines[index]
        new_country = new_question.split(', ')
        self.country = new_country[0].strip()
        self.capital = new_country[1].strip()
        self.txt_capital.delete(0,END)
        self.lbl_country.config(text=f"What is the capital of {self.country.title()}")
        self.lbl_output.config(text="Country updated", fg="green", width=50, relief="raised", font=("Arial", 14))
        self.btn_startquiz.config(state=DISABLED)
        self.count = 2


    # checks the user's answer
    def answer(self):
        # count keeps track of how many chances has been utilzed and button gets disabled
        if self.count > 0:
            ans = False
            self.count -= 1
            self.btn_startquiz.config(state=DISABLED)
            cap = self.txt_capital.get().lower()
            # if the answer matches the capital, button will be re enabled
            if not cap == self.capital.lower():
                self.lbl_output.config(text=f"Nope, that is not the capital and you have {self.count+1} chances left", fg="red")
                cap = self.txt_capital.get().lower()
            # if the answer is wrong, they lose 1 chance
            else:
                self.lbl_output.config(text=f"Congrats {self.username.title()}! You entered the right capital", fg="green")
                ans = True
                self.btn_startquiz.config(state=NORMAL)

        # if all chances are used, correct answer is shown and button is re-enabled
        else:
            self.lbl_output.config(text=f"You've ran out of chances and the capital was {self.capital.title()}")
            self.btn_startquiz.config(state=NORMAL)


# this code allows the file to be used as a module (importable)
# if __name__ == "__main__":
#     root = Tk()
#     startquiz = Quiz(root)
#     root.mainloop()
