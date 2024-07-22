import pytest
from src.class_category import Category


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
    assert category_no_sugar.goods == list([])
    assert category_no_sugar.number_of_category == 2
    assert category_no_sugar.unique_products == {'apple', 'orange'}
    assert category_no_sugar.number_of_unique_products == 2
