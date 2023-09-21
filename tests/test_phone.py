import pytest
from src.phone import Phone
from src.item import Item

# Фикстура для создания экземпляра Phone
@pytest.fixture
def phone_instance():
    """
    Фикстура для создания экземпляра Phone.

    Returns:
        Phone: Экземпляр Phone.
    """
    return Phone("iPhone 14", 120_000, 5, 2)

# Фикстура для создания экземпляра Item
@pytest.fixture
def item_instance():
    """
    Фикстура для создания экземпляра Item.

    Returns:
        Item: Экземпляр Item.
    """
    return Item("Смартфон", 10000, 20)

@pytest.fixture
def other_object():
    """
    Фикстура для создания другого объекта или значения.

    Returns:
        any: Объект или значение.
    """
    # Здесь определяйте ваш объект или значение
    return "some_value"

# Тест для проверки атрибутов Phone
def test_phone_attributes(phone_instance):
    """
    Тестирование атрибутов экземпляра Phone.

    Args:
        phone_instance (Phone): Экземпляр Phone.
    """
    assert phone_instance.name == "iPhone 14"
    assert phone_instance.price == 120_000
    assert phone_instance.quantity == 5
    assert phone_instance.number_of_sim == 2

# Тест для проверки сложения Item и Phone
def test_item_phone_addition(item_instance, phone_instance):
    """
    Тестирование операции сложения экземпляров Item и Phone.

    Args:
        item_instance (Item): Экземпляр Item.
        phone_instance (Phone): Экземпляр Phone.
    """
    result = item_instance + phone_instance
    assert result == 25  # Сумма количества товаров из item_instance и phone_instance

    # Проверяем, что item_instance и phone_instance не изменились после сложения
    assert item_instance.quantity == 20
    assert phone_instance.quantity == 5

# Тест для проверки сложения двух экземпляров Phone
def test_phone_phone_addition(phone_instance):
    """
    Тестирование операции сложения двух экземпляров Phone.

    Args:
        phone_instance (Phone): Экземпляр Phone.
    """
    phone_instance_2 = Phone("iPhone 15", 150_000, 3, 1)
    result = phone_instance + phone_instance_2
    assert result == 8  # Сумма количества товаров из phone_instance и phone_instance_2

    # Проверяем, что phone_instance и phone_instance_2 не изменились после сложения
    assert phone_instance.quantity == 5
    assert phone_instance_2.quantity == 3

# Тест для проверки операции сложения экземпляра Phone с объектом другого типа
def test_phone_addition_with_other_type_should_raise_error(phone_instance, other_object):
    """
    Тестирование операции сложения экземпляра Phone с объектом другого типа.

    Args:
        phone_instance (Phone): Экземпляр Phone.
        other_object (any): Другой объект или значение.
    """
    try:
        phone_instance + other_object
    except TypeError as e:
        assert str(e) == 'Нельзя сложить объект этого типа с объектом другого типа'

# Тест для проверки метода str класса Phone
def test_phone_str_representation(phone_instance):
    """
    Тестирование метода str класса Phone.

    Args:
        phone_instance (Phone): Экземпляр Phone.
    """
    assert str(phone_instance) == 'iPhone 14'

# Тест для проверки метода repr класса Phone
def test_phone_repr_representation(phone_instance):
    """
    Тестирование метода repr класса Phone.

    Args:
        phone_instance (Phone): Экземпляр Phone.
    """
    assert repr(phone_instance) == "Phone('iPhone 14', 120000, 5, 2)"
