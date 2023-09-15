import pytest
import pathlib
from pathlib import Path
from src.item import Item


def test_create_item():
    item = Item("Example Item", 10.0, 5)
    assert item.name == "Example Item"
    assert item.price == 10.0
    assert item.quantity == 5


def test_calculate_total_price():
    item = Item("Item 1", 5.0, 10)  # Include the discount when creating items
    Item("Item 2", 8.0, 7)
    Item("Item 1", 5.0, 3)

    price = item.calculate_total_price()
    assert price == 50.0  # Corrected expected value


def test_apply_discount():

    item = Item("Discounted Item", 20.0, 3)
    Item.pay_rate = 0.8
    assert item.apply_discount() == 16.0  # Check if the discount is correctly applied


def test_total_cost():
    item = Item("Costly Item", 15.0, 6)
    cost = item.total_cost()
    assert cost == 90.0  # Corrected expected value


def test_zero_discount():
    item = Item("Zero Discount Item", 10.0, 5)
    cost = item.total_cost()
    assert cost == 50.0  # Check when discount is zero


def test_negative_quantity():

    with pytest.raises(ValueError):
        item = Item("Negative Discount Item", 10.0, -5)  # Check when discount is negative
        item.total_cost()


def test_quantity_zero():
    item = Item("Zero Quantity Item", 10.0, 0)
    cost = item.total_cost()
    assert cost == 0.0  # Check when quantity is zero


def test_negative_discount():
    item = Item("Negative Discount Item", 10.0, 5)
    cost = item.total_cost()
    assert cost == 50.0     # Check when discount is negative

def test_pay_rate():
    item = Item("Negative Discount Item", 10.0, 5)
    item.set_pay_rate(1.2)
    assert item.pay_rate == 1.2
    item.reset_pay_rate()
    assert item.pay_rate == 1.0

def test_set_name_within_limit():
    item = Item("Short Name", 10.0, 5)
    assert item.name == "Short Name"

    item.name = "New Name"
    assert item.name == "New Name"

def test_set_name_exceeds_limit():
    item = Item(name="Телефон", price=10000, quantity=5)
    assert item.name == "Телефон"
    item.name = "Планшет"
    assert item.name == "Планшет"
    item.name = "0987654321Long Name Exceeding Limit"
    assert item.name == "0987654321"
    assert len(item.name) == 10  # Проверяем, что имя состоит ровно из 10 символов

def test_instiate_from_csv():
    file_path = Path(pathlib.Path.cwd(),'src', 'items.csv')
    Item.instantiate_from_csv(file_path)  # создание объектов из данных файла
    assert len(Item.all) == 5
