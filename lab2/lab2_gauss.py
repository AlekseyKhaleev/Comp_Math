import numpy as np


def gauss(a: np.array, b: np.array) -> np.ndarray:
    """
    Рассчитывает решение системы линейных уравнений с использованием метода Гаусса.

    Параметры:
        a (numpy.ndarray): Матрица коэффициентов системы линейных уравнений.
        b (numpy.ndarray): Вектор правых частей системы линейных уравнений.

    Возвращает:
        x (numpy.ndarray): Вектор решения системы линейных уравнений.
    """
    n = len(a)
    system = np.hstack([a, b.reshape(-1, 1)])
    print(f"Объединенная матрица системы линейных уравнений:\n{system}")

    for i in range(n):
        # нахождение индекса строки с максимальным абсолютным значением
        max_row_index = np.abs(system[i:, i]).argmax() + i

        # перестановка строк
        if i != max_row_index:
            system[[i, max_row_index]] = system[[max_row_index, i]]

        # зануление i-тых элементов строк
        for j in range(i + 1, n):
            system[j] = system[j] - system[i] * system[j, i] / system[i, i]
    print(f"Система приведена к треугольному виду:\n{system.round(4)}")
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (system[i, -1] - np.dot(system[i, :-1], x)) / system[i, i]

    return x


def main() -> None:
    # Использование методов
    A = np.array([[3.11, -1.66, -0.6],
                  [-1.65, 3.51, -0.78],
                  [0.6, 0.78, -1.87]])

    B = np.array([-0.92, 2.57, 1.65])

    solution = gauss(A, B)
    print(f"Решение методом Гаусса:")
    print("; ".join(f'x{i} = {x:.4f}' for i, x in enumerate(solution, 1)))


if __name__ == '__main__':
    main()
