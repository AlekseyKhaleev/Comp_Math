import operator
import warnings
from functools import reduce
from math import factorial

from scipy.misc import derivative

warnings.filterwarnings("ignore", category=DeprecationWarning)


def newton_interpolation(x, y, x0):
    """
    Вычисляет значение интерполированной функции в точке x0 с использованием второй интерполяционной формулы Ньютона.

    Параметры:
    x (list): Список точек интерполяции.
    y (list): Список значений функции в точках интерполяции.
    x0 (float): Точка, в которой требуется вычислить значение интерполированной функции.

    Возвращает:
    y0 (float): Значение интерполированной функции в точке x0.
    """
    n = len(x)

    # Инициализация разделенной разности
    fdd = [[0 for x in range(n)]
            for y in range(n)]
    y = y.copy()

    # Заполнение нулевой строки таблицы разделенных разностей
    for i in range(n):
        fdd[i][0] = y[i]

    # Заполнение других строк таблицы разделенных разностей
    for i in range(1, n):
        for j in range(n - i):
            # Вычисление i-ой разделенной разности
            fdd[j][i] = (fdd[j + 1][i - 1] - fdd[j][i - 1]) / (x[i + j] - x[j])

    # Вычисление значения интерполированной функции
    y0 = fdd[0][0]
    for i in range(1, n):
        prod = 1
        for j in range(i):
            prod *= (x0 - x[j])
        # Добавление i-ого слагаемого в сумму
        y0 += prod * fdd[0][i]

    return y0


if __name__ == "__main__":
    # Вычисление значений в точках
    x = [1.34, 1.345, 1.35, 1.355, 1.36, 1.365, 1.37, 1.375, 1.38, 1.385, 1.39, 1.395]
    y = [4.25562, 4.35325, 4.45522, 4.56184, 4.67344, 4.79038, 4.91306, 5.04192, 5.17744, 5.32016, 5.47069, 5.62968]

    x1 = [1.3617, 1.3921, 1.3359, 1.4]
    y1 = [newton_interpolation(x, y, x1[i]) for i in range(len(x1))]

    print("Метод Ньютона (2 формула):")
    print("|  x1  |  y1 |")
    print("|------|-----|")
    [print(
        f"|{x1[i]:.3f} |{y1[i]:.3f}|")
        for i in range(len(x1))]

