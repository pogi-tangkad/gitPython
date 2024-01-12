
# Functon to check the rows using floor division to determine row number and increment by 1
def row_Check(puzzle, n):
    row_num = (n//9) * 9
    for i in range(row_num, (row_num + 9)):
        if i == n:
            continue
        elif puzzle[n] == puzzle[i]:
            return False
    return True

# Functon to check the colums using modulus to determine increments
def col_Check(puzzle, n):
    col_num = n%9
    for i in range(0,9):
        if col_num == n:
            col_num += 9
            continue
        elif puzzle[n] == puzzle[col_num]:
            return False
        else:
            col_num += 9
    i # sweeping pylint errors under the rug
    return True

# Function to check the 3x3 section containing [n]. I had given up trying to find some
# clever correlation between the 0-80 [n] places and 3x3 sections in a 9x9 grid.
def box_Check(puzzle, n):
    col_num = n%9
    row_num = n//9
    if row_num < 3 and col_num < 3:
        start = 0
    elif row_num < 3 and col_num < 6:
        start = 3
    elif row_num < 3:
        start = 6
    elif row_num < 6 and col_num < 3:
        start = 27
    elif row_num < 6 and col_num < 6:
        start = 30
    elif row_num < 6:
        start = 33
    elif col_num < 3:
        start = 54
    elif col_num < 6:
        start = 57
    else:
        start = 60
    for x in range(0,3):
        for y in range(0,3):
            if n == start:
                start += 1
                continue
            elif puzzle[n] == puzzle[start]:
                return False
            else:
                start += 1
        start += 6
    x,y # sweeping pylint errors under the rug
    return True

# Function for solving 9x9 Sudoku puzzle (my nightmare)
# puzzle = the 81 character string passed in
# n = the current position in the puzzle string
# lap = a counter for determining sequential defaults
#       99 is given for non-default(zero) positions as even
#       a fully default puzzle can only have a lap of 81
def small_Brute(puzzle, n=0, lap=1):
    if n == 81:         # Checks if we are at the end of the puzzle
        return puzzle
    if puzzle[n] != '0' and lap < 99:       # Check if [n] location is a default value
        puzzle = small_Brute(puzzle, (n + 1), (lap + 1))    # Laps keep track of sequential defualts
        if n < 80:                          
            if puzzle[n+1] == '0':          # Checks if next value is fully failed and uses lap
                puzzle = small_Brute(puzzle, n-lap, 99)     # to backtrack to the latest
        return puzzle                                       # non-default value
    else:
        next_val = chr(ord(puzzle[n]) + 1)      # Increments the [n] value for non default values
        if next_val == ':':         # Checks if 1-9 (chr) have been tested already
            puzzle = puzzle[:n] + '0' + puzzle[(n + 1):]        # Resets [n] value and backtracks
            return puzzle
        puzzle = puzzle[:n] + next_val + puzzle[(n + 1):]       # Rebuilds puzzle with next_val
        #print(n, puzzle)
        if row_Check(puzzle, n) and col_Check(puzzle, n) and box_Check(puzzle, n):
            puzzle = small_Brute(puzzle, (n + 1))       # If no conflicts, continues to next box
            if n < 80:                          # Same as above
                if puzzle[n+1] == '0':      # The '0' check indicates the full failure of [n+1]
                    puzzle = small_Brute(puzzle, n, 99)
        else:
            puzzle = small_Brute(puzzle, n, 99)
    return puzzle


if (__name__ == '__main__'):

    # solved = small_Brute('000000960706008400809010002004007000100940805008030104003000609000803500501020080')

    sudoku = input("Enter 81 digit puzzle using 0 (zero) for empty boxes: ")
    solved = small_Brute(sudoku)
    print(solved)
    for check in solved:
        if check == '0':
            print('Unsolvable')
            break
        else:
            grid = []
            line = []
            x = 0
            for row in range(0,9):
                for col in range(x, x + 9):
                    line.append(solved[col])
                x += 9
                grid.append(line)
                line = []
            for row in grid:
                print(end='| ')
                for val in row:
                    print(val, end=' | ')
                print('\n-------------------------------------')
            break