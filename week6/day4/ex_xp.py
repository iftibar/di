my_fav_num = {3, 7, 9}
my_fav_num.add(16)
my_fav_num.add(11)
my_fav_num.remove(11)
friend_fav_num = {12, 14, 19}
our_fav_num = my_fav_num.union(friend_fav_num)

# print(our_fav_num)

# ex2
# no

# # ex3
# for i in range(1,21):
#     print(i)

# # ex4
# new_li = []
# for x in range(3,11):
#    new_li.append(x/2)
# print(new_li)
#
# # ex5
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.pop(2)
# basket.append("kiwi")
# basket.insert(0, "Apples")
# print(basket.count("Apples"))
# basket.clear()
# print(basket)
# #

# # ex7
# my_list = [45, 21, "goa", "ombeach", 55, 33.2, 'true', 'false', 'true']
# for i in my_list:
#     if my_list.index(i) % 2:
#         continue
#     else:
#         print(i)

# # ex8
# for i in range(1500, 2501):
#     if i % 5 == 0 or i % 7 ==0:
#         print(i)

# # ex9
# fruits = input("what is your favorite fruits? ")
# fruit_list = fruits.split()
# ano_fruit = input("another fruit please? ")
# if ano_fruit in fruit_list:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy")
#
# toping_list =[]
# toping = ""
# while toping != "quit":
#     toping = (input("what do you want to add on your pizza?  "))
#     if toping != "quit":
#         toping_list.append((toping))
#         print(f"i will add {toping} on your pizza")
#     else:
#         break
# price = len(toping_list) * 2.5 + 10
# print(f" on your pizaa {toping_list} your total price is {price}")

# # ex11
# sum = 0
# family = (input("what are the ages? "))
# spl_fam = family.split()
# int_family = [int(i) for i in spl_fam]
# for i in int_family :
#     if i <= 3:
#         sum += 0
#     elif i > 3 and i <= 12:
#         sum += 10
#     else:
#         sum += 15
# print(sum)

# ex12
teens = ["allen", "yael", "shimi", "david", "michal"]
new_teen =[]
age = 0
for i in teens:
    age = int(input(f"Hi {i} what is your age? "))
    if age >= 16 and age <= 21:
        new_teen.append(i)
print(new_teen)

# ex12

list = ["roy", "dani", "sigal", "simon", "lea", "frank"]
for i, x in enumerate(list):
    print(i, x)
    age = int(input(f"what is your age {x}? "))
    if age < 16:
        list.remove(x)
        i -= 1
# print(list)

# ex13
sandwich_orders = ["tuna", "salamy", "omlete", "cheese"]
finished_sandwiches = []
for i in sandwich_orders:
    sandwich_orders.remove(i)
    print(sandwich_orders)