class DataBuffer:
    def __init__(self):
        self.buffer = []

    def add_data(self, data):
        self.buffer.append(data)
        if len(self.buffer) >= 5:
            print("Буфер переполнен. Очистка буфера:", self.buffer)
            # Очищаем буфер
            self.buffer = []
        print("Текущий буфер:", self.get_data())

    def get_data(self):
        if not self.buffer:
            print("Буфер пуст. Данные отсутствуют.")
            return None

        return self.buffer


if __name__ == "__main__":
    # Пример использования
    buffer = DataBuffer()

    # Добавление данных
    buffer.add_data(1)
    buffer.add_data(2)
    buffer.add_data(3)
    buffer.add_data(4)
    print(" -- Переполнение --")
    buffer.add_data(5)

    # Проверка на отсутствие данных
    # buffer.get_data()
