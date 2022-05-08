def display_message():
    print("im learning python!")
display_message()

# ex2
def favorite_book(title):
    print(f"one of my favorite books is {title}")
favorite_book("badulina")

# ex3
def describe_city(city, country="israel"):
    print(f"{city} is in {country}")
describe_city("berlin", "germany")

# ex4
import random
def create_random_num(num):
    sec_num = random.randint(1, 100)
    if sec_num == num:
        print("success!")
    else:
        print(f"no luck! {sec_num}, {num}")
create_random_num(40)

def make_shirt(size="large", text="i love python"):
    print(f"size of shirt is {size} and the text is {text}")
make_shirt()
make_shirt(size="medium")
make_shirt(size="small", text="i love apples")
make_shirt("xl", "nothing realy matters")

magician = ["Derren Brown", "David Blaine", "Jerry Sadowitz", "Dynamo", "Apollo Robbins", "Harry Houdini"]
def show_magician(list_of_magicians):
    for magician in list_of_magicians:
        print(magician)
def make_great(list_of_magician):
    for magician2 in list_of_magician:
        magician2 += " the great"
        print(magician2)


show_magician(magician)
make_great(magician)
