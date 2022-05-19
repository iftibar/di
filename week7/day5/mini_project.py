# words = input("give me some words: ")
# spl_list = words.split(",")
# sort_list = sorted(spl_list)
# print(sort_list)

words2 = input("give me some words: ")
spl_list2 = words2.split(",")
for word in spl_list2:
   print(sorted(spl_list2))
sort_list2 = sorted(word for word in words2)

print(sort_list2)