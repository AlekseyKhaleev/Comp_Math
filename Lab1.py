import math

from scipy.misc import derivative
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def f(x: int) -> float:
    """
    Вычисляет значение функции f(x) = x ** 3 + 0.2 * x ** 2 + 0.5 * x - 1.2

    Args:
        x: Значение аргумента функции.

    Returns:
        Значение функции в точке x.
    """
    return x ** 3 + 0.2 * x ** 2 + 0.5 * x - 1.2


def step_method(func: callable, start=0, step=0.01) -> tuple[int, int]:
    """
    Находит отрезок, содержащий корень функции.

    Args:
        func: Функция f(x), корень которой необходимо найти.
        start: Начало отрезка поиска.
        step: Шаг при переборе точек на отрезке.

    Returns:
        Кортеж с началом и концом сегмента, содержащего корень функции.
    """
    x0, x1 = start, start + step
    while func(x0) * func(x1) > 0:
        x0, x1 = x1, x1 + step
    return round(x0,2), round(x1,2)


def newton_method(a, b, epsilon):
    """
    Реализует метод Ньютона (метод касательных) для численного решения уравнения f(x) = 0 на заданном отрезке [a, b].

    Args:
        a: Начало отрезка.
        b: Конец отрезка.
        epsilon: Точность решения.

    Returns:
        Приближенное значение корня уравнения f(x) = 0.
    """
    if f(a) * f(b) >= 0:
        raise ValueError("Условие существования корня не выполнено на заданном отрезке")

    x0 = (a + b) / 2  # Начальное приближение (середина отрезка)
    x_prev = x0
    x_curr = x_prev - f(x_prev) / derivative(f, x0=x_prev)

    while abs(x_curr - x_prev) >= epsilon:
        x_prev = x_curr
        x_curr = x_prev - f(x_prev) / derivative(f, x0=x_prev)

    return x_curr


def simple_iteration_method(a, epsilon):
    """
    Реализует метод простых итераций для численного решения уравнения f(x) = 0 на заданном отрезке [a, b].
    Реализована для случая, когда функция f(x) = x ** 3 + 0.2 * x ** 2 + 0.5 * x - 1.2
    Так как g(x) = (1.2 - 0.2 * x ** 2 - 0.5 * x) ** (1 / 3) является эквивалетной, а
    g'(x) меньше 1 для обоих концов отрезка

    Args:
        a: Начало отрезка.
        epsilon: Точность решения.

    Returns:
        Приближенное значение корня уравнения f(x) = 0.
    """
    g = lambda x: (1.2 - 0.2 * x ** 2 - 0.5 * x) ** (1 / 3)
    if any(derivative(g, x0=point) >= 1 for point in [a, b]):
        raise ValueError("Условие сходимости не выполнено на заданном отрезке")

    x_prev = a
    x_curr = g(x_prev)
    while abs(f(x_curr)) >= epsilon:
        x_prev, x_curr = x_curr, g(x_prev)
    return x_curr


def bisection_method(a, b, epsilon):
    """
    Реализует метод половинного деления (бисекции) для численного решения уравнения f(x) = 0 на заданном отрезке [a, b].

    Args:
        a: Начало отрезка.
        b: Конец отрезка.
        epsilon: Точность решения.

    Returns:
        Приближенное значение корня уравнения f(x) = 0.
    """
    if f(a) * f(b) >= 0:
        raise ValueError("Условие существования корня не выполнено на заданном отрезке")

    while abs(b - a) >= epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2
def main():
    # Использование методов
    a, b = step_method(f)
    print(f"Корень уравнения находится на отрезке [{a}, {b}]")

    # epsilon = 0.0001
    #
    # root_bisection = round(bisection_method(a, b, epsilon), 3)
    # root_newton = round(newton_method(a, b, epsilon), 3)
    # root_simple_iteration = round(simple_iteration_method(a, epsilon), 3)
    #
    # print("Метод половинного деления: ", root_bisection)
    # print("Метод Ньютона: ", root_newton)
    # print("Метод простой итерации: ", root_simple_iteration)

if __name__ == "__main__":
    main()
