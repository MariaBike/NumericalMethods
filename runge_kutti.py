import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x * np.sin(x) * x * np.exp(-x**2) - 2 * x * y


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
    count =0
    for i in range(3,len(x)-1):
        y2[i+1]=y2[i]+step*(55*f(x[i],y2[i])-59*f(x[i-1],y2[i-1])+37*f(x[i-2],y2[i-2])-9*f(x[i-3],y2[i-3]))/24
        count+=1
    print(count)



    
    # Визуализация
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, color='blue')
    plt.plot(x,y2, color='orange')
    #plt.plot(x,y_vals, color='red')
    plt.title('Метод Рунге-Кутты')
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
