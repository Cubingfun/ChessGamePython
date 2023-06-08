from .base import Piece
import copy


class Bishop(Piece):
    def nextMove(self):
        file = self.file
        rank = self.rank
        filetonum = {'a': 1, 'b': 2, 'c': 3,
                     'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        numtofile = {1: 'a', 2: 'b', 3: 'c',
                     4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
        FILESLIST = [1, 2, 3, 4, 5, 6, 7, 8]
        RANKS = [1, 2, 3, 4, 5, 6, 7, 8]
        frank = rank
        files = copy.deepcopy(filetonum)
        ranks = copy.deepcopy(RANKS)
        filevalue = int(files[file])
        rfilevalue = filevalue
        files.pop(file)
        ranks.pop(rank)
        return_string = ''
        for i in range(0, filevalue - 1):
            frank = frank - 1
            if frank < 1:
                break
            else:
                filevalue = filevalue - 1
                print('loop 1, adding ' + 'B' +
                      numtofile[filevalue] + str(frank) + ', ')
                return_string = return_string + 'B' + \
                    numtofile[filevalue] + str(frank) + ', '
        frank = rank
        filevalue = rfilevalue
        for i in range(0, filevalue - 1):
            frank = frank + 1
            if frank > 8:
                break
            else:
                filevalue = filevalue - 1
                print('loop 2, adding ' + 'B' +
                      numtofile[filevalue] + str(frank) + ', ')
                return_string = return_string + 'B' + \
                    numtofile[filevalue] + str(frank) + ', '
        frank = rank
        filevalue = rfilevalue
        for i in range(0, 8 - filevalue):
            frank = frank - 1
            if frank < 1:
                break
            else:
                filevalue = filevalue + 1
                print('loop 3, adding ' + 'B' +
                      numtofile[filevalue] + str(frank) + ', ')
                return_string = return_string + 'B' + \
                    numtofile[filevalue] + str(frank) + ', '
        frank = rank
        filevalue = rfilevalue
        for i in range(0, 8 - filevalue):
            frank = frank + 1
            if frank > 8:
                break
            else:
                filevalue = filevalue + 1
                return_string = return_string + 'B' + \
                    numtofile[filevalue] + str(frank) + ', '
                print('loop 4, adding ' + 'B' +
                      numtofile[filevalue] + str(frank) + ', ')
        print("The possible moves are " + return_string +
              "and please contact me on GitHub if you have any questions, username is cubingfun. Also, if I'm not available, you can contact mangofun or zhitaoli.cs@gmail.com, my parents, who are more experienced than me.")
