from .house import House

class SmallHouse(House):
    def __init__(self, name, price):
        super().__init__(name, price, area=40)


