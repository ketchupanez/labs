class Human:
    def __init__(self, money):
        self._money = money
        self.current_house = None


    def buy_house(self, house, discount):
        final_price = house.final_price(discount)
        if self._money >= final_price:
            print("Ожидайте завершения сделки...")
            self._money -= final_price
            return final_price
        else:
            print("На счету недостаточно средств. Пополните баланс")
            return None

    def make_deal(self, house):
        final_price = self.buy_house(house, discount=5)
        if final_price is not None:
            self.current_house = house
            print(f"Сделка завершена! {self.current_house._area} м^2 дом куплен за {final_price}$.")
            print(f"На вашем счету осталось {self._money}$")



