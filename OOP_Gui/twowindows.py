from tkinter import *

class Window1:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()
        self.curWindow = Toplevel()
        self.curWindow.title("Window 1")
        self.curWindow.geometry("300x200")

        self.lbl_welcome = Label(self.curWindow, text="~*~  Welcome to my program ~*~")
        self.lbl_welcome.pack()

        self.btn_opnWin2 = Button(self.curWindow, text="Open Window 2", command=self.open_window2)
        self.btn_opnWin2.pack()

    def open_window2(self):
        Window2(self.root)
        self.curWindow.destroy()


class Window2:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()
        self.curWindow = Toplevel()
        self.curWindow.title("Window 2")
        self.curWindow.geometry("300x200")

        self.lbl_welcome = Label(self.curWindow, text="~*~  Welcome to my program ~*~")
        self.lbl_welcome.pack()

        self.btn_opnWin1 = Button(self.curWindow, text="Open Window 1", command=self.open_window1)
        self.btn_opnWin1.pack()

    def open_window1(self):
        Window1(self.root)
        self.curWindow.destroy()

root = Tk()
app = Window1(root)
root.mainloop()

