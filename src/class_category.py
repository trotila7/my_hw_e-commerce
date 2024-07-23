from src.class_product import Product


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
        if isinstance(product, Product):
            self.__goods.append(product)

    def goods_info(self):
        for product in self.__goods:
            print(product)

    # @property
    # def view_product(self):
    #    """ Метод, который позволяет просмотреть товары в категории """
    #    list_goods = self.__goods
    #   return list_goods


if __name__ == "__main__":
    apple = Product.create_product('Яблоко', 'Зеленое яблоко', 11.4, 150)
    orange = Product.create_product("Апельсин", "Сочный апельсин", 14.6, 300)
    fruits = Category("Фрукты", "Свежие фрукты", [])
    fruits.add_product(apple)
    fruits.add_product(orange)
    print(fruits.goods_info())
