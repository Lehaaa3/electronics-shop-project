from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    def __add__(self, other):
        if issubclass(self.__class__, Item):
            return self.quantity + other.quantity
        raise Exception("Недопустимый класс для сложения")

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim):
        if new_number_of_sim < 1:
            raise ValueError("Кол-во сим-карт должно быть больше 0")
        if type(new_number_of_sim) is not int:
            raise ValueError("Кол-во сим-карт должно быть числом")
        self.__number_of_sim = new_number_of_sim
        return self.__number_of_sim
