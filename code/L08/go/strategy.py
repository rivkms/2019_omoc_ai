from board import *
from CNN import *
    
#####################################
def selectMove(board, moves, player, val_net, pol_net=None, show_prob=False):
    assert len(moves) > 0
    if val_net != None and pol_net == None:
        """
        bestMove = None
        bestMoveProb = 0
        for move in moves:
            boardNext = board.copy()
            boardNext.setMove(player, move)
            win_prob = val_net.win_prob(boardNext.toState(), player)
            if win_prob > bestMoveProb:
                bestMove = move
                bestMoveProb = win_prob
        return bestMove
        """
        m = val_net.best_state(board.nextStates(player, moves), player, show_prob)
        return moves[m]
    elif pol_net != None and val_net == None:
        print ("not yet implemented")
        assert False
    else:
        assert val_net != None and pol_net != None
        print ("not yet implemented")
        
