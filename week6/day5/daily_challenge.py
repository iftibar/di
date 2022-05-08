user_text = input("enter your text: ")
action = input("to encrypte enter 0, to decrypte enter 1 ")
abc = [*"abcdefghijklmnopqrstuvwxyz"]
new_text = []
for x in user_text:
    text = list(user_text)
    if int(action) == 0:
        if x != " ":
            new_text += chr(ord(x) + 3)
            cypher_text = "".join(new_text)
        else:
            continue
    else:
        new_text += chr(ord(x) - 3)
print(cypher_text)


user_text = input("enter your text: ")
is_decrypt = bool(input("to encrypt enter 0, to decrypt enter 1 "))
cypher_text = ""
for letter in user_text:
	if is_decrypt:
		if letter not in [" ", ',', '.']:
			new_letter = chr(ord(letter) + 3)
			cypher_text = f"{cypher_text}{new_letter}"
		else:
			cypher_text = f"{cypher_text}{letter}"

print(cypher_text)
