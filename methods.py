from functions import*

def exact_solution(x0, y0, X, n):
    h = (X - x0) / n
    x = []
    for i in range(n):
        x.append(x0 + i * h)
    e = []
    for i in range(n):
        e.append(y(x[i], x0, y0))
    a = [x, e]
    return a


def euler_method(x0, y0, b, n):
    h = (b - x0) / n
    x = []
    for i in range(n):
        x.append(x0 + i * h)
    y = [y0]
    for i in range(1, n):
        y.append(y[i - 1] + h * f(x[i - 1], y[i - 1]))
    g = [x, y]
    return g

def improved_euler_method(x0, y0, b, n):
    h = (b - x0) / n
    x = []
    for i in range(n):
        x.append(x0 + i * h)
    y = [y0]
    for i in range(1, n):
        k1 = f(x[i - 1], y[i - 1]) * h
        k2 = f(x[i - 1] + h, y[i - 1] + k1)*h
        y.append(y[i-1] + (k2+k1)/2)
    a = [x, y]
    return a

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
    a = [x, y]
    return a

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


