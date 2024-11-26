from module import ModuleClass

if __name__ == "__main__":
    # Обращение по первому заданию
    numbers = [1, 2, 3, 4.5]
    calculator = ModuleClass()
    result = calculator.first_task(numbers)
    print(f"Сумма чисел {numbers} равна {result}")

    # Обращение по второму заданию
    example_text = "Hello, world! Hello world; it's a wonderful world."
    unique_word_count = calculator.second_task(example_text)
    unique_word_count
