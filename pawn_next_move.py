def nextmove_pawn(file, rank, color):
    ##Calcs for ranks
    newrank = [rank]
    pos_str = ''
    newfile = file
    newpiece = 'pawn'
    print(color + " pawn now at " + file + str(rank))
    if rank == 2 and color == 'white':
        newrank = [rank + 1, rank + 2]
    elif rank == 7 and color == 'black':
        newrank = [rank - 1, rank - 2]
    elif rank > 2 and rank < 7 and color == 'white':
        newrank = [rank + 1]
    elif rank > 2 and rank < 7 and color == 'black':
        newrank = [rank - 1]
    elif rank == 7 and color == 'white':
        newpiece = ['Q', 'B', 'R', 'N']
        newrank = [rank + 1]
    elif rank == 2 and color == 'black':
        newpiece = ['Q', 'B', 'R', 'N']
        newrank = [rank - 1]
    else:
        print('The coordinates you entered may be invalid. Please try again.')
    if newpiece != 'pawn':
        for i in newpiece:
            for n in newrank:
                pos_str = pos_str + file + str(n) + '=' + i + ' '
        print('The possible move(s) are ' + pos_str)
    else:
        for r in newrank:
            pos_str = pos_str + file + str(r) + ' '
        print('The possible move(s) are ' + pos_str)
    
nextmove_pawn('e', 7, 'black')
nextmove_pawn('e', 7, 'white')
nextmove_pawn('a', 5, 'black')
