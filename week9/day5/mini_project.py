class Queue:
    humans = [] # why you make it global

    def add_person(self, person):
        self.humans.append(person)

    def find_in_queue(self, person):
        if person in self.humans: # inorder to access to global attribute use the class name which is best practice like: Queue.humans
            return self.humans.index(person)
        else:
            return None

    def swap(self, person1, person2):
        i = self.find_in_queue(person1)
        j = self.find_in_queue(person2)
        self.humans[i] = person2
        self.humans[j] = person1

    def get_next(self):
        if self.humans:
            return self.humans.pop(0)
        else: # it's redundant, it will return by default none
            return None

    def get_next_blood_type(self, blood_type):
        for person in self.humans:
            if blood_type == person.blood_type:
                return person.name

    def sort_by_age(self):
        self.humans.sort(key=lambda x: x.age, reverse=True)
        for person in self.humans:
            if person.priority:
                self.humans.insert(0, self.humans.pop(self.humans.index(person)))

    def rearange_queue(self):
        for i, person in enumerate(self.humans):
            try: # why you srouund it with try and except, it's redundant
                next = self.humans[i+1]
                if next.name in person.family:
                    print(i, len(self.humans))
                    if i >= len(self.humans) - 2:
                        person.swap(person, self.humans[i-1])
                    else:
                        next.swap(next, self.humans[i+2])
            except:
                pass # it's bad practice always at the except we must do something, event print
        for person in self.humans:
            print(person.name, end=" ")
        print('')


class Human(Queue):
    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = []
        super().__init__()

    def add_family_member(self, person):
        self.family.append(person.name)
        person.family.append(self.name)


ift = Human("123", "ift", 41, False, "A")
igor = Human("456", "igor", 62, False, "B")
ana = Human("789", "ana", 45, True, "AB")
dudi = Human("123", "dudi", 70, False, "B")
yael = Human("234", "yael", 24, True, "O")
yael.add_person(yael)
dudi.add_person(dudi)
igor.add_person(igor)
ift.add_person(ift)
ana.add_person(ana)
# print(dudi.find_in_queue(dudi))
# print(Queue.get_next_blood_type(Queue, "A"))
# print(Queue.get_next(Queue).name)
yael.add_family_member(dudi)
# dudi.swap(dudi, ana)
dudi.rearange_queue()
