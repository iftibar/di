# # ex1
# list1 = ["i love to play drums"]
# list2 = ["and to play bass as well"]
# list1.extend(list2)
# print(list1)

# # ex2
# num = []
# list_num = input("3 numbers: ")
# sp_list = (list_num.split())
# x = 0
# while x < len(sp_list):
#     num.append(sp_list[x]) \\\\ why num[x] = doesnt work?????
#     print(num[x])
#     x += 1
#
# num1 = int(input("first number: "))
# num2 = int(input("first second: "))
# num3 = int(input("first third: "))
# big_num = 0
# if num1 > num2:
#     if num1 > num3:
#         big_num = num1
#     else:
#         big_num = num3
# else:
#     if num3> num2
#         big_num = num3
#     else:
#         big_num = num2
# print(big_num)

#
# # ex3
# list_let = []
# letters = ["abcdefghijklmnopqrstuvwxyz"]
# for ch in letters:
#     list_let = (list(ch))
# vowel = ["a", "e", "i", "o", "u", "y", "w"]
#
# for char in (list_let):
#     if char in vowel:
#         print(f"the letter {char} is a vowel")
#     else:
#         print(f"the letter {char} is a consonant")

# # ex4?????
# index = 0
# user_name = ""
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# user_name = input("what is your name? ")
# for name in names:
#     if name == user_name:
#         index = names.index(user_name)
#         print (f"the first position of {name} is at {index}")
#         break
#     else:
#         user_name = input("what is your name? ")
#         for name in names:
#             if name == user_name:
#                 index = names.index(user_name)
#                 print(f"the first position of {name} is at {index}")
#                 break
# # ex5????
# spl = []
# ind = 0
# words = input("7 words please: ")
# letter = input("enter a letter: ")
# spl = words.split()
# for word in spl:
#     print(word, letter)
#     ind = word.find(letter)
#     print(ind)
#     if ind > -1:
#         print(f"first index of {letter}" is {ind})
#     else:
#         print("its not here im sorry")
#
# # ex6
# num_list = []
# sum_list = 0
# for i in range(1, 1000000):
#     num_list.append(i)
# sum_list = sum(num_list)
# print(sum_list)

num_list = [num for num in  range(100)]
print(sum(num_list), num_list)