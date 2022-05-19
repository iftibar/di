def get_age(year, month):
    current_year = 2022
    current_month = 5
    if month > current_month:
        age = current_year - year - 1
    else:
        age = current_year - year
    print(age)
    return age
#
# def can_retire(gender, year, month):
#     if gender == 'm':
#         if get_age(year, month) >= 67:
#             return True
#     elif gender == 'f':
#         if get_age(year, month) >= 62:
#             return True
#     else:
#         return False
#
#
# user_month = int(input("month of birth? "))
# user_year = int(input("year of birth? "))
# gender = input("what is your gender? ")
# if can_retire(gender, user_year, user_month):
#      print("you can retire")
# else:
#     print("sorry you are too young to retire")

# ex8
num_list = []
def func(x):
    for i in range(1, 5):
        num = str(x) * i
        print(num)
        num_list.append(int(num))
    print(sum(num_list))
func(4)