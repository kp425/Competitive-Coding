
nums = [3, 4, 2]
# nums = [2, 2, 3, 3, 3, 4]

def de(nums,index):
    if nums == [0]*len(nums): return 0
    item = nums[index]
    nums[index] = 0
    for i in range(len(nums)):
        if nums[i]==item-1 or nums[i]==item+1:
            nums[i]=0
    no_zeros = nums.count(0)
    return item+de(sorted(nums),no_zeros)

def sol(nums):
    if nums == []:
        return 0
    m = []
    for i in range(len(nums)):
        temp = list(nums)
        m.append(de(temp,i))
    return max(m)
    # return max([de(nums,i) for i in range(len(nums))])

# print(de(nums,1))

print(sol(nums))

