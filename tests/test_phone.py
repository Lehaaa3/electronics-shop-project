from src.item import Item
from src.phone import Phone

def test_item_add():
    """Проверяем работу магического метода add класса Phone"""
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10