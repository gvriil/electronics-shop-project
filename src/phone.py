class Phone:
    def __init__(self, name, price, quantity, number_of_sim):
        """
        Создает экземпляр класса Phone.

        :param name: Название смартфона.
        :param price: Цена смартфона.
        :param quantity: Количество смартфонов в наличии.
        :param number_of_sim: Количество поддерживаемых сим-карт.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.number_of_sim = number_of_sim

    def __add__(self, other):
        """
        Переопределение оператора сложения (+) для объектов Phone и Item.

        :param other: Другой объект (Phone или Item).
        :return: Сумма количества товаров из self и other.
        :raise TypeError: Если other не является объектом типа Phone или Item.
        """
        from src.item import Item  # Импортируем Item для проверки типа
        if isinstance(other, (Item, Phone)):
            return self.quantity + other.quantity
        else:
            raise TypeError('Нельзя сложить объект этого типа с объектом другого типа')

    def __str__(self):
        """
        Возвращает строковое представление объекта Phone (название смартфона).

        :return: Название смартфона.
        """
        return self.name

    def __repr__(self):
        """
        Возвращает строковое представление объекта Phone для отладки и представления.

        :return: Строковое представление объекта Phone.
        """
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
