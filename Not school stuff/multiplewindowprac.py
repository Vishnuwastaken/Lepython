from tkinter import *

class Window:
    def __init__(self, root):
        self.root = root
        self.root.iconify()
        self.currentWindow = Toplevel()
        self.currentWindow.geometry("200x200")
        self.currentWindow.title("Window 1")

        self.btn_start = Button(self.currentWindow, text="Start game", command=self.begin)
        self.btn_start.pack()


    def begin(self):
        game1 = Window1(self.root)
        self.currentWindow.destroy()

class Window1:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()
        self.currentWindow1 = Toplevel()
        self.currentWindow1.geometry("300x300")
        self.currentWindow1.title("Window 2")

        self.btn_Game = Button(self.currentWindow1, text="Begin game", command=self.begin1)
        self.btn_Game.pack()

        self.btn_back = Button(self.currentWindow1, text="Go back to start", command=self.back)
        self.btn_back.pack()

    def begin1(self):
        close = Window2(self.root)
        self.currentWindow1.destroy()

    def back(self):
        goback = Window(self.root)
        self.currentWindow1.destroy()

class Window2:
    def __init__(self, root):
        self.root = root
        self.currentWindow2 = Toplevel()
        self.currentWindow2.geometry("300x300")
        self.currentWindow2.title("Winodw 3")

        self.btn_exit = Button(self.currentWindow2, text="Exit", command=self.close)
        self.btn_exit.pack()

    def close(self):
        self.currentWindow2.destroy()
        self.root.destroy()

root = Tk()
oerwe = Window(root)
root.mainloop()
