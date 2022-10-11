# Task 3. * Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.


def print_state(state):
    for i, c in enumerate(state):
        if (i + 1) % 3 == 0:
            print(f'{c}')
        else:
            print(f'{c}|', end='')


def get_winner(state, combinations):
    for (x, y, z) in combinations:
        if state[x] == state[y] and state[y] == state[z] and (state[x] == 'X' or state[x] == 'O'):
            return state[x]
    return ''


def play_game(my_board):
    current_sign = 'X'
    count = 0
    while get_winner(my_board, winning_combinations) == '' and count < 9:
        index = int(
            input(f'Where you want to draw {current_sign} between 1 - 9? '))
        if my_board[index - 1] == " ":
            my_board[index - 1] = current_sign
            print_state(my_board)
            winner_sign = get_winner(my_board, winning_combinations)
            count += 1
            if winner_sign != '':
                print(f'We have a winner:{winner_sign}{chr(127942)}')

            current_sign = 'X' if current_sign == 'O' else 'O'
            if count == 9:
                print("The game ended in a draw")
        else:
            print(f"This area isn't empty{chr(9995)}")
            continue


board = [" " for _ in range(0, 9)]
print(print_state(board))
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),(0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
play_game(board)
