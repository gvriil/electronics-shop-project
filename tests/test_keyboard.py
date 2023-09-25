from src.keyboard import MixinKeyboard, Keyboard  # Замените "your_module" на путь к вашему модулю


# Тесты для MixinKeyboard
def test_mixin_keyboard_init():
    """
    Проверяет, что инициализация MixinKeyboard устанавливает атрибут language в "EN".
    """
    keyboard = MixinKeyboard()
    assert keyboard.language == "EN"


def test_mixin_keyboard_change_lang():
    """
    Проверяет, что метод change_lang изменяет язык с "EN" на "RU" и обратно.
    """
    keyboard = MixinKeyboard()
    assert keyboard.change_lang() == "RU"
    assert keyboard.change_lang() == "EN"


# Тесты для Keyboard
def test_keyboard_init():
    """
    Проверяет, что инициализация Keyboard устанавливает атрибуты name, price и quantity.
    """
    keyboard = Keyboard('Dark Project KD87A', 9600, 5)
    assert keyboard.name == 'Dark Project KD87A'
    assert keyboard.price == 9600
    assert keyboard.quantity == 5
    assert keyboard.language == "EN"


def test_keyboard_change_lang():
    """
    Проверяет, что метод change_lang изменяет язык для объекта Keyboard с "EN" на "RU" и обратно.
    """
    keyboard = Keyboard('Dark Project KD87A', 9600, 5)
    assert keyboard.change_lang() == "RU"
    assert keyboard.language == "RU"
    assert keyboard.change_lang() == "EN"
    assert keyboard.language == "EN"


def test_keyboard_str():
    """
    Проверяет, что метод str возвращает правильное имя для объекта Keyboard.
    """
    keyboard = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(keyboard) == 'Dark Project KD87A'

# Запустите тесты с помощью pytest
