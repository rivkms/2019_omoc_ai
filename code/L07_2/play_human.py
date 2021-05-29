from board import *
from tree_search_MCTS import MCTS
from tree_search_minimax import Minimax, AlphaBeta

humanPlayer, computerPlayer = B, W
# humanPlayer, computerPlayer = W, B

#####################################
def playHuman():
    canvas = Canvas()
    board = Board(canvas=canvas)
    maxStep = N*N*2
    player = B
    nStep = 0
    nNoMove = 0
    while nStep < maxStep: # similar to go(CNN)/play.py
        if board.noValidMoves(player):
            nNoMove += 1
            if nNoMove == 2: break
        else:
            nNoMove = 0
            if player == computerPlayer: 
                print ("Computer player searches..")
                # treeSearch = MCTS(board, player, nStep, maxStep, canvas)
                # treeSearch = Minimax(board, 2, player, canvas)
                treeSearch = AlphaBeta(board, 3, player, canvas)
                (v, move) = treeSearch.run()
                print ("Computer player selects", move[0]+1, move[1]+1, v)
            else:
                # i = raw_input("Enter row (1-%d): " %N)
                # j = raw_input("Enter column (1-%d): " %N)
                # i = int(i) if i in digit else 0
                # j = int(j) if j in digit else 0
                # move = (i-1,j-1)
                move = canvas.waitInput()
                if not board.isValidMove(player, move):
                    print ("Invalid move..")
                    continue
            board.setMove(player, move)
            nStep += 1
            
        player = opponent(player)

    winner = board.winner()
    canvas.setMessage("The winner is " + ["B","W"][winner])
        
###################################################    
playHuman()