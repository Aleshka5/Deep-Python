def process_file() -> None:
    try:
        # Открываем файл
        with open("data.txt", "r", encoding="utf-8") as file:
            data = file.readlines()

        # Проходим по строкам
        for line in data:
            line = line.strip()  # Убираем пробелы и переносы строк
            try:
                # Пробуем преобразовать строку в число
                number = float(line)
                print(number)  # Если преобразование успешно, выводим число
            except ValueError:
                # Если строка не может быть преобразована в число, выбрасываем TypeError
                raise TypeError(f"Невозможно преобразовать строку в число: {line}")

    except FileNotFoundError:
        # Обработка отсутствия файла
        print(f"Файл data.txt не найден.")
    except TypeError as te:
        # Обработка ошибок преобразования
        print(te)


if __name__ == "__main__":
    # Пример использования
    process_file()
