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


def newton_method(func: callable, a: float, b: float, epsilon: float) -> float:
    """
    Реализует метод Ньютона (метод касательных)
    для численного решения уравнения f(x) = 0 на заданном отрезке [a, b].

    Параметры:
        func: Функция f(x), корень которой необходимо найти.
        a: Начало отрезка.
        b: Конец отрезка.
        epsilon: Точность решения.

    Возвращаемое значение:
        Приближенное значение корня уравнения f(x) = 0.
    """

    x = a if func(a) * derivative(func, x0=a, n=2) > 0 else b  # начальное приближение
    next_value = lambda x: x - func(x) / derivative(func, x0=x)  # итерационная формула

    while func(x) >= epsilon:
        x = next_value(x)

    return x


def main():
    # Использование методов
    a, b = step_method(func=f, start=0.8, step=0.01)
    root_newton = newton_method(f, a, b, epsilon=0.001)
    print(f"Метод Ньютона (метод касательных): {root_newton:.4f}")


if __name__ == "__main__":
    main()
