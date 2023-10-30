import math

class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def square(self):
        p = (self.a + self.b + self.c) / 2
        s = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        print(f"Периметр треугольника: {s}")

    def perimeter(self):
        p = self.a + self.b + self.c
        print(f"Периметр треугольника: {p}")

    def is_triangle(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            print("Треугольник существует")
            return True

        else:
            print("Треугольника не существует")
            return False




