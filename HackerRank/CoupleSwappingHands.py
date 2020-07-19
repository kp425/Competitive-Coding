
# l = [0, 2, 1, 3]



l = [10, 1, 4, 5, 3, 6, 8, 7, 9, 2]

for i in range(0,len(l),2):
    if l[i]==i or l[i]==i+1:
        l[i] = {l[i]:True}
    else:
        l[i] = {l[i]:False}
    
    if l[i+1]==i or l[i+1]==i+1:
        l[i+1] = {l[i+1]:True}
    else:
        l[i+1] = {l[i+1]:False}

for i in l:
    print(i)
    

# l1 = [l[i] for i in range(0,len(l),2)]
# l2 = [l[i] for i in range(1,len(l),2)]
# print(l1)
# print(l2)