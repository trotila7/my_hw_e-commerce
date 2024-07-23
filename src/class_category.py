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

    def new_goods(self, new_product):
        """ Метод, который позволяет добавить новые товары в список товаров категории """
        list_new_product = new_product.split(" ")
        return self.__goods.extend(list_new_product)

    def view_product(self):
        """ Метод, который позволяет просмотреть товары в категории """
        list_goods = self.__goods
        return list_goods


fruits_1 = Category('fruit', 'Свежие фрукты', ['apple', 'apple', 'orange'])
new_product = "peach banana"

if __name__ == "__main__":
    # print(Category.number_of_category)
    # print(Category.number_of_unique_products)
    print(fruits_1.view_product())
    fruits_1.new_goods(new_product)
    print(fruits_1.view_product())
