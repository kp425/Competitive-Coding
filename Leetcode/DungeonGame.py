
grid =[[-2,-3,3],
        [-5,-10,1],
        [10,30,-5]]

def is_valid(grid,i,j):
    return 0<=i<len(grid) and 0<=j<len(grid[0])

def dg(grid):

    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):   
            if i==0 and j==0:continue
            if is_valid(grid,i,j-1):


            a = grid[i][j-1] if is_valid(grid,i,j-1) else -1*float("inf")
            b = grid[i-1][j] if is_valid(grid,i-1,j) else -1*float("inf")
            grid[i][j] += max(a,b)
            
               
    print(grid)

dg(grid)

