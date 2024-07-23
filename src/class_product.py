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
        """ Метод, который создает товар и возвращает объект, который можно добавлять в список товаров """
        return Product(name, description, price, quantity_in_stock)

    @property
    def info_product(self):
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
