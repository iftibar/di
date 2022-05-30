class Circle():
    circle_list = []
    def __init__(self, radius):
        self.radius = radius
        self.diameter = self.radius * 2
        self.circle_list.append(self)

    def __add__(self, other):
        return  self.area() + other.area()

    def __gt__(self, other):
        return True if self.area() > other.area() else False

    def __eq__(self, other):
        return True if self.area() == other.area() else False

    def area(self):
        area = 3.14 * self.radius ** 2
        return area

    def sort(self):
        self.circle_list.sort()
        return self.circle_list

c1 = Circle(5)
c2 = Circle(7)
c1.area()
print(c1+c2)
print(c1 == c2)
print(c2 > c1)
print(c1.sort())
# missing some additional requirments
