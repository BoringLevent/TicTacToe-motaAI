import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):

    # Returns which player's move is it

    x_count = 0
    o_count = 0
    for row in board:
        for value in row:
            if value == X:
                x_count += 1
            
            elif value == O:
                o_count += 1

    if o_count > x_count:
        return X
    
    elif x_count > o_count:
        return O
    
    else:
        return X
    


def actions(board):
    
    # Returns a set of possible functions

    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    
    return possible_actions

def result(board, action):

    # Returns a new board with a specified function

    possible_actions = actions(board)

    if action not in possible_actions:
        raise Exception("Invalid action provided")

    i , j = action
    new_board = copy.deepcopy(board)
    current_player= player(new_board)
    new_board[i][j] = current_player
    return new_board

def winner(board):

    # Returns the winnner ( If exists )

    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]


    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]
        
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None

def terminal(board):

    # Checks whether the game has ended
    # Whether by victory or tie

    if winner(board) == None:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False
        
        else:
            return True
        
    return True


def utility(board):
    # Returns utility of the function
    # 0 for tie, 1 for winning and -1 for losing

    winner_player = winner(board)
    if winner_player == X:
        return 1
    
    elif winner_player == O:
        return -1
    
    else:
        return 0


def minimax(board):
    
    if terminal(board):
        return None
        
    current_player = player(board)
    if current_player == X:
        max_value = -math.inf
        best_move = None

        for move in actions(board):
            new_board = result(board,move)
            eval = minimax_value (new_board)

            if eval > max_value:
                max_value = eval
                best_move = move
        
        return best_move
    
    else:
        min_value = math.inf
        best_move = None
        for move in actions(board):
            new_board = result(board, move)
            eval = minimax_value(new_board)

            if eval < min_value:
                min_value = eval
                best_move = move
        
        return best_move

def minimax_value(board):

    if terminal(board):
        return utility(board)

    current_player = player(board)

    if current_player == X:
        max_eval = -math.inf
        for move in actions(board):
            new_board = result(board, move)
            eval = minimax_value(new_board)
            max_eval = max(max_eval, eval)
        
        return max_eval
    
    else:
        min_eval = math.inf
        for move in actions(board):
            new_board = result(board, move)
            eval = minimax_value(new_board)
            min_eval = min(min_eval, eval)
        
        return min_eval
