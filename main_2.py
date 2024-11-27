import itertools

# Создание бесконечного генератора чисел
try:
    infinite_generator = itertools.count(
        start=1, step=1
    )  # Генератор чисел, начиная с 1
    for _ in range(5):  # Для примера, выведем только первые 5 чисел
        print("Число из бесконечного генератора:", next(infinite_generator))
except Exception as e:
    print("Ошибка при работе с бесконечным генератором:", e)

# Применение функции к каждому элементу в итераторе
try:
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = map(
        lambda x: x**2, numbers
    )  # Применение функции возведения в квадрат
    print("Квадраты чисел:", list(squared_numbers))
except Exception as e:
    print("Ошибка при применении функции:", e)

# Объединение нескольких итераторов в один
try:
    iterator1 = [1, 2, 3]
    iterator2 = [4, 5, 6]
    iterator3 = []
    combined_iterator = itertools.chain(
        iterator1, iterator2, iterator3
    )  # Объединение итераторов
    combined_list = list(combined_iterator)  # Преобразуем в список для вывода
    if not combined_list:
        raise ValueError("Объединенный итератор пуст.")  # Проверка на отсутствие данных
    print("Объединенный список:", combined_list)
except ValueError as ve:
    print("Итератор пуст:", ve)
except Exception as e:
    print("Ошибка при объединении итераторов:", e)
