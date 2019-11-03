from math import*
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from tkinter import *

x0, y0, X, n = 0, 1, 7, 100

#---------------------------functions part---------------------------#

def f(x, y):
    return 1/cos(x) - y * tan(x)

def const(x, y):
    return (y - sin(x))/cos(x)

def y(x):
    return const(x0, y0) * cos(x) + sin(x)

def input():
    x0 = int(x0_entry.get())
    y0 = int(y0_entry.get())
    X = int(X_entry.get())

def exact_solution(x0, y0, X, n):
    step = (X - x0)/n
    t = arange(x0, X, step)
    s = [y(i) for i in t]
    return s

def euler_method(x0, y0, b, n):
    h = (b - x0) / n
    x = []
    for i in range(n):
        x.append(x0 + i * h)
    y = [y0]
    for i in range(1, n):
        y.append(y[i - 1] + h * f(x[i - 1], y[i - 1]))
    return y

def improved_euler_method(x0, y0, b, n):
    h = (b - x0) / n
    x = []
    for i in range(n):
        x.append(x0 + i * h)
    y = [y0]
    for i in range(1, n):
        k1 = f(x[i - 1], y[i - 1])
        k2 = f(x[i - 1] + h, y[i - 1] + h * k1)
        y.append(y[i - 1] + (h / 2) * (k1 + k2))
    return y

def runge_kutta_method(x0, y0, b, n):
    h = (b - x0) / n
    x = []
    for i in range(n):
        x.append(x0 + i * h)
    y = [y0]
    for i in range(1, n):
        k1 = f(x[i - 1], y[i - 1])
        k2 = f(x[i - 1] + h / 2, y[i - 1] + (h / 2) * k1)
        k3 = f(x[i - 1] + h / 2, y[i - 1] + (h / 2) * k2)
        k4 = f(x[i - 1] + h, y[i - 1] + h * k3)
        y.append(y[i - 1] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4))
    return y

def compute_error(method1, method2):  # compute difference between numerical method and exact solution at each step
    m = len(method1)
    answer = m * [0]
    for i in range(m):
        answer[i] = method1[i] - method2[i]
    return answer

def investigate_convergence(error):  # check if any error doesn't tend to 0, in that case method is not convergent
    for element in error:
        if round(element) != 0:
            print(" is not convergent.")
            return
    print(" is convergent.")

def plotMethods(exact, euler, improved, runge_kutta, f):
    a3 = f.add_subplot(111)
    line1, = a3.plot(exact)
    line2, = a3.plot(euler)
    line3, = a3.plot(improved)
    line4, = a3.plot(runge_kutta)
    a3.legend([line1, line2, line3, line4],
               ['Exact solution', 'Euler method', 'Improved Euler method', 'Runge-Kutta method'])
    dataPlot3 = FigureCanvasTkAgg(f, master=master)
    dataPlot3.show()
    dataPlot3.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=1)

def plotErrors(error1, error2, error3, f):
    a = f.add_subplot(111)
    err_line1, = a.plot(error1)
    err_line2, = a.plot(error2)
    err_line3, = a.plot(error3)
    a.legend([err_line1, err_line2, err_line3],
                ['Euler method error', 'Improved Euler method error', 'Runge-Kutta method error'])
    dataPlot = FigureCanvasTkAgg(f, master=master)
    dataPlot.show()
    dataPlot.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=1)


#---------------------------plotting part---------------------------#

master = Tk()

f_top = Frame()
f_bot = Frame()
master.title("Computational methods")

x0_entry = Entry(f_top, width=15)
y0_entry = Entry(f_top, width=15)
X_entry = Entry(f_top, width=15)


button = Button(f_bot, width=45, text="Submit", command=input)

f_top.pack()
f_bot.pack()

x0_entry.pack(side=LEFT)
y0_entry.pack(side=LEFT)
X_entry.pack(side=LEFT)
button.pack()

cvar1 = BooleanVar()
cvar1.set(0)
c1 = Checkbutton(text="First", variable=cvar1, onvalue=1, offvalue=0)
c1.pack()

cvar2 = BooleanVar()
cvar2.set(0)
c2 = Checkbutton(text="Second", variable=cvar2, onvalue=1, offvalue=0)
c2.pack()

cvar3 = BooleanVar()
cvar3.set(0)
c3 = Checkbutton(text="Third", variable=cvar3, onvalue=1, offvalue=0)
c3.pack()


exact = exact_solution(x0, y0, X, n)
euler = euler_method(x0, y0, X, n)
improved = improved_euler_method(x0, y0, X, n)
runge_kutta = runge_kutta_method(x0, y0, X, n)

error1 = compute_error(exact, euler)
error2 = compute_error(exact, improved)
error3 = compute_error(exact, runge_kutta)


f = Figure(figsize=(2,2), dpi=200)
f2 = Figure(figsize=(2,2), dpi=200)
f3 = Figure(figsize=(2,2), dpi=200)

a = f.add_subplot(111)

t = arange(-10.0,10.0,0.01)
s = [sin(i)+cos(i)*10 for i in t]
a.plot(t,s)

dataPlot = FigureCanvasTkAgg(f, master=master)

dataPlot.show()
dataPlot.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=1)



plotMethods(exact, euler, improved, runge_kutta, f3)
plotErrors(error1, error2, error3, f2)
master.mainloop()