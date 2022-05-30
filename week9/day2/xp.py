class Currency:
    def __init__(self, currency, num):
        self.currency = currency
        self.num = num

    def __str__(self):
        print(f"{self.num} {self.currency}s")
        return "" # why you return empty string?

    def __int__(self):
        print(self.num) # print is redundant I think you added it just for testing
        return self.num 

    def __repr__(self):
        print(f"{self.num} {self.currency}s")
        return "" # why you return empty string?

    def __add__(self, other):
        if self.currency != other.currency:
            raise Exception("TypeError: Cannot add between Currency type <dollar> and <shekel>")
        try: # at this case the exception is redundant 
            print(self.num + other)
        except:
            print(self.num + other.num)



    def __iadd__(self, other):
        try: # try to think for other solution
            self.num = self.num + other.num

        except:
            self.num = self.num + other
        return self

    def __call__(self, *args, **kwargs):
        print(f"{self.num} {self.currency}s")


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

# str(c1)
# '5 dollars'
# int(c1)
# repr(c1)
# '5 dollars'
# c1 + 12
# c1 + c2
# c1()
c1 += 5
c1 += c2
print(c1.num)
c1 + c3
