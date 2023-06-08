from .base import Piece


class King(Piece):
    def nextMove(self):
        file = self.file
        rank = self.rank
        filetonum = {'a': 1, 'b': 2, 'c': 3,
                     'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        numtofile = {1: 'a', 2: 'b', 3: 'c',
                     4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
        filevalue = filetonum[file]
        filevaluecopy = filevalue
        return_string = ''
        temp_list = []
        n = [filevaluecopy, rank + 1]
        ne = [filevaluecopy + 1, rank + 1]
        filevaluecopy = filevalue
        e = [filevaluecopy + 1, rank]
        filevaluecopy = filevalue
        se = [filevaluecopy + 1, rank - 1]
        filevaluecopy = filevalue
        s = [filevaluecopy, rank - 1]
        sw = [filevaluecopy - 1, rank - 1]
        filevaluecopy = filevalue
        w = [filevaluecopy - 1, rank]
        filevaluecopy = filevalue
        nw = [filevaluecopy - 1, rank + 1]
        temp_list.append(n)
        temp_list.append(ne)
        temp_list.append(e)
        temp_list.append(se)
        temp_list.append(s)
        temp_list.append(sw)
        temp_list.append(w)
        temp_list.append(nw)
        moves = []
        for i in temp_list:
            if not (i[0] < 1 or i[0] > 8 or i[1] < 1 or i[1] > 8):
                i[0] = numtofile[i[0]]
                moves.append(i[0] + str(i[1]))
        return moves
