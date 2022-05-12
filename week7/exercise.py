def calculation(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction
res = calculation(40, 10)
print(res)
square = lambda n: n*n - 10
num = square(5)
print (num)

def filter_say_hello(p):
    return len(p) <= 4
def say_hello(f):
    return  "hello " + f

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
filter_list = filter(filter_say_hello, people)
map_list = map(say_hello, filter_list)
print(list(map_list))