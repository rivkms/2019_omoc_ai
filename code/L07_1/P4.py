def f(L):
    n = len(L)
    if n == 1: return L[0]

    # IMPLEMENT HERE!

    
##########################################################
import random

def test():
    n = 18
    # outputs = [104, 97, 104, 87, 85, 94, 102, 69, 79, 69]  # for python2 rand
    outputs = [97, 95, 82, 101, 76, 96, 76, 81, 100, 101]
    correct = True
    for i in range(len(outputs)):
        random.seed(i)
        L = [random.randrange(1,n) for j in range(n)]
        result = f(L)
        if result != outputs[i]:
            print ("Incorrect output for" , str(i+1)+"-th input", result)
            correct = False
    if correct:
        print ("Correct for all inputs")

test()