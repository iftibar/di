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

# ex4
# index = -1
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# user_name = input("what is your name? ")
# for name in names:
#     if user_name == name:
#         index = names.index(name)
#         break
#     else:
#         continue
# if index == -1:
#     print("soory its not here")
# else:
#     print(f"the first position of {name} is at {index}")

# # ex5
# ind = -1
# words = input("7 words please: ")
# letter = input("enter a letter: ")
# spl_words = words.split()
# for word in spl_words:
#     ind = word.find(letter)
#     if ind > -1:
#         print(f"first index of {letter} is located in {ind} in the word {word}")
#     else:
#         print(f"the letter {letter} is not in {word}")
#
# # ex6
# num_list = []
# sum_list = 0
# for i in range(1, 1000000):
#     num_list.append(i)
# sum_list = sum(num_list)
# print(sum_list)
# max = max(num_list)
# min = min(num_list)
# print(min, max)

# # ex7
# num_list = input("enter numbers: ")
# new = num_list.replace(",","")
# print(new)
# print(list(new))
# print(tuple(new))

# ex8
import random
wins = 0
random_num = random.randint(1, 9)
num = int(input("what is your lucky number? "))
while num != 99:
    if num == random_num:
        print("you won!!")
        wins += 1
        random_num = random.randint(1, 9)
        num = int(input("try again? "))
        continue
    else:
        print("better luck next time")
        num = int(input("lets try again? "))
print(f" yow won {wins} times, good job!")


