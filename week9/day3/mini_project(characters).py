class Character():

    def __init__(self, name):
        self.name = name
        self.life = 20
        self.attack = 10
    @property
    def life(self):
        return self.__life

    @life.setter
    def life(self, life):
        if life < 0:
            self.__life = 0
        else:
            self.__life = life

    def basic_attack(self, other):
        other.life -= self.attack
        print(f"{other.name} have {other.life} left")


class Druid(Character):
    def __init__(self, name):
        super().__init__(name)
        print("druid is here to get this game!")

    def meditate(self):
        self.life += 10
        self.attack -= 2
        print(f"{self.name} have {self.life} life and {self.attack} attack")

    def animal_help(self):
        self.attack += 5
        print(f"{self.name} have {self.attack} attack")

    def fight(self, other):
        other.life = 0.75 * other.life
        other.attack = 0.75 * other.attack
        self.life += 0.5 * self.attack
        print(f"{self.name} have {self.life} life and {self.attack} attack")
        print(f"{other.name} have {other.life} life left and {other.attack} attack")


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        print('warrior is here to win!!')

    def brawl(self, other):
        other.life -= 2 * self.attack
        print(f"{other.name} have {other.life} life left and {other.attack} attack")


    def train(self):
        self.life += 2
        self.attack += 2
        print(f"{self.name} have {self.life} life and {self.attack} attack")


    def roar(self, other):
        other.attack -= 3
        print(f"{other.life} life and {other.attack} attack")


class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        print("mage is the one and only left standing")

    def curse(self, other):
        other.attack -= 2
        print(f"{other.name} have {other.life} life and {other.attack} attack")


    def summon(self):
        self.attack += 3
        print(f"{self.name} have {self.attack} attack")

    def cast_spell(self, other):
        other.life -= self.attack / self.life
        print(f"{other.name} have {other.life} life left")



jason = Druid('jason')
mickey = Warrior('mickey')
jane = Mage('jane')
jason.meditate()
jason.animal_help()
jason.fight(mickey)
mickey.brawl(jason)
mickey.train()
print(mickey.life, mickey.attack)
print(jason.life, jason.attack)
jane.curse(mickey)
jane.summon()
jane.cast_spell(jason)
print(jane.attack)
jane.basic_attack(mickey)
jason.basic_attack(mickey)
mickey.train()
