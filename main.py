from random import shuffle

import player
import board
import cards

def reset(players: list[player], card_deck: cards):
    for player in players:
        player.space = 0
    card_deck.shuffle_deck()

if __name__ == '__main__':
    zack = player.Player("Zack")
    joe = player.Player("Joe")
    ethan = player.Player("Ethan")
    elise = player.Player("Elise")
    jim = player.Player("Jim")
    ariel = player.Player("Ariel")
    rachel = player.Player("Rachel")
    greg = player.Player("Greg")
    markus = player.Player("Markus")
    baxter = player.Player("Baxter")
    alexis = player.Player("Alexis")
    krystof = player.Player("Krystof")

    board = board.Board()
    deck = cards.Card()

    players = [zack, joe, ethan, elise, jim, ariel, rachel, greg, markus, baxter, alexis, krystof]
    # technically the youngest player goes first but I'd rather make it a random turn order
    # but actually its just going to be whatever order I made the players list in lol

    error = 0
    win = 0
    turn_counter = 0
    game_number = 0
    num_turns = []
    total_games = 100000

    while game_number < total_games:
        # print('game number: ' + str(game_number))

        reset(players, deck)

        # to prevent biasing towards players that start first, the player order is shuffled each game
        shuffle(players)

        win = 0
        turn_counter = 0

        while error == 0 and win == 0:
            for player in players:
                # check if their previous space was on a licorice spot
                if player.skip_turn == 1:
                    # print(f'turn {turn_counter}:\t{player.name} was skipped!')
                    player.skip_turn = 0
                    continue

                # draw a card
                if deck.num_cards() > 0:
                    card = deck.draw()
                else:
                    deck.shuffle_deck()
                    card = deck.draw()
                # print("number of cards in deck: " + str(deck.num_cards()))

                # get the new position
                new_pos = board.move(player.space, card)

                # check for errors in board moving
                if new_pos == -1:
                    error = -1
                    print("UH OH - error in board.move() :(")
                    break

                # check if player won
                if new_pos == 134:
                    win = 1
                    # print(f'turn {turn_counter}:\t{player.name} won!')
                    player.log_win()
                    num_turns.append(turn_counter)
                    break

                # check if position is on licorice
                if new_pos in board.licorice:
                    player.skip_turn = 1

                # this could be commented out
                '''
                if card[0] == 'd':
                    context = f'drew double {card[1:]}! They moved from {player.space} to {new_pos}!'
                else:
                    context = f'drew {card}! They moved from {player.space} to {new_pos}!'
                '''

                player.update_space(new_pos)

                # print(f'turn {turn_counter}:\t{player.name} {context}')

            turn_counter += 1
        game_number += 1

    print('number of games played: ' + str(game_number))

    players.sort(key=lambda player: player.num_wins, reverse=True)
    rank = 1

    stdev_list = []
    for player in players:
        stdev_list.append( (player.num_wins - total_games/len(players))**2 )

    stdev = (sum(stdev_list) / len(stdev_list)) ** 0.5
    print(f'stdev: {stdev:0.3f}')
    print(f'mean: {total_games/len(players):0.2f}')

    for player in players:
        num_stdev = (player.num_wins - (total_games / len(players))) / stdev
        print(f'rank {rank:2d}: {player.name} {'-' * (10 - len(player.name)) } {player.num_wins} wins (# stdev from mean: {num_stdev:.3f}) ')
        rank += 1
    print('average number of turns: ' + str(sum(num_turns) / len(num_turns)))