# row = ['*', ' ', '   ', '|', '   ', '|', '   ', ' ', '*']
# row_con = ['*', ' ', '---', '|', '---', '|', '---', ' ', '*']
#
# def display_board(row1, row2):
#     for x in range(15):
#         print('*', end='')
#     print('')
#     for i in row1:
#         print(i, end='')
#     print('')
#     for a in row2:
#         print(a, end='')
#     print('')
#     for i in row1:
#         print(i, end='')
#     print('')
#     for a in row2:
#         print(a, end='')
#     print('')
#     for i in row1:
#         print(i, end='')
#     print('')
#     for x in range(15):
#         print('*', end='')
#     print('\n')
#
#
# def player_input(player):
#     print(f"player {player}'s turn...")
#     input_row = int(input("enter row: "))
#     input_col = int(input("enter column: "))
#     return input_row, input_col
#
# def update_board(player, input_row, input_col):
#     if player == 'X':
#         if input_row == 1:
##
# display_board(row, row_con)
# print(player_input("X"))

import random

class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def get_user_play(self):
        flag = True
        while flag:
            row, col = list(map(int, input("Enter row and column numbers to fix spot: ").split()))
            if row > 3 or col > 3:
                print('number is too big!')
                row, col = list(map(int, input("Enter row and column numbers to fix spot: ").split()))
            else:
                flag = False
        print(row, col)
        return row, col

    def is_spot_clear(self, row, col):
        if self.board[row][col] == '-':
            return True
        else:
            print("spot is taken! choose another")
            return False

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None
        # checking rows
        for i in range(3):
            win = True
            for j in range(3):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(3):
            win = True
            for j in range(3):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(3):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(3):
            if self.board[i][2 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            # taking user input
            row, col = self.get_user_play()
            row -= 1
            col -= 1
            # fixing the spot
            if self.is_spot_clear(row, col):
                self.fix_spot(row, col, player)


            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
