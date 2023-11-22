from .Car import Car
class PoliceCar(Car):
    def show_speed(self):
        print(f"Машина {self.name} едет со скоростью {self.speed}")
    def viu(self):
        print("Виу! Виу! Виу! Виу!")

    def stop_request(self):
        print(f"Внимание! {self.color} {self.name} Съедьте на край шоссе! Вы превысили скорость!")
