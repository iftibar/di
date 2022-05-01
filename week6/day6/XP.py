# # ex1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# zipi = zip(keys, values)
# print(tuple(zipi))

# # ex2
# price = 0
# family = {}
# n = int(input("how many people?"))
# for i in range(n):
#     key = input("what is your name?")
#     value = int(input("how old are you?"))
#     family[key] = value
# for person in family.items():
#     (name, age) = person
#     if age < 3:
#         print(f"{name} can enter for free")
#     elif age < 12:
#         print(f"{name} need to pay 10$")
#         price += 10
#     else:
#         print(f"{name} need to pay 15$")
#         price += 15
# print(price)

# ex3
# brand = {
#     "name": "Zara" ,
#     "creation_date": 1975,
#     "creator_name": "Amancio Ortega Gaona",
#     "type_of_clothes": ["men", "women", "children", "home"],
#     "international_competitors": ["Gap", "H&M", "Benetton"],
#     "number_stores": 7000,
#     "major_color": {
#         "France": "blue",
#         "Spain": "red",
#         "US": ["pink", "green"]
# }
# }
#
# last_comp = 0
# brand["number_stores"] = 2
# print(f"{brand['name']} was created in {brand['creation_date']} by {brand['creator_name']} and making clothes for {brand['type_of_clothes'][0]}, {brand['type_of_clothes'][1]} and {brand['type_of_clothes'][2]}")
# brand["country_creation"] = "spain"
# if 'international_competitors' in brand:
#     brand['international_competitors'].append("Desigual")
# del brand['creation_date']
# last_comp = len(brand['international_competitors']) - 1
#
# print(brand['international_competitors'][last_comp])
# print(brand['major_color']['US'])
# print(len(brand))
# print(brand.keys())
# more_on_zara = {
#     "creation_date": 1975,
#     "number_stores": 10000
# }
# brand.update(more_on_zara)
# print(brand['number_stores'])
# print(brand)

# ex4
disney_users_A = {}
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# for x in range(len(users)):
#     disney_users_A[users[x]] = x
# print(disney_users_A)
# disney_users_B = {}
# for x in range(len(users)):
#     disney_users_B[x] = users[x]
# print(disney_users_B)
# disney_users_C = {}
# users.sort()
# for x in range(len(users)):
#     disney_users_C[users[x]] = x
# print(disney_users_C)

for x in range(len(users)):
    if "i" in users[x]:
        disney_users_A[users[x]] = x
    else:
        del users[x]
        x = 0
print(disney_users_A)












