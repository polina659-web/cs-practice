import numpy as np


def make_hours() -> list[int]:
    """Вектор часов: от 0 до 21 с шагом 3."""
    return np.arange(0, 22, 3).tolist()


def vector_report(values: list[float]) -> dict:
    """Третий, последний, средний срез, каждый второй и развёрнутый вектор."""
    arr = np.asarray(values, dtype=float)
    return {
        "third": float(arr[2]),
        "last": float(arr[-1]),
        "middle": arr[2:6].tolist(),
        "every_second": arr[::2].tolist(),
        "reversed": arr[::-1].tolist(),
    }


def change_vector(values: list[float]) -> list[float]:
    """В независимой копии: индексы 2-4 -> 99, затем каждый второй -> -1."""
    arr = np.asarray(values, dtype=float).copy()
    arr[2:5] = 99   # правая граница не входит: индексы 2, 3, 4
    arr[::2] = -1   # каждый второй элемент, начиная с первого
    return arr.tolist()


def cap_above(values: list[float], limit: float) -> list[float]:
    """Одна маска: всё, что больше limit, становится равным limit."""
    arr = np.asarray(values, dtype=float).copy()
    arr[arr > limit] = limit
    return arr.tolist()


def celsius_to_fahrenheit(values: list[float]) -> list[float]:
    """Перевод всего вектора из Цельсия в Фаренгейт без цикла."""
    arr = np.asarray(values, dtype=float)
    return (arr * 9 / 5 + 32).tolist()
