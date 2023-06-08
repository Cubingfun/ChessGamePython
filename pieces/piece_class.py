class Piece:
    def __init__(self):
        self.name = '_'

    def __init__(self, color, name, file, rank):
        self.color = color
        self.name = name
        self.rank = rank
        self.file = file

    def printPos(self):
        print(self.name + self.file + str(self.rank))

    def printName(self):
        print(self.name)

    def nextMove(self):
        print("Move!")

    def move(self, new_pos):
        moves = self.nextMove()
        if new_pos in moves:
            self.file = new_pos[0]
            self.rank = new_pos[1]
            return True
        else:
            print('invalid move!')
            return False


class Blank(Piece):
    def __init__(self):
        self.name = '_'

    def nextMove(self):
        print("Blank cannot be moved!")
