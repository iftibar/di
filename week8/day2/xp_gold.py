# # ex1:
# class Circle:
#     def __init__(self, radius=1.0):
#         self.radius = radius
#
#     def perimeter(self):
#         return self.radius * 2
#     def area(self):
#         return self.radius ** 2 * 3.14
#     def get_def(self):
#         print(f"the perimeter of the circle is {self.perimeter()} and the area is {self.area()}")
#
# x = Circle(6)
# x.get_def()

# # ex2:
# import random
# class Mylist:
#     def __init__(self, list):
#         self.list = list
#     def reverse(self):
#         return reversed(self.list)
#     def sort(self):
#         return sorted(self.list)
#     def generate(self):
#         new_list = [random.randint(0, 1000) for x in self.list]
#         return new_list
#
#
# list_to_pass = ['a', 'b', 'h', 'v', 'd', 'z', 'e']
# example = Mylist(list_to_pass)
# print(list(example.reverse()))
# print(list(example.sort()))
# print(example.generate())

# ex3
class MenuManager:
    def __init__(self, menu):
        self.menu = menu

    def add_item(self, new):
        self.menu.append(new)

    def update_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish["name"] == name:
                self.menu.pop(name)
                rest.add_item(name, price, spice, gluten)
            else:
                print("this dish isn't on the menu")

menu = [
    {
        "name": "soup",
        "price": 10,
        "spice": 'B',
        "gluten": False
    },
    {
        "name": "Hamburger ",
        "price": 15,
        "spice": 'A',
        "gluten": True
    },
    {
        "name": "salad",
        "price": 18,
        "spice": 'A',
        "gluten": False
    },
    {
        "name": "french fries",
        "price": 5,
        "spice": 'C',
        "gluten": False
    },
    {
        "name": " Beef bourguignon",
        "price": 25,
        "spice": 'B',
        "gluten": True
    }
 ]
rest = MenuManager(menu)
new_dish = {"name": 'pizza',"price": 12,"spice": "B","gluten": True}
rest.add_item(new_dish)
rest.update_item("soup", 15, "B", False)
print(menu)
