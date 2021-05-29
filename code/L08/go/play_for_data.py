from board import *
from CNN import *
import random
import numpy as np
from strategy import selectMove

#####################################
def playGames(nGames, valB, polB, randB, valW, polW, randW, initRandomTwo=False):
    # valB/valW: value network for B/W (black/white)
    # polB/polW: policy network for B/W (currently, not used)
    # randB/randW: randomness of B/W
    
    if SHOW_GRAPHICS: canvas = Canvas()
    maxStep = N*N*2
    maxStates = maxStep * nGames
    S = np.zeros((maxStates, N,N,3), np.int)
    WI = np.zeros(maxStates, np.int)  # winner for each state
    turn = np.zeros(maxStates, np.int)
    win_prob = np.zeros(3, np.float)
    
    nState = 0
    for ng in range(nGames):
        if SHOW_GRAPHICS: 
            board = Board(canvas=canvas)
        else:
            board = Board()
            
        if initRandomTwo: # used for testing trained vs. trained
            i1, j1 = random.randrange(N), random.randrange(N)
            board.setMove(B, (i1,j1))
            while True:
                i2, j2 = random.randrange(N), random.randrange(N)
                if not (i1 == i2 and j1 == j2):
                    break
            board.setMove(W, (i2,j2))
            
        nStep = 0
        player = B
        nNoMove = 0
        while nStep < maxStep:  # not board.isEndingPos():
            moves = board.validMoves(player)
            if len(moves) == 0:
                nNoMove += 1
                if nNoMove == 2: break
            else:
                nNoMove = 0
                if player == B:
                    val, pol, rand = valB, polB, randB
                else: # player == W
                    val, pol, rand = valW, polW, randW

                if (rand[ng] < 0 and nStep//2 < -rand[ng]) or \
                   (np.random.rand() <= rand[ng]):
                    move = random.choice(moves)
                else:
                    assert val != None or pol != None
                    move = selectMove(board, moves, player, val, pol)
                    
                board.setMove(player, move)
                # print ("Game %d, Step %d" % (ng, nStep))
                
                S[nState] = board.toState()
                turn[nState] = player
                nState += 1
                nStep += 1
                
            player = opponent(player)

        WI[nState-nStep:nState] = board.winner()
        win_prob[board.winner()] += 1
        if SHOW_GRAPHICS: canvas.clear()

    assert nState <= maxStates
    S, WI, turn = S[:nState], WI[:nState], turn[:nState]
    IB = np.where(turn == B)
    IW = np.where(turn == W)
    return S[IB], WI[IB], S[IW], WI[IW], win_prob/nGames #, float(nState)/nGames
