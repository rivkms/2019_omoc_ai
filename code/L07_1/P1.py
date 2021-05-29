def AcanWin(state):
    # IMPLEMENT HERE!

def BcanWin(state):
    # IMPLEMENT HERE!


###########################################    
def test():
    inputs = range(1,33)
    outputs = [
        True, True, True, True, True, True, False, False, True, 
        True, True, True, True, True, False, False, True, True,
        True, True, True, True, False, False, True, True, True, 
        True, True, True, False, False
    ]
    correct = True
    for i in range(len(inputs)):
        result = AcanWin(inputs[i])
        if result != outputs[i]:
            print ("Incorrect output for input ", inputs[i])
            correct = False
    if correct:
        print ("Correct for all inputs")

test()
