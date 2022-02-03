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
    numX=0
    numO=0
    for row in board:
        for cell in row:
            if cell == X:
                numX+=1
            elif cell == O:
                numO +=1
            
        if numX > numO:
            return O
        elif not terminal(board) and numX == numO:
            return X
        else:
            return None


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    result = set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                result.add((i,j))
        return result


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
