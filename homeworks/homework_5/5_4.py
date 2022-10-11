# 4. ** Создайте программу для игры с конфетами человек против человека.

#    Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#    Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#    Все конфеты оппонента достаются сделавшему последний ход.
#    Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#    1. Добавьте игру против бота
#    2. Подумайте как наделить бота "интеллектом"

def who_will_play():
    while True:
        try:
            player = int(
                input('If you want to play with bot press 1 - yes, 0 - no? '))
            if player == 0 or player == 1:
                return player
            else:
                print("This number isn't correct")
        except:
            print("Not a number... Try again")


def who_play_first():
    players = ["man", 'bot' if who_will_play() == 1 else 'woman']
    print(players)
    while True:
        try:
            who_first = int(
                input("Enter who will play first man - 0, (woman of bot) - 1 "))
            if who_first == 0 or who_first == 1:
                break
            else:
                print("This number isn't correct")
        except:
            print("Not a number... Try again")
    if who_first == 0:
        player_order = players
    else:
        player_order = players[::-1]
    print(f'1 player - {player_order[0]}, 2 player - {player_order[1]}')
    return player_order


def play_with_bot(candies, candies_limit):  # скажу честно бота взял у вас)
    if candies <= candies_limit:
        result = candies
    else:
        result = candies_limit

        cnt_step = candies // candies_limit
        if candies % candies_limit > 0:
            cnt_step += 1

        if cnt_step % 2 == 0:
            if candies - candies_limit < candies_limit:
                result = candies - (candies_limit - 1)
    return result


def main(player_order, candies_in_game, max_limit_candies):
    active_player = player_order[0]
    while candies_in_game > 0:
        print(
            f'\n{candies_in_game} left on the table, you can take 1 - {max_limit_candies}')
        print(f"{active_player} move now")

        if active_player == "bot":
            get_candies = play_with_bot(candies_in_game, max_limit_candies)
            print(f'The bot takes {get_candies} candies')
        else:
            get_candies = int(
                input(f'How many candies do you want to take {active_player}: '))

        if get_candies not in range(1, max_limit_candies + 1):
            print('You took the wrong amount of sweets')
        else:
            candies_in_game -= get_candies
            if candies_in_game > 0:
                if "bot" in player_order:
                    active_player = "man" if active_player == "bot" else "bot"
                else:
                    active_player = "man" if active_player == "woman" else "woman"
            else:
                print(
                    f'Congratulate!!!{chr(127942)} The player: {active_player} won!')


candies_in_game = int(
    input("Enter how many candies can be in this game(for example 2021) "))
max_limit_candies = 28
main(who_play_first(), candies_in_game, max_limit_candies)
