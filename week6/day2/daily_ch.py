str = input("a string: ")
if len(str) < 10:
    print("not long enough")
elif len(str) > 10:
    print("string too long")
print(str[0], str[-1])
new_str = ''
for ch in str:
    new_str += ch
    # print(new_str)
import random
new_str = ''.join(random.sample(str, len(str)))
print(new_str)