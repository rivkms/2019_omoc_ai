import random
from board import *
from tree_search_MCTS import MCTS
from tree_search_minimax import Minimax, AlphaBeta

#####################################
def playAuto(nGame):
    canvas = Canvas()
    maxStep = N*N*2
    for g in range(nGame):
        random.seed(g)  # make deterministic for DEBUG
        canvas.clear()
        board = Board(canvas=canvas)
        player = B
        nStep = 0
        nNoMove = 0
        while nStep < maxStep: # similar to go(CNN)/play.py
            if board.noValidMoves(player):
                nNoMove += 1
                if nNoMove == 2: break
            else:
                nNoMove = 0
                print ("[Game %d] %s searches.." %(g, ["black","white"][player]))
                # treeSearch = MCTS(board, player, nStep, maxStep, canvas)
                treeSearch = AlphaBeta(board, 4, player, canvas)
                # treeSearch = Minimax(board, 2, player, canvas)
                (v, move) = treeSearch.run()
                print ("[Game %d] %s selects" \
                    %(g, ["black","white"][player]), move[0]+1, move[1]+1, v)
                board.setMove(player, move)
                nStep += 1

            player = opponent(player)

        winner = board.winner()
        canvas.setMessage("The winner is " + ["B","W"][winner])
        time.sleep(2)
    
        
###################################################    
playAuto(1000)