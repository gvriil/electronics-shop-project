from src.item import Item  # Импортируем базовый класс Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        """
        Создает экземпляр класса Phone.

        :param name: Название смартфона.
        :param price: Цена смартфона.
        :param quantity: Количество смартфонов в наличии.
        :param number_of_sim: Количество поддерживаемых сим-карт.
        """
        super().__init__(name, price, quantity)  # Вызываем конструктор базового класса
        self.number_of_sim = number_of_sim  # Добавляем новый атрибут

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

    @property
    def number_of_sim(self):
        """
        Геттер для количества сим-карт.

        Returns:
            int: Количество сим-карт.
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """
        Сеттер для количества сим-карт. Проверяет, что количество сим-карт не отрицательное.

        Args:
            value (int): Новое количество сим-карт.

        Raises:
            ValueError: Если количество сим-карт отрицательное.
        """
        if value < 0:
            raise ValueError("Количество сим-карт не может быть отрицательным")
        self.__number_of_sim = value
