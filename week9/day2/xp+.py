class Family():
    def __init__(self):
        self.members = [
            # {'name': 'Michael', 'age':35, 'gender':'Male', 'is_child': False},
            # {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
            ]
        self.last_name = 'kats'

    def born(self, **kwargs):
        print("congratulation for the new addition to the family!")
        self.members.append(kwargs)

    def is_18(self, name):
        for person in self.members:
            if person["name"] == name:
                if person["age"] > 18:
                   return True
                else:
                   return False

    def print_members(self):
        for person in self.members:
            list_to_print = {k: v for k, v in person.items() if k == 'name' or k == 'age' or k == 'gender' or k == 'is_child'}
        print(list_to_print)


# kats = Family()
# kats.born(name='eli', age=0, gender='female', is_child=True)
# print(kats.is_18('eli'))
# kats.print_members()

# ex2
class TheIncredibles(Family):

    def use_power(self):
      if parr.is_18(self):
          print(self.members["power"])

    def incredible_presentation(self):
        print(self.members)

parr = TheIncredibles()
parr.born(name='bob', age=44, gender='male', is_child=False, power='speed_of_light', incredible_name='Mr. incredible')
parr.born(name='Helen', age=41, gender='female', is_child=False, power='flying high', incredible_name='Mrs. incredible')
parr.born(name='Violet', age=14, gender='female', is_child=True, power='invisible', incredible_name='ultra violet')
parr.born(name='Robert', age=10, gender='male', is_child=True, power='run over water', incredible_name='Dash')
parr.born(name='John', age=4, gender='male', is_child=True, power='unknown power', incredible_name='Jack-Jack')



parr.print_members()
parr.incredible_presentation()