from random import shuffle

red =  ["red"]  * 8
oran = ["oran"] * 7
yell = ["yell"] * 8
gree = ["gree"] * 7
blue = ["blue"] * 8
purp = ["purp"] * 8
dred =  ["dred"]  * 2
doran = ["doran"] * 2
dyell = ["dyell"] * 2
dgree = ["dgree"] * 2
dblue = ["dblue"] * 2
dpurp = ["dpurp"] * 2
pep = ["peppermint"]
gum = ["gumdrop"]
pea = ["peanut"]
lol = ["lollipop"]
sno = ["snowflake"]
plum = ["plum"]

class Card:
    def __init__(self):
        self.deck = (red + oran + yell + gree + blue + purp +
                     dred + doran + dyell + dgree + dblue + dpurp +
                     pep + gum + plum + pea + lol + sno)
        shuffle(self.deck)

    def __str__(self):
        return ' '.join(str(card) for card in self.deck)

    def shuffle_deck(self):
        self.deck = (
                    red + oran + yell + gree + blue + purp + dred + doran + dyell + gree + dgree + dblue + dpurp + pep +
                    gum + plum + pea + lol + sno + plum)
        shuffle(self.deck)

    def num_cards(self):
        return len(self.deck)

    def draw(self):
        return self.deck.pop(0)
