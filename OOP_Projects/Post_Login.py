from tkinter import *
from Guessing_Game import *
from Country_quiz import *
from tkinter import messagebox

#  this class displays a new window with mainmenu
class Mainmenu:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.withdraw()
        self.currentWindow = Toplevel()
        self.currentWindow.title("The Mainmenu")
        self.currentWindow.geometry("500x500")
        self.currentWindow.configure(bg="olivedrab")

        # gives them a welcome msg after logging in
        self.lbl_welcome = Label(self.currentWindow, text=f"Welcome {username.title()}, you can play the game or do the quiz. Have fun!", font=("arial"), fg="gold", relief='raised')
        self.lbl_welcome.pack()

        # a btn for them to go to the guessing game
        self.btn_game = Button(self.currentWindow, text="Go to game", command=self.Game, fg="navy")
        self.btn_game.pack(pady=20)

        # a button for them to go to the country quiz
        self.btn_quiz = Button(self.currentWindow, text="Go to country quiz", command=self.Quiz, fg="navy")
        self.btn_quiz.pack(pady=20)

        # if they want to compeletly close, this is pressed
        self.btn_exit = Button(self.currentWindow, text="Exit the app", command=self.Exit, fg="orangered")
        self.btn_exit.pack(pady=20)

        # if they want to logout
        self.btn_logout = Button(self.currentWindow, text="Log out", command=self.Logout, fg="crimson")
        self.btn_logout.pack(pady=20)

    # it opens the Guessing game
    def Game(self):
        Random_Number(self.root, self.username)
        self.currentWindow.destroy()

    # it opens the quiz
    def Quiz(self):
        Quiz(self.root, self.username)
        self.currentWindow.destroy()

    # it closes everything
    def Exit(self):
        self.currentWindow.destroy()
        self.root.destroy()

    # they can go back to the mainwindow
    def Logout(self):
        messagebox.showinfo("Closing app", f"Goodbye {self.username.title()} :(, you will be missed.")
        from Mainfile import Login
        Login(self.root)
        self.currentWindow.destroy()

# this  allows the file to be used as a module (importable)
# if __name__ == "__main__":
#     root = Tk()
#     Mainmenu(root)
#     root.mainloop()

