from constant import *
from graphics import Canvas
import copy
import threading, time  # for mouse events
import numpy as np
import random

##################################################
class Board(object):
    def isEmpty(self, i,j): return self.cell[i][j] == EMPTY
    def stone(self, i,j): return self.cell[i][j]
    
    def __init__(self, state=None, canvas=None):
        self.cell = [ [EMPTY]*N  for i in range(N) ]
        self.ko = (None,None) # for Ko (pai) rule
        
        self.num_turn = 0
        self.canvas = canvas
        if state != None:  # only for debugging
            for i in range(N):
                for j in range(N):
                    count = 0
                    for k in range(3):
                        if state[i][j][k] == 1: count += 1
                    assert count == 1
                    for k in range(3):
                        if state[i][j][k] == 1: self.cell[i][j] = k

    def print_board(self):  # only for debugging
        s = ["B", "W", "."]  # ["0", "1", "."]
        for i in range(N):
            for j in range(N):
                print (s[self.stone(i,j)], end=" ")
            print ()
        print (self.ko)

    def toState(self):
        # S = [ [ [0]*3  for i in range(N) ]  for j in range(N) ]
        S = np.zeros((N,N,3), np.int)  # one-hot vector representation
        for i in range(N):
            for j in range(N):
                S[i][j][self.stone(i,j)] = 1
        return S

    def nextStates(self, player, moves):
        m = len(moves)
        S = np.zeros((m, N,N,3), np.int)
        for k in range(m):
            boardNext = self.copy()
            boardNext.setMove(player, moves[k])
            S[k] = boardNext.toState()
        return S

    def surroundedBy(self, player, i,j):
        D = [ (-1,0), (1,0), (0,-1), (0,1) ]
        for (di,dj) in D:
            p, q = i+di, j+dj
            if withinBoard(p,q) and self.stone(p,q) != player:
                return False
        return True
        
    def winner(self):
        # assert self.isEndingPos()
        D = [ (-1,0), (1,0), (0,-1), (0,1) ]
        score = [0,0]
        for i in range(N):
            for j in range(N):
                if self.isEmpty(i,j):
                    if self.surroundedBy(B, i,j): score[B] += 1
                    elif self.surroundedBy(W, i,j): score[W] += 1
                    
        if self.canvas: print ("[score-B/W]:", score[B], score[W])
        if score[B] > score[W]+3: return B
        else: return W  # 3.5-point compensation (Komi) for W

    def validMoves(self, player):
        L = []
        for i in range(N):
            for j in range(N):
                move = (i,j)
                if self.isValidMove(player, move):
                    L.append(move)
        random.shuffle(L)
        return L
                
    def isValidMove(self, player, move):
        if move == self.ko: return False  # violates Ko (pai) rule
        i,j = move
        if not self.isEmpty(i,j): return False

        b1 = self.copy()
        b1.cell[i][j] = player

        if len(b1.capturedBy(i,j)) >= 1:
            return True
            
        if len(b1.capturedFrom(i,j)) >= 1:
            return False  # suicide move
        
        # moving to player's single-size territory is prohibited unless
        # it prevents opponent from moving there to capture player's stones
        if b1.surroundedBy(player, i,j):
            b2 = b1.copy()
            b2.cell[i][j] = opponent(player)
            return len(b2.capturedBy(i,j)) >= 1
        else:
            return True
        
    def setMove(self, player, move):
        # self.isValidMove(player, move)
        # assert player in [B,W]
        i,j = move
        self.ko = (None,None)

        self.cell[i][j] = player
        stones = self.capturedBy(i,j)
        if len(stones) == 1:  # check Ko (pai)
            p,q = stones[0]  # opponent
            if len(self.capturedBy(p,q)) == 1:  # must be (i,j) set by player
                self.ko = (p,q)  # (p,q) is prohibited in the next turn
        for (p,q) in stones:
            self.cell[p][q] = EMPTY
            
        self.num_turn += 1
        if self.canvas != None:
            self.canvas.addStone(i,j, player, self.num_turn)
            if len(stones) > 0:
                time.sleep(0.5)
                for (p,q) in stones: self.canvas.removeStone(p,q)

    def capturedBy(self, i,j): # opponent's stones captured by player at (i,j)
        player = self.stone(i,j)
        opp = opponent(player)
        sN, sS, sW, sE = [], [], [], []
        if i>0   and self.stone(i-1,j) == opp: sN = self.capturedFrom(i-1,j)
        if i<N-1 and self.stone(i+1,j) == opp: sS = self.capturedFrom(i+1,j)
        if j>0   and self.stone(i,j-1) == opp: sW = self.capturedFrom(i,j-1)
        if j<N-1 and self.stone(i,j+1) == opp: sE = self.capturedFrom(i,j+1)
        return list(set(sN + sS + sW + sE))
        
    def capturedFrom(self, i,j):
        opp = self.stone(i,j)
        # player = opponent(opp)
        D = [ (-1,0), (1,0), (0,-1), (0,1) ]
        
        visited = [[False]*N  for k in range(N)]
        visited[i][j] = True
        stack = [(i,j)]  # for DFS
        stones = [(i,j)]
        regionCaptured = True
        while regionCaptured and len(stack) > 0:
            i,j = stack.pop()  # O(1) whereas pop(0) for BFS requires O(N)
            for (di,dj) in D:
                p, q = i+di, j+dj
                if withinBoard(p,q) and not visited[p][q]:
                    if self.isEmpty(p,q):
                        regionCaptured = False
                        break
                    elif self.stone(p,q) == opp:
                        visited[p][q] = True
                        stack.append((p,q))
                        stones.append((p,q))
        return (stones if regionCaptured else [])

    # create and return a new copy of this Board object
    def copy(self):
        b = Board()
        b.cell = copy.deepcopy(self.cell)
        b.ko = self.ko[:]
        return b

    # used by go_hw/test.py (to prevent deterministic result)
    def setTwoRandomMoves(self):
        i1, j1 = random.randrange(N), random.randrange(N)
        self.setMove(B, (i1,j1))
        while True:
            i2, j2 = random.randrange(N), random.randrange(N)
            if not (i1 == i2 and j1 == j2):
                break
        self.setMove(W, (i2,j2))
        
        