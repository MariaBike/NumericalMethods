import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x * np.sin(x) * x * np.exp(-x**2) - 2 * x * y

def f_x(x, y):
    return np.sin(x)*np.exp(-x*x)+x*np.cos(x)*np.exp(-x*x)-2*x*x*np.sin(x)*np.exp(-x*x)-2*y

def f_y(x, y):
    return -2*x

def solution(x):
    return np.exp(-x**2) * (-x**2 * np.cos(x) + 2*x*np.sin(x) + 2*np.cos(x) - 1)


def method(x0, y0, x_max, step=0.01):
    # метод Рунге-Кутты
    x = np.arange(x0, x_max, step)
    y = np.zeros(len(x))
    y[0] = y0  
    phi1 = step*f(x[0],y[0])
    phi2 = step*f(x[0]+step/2,y[0]+phi1/2)
    phi3 = step*f(x[0]+step/2,y[0]+phi2/2)
    phi4 = step*f(x[0]+step,y[0]+phi3)
    for i in range(len(x)-1):
        y[i+1] = y[i]+(phi1+2*phi2+2*phi3+phi4)/6
        phi1=step*f(x[i],y[i])
        phi2=step*f(x[i]+step/2,y[i]+phi1/2)
        phi3=step*f(x[i]+step/2,y[i]+phi2/2)
        phi4=step*f(x[i]+step,y[i]+phi3)

    # метод Адамса
    y2 = np.zeros(len(x))
    y2[0]=y0
    y2[1]=y[1]
    y2[2]=y[2]
    y2[3]=y[3]
    for i in range(3,len(x)-1):
        y2[i+1]=y2[i]+step*(55*f(x[i],y2[i])-59*f(x[i-1],y2[i-1])+37*f(x[i-2],y2[i-2])-9*f(x[i-3],y2[i-3]))/24

    # первый усовершенствованный метод Эйлера
    y3 = np.zeros(len(x))
    y3[0] = y0  
    for i in range(len(x)-1):
        x_frac=(x[i]+x[i+1])/2
        y_frac=y3[i]+step*f(x[i],y3[i])/2
        y3[i+1]=y3[i]+step*f(x_frac,y_frac)

    # исправленный метод Эйлера
    y4 = np.zeros(len(x))
    y4[0] = y0  
    for i in range(len(x)-1):
        y4[i+1] = y4[i]+step*f(x[i],y4[i])+step*step*(f_x(x[i],y4[i])+f_y(x[i],y4[i])*f(x[i],y4[i]))/2
    
    # метод Эйлера
    y5 = np.zeros(len(x))
    y5[0] = y0  
    for i in range(len(x)-1):
        y5[i+1]=y5[i]+step*f(x[i],y5[i])
    
    # аналитическое решение
    y6 = solution(x)
    # Визуализация
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='метод Рунге-Кутты', color='blue')
    plt.plot(x,y2, label='метод Адамса', color='orange')
    plt.plot(x,y3, label='первый усовершенствованный метод Эйлера', color='red')
    plt.plot(x,y4, label='исправленный метод Эйлера', color='pink')
    plt.plot(x,y5, label='метод Эйлера', color='green')
    plt.plot(x,y6, label=r'$y(x) = e^{-x^2}(-x^2\cos(x) + 2x\sin(x) + 2\cos(x) - 1)$', color='black')
    
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
method(x0, y0, x_max)
