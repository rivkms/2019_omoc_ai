import sys

def solve(L):
    n = len(L)
    D = [[None]*n for i in range(n)]
    S = [[0]*n for i in range(n)]
    for i in range(n):
        S[i][i] = L[i]
        for j in range(i+1,n):
            S[i][j] = S[i][j-1] + L[j]
    
    for i in range(n):
        D[i][i] = L[i]

    # IMPLEMENT HERE

            
    return D[0][n-1]

# sample input
print (solve([1,2,5,2]))  # 6
print (solve([1,1,1,1,2,2,2,2,2]))  # 8

##########################################################
import random

def test():
    n = 1000
    # outputs = [253118, 260041, 252944, 255138, 257680, \
    #            249488, 247168, 243882, 256308, 243734]  # for python2 random
    outputs = [257054, 259492, 261726, 260375, 260791, \
               253454, 255732, 252039, 255075, 253121]
    correct = True
    for i in range(len(outputs)):
        random.seed(i)
        L = [random.randrange(1,n) for j in range(n)]
        result = solve(L)
        if result != outputs[i]:
            print ("Incorrect output for" , str(i+1)+"-th input")
            correct = False
    if correct:
        print ("Correct for all inputs")

test()