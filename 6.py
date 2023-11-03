import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x, xi, yi):
    n = len(xi)
    result = 0.0
    for i in range(n):
        term = yi[i]
        for j in range(n):
            if j != i:
                term *= (x - xi[j]) / (xi[i] - xi[j])
        result += term
    return result

# Задана таблиця значень функції
xi = [-2, 0, 1, 2]
yi = [-11, -3, -11, 5]

# Задані точки, в яких потрібно знайти значення функції
x_values = [-1.5, -0.5, 0.5, 2.5]

# Знаходимо інтерполяційні значення функції для кожної заданої точки
interpolated_values = [lagrange_interpolation(x, xi, yi) for x in x_values]

for i, x in enumerate(x_values):
    print(f"Ln({x}) ≈ {interpolated_values[i]:.3f}")

# Побудова графіка
x_range = np.linspace(-2.5, 2.5, 400)
y_range = [lagrange_interpolation(x, xi, yi) for x in x_range]

plt.plot(xi, yi, 'ro', label="Задані точки")
plt.plot(x_range, y_range, label="Ln(x)")
plt.xlabel("x")
plt.ylabel("Ln(x)")
plt.legend()
plt.grid(True)
plt.show()
