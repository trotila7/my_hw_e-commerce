class Product:
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    @staticmethod
    def create_product(name, description, price, quantity_in_stock):
        return Product(name, description, price, quantity_in_stock)

    @property
    def name_prod(self):
        name_prod = self.name
        return name_prod

    @property
    def product_info(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity_in_stock} шт."

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("Цена введена некорректная. Цена должна быть больше нуля.")


apple = Product('Яблоко', 'Зеленое яблоко', 11.4, 150)
orange = Product("Апельсин", "Сочный апельсин", 14.6, 300)

if __name__ == "__main__":
    print(apple.price_and_quan)
