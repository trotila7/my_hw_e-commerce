from abc import ABC, abstractmethod


class MixinLog:
    def __repr__(self):
        class_name = self.__class__.__name__
        params = [f"{key}='{value}'" for key, value in self.__dict__.items()]
        return f"Создан объект класса {class_name}, с параметрами: {', '.join(params)}"


class Product(ABC, MixinLog):
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
        print(self.__repr__())

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        if isinstance(other, self.__class__):
            total_value_self = self.price * self.quantity_in_stock
            total_value_other = other.price * other.quantity_in_stock
            return total_value_self + total_value_other
        raise TypeError

    @classmethod
    @abstractmethod
    def create_product(cls, *args):
        pass

    @property
    def new_price(self):
        return self.price

    @new_price.setter
    def new_price(self, new_value):
        if new_value > 0:
            self.price = new_value
        else:
            print("Цена введена некорректная. Цена должна быть больше нуля.")

    @new_price.deleter
    def new_price(self) -> None:
        print(f"Цена товара '{self.name}' удалена")
        self.price = 0


class Smartphone(Product):
    performance: float
    model: str
    internal_memory: int

    def __init__(self, name, description, price, quantity_in_stock, color, performance, model, internal_memory):
        super().__init__(name, description, price, quantity_in_stock, color)
        self.performance = performance
        self.model = model
        self.internal_memory = internal_memory

    def __str__(self):
        return (f"{self.name} (Модель: {self.model}, Производительность: {self.performance}), {self.price} руб. "
                f"Остаток: {self.quantity_in_stock} шт.")

    def __add__(self, other):
        return super().__add__(other)

    @classmethod
    def create_product(cls, name, description, price, quantity_in_stock, color, performance, model,
                       internal_memory):
        if cls == Smartphone:
            """Метод, который создает товар и возвращает объект, который можно добавлять в список товаров"""
            return cls(name, description, price, quantity_in_stock, color, performance, model, internal_memory)
        return "Объект не создан"


class LawnGrass(Product):
    made_in: str
    germination: float

    def __init__(self, name, description, price, quantity_in_stock, color, made_in, germination):
        super().__init__(name, description, price, quantity_in_stock, color)
        self.made_in = made_in
        self.germination = germination

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity_in_stock} шт."

    def __add__(self, other):
        return super().__add__(other)

    @classmethod
    def create_product(cls, name, description, price, quantity_in_stock, color, made_in, germination):
        if cls == LawnGrass:
            """Метод, который создает товар и возвращает объект, который можно добавлять в список товаров"""
            return cls(name, description, price, quantity_in_stock, color, made_in, germination)
        return "Объект не создан"


if __name__ == "__main__":
    phone = Smartphone.create_product("phone 1", "Описание", 178999.4, 50, "black", 12.4, "new", 128)
    ordinary_grass = LawnGrass.create_product("Обычная трава", "Зеленая трава", 500, 1, "green", "Russia", 2)
    print(phone)
    print(ordinary_grass)
