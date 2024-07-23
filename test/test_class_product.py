import pytest
from src.class_product import Product


@pytest.fixture()
def product_milk():
    return Product('milk', 'Коровье молоко, жирность 3,2%', 87.67, 178787)


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



