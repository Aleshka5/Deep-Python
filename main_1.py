from datetime import datetime

# Отображение текущей даты и времени
current_datetime = datetime.now()
print("Текущая дата и время:", current_datetime)

# Вычисление разницы между двумя датами
date1 = datetime(2024, 11, 27, 14, 0)  # Первая дата
date2 = datetime(2024, 12, 25, 18, 0)  # Вторая дата
date_difference = date2 - date1  # Разница между датами
print("Разница между двумя датами:", date_difference)

# Преобразование строки в объект даты и времени
date_string = "2024-11-27 15:30:00"  # Строка с датой
date_object = datetime.strptime(
    date_string, "%Y-%m-%d %H:%M:%S"
)  # Преобразование строки в объект datetime
print("Преобразованная дата и время из строки:", date_object)
