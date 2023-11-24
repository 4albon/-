import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares

def func(x):
    return np.exp(-x) + x**2

# Задаємо значення x
x_values = np.array([i * 0.1 for i in range(10)])

# Обчислюємо значення функції для кожного x
y_values = np.array([func(xi) for xi in x_values])

# Виводимо таблицю
print("  i   |   xi   |   f(xi)")
print("-------------------------")
for i, (xi, yi) in enumerate(zip(x_values, y_values)):
    print(f"  {i}   |  {xi:.1f}   |  {yi:.4f}")

# Визначаємо функцію для методу найменших квадратів
def fun(a, x, y):
    return np.exp(-a[0]*x) + a[1]*x**2 - y

# Початкове наближення для параметрів a
a0 = np.array([1, 1])

# Застосовуємо метод найменших квадратів
res_lsq = least_squares(fun, x0=a0, args=(x_values, y_values))

# Виводимо результати апроксимації
print("\nРезультати апроксимації:")
print("a0 = %.4f, a1 = %.4f" % tuple(res_lsq.x))

# Визначаємо апроксимовану функцію
f = lambda x: np.exp(-res_lsq.x[0]*x) + res_lsq.x[1]*x**2

# Генеруємо значення для графіка
x_plot = np.linspace(min(x_values), max(x_values), 100)
y_plot = f(x_plot)

# Побудова графіка
plt.plot(x_values, y_values, 'o', label='Дані')
plt.plot(x_plot, y_plot, 'b', label='Апроксимація')
plt.title("Апроксимація функції")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
