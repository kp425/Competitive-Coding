
# 10
# 4
# 11
# 6
# 2

m = 2
n = 2
N = 2
i = 0
j = 0

# m = 1
# n = 3
# N = 3
# i = 0
# j = 1

def is_valid(x,y,m,n):
    return 0<=x<m and 0<=y<n

def fp_rec(m,n,N,i,j):
    if N==0:
        return 0
    rgt = 1 if not is_valid(i,j+1,m,n) else fp_rec(m,n,N-1,i,j+1)
    lft = 1 if not is_valid(i,j-1,m,n) else fp_rec(m,n,N-1,i,j-1)
    up = 1 if not is_valid(i-1,j,m,n) else fp_rec(m,n,N-1,i-1,j)
    down = 1 if not is_valid(i+1,j,m,n) else fp_rec(m,n,N-1,i+1,j)
    return rgt+lft+up+down


def fp(m,n,N,i,j,memo):

    if N==0:
        return 0
    
    if memo[i][j]!= None:
        print(i,j)
        return memo[i][j]
    
    else:

        rgt = memo[i][j-1] if is_valid(i,j-1,m,n) else 0 or fp_rec(m,n,N-1,i,j-1)
        lft = memo[i][j+1] if is_valid(i,j-1,m,n) else 0 or fp_rec(m,n,N-1,i,j+1)
        up = memo[i-1][j] if is_valid(i,j-1,m,n) else 0 or fp_rec(m,n,N-1,i-1,j)
        dwn = memo[i+1][j] if is_valid(i,j-1,m,n) else 0 or fp_rec(m,n,N-1,i+1,j)
        memo[i][j] = rgt+lft+up+dwn
    
    return memo[i][j]
        

    

    
    
    memo[i][j-1] = 1



    
    if memo[N-1][i][j] == None:
        if not is_valid(i,j+1,m,n):
            memo[N-2][i][j+1] = 1
        else:
            memo[N-2][i][j+1] = fp_rec(m,n,N-1,i,j+1)

    return memo[N-1][i][j]


def sol(m,n,N,i,j):
    # memo = [[[None]*n for x in range(m)] for y in range(N)]
    memo = [[None]*n for x in range(m)]
    dirs = [(0,-1),(0,1),(1,0),(-1,0)]
    return fp(m,n,N,i,j,memo)

print(sol(m,n,N,i,j))








    





