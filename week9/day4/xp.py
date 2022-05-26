class City:
    buildings = []
    averages = []

    def __init__(self, name):
        self.name = name


    def info(self):
        Building.average()
        num_of_buildings = len(self.buildings)
        aver = sum(City.averages) / len(City.averages)
        print(f" number of total buildings in {self.name} is {num_of_buildings} average age is {aver}")


class Building(City):
    inhabitants = []

    def __init__(self, address):
        self.address = address
        super().__init__(City)

    def construct(self, address):
        self.buildings.append(address)
        print(f"we have a new building at {self.address}")
        return None

    def average():
        sum_of_age = 0
        for person in Building.inhabitants:
            sum_of_age += person.age
        City.averages.append(sum_of_age / len(Building.inhabitants))


class Human(Building):
    def __init__(self, name, age, living_place=None):
        self.name = name
        self.age = age
        self.living_place = living_place
        print("a human was born")
        super().__init__(Building)

    def move(self, building):
        self.living_place = building
        self.inhabitants.append(self)
        print(f"{self.name} has moved")


iftach = Human("iftach", 41)
noga = Building("noga 6")
noga.construct("noga 6")
pardes = City("pardes")
iftach.move(noga)
naama = Human("naama", 39)
naama.move(noga)
alumot = Building("alumot 12")
john = Human("john", 20)
john.move(alumot)
alumot.construct("alumot 12")
print(pardes.buildings)
pardes.info()