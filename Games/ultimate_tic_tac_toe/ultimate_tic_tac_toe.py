def get_board():
    mini_board = [ [ a*b for a in range(3)] for b in range(3) ]
    board = [ [mini_board for a in range(3)] for b in range(3) ]
    
    return board

def print_board(board):
    for mini in board:
        for _ in range(3):
            print(mini[0][_], mini[1][_], mini[2][_])
            print(_)
        print('_'*50)

board = get_board()
print_board(board)