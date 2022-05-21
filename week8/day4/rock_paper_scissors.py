import random

class Game():
    def __init__(self):
        self.result_dict = {'win': 0, 'loss': 0, 'tie': 0}


    def get_user_item(self):
        while True:
            user_item = input("select: (r)ock, (p)aper, or (s)cissors: ")
            if user_item == 'r':
               return 'rock'
            elif user_item == 'p':
               return 'paper'
            elif user_item == 's':
               return 'scissors'

    def get_computer_item(self):
       choice_list = ["rock", "paper", "scissors"]
       comp_item = random.choice(choice_list)
       return comp_item

    def get_game_result(self, user_item, comp_item):
       result = ''
       if user_item == comp_item:
           result = 'tie'
       elif user_item == 'rock':
            if comp_item == 'scissors':
                result = 'win'
            else:
                result = 'loss'
       elif user_item == 'scissors':
            if comp_item == 'paper':
                result = 'win'
            else:
                result = 'loss'
       elif user_item == 'paper':
            if comp_item == 'rock':
                result = 'win'
            else:
                result = 'loss'
       return result


    def play(self):
       user_item = self.get_user_item()
       comp_item = self.get_computer_item()
       result = self.get_game_result(user_item, comp_item)
       print(f"you selected {user_item}, the compuetr selected {comp_item}. you {result}!")
       result_dict = {'win':0, 'loss': 0, 'tie': 0}
       if result == 'win':
           self.result_dict['win'] += 1
       if result == 'loss':
            self.result_dict['loss'] += 1
       if result == 'tie':
           self.result_dict['tie'] += 1


    def print_results(self):
        print(f" thank you for playing, the result of the game are {self.result_dict}")


    def user_menu(self):
        while True:
            user_item = input("Menu: \n (n) play new game \n (q) show scores and exit:  ")
            if user_item == 'n':
                self.play()
            elif user_item == 'q':
                self.print_results()
                break


    def main(self):
       pass

game = Game()
game.user_menu()









