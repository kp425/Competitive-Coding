heights = [2,1,5,6,2,3]

# heights = [1,1]

def sol(heights):
    max_ = 0
    for i in range(len(heights)):
        for j in range(i,len(heights)):
            if i==j:
                area = heights[i]*1
            else:
                _ = heights[i:j+1]
                width = len(_)
                area = min(_)*width
            if area>max_:
                max_ = area
    return max_

print(sol(heights))
        