def canWin(k, n):
    # IMPLEMENT HERE!


def P3_CanWin(n):
    assert n > 5
    return not canWin(1, n)  # start from B

##################################################################    
def main():
    inputs = [ 44, 45, 46, 148, 149, 150 ]
    outputs = [ False, True, True, True, True, False ]
    
    correct = True
    for i in range(len(inputs)):
        result = P3_CanWin(inputs[i])
        if result != outputs[i]:
            print ("Incorrect output for" , str(i+1)+"-th input")
            correct = False
    if correct:
        print ("Correct for all inputs")

main()
