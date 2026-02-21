import numpy as np
import matplotlib.pyplot as plt

# Определяем функцию решения
def y(x):
    return np.exp(-x**2) * (-x**2 * np.cos(x) + 2*x*np.sin(x) + 2*np.cos(x) - 1)

# Создаем массив значений x от 0 до 1 с шагом 0.01
x_values = np.linspace(0, 1, 100)
y_values = y(x_values)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label=r'$y(x) = e^{-x^2}(-x^2\cos(x) + 2x\sin(x) + 2\cos(x) - 1)$', color='blue')

# Настройка отображения
plt.title('График решения задачи Коши', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y(x)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.axhline(0, color='black',linewidth=0.8)
plt.axvline(0, color='black',linewidth=0.8)
plt.xlim(0, 1)
plt.ylim(auto=True)

# Добавляем сетку и подписи
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='gray')

# Показываем график
plt.show()
