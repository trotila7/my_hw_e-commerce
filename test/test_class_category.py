import pytest
from src.class_category import Category


@pytest.fixture()
def category_fruit():
    return Category('fruit', 'Свежие фрукты', ['apple', 'apple', 'orange'])


def test_init(category_fruit):
    assert category_fruit.name == 'fruit'
    assert category_fruit.description == 'Свежие фрукты'
    assert category_fruit.goods == ['apple', 'apple', 'orange']
