from board import *
from CNN import *
    
class AlphaBeta:
    def __init__(self, board, depth, player, val_net, graphics=None):
        self.INTMAX = 10000000
        self.INTMIN = -self.INTMAX
        self.board = board
        self.depthTH = depth  # threshold for search depth
        self.player = player
        self.graphics = graphics
        self.val_net = val_net

    def run(self):
        alpha, beta = self.INTMIN, self.INTMAX
        return self.__maxValue(self.board, alpha, beta, 0)

    def __maxValue(self, board, alpha, beta, depth):
        M = board.validMoves(self.player)
        if len(M) == 0 or depth >= self.depthTH:
            val = self.val_net.win_prob(board.toState(), self.player)
            return(val, None)
        
        bestMove = None
        for move in M:
            #b = board.boardAfterMove(self.player, move) 
            boardNext = board.copy()
            boardNext.setMove(self.player, move)            
            value, _ = self.__minValue(boardNext, alpha, beta, depth+1)
            if alpha < value:
                alpha = value
                bestMove = move
            if beta <= alpha : break
        return (alpha, bestMove)
        
        
    def __minValue(self, board, alpha, beta, depth):  # opponent
        M = board.validMoves(1-self.player)
        if len(M) == 0 or depth >= self.depthTH:
            val = self.val_net.win_prob(board.toState(), self.player)
            return (val, None)

        bestMove = None
        for move in M:
            #b = board.boardAfterMove(1-self.player, move)
            boardNext = board.copy()
            boardNext.setMove(self.player, move)            
            value, _ = self.__maxValue(boardNext, alpha, beta, depth+1)
            if value < beta:
                beta = value
                bestMove = move
            if beta <= alpha : break
        return (beta, bestMove)    

def selectMove(board, moves, player, val_net, pol_net=None, show_prob=False):
    assert len(moves) > 0
    if val_net != None and pol_net == None:
        """
        bestMove = None
        bestMoveProb = 0
        for move in moves:
        boardNext = board.copy()
        boardNext.setMove(self.player, move)
        win_prob = val_net.win_prob(boardNext.toState(), player)
        if win_prob > bestMoveProb:
            bestMove = move
            bestMoveProb = win_prob
            return bestMove
        """
        
        # m = AlphaBeta(board, 3, player, val_net).run()
        #m.__maxValue( , , , )
        (v, move) = AlphaBeta(board, 3, player, val_net).run()
        return move

        #m = val_net.best_state(board.nextStates(player, moves), player, show_prob)
        return moves[m]
    elif pol_net != None and val_net == None:
        print ("not yet implemented")
        assert False
    else:
        assert val_net != None and pol_net != None
        print ("not yet implemented")
        
