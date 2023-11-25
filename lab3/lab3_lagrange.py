import operator
import warnings
from functools import reduce
from math import factorial

from scipy.misc import derivative

warnings.filterwarnings("ignore", category=DeprecationWarning)


def lagrange_interpolation(x_values, y_values, x):
    """
    Расчитывает значение в точке x для интерполирующего многочлена
    для данной последовательности точек, используя метод Лагранжа.

    Аргументы:
        x_values (list): список x-координат точек данных.
        y_values (list): список y-координат точек данных.
        x (float): точка, в которой вычисляется полином.

    Возвращает:
        float: значение интерполирующего полинома в точке x.
    """
    n = len(x_values)
    p = 0  # Инициализация интерполирующего полинома

    for i in range(n):
        L = 1  # Инициализация полинома Лагранжа
        for j in range(n):
            if i != j:
                L *= (x - x_values[j]) / (x_values[i] - x_values[j])
        p += y_values[i] * L

    return p


def lagrange_error(x_values, y_values, x):
    """
    Вычислить погрешность в интерполяции Лагранжа.

    Аргументы:
        x_values (list): список x-координат точек данных.
        x (float): точка, в которой вычисляется ошибка.

    Возвращает:
        float: оценка погрешности интерполяции Лагранжа в точке x.
    """
    n = len(x_values)
    product = reduce(operator.mul, [(x - xi) for xi in x_values])

    func = lambda x: lagrange_interpolation(x_values, y_values, x)
    # значение (n+1)-ой производной в точке x.
    nth_derivative = derivative(func, x0=x, n=n - 1, order=n + [1, 0][n % 2])

    return nth_derivative * product / factorial(n + 1)


if __name__ == "__main__":
    # Вычисление значений в точках
    x = [0.43, 0.48, 0.55, 0.62, 0.70, 0.75]
    y = [1.63597, 1.73234, 1.87686, 2.03345, 2.22846, 2.35973]

    x1 = [0.702, 0.512, 0.645, 0.736]
    y1 = [lagrange_interpolation(x, y, x1[i]) for i in range(len(x1))]
    err1 = [lagrange_error(x, y, x1[i]) for i in range(len(x1))]

    x2 = [0.503, 0.441, 0.602, 0.732]
    y2 = [lagrange_interpolation(x, y, x2[i]) for i in range(len(x2))]
    err2 = [lagrange_error(x, y, x2[i]) for i in range(len(x2))]
    print("Метод Лагранжа:")
    print("|  x1  |  y1  |     err1")
    print("|------|------| ---------")
    [print(
        f"|{x1[i]} |{y1[i]:.3f} | {err1[i]:.8f} ")
        for i in range(len(x1))]
    print("\n|  x2  |  y2  |     err2")
    print("|------|------| ---------")
    [print(
        f"|{x2[i]} |{y2[i]:.3f} | {err2[i]:.8f} ")
        for i in range(len(x1))]
