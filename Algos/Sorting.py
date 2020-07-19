
def BubbleSort(l):
    count = 0
    while (True):
        count = 0
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp
                count+=1
        if(count == 0):
            return l

def SelectionSort(l):
    
    for i in range(0, len(l)):
        min_value = l[i]
        for j in range(i, len(l)):
            if (min_value > l[j]):
                min_value = l[j]
        temp = l[i]
        l[i] = min_value
        l[i+1] = temp
        
    return l
        



if __name__ == "__main__":

    l1 = [10, 3, 8, 6]
    l2 = [10, 3, 8, 6, 1, 3, 12]

    print(BubbleSort(l2))
    print(SelectionSort(l2))