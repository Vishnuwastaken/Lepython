from tkinter import *

def Click():
    window = Toplevel()
    root.withdraw()
    window.title("Second Window")
    window.geometry("500x300")
    btn_W2 = Button(window, text="Go back to main window", command=window.destroy)
    btn_W2.pack()


root = Tk()
root.title("Main Window made using TK")
root.geometry("500x300")


btn_W1 = Button(root, text="Go to window 2", command=Click)
btn_W1.pack()


root.mainloop()
