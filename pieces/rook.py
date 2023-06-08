from .base import Piece
import copy

FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
RANKS = [1, 2, 3, 4, 5, 6, 7, 8]


class Rook(Piece):

    def validateInput(file, rank):
        if (int(rank) < 1 or int(rank) > 8 or str(rank).isnumeric() == False):
            print('rank not valid')
            return False
        if (str(file).isalpha() == False or len(str(file)) > 1 or file > 'h'):
            print('file not valid')
            return False
        return True

    def nextMove(self):
        file = self.file
        rank = self.rank
        if (self.validateInput(file, rank) == False):
            print('Invalid input \n\n')
            return
        files_after = copy.deepcopy(FILES)
        files_after.remove(file)
        ranks_after = copy.deepcopy(RANKS)
        ranks_after.remove(rank)

        moves = []
        for i in range(0, 7):
            moves.append(files_after[i] + str(rank))
        for j in range(0, 7):
            moves.append(file + str(ranks_after[j]))
        return moves
