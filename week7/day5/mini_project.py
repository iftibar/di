# words = input("give me some words: ")
# spl_list = words.split(",")
# sort_list = sorted(spl_list)
# print(sort_list)

words2 = input("give me some words: ")
spl = words2.split(",")
sort_list = sorted(word for word in spl)
print(sort_list)