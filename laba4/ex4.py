class BouquetShop:
    def __init__(self, name, price, species):
        self.name = str(name)
        self.price = price
        self.species = str(species)

    @staticmethod
    def output():
        print("- Добро пожаловать в наш цветочный магазин! Какой букет желаете приобрести?")

    @classmethod
    def catalog(cls):
        bouq1 = BouquetShop("Вы любите розы?", 79, "роз")
        bouq2 = BouquetShop("За тебя калым отдам", 87, "хризантем")
        bouq4 = BouquetShop("Мало половин", 61, "васильков+ромашек")
        bouq5 = BouquetShop("Желтые тюльпаны", 70, "желтых тюльпанов")
        print(" У нас в наличии:")
        print(f"1. '{bouq1.name}' - {bouq1.price}$, композиция состоит из: {bouq1.species}")
        print(f"2. '{bouq2.name}' - {bouq2.price}$, композиция состоит из: {bouq2.species}")
        print(f"3. '{bouq4.name}' - {bouq4.price}$, композиция состоит из: {bouq4.species}")
        print(f"4. '{bouq5.name}' - {bouq5.price}$, композиция состоит из: {bouq5.species}\n")

    def __str__(self):
        pass


