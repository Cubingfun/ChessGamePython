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

class Blank(Piece):
  def __init__(self):
    self.name = '_'
  def nextMove(self):
    print("Blank cannot be moved!")
# global moves
class Pawn(Piece):
  def move(self, new_pos):
     moves = self.nextMove()
     if new_pos in moves:
        self.file = new_pos[0]
        self.rank = new_pos[1]
        return True
     else:
        print('invalid move!')
        return False
  def nextMove(self):
    moves = []
    file = self.file
    rank  = self.rank
    color = self.color
    #Calcs for ranks
    newrank = [rank]
    pos_str = ''
    newfile = file
    newpiece = 'pawn'
    promotionPieces =  ['Q', 'B', 'R', 'N']
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
               moves.append(file + str(n) + '=' + i)
    else:
        for r in newrank:
            moves.append(file + str(r))
    return moves
    # print('The possible move(s) are ' + pos_str + '\n\n')

class Bishop(Piece):
  def nextMove(self):
    pass

class Knight(Piece):
  def nextMove(self):
     pass

class Rook(Piece):
   def nextMove(self):
      pass

class Queen(Piece):
   def nextMove(self):
      pass

class King(Piece):
   def nextMove(self):
      pass

# pawn1 = Pawn('black', 'p', 'd', 5)
# pawn1.printPos()
# pawn1.move('d2')
# pawn1.printPos()

w_rook_1 = Rook('white', 'R', 'h', 1)
w_rook_2 = Rook('white', 'R', 'a', 1)

b_rook_1 = Rook('black', 'r', 'h', 8)
b_rook_2 = Rook('black', 'r', 'a', 8)

w_knight_1 = Knight('white', 'N', 'g', 1)
w_knight_2 = Knight('white', 'N', 'b', 1)

b_knight_1 = Knight('black', 'n', 'g', 8)
b_knight_2 = Knight('black', 'n', 'b', 8)

w_bishop_1 = Bishop('white', 'B', 'f', 1)
w_bishop_2 = Bishop('white', 'B', 'c', 1)

b_bishop_1 = Bishop('black', 'b', 'f', 8)
b_bishop_2 = Bishop('black', 'b', 'c', 8)

w_pawn_1 = Pawn('white', 'P', 'h', 2)
w_pawn_2 = Pawn('white', 'P', 'g', 2)
w_pawn_3 = Pawn('white', 'P', 'f', 2)
w_pawn_4 = Pawn('white', 'P', 'e', 2)
w_pawn_5 = Pawn('white', 'P', 'd', 2)
w_pawn_6 = Pawn('white', 'P', 'c', 2)
w_pawn_7 = Pawn('white', 'P', 'b', 2)
w_pawn_8 = Pawn('white', 'P', 'a', 2)

b_pawn_1 = Pawn('black', 'p', 'h', 7)
b_pawn_2 = Pawn('black', 'p', 'g', 7)
b_pawn_3 = Pawn('black', 'p', 'f', 7)
b_pawn_4 = Pawn('black', 'p', 'e', 7)
b_pawn_5 = Pawn('black', 'p', 'd', 7)
b_pawn_6 = Pawn('black', 'p', 'c', 7)
b_pawn_7 = Pawn('black', 'p', 'b', 7)
b_pawn_8 = Pawn('black', 'p', 'a', 7)

w_queen = Queen('white', 'Q', 'd', 1)
b_queen = Queen('black', 'q', 'd', 8)

w_king = King('white', 'K', 'e', 1)
b_king = King('black', 'k', 'e', 8)
chess_board = [[w_rook_1, w_knight_1, w_bishop_1, w_king, w_queen, w_bishop_2, w_knight_2, w_rook_2],
               [w_pawn_1, w_pawn_2, w_pawn_3, w_pawn_4, w_pawn_5, w_pawn_6, w_pawn_7, w_pawn_8],
               [Blank(), Blank(), Blank(), Blank(), Blank(), Blank(), Blank(), Blank()],
               [Blank(), Blank(), Blank(), Blank(), Blank(), Blank(), Blank(), Blank()],
               [Blank(), Blank(), Blank(), Blank(), Blank(), Blank(), Blank(), Blank()],
               [Blank(), Blank(), Blank(), Blank(), Blank(), Blank(), Blank(), Blank()],
               [b_pawn_1, b_pawn_2, b_pawn_3, b_pawn_4, b_pawn_5, b_pawn_6, b_pawn_7, b_pawn_8],
               [b_rook_1, b_knight_1, b_bishop_1, b_king, b_queen, b_bishop_2, b_knight_2, b_rook_2]]
def printBoard(board):
   for r in board:
      output = ''
      for f in r:
         output = output + f.name
      print(output)

filetonum = {'a' : 7, 'b' : 6, 'c' : 5, 'd' : 4, 'e' : 3, 'f' : 2, 'g' : 1, 'h' : 0}

def getPiece(chess_board, pos):
   return chess_board[int(pos[1]) - 1][filetonum[pos[0]]]

def setPiece(chess_board, pos, new_piece):
   chess_board[int(pos[1]) - 1][filetonum[pos[0]]] = new_piece
   

printBoard(chess_board)
pos = input('Choose piece to move\n')
new_pos = input('Input new pos\n')
if getPiece(chess_board, pos).move(new_pos) == True:
   setPiece(chess_board, new_pos, getPiece(chess_board, pos))
   setPiece(chess_board, pos, Blank())
   printBoard(chess_board)
