from collections import Counter
import string


class ModuleClass:
    @staticmethod
    def first_task(numbers):
        if not all(isinstance(num, (int, float)) for num in numbers):
            raise ValueError("Все элементы списка должны быть числами.")
        return sum(numbers)

    @staticmethod
    def second_task(text):
        """
        Counts the number of unique words in a given string, ignoring punctuation and spaces.

        :param text: Input string.
        :return: Count of unique words.
        """
        # Удаление знаков препинания
        cleaned_text = text.translate(str.maketrans("", "", string.punctuation)).lower()
        # Разбиение на слова
        words = cleaned_text.split()
        # Подсчёт слов
        word_counts = Counter(words)
        return len(word_counts)
