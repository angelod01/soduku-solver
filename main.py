# Ramos, Angelo
board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

def solve(brd):
    find = is_empty(brd)
    if find == None:
        return True #no cells empty
    else:
        row, col = find
    
    for i in range(1,10):
        if is_valid(brd, i, (row,col)): #checks validity of adding
            brd[row][col] = i 

            if solve(brd): #recursively call solve after adding previous val
                return True 
            brd[row][col] = 0 #resets cell if recursive calls end up not working
            
    return False
        

def is_valid(brd, num, pos): # pos -> row, col
    row, col = pos

    #check row
    if num in brd[row]:
        return False
    #check col
    for i in range(len(brd)): #iterate through each row
        if num in [brd[i][col] for i in range(len(brd))]: #check if num is in col
            return False
    #check subgrid
    box_row, box_col = row // 3, col // 3 #use int division to get position of the current subgrid
    for i in range(box_row*3, box_row*3+3): #iterates through x vals in subgrid
        for j in range(box_col*3, box_col*3+3): #iterates through y in subgrid
            if brd[i][j] == num and (i,j) != pos:
                return False

    return True #all checks pass



def print_layout(brd):
    for i, row in enumerate(brd):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j, val in enumerate(row):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(val) #adds the endline
            else:
                print(str(val) + " ", end="")


def is_empty(brd):
    for i in range(len(brd)):
        for j in range (len(brd[0])):
            if brd[i][j] == 0:
                return (i,j) # row num, col num
    return None

print("\n Board before solving: \n")
print_layout(board)
solve(board)
print("\n Board after solving: \n\n")
print_layout(board)
