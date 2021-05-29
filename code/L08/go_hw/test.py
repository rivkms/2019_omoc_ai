from board import *
from CNN import *
import random
import numpy as np
from strategy import selectMove

#####################################
def test_yours():
    random.seed(0)
    nGames = 500 # 1000
    valB = CNN_Test("val_net_B_" + str(val_net_B_gen))
    valW = CNN_Test("val_net_W_" + str(val_net_W_gen))
    
    if SHOW_GRAPHICS: canvas = Canvas()
    maxStep = N*N*2
    numWins = [0,0]

    for ng in range(nGames):
        if SHOW_GRAPHICS: 
            board = Board(canvas=canvas)
        else:
            board = Board()

        yours = B if ng%2 == 0 else W
        board.setTwoRandomMoves()
        player = B
        nNoMove = 0
        nStep = 0
        while nStep < maxStep:
            moves = board.validMoves(player)
            if len(moves) == 0:
                nNoMove += 1
                if nNoMove == 2: break
            else:
                nNoMove = 0
                val = valB if player == B else valW
                if player == yours:
                    move = selectMove(board, moves, player, val) # your strategy
                else: # greedy w.r.t. value network
                    m = val.best_state(board.nextStates(player, moves), player)
                    move = moves[m]  
                board.setMove(player, move)
                nStep += 1
                
            player = opponent(player)

        if board.winner() == yours: numWins[yours] += 1
        if SHOW_GRAPHICS: canvas.clear()
        print ("Game %d: you %s" %(ng+1, ["lose","win"][board.winner()==yours]))

    print ("Winning rate of your Black:", numWins[B]/(nGames/2.0))
    print ("Winning rate of your White:", numWins[W]/(nGames/2.0))
    print ("Overall winning rate:", sum(numWins)/float(nGames))
        
#####################################
test_yours()
