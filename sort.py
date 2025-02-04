class Product:
    def __init__(self, name, quantity, quality):
        self.name = name
        self.quantity = quantity
        self.quality = quality

    def __str__(self):
        return f"{self.name}, Количество: {self.quantity}, Качество: {self.quality}"


def main():
    # Список продуктов
    products = [
        Product("Яблоки", 50, "Высокое"),
        Product("Молоко", 20, "Среднее"),
        Product("Хлеб", 100, "Высокое"),
        Product("Мясо", 10, "Низкое"),
        Product("Картофель", 70, "Среднее")
    ]

    # Сортировка по количеству
    products.sort(key=lambda p: p.quantity)

    # Вывод отсортированного списка по количеству
    print("Продукты, отсортированные по количеству:")
    for product in products:
        print(product)

    print()

    # Сортировка по качеству
    # Используем словарь для приоритета качества: "Высокое" > "Среднее" > "Низкое"
    quality_order = {"Высокое": 3, "Среднее": 2, "Низкое": 1}
    products.sort(key=lambda p: quality_order[p.quality], reverse=True)

    # Вывод отсортированного списка по качеству
    print("Продукты, отсортированные по качеству:")
    for product in products:
        print(product)


if __name__ == "__main__":
    main()
