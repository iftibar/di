class Farm:
    def __init__(self, name):
        self.name_of_farm = name
        self.stock = {}


    def add_animal(self, animal, amount=1):
        if animal in self.stock:
            self.stock[animal] += amount
        else:
            self.stock[animal] = amount


    def get_info(self):
        print(self.name_of_farm, "'s farm")
        for animal, amount in self.stock.items():
            print(animal, ":", amount)
        print("\n      E-I_E_I_O!")

    def get_animal_types(self):
        animal_list = self.stock.keys()
        return sorted(animal_list)

    def get_short_info(self):
        animals = macdonald.get_animal_types()
        last_animal = animals[len(animals) - 1]
        print(f"Mcdonald farm has {animals[0]}s, {animals[1]}s and {last_animal}.")



macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()
macdonald.get_short_info()