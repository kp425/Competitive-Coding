
def is_valid(matrix,m,n):
    return 0<=m<len(matrix) and 0<=n<=len(matrix[0])

def ms(matrix,m,n):

    if m<0 and n<0:
        return 0
    if is_valid(matrix,m,n):
        return matrix[m][n]+ max(ms(matrix,m,n-1),\
                    ms(matrix,m-1,n-1),ms(matrix,m-1,n))


mat = [[500, 100, 230],
        [1000, 300, 100],
        [200, 1000, 200]]

# mat = [[100, -350, -200],
#            [-100, -300, 700]]



def ms_(matrix,m,n):
    global cache
    if m<0 and n<0:
        return 0
    if cache[m][n] != None:
        print('used')
        return cache[m][n]
    if is_valid(matrix,m,n):
        cache[m][n-1]   = ms_(matrix,m,n-1)
        cache[m-1][n-1] = ms_(matrix,m-1,n-1)
        cache[m-1][n]   = ms_(matrix,m-1,n)
         
        return  matrix[m][n] + max(cache[m][n-1],cache[m-1][n-1],cache[m-1][n])

from random import randint

mat = [[randint(-100,100) for i in range(10)] for j in range(10)]
mat = [[500, 100, 230],
        [1000, 300, 100],
        [200, 1000, 200]]
cache =  [[None]*len(mat[0])]*len(mat)


# print(ms(mat,len(mat)-1,len(mat[0])-1))

print(ms_(mat,len(mat)-1,len(mat[0])-1))

for i in cache:
    print(i)

   