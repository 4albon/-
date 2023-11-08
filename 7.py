import numpy as np
import matplotlib.pyplot as plt

def divided_difference(x, y):
    n = len(x)
    F = [[0] * n for _ in range(n)]
    for i in range(n):
        F[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = (F[i + 1][j - 1] - F[i][j - 1]) / (x[i + j] - x[i])
    return F

def newton_interpolation(x, y, xi):
    n = len(x)
    F = divided_difference(x, y)
    result = 0
    for i in range(n):
        term = F[0][i]
        for j in range(i):
            term *= (xi - x[j])
        result += term
    return result

x = [0.115, 0.120, 0.125, 0.130, 0.135, 0.140, 0.145, 0.150, 0.155, 0.160, 0.165]
y = [8.6572, 8.2932, 7.9582, 7.6489, 7.3623, 7.0961, 6.8491, 6.6185, 6.3998, 6.1965, 6.0055]


xi = np.linspace(0.115, 0.165, 100) 


yi = [newton_interpolation(x, y, xi_value) for xi_value in xi]

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o', label='Задана таблиця значень')
plt.plot(xi, yi, label='Інтерполяційна функція')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Графік інтерполяційної функції')
plt.show()
