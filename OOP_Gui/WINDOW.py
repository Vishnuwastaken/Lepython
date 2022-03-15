from tkinter import *


class MainWindow:
    def __init__(self):
        self.frame = Tk()
        self.frame.config(bg='gold1')
        self.frame.title("Python GUI Intro")
        self.frame.geometry("500x400")
        self.lbl_welcome = Label(text="Welcome to my first GUI program", bg="blue", fg="white")

        self.lbl_welcome.pack()

        self.lbl_fNumber = Label(text="Enter first number: ")
        self.lbl_sNumber = Label(text="Enter second number: ")
        self.txt_fNumber = Entry()
        self.txt_sNumber = Entry()

        self.lbl_fNumber.pack()
        self.txt_fNumber.pack()
        self.lbl_sNumber.pack()
        self.txt_sNumber.pack()

        self.btn_sum = Button(text="Sum", command=self.sum)
        self.lbl_result = Label(text="Result")
        self.btn_sum.pack()
        self.lbl_result.pack()

        self.btn_sub = Button(text="Sub", command=self.sub)
        self.lbl_result1 = Label(text="Result")
        self.btn_sub.pack()
        self.lbl_result1.pack()

        self.btn_mul = Button(text="Mul", command=self.mul)
        self.lbl_result2 = Label(text="Result")
        self.btn_mul.pack()
        self.lbl_result2.pack()

        self.btn_div = Button(text="Div", command=self.div)
        self.lbl_result3 = Label(text="Result")
        self.btn_div.pack()
        self.lbl_result3.pack()

    def run(self):
        self.frame.mainloop()

    def sum(self):
        num1 = float(self.txt_fNumber.get())
        num2 = float(self.txt_sNumber.get())
        ans = num1 + num2
        self.lbl_result.config(text=ans)

    def sub(self):
        num1 = float(self.txt_fNumber.get())
        num2 = float(self.txt_sNumber.get())
        ans = num1 - num2
        self.lbl_result1.config(text=ans)

    def mul(self):
        num1 = float(self.txt_fNumber.get())
        num2 = float(self.txt_sNumber.get())
        ans = num1 * num2
        self.lbl_result2.config(text=ans)

    def div(self):
        num1 = float(self.txt_fNumber.get())
        num2 = float(self.txt_sNumber.get())
        ans = num1/num2
        self.lbl_result3.config(text=ans)


app = MainWindow()
app.run()
