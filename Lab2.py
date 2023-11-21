import numpy as np

A = np.array([[3.11, -1.66, -0.6],
              [-1.65, 3.51, -0.78],
              [0.6, 0.78, -1.87]])

b = np.array([-0.92, 1.65, 1.65])


def gauss_elimination(A, b, epsilon=0.001):
    n = len(A)
    Ab = np.concatenate((A, b.reshape(n, 1)), axis=1)
    for i in range(n):
        # Поиск максимального элемента в столбце под текущей диагональю
        max_row = i
        for j in range(i + 1, n):
            if abs(Ab[j, i]) > abs(Ab[max_row, i]):
                max_row = j

        # Перестановка строк, чтобы максимальный элемент был на диагонали
        Ab[[i, max_row]] = Ab[[max_row, i]]
        if abs(Ab[i, i]) < epsilon:
            raise ValueError("Система уравнений не имеет единственного решения")

        # Приведение к треугольному виду
        for j in range(i + 1, n):
            ratio = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= ratio * Ab[i, i:]
    # Обратный ход
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i + 1:-1], x[i + 1:])) / Ab[i, i]

    return list(round(el, 2) for el in x)


def jacobi_iteration(A, b, epsilon=0.001, max_iterations=1000):
    n = len(A)
    x = np.zeros(n)
    x_new = np.zeros(n)
    iterations = 0
    error = epsilon + 1

    while error > epsilon and iterations < max_iterations:
        for i in range(n):
            x_new[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

        error = np.max(np.abs(x_new - x))
        x = x_new.copy()
        iterations += 1

    if iterations == max_iterations:
        raise ValueError("Метод Якоби не сошелся за заданное количество итераций")

    return [round(el, 2) for el in x]


def gauss_seidel_iteration(A, b, epsilon=0.001, max_iterations=1000):
    n = len(A)
    x = np.zeros(n)
    iterations = 0
    error = epsilon + 1

    while error > epsilon and iterations < max_iterations:
        x_prev = x.copy()

        for i in range(n):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i + 1:], x_prev[i + 1:])) / A[i, i]

        error = np.max(np.abs(x - x_prev))
        iterations += 1

    if iterations == max_iterations:
        raise ValueError("Метод Гаусса-Зейделя не сошелся за заданное количество итераций")

    return list(round(el, 2) for el in x)


solutions = [gauss_elimination(A, b), jacobi_iteration(A, b), gauss_seidel_iteration(A, b)]

for solution, name in zip(solutions, ["Gauss", "Simple iteration(Jacobi)", "Gauss-Seidel"]):
    print(f"{name} method:\n" + "; ".join(f'x{i} = {x:.2f}' for i, x in enumerate(solution, 1)))
