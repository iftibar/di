# ex2
import datetime
import string
import random

#
# def rando(user_num):
#     random_num = random.randint(1, 100)
#     if user_num == random_num:
#         print("success massage!")
#     else:
#         print(random_num)
#
# user_num = int(input("a number: "))
# rando(user_num)

# # ex3
# result = ''
# low_list = list(string.ascii_lowercase)
# cap_list = list(string.ascii_uppercase)
# letters = low_list + cap_list
# for i in range(5):
#     result += "".join(random.choice(letters))
# print(result)

# # ex4
# import datetime
# def current_date():
#    print(datetime.datetime.today())
#
# current_date()

# ex5
# import datetime
#
# def get_relative_time(dt):
#     now = datetime.datetime.now()
#     delta_time = dt - now
#     return  delta_time
#
#
# future_date = datetime.datetime(2023, 1, 1)
# print(f"the 1st of january 2023 is in {get_relative_time(future_date)} hours")

# ex6
import datetime
#
#
# def minutes_lived(date):
#     now = datetime.datetime.now()
#     delta_time = now - date
#     days = delta_time.days * 60
#     hours = days * 24 + now.hour * 60
#     minutes = hours * 60 + now.minute
#     return minutes
#
#
# birthday = datetime.datetime(1980, 8, 5)
# print(f"you have lived {minutes_lived(birthday)} minutes so far")

# # ex7
# def today_date():
#     now = datetime.datetime.today()
#     print(f" today is {now}")
#     next_holiday = datetime.datetime(2023, 6, 4)
#     delta = next_holiday - now
#     holiday = "shvauot"
#     print(f"next holiday is {holiday} in {delta} hours")
#
#
# today_date()

# ex8
# def calculate_age(age):
#     earth_age = age / 31557600
#     print(f" age on earth is {earth_age}")
#     mercury_age = earth_age * 0.24
#     print(f"mercury age is {mercury_age}")
#     venus_age = earth_age * 0.61
#     print(f"venus age is {venus_age}")
#     mars_age = earth_age * 1.88
#     print(f"mars age is {mars_age}")
#     jupiter_age = earth_age * 11.86
#     print(f"jupiter age is {jupiter_age}")
#
#
# calculate_age(1000000000)

# ex9
from faker import Faker
users = []
fake = Faker()

def add_fake_dict():
    new_dict = {"name": fake.name(),
                "address": fake.address(),
                }

    users.append(new_dict)


add_fake_dict()
print(users)
