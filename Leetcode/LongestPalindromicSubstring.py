
def longest_p(string,i,j,l):

	if string!="" and string not in l:
		if string == string[::-1]:
			l.append(string)
		if j == len(string):
			j = 0
			i += 1
		longest_p(string[i:j+1],i,j+1,l)
		
	return l
	# if l == []:
	#     return ""
	# return max(l,key=len)



string = "babad"
# string = "cbbd"
# string = ""
# string = "babaddtattarrattatddetartrateedredividerb"

m = longest_p(string,0,0,[])



print(m)