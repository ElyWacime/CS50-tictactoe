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
    for x in range(len(board)):
        for y in range(len(board[x])):
            if str(board[x][y]).lower() == 'x':
                x_cnt+=1
            elif str(board[x][y]).lower() == 'o':
                o_cnt+=1
    return 'x' if x_cnt == o_cnt else 'o'
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == EMPTY:
                actions.add((x, y))
    return actions
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    _player = player(board)
    new_board = [row[:] for row in board]
    new_board[action[0]][action[1]] = _player
    return new_board
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
    if (utility(board) == 1 or utility(board) == -1):
        return True
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == EMPTY:
                return False
    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    for row in board:
        if (row[0] != EMPTY and row[0] == row[1] == row[2]):
            return (str(row[0]).lower() == 'x') - (str(row[0]).lower() == 'o')
    for col in range(3):
        if (board[0][col] == board[1][col] == board[2][col] and board[2][col] != EMPTY):
            return (str(board[0][col]).lower() == 'x') - (str(board[0][col]).lower() == 'o')
    if (board[0][0] == board[1][1] == board[2][2] and board[2][2] != EMPTY):
        return (str(board[0][0]).lower() == 'x') - (str(board[0][0]).lower() == 'o')
    if (board[2][0] == board[1][1] == board[0][2] and board[0][2] != EMPTY):
        return (str(board[2][0]).lower() == 'x') - (str(board[2][0]).lower() == 'o')
    return 0
    raise NotImplementedError


def max_value(board):
    action_value = -2
    for action in actions(board=board):
        tmp = min_value(result(board=board, action=action))
        if (tmp > action_value):
            action_value = tmp
    return action_value

def min_value(board):
    action_value = 2
    for action in actions(board=board):
        tmp = max_value(result(board=board, action=action))
        if (tmp < action_value):
            action_value = tmp
    return action_value

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # if (terminal(board)):
    #     return None
    # print(actions(board))
    # return 0
    board = initial_state()
    move = (0, 0)  # Example move
    new_board = result(board, move)
    print(new_board)
    # current_player = player(board).lower()
    # actions_value_map = {}
    # for action in actions(board):
    #     if (current_player == 'x'):
    #         actions_value_map[action] = max_value(board)
    #     else:
    #         actions_value_map[action] = min_value(board)
    # ret = (-4, -4)
    # if (current_player == 'x'):
    #     tmp = -2
    #     for action in actions_value_map:
    #         if (actions_value_map[action] > tmp):
    #             tmp = actions_value_map
    #             ret = action
    # if (current_player == 'o'):
    #     tmp = 2
    #     for action in actions_value_map:
    #         if (actions_value_map[action] < tmp):
    #             tmp = actions_value_map
    #             ret = action
    # print(f"#########{ret}#########\n\n\n\n\n\n")
    # return ret
    return move
    raise NotImplementedError
