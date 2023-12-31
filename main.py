board = [
    [0,0,8,0,0,4,0,0,2],
    [0,5,0,0,0,1,0,0,0],
    [7,0,0,2,5,0,0,3,0],
    [4,0,0,0,0,0,6,0,0],
    [0,6,0,5,3,0,0,0,8],
    [0,0,0,0,1,0,0,0,0],
    [0,0,9,0,0,0,0,7,0],
    [0,4,0,8,6,0,0,0,3],
    [0,0,0,0,0,2,0,0,0]
]

def solve(bd):

    find = find_empty(bd)

    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(bd, i, (row, col)):
            bd[row][col] = i

            if solve(bd):
                return True
            
            bd[row][col] = 0

    return False

def is_valid(bd, num, pos):

    # Check Row
    for i in range(len(bd[0])):
        if bd[pos[0]][i] == num and pos[1] != i:
            return False
        
    # Check Column
    for i in range(len(bd)):
        if bd[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3 X 3 Box
    box_x = pos[1] // 3
    box_y = pos[0] // 3


    for i in range(box_y* 3, box_y*3+3):
        for j in range(box_x* 3, box_x*3+3):
            if bd[i][j] == num and (i, j)!= pos:
                return False
            
    return True


def print_board(bd):
    for i in range(len(bd)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        
        for j in range(len(bd[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8:
                print(bd[i][j])
            
            else:
                print(str(bd[i][j])+ " ", end="")

def find_empty(bd):
    for i in range(len(bd)):
        for j in range(len(bd[0])):
            if bd[i][j] == 0:
                return (i , j)
    
    return None

print_board(board)
solve(board)
print("\n-------- Solved --------\n")
print_board(board)