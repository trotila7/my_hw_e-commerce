import pytest
from src.class_product import Product


@pytest.fixture()
def product_milk():
    return Product('milk', 'Коровье молоко, жирность 3,2%', 87.67, 178787)


@pytest.fixture()
def product_no_milk():
    return Product('nomilk', 'Не Коровье молоко, жирность 3,2%', 157.1, 45)


@pytest.fixture()
def add_product():
    result = (87.67 * 178787) + (157.1 * 45)
    return result


def test_init(product_milk):
    assert product_milk.name == 'milk'
    assert product_milk.description == 'Коровье молоко, жирность 3,2%'
    assert product_milk.price == 87.67
    assert product_milk.quantity_in_stock == 178787


@pytest.fixture()
def product_apple():
    return Product("Яблоко", "Зеленое", 120, 5)


def test_product_price_getter(product_milk):
    assert product_milk.price == 87.67


def test_product_price_setter_correct(product_milk):
    product_milk.price = 100
    assert product_milk.price == 100


def test_product_price_setter_incorrect(product_milk):
    product_milk.price = -50
    assert product_milk.price == 87.67  # Цена не должна измениться


@pytest.fixture()
def str_product():
    return "milk, 87.67 руб. Остаток: 178787 шт."


def test_str_milk(product_milk, str_product):
    assert str(product_milk) == str_product


def test_add_product(add_product, product_milk, product_no_milk):
    assert (product_milk + product_no_milk) == add_product
