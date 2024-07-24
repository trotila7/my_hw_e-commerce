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

    @classmethod
    def create_product(cls, name, description, price, quantity_in_stock):
        """ Метод, который создает товар и возвращает объект, который можно добавлять в список товаров """
        return Product(name, description, price, quantity_in_stock)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("Цена введена некорректная. Цена должна быть больше нуля.")

    @price.deleter
    def price(self):
        print(f"Цена товара '{self.name}' удалена")
        self._price = None


if __name__ == "__main__":
    apple = Product.create_product('Яблоко', 'Зеленое яблоко', 11.4, 150)
    orange = Product.create_product("Апельсин", "Сочный апельсин", 14.6, 300)
    apple.price = 100
    del apple.price
    print(apple.price)
    # apple.price = -50
