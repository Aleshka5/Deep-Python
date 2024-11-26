# Логирование операций
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger()


class Product:
    def __init__(self, name, quantity, price):
        self.name = name  # Название продукта
        self.quantity = quantity  # Кол-во продуктов
        self.price = price  # Цена

    def increase_quantity(self, amount):
        self.quantity += amount

    def decrease_quantity(self, amount):
        if amount > self.quantity:
            raise ValueError(f"Недостаточно товара '{self.name}' на складе.")
        self.quantity -= amount

    def calculate_total_cost(self):
        return self.quantity * self.price


class Warehouse:
    def __init__(self):
        self.products = {}  # Продукты на складе

    def add_product(self, product: Product):
        if product.name in self.products:
            self.products[product.name].increase_quantity(product.quantity)
        else:
            self.products[product.name] = product
        logger.info(f"Добавлен {product.name} в кол-ве {product.quantity}")

    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]
        else:
            raise ValueError(f"Товар '{product_name}' отсутствует на складе.")

    def calculate_total_value(self):
        warehouse_value = sum(
            product.calculate_total_cost() for product in self.products.values()
        )
        logger.info(f"Оставшаяся стоимость товаров на складе: {warehouse_value} руб.")
        return warehouse_value


class Seller:
    def __init__(self, name):
        self.name = name
        self.sales_report = []
        self.total_revenue = 0

    def sell_product(self, warehouse, product_name, quantity):
        if product_name not in warehouse.products:
            raise ValueError(f"Товар '{product_name}' отсутствует на складе.")

        product = warehouse.products[product_name]
        product.decrease_quantity(quantity)

        cost = product.price * quantity
        self.sales_report.append(
            {"name": product_name, "quantity": quantity, "revenue": cost}
        )
        self.total_revenue += cost

        # Удалить товар, если его количество стало равно нулю
        if product.quantity == 0:
            warehouse.remove_product(product_name)
            logger.info(f"Товар {product.name} удалён")

        logger.info(f"Продали {quantity} товара {product_name}")

    def generate_sales_report(self):
        report_lines = [
            f"{sale['quantity']} x {sale['name']} = {sale['revenue']} руб."
            for sale in self.sales_report
        ]
        report = "\n".join(report_lines) + f"\nОбщая выручка: {self.total_revenue} руб."
        logger.info(f"Отчёт о продажах:\n{report}")
        return report


if __name__ == "__main__":
    # Демонстрация работы системы
    warehouse = Warehouse()
    seller = Seller(name="Анна")

    # Добавление товаров
    warehouse.add_product(Product(name="Молоко", quantity=50, price=60))
    warehouse.add_product(Product(name="Хлеб", quantity=30, price=40))
    warehouse.add_product(Product(name="Яблоки", quantity=100, price=20))

    # Продажа товаров
    seller.sell_product(warehouse, "Молоко", 10)
    seller.sell_product(warehouse, "Хлеб", 5)
    seller.sell_product(warehouse, "Яблоки", 20)

    # Отчёт о продажах
    sales_report = seller.generate_sales_report()

    # Вывод итогов
    warehouse_value = warehouse.calculate_total_value()
