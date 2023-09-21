import pytest
from src.item import Item
from src.phone import Phone


# Фикстура для создания экземпляра Phone
@pytest.fixture
def phone_instance():
    """
    Создает экземпляр класса Phone для тестирования.

    Returns:
        Phone: Экземпляр класса Phone с заданными параметрами.
    """
    return Phone("iPhone 14", 120_000, 5, 2)


# Фикстура для создания экземпляра Item
@pytest.fixture
def item_instance():
    """
    Создает экземпляр класса Item для тестирования.

    Returns:
        Item: Экземпляр класса Item с заданными параметрами.
    """
    return Item("Смартфон", 10_000, 20)


# Фикстура для создания другого экземпляра Item
@pytest.fixture
def item_instance_2():
    """
    Создает второй экземпляр класса Item для тестирования.

    Returns:
        Item: Второй экземпляр класса Item с заданными параметрами.
    """
    return Item("Другой Смартфон", 150_000, 3)


# Фикстура для создания объекта другого типа
@pytest.fixture
def other_object():
    """
    Создает объект другого типа для тестирования.

    Returns:
        str: Объект другого типа (строка) для использования в тестах.
    """
    return "some_value"
