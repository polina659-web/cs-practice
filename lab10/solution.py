import numpy as np


def make_table(rows: int, columns: int) -> list[list[int]]:
    """Таблица формы (rows, columns) из чисел от 0 по порядку."""
    return np.arange(rows * columns).reshape(rows, columns).tolist()


def rectangle(matrix: list[list[float]], row_start: int, row_stop: int,
              column_start: int, column_stop: int) -> list[list[float]]:
    """Прямоугольный фрагмент матрицы обычным срезом."""
    arr = np.asarray(matrix, dtype=float)
    return arr[row_start:row_stop, column_start:column_stop].tolist()


def replace_rectangle(matrix: list[list[float]], row_start: int, row_stop: int,
                      column_start: int, column_stop: int,
                      value: float) -> list[list[float]]:
    """В независимой копии заменяет прямоугольный срез одним значением."""
    arr = np.asarray(matrix, dtype=float).copy()
    arr[row_start:row_stop, column_start:column_stop] = value
    return arr.tolist()


def matrix_vector_product(matrix: list[list[float]],
                          vector: list[float]) -> list[float]:
    """Умножение матрицы на вектор через оператор @."""
    arr = np.asarray(matrix, dtype=float)
    vec = np.asarray(vector, dtype=float)
    return (arr @ vec).tolist()


def matrix_multiply(left: list[list[float]],
                    right: list[list[float]]) -> list[list[float]]:
    """Матричное произведение left @ right."""
    return (np.asarray(left, dtype=float) @ np.asarray(right, dtype=float)).tolist()


def transpose_matrix(matrix: list[list[float]]) -> list[list[float]]:
    """Транспонирование: строки становятся столбцами."""
    return np.asarray(matrix, dtype=float).T.tolist()


def solve_system(matrix: list[list[float]],
                 vector: list[float]) -> list[float]:
    """Решение системы matrix @ x = vector через np.linalg.solve."""
    solution = np.linalg.solve(np.asarray(matrix, dtype=float),
                               np.asarray(vector, dtype=float))
    return [round(float(x), 6) for x in solution]


def tensor_channel_mean(tensor: list) -> list:
    """Усреднение последней оси тензора (например, RGB-каналов)."""
    arr = np.asarray(tensor, dtype=float)
    return arr.mean(axis=-1).tolist()


def point_distance(first: list[float], second: list[float]) -> float:
    """Евклидово расстояние между двумя точками."""
    distance = np.linalg.norm(np.asarray(first, dtype=float) -
                              np.asarray(second, dtype=float))
    return round(float(distance), 6)
