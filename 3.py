# import sympy as sp

# # Оголосимо символьну змінну x
# x = sp.symbols('x')

# # Визначимо рівняння
# equation = 6*x**4 + 8*x**3 - 24*x**2 - 7

# # Початкове наближення для методу Ньютона
# x0 = 1.0

# # Визначимо похідну рівняння
# derivative = sp.diff(equation, x)

# # Проведемо ітерації методом Ньютона
# for i in range(100):
#     f_x0 = equation.subs(x, x0)
#     df_x0 = derivative.subs(x, x0)
#     if df_x0 == 0:
#         print("Похибка: Похідна рівна 0. Зупинка ітерації.")
#         break
#     x0 = x0 - f_x0 / df_x0
#     if abs(f_x0) < 1e-6:
#         break
# else:
#     print("Похибка: Досягнуто максимальну кількість ітерацій без знаходження розв'язку.")

# # Результат
# print(f"Розв'язок методом Ньютона: x = {x0}")

import sympy as sp

# Оголосимо символьну змінну x
x = sp.symbols('x')

# Визначимо рівняння
equation = 6*x**4 + 8*x**3 - 24*x**2 - 7

# Початкові наближення для методу січення і методу Ньютона
x0 = 1.0
x1 = 0.9

# Проведемо ітерації комбінованим методом
for i in range(100):
    f0 = equation.subs(x, x0)
    f1 = equation.subs(x, x1)
    df = (f1 - f0) / (x1 - x0)

    x2 = x1 - f1 / df

    if abs(equation.subs(x, x2)) < 1e-6:
        break

    x0, x1 = x1, x2

# Результат
print(f"Розв'язок комбінованим методом: x = {x2}")
