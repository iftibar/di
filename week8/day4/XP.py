import random


class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
#
# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
#
# class White(Cat):
#     def gurg(self, sound):
#         return f'{sound}'
#
#
# jimmy = Bengal('jimmy', 12)
# chu = Chartreux('chu', 4)
# boby = White('boby', 2)
# my_cats = [jimmy, chu, boby]
# my_pets = Pets('josh')
# my_cats.append(Bengal('miuw', 3))
# for cat in my_cats:
#     print(cat.walk())

# ex2
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
            return f'{self.name} is barking'

    def run_speed(self):
            speed = self.weight / self.age * 10
            return speed

    def fight(self, other_dog):
            speed1 = self.run_speed()
            if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
                return f'{self.name} won the fight!'
            else:
                return f'{other_dog.name} won the fight'


jimmy = Dog('jimmy', 10, 30)
jonny = Dog('jonny', 8, 23)
yup = Dog('yup', 6, 19)
# print(jonny.run_speed())
# print(jimmy.fight(jonny))

# ex3

class PetDog(Dog):

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *dogs):
        for dog in dogs:
            print(dog.name, end = ' ')
        print(f"and {self.name} all play together")

    def do_a_trick(self):
        if self.trained:
            rand = random.randint(1,4)
            if rand == 1:
                print(f'{self.name} does a barrel roll')
            elif rand == 2:
                print(f'{self.name} stands on his back legs')
            elif rand == 3:
                print(f'{self.name} shakes your hand')
            elif rand == 4:
                print(f'{self.name} plays dead')
        else:
            print(f"you need to train {self.name}")

pike = PetDog('pike', 12, 35)
print(pike.trained)
pike.play(jonny, jimmy)
pike.train()
pike.do_a_trick()