import math

def __binary_search_recursion(l, value, low, high):

    if(high<low):
        return False

    middle = int((high+low)/2)

    if(value == l[middle]):
        return middle

    if(value < l[middle]):
        return __binary_search_recursion(l ,value, low, middle-1)
    elif(value > l[middle]):
        return __binary_search_recursion(l ,value, middle+1, high)
    
    

def binary_search_recursion(l, target):
    return __binary_search_recursion(l, target, 0, len(l)-1)



def __ternary_search_recursion(l, target, left, right):

    if(left > right):
        return False

    partition_size = int((right-left)/3)
    mid1 = left + partition_size
    mid2 = right - partition_size

    if(target == l[mid1]):
        return mid1
    elif (target == l[mid2]):
        return mid2

    if (target < l[mid1]):
        return __ternary_search_recursion(l, target, left, mid1-1)

    elif(target > l[mid2]):
        return __ternary_search_recursion(l, target, mid2+1, right)

    elif (l[mid1] < target <l[mid2]):
        return __ternary_search_recursion(l, target, mid1+1, mid2-1)

    

def ternary_search_recursion(l, target):
    return __ternary_search_recursion(l, target, 0, len(l)-1)


def jump_search(l, target):
    block_size = int(math.sqrt(len(l)))
    count = 0
    while(True):   
        current = count * block_size
        next_ = (count+1) * block_size

        if(target > l[next_]):
            count+=1
        elif(target == l[next_]):
            return next_
        else:
            for i in range(current, next_+1):
                if(l[i] == target):
                    return i
            
            return -1

def exponential_search(l, target):
    bound = 1
    while( bound< len(l) and l[bound] < target):
        bound*=2
    return __binary_search_recursion(l, target, int(bound/2), min(bound, len(l)-1))



if __name__ == "__main__":

    l = [3,5,6,9,11,20,25,30,21,18]

    l1 = [10,20,30,40,50]

   # print(ternary_search_recursion(l1, 50))

    print(exponential_search([1,20], 20))


