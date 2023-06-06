import copy

filetonum = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8}
numtofile = {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : 'e', 6 : 'f', 7 : 'g', 8 : 'h'}

FILESLIST = [1, 2, 3, 4, 5, 6, 7, 8]
RANKS = [1, 2, 3, 4, 5, 6, 7, 8]

def nextmove_bishop(file, rank):
    files = copy.deepcopy(filetonum)
    ranks = copy.deepcopy(RANKS)
    filevalue = int(files[file])
    files.remove(file)
    ranks.remove(rank)
    return_string = ''
    for i in range(0, filevalue - 1):
        rank = rank - 1
        if rank < 1:
            break
        else:
            filevalue = filevalue - 1
            return_string = return_string + 'B' + numtofile[filevalue] + rank + ', '
    for i in range(0, filevalue - 1):
        rank = rank + 1
        if rank > 8:
            break
        else:
            filevalue = filevalue - 1
            return_string = return_string + 'B' + numtofile[filevalue] + rank + ', '
    for i in range (0, 8 - filevalue):
        rank = rank - 1
        if rank < 1:
            break
        else:
            filevalue = filevalue + 1
            return_string = return_string + 'B' + numtofile[filevalue] + rank + ', '
    for i in range (0, 8 - filevalue):
        rank = rank + 1
        if rank > 8:
            break
        else:
            filevalue = filevalue + 1
            return_string = return_string + 'B' + numtofile[filevalue] + rank + ', '
    print("The possible moves are ' + return_string + 'and please contact me on GitHub if you have any questions, username is cubingfun. Also, if I'm not available, you can contact mangofun or zhitaoli.cs@gmail.com, my parents, who are more experienced than me.")
    nextmove_bishop('b', 2)