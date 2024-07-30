from src.class_product import Product, Smartphone, LawnGrass


class Category:
    """ Класс для определения категории товаров"""
    name: str
    description: str
    __goods: list

    number_of_category = 0
    unique_products = set()
    number_of_unique_products = 0

    def __init__(self, name, description, __goods):
        self.name = name
        self.description = description
        self.__goods = list(__goods)

        Category.number_of_category += 1
        Category.unique_products.update(self.__goods)
        Category.number_of_unique_products = len(list(Category.unique_products))

    @property
    def goods(self):
        return self.__goods

    def add_product(self, product):
        """ Метод, который позволяет добавить новый товар в список товаров """
        if not isinstance(product, Product):
            raise TypeError("Можно добавить только объекты типа Product.")
        if product.quantity_in_stock <= 0:
            raise ValueError("Товар с нулевым или отрицательным количеством не может быть добавлен.")
        self.__goods.append(product)

    def __len__(self):
        return sum(product.quantity_in_stock for product in self.__goods)  # считаем кол-во продуктов в категории

    def __str__(self):
        total_quantity_in_stock = len(self)
        return f'{self.name}, количество продуктов: {total_quantity_in_stock} шт.'

    @property
    def goods_info(self):
        result = [str(product) for product in self.__goods]
        return '\n'.join(result)

    def average_price(self):
        """ Метод, который подсчитывает средний ценник всех товаров """
        try:
            total_price = sum(good.price * good.quantity_in_stock for good in self.__goods)
            total_quantity = sum(good.quantity_in_stock for good in self.__goods)

            if total_quantity == 0:
                raise ZeroDivisionError("В категории нет товаров")
            avg_price = round(total_price / total_quantity, 2)
        except ZeroDivisionError:
            avg_price = 0
        return f"Средний ценник всех товаров {avg_price} руб."


if __name__ == "__main__":
    apple = Smartphone.create_product('Яблоко', 'Зеленое яблоко', 11.4, 150, 'зеленый', 11, "fdf", 128)
    orange = LawnGrass.create_product("Трава", "Зеленая", 14.6, 300, 'зеленая', "Russia", 50)
    all_goods = Category("Товары", "Все товары", [])
    all_goods.add_product(apple)
    all_goods.add_product(orange)
    print(Category.average_price(all_goods))
