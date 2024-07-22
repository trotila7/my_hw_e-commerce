class Category:
    """ Класс для определения категории товаров"""
    name: str
    description: str
    goods: list

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods
