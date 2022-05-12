sentence = input("enter a sentence: ")
rev_sent = sentence[::-1].split()
new_word = ""
new_sent = []
for word in rev_sent:
    new_word = word[::-1]
    new_sent.append(new_word)
a = " ".join(new_sent)
print(a)