import csv
import os


class Item:
    all = []  # Список для хранения всех экземпляров класса Item
    pay_rate = 1.0  # Ставка оплаты по умолчанию

    def __init__(self, name, price, quantity):
        super().__init__()
        """
        Конструктор класса Item.

        Args:
            name (str): Наименование товара.
            price (float): Цена товара.
            quantity (int): Количество товара в наличии.

        """
        self.__name = name  # Приватный атрибут с наименованием товара
        self.price = price  # Атрибут с ценой товара
        self.quantity = quantity  # Атрибут с количеством товара в наличии
        self.__class__.all.append(
            self)  # Добавление текущего экземпляра в список всех экземпляров класса

    def __add__(self, other):
        from src.phone import Phone
        if isinstance(other, (Item, Phone)):
            return self.quantity + other.quantity
        else:
            raise TypeError('Нельзя сложить объект этого типа с объектом другого типа')

    def __repr__(self):
        """
        Магический метод __repr__, который возвращает строковое представление объекта.
        """
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Магический метод __str__, который возвращает строковое представление объекта при вызове str().
        В данной реализации, это просто имя товара.
        """
        return self.name

    @property
    def name(self):
        """
        Геттер для наименования товара.

        Returns:
            str: Наименование товара.

        """
        return self.__name

    @name.setter
    def name(self, new_name):
        """
        Сеттер для наименования товара. Обрезает наименование до 10 символов.

        Args:
            new_name (str): Новое наименование товара.

        """
        self.__name = new_name[:10]

    def calculate_total_price(self):
        """
        Вычисляет общую стоимость товара.

        Returns:
            float: Общая стоимость товара.

        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Вычисляет стоимость товара с учетом скидки.

        Returns:
            float: Стоимость товара со скидкой.

        """
        return self.price * self.pay_rate

    def total_cost(self):
        """
        Вычисляет общую стоимость всех единиц товара в наличии.

        Raises:
            ValueError: Если количество товара отрицательно.

        Returns:
            float: Общая стоимость товара в наличии.

        """
        if self.quantity < 0:
            raise ValueError("Количество товара не может быть отрицательным")
        return self.price * self.quantity

    @classmethod
    def set_pay_rate(cls, rate):
        """
        Устанавливает ставку оплаты для всех экземпляров класса.

        Args:
            rate (float): Новая ставка оплаты.

        """
        cls.pay_rate = rate

    @classmethod
    def reset_pay_rate(cls):
        """
        Сбрасывает ставку оплаты к значению по умолчанию (1.0).

        """
        cls.pay_rate = 1.0

    @classmethod
    def instantiate_from_csv(cls, file_name='src/items.csv'):
        try:
            # Получить абсолютный путь к файлу на основе текущей директории и относительного пути
            file_path = os.path.join(os.path.split(os.path.dirname(__file__))[0],
                                     *os.path.split(file_name))
            print(file_path)
            with open(file_path, newline='', encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                cls.all.clear()
                # Проверка наличия необходимых столбцов в CSV-файле
                required_columns = {'name', 'price', 'quantity'}
                if not required_columns.issubset(reader.fieldnames):
                    raise InstantiateCSVError(
                        "Файл item.csv поврежден: отсутствуют необходимые столбцы")
                for row in reader:
                    name = row['name']
                    price = cls.string_to_number(row['price'])
                    quantity = int(row['quantity'])
                    cls(name, price, quantity)
        except FileNotFoundError as e:
            raise FileNotFoundError("Отсутствует файл item.csv") from e
        except InstantiateCSVError as e:
            raise e


    @staticmethod
    def string_to_number(string):
        """
        Преобразует строку, представляющую число, в численное значение.

        Args:
            string (str): Строка, представляющая число.

        Returns:
            int: Численное значение.

        """
        return int(float(string))

class InstantiateCSVError(Exception):
    def __init__(self, message="Файл item.csv поврежден"):
        self.message = message
        super().__init__(self.message)