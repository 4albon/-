# def f(x):
#     return 6*x**4 + 8*x**3 - 24*x**2 - 7

# def bisection_method(a, b, tolerance):
#     if f(a) * f(b) >= 0:
#         print("Помилка: Функція не змінює знак між a та b")
#         return None

#     while (b - a) / 2.0 > tolerance:
#         c = (a + b) / 2.0
#         if f(c) == 0:
#             return c
#         elif f(c) * f(a) < 0:
#             b = c
#         else:
#             a = c

#     return (a + b) / 2.0

# a = -2.0
# b = 0.0
# tolerance = 0.0001
# result = bisection_method(a, b, tolerance)
# print("Метод половинного ділення для x2:", result)



def f(x):
    return 6*x**4 + 8*x**3 - 24*x**2 - 7

def secant_method(x0, x1, tolerance, max_iterations):
    for i in range(max_iterations):
        if abs(f(x1) - f(x0)) < tolerance:
            return x1
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        x0, x1 = x1, x2
    return x1

x0 = -2.0
x1 = 0.0
tolerance = 0.0001
max_iterations = 100
result = secant_method(x0, x1, tolerance, max_iterations)
print("Метод хорд для x2:", result)

