
digits=[8,1,9]
# digits = [8,6,7,1,0]
# digits = [0,0,0,0,0,0]
# digits = [1]
digits = [5,8]

def lm(digits):
    set_ = []
    sum_ = 0
    for i in digits:
        if i not in set_:
            set_.append(i)
        sum_+=i

    temp = sum_    
    if temp%3 != 0:
        for i in sorted(set_):
            if (temp-i)%3 == 0:
                digits.remove(i)
                break
    _ = "".join(map(str,sorted(digits,reverse=True)))
    if _!="":
        return str(int(_))
    return _

print(lm(digits))