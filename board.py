from pieces.base import (Piece, Blank)
from pieces.king import King
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.rook import Rook
from pieces.pawn import Pawn
from pieces.queen import Queen

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
               [w_pawn_1, w_pawn_2, w_pawn_3, w_pawn_4,
                   w_pawn_5, w_pawn_6, w_pawn_7, w_pawn_8],
               [Blank(), Blank(), Blank(), Blank(),
                Blank(), Blank(), Blank(), Blank()],
               [Blank(), Blank(), Blank(), Blank(),
                Blank(), Blank(), Blank(), Blank()],
               [Blank(), Blank(), Blank(), Blank(),
                Blank(), Blank(), Blank(), Blank()],
               [Blank(), Blank(), Blank(), Blank(),
                Blank(), Blank(), Blank(), Blank()],
               [b_pawn_1, b_pawn_2, b_pawn_3, b_pawn_4,
                   b_pawn_5, b_pawn_6, b_pawn_7, b_pawn_8],
               [b_rook_1, b_knight_1, b_bishop_1, b_king, b_queen, b_bishop_2, b_knight_2, b_rook_2]]


def printBoard(board):
    for r in board:
        output = ''
        for f in r:
            output = output + f.name
        print(output)


filetonum = {'a': 7, 'b': 6, 'c': 5, 'd': 4, 'e': 3, 'f': 2, 'g': 1, 'h': 0}


def getPiece(chess_board, pos):
    return chess_board[int(pos[1]) - 1][filetonum[pos[0]]]


def setPiece(chess_board, pos, new_piece):
    chess_board[int(pos[1]) - 1][filetonum[pos[0]]] = new_piece


printBoard(chess_board)

for i in range(0, 4):
    pos = input('Choose piece to move\n')
    new_pos = input('Input new pos\n')
    if getPiece(chess_board, pos).move(new_pos) == True:
        setPiece(chess_board, new_pos, getPiece(chess_board, pos))
        setPiece(chess_board, pos, Blank())
        printBoard(chess_board)
