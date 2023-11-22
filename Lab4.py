import numpy as np


def func(x):
    return (np.log10(x ** 2 + 1)) / x


def rectangular_rule(a, b, n):
    """
    Вычисляет определенный интеграл функции с использованием метода прямоугольников.

    Аргументы:
        a (float): Нижний предел интегрирования.
        b (float): Верхний предел интегрирования.
        n (int): Количество интервалов, на которые разбивается область интегрирования.

    Возвращает:
        float: Приближенное значение определенного интеграла.
    """
    h = (b - a) / n
    integral = 0

    for i in range(n):
        x = a + (i + 0.5) * h
        integral += func(x)

    integral *= h
    return integral


def trapezoidal_rule(a, b, n):
    """
    Вычисляет определенный интеграл функции с использованием метода трапеций.

    Аргументы:
        a (float): Нижний предел интегрирования.
        b (float): Верхний предел интегрирования.
        n (int): Количество интервалов, на которые разбивается область интегрирования.

    Возвращает:
        float: Приближенное значение определенного интеграла.
    """
    h = (b - a) / n
    integral = 0

    for i in range(n + 1):
        x = a + i * h
        if i == 0 or i == n:
            integral += func(x) / 2
        else:
            integral += func(x)

    integral *= h
    return integral


def simpsons_rule(a, b, n):
    """
    Вычисляет определенный интеграл функции с использованием правила Симпсона.

    Параметры:
        a (float): Нижний предел интегрирования.
        b (float): Верхний предел интегрирования.
        n (int): Количество подинтервалов. Должно быть четным числом.

    Возвращает:
        float: Приближенное значение определенного интеграла.
    """
    if n % 2 != 0:
        raise ValueError("n must be an even number.")

    h = (b - a) / n
    integral = 0

    for i in range(n + 1):
        x = a + i * h
        if i == 0 or i == n:
            integral += func(x)
        elif i % 2 == 0:
            integral += 2 * func(x)
        else:
            integral += 4 * func(x)

    integral *= h / 3
    return integral


# Вычисление интегралов
a = 0.8
b = 1.6
n1 = 8
n2 = 20

integral_rectangular_8 = rectangular_rule(a, b, n1)
integral_rectangular_20 = rectangular_rule(a, b, n2)

integral_trapezoidal_8 = trapezoidal_rule(a, b, n1)
integral_trapezoidal_20 = trapezoidal_rule(a, b, n2)

integral_simpsons_8 = simpsons_rule(a, b, n1)
integral_simpsons_20 = simpsons_rule(a, b, n2)

# Оценка погрешности результата
error_rectangular = abs(integral_rectangular_20 - integral_rectangular_8)
error_trapezoidal = abs(integral_trapezoidal_20 - integral_trapezoidal_8)
error_simpsons = abs(integral_simpsons_20 - integral_simpsons_8)

print("Интеграл по формуле центральных прямоугольников:")
print(f"n=8: {integral_rectangular_8}, Оценка погрешности: {error_rectangular}")
print(f"n=20: {integral_rectangular_20}")

print("\nИнтеграл по формуле трапеций:")
print(f"n=8: {integral_trapezoidal_8}, Оценка погрешности: {error_trapezoidal}")
print(f"n=20: {integral_trapezoidal_20}")

print("\nИнтеграл по формуле Симпсона:")
print(f"n=8: {integral_simpsons_8}, Оценка погрешности: {error_simpsons}")
print(f"n=20: {integral_simpsons_20}")