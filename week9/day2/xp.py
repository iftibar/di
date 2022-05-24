class Currency:
    def __init__(self, currency, num):
        self.currency = currency
        self.num = num

    def __str__(self):
        print(f"{self.num} {self.currency}s")
        return ""

    def __int__(self):
        print(self.num)
        return self.num

    def __repr__(self):
        print(f"{self.num} {self.currency}s")
        return ""

    def __add__(self, other):
        try:
            print(self.num + other)
        except:
            print(self.num + other.num)

    def __iadd__(self, other):
        try:
            return self.num + other.num

        except:
            self.value = self.num + other
            print(self.value)

    def __call__(self, *args, **kwargs):
        print(f"{self.num} {self.currency}s")


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

str(c1)
'5 dollars'
int(c1)
repr(c1)
'5 dollars'
c1 + 12
c1 + c2
c1()
c1 += 5
c1 += c2

# 20 dollars
#
# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>