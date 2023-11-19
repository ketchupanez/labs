class House:
    def __init__(self, name, price, area):
     self._name = name
     self._price = price
     self._area = area

    def print_info(self):
     print(f"Название дома: {self._name}")
     print(f"Цена дома: {self._price}$")
     print(f"Площадь дома: {self._area} м^2\n")


    def final_price(self, discount):
        self._price = self._price * (100 - discount) / 100
        return self._price




