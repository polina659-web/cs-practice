import numpy as np

# =====================
# Задание 1. Создание векторов и матриц
# =====================
hours = np.arange(0, 22, 3)          # числа от 0 до 21 с шагом 3
line = np.linspace(0, 1, 5)          # 5 равноудалённых чисел от 0 до 1 включительно
zeros = np.zeros(6, dtype=int)       # вектор из 6 нулей целого типа
unknown_table = np.full((2, 3), -1)  # матрица (2, 3), заполненная -1
identity = np.eye(3)                 # единичная матрица 3x3

print("hours:", hours)
print("hours shape:", hours.shape)
print("hours ndim:", hours.ndim)
print("hours size:", hours.size)
print("hours dtype:", hours.dtype)
print("line:", line)
print("zeros:", zeros)
print("unknown_table:\n", unknown_table)
print("identity:\n", identity)

# =====================
# Задание 2. Индексы и срезы в векторе
# =====================
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2-5:", hours[2:6])   # правая граница не входит
print("Каждый второй элемент:", hours[::2])
print("В обратном порядке:", hours[::-1])

# =====================
# Задание 3. Строки и столбцы таблицы
# =====================
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("Форма:", temperatures.shape)
print("Число измерений:", temperatures.ndim)
print("Число элементов:", temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])
print("Центральный фрагмент 2x2:\n", temperatures[:2, 1:3])
print("Форма центрального фрагмента:", temperatures[:2, 1:3].shape)

