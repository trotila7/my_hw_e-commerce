class Category:
    """ Класс для определения категории товаров"""
    name: str
    description: str
    goods: list

    number_of_category = 0
    unique_products = set()
    number_of_unique_products = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods

        Category.number_of_category += 1
        Category.unique_products.update(self.goods)
        Category.number_of_unique_products = len(list(Category.unique_products))


#fruits_1 = Category('fruit', 'Свежие фрукты', ['apple', 'apple', 'orange'])

if __name__ == "__main__":
    print(Category.number_of_category)
    print(Category.number_of_unique_products)
