import numpy as np
import matplotlib.pyplot as plt

def trapezoidal_integrate(f, x0, x1, n=1000):
    """Численное интегрирование методом трапеций"""
    h = (x1 - x0) / n
    x = np.linspace(x0, x1, n+1)
    y = f(x)
    integral = h * (0.5 * y[0] + 0.5 * y[-1] + np.sum(y[1:-1]))
    return integral

def f(x, y):
    """Правая часть дифференциального уравнения"""
    return x * np.sin(x) * x * np.exp(-x**2) - 2 * x * y

def picard_method(f, x0, y0, x_max, n_iterations=5, step=0.01):
    """Метод последовательных приближений"""
    x_vals = np.arange(x0, x_max + step, step)
    approximations = [np.full_like(x_vals, y0)]  # Первое приближение
    
    def next_approximation(prev_approx):
        def integrand(t):
            idx = np.searchsorted(x_vals, t)
            return f(t, prev_approx[idx])
        return np.array([
            y0 + trapezoidal_integrate(integrand, x0, x)
            for x in x_vals
        ])
    
    for _ in range(n_iterations):
        new_approx = next_approximation(approximations[-1])
        approximations.append(new_approx)
    
    # Визуализация
    plt.figure(figsize=(10, 6))
    for i, approx in enumerate(approximations):
        plt.plot(x_vals, approx, label=f'Приближение {i}')
    
    plt.title('Метод последовательных приближений')
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

    print("\nТаблица значений для последнего приближения:")
    print(f"{'x':<10}{'y(x)':<15}")
    print("-" * 25)
    for x, y in zip(x_vals, approximations[-1]):
        print(f"{x:<10.4f}{y:<15.8f}")


# Параметры задачи
x0 = 0
y0 = 1
x_max = 1

# Решение
picard_method(f, x0, y0, x_max, n_iterations=4)
