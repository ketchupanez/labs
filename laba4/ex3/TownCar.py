from .Car import Car
class TownCar(Car):
  def show_speed(self):
   print(f"Машина {self.name} едет со скоростью {self.speed}")

   if self.speed > 60:
    print("Внимание! Скорость превышает 60 км/ч, Вам необходимо снизить ее!")

