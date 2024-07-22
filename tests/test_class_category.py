import pytest
from src.class_category import Category


@pytest.fixture()
def category_fruit():
    return Category('fruit', 'Свежие фрукты', ['apple', 'apple', 'orange'])
