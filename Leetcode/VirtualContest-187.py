maxChoosableInteger = 10
desiredTotal = 11

def sol(limit, total):
	if 0<total<=limit:
		return True
	nums = [i for i in range(limit)]
	memo = [None for i in range(limit)]
	return game(nums,total,memo)


def game(nums,total,memo,turn="0"):
	
	if total<=0:
		if turn == "0":
			return False
		return True
	
	if total>=0 and len(nums)==0:
		return False

	for i in range(len(nums)):
		if memo[i] == None:
			if turn == "0":
				turn = "1"
			else:
				turn = "0"
			memo[i] = game([nums[x] for x in range(len(nums)) if x!=i ],\
							total-nums[i],memo,turn)
		else:
			return memo[i]





print(sol(maxChoosableInteger,desiredTotal))
