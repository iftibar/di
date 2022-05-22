class Farm:
    def __init__(self, name):
        self.name_of_farm = name
        self.stock = {}


    def add_animal(self, animal, amount=1):
        # if self.stock[animal] >= 0: in!!!
            self.stock[animal] += amount
        else:
            self.stock[animal] = amount


    def get_info(self):
        print(self.name_of_farm, "'s farm")
        for animal, amount in self.stock.items():
            print(animal, ":", amount)






macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()