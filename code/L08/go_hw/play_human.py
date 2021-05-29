import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import sys
from constant import *
from board import *
from CNN import *
from strategy import selectMove

humanPlayer, yours = B, W
# humanPlayer, yours = W, B

#####################################
def playHuman():
    if yours == B:
        val = CNN_Test("val_net_B_" + str(val_net_B_gen))
    else:
        val = CNN_Test("val_net_W_" + str(val_net_W_gen))
    
    canvas = Canvas()
    board = Board(canvas=canvas)
    maxStep = N*N*2
    player = B
    nStep = 0
    nNoMove = 0
    while nStep < maxStep: # similar to go(CNN)/play.py
        moves = board.validMoves(player)
        if len(moves) == 0:
            nNoMove += 1
            if nNoMove == 2: break
        else:
            nNoMove = 0
            if player == yours:
                move = selectMove(board, moves, player, val) # your strategy
            else:
                move = canvas.waitInput()
                if move not in moves:
                    print ("Invalid move")
                    continue
            board.setMove(player, move)
            nStep += 1

        player = opponent(player)

    winner = board.winner()
    canvas.setMessage("The winner is " + ["B","W"][winner])
    
###################################################    
playHuman()