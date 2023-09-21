import pytest

from src.item import Item
from src.phone import Phone


# Тест создания экземпляра товара (Item)
def test_create_item():
    """
    Тестирование создания экземпляра товара (Item).
    Убеждаемся, что атрибуты экземпляра корректно инициализируются.
    """
    item = Item("Example Item", 10.0, 5)
    assert item.name == "Example Item"
    assert item.price == 10.0
    assert item.quantity == 5


# Тестирование метода calculate_total_price() класса Item
def test_calculate_total_price():
    """
    Тестирование метода calculate_total_price() класса Item.
    Убеждаемся, что метод правильно вычисляет общую стоимость товара.
    """
    item = Item("Item 1", 5.0, 10)  # Включаем скидку при создании товара
    Item("Item 2", 8.0, 7)
    Item("Item 1", 5.0, 3)

    price = item.calculate_total_price()
    assert price == 50.0  # Правильное ожидаемое значение


# Тестирование метода apply_discount() класса Item
def test_apply_discount():
    """
    Тестирование метода apply_discount() класса Item.
    Убеждаемся, что метод правильно применяет скидку к товару.
    """
    item = Item("Discounted Item", 20.0, 3)
    Item.pay_rate = 0.8
    assert item.apply_discount() == 16.0  # Проверяем, что скидка корректно применена


# Тестирование метода total_cost() класса Item
def test_total_cost():
    """
    Тестирование метода total_cost() класса Item.
    Убеждаемся, что метод правильно вычисляет общую стоимость товара.
    """
    item = Item("Costly Item", 15.0, 6)
    cost = item.total_cost()
    assert cost == 90.0  # Правильное ожидаемое значение


# Тестирование метода total_cost() класса Item, когда скидка равна нулю
def test_zero_discount():
    """
    Тестирование метода total_cost() класса Item, когда скидка равна нулю.
    """
    item = Item("Zero Discount Item", 10.0, 5)
    cost = item.total_cost()
    assert cost == 50.0  # Проверяем, что скидка равна нулю


# Тестирование метода total_cost() класса Item, когда количество товара отрицательно
def test_negative_quantity():
    """
    Тестирование метода total_cost() класса Item, когда количество товара отрицательно.
    Ожидаем поднятие исключения ValueError.
    """
    with pytest.raises(ValueError):
        item = Item("Negative Discount Item", 10.0, -5)
        item.total_cost()


# Тестирование метода total_cost() класса Item, когда количество товара равно нулю
def test_quantity_zero():
    """
    Тестирование метода total_cost() класса Item, когда количество товара равно нулю.
    """
    item = Item("Zero Quantity Item", 10.0, 0)
    cost = item.total_cost()
    assert cost == 0.0  # Проверяем, что стоимость равна нулю


# Тестирование метода total_cost() класса Item, когда скидка отрицательна
def test_negative_discount():
    """
    Тестирование метода total_cost() класса Item, когда скидка отрицательна.
    """
    item = Item("Negative Discount Item", 10.0, 5)
    cost = item.total_cost()
    assert cost == 50.0  # Проверяем, что скидка отрицательна


# Тестирование методов set_pay_rate() и reset_pay_rate() класса Item
def test_pay_rate():
    """
    Тестирование методов set_pay_rate() и reset_pay_rate() класса Item.
    Убеждаемся, что ставка оплаты корректно устанавливается и сбрасывается.
    """
    item = Item("Negative Discount Item", 10.0, 5)
    item.set_pay_rate(1.2)
    assert item.pay_rate == 1.2  # Проверяем, что ставка установлена корректно
    item.reset_pay_rate()
    assert item.pay_rate == 1.0  # Проверяем, что ставка сброшена к значению по умолчанию


# Тестирование установки имени товара в пределах лимита (не более 10 символов)
def test_set_name_within_limit():
    """
    Тестирование установки имени товара в пределах лимита (не более 10 символов).
    """
    item = Item("Short Name", 10.0, 5)
    assert item.name == "Short Name"  # Проверяем, что имя установлено корректно

    item.name = "New Name"
    assert item.name == "New Name"  # Проверяем, что новое имя установлено корректно


# Тестирование установки имени товара, превышающего лимит (более 10 символов)
def test_set_name_exceeds_limit():
    """
    Тестирование установки имени товара, превышающего лимит (более 10 символов).
    """
    item = Item(name="Телефон", price=10000, quantity=5)
    assert item.name == "Телефон"  # Проверяем, что имя установлено корректно
    item.name = "Планшет"
    assert item.name == "Планшет"  # Проверяем, что новое имя установлено корректно
    item.name = "0987654321Long Name Exceeding Limit"
    assert item.name == "0987654321"  # Проверяем, что имя обрезано до 10 символов
    assert len(item.name) == 10  # Проверяем, что имя состоит ровно из 10 символов


# Тестирование метода instantiate_from_csv() класса Item
def test_instiate_from_csv():
    """
    Тестирование метода instantiate_from_csv() класса Item.
    Убеждаемся, что объекты корректно создаются из данных файла CSV.
    """

    file_path = 'tests/test_data.csv'

    Item.instantiate_from_csv(file_path)
    assert len(Item.all) == 5  # Проверяем, что создано 5 объектов
    file_path = 'tests/not_found.csv'
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(file_path)


# Проверяет, что метод __repr__ класса Item возвращает ожидаемую строку
def test_item_repr():
    """
    Проверяет, что метод __repr__ класса Item возвращает ожидаемую строку.
    """
    item = Item("Телефон", 10000, 5)
    assert repr(item) == "Item('Телефон', 10000, 5)"


# Проверяет, что метод __str__ класса Item возвращает ожидаемое имя товара
def test_item_str():
    """
    Проверяет, что метод __str__ класса Item возвращает ожидаемое имя товара.
    """
    item = Item("Смартфон", 15000, 10)
    assert str(item) == "Смартфон"


# Тестирование метода instantiate_from_csv класса Item на обработку поврежденного CSV-файла
def test_instantiate_from_corrupted_csv():
    """
    Тестирование метода instantiate_from_csv класса Item на обработку поврежденного CSV-файла.
    """

    # Путь к поврежденному CSV-файлу (например, уберите одну из колонок или строки)
    file_name = 'tests/test_damaged_data.csv'

    # Попробуйте обработать поврежденный файл с помощью метода instantiate_from_csv.
    # Ожидается, что при обработке поврежденного файла возникнет исключение (любого типа).
    with pytest.raises(Exception):
        Item.instantiate_from_csv(file_name)


# Тест для проверки атрибутов Phone
def test_items_attributes(item_instance):
    assert item_instance.name == 'Смартфон'
    assert item_instance.price == 20000
    assert item_instance.quantity == 20


# Тест для проверки сложения Item и Phone
def test_item_phone_addition(item_instance, phone_instance):
    result = item_instance + phone_instance
    assert result == 25  # Сумма количества товаров из item_instance и phone_instance

    # Проверяем, что item_instance и phone_instance не изменились после сложения
    assert item_instance.quantity == 20
    assert phone_instance.quantity == 5


# Тест для проверки сложения двух экземпляров Item
def test_item_addition(item_instance):
    item_instance_2 = Item("Другой Смартфон", 10000, 10)
    result = item_instance + item_instance_2
    assert result == 30  # Сумма количества товаров item_instance и item_instance_2

    # Проверяем, что item_instance и item_instance_2 не изменились после сложения
    assert item_instance.quantity == 20
    assert item_instance_2.quantity == 10


# Тест для проверки сложения экземпляра Item с объектом другого типа
def test_item_addition_with_other_type_should_raise_error(item_instance, other_object):
    try:
        item_instance + other_object
    except TypeError as e:
        assert str(e) == 'Нельзя сложить объект этого типа с объектом другого типа'
