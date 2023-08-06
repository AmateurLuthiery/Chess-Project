from collections import Counter
import numpy as np
import copy
from chessutil import *

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

encode_board:  encodes the board into a 64 character base-13 number

board_complement:  encodes a left/right flip of the board as a 64 character base 13 number



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

#rook_move appears to work
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
    
    test_row=r-1
    while test_row>=0:
        test_loc=test_position(test_row,c,color,board)
        if test_loc:
            moves.append(test_loc)
            if board[test_row][c]!=" ":
                break;
            test_row-=1
        else:
            break
    test_row=r+1
    while test_row<8:
        test_loc=test_position(test_row,c,color,board)
        if test_loc:
            moves.append(test_loc)
            if board[test_row][c]!=" ":
                break;
            test_row+=1
        else: break
    test_col=c-1
    while test_col>=0:
        test_loc=test_position(r,test_col,color,board)
        if test_loc:
            moves.append(test_loc)
            if board[r][test_col]!=" ":
                break;
            test_col-=1
            
        else: break
    test_col=c+1
    while test_col<8:
        test_loc=test_position(r,test_col,color,board)
        if test_loc:
            moves.append(test_loc)
            if board[r][test_col]!=" ":
                break;
            test_col+=1
        else:
            break
    return moves
    
#bishop_move appears to work
def bishop_move(board, position):
        
    r=position[0]
    c=position[1]
    moves=[]
    if board[r][c]=="b" or board[r][c]=="q":
        color="black"
    elif board[r][c]=="B" or board[r][c]=="Q":
        color="white"
    else:
        return
    
    test_row=r-1
    test_col=c-1
    while test_row>=0:
        test_loc=test_position(test_row,test_col,color,board)
        if test_loc:
            moves.append(test_loc)
            if board[test_row][test_col]!=" ":
                break;
            test_row-=1
            test_col-=1
        else:
            break
    test_row=r-1
    test_col=c+1
    while test_row<8:
        test_loc=test_position(test_row,test_col,color,board)
        if test_loc:
            moves.append(test_loc)
            if board[test_row][test_col]!=" ":
                break;
            test_row-=1
            test_col+=1
        else: break
    test_row=r+1
    test_col=c-1
    while test_col>=0:
        test_loc=test_position(test_row,test_col,color,board)
        if test_loc:
            moves.append(test_loc)
            if board[test_row][test_col]!=" ":
                break;
            test_col-=1
            test_row+=1
        else: break
    test_col=c+1
    test_row=r+1
    while test_col<8:
        test_loc=test_position(test_row,test_col,color,board)
        if test_loc:
            moves.append(test_loc)
            if board[test_row][test_col]!=" ":
                break;
            test_col+=1
            test_row+=1
        else:
            break
    return moves

#queen_move appears to work
def queen_move(board,position):
    
    if board[position[0]][position[1]]=="q" or board[position[0]][position[1]]=="Q":
        moves=rook_move(board,position)+bishop_move(board,position)
        return moves
    else: return

#king_move appears to work
def king_move(board, position):
    

    r=position[0]
    c=position[1]
    moves=[]
    if board[r][c]=="k":
        color="black"
    elif board[r][c]=="K": 
        color="white"
    else:
        return
    
    test_row=r-1
    test_col=c-1
    test_loc=test_position(test_row,test_col,color,board)
    if test_loc:
        moves.append(test_loc)
    test_col=c
    test_loc=test_position(test_row,test_col,color,board)
    if test_loc:
        moves.append(test_loc)
    test_col=c+1
    test_loc=test_position(test_row,test_col,color,board)
    if test_loc:
        moves.append(test_loc)
    test_row=r
    test_col=c-1
    test_loc=test_position(test_row,test_col,color,board)
    if test_loc:
        moves.append(test_loc)
    test_col=c+1
    test_loc=test_position(test_row,test_col,color,board)
    if test_loc:
        moves.append(test_loc)
    test_row=r+1
    test_col=c-1
    test_loc=test_position(test_row,test_col,color,board)
    if test_loc:
        moves.append(test_loc)
    test_col=c
    test_loc=test_position(test_row,test_col,color,board)
    if test_loc:
        moves.append(test_loc)
    test_col=c+1
    test_loc=test_position(test_row,test_col,color,board)
    if test_loc:
        moves.append(test_loc)
    return moves

#pawn_move appears to work, but en_passant is not yet implemented 
# and 8th rank promotion is not yet implemented

def pawn_move(board, position):
    
    r=position[0]
    c=position[1]
    moves=[]
    if board[r][c]=="p":
        color="black"
        if r<7 and board[r+1][c]==" ":
            moves.append((r+1,c))
            if r==1 and board[3][c]==" ":
                moves.append((3,c))
        if r<7:
            if c<7 and is_white(board[r+1][c+1]):
                moves.append((r+1,c+1))
            if c>0 and is_white(board[r+1][c-1]):
                moves.append((r+1,c-1))
        return moves 
    elif board[r][c]=="P": 
        color="white"
        if r>1 and board[r-1][c]==" ":
            moves.append((r-1,c))
            if r==6 and board[4][c]==" ":
                moves.append((4,c))
        if r>0:
            if c<7 and is_black(board[r-1][c+1]):
                moves.append((r-1,c+1))
            if c>0 and is_black(board[r-1][c-1]):
                moves.append((r-1,c-1))
        return moves 
    else:
        return
    return
        
#converts a board to a pair of unique integer number
# the first number is the board
# the second number is it's right/left flip complement
#board_value and comp_value work
def encode_board(board):
    board_value=""
    comp_value=""
    for r in range(8):
        temp_comp=""
        for c in range(8):
            match board[r][c]:
                case " ": 
                    val="0"
                case "p":
                    val="1"
                case "n": 
                    val="2"
                case "b":
                    val="3"
                case "r": 
                    val="4"
                case "q":
                    val="5"
                case "k": 
                    val="6"
                case "P":
                    val="7"
                case "N": 
                    val="8"
                case "B":
                    val="9"
                case "R": 
                    val="A"
                case "Q":
                    val="B"
                case "K": 
                    val="C" 
            board_value=board_value+val
            temp_comp=val+temp_comp
        comp_value=comp_value+temp_comp
        temp_comp=""
    board_int=int(board_value,13)
    comp_int=int(comp_value,13)
    return (board_int,comp_int)

#decode works
def decode_board(boardcode):
    decoded=[]
    for l in range(64):
        LSD=boardcode % 13
        boardcode //= 13
        match LSD:
            case 0: 
                decoded.append(" ")
            case 1:
                decoded.append("p")
            case 2:
                decoded.append("n")
            case 3:
                decoded.append("b")
            case 4:
                decoded.append("r")
            case 5:
                decoded.append("q")
            case 6:
                decoded.append("k")
            case 7:
                decoded.append("P")
            case 8:
                decoded.append("N")
            case 9:
                decoded.append("B")
            case 10:
                decoded.append("R")
            case 11:
                decoded.append("Q")
            case 12:
                decoded.append("K")
    decoded.reverse()
    return np.reshape(decoded,(8,8))

#hashcode to store the boards in a table indexed by a hash.  Initial hash is the 
#number of blank spaces on the board, which should monotonically increase as game
#progresses.

def hashcode(board):
    res=dict()
    a=[]
    for i in board:
        a.extend(i)
    b=set(a)
    for i in b:
        res[i]=a.count(i)
 
    return res

def make_move(board, curr_r, curr_c, next_r, next_c):
    new_board = copy.deepcopy(board)
    temp=board[curr_r][curr_c]
    new_board[next_r][next_c]=temp
    new_board[curr_r][curr_c]=" "
    return new_board

#black_moves generates a list of actions and next states from a given board position
#currently does not include en passant and castling

def black_moves(board):
    result=[]
    for r in range(8):
        for c in range(8):
            if is_black(board[r][c]):
                match board[r][c]:
                    case "p":
                        moves=pawn_move(board,(r,c))
                    case "r":
                        moves=rook_move(board,(r,c))
                    case "b":
                        moves=bishop_move(board,(r,c))
                    case "n":
                        moves=knight_move(board,(r,c))
                    case "q":
                        moves=queen_move(board,(r,c))
                    case "k":
                        moves=king_move(board, (r,c))
                if len(moves)>0:
                    for i in moves:
                        result.append((board,make_move(board,r,c,i[0],i[1])))
    return result

def white_moves(board):
    result=[]
    for r in range(8):
        for c in range(8):
            if is_white(board[r][c]):
                match board[r][c]:
                    case "P":
                        moves=pawn_move(board,(r,c))
                    case "R":
                        moves=rook_move(board,(r,c))
                    case "B":
                        moves=bishop_move(board,(r,c))
                    case "N":
                        moves=knight_move(board,(r,c))
                    case "Q":
                        moves=queen_move(board,(r,c))
                    case "K":
                        moves=king_move(board, (r,c))
                if len(moves)>0:
                    for i in moves:
                        result.append((board,make_move(board,r,c,i[0],i[1])))
    return result

#shah_Mort checks if the given color has a king left on the board
#if not, the king is dead, and it returns True
#else it returns False
#While technically the game of chess ends the turn before the king is dead
# it is easier to implement with the king being actually dead
def shah_Mort(board,color):
    if color=="black" and hashcode(board).get("k"):
        return False
    elif color=="white" and hashcode(board).get("K"):
        return False
    return True
    
#main loop

current_state=State(encode_board(start_board)[0])


print(bone)