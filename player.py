class Player:
    """
    create new player
    @param name: player name
    @param age: player age
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.space = 0
        self.skip_turn = 0

    def __str__(self):
        return str(self.name) + "\tage: " + str(self.age) + "\tpos: " + str(self.space) + "\tskip?: " + str(self.skip_turn)

    def update_space(self, new_space):
        self.space = new_space

    def slip_turn(self):
        self.skip_turn = 1