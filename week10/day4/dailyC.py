class Text(str):
    def __init__(self, str):
        self.string = str

    def freq_of_word(self, word):
        list_of_words = []
        list_of_words = self.string.split()
        counter = list_of_words.count(word)
        if counter:
            print(f'the word {word} appears {counter} times in the text')
            return counter
        else:
            return None

    def most_common_word(self):
        list_of_words = []
        common = 0
        common_word = ''
        list_of_words = self.string.split()
        for word in list_of_words:
            counter = list_of_words.count(word)
            if counter > common:
                common = counter
                common_word = word
            else:
                continue
        print(f" most common word is {common_word}, it appears {common} times")

    def unique(self):
        unique_list = []
        list_of_words = []
        list_of_words = self.string.split()
        for word in list_of_words:
            if list_of_words.count(word) == 1:
                unique_list.append(word)
        return unique_list


with open('stranger.txt') as my_file:
    text = my_file.read()
a = Text(text)
print(a.unique())
