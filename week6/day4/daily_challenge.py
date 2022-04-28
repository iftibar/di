birthday = (input("what is your birthday?? dd mm yyyy format "))
birth = birthday.split()
this_year = 2022
this_month = 4
this_day = 28
if this_month > int(birth[1]):
    age = this_year - int(birth[2])
elif this_month == int(birth[1]):
    if this_day > int(birth[0]):
        age = this_year - int(birth[2])
    elif this_day == int(birth[0]):
        print ("today is your birthday!")
        age = this_year - int(birth[2])
    else:
        age = this_year - int(birth[2]) - 1
else:
    age = this_year - int(birth[2]) - 1
age = age / 10
from math import trunc
trun_age = trunc(age)
candels = ""
for i in range(0, trun_age):
    candels += "i"
# drow the cake"
str_space = ""
space = trunc((13 - trun_age) / 2)
for x in range(0, space):
    str_space += "_"
print("  " + str_space + candels + str_space)
print("  |:H:a:p:p:y:|")
print("__|___________|__")
print("|^^^^^^^^^^^^^^^^^|")
print("|:B:i:r:t:h:d:a:y:|")
print("|                 |")
print("~~~~~~~~~~~~~~~~~~~")