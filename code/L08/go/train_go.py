import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'  # disable TF logging
import numpy as np
from constant import *
from board import Board
from CNN import CNN_Train
from play_for_data import playGames

#####################################
def genSymmetry(S, W):
    # original, horizontal flip, vertical flip, both flips
    # 90 deg rotation for each of the above reflections
    nGames, Nr, Nc, _ = S.shape
    assert Nr == Nc == N
    S8 = np.zeros((nGames*8, N,N,3), np.int)
    W8 = np.zeros(nGames*8, np.int)  # winner for each state

    S8[:nGames] = S
    S8[nGames:2*nGames] = S[:, ::-1, :, :]
    S8[2*nGames:3*nGames] = S[:, :, ::-1, :]
    S8[3*nGames:4*nGames] = S[:, ::-1, ::-1, :]
    R = np.rollaxis(S, 2, 1)
    S8[4*nGames:5*nGames] = R
    S8[5*nGames:6*nGames] = R[:, ::-1, :, :]
    S8[6*nGames:7*nGames] = R[:, :, ::-1, :]
    S8[7*nGames:8*nGames] = R[:, ::-1, ::-1, :]

    for k in range(8): W8[k*nGames:(k+1)*nGames] = W

    return S8, W8
        
#####################################
def train():
    val_net_B = [None]*(nGen+1)
    val_net_W = [None]*(nGen+1)
    
    # 1st generation
    nTrain_1st = int(nTrain/2.5)
    rand1 = np.ones(nTrain_1st)
    SB, WB, SW, WW, P = playGames(nTrain_1st, None, None, rand1, None, None, rand1)
    print ("[Train/Gen-1] win prob.", P[0], "/", P[1])
    SB, WB = genSymmetry(SB, WB)
    val_net_B[1] = CNN_Train(SB, WB, "val_net_B_1")
    SW, WW = genSymmetry(SW, WW)
    val_net_W[1] = CNN_Train(SW, WW, "val_net_W_1")

    # generations from 2 to nGen
    for g in range(2,nGen+1):
        randB = np.random.rand(nTrain)
        randW = np.random.rand(nTrain)
        m = N*N//2
        for i in range(nTrain):
            if np.random.rand() < 0.5: randB[i] = np.random.randint(-m,0)
            if np.random.rand() < 0.5: randW[i] = np.random.randint(-m,0)
        SB, WB, SW, WW, P = playGames(nTrain, val_net_B[g-1], None, randB, \
                                      val_net_W[g-1], None, randW)
        print ("[Train/Gen-%d] win prob." %g, P[0], "/", P[1])
        SB, WB = genSymmetry(SB, WB)
        val_net_B[g] = CNN_Train(SB, WB, "val_net_B_" + str(g))
        SW, WW = genSymmetry(SW, WW)
        val_net_W[g] = CNN_Train(SW, WW, "val_net_W_" + str(g))

#####################################
"""        
def trainFrom(genFr, genTo):
    assert genFrom >= 1
    val_net_B = [None]*(genTo+1)
    val_net_W = [None]*(genTo+1)

    val_net_B[genFr] = CNN_Test("val_net_B_" + str(genFr))
    val_net_W[genFr] = CNN_Test("val_net_W_" + str(genFr))
    
    for g in range(genFr+1,genTo+1):
        randB = np.random.rand(nTrain)
        randW = np.random.rand(nTrain)
        m = N*N//2
        for i in range(nTrain):
            if np.random.rand() < 0.5: randB[i] = np.random.randint(-m,0)
            if np.random.rand() < 0.5: randW[i] = np.random.randint(-m,0)
        SB, WB, SW, WW, P = playGames(nTrain, val_net_B[g-1], None, randB, \
                                      val_net_W[g-1], None, randW)
        print ("[Train/Gen-%d] win prob." %g, P[0], "/", P[1])
        SB, WB = genSymmetry(SB, WB)
        val_net_B[g] = CNN_Train(SB, WB, "val_net_B_" + str(g))
        SW, WW = genSymmetry(SW, WW)
        val_net_W[g] = CNN_Train(SW, WW, "val_net_W_" + str(g))
"""        
#####################################
train()
# trainFrom(10,20)