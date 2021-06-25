from tkinter import*
import tkinter as tk

app = tk.Tk()
app.title('Calculator')
app.geometry('250x350')

equation = StringVar()

exp = ""


def operate(num):
    global exp
    exp = exp + str(num)
    equation.set(exp)


def equaloperate():
    try:
        global exp
        total = str(eval(exp))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        exp = ""


def clr():
    global exp
    expression = ""
    equation.set("")

result = tk.Variable(app)
exp_display = Entry(app, textvariable=equation,width=35).place(x=20, y=20)

tk.Button(app, text='7', width=5, height=2,command=lambda: operate(7)).place(x=30, y=70)
tk.Button(app, text='8', width=5, height=2,command=lambda: operate(8)).place(x=80, y=70)
tk.Button(app, text='9', width=5, height=2,command=lambda: operate(9)).place(x=130, y=70)
tk.Button(app, text='/', width=5, height=2,command=lambda: operate('/')).place(x=180, y=70)
tk.Button(app, text='4', width=5, height=2,command=lambda: operate(4)).place(x=30, y=140)
tk.Button(app, text='5', width=5, height=2,command=lambda: operate(5)).place(x=80, y=140)
tk.Button(app, text='6', width=5, height=2,command=lambda: operate(6)).place(x=130, y=140)
tk.Button(app, text='', width=5, height=2,command=lambda: operate('')).place(x=180, y=140)
tk.Button(app, text='1', width=5, height=2,command=lambda: operate(1)).place(x=30, y=210)
tk.Button(app, text='2', width=5, height=2,command=lambda: operate(2)).place(x=80, y=210)
tk.Button(app, text='3', width=5, height=2,command=lambda: operate(3)).place(x=130, y=210)
tk.Button(app, text='-', width=5, height=2,command=lambda: operate('-')).place(x=180, y=210)
tk.Button(app, text='C', width=5, height=2,command=lambda: clr()).place(x=30, y=280)
tk.Button(app, text='0', width=5, height=2,command=lambda: operate(0)).place(x=80, y=280)
tk.Button(app, text='=', width=5, height=2,command=lambda: equaloperate()).place(x=130, y=280)
tk.Button(app, text='+', width=5, height=2,command=lambda: operate('+')).place(x=180, y=280)


app.mainloop()
