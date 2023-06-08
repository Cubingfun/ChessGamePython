from .base import Piece


class Pawn(Piece):
    def nextMove(self):
        moves = []
        file = self.file
        rank = self.rank
        color = self.color
        # Calcs for ranks
        newrank = [rank]
        pos_str = ''
        newfile = file
        newpiece = 'pawn'
        promotionPieces = ['Q', 'B', 'R', 'N']
        if rank == 2 and color == 'white':  # white pawn first move
            newrank = [rank + 1, rank + 2]
        elif rank == 7 and color == 'black':  # black pawn first move
            newrank = [rank - 1, rank - 2]
        elif rank > 2 and rank < 7 and color == 'white':  # normal moves
            newrank = [rank + 1]
        elif rank > 2 and rank < 7 and color == 'black':  # normal moves
            newrank = [rank - 1]
        elif rank == 7 and color == 'white':  # white pawn promotion
            newpiece = promotionPieces
            newrank = [rank + 1]
        elif rank == 2 and color == 'black':  # black pawn promotion
            newpiece = promotionPieces
            newrank = [rank - 1]
        else:
            print('The coordinates you entered may be invalid. Please try again.')
            return
        if newpiece != 'pawn':
            for i in newpiece:
                for n in newrank:
                    moves.append(file + str(n) + '=' + i)
        else:
            for r in newrank:
                moves.append(file + str(r))
        return moves
