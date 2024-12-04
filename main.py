import db

# Пример вызова
if __name__ == "__main__":
    print("1. Продукты в полуинтервале [3, 7):", db.request())
    print(
        "2. Минимальная цена в 1 категории:",
        db.get_min_price_by_category(category_id=1),
    )
    print(
        "3. Максимальная цена продукта у каждого поставщика:",
        db.get_max_price_by_suppliers(),
    )
