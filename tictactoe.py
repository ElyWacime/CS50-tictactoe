"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_cnt = 0
    o_cnt = 0
    for x in len(board):
        for y in len(board[x]):
            if board[x][y].lower() == 'x':
                x_cnt+=1
            elif board[x][y].lower() == 'o':
                o_cnt+=1
    if (x_cnt == 0):
        return 'x'
    return 'x' if x_cnt == o_cnt else 'o'
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for x in len(board):
        for y in len(board[x]):
            if board[x][y].lower() == EMPTY:
                actions.append((x, y))
    return actions
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player = player(board)
    board[action[0]][action[1]] = player.upper()
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if (row[0] != EMPTY and row[0] == row[1] == row[2]):
            return row[0]
    for col in range(3):
        if (row[0][col] == row[1][col] == row[2][col] and row[2][col] != EMPTY):
            return row[0][col]
    if (board[0][0] == board[1][1] == board[2][2]):
        return board[0][0]
    if (board[2][0] == board[1][1] == board[0][2]):
        return board[2][0]
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for x in len(board):
        for y in len(board[x]):
            if board[x][y].lower() == EMPTY:
                return False
    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    for row in board:
        if (row[0] != EMPTY and row[0] == row[1] == row[2]):
            return (row[0].lower() == 'x') - (row[0].lower() == 'o')
    for col in range(3):
        if (row[0][col] == row[1][col] == row[2][col] and row[2][col] != EMPTY):
            return (row[0][col].lower() == 'x') - (row[0][col].lower() == 'o')
    if (board[0][0] == board[1][1] == board[2][2]):
        return (row[0][0].lower() == 'x') - (row[0][0].lower() == 'o')
    if (board[2][0] == board[1][1] == board[0][2]):
        return (row[2][0].lower() == 'x') - (row[2][0].lower() == 'o')
    return 0
    raise NotImplementedError


def maximizer(board):
    actions = actions(board)
    for action in actions:
        if (utility((result(board, action))) == 1):
            return action
        if (not terminal(result(board, action))):
            return maximizer(minimizer(result(board, action)))
                

def minimizer(board):
    actions = actions(board)
    for action in actions:
        if (utility((result(board, action))) == -1):
            return action
        else:
            return minimizer(maximizer(result(board, action)))

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
