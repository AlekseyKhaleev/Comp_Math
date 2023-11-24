import math


def func(x: float) -> float:
    return math.log10(x ** 2 + 1) / x  # подынтегральная функция


def rectangular_rule(a: float, b: float, n: int) -> float:
    """
    Вычисляет определенный интеграл функции с использованием метода центральных прямоугольников.

    Аргументы:
        a (float): Нижний предел интегрирования.
        b (float): Верхний предел интегрирования.
        n (int): Количество интервалов, на которые разбивается область интегрирования.

    Возвращает:
        float: Приближенное значение определенного интеграла.
    """
    h = (b - a) / n  # шаг
    integral = 0  # аккумулятор значения интеграла

    for i in range(n):
        x = a + h * (i + 0.5)  # вычисление значения Xi-1/2 с учетом 0-индексированного цикла
        integral += h * func(x)  # аккумуляция значения интеграла
    return integral


def main() -> None:
    # Вычисление интегралов
    integral_rectangular_8 = rectangular_rule(a=0.8, b=1.6, n=8)
    integral_rectangular_20 = rectangular_rule(a=0.8, b=1.6, n=20)
    error_rectangular = abs(integral_rectangular_20 - integral_rectangular_8)
    print("Интеграл по формуле центральных прямоугольников:")
    print(f"n=8 : {integral_rectangular_8}\nn=20: {integral_rectangular_20}")
    print(f"Оценка погрешности: {round(error_rectangular, 4)}")


if __name__ == '__main__':
    main()
