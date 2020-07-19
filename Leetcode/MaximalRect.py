matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]


def mr(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    max_ = 0
    height = [[0]*cols for i in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "1":
                if i-1>=0:
                    if height[i-1][j]>0:
                        height[i][j] = 1+height[i-1][j]
                    else:
                        height[i][j] = 1
                else:
                    height[i][j] = 1

                if j-1>=0:
                    matrix[i][j] = (int(matrix[i][j])+matrix[i][j-1])
                    # matrix[i][j] = (int(matrix[i][j])+matrix[i][j-1])*height[i][j]
                else:
                    matrix[i][j] = 1
                    # matrix[i][j] = 1*height[i][j]
            else:
                matrix[i][j] = 0
        _ = max(matrix[i])
        if _>max_:
            max_ = _
    
    print(height)
    print(matrix)
    

mr(matrix)
