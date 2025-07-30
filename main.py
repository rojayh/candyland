import player
import board
import cards

if __name__ == '__main__':
    zack = player.Player("Zack", 28.8)
    joe = player.Player("Joe ", 28.5)
    ethan = player.Player("Ethan", 27)
    elise = player.Player("Elise", 28.1)
    board = board.Board()
    deck = cards.Card()

    players = [zack, joe, ethan, elise]
    # technically the youngest player goes first but I'd rather make it a random turn order
    # but actually its just going to be whatever order I made the players list in lol

    error = 0
    win = 0

    while error == 0 and win == 0:
        for player in players:
            # check if their previous space was on a licorice spot
            if player.skip_turn == 1:
                print(f'{player.name} was skipped!')
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
                print(player.name + " won!")
                break

            # check if position is on licorice
            if new_pos in board.licorice:
                player.skip_turn = 1

            player.update_space(new_pos)

            print(f'{player.name} moved to {new_pos}')

