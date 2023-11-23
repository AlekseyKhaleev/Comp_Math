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


def bisection_method(func: callable, a: float, b: float, epsilon: float) -> float:
    """
    Реализует метод половинного деления для численного решения уравнения
     f(x) = 0 на заданном отрезке [a, b].

    Параметры:
        a: Начало отрезка.
        b: Конец отрезка.
        epsilon: Точность решения.

    Возвращаемое значение:
        Приближенное значение корня уравнения f(x) = 0.
    """
    if func(a) * func(b) >= 0:
        raise ValueError("Условие существования корня не выполнено на заданном отрезке")

    while abs(func(x := ((a + b) / 2))) >= epsilon:
        if func(x) * func(a) < 0:
            b = x
        else:
            a = x
    return x


def main():
    # Использование методов
    a, b = step_method(func=f, start=0.8, step=0.01)
    root_bisection = bisection_method(f,a, b, epsilon=0.001)
    print(f"Метод половинного деления: {root_bisection:.4f}")


if __name__ == "__main__":
    main()
