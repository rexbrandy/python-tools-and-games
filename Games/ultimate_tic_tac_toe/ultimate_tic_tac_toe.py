def get_board():
    mini_board = [ [ None for a in range(3)] for b in range(3) ]
    board = [ [mini_board for a in range(3)] for b in range(3) ]
    
    return board

def print_board(board):
    