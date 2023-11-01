from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt
# Функція, яка обчислює відхилення від рівнянь системи
def equations(vars):
    x, y = vars
    eq1 = np.cos(x + 0.5) + y - 0.8
    eq2 = np.sin(y) - 2 * x - 1.6
    return [eq1, eq2]

# Початкове наближення
initial_guess = [0.0, 0.0]

# Розв'язання системи рівнянь
solution = fsolve(equations, initial_guess)

x, y = solution
print(f"x = {x}, y = {y}")

# Функції, які представляють вихідні рівняння
def eq1(x, y):
    return np.cos(x + 0.5) + y - 0.8

def eq2(x, y):
    return np.sin(y) - 2 * x - 1.6

# Створення масивів значень x та y для побудови графіка
x_values = np.linspace(-2, 2, 400)
y_values = np.linspace(-2, 2, 400)

# Створення сітки значень для обчислення графіків
X, Y = np.meshgrid(x_values, y_values)
Z1 = eq1(X, Y)
Z2 = eq2(X, Y)

# Побудова графіків
plt.figure(figsize=(12, 6))
plt.contour(X, Y, Z1, levels=[0], colors='r')
plt.text(1.0, 1.0, 'cos(x + 0.5) + y = 0.8', color='r', fontsize=12)
plt.contour(X, Y, Z2, levels=[0], colors='b')
plt.text(-1.5, -1.5, 'sin(y) - 2x = 1.6', color='b', fontsize=12)

plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.title('Графіки рівнянь')
plt.show()
