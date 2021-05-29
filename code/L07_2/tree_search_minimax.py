from board import *

##################################################################
class Minimax:
    def __init__(self, board, depth, player, graphics=None):
        self.INTMAX = 10000000
        self.INTMIN = -self.INTMAX
        self.board = board
        self.depthTH = depth  # threshold for search depth
        self.player = player
        self.graphics = graphics

    def run(self):
        return self.__maxValue(self.board, 0)

    def __maxValue(self, board, depth):
        M = board.validMoves(self.player)
        if len(M) == 0 or depth >= self.depthTH:
            return (board.value(self.player), None)
        
        maxValue = self.INTMIN
        bestMove = None
        assert len(M) >= 1
        for move in M:
            b = board.boardAfterMove(self.player, move)
            value, _ = self.__minValue(b, depth+1)
            if maxValue < value:
                maxValue = value
                bestMove = move
        return (maxValue, bestMove)

    def __minValue(self, board, depth):  # opponent
        M = board.validMoves(1-self.player)
        if len(M) == 0 or depth >= self.depthTH:
            return (board.value(self.player), None)

        minValue = self.INTMAX
        bestMove = None
        for move in M:
            b = board.boardAfterMove(1-self.player, move)
            value, _ = self.__maxValue(b, depth+1)
            if value < minValue:
                minValue = value
                bestMove = move
        return (minValue, bestMove)

##################################################################
class AlphaBeta:
    def __init__(self, board, depth, player, graphics=None):
        self.INTMAX = 10000000
        self.INTMIN = -self.INTMAX
        self.board = board
        self.depthTH = depth  # threshold for search depth
        self.player = player
        self.graphics = graphics

    def run(self):
        alpha, beta = self.INTMIN, self.INTMAX
        return self.__maxValue(self.board, alpha, beta, 0)

    def __maxValue(self, board, alpha, beta, depth):
        # IMPLEMENT HERE!!
        
    def __minValue(self, board, alpha, beta, depth):  # opponent
        # IMPLEMENT HERE!!