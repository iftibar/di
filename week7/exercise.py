# def calculation(a, b):
#     addition = a + b
#     subtraction = a - b
#     return addition, subtraction
# res = calculation(40, 10)
# print(res)
# square = lambda n: n*n - 10
# num = square(5)
# print (num)
#
# def filter_say_hello(p):
#     return len(p) <= 4
# def say_hello(f):
#     return  "hello " + f
#
# people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
# filter_list = filter(filter_say_hello, people)
# map_list = map(say_hello, filter_list)
# print(list(map_list))
#
# def insertion_sort(alist):
#    for index in range(1,len(alist)):
#
#      currentvalue = alist[index]
#      position = index
#
#      while position>0 and alist[position-1]>currentvalue:
#          alist[position]=alist[position-1]
#          position = position-1
#
#      alist[position]=currentvalue
#
# alist = [54,26,93,17,77,31,44,55,20]
# insertion_sort(alist)
# print(alist)

def febbu(num):
        a = 0
        b = 1
        for i in range(num):
            yield a
            print("first", a)
            temp = a
            a = b
            b = b + temp
            print(a, b)
#
# for x in febbu(5):
#     print(x)

        # list = [0, 1]
        # for i in range(2, num):
        #     list.append(list[i-1] + list[i-2])
        #     print(list)

#
# febbu(1000)
#
# class BankAccount:
#
#     def __init__(self, account_number, balance=0):
#         self.account_number = account_number
#         self.balance = balance
#         self.transactions = []
#
#     def view_balance(self):
#         self.transactions.append("View Balance")
#         print(f"Balance for account {self.account_number}: {self.balance}")
#
#     def deposit(self, amount):
#         if amount <= 0:
#             print("Invalid amount")
#         elif amount < 100:
#             print("Minimum deposit is 100")
#         else:
#             self.balance += amount
#             self.transactions.append(f"Deposit: {amount}")
#             print("Deposit Succcessful")
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient Funds")
#         else:
#             self.balance -= amount
#             self.transactions.append(f"Withdraw: {amount}")
#             print("Withdraw Approved")
#             return amount
#
#     def view_transactions(self):
#         print("Transactions:")
#         print("-------------")
#         for transaction in self.transactions:
#             print(transaction)
#
# my_bank = BankAccount(150, 200)
# my_bank.deposit(120)
# my_bank.deposit(130)
# my_bank.withdraw(300)
# my_bank.view_balance()
# print(my_bank.view_transactions())
# #
# class Circle:
#     def __init__(self, diameter):
#       self.diameter = diameter
#
#     def grow(self, factor=2):
#         """grows the circle's diameter by factor"""
#         self.diameter = self.diameter * factor
#
# class NewCircle(Circle):
#     def grow(self, factor=2):
#         """grows the area by factor..."""
#         self.diameter = (self.diameter * factor * 2)
#
# nc = NewCircle(1)
# print(nc.diameter)
#
# nc.grow()
#
# print(nc.diameter)

# class Door:
#     def __init__(self, is_opened):
#         self.is_opened = is_opened
#     def open_door(self, is_opened):
#         if is_opened:
#             print("door is already open")
#         else:
#             is_opened = True
#             print("opening the door now")
#     def close_door(self, is_opened):
#         if is_opened:
#             is_opened = False
#             print("closing the door now")
#         else:
#             print("cant close a closed door")
#
#
# class BlockedDoor(Door):
#     def open_door(self):
#         raise Exception("cant open a blocked door")
#     def close_door(self):
#         raise Exception("cant close a blocked door")
#
#
# is_opened = False
# act = Door(is_opened)
# act.open_door(is_opened)
# act.close_door(is_opened)
# block = BlockedDoor(is_opened)
# block.open_door()

class A():

    def dothis(self):
        print("doing this in A")


class B(A):
    pass


class C():
    def dothis(self):
        print("doing this in C")


class D(B, C):
    pass

d_instance = D()
d_instance.dothis()
