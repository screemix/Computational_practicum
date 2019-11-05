from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from tkinter import *

def plotMethods(exact, euler, improved, runge_kutta, f, a, dataPlot, x0, X):
    a.clear()
    a.grid()
    line1, = a.plot(exact[0], exact[1])
    line2, = a.plot(euler[0], euler[1])
    line3, = a.plot(improved[0], improved[1])
    line4, = a.plot(runge_kutta[0], runge_kutta[1])

    a.legend([line1, line2, line3, line4],
               ['Exact solution', 'Euler method', 'Improved Euler method', 'Runge-Kutta method'], loc=4, prop={'size': 4})
    axes = f.gca()
    axes.set_xlim([x0, X])
    axes.set_ylim([-15, 15])
    dataPlot.show()
    dataPlot.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=1)

def plotErrors(error1, error2, error3, f, a, exact, dataPlot, x0, X):
    a.clear()
    a.grid()
    err_line1, = a.plot(exact[0], error1)
    err_line2, = a.plot(exact[0], error2)
    err_line3, = a.plot(exact[0], error3)
    a.legend([err_line1, err_line2, err_line3],
                ['Euler method error', 'Improved Euler method error', 'Runge-Kutta method error'],  loc=4, prop={'size': 4})
    axes = f.gca()
    axes.set_xlim([x0, X])
    axes.set_ylim([-15, 15])
    dataPlot.show()
    dataPlot.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=1)


