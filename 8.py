import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.1, 0.3, 0.6, 1.1, 1.8])
y = np.array([2.65, 2.75, 2.19, 1.76, 3.43])

h = np.diff(x)

y_double_prime = np.zeros(len(x))
for i in range(1, len(x) - 1):
    y_double_prime[i] = (6 / (h[i - 1] + h[i])) * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])

a = y[:-1]
b = (np.diff(y) / h) - (h * (y_double_prime[1:] + 2 * y_double_prime[:-1]) / 6)
c = y_double_prime / 2
d = (np.diff(y_double_prime) / (6 * h))

for i in range(len(x) - 1):
    print(f"Відрізок {i + 1}:")
    print(f"S_{i}(x) = {a[i]} + {b[i].round(4)}(x - {x[i]}) + {c[i].round(4)}(x - {x[i]})^2 + {d[i].round(4)}(x - {x[i]})^3, x належить [{x[i]}, {x[i+1]}]")

def spline_value(t, i):
    delta_x = t - x[i]
    return a[i] + b[i] * delta_x + c[i] * delta_x ** 2 + d[i] * delta_x ** 3

for i in range(len(x) - 1):
    spline = spline_value(x[i], i)
    print(f"Point {i}: Spline Value = {spline}, Original Value = {y[i]}")

t = np.linspace(min(x), max(x), 100)
spline_values = np.zeros_like(t)

for i in range(len(x) - 1):
    mask = (x[i] <= t) & (t <= x[i + 1])
    spline_values[mask] = spline_value(t[mask], i)

plt.plot(t, spline_values, label='Spline')
plt.plot(x, y, 'ro', label='Data Points')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
