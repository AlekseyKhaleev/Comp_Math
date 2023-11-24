import math


def func(x: float) -> float:
    return math.log10(x ** 2 + 1) / x  # подынтегральная функция


def simpson_rule(a: float, b: float, n: int) -> float:
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
        raise ValueError("число n должно быть четным")

    h = (b - a) / n  # шаг
    integral = 0  # аккумулятор значения интеграла

    for i in range(n + 1):
        x = a + i * h  # вычисление значения x на основании шага и индекса текущей итерации
        if i == 0 or i == n:
            integral += func(x)  # первый и последний индекс без множителя
        elif i % 2 == 0:
            integral += 2 * func(x)  # для четных индексов множитель = 2
        else:
            integral += 4 * func(x)  # для нечетных индексов множитель = 4

    integral *= h / 3  # умножаем полученную сумму на коэффициент (шаг деленный на 3)
    return integral


def main() -> None:
    # Вычисление интегралов
    integral_simpson_8 = simpson_rule(a=0.8, b=1.6, n=8)
    integral_simpson_20 = simpson_rule(a=0.8, b=1.6, n=20)
    error_rectangular = abs(integral_simpson_20 - integral_simpson_8)
    print("Интеграл по формуле Симпсона:")
    print(f"n=8 : {integral_simpson_8}\nn=20: {integral_simpson_20}")
    print(f"Оценка погрешности: {error_rectangular:.7f}")


if __name__ == '__main__':
    main()
