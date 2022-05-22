# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# cat1 = Cat('jonny', 9)
# cat2 = Cat('shush', 4)
# cat3 = Cat('miuw', 13)
# def find_oldest(cat1, cat2,cat3):
#     oldest = {}
#     if cat1.age > cat2.age:
#         if cat1.age > cat3.age:
#             oldest[cat1.name] = cat1.age
#         else:
#             oldest[cat3.name] = cat3.age
#     else:
#         if cat2.age > cat3.age:
#             oldest[cat2.name] = cat2.age
#         else:
#             oldest[cat3.name] = cat3.age
#     for cat, age in oldest.items():
#         print(f" the oldest cat is {cat} and he is {age} years old")
#
# find_oldest(cat1, cat2, cat3)

# ex2
#
# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#
#     def bark(self):
#         print(f"{self.name} goes wooooof")
#
#     def jump(self):
#         print(f"{self.name} jumps {self.height * 2} cm high!")
#
# davids_dog = Dog('rex', 50)
# print(davids_dog.name, davids_dog.height)
# davids_dog.bark()
# davids_dog.jump()
# sarahs_dog = Dog("teacup", 20)
# print(sarahs_dog.name, sarahs_dog.height)
# sarahs_dog.bark()
# sarahs_dog.jump()
# if sarahs_dog.height > davids_dog.height:
#     print(sarahs_dog.name)
# else:
#     print(davids_dog.name)

# # ex3
# class Song:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)
#
# stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()

# ex4
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sort_list = sorted(self.animals)
        print(sort_list)


    def get_groups(self):
        groups = {}
        counter, first_letter = 0, ""

        for animal in sorted(self.animals):
            if animal[0].upper() != first_letter:
                counter += 1
                first_letter = animal[0].upper()
                groups[counter] = [animal]
            else:
                groups[counter].append(animal)
        print(groups)


ramat_gan_safari = Zoo("ramat_gan_safari")
ramat_gan_safari.add_animal("giraffe")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Emu")
ramat_gan_safari.add_animal("Eel")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.sell_animal("giraffe")
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()













