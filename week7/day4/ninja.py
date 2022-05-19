# def get_full_name(first, last,  middle=""):
#     print(first, middle, last)
# first_name = input("first name: ")
# middle_name = input("middle name: (optional) ")
# last_name = input("last name: ")
# get_full_name(first_name, last_name, middle_name)

# ex2
morse = {
    'A': ".-",
    'B': "-...",
    'C': "-.-. ",
    'D': "-.. ",
    'E': '.',
    'F': "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-	",
    "V": "...-",
    "W": ".--	",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--.."
}
def convert_to_morse(text):
    converted_text = ""
    for char in text:
        converted_text += morse[char] + "/ "



