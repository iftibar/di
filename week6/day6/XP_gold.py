
birthday = {
'naama': "14/3/1981",
'david': "6/9/1945",
'shlomit': "5/7/1945",
'pike':" 10/1/2010",
'dani':" 12/11/1985"
}
print("welcome!")
name = ''
# while name != 'quit':
#     name = input("give me a name to look up: ")
#     dic = birthday.items()
#     dic_keys = birthday.keys()
#     for person in dic_keys:
#         if person == name:
#             print(f"your happy birthday is: {birthday[person]}")
#         else:
#             print("sorry its not here")
#             break

# ex2+3
# new_name = input("what is the name  to add? ")
# add_birthday = input("what is your birthday? ")
# birthday[new_name] = add_birthday
# dic_keys = list(birthday.keys())
# print(dic_keys)
# while name != "quit":
#     name = input("give me a name to look up: ")
#     if (name in dic_keys):
#         print(f"your happy birthday is: {birthday[name]}")
#     else:
#         print(f"sorry we don't have birthday info about {name}")
#
# # ex4
# sum = 0
# items = {
#     "banana": { "price": 4, "stock": 2},
#     "apple": {"price": 2, "stock": 5},
#     "orange": {"price": 1.5, "stock": 4},
#     "pear": {"price": 3, "stock": 10}
#     }
# fruits = list(items.keys())
# prices = list(items.values())
# for i in range(len(fruits)):
#     print(f"we have {fruits[i]} which costs {prices[i]} shekels")
# for x in items:
#     sum += items[x]["price"] * items[x]["stock"]
# print(sum)

# ex5:
cars = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
spl_car = cars.split()
spl_car.sort(reverse=True)
# print(f"we have {len(spl_car)} companies in our list {spl_car}")
o_cars = [car for car in spl_car if 'o' in car]
i_cars_false = [car for car in spl_car if "i" not in car]
# print(o_cars)
# print(i_cars_false)
new_car = set(["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"])
str = ",".join(new_car)
# print(str)
# print(f"there are {len(new_car)} companies in the list")
new_car = list(new_car)
new_car.sort()
rev_car = [car[::-1] for car in new_car]
print(rev_car)