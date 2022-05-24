class Character():

    def __init__(self, name):
        self.name = name
        self.life = 20
        self.attack = 10

    def basic_attack(self, other):
        other.life -= self.attack


class Druid(Character):
    def __init__(self, name):
        super().__init__(name)
        print("druid is here to get this game!")

    def meditate(self):
        self.life += 10
        self.attack -= 2

    def animal_help(self):
        self.attack += 5

    def fight(self, other):
        other.life = 0.75 * other.life
        other.attack = 0.75 * other.attack
        self.life += 0.5 * self.attack

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        print('warrior is here to win!!')

    def brawl(self, other):
        other.life -= 2 * self.attack

    def train(self):
        self.life += 2
        self.attack += 2

    def roar(self, other):
        other.attack -= 3


class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        print("mage is the one and only left standing")

    def curse(self, other):
        other.attack -= 2

    def summon(self):
        self.attack += 3

    def cast_spell(self, other):
        other.life -= self.attack / self.life


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