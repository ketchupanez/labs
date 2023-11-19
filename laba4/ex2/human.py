class Human:
    def __init__(self, money):
        self._money = money
        self.current_house = None


    def buy_house(self, house, discount):
        if self._money >= house._price:
            _price = house.final_price(discount)
            print("Ожидайте завершения сделки...")
            return True
        else:
            print("На счету недостаточно средств. Пополните баланс")
            return False

    def make_deal(self, house, _price):
        if self.buy_house(house, 5):
            self._money = self._money - _price
            self.current_house = house
            print(f"Сделка завершена! {self.current_house._area} м^2 дом куплен за {_price}$.")
            print(f"На вашем счету осталось {self._money}$")



