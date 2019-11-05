from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from tkinter import *

from plotting import *
from methods import *
from functions import *
#---------------------------main part---------------------------#

def input():
    x0 = float(x0_entry.get())
    y0 = float(y0_entry.get())
    X = float(X_entry.get())
    n = int(n_entry.get())

    exact = exact_solution(x0, y0, X, n)
    euler = euler_method(x0, y0, X, n)
    improved = improved_euler_method(x0, y0, X, n)
    runge_kutta = runge_kutta_method(x0, y0, X, n)

    error1 = compute_error(exact[1], euler[1])
    error2 = compute_error(exact[1], improved[1])
    error3 = compute_error(exact[1], runge_kutta[1])

    plotMethods(exact, euler, improved, runge_kutta, f1, a, dataPlot1, x0, X)
    plotErrors(error1, error2, error3, f2, a2, exact, dataPlot2, x0, X)

master = Tk()

f_top = Frame()
f_mid = Frame()
f_bot = Frame()
master.title("Computational methods")

x0_entry = Entry(f_top, width=15)
y0_entry = Entry(f_top, width=15)
X_entry = Entry(f_top, width=15)
n_entry = Entry(f_top, width=15)

x0_label = Label(f_mid, width=15, text = "enter x0")
y0_label = Label(f_mid, width=15, text = "enter y0")
X_label = Label(f_mid, width=15, text = "enter X")
n_label = Label(f_mid, width=15, text = "enter n")

button = Button(f_bot, width=60, text="Submit", command=input)

f_top.pack()
f_mid.pack()
f_bot.pack()

x0_entry.pack(side=LEFT)
y0_entry.pack(side=LEFT)
X_entry.pack(side=LEFT)
n_entry.pack(side=LEFT)
x0_label.pack(side=LEFT)
y0_label.pack(side=LEFT)
X_label.pack(side=LEFT)
n_label.pack(side=LEFT)
button.pack()

f1 = Figure(figsize=(2,2), dpi=200)
a = f1.add_subplot(111)
dataPlot1 = FigureCanvasTkAgg(f1, master=master)

f2 = Figure(figsize=(2,2), dpi=200)
a2 = f2.add_subplot(111)
dataPlot2 = FigureCanvasTkAgg(f2, master=master)

f3 = Figure(figsize=(2,2), dpi=200)
a3 = f3.add_subplot(111)
dataPlot3 = FigureCanvasTkAgg(f3, master=master)

master.mainloop()
