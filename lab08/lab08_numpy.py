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

# =====================
# Задание 4. Прямоугольные срезы
# =====================
matrix = np.arange(1, 26).reshape(5, 5)

print("Первые три строки:\n", matrix[:3])
print("Форма:", matrix[:3].shape)
print("Последние две строки:\n", matrix[3:])
print("Форма:", matrix[3:].shape)
print("Первые два столбца:\n", matrix[:, :2])
print("Форма:", matrix[:, :2].shape)
print("Строки 1-3, столбцы 2-4:\n", matrix[1:4, 2:5])
print("Форма:", matrix[1:4, 2:5].shape)
print("Угловой блок 2x2 справа внизу:\n", matrix[3:, 3:])
print("Форма:", matrix[3:, 3:].shape)

# =====================
# Задание 5. Изменение массива с помощью срезов
# =====================
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

# .copy() нужна, потому что обычное присваивание changed_hours = hours
# не создаёт новый массив: обе переменные смотрят на одни и те же данные,
# и любое изменение через срез испортило бы исходный hours.
changed_hours = hours.copy()
changed_hours[2:5] = 99    # элементы с индексами 2-4 -> 99
changed_hours[::2] = -1    # каждый второй элемент, начиная с первого, -> -1
print("changed_hours:", changed_hours)
print("Исходный hours:", hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0        # вся вторая строка -> нули
changed_matrix[:, -1] = -1      # последний столбец -> -1
changed_matrix[1:4, 1:4] = 100  # центральный блок 3x3 (индексы 1-3) -> 100
print("Изменённая матрица:\n", changed_matrix)
print("Исходная матрица:\n", matrix)

# =====================
# Задание 6. Изменение формы
# =====================
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("Форма numbers:", numbers.shape)
print("Форма table:", table.shape)
print("Форма transposed:", transposed.shape)
print("table:\n", table)
print("transposed:\n", transposed)

# reshape(3, 4) работает, потому что 3 * 4 = 12 — столько же элементов,
# сколько в numbers. reshape(5, 3) требует 5 * 3 = 15 элементов, а у нас
# их только 12, поэтому NumPy выдаёт ValueError.
