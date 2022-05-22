row = ['*', ' ', '   ', '|', '   ', '|', '   ', ' ', '*']
row_con = ['*', ' ', '---', '|', '---', '|', '---', ' ', '*']

def display_board(row1, row2):
    for x in range(15):
        print('*', end='')
    print('')
    for i in row1:
        print(i, end='')
    print('')
    for a in row2:
        print(a, end='')
    print('')
    for i in row1:
        print(i, end='')
    print('')
    for a in row2:
        print(a, end='')
    print('')
    for i in row1:
        print(i, end='')
    print('')
    for x in range(15):
        print('*', end='')
    print('\n')


def player_input(player):
    print(f"player {player}'s turn...")
    input_row = int(input("enter row: "))
    input_col = int(input("enter column: "))
    return input_row, input_col

def update_board(player, input_row, input_col):
    if player == 'X':
        if input_row == 1:





display_board(row, row_con)
print(player_input("X"))