import numpy as np


def gauss_seidel(a, b, epsilon=0.001, max_iterations=1000):
    """
    Рассчитывает решение системы линейных уравнений с использованием метода Гаусса-Зейделя.

    Параметры:
        a (numpy.ndarray): Матрица коэффициентов системы линейных уравнений.
        b (numpy.ndarray): Вектор правых частей системы линейных уравнений.
        epsilon (float, опционально): Точность сходимости. По умолчанию 0.0001.
        max_iterations (int, опционально): Максимальное количество итераций. По умолчанию 1000.

    Возвращает:
        x (numpy.ndarray): Вектор решения системы линейных уравнений.
    """
    n = len(a)
    x = np.zeros(n)  # начальное приближение (нулевой вектор)
    it_counter = 0
    for _ in range(max_iterations):
        it_counter += 1
        for i in range(n):
            s1 = np.dot(a[i, :i], x[:i])  # произведение векторов (срезов, чтобы исключить диагональные элементы)
            s2 = np.dot(a[i, i + 1:], x[i + 1:])
            x[i] = (b[i] - s1 - s2) / a[i, i]  # обновление значений вектора в процессе итерации

        if np.allclose(np.dot(a, x), b, rtol=epsilon):  # проверка на соответствие заданной точности
            break
    print(f"Количеcтво итераций: {it_counter}")
    return x


def main() -> None:
    # Использование методов
    A = np.array([[3.11, -1.66, -0.6],
                  [-1.65, 3.51, -0.78],
                  [0.6, 0.78, -1.87]])

    B = np.array([-0.92, 2.57, 1.65])

    solution = gauss_seidel(A, B, epsilon=0.001)
    print(f"Решение методом Гаусса-Зейделя:")
    print("; ".join(f'x{i} = {x:.4f}' for i, x in enumerate(solution, 1)))


if __name__ == '__main__':
    main()
