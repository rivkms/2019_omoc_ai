def withinBoundary(height, width, i, j):
    return i>=0 and i<height and j>=0 and j<width

def countMines(mineField):
    # ADD ADDITIONAL CODE HERE!



def main():
    T = True
    F = False
    mineField = [
        [T, F, F, F, F, T],
        [F, F, F, F, F, T],
        [T, T, F, T, F, T],
        [T, F, F, F, F, F],
        [F, F, T, F, F, F],
        [F, F, F, F, F, F]
    ]

    mines = countMines(mineField)

    for i in range(len(mines)):
        print(mines[i])
    
main()
  # [1, 1, 0, 0, 2, 2]
  # [3, 3, 2, 1, 4, 3]
  # [3, 3, 2, 1, 3, 2]
  # [3, 4, 3, 2, 2, 1]
  # [1, 2, 1, 1, 0, 0]
  # [0, 1, 1, 1, 0, 0]

