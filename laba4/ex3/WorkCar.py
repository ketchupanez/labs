from .Car import Car
class WorkCar(Car):
    def show_speed(self):
        print(f"Машина {self.name} едет со скоростью {self.speed}")

        if self.speed > 40:
            print("Внимание! Скорость превышает 40 км/ч, Вам необходимо снизить ее!")