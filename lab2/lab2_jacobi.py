import numpy as np
def jacobi(a: np.ndarray, b: np.ndarray, epsilon: float, max_iterations: int = 1000) -> np.ndarray:
    """
    Рассчитывает решение системы линейных уравнений с использованием метода Якоби.

    Параметры:
        a (numpy.ndarray): Матрица коэффициентов системы линейных уравнений.
        b (numpy.ndarray): Вектор правых частей системы линейных уравнений.
        epsilon (float, опционально): Точность сходимости. По умолчанию 0.0001.
        max_iterations (int, опционально): Максимальное количество итераций. По умолчанию 1000.

    Возвращает:
        x (numpy.ndarray): Вектор решения системы линейных уравнений.
    """
    n = len(a)
    x = np.zeros(n)
    tmp = 0
    for _ in range(max_iterations):
        x_new = np.copy(x)
        tmp += 1

        for i in range(n):
            s1 = np.dot(a[i, :i], x[:i])
            s2 = np.dot(a[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / a[i, i]

        if np.allclose(x, x_new, rtol=epsilon):
            break

        x = x_new
    print(f"Количеcтво итераций: {tmp}")
    return x


def main() -> None:
    # Использование методов
    A = np.array([[3.11, -1.66, -0.6],
                  [-1.65, 3.51, -0.78],
                  [0.6, 0.78, -1.87]])

    B = np.array([-0.92, 2.57, 1.65])

    solution = jacobi(A, B, epsilon=0.001)
    print(f"Решение методом простых итераций (Якоби):")
    print("; ".join(f'x{i} = {x:.4f}' for i, x in enumerate(solution, 1)))


if __name__ == '__main__':
    main()