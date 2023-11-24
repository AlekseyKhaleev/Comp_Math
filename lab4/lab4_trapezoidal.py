import math


def func(x: float) -> float:
    return math.log10(x ** 2 + 1) / x  # подынтегральная функция


def trapezoidal_rule(a: float, b: float, n: int) -> float:
    """
       Вычисляет определенный интеграл функции с использованием метода трапеций.

       Аргументы:
           a (float): Нижний предел интегрирования.
           b (float): Верхний предел интегрирования.
           n (int): Количество интервалов, на которые разбивается область интегрирования.

       Возвращает:
           float: Приближенное значение определенного интеграла.
       """
    h = (b - a) / n  # шаг
    integral = 0  # аккумулятор значения интеграла

    for i in range(n + 1):
        x = a + i * h  # вычисление значения x на основании шага и индекса текущей итерации
        if i == 0 or i == n:
            integral += func(x) / 2  # первое и последнее значение делятся на 2
        else:
            integral += func(x)  # остальные значения прибавляются без изменений

    integral *= h  # умножение на шаг
    return integral


def main() -> None:
    # Вычисление интегралов
    integral_trapezoidal_8 = trapezoidal_rule(a=0.8, b=1.6, n=8)
    integral_trapezoidal_20 = trapezoidal_rule(a=0.8, b=1.6, n=20)
    error_rectangular = abs(integral_trapezoidal_20 - integral_trapezoidal_8)
    print("Интеграл по формуле трапеций:")
    print(f"n=8 : {integral_trapezoidal_8}\nn=20: {integral_trapezoidal_20}")
    print(f"Оценка погрешности: {round(error_rectangular, 4)}")


if __name__ == '__main__':
    main()
