class Item:
    # Статический список для хранения всех созданных экземпляров класса
    all = []

    # Коэффициент оплаты
    pay_rate = 1.0

    def __init__(self, name, price, quantity):
        # Инициализация атрибутов объекта
        self.name = name  # Название товара
        self.price = price  # Цена за единицу товара
        self.quantity = quantity  # Количество товара в магазине

        # Добавляем текущий экземпляр в статический список instances
        self.__class__.all.append(self)


    def calculate_total_price(self):
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :param name: Название товара для подсчета
        :return: Общая стоимость товара
        """

        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.

        :param discount: Уровень скидки (например, 0.15 для 15% скидки)
        """
        return self.price * self.pay_rate

    def total_cost(self):
        """
        Рассчитывает общую стоимость товара с учетом скидки.

        :return: Общая стоимость товара
        """
        if self.quantity < 0:
            raise ValueError("Количество товара не может быть отрицательным")

        return self.price * self.quantity

    @classmethod
    def set_pay_rate(cls, rate):
        """
        Устанавливает коэффициент оплаты для всех товаров.

        :param rate: Новый коэффициент оплаты
        """
        cls.pay_rate = rate

    @classmethod
    def reset_pay_rate(cls):
        """
        Сбрасывает коэффициент оплаты в 1.0 (без скидки).
        """
        cls.pay_rate = 1.0
