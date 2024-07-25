import pytest
from src.class_category import Category
from src.class_product import Smartphone, LawnGrass


@pytest.fixture()
def category_fruit():
    return Category('fruit', 'Свежие фрукты', ['apple', 'apple', 'orange'])


def test_init(category_fruit):
    assert category_fruit.name == 'fruit'
    assert category_fruit.description == 'Свежие фрукты'
    assert category_fruit.goods == ['apple', 'apple', 'orange']
    assert category_fruit.number_of_category == 1
    assert category_fruit.unique_products == {'apple', 'orange'}
    assert category_fruit.number_of_unique_products == 2


@pytest.fixture()
def category_no_sugar():
    return Category('no_sugar', 'Продукты, которые не содержат сахар', [])


def test_init_2(category_no_sugar):
    assert category_no_sugar.name == 'no_sugar'
    assert category_no_sugar.description == 'Продукты, которые не содержат сахар'
    assert category_no_sugar.number_of_category == 2
    assert category_no_sugar.unique_products == {'apple', 'orange'}
    assert category_no_sugar.number_of_unique_products == 2


@pytest.fixture
def product_1():
    return Smartphone.create_product('Яблоко', 'Зеленое яблоко', 11.4, 150, 'зеленый', 11, "fdf", 128)


@pytest.fixture
def product_2():
    return LawnGrass.create_product("Трава", "Зеленая", 14.6, 300, 'зеленая', "Russia", 50)


def test_goods_info(category_no_sugar, product_1):
    category_no_sugar.add_product(product_1)
    result = category_no_sugar.goods_info
    assert result == "Яблоко (Модель: fdf, Производительность: 11), 11.4 руб. Остаток: 150 шт."


def test_add_product(category_no_sugar, product_1, product_2):
    category_no_sugar.add_product(product_1)
    category_no_sugar.add_product(product_2)
    print(dir(category_no_sugar))
    assert len(category_no_sugar._Category__goods) == 2  # не знаю как тут использовать артибут goods


@pytest.fixture()
def len_goods(product_1, product_2):
    return 450


def test_len(len_goods, category_no_sugar, product_1, product_2):
    category_no_sugar.add_product(product_1)
    category_no_sugar.add_product(product_2)
    assert len(category_no_sugar) == len_goods


@pytest.fixture()
def str_category(category_no_sugar):
    return 'no_sugar, количество продуктов: 450 шт.'


def test_str(str_category, category_no_sugar, product_1, product_2):
    category_no_sugar.add_product(product_1)
    category_no_sugar.add_product(product_2)
    assert str(category_no_sugar) == str_category
