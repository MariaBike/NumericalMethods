import numpy as np

def f(x, y):
    return x * np.sin(x) * x * np.exp(-x**2) - 2 * x * y

def solution(x):
    return np.exp(-x**2) * (-x**2 * np.cos(x) + 2*x*np.sin(x) + 2*np.cos(x) - 1)

eps = 0.00001

def method(step):
    x0 = 0
    y0 = 1
    x_max = 1
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
    return y[-1]

def runge_romberg(h1,h2):
    v1 = method(h1)
    v2 = method(h2)
    delta = (v1-v2)/15
    count=0
    while(abs(delta)>eps):
        v1=v2
        h2/=2
        v2=method(h2)
        delta=abs(v1-v2)/15
        count+=1
    print(count)
    return v2+delta


print("метод Рунге-Ромберга",runge_romberg(0.1,0.05))
print("точное решение",solution(1))
