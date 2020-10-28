import tkinter
from tkinter import *
from tkinter import messagebox

val =""
A = 0
operator = ""


def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)

def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)

def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)

def btn_5_isclicked():
    global val
    val = val + "4"
    data.set(val)

def btn_6_isclicked():
    global val
    val = val + "5"
    data.set(val)

def btn_7_isclicked():
    global val
    val = val + "6"
    data.set(val)

def btn_9_isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn_10_isclicked():
    global val
    val = val + "8"
    data.set(val)

def btn_11_isclicked():
    global val
    val = val + "9"
    data.set(val)

def btn_14_isclicked():
    global val
    val = val + "0"
    data.set(val)

def btn_4_isclicked():
    global A
    global operator
    global val
    A = float(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_8_isclicked():
    global A
    global operator
    global val
    A = float(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_12_isclicked():
    global A
    global operator
    global val
    A = float(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btn_16_isclicked():
    global A
    global operator
    global val
    A = float(val)
    operator = "/"
    val = val + "/"
    data.set(val)     

def btn_13_isclicked():
    global A
    global operator
    global val
    A = 0
    operator = ""
    val = ""
    data.set(val)

def result():
    global A
    global operator
    global val
    x = val
    if operator == "+":
        B = int((x.split("+")[1]))
        C = A+B
        data.set(C) 
        C = round(C,4)
        val = str(C)   
    elif operator == "-":
        B = int((x.split("-")[1]))
        C = A-B
        data.set(C) 
        C = round(C,4)
        val = str(C)
    elif operator == "*":
        B = int((x.split("*")[1]))
        C = A*B
        data.set(C)
        C = round(C,4)
        val = str(C)
    elif operator == "/":
        B = int((x.split("/")[1]))
        if B == 0:
            messagebox.showerror("Error","Can't divide by zero")
            val = ""
            A = ""
            data.set(val)
        else:
            C = A / B
            C = round(C,4)
            data.set(C)
            val = str(C)






root = tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("Calculator")

data = StringVar()


lbl = Label(
    root,
    text = "Label",
    anchor = SE,
    font = ("Verdana", 22),
    textvariable = data, 
    background = "#ffffff",
    fg = "#000000"
)
lbl.pack(expand = True, fill = "both",)

btnrow1 = Frame(root,bg = "#000000")
btnrow1.pack(expand = True, fill = "both",)

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both",)

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both",)

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both",)

btn1 = Button(
    btnrow1,
    text = 1,
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_1_isclicked,
)
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow1,
    text = 2,
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_2_isclicked,
)
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow1,
    text = 3,
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_3_isclicked,
)
btn3.pack(side = LEFT, expand = True, fill = "both",)

btn4 = Button(
    btnrow1,
    text = "+",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_4_isclicked,
)
btn4.pack(side = LEFT , expand = True, fill = "both",)




btn5 = Button(
    btnrow2,
    text = 4,
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_5_isclicked,
)
btn5.pack(side = LEFT, expand = True, fill = "both",)

btn6 = Button(
    btnrow2,
    text = 5,
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_6_isclicked,
)
btn6.pack(side = LEFT, expand = True, fill = "both",)

btn7 = Button(
    btnrow2,
    text = 6,
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_7_isclicked,
)
btn7.pack(side = LEFT, expand = True, fill = "both",)

btn8 = Button(
    btnrow2,
    text = "-",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_8_isclicked,
)
btn8.pack(side = LEFT , expand = True, fill = "both",)






btn9 = Button(
    btnrow3,
    text = 7,
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_9_isclicked,
)
btn9.pack(side = LEFT, expand = True, fill = "both",)

btn10 = Button(
    btnrow3,
    text = 8,
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_10_isclicked,
)
btn10.pack(side = LEFT, expand = True, fill = "both",)

btn11 = Button(
    btnrow3,
    text = 9,
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_11_isclicked,
)
btn11.pack(side = LEFT, expand = True, fill = "both",)

btn12 = Button(
    btnrow3,
    text = "*",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_12_isclicked,
)
btn12.pack(side = LEFT , expand = True, fill = "both",)







btn13 = Button(
    btnrow4,
    text = "AC",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_13_isclicked,
)
btn13.pack(side = LEFT, expand = True, fill = "both",)

btn14 = Button(
    btnrow4,
    text = 0,
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_14_isclicked,
)
btn14.pack(side = LEFT, expand = True, fill = "both",)

btn15 = Button(
    btnrow4,
    text = "=",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = result,
)
btn15.pack(side = LEFT, expand = True, fill = "both",)

btn16 = Button(
    btnrow4,
    text = "/",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_16_isclicked,
)
btn16.pack(side = LEFT , expand = True, fill = "both",)



root.mainloop()