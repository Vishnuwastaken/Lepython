from tkinter import *

class MainWindow:
    def __init__(self):
        self.frame = Tk()
        self.frame.config(bg='gold1')
        self.frame.title("Python GUI Converter")
        self.frame.geometry("500x400")
        self.lbl_welcome = Label(text="Welcome to my convertor", bg="blue", fg="white")

        self.lbl_welcome.pack()

        self.lbl_fNumber = Label(text="Enter a valu in meters: ")
        self.txt_fNumber = Entry()
        self.lbl_fNumber.pack()
        self.txt_fNumber.pack()

        self.btn_cm = Button(text="CM", command=self.convert_cm)
        self.lbl_result = Label(text="Result")
        self.btn_cm.pack()
        self.lbl_result.pack()

        self.btn_km = Button(text="KM", command=self.convert_km)
        self.lbl_result1 = Label(text="Result")
        self.btn_km.pack()
        self.lbl_result1.pack()

        self.btn_mm = Button(text="MM", command=self.convert_mm)
        self.lbl_result2 = Label(text="Result")
        self.btn_mm.pack()
        self.lbl_result2.pack()

        self.btn_ft = Button(text="FT", command=self.convert_ft)
        self.lbl_result3 = Label(text="Result")
        self.btn_ft.pack()
        self.lbl_result3.pack()

    def run(self):
        self.frame.mainloop()

    def convert_cm(self):
        num = float(self.txt_fNumber.get())
        ans = num*100
        self.lbl_result.config(text=ans)

    def convert_km(self):
        num1 = float(self.txt_fNumber.get())
        ans = num1/1000
        self.lbl_result1.config(text=ans)

    def convert_mm(self):
        num2 = float(self.txt_fNumber.get())
        ans = num2*1000
        self.lbl_result2.config(text=ans)

    def convert_ft(self):
        num3= float(self.txt_fNumber.get())
        ans = num3 * 3.281
        self.lbl_result3.config(text=ans)

app = MainWindow()
app.run()
