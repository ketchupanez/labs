from .Car import Car
class SportCar(Car):
    def show_speed(self):
        print(f"Машина {self.name} едет со скоростью {self.speed}")
        print("")
    def vrum(self):
        print("Врум! Врууум!")