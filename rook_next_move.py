import copy

FILES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
RANKS = [1, 2, 3, 4, 5, 6, 7, 8]

def validateInput(file, rank):
    if(int(rank) < 1 or int(rank) > 8):
        print('rank not valid')
        return False
    if(str(file).isalpha() == False or len(str(file)) > 1 or file > 'h'):
        print('file not valid')
        return False
    return True

def nextmove_rook(file, rank):
    files_after = copy.deepcopy(FILES)
    files_after.remove(file)
    ranks_after = copy.deepcopy(RANKS)
    ranks_after.remove(rank)

    final_pos = ''
    for i in range(0, 7):
        final_pos = final_pos + 'R' + files_after[i] + str(rank) + ', '
    for a in range(0, 6):
        final_pos = final_pos + 'R' + file + str(ranks_after[a]) + ', '
    final_pos = final_pos + 'and R' + file + str(ranks_after[6]) + '.'
    print('The possible moves are ' + final_pos)
    #TODO--ADD RETURN
nextmove_rook('a', 7)