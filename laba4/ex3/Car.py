class Car:
    def __init__(self, name, color, speed, is_police):
        self.name = str(name)
        self.color = str(color)
        self.speed = speed
        self.is_police = bool(is_police)

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction="право"): #направление в котором едет машина
        print(f"Машина {self.name} повернула на {direction}")

    def show_speed(self):
        print(f"Машина {self.name} едет со скоростью {self.speed}")





