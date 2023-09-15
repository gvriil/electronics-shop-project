import os
import csv

class Item:
    all = []
    pay_rate = 1.0

    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.__class__.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name[:10]

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        return self.price * self.pay_rate

    def total_cost(self):
        if self.quantity < 0:
            raise ValueError("Количество товара не может быть отрицательным")
        return self.price * self.quantity

    @classmethod
    def set_pay_rate(cls, rate):
        cls.pay_rate = rate

    @classmethod
    def reset_pay_rate(cls):
        cls.pay_rate = 1.0

    @classmethod
    def instantiate_from_csv(cls, file_name):
        file_path = "../src/items.csv"
       # file_path = os.path.join(os.path.dirname(__file__), os.path.split(file_name)[-1])
        with open(file_path, newline='', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            cls.all.clear()
            for row in reader:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = int(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(string):
        return int(float(string))
