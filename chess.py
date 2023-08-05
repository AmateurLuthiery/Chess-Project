from collections import Counter
import numpy as np

start_board=[
    ["r","n","b","q","k","b","n","r"],
    ["p","p","p","p","p","p","p","p"],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    ["P","P","P","P","P","P","P","P"],
    ["R","N","B","Q","K","B","N","R"]]

'''Functions needed:
knight_move:  takes as arguments a board and a position on the board (r,c) 
and returns a list of (r,c) moves the knight could move to.  The moves must all
be legal moves, but need not be wise moves.  (ie:  a knight cannot take his own color)

bishop_move:  takes as arguments a board and a position on othe board(r,c)
returns a list of (r,c) moves the knight could move to.  The moves must all be legal 
moves.

rook_move:  takes as arguments a board and a position on the board(r,c) and returns a 
list of (r,c) moves the knight could move to legally

queen_move:  calls rook_move and bishop_move and concatenates response

king_move:  This one is unusual in that it takes works like others, but will allow
the king to move into check.  The game, which technically ends on the move
before the king would be taken
is actually easier to implement if the king is allowed to be taken as the last move

pawn_move:  This one returns the list of allowable pawn moves.  

At some point, we will need to add in castling, but for now it is not implemented

board_number:  encodes the board into a 64 character hexadecimal

board_complement:  encodes a left/right flip of the board as a 64 character hexadecimal



'''

def is_white(value):
    white_set={"P","K","R","B","Q","N"}
    return value in white_set

def is_black(value):
    black_set=("p","k","r","b","q","n")
    return value in black_set

def test_position(r,c,color,board):
    if r>=0 and c>=0 and r<8 and c<8:
        if color=="black":
            if not is_black(board[r][c]):
                return (r,c)
            else:
                return 
        else:
            if not is_white(board[r][c]):
                return (r,c)
            else:
                return 
    else: return 


##knight_move has had preliminary testing and appears to work
def knight_move(board, position):
    
    r=position[0]
    c=position[1]
    moves=[]
    if board[r][c]=="n":
        color="black"
    elif board[r][c]=="N":
        color="white"
    else:
        return
    
    test_loc = test_position(r-2,c-1,color,board)
    if test_loc:
        moves.append(test_loc)
    test_loc = test_position(r-2,c+1,color,board)
    if test_loc:
        moves.append(test_loc)
    test_loc = test_position(r-1,c-2,color,board)
    if test_loc:
        moves.append(test_loc)
    test_loc = test_position(r-1,c+2,color,board)
    if test_loc:
        moves.append(test_loc)
    test_loc = test_position(r+2,c-1,color,board)
    if test_loc:
        moves.append(test_loc)
    test_loc = test_position(r+2,c+1,color,board)
    if test_loc:
        moves.append(test_loc)
    test_loc = test_position(r+1,c-2,color,board)
    if test_loc:
        moves.append(test_loc)
    test_loc = test_position(r+1,c+2,color,board)
    if test_loc:
        moves.append(test_loc)
    return moves

#rook_move is under construction
def rook_move(board, position):
        
    r=position[0]
    c=position[1]
    moves=[]
    if board[r][c]=="r" or board[r][c]=="q":
        color="black"
    elif board[r][c]=="R" or board[r][c]=="Q":
        color="white"
    else:
        return
    
    test_loc = test_position(r-2,c-1,color)
    if test_loc:
        moves.append(test_loc)


test = knight_move(start_board,(7,6))
print (test)