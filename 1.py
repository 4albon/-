import math

# Вихідні значення
exact_sqrt_74 = math.sqrt(74)
exact_12_div_11 = 12 / 11

# Наближені значення
approx_sqrt_74 = 8.60
approx_12_div_11 = 1.091

# Розрахунок абсолютних похибок
error_sqrt_74 = abs(exact_sqrt_74 - approx_sqrt_74)
error_12_div_11 = abs(exact_12_div_11 - approx_12_div_11)

# Порівняння похибок і виведення результату
if error_sqrt_74 < error_12_div_11:
    print("√74 ~ 8.60 є точнішою рівністю.")
else:
    print("12/11 ~ 1.091 є точнішою рівністю.")


