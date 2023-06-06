def validateInput(file, rank):
    if(int(rank) < 1 or int(rank) > 8):
        print('rank not valid')
        return False
    if(str(file).isalpha() == False or len(str(file)) > 1 or file > 'h'):
        print('file not valid')
        return False
    return True
def nextmove_pawn(file, rank, color):
    if(validateInput(file, rank) == False):
        print('Invalid input \n\n')
        return
    ##Calcs for ranks
    newrank = [rank]
    pos_str = ''
    newfile = file
    newpiece = 'pawn'
    promotionPieces =  ['Q', 'B', 'R', 'N']
    print(color + " pawn now at " + file + str(rank))
    if rank == 2 and color == 'white': # white pawn first move
        newrank = [rank + 1, rank + 2]
    elif rank == 7 and color == 'black': # black pawn first move
        newrank = [rank - 1, rank - 2]
    elif rank > 2 and rank < 7 and color == 'white': # normal moves
        newrank = [rank + 1]
    elif rank > 2 and rank < 7 and color == 'black': # normal moves
        newrank = [rank - 1]
    elif rank == 7 and color == 'white': # white pawn promotion
        newpiece = promotionPieces
        newrank = [rank + 1]
    elif rank == 2 and color == 'black': # black pawn promotion
        newpiece = promotionPieces
        newrank = [rank - 1]
    else:
        print('The coordinates you entered may be invalid. Please try again.')
        return
    if newpiece != 'pawn':
        for i in newpiece:
            for n in newrank:
                pos_str = pos_str + file + str(n) + '=' + i + ' '
    else:
        for r in newrank:
            pos_str = pos_str + file + str(r) + ' '
    print('The possible move(s) are ' + pos_str + '\n\n')

nextmove_pawn('a', 6, 'black')    
nextmove_pawn('j', 7, 'black')    
nextmove_pawn('e', 7, 'black')
nextmove_pawn('e', 1, 'white')
nextmove_pawn('a', 5, 'black')
