class Product:
    """Класс описывающий каждый продукт"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс описывающий каждую категорию товара"""
    number_of_categories = 0
    number_of_products = 0

    name: str
    description: str
    products: list[Product]

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.number_of_categories += 1
        Category.number_of_products += len(self.products)

