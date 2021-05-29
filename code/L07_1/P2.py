def canWin(k, n):
    # IMPLEMENT HERE!


###########################################    
def main():
    inputs = [
        (10,100), (11,100), (12,100), (13,100), (50,100), (99,100),
        (124,10000000), (452,10000000), (7051,10000000), (40297,10000000),
        (170029,10000000), (605018,10000000), (2189729,10000000) 
    ]
    outputs = [
        False, False, True, True, True, True,
        False, True, True, False, True, False, True
    ]
    
    correct = True
    for i in range(len(inputs)):
        result = canWin(inputs[i][0], inputs[i][1])
        if result != outputs[i]:
            print ("Incorrect output for" , str(i+1)+"-th input")
            correct = False
    if correct:
        print ("Correct for all inputs")

main()