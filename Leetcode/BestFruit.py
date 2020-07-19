

no_fruits = 3
no_judges = 3
fav_fruits = [[1,2,3],[2,3,1]]

no_fruits = 4
no_judges = 5
fav_fruits = [[1,2,3,4],[1,2,3,4],[2,4,3,1],[3,4,2,1],[4,3,2,1]]

no_fruits = 2
no_judges = 1
fav_fruits = [[2,1]]

no_fruits = 10
no_judges = 10
l = list(range(1,11))
fav_fruits =  [l[i:]+l[:i] for i in range(0,10)]

for i in fav_fruits:
    print(i)

fruits = {}

#init fruits dict   
for i in range(1,no_fruits+1):
    fruits[i] = 0




def sol(no_fruits, fav_fruits):

    global fruits

    #counting votes
    for i in fav_fruits:
        fruits[i[0]]+=1

    #finding the worst fruit
    to_remove = min([key for key in fruits if fruits[key] == min(fruits.values())])
    print(to_remove)

    #Removing the worst fruit
    fruits.pop(to_remove,None)
    for i in fav_fruits:
        i.remove(to_remove)

    #refresh dict
    for i in fruits.keys():
        fruits[i] = 0
    
    print(fruits)
    print(fav_fruits)
    return fav_fruits


for i in range(no_judges):
    fav_fruits = sol(no_fruits, fav_fruits)
    print("\n")

# fav_fruits = sol(3, fav_fruits)

