s = input("string: ")
ch = input("character: ")
count = 0
for c in s:
    if c == ch:
        count += 1
print(count)