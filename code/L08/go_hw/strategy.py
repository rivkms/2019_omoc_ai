from board import *
from CNN import *
    
#####################################
def selectMove(board, moves, player, val_net):
    assert len(moves) > 0 and val_net != None

    # WRITE YOUR OWN CODE HERE!!
    # Your strategy may be based on alpha-beta + value network
    #                               or MCTS + value network or ..

    
    # Replace the following code that is greedy w.r.t. value network
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
    m = val_net.best_state(board.nextStates(player, moves), player)
    return moves[m]

