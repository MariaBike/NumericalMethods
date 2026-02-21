import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x * np.sin(x) * x * np.exp(-x**2) - 2 * x * y


def f_x(x, y):
    return np.sin(x)*np.exp(-x*x)+x*np.cos(x)*np.exp(-x*x)-2*x*x*np.sin(x)*np.exp(-x*x)-2*y

def f_y(x, y):
    return -2*x


def euler_method(x0, y0, x_max, step=0.01):
    # исправленный метод Эйлера
    x = np.arange(x0, x_max, step)
    y = np.zeros(len(x))
    y[0] = y0  
    for i in range(len(x)-1):
        y[i+1] = y[i]+step*f(x[i],y[i])+step*step*(f_x(x[i],y[i])+f_y(x[i],y[i])*f(x[i],y[i]))/2
    
    # метод Эйлера
    y_vals = np.zeros(len(x))
    y_vals[0] = y0  
    for i in range(len(x)-1):
        y_vals[i+1]=y_vals[i]+step*f(x[i],y_vals[i])

    # первый усовершенствованный метод Эйлера
    y2 = np.zeros(len(x))
    y2[0] = y0  
    for i in range(len(x)-1):
        x_frac=(x[i]+x[i+1])/2
        y_frac=y2[i]+step*f(x[i],y2[i])/2
        y2[i+1]=y2[i]+step*f(x_frac,y_frac)
    # Визуализация
    plt.figure(figsize=(10, 6))
    
    plt.plot(x,y_vals, color='red')
    plt.plot(x, y, color='blue')
    plt.plot(x,y2,color='pink')
    plt.title('Метод Эйлера')
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

    

# Параметры задачи
x0 = 0
y0 = 1
x_max = 1

# Решение
euler_method(x0, y0, x_max)
