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
