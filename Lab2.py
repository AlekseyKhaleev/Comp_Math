import numpy as np

A = np.array([[3.11, -1.66, -0.6],
              [-1.65, 3.51, -0.78],
              [0.6, 0.78, -1.87]])

B = np.array([-0.92, 2.57, 1.65])


def gauss(a: np.ndarray, b: np.ndarray) -> np.ndarray:
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

    for i in range(n):
        max_row_index = np.abs(system[i:, i]).argmax() + i

        if i != max_row_index:
            system[[i, max_row_index]] = system[[max_row_index, i]]

        for j in range(i + 1, n):
            system[j] = system[j] - system[i] * system[j, i] / system[i, i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (system[i, -1] - np.dot(system[i, :-1], x)) / system[i, i]

    return x


def jacobi(a: np.ndarray, b: np.ndarray, epsilon: float = 0.0001, max_iterations: int = 1000) -> np.ndarray:
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

    for _ in range(max_iterations):
        x_new = np.copy(x)

        for i in range(n):
            s1 = np.dot(a[i, :i], x[:i])
            s2 = np.dot(a[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / a[i, i]

        if np.allclose(x, x_new, rtol=epsilon):
            break

        x = x_new

    return x


def gauss_seidel(a, b, epsilon=0.0001, max_iterations=1000):
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
    x = np.zeros(n)

    for _ in range(max_iterations):
        for i in range(n):
            s1 = np.dot(a[i, :i], x[:i])
            s2 = np.dot(a[i, i + 1:], x[i + 1:])
            x[i] = (b[i] - s1 - s2) / a[i, i]

        if np.allclose(np.dot(a, x), b, rtol=epsilon):
            break

    return x


solutions = [gauss(A, B), jacobi(A, B), gauss_seidel(A, B)]

for solution, name in zip(solutions, ["Gauss", "Simple iteration(Jacobi)", "Gauss-Seidel"]):
    print(f"{name} method:\n" + "; ".join(f'x{i} = {x:.4f}' for i, x in enumerate(solution, 1)))
