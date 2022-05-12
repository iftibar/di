import random

def get_random_temp(season):
    if season == "winter":
        temp = random.uniform(-10, 16)
    if season == "spring":
        temp = random.uniform(10, 25)
    if season == "summer":
        temp = random.uniform(18, 45)
    if season == "fall":
        temp = random.uniform(8, 24)
    return temp

input_season = input("what season: ")
def main():
    t = get_random_temp(input_season)
    if t < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif t < 16 and t >= 0:
        print("Quite chilly! Don’t forget your coat")
    elif t < 23 and t >= 16:
        print("its a nice weather to be in the sun")
    elif t < 32 and t >= 23:
        print("pretty hot today")
    elif t < 40 and t >= 32:
         print("its hell out there")
    print(t)

main()