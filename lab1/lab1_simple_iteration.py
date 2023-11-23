from scipy.misc import derivative
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


def f(x: float) -> float:
    """
    Вычисляет значение функции f(x) = x ** 3 + 0.2 * x ** 2 + 0.5 * x - 1.2

    Параметры:
        x: Значение аргумента функции.

    Возвращаемое значение:
        Значение функции в точке x.
    """
    return x ** 3 + 0.2 * x ** 2 + 0.5 * x - 1.2


def step_method(func: callable, start: float, step: float) -> tuple[int, int]:
    """
    Находит отрезок, содержащий корень функции.

    Параметры:
        func: Функция f(x), корень которой необходимо найти.
        start: Начало отрезка поиска.
        step: Шаг при переборе точек на отрезке.

    Возвращаемое значение:
        Кортеж с началом и концом сегмента, содержащего корень функции.
    """
    x0, x1 = start, start + step
    while func(x0) * func(x1) >= 0:
        x0, x1 = x1, x1 + step
    return round(x0, 2), round(x1, 2)


def simple_iteration_method(func: callable, a: float, b: float, epsilon: float) -> float:
    """
    Реализует метод простых итераций для численного решения уравнения
       f(x) = 0 на заданном отрезке [a, b].
    Реализовано для функции f(x) = x ** 3 + 0.2 * x ** 2 + 0.5 * x - 1.2 = 0
    Тогда g(x) = (1.2 - 0.2 * x ** 2 - 0.5 * x) ** (1 / 3) является эквивалентной,
      так как g'(x) меньше 1 для обоих концов отрезка

    Параметры:
        a: Начало отрезка.
        epsilon: Точность решения.

    Возвращаемое значение:
        Приближенное значение корня уравнения f(x) = 0.
    """
    g = lambda x: (1.2 - 0.2 * x ** 2 - 0.5 * x) ** (1 / 3)
    if any(derivative(g, x0=point) >= 1 for point in [a, b]):
        raise ValueError("Условие сходимости не выполнено на заданном отрезке")
    xi = g(a)
    while abs(func(xi)) >= epsilon:
        xi = g(xi)
    return xi


def main():
    # Использование методов
    a, b = step_method(func=f, start=0.8, step=0.01)
    root_jacobi = simple_iteration_method(f, a, b, epsilon=0.001)
    print(f"Метод простых итераций (Якоби): {root_jacobi:.4f}")


if __name__ == "__main__":
    main()
