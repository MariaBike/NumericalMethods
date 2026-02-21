import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x * np.sin(x) * x * np.exp(-x**2) - 2 * x * y

def euler_method(x0, y0, x_max, step=0.01):
    x = np.arange(x0, x_max, step)
    #x_frac=np.arange(x0+step/2, x_max-step/2, step)
    y = np.zeros(len(x))
    y[0] = y0  
    for i in range(len(x)-1):
        x_frac=(x[i]+x[i+1])/2
        y_frac=y[i]+step*f(x[i],y[i])/2
        y[i+1]=y[i]+step*f(x_frac,y_frac)
    


    
    # Визуализация
    plt.figure(figsize=(10, 6))
    
    plt.plot(x, y)
    
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
