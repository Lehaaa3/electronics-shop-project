import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        with open(r'C:\Users\Lenovo\projects 2023\electronics-shop-project\src\items.csv') as f:
            info = csv.DictReader(f)
            for row in info:
                Item(row['name'], row['price'], row['quantity'])

    @property
    def change_name(self):
        pass

    @change_name.setter
    def change_name(self, new_name):
        if len(new_name) > 10:
            self.name = new_name[:9]
        else:
            self.name = new_name

    @staticmethod
    def string_to_number(string_number):
        number = int(float(string_number))
        return number

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate


