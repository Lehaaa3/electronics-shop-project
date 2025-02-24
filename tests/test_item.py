"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item
from src.phone import Phone
from src.item import InstantiateCSVError

@pytest.fixture
def item1():
    item1 = Item("apple", 10.0, 5)
    return item1


def test_instantiate_from_csv():
    """Создаем экземпляры класса Item из csv файла. Проверяем количество созданных экземпляров"""
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    #перед следующим тестом изменяем название файла items.csv
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()
    #перед следующим тестом удаляем любое из значений в колонках файла items.csv
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()


def test_item_calculate_total_price():
    """Создаем класс продукта с его стоимостью и количеством, с помощью функции получаем общую стоимость"""
    item1 = Item("apple", 10.0, 5)
    assert item1.calculate_total_price() == 50


def test_apply_discount():
    """Применяем скидку к стоимости товара, получаем новое значение цены"""
    item2 = Item("orange", 15.0, 10)
    assert item2.price == 15.0
    Item.pay_rate = 0.5
    item2.apply_discount()
    assert item2.price == 7.5


def test_string_to_number():
    """Проверяем правильность перевода str в int"""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_item_repr():
    """Проверяем работу магического метода repr класса Item"""
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_item_str():
    """Проверяем работу магического метода str класса Item"""
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_item_add():
    """Проверяем работу магического метода add класса Item"""
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert item1 + item1 == 40
