from scipy import integrate
import numpy as np

eps = 0.0001
a = 0.4
b = 1.2

# Задана функція для інтегрування
def integrand(x):
    return 1 / np.sqrt(0.5 * x + 2)

# Метод прямокутників для лівих прямокутників
def left_rectangles(f, a, b, n):
    h = (b - a) / n
    sum_result = sum(f(a + i * h) for i in range(n))
    return sum_result * h

# Метод прямокутників для правих прямокутників
def right_rectangles(f, a, b, n):
    h = (b - a) / n
    sum_result = sum(f(a + (i + 1) * h) for i in range(n))
    return sum_result * h

# Метод прямокутників для середніх прямокутників
def middle_rectangles(f, a, b, n):
    h = (b - a) / n
    sum_result = sum(f(a + (i + 0.5) * h) for i in range(n))
    return sum_result * h

# Обчислення інтегралу методом прямокутників
result_left = left_rectangles(integrand, a, b, 10)
result_right = right_rectangles(integrand, a, b, 10)
result_middle = middle_rectangles(integrand, a, b, 10)

# Виведення результатів
print("Left rectangles:", round(result_left, 5))
print("Right rectangles:", round(result_right, 5))
print("Middle rectangles:", round(result_middle, 5))

# Перевірка
v, err = integrate.quad(integrand, a, b)
if abs(result_left - result_right) / 3. <= eps:
    print("Check for the rectangle method =", round(v, 5))


# Задаємо функцію, яку необхідно інтегрувати
def f(x):
    return np.sin(2*x) / x**2

# Задаємо межі інтегрування та початкову кількість розбиттів
a = 0.8
b = 1.2
n = 8

# Обчислюємо значення інтегралу методом Симпсона
def simpson_rule(f, a, b, n):
    h = (b - a) / n
    integr = f(a) + f(b)

    for i in range(1, n):
        k = a + i*h
        if i % 2 == 0:
            integr += 2 * f(k)
        else:
            integr += 4 * f(k)

    integr *= h / 3
    return integr

# Обчислюємо значення інтегралу методом Сімпсона з точністю 0.0001
integral1 = simpson_rule(f, a, b, n)
n *= 2
integral2 = simpson_rule(f, a, b, n)

while abs(integral2 - integral1) / 15 > 0.0001:
    integral1 = integral2
    n *= 2
    integral2 = simpson_rule(f, a, b, n)

# Виводимо результат
print("Simpson method:", round(integral2, 5))

# Перевірка 
v, err = integrate.quad(f, a, b)
print("Check for the Simpson method:", round(v, 5))

# Задаємо функцію, яку необхідно інтегрувати
def f(x):
    return 1.4 / (np.sqrt(12 * x**2 + 0.5))

# Задаємо межі інтегрування та початкову кількість розбиттів
a = 0.6
b = 1.4
n = 20

# Обчислюємо значення інтегралу методом трапецій
def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = a
    integral = 0.5 * (f(a) + f(b))
    
    for i in range(1, n):
        x += h
        integral += f(x)

    integral *= h
    return integral

# Обчислюємо значення інтегралу методом трапецій з точністю 0.0001
# Перевірка точності за правилом Рунге
integral1 = trapezoidal_rule(f, a, b, n)
n *= 2
integral2 = trapezoidal_rule(f, a, b, n)

while abs(integral2 - integral1) / 3 > 0.0001:
    integral1 = integral2
    n *= 2
    integral2 = trapezoidal_rule(f, a, b, n)

# Виводимо результат
print("Trapezoidal method:", round(integral2, 5))

# Перевірка результату за допомогою вбудованої функції quad
v, err = integrate.quad(f, a, b)
print("Check for the Trapezoidal method:", round(v, 5))
