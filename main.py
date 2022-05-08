import tkinter
from tkinter import *
from tkinter.font import Font

calculator = tkinter.Tk()
picture = PhotoImage(file='Calculator-icon.png')
calculator.iconphoto(True, picture)
calculator.title("Calculator By OJ")
equationToCalculate = ""
input_text = tkinter.StringVar()
result_text = tkinter.StringVar()


def evaluateButton(item):
    global equationToCalculate
    equationToCalculate = equationToCalculate + str(item)
    input_text.set(equationToCalculate)


def equalButton():
    global equationToCalculate
    result = str(eval(equationToCalculate))
    result_text.set("=" + result)


def backspaceButton():
    global equationToCalculate
    equationToCalculate = equationToCalculate[:-1]
    input_text.set(equationToCalculate)


def clearButton():
    global equationToCalculate
    equationToCalculate = ""
    input_text.set("")
    result_text.set("")


input_frame = Frame(calculator, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=1, background="grey")
input_frame.pack(side=TOP)
input_field = Entry(input_frame, font=('Times New Roman', 17, 'bold'), textvariable=input_text, width=30, bg="#eee",
                    bd=0, justify=RIGHT)
input_field.pack(ipady=20)
result_frame = Frame(calculator, width=400, height=50, bd=0, highlightbackground="grey", highlightcolor="grey",
                     highlightthickness=1, background="blue")
result_field = Entry(result_frame, font=('Times New Roman', 17, 'bold'), textvariable=result_text, width=30, bg="#eee",
                     bd=0, justify=RIGHT)
result_field.pack(ipady=20)
result_frame.pack(side=TOP)
buttonWindow = Frame(calculator, width=400, height=500, bg="#C1C0C0")
buttonFont = Font(family='Amasis MT Pro', size=10, weight='normal')
Button(buttonWindow, text="0", fg="white", width=21, height=3, bd=0, bg="#3F3F3F", cursor="hand2",
       command=lambda: evaluateButton(0), font=buttonFont).grid(row=4, column=0, columnspan=2, padx=2, pady=2)
Button(buttonWindow, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
       command=lambda: evaluateButton("."), font=buttonFont).grid(row=4, column=2, padx=2, pady=2)
Button(buttonWindow, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
       command=equalButton, font=buttonFont).grid(row=4, column=3, padx=2, pady=2)
Button(buttonWindow, text="1", fg="white", width=10, height=3, bd=0, bg="#3F3F3F", cursor="hand2",
       command=lambda: evaluateButton(1), font=buttonFont).grid(row=3, column=0, padx=2, pady=2)
Button(buttonWindow, text="2", fg="white", width=10, height=3, bd=0, bg="#3F3F3F", cursor="hand2",
       command=lambda: evaluateButton(2), font=buttonFont).grid(row=3, column=1, padx=2, pady=2)
Button(buttonWindow, text="3", fg="white", width=10, height=3, bd=0, bg="#3F3F3F", cursor="hand2",
       command=lambda: evaluateButton(3), font=buttonFont).grid(row=3, column=2, padx=2, pady=2)
Button(buttonWindow, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
       command=lambda: evaluateButton("+"), font=buttonFont).grid(row=3, column=3, padx=2, pady=2)
Button(buttonWindow, text="4", fg="white", width=10, height=3, bd=0, bg="#3F3F3F", cursor="hand2",
       command=lambda: evaluateButton(4), font=buttonFont).grid(row=2, column=0, padx=2, pady=2)
Button(buttonWindow, text="5", fg="white", width=10, height=3, bd=0, bg="#3F3F3F", cursor="hand2",
       command=lambda: evaluateButton(5), font=buttonFont).grid(row=2, column=1, padx=2, pady=2)
Button(buttonWindow, text="6", fg="white", width=10, height=3, bd=0, bg="#3F3F3F", cursor="hand2",
       command=lambda: evaluateButton(6), font=buttonFont).grid(row=2, column=2, padx=2, pady=2)
Button(buttonWindow, text="-", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: evaluateButton("-"), font=buttonFont).grid(row=2, column=3, padx=2, pady=2)
Button(buttonWindow, text="7", fg="white", width=10, height=3, bd=0, bg="#3F3F3F", cursor="hand2",
       command=lambda: evaluateButton(7), font=buttonFont).grid(row=1, column=0, padx=2, pady=2)
Button(buttonWindow, text="8", fg="white", width=10, height=3, bd=0, bg="#3F3F3F", cursor="hand2",
       command=lambda: evaluateButton(8), font=buttonFont).grid(row=1, column=1, padx=2, pady=2)
Button(buttonWindow, text="9", fg="white", width=10, height=3, bd=0, bg="#3F3F3F", cursor="hand2",
       command=lambda: evaluateButton(9), font=buttonFont).grid(row=1, column=2, padx=2, pady=2)
Button(buttonWindow, text="*", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: evaluateButton("*"), font=buttonFont).grid(row=1, column=3, padx=2, pady=2)
Button(buttonWindow, text="Clear", fg="white", width=10, height=3, bd=0, bg="#3F3F3F", cursor="hand2",
       command=clearButton, font=buttonFont).grid(row=0, column=0, padx=2, pady=2)
Button(buttonWindow, text="<=", fg="white", width=10, height=3, bd=0, bg="#3F3F3F", cursor="hand2",
       command=backspaceButton, font=buttonFont).grid(row=0, column=1, padx=2, pady=2)
Button(buttonWindow, text="%", fg="white", width=10, height=3, bd=0, bg="#3F3F3F", cursor="hand2",
       command=lambda: evaluateButton("%"), font=buttonFont).grid(row=0, column=2, padx=2, pady=2)
Button(buttonWindow, text="/", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: evaluateButton("/"), font=buttonFont).grid(row=0, column=3, padx=2, pady=2)
buttonWindow.pack()
calculator.mainloop()
