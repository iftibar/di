user_text = input("enter your text: ")
action = input("to encrypte enter 0, to decrypte enter 1 ")
letters = ["abcdefghijklmnopqrstuvwxyz"]
let = []
new_text = []
i = 0
for x in user_text:
    text = list(user_text)
    if int(action) == 0:
        for ch in letters:
            let = (list((ch)))
            if i == len(let) - 2:
                list[i] = list[i - 24]
            else:
                new_text[i] += let[i+3]
        i += 1
print(text)
print(new_text)

