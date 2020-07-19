def isValid(string):
    count = 0
    for i in range(len(string)):
        if string[i]=="(": 
            count+=1
        elif string[i]==")":
            count-=1
            if count < 0:
                return False
    return count == 0

s = "()())()"

# s = "(a)())()"

# s = ")("

l = []

for i in range(1,len(s)+1):
    print(s[:i])
    l.append(isValid(s[:i]))

print(set(s))


