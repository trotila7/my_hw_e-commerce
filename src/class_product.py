class Product:
    name: str
    description: str
    price: float
    quantity_in_stock: int
    color: str

    def __init__(self, name, description, price, quantity_in_stock, color):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        self.color = color

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity_in_stock} шт.'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            total_value_self = self.price * self.quantity_in_stock
            total_value_other = other.price * other.quantity_in_stock
            return total_value_self + total_value_other
        raise TypeError

    @classmethod
    def create_product(cls, *args):
        """ Метод, который создает товар и возвращает объект, который можно добавлять в список товаров """
        if cls == Product:
            return cls(*args)
        raise NotImplementedError("Создание продукта для этого класса не поддерживается")

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


class Smartphone(Product):
    performance: float
    model: str
    internal_memory: int

    def __init__(self, name, description, price, quantity_in_stock, color, performance, model, internal_memory):
        super().__init__(name, description, price, quantity_in_stock, color)
        self.performance = performance
        self.model = model
        self.internal_memory = internal_memory

    @classmethod
    def create_product(cls, name, description, price, quantity_in_stock, color, performance, model, internal_memory):
        if cls == Smartphone:
            """ Метод, который создает товар и возвращает объект, который можно добавлять в список товаров """
            return cls(name, description, price, quantity_in_stock, color, performance,
                       model,
                       internal_memory)
        return super().create_product(name, description, price, quantity_in_stock, color)


class LawnGrass(Product):
    made_in: str
    germination: float

    def __init__(self, name, description, price, quantity_in_stock, color, made_in, germination):
        super().__init__(name, description, price, quantity_in_stock, color)
        self.made_in = made_in
        self.germination = germination


if __name__ == "__main__":
    apple = Product.create_product('Яблоко', 'Зеленое яблоко', 11.4, 150, 'зеленый')
    orange = Product.create_product("Апельсин", "Сочный апельсин", 14.6, 300, 'оранжевый')
    phone = Smartphone.create_product('phone 1', 'Описание', 178999.4, 50, 'black', 12.4, 'new', 128)
    print(phone)
