from itertools import groupby


def insert():
    pass

# def remove(l,c):
#     [x for x in l if ]


def sol(board, hand):
    groups = groupby(board)
    result = [[label, sum(1 for _ in group)] for label, group in groups]


    return result




board = "WRRBBW"
hand = "RB"

board = "WWRRBBWW"
k = sol(board, hand)
print(k)

