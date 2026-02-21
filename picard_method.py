import numpy as np
import matplotlib.pyplot as plt
import math as m

# Функция f(x, y) из дифференциального уравнения y' = f(x, y)

def f(x, y):
    return y*y*np.exp(2*x)-3*y
    #return x + y # Пример: y' = x + y


"""
def f(x,y):
    return x*m.sin(x)*m.exp(-x*x)-2*x*y
"""

# Функция для численного интегрирования (метод прямоугольников)
def integrate(x0, y0, x, h, y_prev):
    sum = 0
    current_x = x0
    while current_x < x:
        sum += f(current_x, y_prev(current_x)) * h
        current_x += h
    return y0 + sum



# Метод последовательных приближений
def picard_method(x0, y0, x_end, n_iterations, h):
    # Создаем массив точек
    x_values = np.arange(x0, x_end + h, h)
    y_values = np.zeros_like(x_values)
    
    # Первое приближение - константа
    y_values[0] = y0
    
    # Последовательные приближения
    for i in range(1, len(x_values)):
        y_prev = lambda t: np.interp(t, x_values[:i], y_values[:i])
        y_values[i] = integrate(x0, y0, x_values[i], h, y_prev)
        
        # Выполняем n_iterations итераций
        for _ in range(n_iterations - 1):
            y_prev = lambda t: np.interp(t, x_values[:i+1], y_values[:i+1])
            y_values[i] = integrate(x0, y0, x_values[i], h, y_prev)
    
    return x_values, y_values

# Параметры задачи
x0 = 0.0 # Начальная точка
y0 = 1.0 # Начальное значение
x_end = 1.0 # Конечная точка
n_iterations = 5 # Количество итераций метода
h = 0.1 # Шаг интегрирования

# Решаем задачу
x, y = picard_method(x0, y0, x_end, n_iterations, h)

# Визуализация
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Решение y(x)', color='blue')
plt.scatter(x0, y0, color='red', zorder=5) # Отмечаем начальную точку
plt.title('Решение задачи Коши методом последовательных приближений')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()
