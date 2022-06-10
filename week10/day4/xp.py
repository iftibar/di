# import random
#
# list_of_words = []
#
#
# def get_words_from_file():
#     with open(r"C:\Users\user\Desktop\DI\week10\day4\sowpods.txt") as f:
#         lines = f.readlines()
#         lines_without_n = [line.strip("\n") for line in lines]
#         for line in lines_without_n:
#             list_of_words.append(line.lower())
#         return list_of_words
#
# def get_random_sentence(length):
#     sentence = ''
#     list_of = get_words_from_file()
#     for i in range(length):
#         sentence += random.choice(list_of) + " "
#     print(sentence)
#
# def main():
#     print("this program generates a random sentence, you can choose hoe long will it be")
#     user_input = int(input("choose the length of sentence between 2-20: "))
#     if user_input < 2 or user_input > 20:
#         print("error message")
#     else:
#         get_random_sentence(user_input)
#
#
# main()

import json
import flask

app = flask.Flask(__name__)


sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)
print(data['company']['employee']['payable']['salary'])
data['company']['employee']['birth_date'] = 3.3
new_data = json.dumps(data, indent=2, sort_keys=True)
print(new_data)